//! What a publisher submits, and what the hub publishes.
//!
//! An index entry is one app version: the manifest that governs it, the hash
//! of the bundle it describes, who published it, where the source lives, and
//! whether it is still offered. A catalog is the signed list of entries a
//! device reads.
//!
//! The manifest is embedded rather than referenced so that what a reviewer
//! read, what the hub signed and what the device enforces are the same bytes.
use octosense_app_policy::{AppManifest, Listing};
use serde::{Deserialize, Serialize};

/// Whether this version is still offered, and why not.
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case", tag = "state", content = "reason")]
pub enum Status {
    /// Offered for install.
    Offered,
    /// No longer offered and, on a device, no longer runnable. The reason is
    /// shown to the person, so it is written for them.
    Withdrawn(String),
}

impl Status {
    pub fn is_offered(&self) -> bool {
        matches!(self, Status::Offered)
    }
}

/// One app version in the index.
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Entry {
    /// The manifest exactly as the publisher signed it.
    pub manifest: AppManifest,
    /// The listing as reviewed: what the store shows about the app. The
    /// permissions the store shows still come from the manifest.
    #[serde(default)]
    pub listing: Option<Listing>,
    /// Where the hub's own copy of the bundle lives, relative to the catalog.
    pub artifact: String,
    /// The publisher's key identity, as the hub knows it. Update continuity
    /// is checked against this.
    pub publisher: String,
    /// The publisher's public key, hex. Distributed IN the catalog because
    /// the catalog is signed: a device can then check the publisher's
    /// signature itself, and an update signed by a different key is visible
    /// rather than silent. Empty when the app was admitted unsigned.
    #[serde(default)]
    pub publisher_key: String,
    /// Where the source lives, for transparency. Never fetched at install.
    pub source: Source,
    pub status: Status,
    /// When the hub admitted it, as an ISO 8601 date.
    pub admitted: String,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Source {
    pub repository: String,
    pub commit: String,
}

impl Entry {
    pub fn app_id(&self) -> &str {
        &self.manifest.id
    }

    pub fn version(&self) -> &str {
        &self.manifest.version
    }

    /// What the person is told this app may do, in plain words, derived from
    /// the manifest rather than from anything the app says about itself.
    pub fn permissions_summary(&self) -> Vec<String> {
        let mut lines = Vec::new();
        for capability in &self.manifest.capabilities {
            lines.push(match capability.as_str() {
                "storage" => "Keep its own data on this device".to_string(),
                "net" if self.manifest.network.hosts.is_empty() => "Reach the network: nothing listed".to_string(),
                "net" => format!("Reach only: {}", self.manifest.network.hosts.join(", ")),
                "prompt" => "Ask you questions".to_string(),
                "ledger.read" => "Read your shared data".to_string(),
                "location" => "Use your location".to_string(),
                "camera" => "Use the camera".to_string(),
                "clipboard" => "Use the clipboard".to_string(),
                other => format!("Use {other}"),
            });
        }
        if let Some(agent) = &self.manifest.agent {
            let tools = if agent.tools.is_empty() { "no tools".to_string() } else { agent.tools.join(", ") };
            lines.push(format!("Run an assistant for this app ({tools}), inside this app's own data only"));
        }
        if lines.is_empty() {
            lines.push("Draw its screens, and nothing else".to_string());
        }
        lines
    }
}

/// The signed list a device reads. `signature` covers [`Catalog::signing_bytes`].
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Catalog {
    pub schema: u32,
    /// Increases with every publish; a device refuses to go backwards, so a
    /// replayed older catalog cannot un-withdraw an app.
    pub sequence: u64,
    /// When this catalog was signed, ISO 8601. The device's freshness window
    /// is measured from here.
    pub published: String,
    pub entries: Vec<Entry>,
    /// Hex ed25519 signature by the hub's working key.
    #[serde(default)]
    pub signature: Option<String>,
    /// The working key that signed it, and the anchor's certificate for it.
    #[serde(default)]
    pub key: Option<WorkingKey>,
}

/// The hub's day-to-day signing key, certified by the offline anchor. A
/// device trusts the anchor only; rotating the working key is then a signed
/// statement it already knows how to check, with no shell release.
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct WorkingKey {
    /// Hex ed25519 public key.
    pub public: String,
    /// Hex ed25519 signature by the ANCHOR over the working public key bytes.
    pub anchor_certificate: String,
}

pub const CATALOG_SCHEMA: u32 = 1;

impl Catalog {
    pub fn new(sequence: u64, published: &str, entries: Vec<Entry>) -> Self {
        Catalog {
            schema: CATALOG_SCHEMA,
            sequence,
            published: published.to_string(),
            entries,
            signature: None,
            key: None,
        }
    }

    /// The bytes the hub signs: the catalog without its signature or key, in
    /// canonical form, so the same catalog always signs the same way.
    pub fn signing_bytes(&self) -> Result<Vec<u8>, String> {
        let mut bare = self.clone();
        bare.signature = None;
        bare.key = None;
        let value = serde_json::to_value(&bare).map_err(|e| e.to_string())?;
        Ok(canonical(&value).into_bytes())
    }

    /// The offered entry for an app id, if any.
    pub fn offered(&self, app_id: &str) -> Option<&Entry> {
        self.entries.iter().find(|e| e.app_id() == app_id && e.status.is_offered())
    }
}

/// Canonical JSON: sorted keys, no insignificant whitespace.
pub(crate) fn canonical(value: &serde_json::Value) -> String {
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
        serde_json::Value::Array(items) => format!("[{}]", items.iter().map(canonical).collect::<Vec<_>>().join(",")),
        other => other.to_string(),
    }
}
