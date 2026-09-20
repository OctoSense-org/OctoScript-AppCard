//! Resolving a manifest into what the app actually gets.
//!
//! Every rule here fails closed: an unknown capability, a host that is not a
//! bare host name, a tool the host does not offer, a quota above the host's
//! ceiling. A manifest asks; the host decides; the app is never consulted
//! again. This is the only place that produces [`AppPolicy`], and the two
//! containers are derived from it, never set by hand.
use crate::manifest::{AgentSpec, AppManifest, ProfileMode, KNOWN_CAPABILITIES};
use std::collections::BTreeSet;

/// The host's own ceilings. An app may ask for less and get it; asking for
/// more is clamped, not refused, because a bundle built for a roomier device
/// should still run here — just smaller.
#[derive(Clone, Debug)]
pub struct HostLimits {
    pub max_storage_bytes: u64,
    pub max_instruction_budget: u64,
    pub max_memory_bytes: u64,
    pub max_iterations: u32,
    pub max_token_budget: u64,
    /// Tools this host offers to contained apps at all. Shell, process and
    /// arbitrary-path file tools are absent from this list by design.
    pub offered_tools: Vec<String>,
    /// Whether a bundle must carry a signature to be admitted.
    pub require_signature: bool,
}

impl Default for HostLimits {
    /// Phone-sized defaults: the isolate jail's own ceiling for storage, a
    /// budget that cannot spin the UI thread for a second, and a tool list
    /// holding only what a card app legitimately needs.
    fn default() -> Self {
        HostLimits {
            max_storage_bytes: 16 * 1024 * 1024,
            max_instruction_budget: 20_000_000,
            max_memory_bytes: 64 * 1024 * 1024,
            max_iterations: 8,
            max_token_budget: 200_000,
            offered_tools: ["ledger.read", "ledger.write", "net.fetch", "storage.read", "storage.write", "card.render"]
                .iter()
                .map(|s| s.to_string())
                .collect(),
            require_signature: true,
        }
    }
}

