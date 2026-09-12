//! Live, read-only RSS discovery and publisher-specific article extraction.
//! No fixture fallback: unavailable feeds/articles are reported as failures.
use crate::{news_digest, news_query, Case, Result};
use chrono::{DateTime, Utc};
use futures::{stream, StreamExt};
use scraper::{Html, Selector};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use splash_capabilities::{
    CapabilityModule, CapabilityRuntime, JsonToolContract, ToolMetadata, ToolPolicy,
};
use std::{
    cell::RefCell,
    collections::{BTreeMap, BTreeSet},
    rc::Rc,
    time::{Duration, Instant},
};

const TEXT_BYTES: usize = 6000;
const HTTP_BYTES: usize = 2 * 1024 * 1024;
const DEADLINE_SECS: u64 = 20;

#[derive(Clone, Copy)]
struct Feed {
    publisher: &'static str,
    url: &'static str,
}

fn feeds(topic: &str) -> Result<[Feed; 2]> {
    let urls = match topic {
        "technology" => [
            "https://feeds.bbci.co.uk/news/technology/rss.xml",
            "https://www.theguardian.com/technology/rss",
        ],
        "world" => [
            "https://feeds.bbci.co.uk/news/world/rss.xml",
            "https://www.theguardian.com/world/rss",
        ],
        "business" => [
            "https://feeds.bbci.co.uk/news/business/rss.xml",
            "https://www.theguardian.com/business/rss",
        ],
        _ => return Err("supported news topics: technology, world, business".into()),
    };
    Ok([
        Feed {
            publisher: "bbc",
            url: urls[0],
        },
        Feed {
            publisher: "guardian",
            url: urls[1],
        },
    ])
}

pub fn case(language: &str, topic: &str) -> Result<Case> {
    if topic.trim().is_empty() || topic.chars().count() > 160 {
        return Err("enter a news topic or search query of 1..=160 characters".into());
    }
    if !["en", "zh-CN"].contains(&language) {
        return Err("supported languages: en, zh-CN".into());
    }
    Ok(Case {
        name: "news-digest".into(),
        source: include_str!("../templates/news-digest.splash").into(),
        input: json!({"search":{"topic":topic,"limit":3,"max_age_hours":72},"language":language,
            "normalize_query":news_query::needed(topic)}),
        tools: Vec::new(),
    })
}

fn string(max: usize) -> Value {
    json!({"type":"string","minLength":1,"maxLength":max})
}
fn object(properties: Value) -> Value {
    json!({"type":"object","additionalProperties":false,
        "required":properties.as_object().unwrap().keys().collect::<Vec<_>>(),"properties":properties})
}

pub fn article_schema() -> Value {
    object(
        json!({"id":string(80),"title":string(1024),"language":string(16),"text":string(TEXT_BYTES),
        "source":object(json!({"kind":string(32),"publisher":string(32),"url":string(2048),
            "feed_url":string(2048),"retrieved_at":string(64),"published_at":string(64),
            "extractor":string(64),"evidence_sha256":string(64),
            "evidence_bytes":{"type":"integer","minimum":1,"maximum":TEXT_BYTES},
            "extracted_bytes":{"type":"integer","minimum":1},"content_truncated":{"type":"boolean"}}))}),
    )
}

