//! What an installed app declares about itself.
//!
//! The manifest is the ONLY thing an app may say about its own limits, and
//! saying it is not the same as getting it: every field is a request that
//! [`crate::policy`] resolves against the host's ceilings. Unknown fields are
//! refused rather than ignored, so a manifest written for a newer host does
//! not silently run with less containment than it asked for.
use serde::{Deserialize, Serialize};

/// The manifest schema this build understands. A bundle declaring anything
/// else is refused: an older host must not guess at a newer grammar.
pub const SCHEMA: u32 = 1;

/// Every capability an app may request. The list is closed on purpose — a
/// capability that is not here cannot be granted, so adding one is a change
/// to this file and to the service that enforces it, together.
pub const KNOWN_CAPABILITIES: &[&str] = &[
    // Read and write inside the app's own storage jail.
    "storage",
    // Make requests, but only to the hosts in `network.hosts`.
    "net",
    // Raise a prompt the person answers (a permission ask, a confirmation).
    "prompt",
    // Read the shared ledger. Writing is always the app's own rows.
    "ledger.read",
    // Location, camera and clipboard reach the person's world; each is a
    // separate consent, never implied by another.
    "location",
    "camera",
    "clipboard",
];

/// The permission profiles an app's agent session may ask for. Full access is
/// absent by construction: it is an operator setting for machines they own,
/// and no manifest may name it (ADR 0002, "the rule at the boundary").
#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub enum ProfileMode {
    /// No writes at all; every write asks.
    ReadOnly,
    /// Read and write inside the workspace; anything else asks.
    WorkspaceWrite,
    /// Read and write inside the workspace; anything else is refused
    /// outright rather than asked. The right default for an unattended app.
    WorkspaceWriteNeverAsk,
}

impl ProfileMode {
    /// The string the kernel's permission profile uses.
    pub fn as_kernel_mode(self) -> &'static str {
        match self {
            ProfileMode::ReadOnly => "read-only",
            ProfileMode::WorkspaceWrite => "workspace-write",
            ProfileMode::WorkspaceWriteNeverAsk => "workspace-write-never",
        }
    }
}

#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct AppManifest {
    /// Must equal [`SCHEMA`].
    pub schema: u32,
    /// Stable identity. Also the name of the app's storage jail, so it is
    /// constrained to the characters a path component may hold.
    pub id: String,
    /// Opaque to the host, but pinned: a different version is a different
    /// bundle and must be admitted again.
    pub version: String,
    /// What a person calls it.
    pub name: String,
    pub integrity: Integrity,
    #[serde(default)]
    pub capabilities: Vec<String>,
    #[serde(default)]
    pub network: Network,
    #[serde(default)]
    pub storage: Storage,
    #[serde(default)]
    pub compute: Compute,
    /// Absent means the app gets no agent at all, which is the default.
    #[serde(default)]
    pub agent: Option<AgentSpec>,
}

/// What the bundle must hash to. The digest covers the bundle bytes as they
/// were signed; a signature, when we have one, signs this manifest.
#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Integrity {
    /// Lowercase hex blake3 of the bundle.
    pub bundle_blake3: String,
    /// Detached signature over the canonical manifest bytes, if the host
    /// requires signing. Verified by a [`crate::verify::SignatureVerifier`].
    #[serde(default)]
    pub signature: Option<Signature>,
}

#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Signature {
    /// Which key signed it, as the host knows the key.
    pub key_id: String,
    /// Lowercase hex signature bytes.
    pub value: String,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Network {
    /// The hosts this app may reach, exactly. No wildcards, no schemes, no
    /// paths: a host and nothing else, and the request is HTTPS by the time
    /// the service makes it.
    #[serde(default)]
    pub hosts: Vec<String>,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Storage {
    /// Whole-jail ceiling the app asks for. Clamped to the host's maximum.
    #[serde(default)]
    pub max_bytes: Option<u64>,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Compute {
    /// Script instructions the app may run per session, cumulative — not the
    /// per-evaluation cap, which only stops one runaway expression.
    #[serde(default)]
    pub instruction_budget: Option<u64>,
    /// Ceiling for the isolate's heap.
    #[serde(default)]
    pub memory_bytes: Option<u64>,
}

/// The agent session an app asks for. Everything here is bounded by the same
/// manifest: its workspace is the app's jail, its network is the app's hosts.
#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct AgentSpec {
    pub profile: ProfileMode,
    /// The tools the session may call. Closed list, resolved against the
    /// host's own allowlist; shell and arbitrary file tools are never in it.
    #[serde(default)]
    pub tools: Vec<String>,
    /// Model turns per request before the session stops and reports.
    #[serde(default)]
    pub max_iterations: Option<u32>,
    /// Tokens the session may spend per request.
    #[serde(default)]
    pub token_budget: Option<u64>,
}

impl AppManifest {
    /// Parse a manifest, refusing unknown fields and a foreign schema.
    pub fn parse(json: &str) -> Result<Self, String> {
        let manifest: AppManifest = serde_json::from_str(json).map_err(|e| format!("manifest is not valid: {e}"))?;
        if manifest.schema != SCHEMA {
            return Err(format!("manifest schema {} is not {}", manifest.schema, SCHEMA));
        }
        Ok(manifest)
    }

    /// The bytes a signature covers: the manifest without its own signature,
    /// serialised canonically, so the same manifest always signs the same way.
    pub fn signing_bytes(&self) -> Result<Vec<u8>, String> {
        let mut bare = self.clone();
        bare.integrity.signature = None;
        let value = serde_json::to_value(&bare).map_err(|e| e.to_string())?;
        Ok(canonical(&value).into_bytes())
    }
}

/// Canonical JSON: object keys sorted, no insignificant whitespace. Enough
/// for a stable signing input; it is not a general JCS implementation.
fn canonical(value: &serde_json::Value) -> String {
    match value {
        serde_json::Value::Object(map) => {
            let mut keys: Vec<&String> = map.keys().collect();
            keys.sort();
            let body: Vec<String> = keys
                .iter()
                .map(|k| format!("{}:{}", serde_json::Value::String((*k).clone()), canonical(&map[*k])))
                .collect();
            format!("{{{}}}", body.join(","))
        }
        serde_json::Value::Array(items) => {
            let body: Vec<String> = items.iter().map(canonical).collect();
            format!("[{}]", body.join(","))
        }
        other => other.to_string(),
    }
}
