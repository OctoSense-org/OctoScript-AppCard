//! JSON-lines bridge: the real Splash VM owns dependencies; the host owns I/O.
use serde_json::{json, Value};
use splash_capabilities::{CapabilityModule, CapabilityRuntime, JsonToolContract, ToolError, ToolMetadata, ToolPolicy};
use splash_core::ExecutionLimits;
use std::{io::{self, BufRead, Write}, collections::BTreeMap, time::{Duration, Instant}};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut lines = io::stdin().lock().lines();
    let request: Value = serde_json::from_str(&lines.next().ok_or("missing request")??)?;
    let jobs = request["jobs"].as_array().ok_or("missing jobs")?;
    if jobs.is_empty() || jobs.len() > 8 { return Err("expected 1..=8 jobs".into()); }
    let mut runtime = CapabilityRuntime::with_limits_and_pending(ExecutionLimits::default(), 12)?;
    let mut module = CapabilityModule::new("composition", "Bounded live composition study");
    let mut policy = ToolPolicy::json("composition.fetch");
    policy.max_calls = jobs.len(); policy.max_input_bytes = 4096; policy.max_output_bytes = 32768;
    policy.max_deferred_duration = Some(Duration::from_secs(40));
    runtime.register_validated_external_json_tool(policy, ToolMetadata::new("Read one admitted source"),
        JsonToolContract::new(json!({"enum":jobs}), json!({"type":"object"}))?)?;
    module = module.with_deferred_method("fetch", "composition.fetch");
    let mut policy = ToolPolicy::json("composition.synthesize");
    policy.max_calls = 1; policy.max_input_bytes = 65536; policy.max_output_bytes = 16384;
    policy.max_deferred_duration = Some(Duration::from_secs(60));
    runtime.register_validated_external_json_tool(policy, ToolMetadata::new("Evidence-bound synthesis"),
        JsonToolContract::new(json!({"type":"object"}), request["output_schema"].clone())?)?;
    module = module.with_deferred_method("synthesize", "composition.synthesize");
    runtime.register_capability_module(module)?;
    runtime.set_json_global("request", &request, 65536, 12)?;
    let started = Instant::now();
    let mut evaluation = runtime.eval(include_str!("../../templates/composition.splash"))?;
    let mut pending = BTreeMap::new();
    loop {
        if !evaluation.succeeded() { return Err(format!("Splash failed: {:?}",evaluation.diagnostics).into()); }
        while let Some(call) = runtime.claim_next_external_tool() {
            let token = pending.len().to_string() + ":" + &format!("{}",started.elapsed().as_nanos());
            println!("{}",json!({"invoke":token,"tool":call.name,"input":serde_json::from_str::<Value>(&call.input)?,"ms":started.elapsed().as_secs_f64()*1000.0}));
            io::stdout().flush()?;
            pending.insert(token, call.id);
        }
        if !evaluation.suspended {
            if !pending.is_empty() { return Err("unfinished tools".into()); }
            let output = runtime.script_value_as_json(evaluation.value, 131072, 16)?;
            println!("{}",json!({"done":output,"elapsed_ms":started.elapsed().as_secs_f64()*1000.0}));
            return Ok(());
        }
        let reply: Value = serde_json::from_str(&lines.next().ok_or("host disconnected")??)?;
        let token = reply["reply"].as_str().ok_or("missing reply token")?;
        let id = pending.remove(token).ok_or("unknown/duplicate reply")?;
        let result = if let Some(error) = reply["error"].as_str() { Err(ToolError::Failed(error.into())) }
            else { Ok(reply["output"].to_string()) };
        if let Some(next) = runtime.complete_external_tool(id, result)? { evaluation = next; }
    }
}