pub fn register(
    runtime: &mut CapabilityRuntime,
    mut module: CapabilityModule,
    case: &Case,
) -> Result<CapabilityModule> {
    let search_input = object(
        json!({"topic":string(160),
        "limit":{"type":"integer","enum":[3]},"max_age_hours":{"type":"integer","enum":[72]}}),
    );
    let mut query_policy = ToolPolicy::json("research.query");
    query_policy.max_calls = 1;
    query_policy.max_input_bytes = 2048;
    query_policy.max_output_bytes = 2048;
    query_policy.max_deferred_duration = Some(Duration::from_secs(DEADLINE_SECS));
    runtime.register_validated_external_json_tool(query_policy, ToolMetadata::new("Translate news search terms"),
        JsonToolContract::new(object(json!({"query":{"type":"string","enum":[case.input["search"]["topic"]]}})), news_query::schema())?)?;
    module = module.with_deferred_method("query", "research.query");
    let feed_status = object(
        json!({"publisher":string(32),"url":string(2048),"ok":{"type":"boolean"},
        "error":{"type":"string","maxLength":2048},"elapsed_ms":{"type":"number"},
        "candidates":{"type":"integer","minimum":0},"http_date":{"type":"string","maxLength":128}}),
    );
    let search_output = object(
        json!({"items":{"type":"array","maxItems":3,"items":object(json!({"id":string(80)}))},
        "source":object(json!({"kind":string(32),"topic":string(160),"retrieved_at":string(64),
            "max_age_hours":{"type":"integer"},"selected":{"type":"integer"},
            "partial":{"type":"boolean"},"feeds":{"type":"array","maxItems":2,"items":feed_status}}))}),
    );
    for (method, calls, input, output) in [
        ("search", 1, search_input, search_output),
        (
            "article",
            3,
            object(json!({"id":string(80)})),
            article_schema(),
        ),
    ] {
        let name = format!("research.{method}");
        let mut policy = ToolPolicy::json(&name);
        policy.max_calls = calls;
        policy.max_input_bytes = 2048;
        policy.max_output_bytes = 16384;
        policy.max_deferred_duration = Some(Duration::from_secs(DEADLINE_SECS));
        runtime.register_validated_external_json_tool(
            policy,
            ToolMetadata::new("Live bounded news adapter"),
            JsonToolContract::new(input, output)?,
        )?;
        module = module.with_deferred_method(method, name);
    }
    news_digest::register_schema(
        runtime,
        module,
        case.input["language"].clone(),
        article_schema(),
        None,
    )
}

#[derive(Clone)]
struct Candidate {
    id: String,
    title: String,
    url: String,
    published: DateTime<Utc>,
    feed: Feed,
    discovery_url: String,
    relevance: usize,
}

// The VM and its futures run on one thread. No borrow is held across await.
#[derive(Clone)]
pub struct LiveNews {
    client: reqwest::Client,
    articles: Rc<RefCell<BTreeMap<String, Candidate>>>,
    discovery: Rc<RefCell<Option<Value>>>,
}

impl LiveNews {
    pub fn new() -> Result<Self> {
        Ok(Self {
            client: reqwest::Client::builder()
                .user_agent("Octos-News-Research/0.1")
                .connect_timeout(Duration::from_secs(5))
                .timeout(Duration::from_secs(15))
                .redirect(reqwest::redirect::Policy::custom(|attempt| {
                    if attempt.previous().len() >= 3 || !allowed_url(attempt.url()) {
                        attempt.error("unapproved news redirect")
                    } else {
                        attempt.follow()
                    }
                }))
                .build()?,
            articles: Rc::default(),
            discovery: Rc::default(),
        })
    }

    pub fn discovery(&self) -> Result<Value> {
        self.discovery
            .borrow()
            .clone()
            .ok_or_else(|| "no live discovery result".into())
    }

    pub async fn call(&self, method: &str, input: &Value) -> Result<String> {
        let value = match method {
            "research.search" => self.search(input).await?,
            "research.article" => {
                self.article(input["id"].as_str().ok_or("missing article ID")?)
                    .await?
            }
            _ => return Err("unknown live news capability".into()),
        };
        Ok(value.to_string())
    }

    async fn fetch(&self, url: &str) -> Result<(String, String, String)> {
        if !allowed_url(&reqwest::Url::parse(url)?) {
            return Err("unapproved news URL".into());
        }
        let mut response = self.client.get(url).send().await?.error_for_status()?;
        let final_url = response.url().to_string();
        let date = response
            .headers()
            .get("date")
            .and_then(|v| v.to_str().ok())
            .unwrap_or("")
            .to_owned();
        let mut bytes = Vec::new();
        while let Some(chunk) = response.chunk().await? {
            if bytes.len() + chunk.len() > HTTP_BYTES {
                return Err("news response exceeds 2 MiB".into());
            }
            bytes.extend_from_slice(&chunk);
        }
        Ok((String::from_utf8(bytes)?, final_url, date))
    }

