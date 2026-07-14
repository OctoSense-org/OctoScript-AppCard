//! Encode an octos LLM config (and optional server auth) into a QR code that the
//! app's composer scans to provision itself — so a user brings their own key
//! without it ever touching the repo, a keyboard, or the network.
//!
//! The QR payload is a single compact JSON object carrying ALL the info (no URL):
//!
//! ```text
//! {"llm_family":"zai","llm_model":"glm-5.2","llm_key":"sk-XXXX"
//!  [,"base_url":"...","profile":"...","token":"..."]}
//! ```
//!
//! The app parses it and writes `llm_family`/`llm_model` into the octos profile
//! config (`_main.json` → config.llm) and `llm_key` into
//! config.env_vars.<PROVIDER>_API_KEY; the optional server fields go through the
//! existing auth-provisioning path.
//!
//! Usage:
//! ```text
//! cargo run --manifest-path tools/llm-qr/Cargo.toml -- --family zai --model glm-5.2 --key sk-XXXX
//! cargo run --manifest-path tools/llm-qr/Cargo.toml -- --json '{"llm_family":"zai",...}'
//! ```
//!
//! By default it prints the JSON payload and a Unicode QR to the terminal (scan it
//! straight off the screen). NOTE: the key is a secret — treat the QR like a password.

use qrcode::render::unicode;
use qrcode::{EcLevel, QrCode};
use serde_json::{Map, Value};
use std::process::exit;

/// Provider family_id -> the env-var name octos reads the key from. Extend as the
/// octos provider registry grows (crates/octos-llm/src/registry/*). Used only for
/// the "unknown family" hint; the app does the real mapping.
const KNOWN_FAMILIES: &[&str] = &[
    "zai", "deepseek", "openai", "anthropic", "gemini", "openrouter",
];

struct Args {
    family: Option<String>,
    model: Option<String>,
    key: Option<String>,
    base_url: Option<String>,
    profile: Option<String>,
    token: Option<String>,
    json: Option<String>,
}

fn die(msg: &str) -> ! {
    eprintln!("{msg}");
    exit(1);
}

fn parse_args() -> Args {
    let mut a = Args {
        family: None,
        model: None,
        key: None,
        base_url: None,
        profile: None,
        token: None,
        json: None,
    };
    let mut it = std::env::args().skip(1);
    while let Some(flag) = it.next() {
        // Accept `--flag value` and `--flag=value`.
        let (flag, inline) = match flag.split_once('=') {
            Some((f, v)) => (f.to_string(), Some(v.to_string())),
            None => (flag, None),
        };
        let mut val = || inline.clone().or_else(|| it.next());
        match flag.as_str() {
            "--family" => a.family = val(),
            "--model" => a.model = val(),
            "--key" => a.key = val(),
            "--base-url" => a.base_url = val(),
            "--profile" => a.profile = val(),
            "--token" => a.token = val(),
            "--json" => a.json = val(),
            "-h" | "--help" => {
                print_help();
                exit(0);
            }
            other => die(&format!("error: unknown argument '{other}' (try --help)")),
        }
    }
    a
}

fn print_help() {
    println!(
        "Encode an octos LLM config as a QR code (JSON payload).\n\n\
         Options:\n  \
         --family <id>     provider family_id (zai, deepseek, openai, anthropic, …)\n  \
         --model  <id>     model_id (e.g. glm-5.2, deepseek-v4-pro)\n  \
         --key    <key>    the provider API key (stays on-device once scanned)\n  \
         --base-url <url>  optional octos server URL\n  \
         --profile  <id>   optional octos profile id\n  \
         --token    <tok>  optional server bearer token\n  \
         --json   <json>   encode a ready-made JSON payload instead\n  \
         -h, --help        show this help"
    );
}

/// Build the compact JSON payload (no spaces — QR capacity is limited).
fn build_payload(a: &Args) -> String {
    if let Some(json) = &a.json {
        // Validate it parses; re-serialize compact so spacing never bloats the QR.
        let v: Value = serde_json::from_str(json)
            .unwrap_or_else(|e| die(&format!("error: --json is not valid JSON: {e}")));
        return serde_json::to_string(&v).expect("re-serialize");
    }
    let (Some(family), Some(key)) = (&a.family, &a.key) else {
        die("error: --family and --key are required (or pass --json)");
    };
    let mut m = Map::new();
    m.insert("llm_family".into(), Value::String(family.clone()));
    m.insert("llm_key".into(), Value::String(key.clone()));
    if let Some(model) = &a.model {
        m.insert("llm_model".into(), Value::String(model.clone()));
    }
    for (k, v) in [
        ("base_url", &a.base_url),
        ("profile", &a.profile),
        ("token", &a.token),
    ] {
        if let Some(v) = v {
            m.insert(k.into(), Value::String(v.clone()));
        }
    }
    serde_json::to_string(&Value::Object(m)).expect("serialize payload")
}

/// Render a Unicode QR (half-block chars) that scans straight off a dark terminal.
fn render_qr(payload: &str) {
    let code = QrCode::with_error_correction_level(payload.as_bytes(), EcLevel::M)
        .unwrap_or_else(|e| die(&format!("error: could not encode QR (payload too long?): {e}")));
    // Dense1x2 packs two module rows per line; swapping the colors inverts it so
    // the dark background of a typical terminal becomes the QR's light field.
    let art = code
        .render::<unicode::Dense1x2>()
        .dark_color(unicode::Dense1x2::Light)
        .light_color(unicode::Dense1x2::Dark)
        .quiet_zone(true)
        .build();
    println!("{art}");
}

fn main() {
    let a = parse_args();
    let payload = build_payload(&a);
    if let Some(family) = &a.family {
        if !KNOWN_FAMILIES.contains(&family.as_str()) {
            eprintln!(
                "note: unknown family '{family}' — the app maps it via octos's \
                 provider registry (key env may fall back to {}_API_KEY).",
                family.to_uppercase()
            );
        }
    }
    println!("QR payload (treat as a secret):\n  {payload}\n");
    render_qr(&payload);
}
