//! Experiment using the actual standalone Splash VM and capability boundary.
//! Fixture benchmarks and bounded live weather/news adapters share the executor.
mod live_news;
mod news_digest;
mod news_query;

use futures::{stream::FuturesUnordered, StreamExt};
use serde_json::{json, Value};
use octoscript_capabilities::{
    CapabilityModule, CapabilityRuntime, JsonToolContract, ToolError, ToolMetadata, ToolPolicy,
};
use octoscript_core::ExecutionLimits;
#[cfg(test)]
use octoscript_schema::JsonSchema;
use std::{
    collections::BTreeMap,
    time::{Duration, Instant},
};

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

#[derive(Clone)]
struct Case {
    name: String,
    source: String,
    input: Value,
    tools: Vec<Value>,
}

fn cases() -> Vec<Case> {
    serde_json::from_str::<Vec<Value>>(include_str!("../fixtures.json"))
        .unwrap()
        .into_iter()
        .map(|v| {
            let name = v["name"].as_str().unwrap().to_owned();
            let source = match name.as_str() {
                "weather" => include_str!("../templates/weather.splash"),
                "stock" => include_str!("../templates/stock.splash"),
                "news" => include_str!("../templates/news.splash"),
                _ => unreachable!(),
            }
            .to_owned();
            Case {
                name,
                source,
                input: v["input"].clone(),
                tools: v["tools"].as_array().unwrap().clone(),
            }
        })
        .collect()
}

// Fixture-derived structural contracts keep this experiment small. Production
// uses the admitted UI contract and adapter-owned semantic schemas instead.
fn schema(value: &Value) -> Value {
    match value {
        Value::Object(fields) => json!({"type":"object", "additionalProperties":false,
            "required":fields.keys().collect::<Vec<_>>(),
            "properties":fields.iter().map(|(k,v)| (k.clone(),schema(v))).collect::<BTreeMap<_,_>>() }),
        Value::Array(items) => json!({"type":"array","maxItems":3,
            "items":items.first().map(schema).unwrap_or(json!({"type":"object"}))}),
        Value::String(_) => json!({"type":"string","minLength":1,"maxLength":1024}),
        Value::Number(_) => json!({"type":"number"}),
        Value::Bool(_) => json!({"type":"boolean"}),
        Value::Null => json!({"type":"null"}),
    }
}

fn runtime(case: &Case) -> Result<CapabilityRuntime> {
    runtime_with_live_news(case, false)
}

fn runtime_with_live_news(case: &Case, live_news: bool) -> Result<CapabilityRuntime> {
    // Pending records include settled promises; this is separate from active I/O.
    let mut runtime = CapabilityRuntime::with_limits_and_pending(ExecutionLimits::default(), 8)?;
    let mut module = CapabilityModule::new(
        "research",
        "Experiment: reviewed read-only research adapters",
    );
    let mut grouped = BTreeMap::<String, Vec<&Value>>::new();
    for tool in &case.tools {
        grouped
            .entry(tool["method"].as_str().unwrap().to_owned())
            .or_default()
            .push(tool);
    }
    for (method, fixtures) in grouped {
        let name = format!("research.{method}");
        let mut policy = ToolPolicy::json(&name);
        policy.max_calls = fixtures.len();
        policy.max_input_bytes = 2048;
        policy.max_output_bytes = 16384;
        policy.max_deferred_duration = Some(Duration::from_secs(5));
        runtime.register_validated_external_json_tool(
            policy,
            ToolMetadata::new("Bounded experiment adapter"),
            JsonToolContract::new(
                schema(&fixtures[0]["input"]),
                schema(&fixtures[0]["output"]),
            )?,
        )?;
        module = module.with_deferred_method(method, name);
    }
    if live_news {
        module = live_news::register(&mut runtime, module, case)?;
    } else if case.name == "news-digest" {
        module = news_digest::register(&mut runtime, module, case)?;
    }
    runtime.register_capability_module(module)?;
    runtime.set_json_global("request", &case.input, 4096, 8)?;
    Ok(runtime)
}