    async fn search(&self, input: &Value) -> Result<Value> {
        let topic = input["topic"].as_str().ok_or("missing topic")?;
        let now = Utc::now();
        let hours = input["max_age_hours"]
            .as_i64()
            .ok_or("missing freshness window")?;
        if hours != 72 || input["limit"] != 3 {
            return Err("invalid discovery bounds".into());
        }
        let is_search = feeds(topic).is_err();
        let targets: Vec<_> = if let Ok(feeds) = feeds(topic) {
            feeds
                .into_iter()
                .map(|feed| (feed, feed.url.to_owned()))
                .collect()
        } else {
            feeds("technology")?
                .into_iter()
                .map(|feed| {
                    let sites = if feed.publisher == "bbc" {
                        "(site:bbc.co.uk OR site:bbc.com)"
                    } else {
                        "site:theguardian.com"
                    };
                    let mut url =
                        reqwest::Url::parse("https://www.bing.com/news/search").expect("fixed URL");
                    url.query_pairs_mut()
                        .append_pair("q", &format!("{topic} {sites}"))
                        .append_pair("format", "rss")
                        .append_pair("mkt", "en-US");
                    (feed, url.to_string())
                })
                .collect()
        };
        let results = stream::iter(targets)
            .map(|(feed, url)| async move {
                let started = Instant::now();
                let result = async {
                    let (xml, _, date) = self.fetch(&url).await?;
                    let mut items = parse_feed(&xml, feed, now, hours)?;
                    for (position, item) in items.iter_mut().enumerate() {
                        item.discovery_url = url.clone();
                        if is_search {
                            let title = item.title.to_lowercase();
                            let matches = topic
                                .to_lowercase()
                                .split_whitespace()
                                .filter(|term| term.len() > 1 && title.contains(term))
                                .count();
                            item.relevance = matches * 1000 + 100usize.saturating_sub(position);
                        }
                    }
                    Ok::<_, Box<dyn std::error::Error>>((items, date))
                }
                .await;
                (feed, url, result, started.elapsed().as_secs_f64() * 1000.0)
            })
            .buffered(2)
            .collect::<Vec<_>>()
            .await;
        let mut candidates = Vec::new();
        let mut statuses = Vec::new();
        for (feed, url, result, elapsed) in results {
            let (ok, error, count, date) = match result {
                Ok((items, date)) => {
                    let n = items.len();
                    candidates.extend(items);
                    (true, String::new(), n, date)
                }
                Err(error) => (false, error.to_string(), 0, String::new()),
            };
            statuses.push(
                json!({"publisher":feed.publisher,"url":url,"ok":ok,"error":error,
                "candidates":count,"elapsed_ms":elapsed,"http_date":date}),
            );
        }
        let selected = select(candidates);
        let items: Vec<_> = selected.iter().map(|a| json!({"id":a.id})).collect();
        *self.articles.borrow_mut() = selected.into_iter().map(|a| (a.id.clone(), a)).collect();
        let output = json!({"items":items,"source":{"kind":if is_search {"live-news-search"} else {"live-rss"},"topic":topic,
            "retrieved_at":now.to_rfc3339(),"max_age_hours":hours,"selected":items.len(),
            "partial":statuses.iter().any(|s| s["ok"] != true) || items.len() < 3,"feeds":statuses}});
        *self.discovery.borrow_mut() = Some(output.clone());
        Ok(output)
    }

    async fn article(&self, id: &str) -> Result<Value> {
        let candidate = self
            .articles
            .borrow()
            .get(id)
            .cloned()
            .ok_or("article ID was not discovered in this run")?;
        let (html, url, _) = self.fetch(&candidate.url).await?;
        if publisher(&reqwest::Url::parse(&url)?) != Some(candidate.feed.publisher) {
            return Err("article redirected to a different publisher".into());
        }
        let (text, extracted_bytes, extractor) = extract(&html, candidate.feed.publisher)?;
        Ok(
            json!({"id":id,"title":candidate.title,"language":"en","text":text,
            "source":{"kind":"live-article","publisher":candidate.feed.publisher,"url":url,
                "feed_url":candidate.discovery_url,"retrieved_at":Utc::now().to_rfc3339(),
                "published_at":candidate.published.to_rfc3339(),"extractor":extractor,
                "evidence_sha256":hash(&text),"evidence_bytes":text.len(),"extracted_bytes":extracted_bytes,
                "content_truncated":text.len() < extracted_bytes}}),
        )
    }
}

