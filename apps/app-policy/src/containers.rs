//! The two containers, derived from one policy.
//!
//! [`IsolateSettings`] is what the widget that mounts the app applies to its
//! splash isolate at creation — the same four knobs the isolate already has,
//! plus the two budgets ADR 0002 phase 4 adds. [`SessionProfile`] is what the
//! kernel is asked for when the app wants an agent. Both come from the same
//! [`AppPolicy`], which is the point: one declaration, two containers, no way
//! for them to disagree.
use crate::policy::AppPolicy;
use serde::Serialize;
use std::path::{Path, PathBuf};

/// What the host applies to the app's splash isolate.
#[derive(Clone, Debug, PartialEq, Eq, Serialize)]
pub struct IsolateSettings {
    /// Reported by `host.capabilities()` inside the isolate AND checked by
    /// every host service before it acts (phase 2).
    pub capabilities: Vec<String>,
    /// The isolate's own network module is granted only when the app has the
    /// capability and at least one host to reach.
    pub allow_net: bool,
    /// Whole-jail ceiling in bytes.
    pub storage_quota: u64,
    /// May this isolate raise a prompt.
    pub host_prompts: bool,
    /// Cumulative script instructions for the app's session.
    pub instruction_budget: u64,
    /// Heap ceiling for the isolate.
    pub memory_bytes: u64,
    /// The jail's directory, under the host's app-data root.
    pub jail_root: PathBuf,
    /// Exactly the hosts the isolate may reach, on every network path.
    pub hosts: Vec<String>,
}

/// What the kernel is asked for: a session that can reach no more than the
/// app itself can. Serialises into the shape the kernel's profile takes.
#[derive(Clone, Debug, PartialEq, Eq, Serialize)]
pub struct SessionProfile {
    /// `<app id>.agent`, so a session is traceable to the app in every log.
    pub session_id: String,
    /// The permission profile mode, as the kernel names it.
    pub mode: &'static str,
    /// The only directory the session may write: the app's own jail.
    pub workspace: PathBuf,
    /// Nothing outside the workspace is readable unless listed here, and
    /// nothing is listed here today.
    pub read_allow_paths: Vec<PathBuf>,
    pub tools: Vec<String>,
    pub hosts: Vec<String>,
    pub max_iterations: u32,
    pub token_budget: u64,
    /// Every ledger write this session makes carries this tag (phase 5).
    pub provenance: Provenance,
}

#[derive(Clone, Debug, PartialEq, Eq, Serialize)]
pub struct Provenance {
    pub app_id: String,
    pub app_version: String,
}

impl AppPolicy {
    /// The app's jail: one directory per app under the host's data root.
    pub fn jail_root(&self, app_data_root: &Path) -> PathBuf {
        app_data_root.join(&self.app_id)
    }

    /// The settings for this app's isolate.
    pub fn isolate_settings(&self, app_data_root: &Path) -> IsolateSettings {
        IsolateSettings {
            capabilities: self.capabilities.iter().cloned().collect(),
            // A granted `net` with no hosts reaches nothing, so the module is
            // not handed over at all: less surface, same behaviour.
            allow_net: self.allows("net") && !self.hosts.is_empty(),
            storage_quota: self.storage_bytes,
            host_prompts: self.may_prompt,
            instruction_budget: self.instruction_budget,
            memory_bytes: self.memory_bytes,
            jail_root: self.jail_root(app_data_root),
            hosts: self.hosts.iter().cloned().collect(),
        }
    }

    /// The agent session for this app, when it asked for one. The workspace
    /// is the app's jail, so the agent's reach is the app's reach.
    pub fn session_profile(&self, app_data_root: &Path) -> Option<SessionProfile> {
        let agent = self.agent.as_ref()?;
        Some(SessionProfile {
            session_id: format!("{}.agent", self.app_id),
            mode: agent.profile.as_kernel_mode(),
            workspace: self.jail_root(app_data_root),
            read_allow_paths: Vec::new(),
            tools: agent.tools.iter().cloned().collect(),
            hosts: self.hosts.iter().cloned().collect(),
            max_iterations: agent.max_iterations,
            token_budget: agent.token_budget,
            provenance: Provenance { app_id: self.app_id.clone(), app_version: self.version.clone() },
        })
    }
}