#[derive(Default, Clone)]
struct Fault {
    method: Option<String>,
    invalid_output: bool,
    deadline_ms: Option<u64>,
    cancel_ms: Option<u64>,
}

#[cfg(test)]
async fn run(case: &Case, concurrency: usize, fault: Fault) -> Result<Value> {
    execute(case, concurrency, fault, None).await
}

// Optional real read-only adapter. The host fixes origin, path, fields, method,
// redirects, timeout and response size; Splash supplies only coordinates.
async fn open_meteo(
    client: &reqwest::Client,
    method: &str,
    input: &Value,
) -> std::result::Result<String, ToolError> {
    async fn fetch(client: &reqwest::Client, method: &str, input: &Value) -> Result<String> {
        let (endpoint, field, output_field) = match method {
            "forecast" => (
                "https://api.open-meteo.com/v1/forecast",
                "temperature_2m",
                "temperature_c",
            ),
            "air_quality" => (
                "https://air-quality-api.open-meteo.com/v1/air-quality",
                "us_aqi",
                "us_aqi",
            ),
            _ => return Err("no live adapter for this method".into()),
        };
        let latitude = input["latitude"].as_f64().ok_or("missing latitude")?;
        let longitude = input["longitude"].as_f64().ok_or("missing longitude")?;
        if !(-90.0..=90.0).contains(&latitude) || !(-180.0..=180.0).contains(&longitude) {
            return Err("invalid coordinates".into());
        }
        let mut response = client
            .get(endpoint)
            .query(&[
                ("latitude", latitude.to_string()),
                ("longitude", longitude.to_string()),
                ("current", field.to_owned()),
                ("timezone", "UTC".to_owned()),
            ])
            .send()
            .await?
            .error_for_status()?;
        let url = response.url().to_string();
        let retrieved_at = response
            .headers()
            .get("date")
            .and_then(|v| v.to_str().ok())
            .ok_or("missing HTTP Date")?
            .to_owned();
        let mut bytes = Vec::new();
        while let Some(chunk) = response.chunk().await? {
            if bytes.len() + chunk.len() > 16384 {
                return Err("response exceeds 16 KiB".into());
            }
            bytes.extend_from_slice(&chunk);
        }
        let raw: Value = serde_json::from_slice(&bytes)?;
        let value = raw["current"][field]
            .as_f64()
            .ok_or("missing current value")?;
        let as_of = raw["current"]["time"]
            .as_str()
            .ok_or("missing current time")?;
        Ok(json!({output_field:value,"as_of":format!("{as_of}:00Z"),"source":{"url":url,"retrieved_at":retrieved_at,"kind":"open-meteo"}}).to_string())
    }
    fetch(client, method, input)
        .await
        .map_err(|e| ToolError::Failed(e.to_string()))
}

async fn execute(
    case: &Case,
    concurrency: usize,
    fault: Fault,
    live: Option<reqwest::Client>,
) -> Result<Value> {
    execute_with_model(case, concurrency, fault, live, None).await
}

async fn execute_with_model(
    case: &Case,
    concurrency: usize,
    fault: Fault,
    live: Option<reqwest::Client>,
    model: Option<news_digest::Model>,
) -> Result<Value> {
    execute_with_backends(case, concurrency, fault, live, model, None).await
}