fn publisher(url: &reqwest::Url) -> Option<&'static str> {
    match url.host_str()? {
        "www.bbc.co.uk" | "www.bbc.com" => Some("bbc"),
        "www.theguardian.com" => Some("guardian"),
        _ => None,
    }
}
fn allowed_url(url: &reqwest::Url) -> bool {
    url.scheme() == "https"
        && url.username().is_empty()
        && url.password().is_none()
        && url.port_or_known_default() == Some(443)
        && (publisher(url).is_some()
            || matches!(url.host_str(), Some("feeds.bbci.co.uk" | "www.bing.com")))
}
fn hash(text: &str) -> String {
    format!("{:x}", Sha256::digest(text.as_bytes()))
}

fn parse_feed(xml: &str, feed: Feed, now: DateTime<Utc>, hours: i64) -> Result<Vec<Candidate>> {
    let channel = rss::Channel::read_from(xml.as_bytes())?;
    let mut candidates = Vec::new();
    for item in channel.items().iter().take(100) {
        let Some((title, link, published)) = item
            .title()
            .zip(item.link())
            .zip(item.pub_date())
            .map(|((a, b), c)| (a, b, c))
        else {
            continue;
        };
        let (Ok(mut url), Ok(published)) = (
            reqwest::Url::parse(link),
            DateTime::parse_from_rfc2822(published),
        ) else {
            continue;
        };
        // Decode the search wrapper as data; fetch only admitted publisher URLs.
        if url.host_str() == Some("www.bing.com") && url.path() == "/news/apiclick.aspx" {
            let Some(target) = url
                .query_pairs()
                .find(|(k, _)| k == "url")
                .map(|(_, v)| v.into_owned())
            else {
                continue;
            };
            let Ok(target) = reqwest::Url::parse(&target) else {
                continue;
            };
            url = target;
            if feed.publisher == "bbc" && !url.path().starts_with("/news/articles/") {
                continue;
            }
        }
        let published = published.with_timezone(&Utc);
        if !allowed_url(&url)
            || publisher(&url) != Some(feed.publisher)
            || title.trim().is_empty()
            || title.chars().count() > 1024
            || published < now - chrono::Duration::hours(hours)
            || published > now + chrono::Duration::minutes(5)
        {
            continue;
        }
        // The supported publishers identify articles by path; remove RSS tracking.
        url.set_query(None);
        url.set_fragment(None);
        let url = url.to_string();
        candidates.push(Candidate {
            id: format!("n{}", &hash(&url)[..16]),
            title: title.trim().into(),
            url,
            published,
            feed,
            discovery_url: feed.url.to_owned(),
            relevance: 0,
        });
    }
    Ok(candidates)
}

fn select(mut candidates: Vec<Candidate>) -> Vec<Candidate> {
    candidates.sort_by(|a, b| {
        b.relevance.cmp(&a.relevance).then_with(|| {
            b.published
                .cmp(&a.published)
                .then_with(|| a.url.cmp(&b.url))
        })
    });
    let mut seen_urls = BTreeSet::new();
    let mut seen_titles = BTreeSet::new();
    candidates
        .retain(|a| seen_urls.insert(a.url.clone()) && seen_titles.insert(a.title.to_lowercase()));
    // Preserve source diversity when both publishers have fresh items, then fill
    // the remaining slot by publication time. This is not semantic story dedup.
    let mut chosen = Vec::new();
    let mut publishers = BTreeSet::new();
    for a in &candidates {
        if publishers.insert(a.feed.publisher) {
            chosen.push(a.clone());
        }
    }
    for a in candidates {
        if chosen.len() == 3 {
            break;
        }
        if !chosen.iter().any(|c| c.id == a.id) {
            chosen.push(a);
        }
    }
    chosen.sort_by(|a, b| {
        b.relevance.cmp(&a.relevance).then_with(|| {
            b.published
                .cmp(&a.published)
                .then_with(|| a.url.cmp(&b.url))
        })
    });
    chosen
}