/// What the app gets. Produced only by [`resolve`].
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct AppPolicy {
    pub app_id: String,
    pub version: String,
    pub display_name: String,
    /// Granted capabilities, sorted and deduplicated.
    pub capabilities: BTreeSet<String>,
    /// Exactly the hosts the app may reach. Empty means no network, whatever
    /// the `net` capability says.
    pub hosts: BTreeSet<String>,
    pub storage_bytes: u64,
    pub instruction_budget: u64,
    pub memory_bytes: u64,
    /// May the app cause a prompt the person has to answer.
    pub may_prompt: bool,
    /// None when the manifest asked for no agent.
    pub agent: Option<AgentPolicy>,
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct AgentPolicy {
    pub profile: ProfileMode,
    pub tools: BTreeSet<String>,
    pub max_iterations: u32,
    pub token_budget: u64,
}

impl AppPolicy {
    /// Whether a granted capability covers this action. The single question
    /// every host service asks before doing work on an app's behalf.
    pub fn allows(&self, capability: &str) -> bool {
        self.capabilities.contains(capability)
    }

    /// Whether the app may reach this host. Requires the capability AND the
    /// entry: a granted `net` with an empty list reaches nothing.
    pub fn allows_host(&self, host: &str) -> bool {
        self.allows("net") && self.hosts.contains(host)
    }
}

/// Resolve a parsed manifest against this host.
pub fn resolve(manifest: &AppManifest, limits: &HostLimits) -> Result<AppPolicy, String> {
    check_id(&manifest.id)?;
    if manifest.version.trim().is_empty() {
        return Err("manifest version is empty".into());
    }
    if limits.require_signature && manifest.integrity.signature.is_none() {
        return Err(format!("app {} is unsigned and this host requires a signature", manifest.id));
    }

    let mut capabilities = BTreeSet::new();
    for capability in &manifest.capabilities {
        if !KNOWN_CAPABILITIES.contains(&capability.as_str()) {
            return Err(format!("app {} requests unknown capability {:?}", manifest.id, capability));
        }
        capabilities.insert(capability.clone());
    }

    let mut hosts = BTreeSet::new();
    for host in &manifest.network.hosts {
        check_host(host)?;
        hosts.insert(host.to_ascii_lowercase());
    }
    // A host list without the capability is a manifest mistake, not a silent
    // grant: refuse it so the author notices before the app ships.
    if !hosts.is_empty() && !capabilities.contains("net") {
        return Err(format!("app {} lists hosts but does not request the net capability", manifest.id));
    }

    let agent = match &manifest.agent {
        None => None,
        Some(spec) => Some(resolve_agent(&manifest.id, spec, limits)?),
    };

    Ok(AppPolicy {
        app_id: manifest.id.clone(),
        version: manifest.version.clone(),
        display_name: manifest.name.clone(),
        may_prompt: capabilities.contains("prompt"),
        capabilities,
        hosts,
        storage_bytes: clamp(manifest.storage.max_bytes, limits.max_storage_bytes),
        instruction_budget: clamp(manifest.compute.instruction_budget, limits.max_instruction_budget),
        memory_bytes: clamp(manifest.compute.memory_bytes, limits.max_memory_bytes),
        agent,
    })
}

fn resolve_agent(app_id: &str, spec: &AgentSpec, limits: &HostLimits) -> Result<AgentPolicy, String> {
    let mut tools = BTreeSet::new();
    for tool in &spec.tools {
        if !limits.offered_tools.iter().any(|offered| offered == tool) {
            return Err(format!("app {app_id} requests tool {tool:?}, which this host does not offer contained apps"));
        }
        tools.insert(tool.clone());
    }
    Ok(AgentPolicy {
        profile: spec.profile,
        tools,
        max_iterations: clamp_u32(spec.max_iterations, limits.max_iterations),
        token_budget: clamp(spec.token_budget, limits.max_token_budget),
    })
}

/// An id is a path component of the app's jail, so it may not be empty, may
/// not navigate, and may not surprise a filesystem.
fn check_id(id: &str) -> Result<(), String> {
    if id.is_empty() || id.len() > 64 {
        return Err(format!("app id {id:?} must be 1 to 64 characters"));
    }
    if !id.chars().all(|c| c.is_ascii_lowercase() || c.is_ascii_digit() || c == '-' || c == '.') {
        return Err(format!("app id {id:?} may hold only lowercase letters, digits, '-' and '.'"));
    }
    if id.starts_with('.') || id.contains("..") {
        return Err(format!("app id {id:?} may not navigate the filesystem"));
    }
    Ok(())
}

/// A bare host: no scheme, no path, no port, no wildcard. The service adds
/// HTTPS; the app never names a scheme, so it cannot ask for plain HTTP.
fn check_host(host: &str) -> Result<(), String> {
    if host.is_empty() || host.len() > 253 {
        return Err(format!("host {host:?} must be 1 to 253 characters"));
    }
    if host.contains("://") || host.contains('/') {
        return Err(format!("host {host:?} must be a bare host name, with no scheme or path"));
    }
    if host.contains('*') {
        return Err(format!("host {host:?} may not use a wildcard"));
    }
    if host.contains(':') {
        return Err(format!("host {host:?} may not name a port"));
    }
    if !host.chars().all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '.') {
        return Err(format!("host {host:?} holds a character a host name may not"));
    }
    if host.starts_with('.') || host.ends_with('.') || host.contains("..") {
        return Err(format!("host {host:?} is not a well-formed host name"));
    }
    Ok(())
}

fn clamp(asked: Option<u64>, ceiling: u64) -> u64 {
    asked.unwrap_or(ceiling).min(ceiling)
}

fn clamp_u32(asked: Option<u32>, ceiling: u32) -> u32 {
    asked.unwrap_or(ceiling).min(ceiling)
}