async fn execute_with_backends(
    case: &Case,
    concurrency: usize,
    fault: Fault,
    live: Option<reqwest::Client>,
    model: Option<news_digest::Model>,
    news: Option<live_news::LiveNews>,
) -> Result<Value> {
    if !(1..=4).contains(&concurrency) {
        return Err("concurrency must be 1..=4".into());
    }
    if news.is_some() && model.is_none() {
        return Err("live news requires a real model endpoint".into());
    }
    let mut runtime = if news.is_some() {
        runtime_with_live_news(case, true)?
    } else {
        runtime(case)?
    };
    let started = Instant::now();
    let mut evaluation = runtime.eval(&case.source)?;
    let mut tasks = FuturesUnordered::new();
    let mut trace = Vec::new();
    let mut peak = 0;
    let mut first_data_ms = None;
    let mut cancelled = false;
    let mut llm_calls = 0;
    let mut model_measurements = Vec::new();
    loop {
        // The VM stays on this thread. Only owned invocation data crosses into
        // adapter futures. Do not synchronously pump network calls inside the VM.
        if !evaluation.succeeded() {
            return Err(format!("Splash failed: {:?}", evaluation.diagnostics).into());
        }
        while evaluation.suspended && tasks.len() < concurrency {
            let Some(invocation) = runtime.claim_next_external_tool() else {
                break;
            };
            let input: Value = serde_json::from_str(&invocation.input)?;
            let is_digest = invocation.name == "research.digest";
            let is_query = invocation.name == "research.query";
            let fixture = if news.is_some() {
                if is_digest || is_query {
                    llm_calls += 1;
                }
                json!({"method":invocation.name.trim_start_matches("research."),"delay_ms":0})
            } else if is_digest {
                if model.is_some() {
                    llm_calls += 1;
                }
                json!({"method":"digest","delay_ms":10,"output":news_digest::fixture_digest(&input)})
            } else {
                case.tools
                    .iter()
                    .find(|t| {
                        format!("research.{}", t["method"].as_str().unwrap()) == invocation.name
                            && t["input"] == input
                    })
                    .ok_or("fixture adapter received an unexpected input")?
                    .clone()
            };
            trace.push(json!({"event":"start","tool":invocation.name,"input":input,"ms":started.elapsed().as_secs_f64()*1000.0}));
            let fault = fault.clone();
            let client = live.clone();
            let model = model.clone();
            let news = news.clone();
            tasks.push(async move {
                let delay = Duration::from_millis(fixture["delay_ms"].as_u64().unwrap());
                let fail = fault.method.as_deref() == fixture["method"].as_str();
                let deadline = if fail {
                    fault.deadline_ms.unwrap_or(5000)
                } else if is_digest {
                    45000
                } else if news.is_some() {
                    20000
                } else {
                    5000
                };
                let completed = tokio::time::timeout(Duration::from_millis(deadline), async {
                    if is_query && !fail {
                        if let Some(model) = &model {
                            return match news_query::translate(model, &input).await {
                                Ok((output, timing)) => (Ok(output), Some(timing)),
                                Err(error) => (Err(ToolError::Failed(error.to_string())), None),
                            };
                        }
                    }
                    if is_digest && !fail {
                        if let Some(model) = model {
                            return match news_digest::summarize(&model, &input).await {
                                Ok((output, timing)) => (Ok(output), Some(timing)),
                                Err(error) => (Err(ToolError::Failed(error.to_string())), None),
                            };
                        }
                    }
                    if let Some(news) = news {
                        return (
                            news.call(&invocation.name, &input)
                                .await
                                .map_err(|e| ToolError::Failed(e.to_string())),
                            None,
                        );
                    }
                    if let Some(client) = client {
                        return (
                            open_meteo(&client, fixture["method"].as_str().unwrap(), &input).await,
                            None,
                        );
                    }
                    tokio::time::sleep(delay).await;
                    if fail && fault.invalid_output {
                        (Ok("{\"invalid\":true}".to_owned()), None)
                    } else if fail && fault.deadline_ms.is_none() {
                        (
                            Err(ToolError::Failed("injected adapter failure".into())),
                            None,
                        )
                    } else {
                        (Ok(fixture["output"].to_string()), None)
                    }
                })
                .await
                .unwrap_or_else(|_| (Err(ToolError::TimedOut("adapter deadline".into())), None));
                (invocation, completed.0, completed.1)
            });
            peak = peak.max(tasks.len());
        }
        if !evaluation.suspended {
            if !tasks.is_empty() {
                return Err("template returned with unfinished adapters".into());
            }
            break;
        }
        if tasks.is_empty() {
            return Err("suspended with no runnable adapter".into());
        }
        let cancel_at = started + Duration::from_millis(fault.cancel_ms.unwrap_or(60_000));
        tokio::select! {
            result = tasks.next() => {
                let (invocation, output, measurement) = result.unwrap();
                if let Some(measurement) = measurement { model_measurements.push(measurement); }
                let ms = started.elapsed().as_secs_f64()*1000.0;
                // This is adapter completion, not publication of a complete UI dataset.
                if output.is_ok() { first_data_ms.get_or_insert(ms); }
                trace.push(json!({"event":"complete","tool":invocation.name,"input":serde_json::from_str::<Value>(&invocation.input)?,"ms":ms,"adapter_ok":output.is_ok(),"error":output.as_ref().err().map(ToString::to_string)}));
                if let Some(resumed) = runtime.complete_external_tool(invocation.id, output)? { evaluation = resumed; }
            }
            _ = tokio::time::sleep_until(tokio::time::Instant::from_std(cancel_at)), if fault.cancel_ms.is_some() => {
                // Dropping owned sleeps/reqwest futures cancels local work.
                // A remote model server may finish an already submitted request.
                tasks.clear();
                cancelled = true;
                break;
            }
        }
    }
    let output = if cancelled {
        Value::Null
    } else {
        runtime.script_value_as_json(evaluation.value, 131072, 16)?
    };
    if !cancelled {
        let discovery = news
            .as_ref()
            .map(live_news::LiveNews::discovery)
            .transpose()?;
        validate_dataset(case, &output, discovery.as_ref())?;
    }
    Ok(
        json!({"case":case.name,"concurrency":concurrency,"peak_active_tools":peak,
        "elapsed_ms":started.elapsed().as_secs_f64()*1000.0,"first_adapter_result_ms":first_data_ms,
        "cancelled":cancelled,"llm_calls":llm_calls,"model_calls":model_measurements,"output":output,"trace":trace}),
    )
}