fn extract(html: &str, publisher: &str) -> Result<(String, usize, &'static str)> {
    let (selector, version) = match publisher {
        "bbc" => ("article [data-block='text'] p, article [data-component='text-block'] p", "bbc-text-v2"),
        "guardian" => ("article .article-body-viewer-selector > p, article .article-body-commercial-selector > p", "guardian-body-v1"),
        _ => return Err("unsupported article publisher".into()),
    };
    let html = Html::parse_document(html);
    let selector = Selector::parse(selector).map_err(|_| "invalid article selector")?;
    let mut seen = BTreeSet::new();
    let paragraphs: Vec<String> = html
        .select(&selector)
        .map(|p| {
            p.text()
                .collect::<Vec<_>>()
                .join("")
                .split_whitespace()
                .collect::<Vec<_>>()
                .join(" ")
        })
        .filter(|p| {
            !p.is_empty()
                && !p.to_lowercase().starts_with("sign up for our ")
                && seen.insert(p.clone())
        })
        .collect();
    let full = paragraphs.join("\n\n");
    if full.chars().count() < 400 {
        return Err("no usable article body (blocked, short or unsupported page)".into());
    }
    let mut text = String::new();
    for paragraph in paragraphs {
        let separator = if text.is_empty() { "" } else { "\n\n" };
        if text.len() + separator.len() + paragraph.len() > TEXT_BYTES {
            break;
        }
        text.push_str(separator);
        text.push_str(&paragraph);
    }
    if text.chars().count() < 400 {
        return Err("article paragraphs exceed the evidence budget".into());
    }
    Ok((text, full.len(), version))
}