// Splash numbers round-trip integral floats as JSON integers. Compare numeric
// values, while still binding every provenance key and string exactly.
fn json_equivalent(a: &Value, b: &Value) -> bool {
    match (a, b) {
        (Value::Number(a), Value::Number(b)) => a.as_f64() == b.as_f64(),
        (Value::Array(a), Value::Array(b)) => {
            a.len() == b.len() && a.iter().zip(b).all(|(a, b)| json_equivalent(a, b))
        }
        (Value::Object(a), Value::Object(b)) => {
            a.len() == b.len()
                && a.iter()
                    .all(|(k, a)| b.get(k).is_some_and(|b| json_equivalent(a, b)))
        }
        _ => a == b,
    }
}

fn validate_dataset(case: &Case, output: &Value, live_discovery: Option<&Value>) -> Result<()> {
    if output["schema_id"] != format!("{}.v1", case.name)
        || !matches!(output["status"].as_str(), Some("ready" | "partial"))
    {
        return Err("invalid dataset identity or state".into());
    }
    let data = &output["data"];
    let require = |valid: bool| -> Result<()> {
        if valid {
            Ok(())
        } else {
            Err("invalid dataset semantics".into())
        }
    };
    match case.name.as_str() {
        "weather" => {
            require(data["forecast"].is_object())?;
            require((output["status"] == "partial") == data["air_quality"].is_null())?;
        }
        "stock" => {
            let quote = &data["quote"];
            let baseline = &data["baseline"];
            require(
                quote["symbol"] == case.input["instrument"]["symbol"]
                    && quote["symbol"] == baseline["symbol"]
                    && quote["currency"] == baseline["currency"],
            )?;
            let base = baseline["price"].as_f64().ok_or("missing baseline price")?;
            require(base > 0.0)?;
            let expected =
                (quote["price"].as_f64().ok_or("missing quote price")? / base - 1.0) * 100.0;
            require(
                (data["return_pct"].as_f64().ok_or("missing return")? - expected).abs() < 1e-8,
            )?;
            require((output["status"] == "partial") == data["headlines"].is_null())?;
        }
        "news" | "news-digest" => {
            let rows = data["articles"].as_array().ok_or("missing articles")?;
            let missing = data["missing"].as_u64().ok_or("missing coverage")?;
            let discovery = live_discovery.unwrap_or_else(|| &case.tools[0]["output"]);
            let expected = discovery["items"].as_array().ok_or("missing discovery")?;
            require(rows.len() + missing as usize == expected.len())?;
            let missing_digest =
                case.name == "news-digest" && !rows.is_empty() && data["digest"].is_null();
            let partial_discovery = discovery["source"]["partial"] == true || expected.is_empty();
            require(
                (output["status"] == "partial")
                    == (missing > 0 || missing_digest || partial_discovery),
            )?;
            require(json_equivalent(&data["discovery"], &discovery["source"]))?;
            let unique: std::collections::BTreeSet<_> =
                rows.iter().map(|r| r["id"].as_str()).collect();
            require(unique.len() == rows.len())?;
            for row in rows {
                require(expected.iter().any(|item| item["id"] == row["id"]))?;
            }
            if case.name == "news-digest" {
                require(data["language"] == case.input["language"])?;
                if !data["digest"].is_null() {
                    news_digest::validate(
                        &json!({"articles":rows,"language":data["language"]}),
                        &data["digest"],
                    )?;
                }
            }
        }
        _ => return Err("unknown dataset".into()),
    }
    Ok(())
}