/// Published diagnostics retain provenance and hashes, not copies of articles.
pub fn redact_evidence(value: &mut Value) {
    match value {
        Value::Object(fields) => {
            if fields.contains_key("source") && fields.contains_key("text") {
                fields.remove("text");
            }
            for child in fields.values_mut() {
                redact_evidence(child);
            }
        }
        Value::Array(items) => {
            for child in items {
                redact_evidence(child);
            }
        }
        _ => (),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn discovery_filters_stale_future_foreign_and_duplicate_articles() -> Result<()> {
        let feed = feeds("technology")?[0];
        let now = DateTime::parse_from_rfc3339("2026-09-10T05:00:00Z")?.with_timezone(&Utc);
        let item = |title: &str, path: &str, date: &str| {
            format!(
                "<item><title>{title}</title><link>{path}</link><pubDate>{date}</pubDate></item>"
            )
        };
        let xml = format!("<rss version='2.0'><channel><title>Test</title><link>https://www.bbc.com</link><description>Authored test</description>{}{}{}{}{}</channel></rss>",
            item("Fresh", "https://www.bbc.com/news/a?at_medium=RSS", "Thu, 10 Sep 2026 04:00:00 GMT"),
            item("Fresh", "https://www.bbc.com/news/a", "Thu, 10 Sep 2026 04:00:00 GMT"),
            item("Old", "https://www.bbc.com/news/old", "Tue, 01 Sep 2026 04:00:00 GMT"),
            item("Future", "https://www.bbc.com/news/future", "Fri, 11 Sep 2026 04:00:00 GMT"),
            item("Foreign", "https://example.com/news/a", "Thu, 10 Sep 2026 04:00:00 GMT"));
        let chosen = select(parse_feed(&xml, feed, now, 72)?);
        assert_eq!(chosen.len(), 1);
        assert_eq!(chosen[0].url, "https://www.bbc.com/news/a");
        assert!(!allowed_url(&reqwest::Url::parse(
            "https://www.bbc.com@127.0.0.1/news"
        )?));
        assert!(!allowed_url(&reqwest::Url::parse(
            "https://www.bbc.com:8443/news"
        )?));
        Ok(())
    }
    #[test]
    fn extraction_excludes_chrome_and_bounds_complete_unicode_paragraphs() -> Result<()> {
        let paragraph =
            "This is an authored evidence paragraph with measurements and their conditions. "
                .repeat(8);
        let body = format!("<article><nav><p>Never summarize this menu</p></nav><div data-block='text'><p>{paragraph}</p><p>{}</p></div></article>", "测试原文。".repeat(1500));
        let (text, total, _) = extract(&body, "bbc")?;
        assert!(text.len() <= TEXT_BYTES && text.len() < total);
        assert!(!text.contains("menu"));
        assert!(text.contains("conditions"));
        assert!(extract(
            "<article><p>Please sign in to continue</p></article>",
            "bbc"
        )
        .is_err());
        Ok(())
    }
    #[tokio::test]
    async fn undiscovered_ids_cannot_trigger_an_article_fetch() -> Result<()> {
        assert!(LiveNews::new()?.article("unknown").await.is_err());
        Ok(())
    }

    #[test]
    fn search_wrappers_only_resolve_to_supported_article_pages() -> Result<()> {
        let feed = feeds("technology")?[0];
        let now = DateTime::parse_from_rfc3339("2026-09-10T05:00:00Z")?.with_timezone(&Utc);
        let mut xml = "<rss version='2.0'><channel><title>Test</title><link>https://www.bing.com</link><description>Authored test</description>".to_owned();
        for target in ["https://www.bbc.co.uk/news/articles/one", "https://127.0.0.1/private", "https://www.bbc.co.uk/programmes/video"] {
            let mut wrapper = reqwest::Url::parse("http://www.bing.com/news/apiclick.aspx")?;
            wrapper.query_pairs_mut().append_pair("url", target);
            xml.push_str(&format!("<item><title>Apple news</title><link>{wrapper}</link><pubDate>Thu, 10 Sep 2026 04:00:00 GMT</pubDate></item>"));
        }
        xml.push_str("</channel></rss>");
        let found = parse_feed(&xml, feed, now, 72)?;
        assert_eq!(found.len(), 1);
        assert_eq!(found[0].url, "https://www.bbc.co.uk/news/articles/one");
        assert!(case("en", "Apple iPhone").is_ok());
        assert!(case("en", "").is_err());
        assert!(case("en", &"x".repeat(161)).is_err());
        Ok(())
    }

    #[test]
    fn empty_live_discovery_keeps_failures_and_skips_inference() -> Result<()> {
        let case = case("zh-CN", "technology")?;
        let mut runtime = crate::runtime_with_live_news(&case, true)?;
        assert!(runtime.eval(&case.source)?.suspended);
        let invocation = runtime.claim_next_external_tool().ok_or("missing search")?;
        assert_eq!(invocation.name, "research.search");
        let discovery = json!({"items":[],"source":{"kind":"live-rss","topic":"technology",
            "retrieved_at":"2026-09-10T00:00:00Z","max_age_hours":72,"selected":0,"partial":true,
            "feeds":[{"publisher":"bbc","url":"https://feeds.bbci.co.uk/news/technology/rss.xml",
                "ok":false,"error":"test timeout","elapsed_ms":15000.0,"candidates":0,"http_date":""}]}});
        let evaluation = runtime
            .complete_external_tool(invocation.id, Ok(discovery.to_string()))?
            .ok_or("VM did not resume")?;
        assert!(evaluation.succeeded() && !evaluation.suspended);
        assert!(runtime.claim_next_external_tool().is_none());
        let output = runtime.script_value_as_json(evaluation.value, 16384, 16)?;
        crate::validate_dataset(&case, &output, Some(&discovery))?;
        assert_eq!(output["status"], "partial");
        assert_eq!(
            output["data"]["discovery"]["feeds"][0]["error"],
            "test timeout"
        );
        assert!(output["data"]["digest"].is_null());
        Ok(())
    }

    #[test]
    fn selection_keeps_two_publishers_and_redaction_keeps_provenance() -> Result<()> {
        let feeds = feeds("technology")?;
        let mut candidates = Vec::new();
        for (n, feed) in [feeds[0], feeds[0], feeds[0], feeds[1]]
            .into_iter()
            .enumerate()
        {
            candidates.push(Candidate {
                id: n.to_string(),
                title: format!("Article {n}"),
                url: format!("https://publisher.invalid/{n}"),
                published: Utc::now() - chrono::Duration::hours(n as i64),
                feed,
                discovery_url: feed.url.to_owned(),
                relevance: 0,
            });
        }
        let chosen = select(candidates);
        assert_eq!(chosen.len(), 3);
        assert!(chosen.iter().any(|a| a.feed.publisher == "guardian"));
        let mut result = json!({"output":{"articles":[{"id":"a","text":"Private evidence","source":{"evidence_sha256":"hash"}}]},
            "trace":[{"input":{"articles":[{"id":"a","text":"Private evidence","source":{"evidence_sha256":"hash"}}]}}]});
        redact_evidence(&mut result);
        assert!(!result.to_string().contains("Private evidence"));
        assert_eq!(
            result["output"]["articles"][0]["source"]["evidence_sha256"],
            "hash"
        );
        Ok(())
    }
}