fn median(mut values: Vec<f64>) -> f64 {
    values.sort_by(f64::total_cmp);
    values[values.len() / 2]
}

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<()> {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if args.first().map(String::as_str) == Some("--live-news") {
        if !(2..=4).contains(&args.len()) {
            return Err("usage: --live-news en|zh-CN [TOPIC_OR_QUERY] [MODEL_BASE_URL]".into());
        }
        let wall_started = Instant::now();
        let started_at = chrono::Utc::now().to_rfc3339();
        let case = live_news::case(
            &args[1],
            args.get(2).map(String::as_str).unwrap_or("technology"),
        )?;
        let model = news_digest::Model {
            client: reqwest::Client::builder()
                .no_proxy()
                .redirect(reqwest::redirect::Policy::none())
                .timeout(Duration::from_secs(45))
                .build()?,
            base_url: args
                .get(3)
                .cloned()
                .unwrap_or_else(|| "http://127.0.0.1:30881/v1".into()),
            name: "qwen3.8-27b".into(),
        };
        let mut result = execute_with_backends(
            &case,
            3,
            Fault::default(),
            None,
            Some(model),
            Some(live_news::LiveNews::new()?),
        )
        .await?;
        result["mode"] = json!("live_rss_articles_rtx_splash");
        result["started_at"] = json!(started_at);
        result["host_elapsed_ms"] = json!(wall_started.elapsed().as_secs_f64() * 1000.0);
        live_news::redact_evidence(&mut result);
        println!("{}", serde_json::to_string_pretty(&result)?);
        return Ok(());
    }
    if args.first().map(String::as_str) == Some("--news-digest") {
        if !(2..=3).contains(&args.len()) {
            return Err("usage: --news-digest en|zh-CN [MODEL_BASE_URL]".into());
        }
        let case = news_digest::case(&args[1])?;
        let model = news_digest::Model {
            client: reqwest::Client::builder()
                .no_proxy()
                .redirect(reqwest::redirect::Policy::none())
                .timeout(Duration::from_secs(45))
                .build()?,
            base_url: args
                .get(2)
                .cloned()
                .unwrap_or_else(|| "http://127.0.0.1:30881/v1".into()),
            name: "qwen3.8-27b".into(),
        };
        let result = execute_with_model(&case, 3, Fault::default(), None, Some(model)).await?;
        println!("{}", serde_json::to_string_pretty(&result)?);
        return Ok(());
    }
    if args.first().map(String::as_str) == Some("--once") {
        if args.len() != 3 {
            return Err("usage: --once CASE INPUT_JSON_FILE".into());
        }
        let case = cases()
            .into_iter()
            .find(|c| c.name == args[1])
            .ok_or("unknown template")?;
        let input: Value = serde_json::from_str(&std::fs::read_to_string(&args[2])?)?;
        if input != case.input {
            return Err("fixture input mismatch; no synthetic substitution permitted".into());
        }
        let result = execute(&case, 3, Fault::default(), None).await?;
        println!("{}", serde_json::to_string(&result)?);
        return Ok(());
    }
    let live = match std::env::args().nth(1).as_deref() {
        None => None,
        Some("--live-weather") => Some(
            reqwest::Client::builder()
                .no_proxy()
                .redirect(reqwest::redirect::Policy::none())
                .timeout(Duration::from_secs(5))
                .build()?,
        ),
        _ => return Err("usage: octos-one-splash-research-experiment [--live-weather]".into()),
    };
    let mut runs = Vec::new();
    let mut summary = Vec::new();
    for case in cases() {
        if live.is_some() && case.name != "weather" {
            continue;
        }
        // Warm both modes, then alternate order to reduce order/initialization bias.
        for cap in [1, 3] {
            execute(&case, cap, Fault::default(), live.clone()).await?;
        }
        let mut sequential = Vec::new();
        let mut parallel = Vec::new();
        for round in 0..5 {
            for cap in if round % 2 == 0 { [1, 3] } else { [3, 1] } {
                let result = execute(&case, cap, Fault::default(), live.clone()).await?;
                let elapsed = result["elapsed_ms"].as_f64().unwrap();
                if cap == 1 {
                    sequential.push(elapsed);
                } else {
                    parallel.push(elapsed);
                }
                runs.push(result);
            }
        }
        let seq = median(sequential);
        let par = median(parallel);
        summary.push(json!({"case":case.name,"sequential_median_ms":seq,"parallel_median_ms":par,"speedup":seq/par}));
    }
    println!(
        "{}",
        serde_json::to_string_pretty(
            &json!({"mode":if live.is_some() {"live_open_meteo_real_splash_vm"} else {"fixture_io_real_splash_vm"},"repetitions":5,"summary":summary,"runs":runs})
        )?
    );
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    #[tokio::test]
    async fn digest_runs_after_retrieval_and_failure_keeps_original_sources() -> Result<()> {
        let case = news_digest::case("zh-CN")?;
        let good = run(&case, 3, Fault::default()).await?;
        let trace = good["trace"].as_array().unwrap();
        let digest_start = trace
            .iter()
            .find(|e| e["event"] == "start" && e["tool"] == "research.digest")
            .unwrap()["ms"]
            .as_f64()
            .unwrap();
        assert!(trace
            .iter()
            .filter(|e| e["event"] == "complete" && e["tool"] == "research.article")
            .all(|e| e["ms"].as_f64().unwrap() <= digest_start));
        assert_eq!(good["output"]["data"]["digest"]["language"], "zh-CN");
        for fault in [
            Fault {
                method: Some("digest".into()),
                ..Default::default()
            },
            Fault {
                method: Some("digest".into()),
                invalid_output: true,
                ..Default::default()
            },
            Fault {
                method: Some("digest".into()),
                deadline_ms: Some(1),
                ..Default::default()
            },
        ] {
            let bad = run(&case, 3, fault).await?;
            assert_eq!(bad["output"]["status"], "partial");
            assert!(bad["output"]["data"]["digest"].is_null());
            assert_eq!(
                bad["output"]["data"]["articles"],
                good["output"]["data"]["articles"]
            );
        }
        Ok(())
    }

    #[tokio::test]
    async fn no_digest_is_requested_when_all_article_reads_fail() -> Result<()> {
        let case = news_digest::case("en")?;
        let result = run(
            &case,
            3,
            Fault {
                method: Some("article".into()),
                ..Default::default()
            },
        )
        .await?;
        assert_eq!(result["output"]["status"], "partial");
        assert_eq!(result["output"]["data"]["missing"], 3);
        assert!(!result["trace"]
            .as_array()
            .unwrap()
            .iter()
            .any(|e| e["tool"] == "research.digest"));
        Ok(())
    }
    #[tokio::test]
    async fn same_results_with_bounded_parallelism_and_real_dependencies() -> Result<()> {
        for case in cases() {
            let seq = run(&case, 1, Fault::default()).await?;
            let par = run(&case, 3, Fault::default()).await?;
            assert_eq!(seq["output"], par["output"]);
            assert!(par["peak_active_tools"].as_u64().unwrap() > 1);
            assert!(par["peak_active_tools"].as_u64().unwrap() <= 3);
            if case.name == "news" {
                let trace = par["trace"].as_array().unwrap();
                let discovery = trace
                    .iter()
                    .find(|e| e["event"] == "complete" && e["tool"] == "research.search")
                    .unwrap()["ms"]
                    .as_f64()
                    .unwrap();
                assert!(trace
                    .iter()
                    .filter(|e| e["event"] == "start" && e["tool"] == "research.article")
                    .all(|e| e["ms"].as_f64().unwrap() >= discovery));
                let completed_ids = trace
                    .iter()
                    .filter(|e| e["event"] == "complete" && e["tool"] == "research.article")
                    .map(|e| e["input"]["id"].clone())
                    .collect::<Vec<_>>();
                assert_eq!(completed_ids, vec![json!("b"), json!("c"), json!("a")]);
                assert_eq!(par["output"]["data"]["articles"][0]["id"], "a");
            }
        }
        Ok(())
    }
    #[tokio::test]
    async fn optional_failure_timeout_and_bad_schema_keep_partial_data() -> Result<()> {
        let case = cases().remove(0);
        for fault in [
            Fault {
                method: Some("air_quality".into()),
                ..Default::default()
            },
            Fault {
                method: Some("air_quality".into()),
                deadline_ms: Some(10),
                ..Default::default()
            },
            Fault {
                method: Some("air_quality".into()),
                invalid_output: true,
                ..Default::default()
            },
        ] {
            let result = run(&case, 3, fault).await?;
            assert_eq!(result["output"]["status"], "partial");
            assert!(result["output"]["data"]["forecast"].is_object());
            assert!(result["output"]["data"]["air_quality"].is_null());
        }
        Ok(())
    }
    #[tokio::test]
    async fn required_failure_does_not_publish_a_ready_dataset() {
        let case = cases().remove(0);
        assert!(run(
            &case,
            3,
            Fault {
                method: Some("forecast".into()),
                ..Default::default()
            }
        )
        .await
        .is_err());
    }
    #[tokio::test]
    async fn cancellation_discards_inflight_results() -> Result<()> {
        let result = run(
            &cases().remove(0),
            3,
            Fault {
                cancel_ms: Some(10),
                ..Default::default()
            },
        )
        .await?;
        assert_eq!(result["cancelled"], true);
        assert!(result["output"].is_null());
        assert_eq!(result["trace"].as_array().unwrap().len(), 2);
        Ok(())
    }
    #[test]
    fn rejects_unregistered_tools_bad_inputs_and_call_budget_overflow() -> Result<()> {
        for source in [
            "use mod.tool\ntool.start_json(\"shell.exec\", {command: \"id\"}).await()",
            "use mod.research\nresearch.forecast({unexpected: true}).await()",
            "use mod.research\nlet a = research.forecast(request.location)\nlet b = research.forecast(request.location)\nb.await()",
        ] {
            let mut runtime = runtime(&cases().remove(0))?;
            let result = runtime.eval(source)?;
            assert!(!result.succeeded());
        }
        // Structural contracts are actually compiled, not documentation hints.
        let contract = JsonSchema::compile(schema(&json!({"price":1.0})))?;
        assert!(contract.validate(&json!({"price":"invented"})).is_err());
        Ok(())
    }
}
