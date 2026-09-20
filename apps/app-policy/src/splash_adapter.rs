//! Applying a resolved policy to the isolate that will run the app.
//!
//! This is ADR 0002 phase 1 in seven calls, and since phases 2 to 4 landed
//! in the runtime every one of them is ENFORCED: a card's surface gets its
//! jail and quota, its capability list (checked before any host request is
//! queued), its prompt right, its host allowlist (checked on every network
//! path, including artwork and `sys.*` data), a cumulative instruction
//! budget, and a heap ceiling — at creation, from one place. A mount path
//! that calls [`apply`] cannot forget one of them, and nothing downstream may
//! widen what it set.
use crate::containers::IsolateSettings;
use makepad_widgets::{Cx, SplashRef};

/// What [`apply`] set, for a host that wants to show it.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Applied {
    pub capabilities: usize,
    pub hosts: usize,
    pub storage_quota: u64,
    pub instruction_budget: u64,
    pub memory_bytes: u64,
}

/// Seat `settings` on `splash` before its body is evaluated.
///
/// Order matters: the jail and the quota are set before anything the app runs
/// can write; the policy (capabilities, hosts, budget) and the heap ceiling
/// come next; the isolate's own network module is granted last, so a failure
/// earlier leaves an isolate with less reach rather than more.
pub fn apply(splash: &SplashRef, cx: &mut Cx, settings: &IsolateSettings) -> Applied {
    splash.set_sandbox_dir(cx, Some(settings.jail_root.clone()));
    splash.set_storage_quota(cx, Some(settings.storage_quota));
    splash.set_host_caps(cx, settings.capabilities.clone());
    splash.set_host_prompts(cx, settings.host_prompts);
    // `Some(hosts)` is what turns enforcement on for this isolate; an empty
    // list under a granted `net` reaches nothing, as the policy resolved.
    splash.set_policy(cx, Some(settings.hosts.clone()), Some(settings.instruction_budget));
    splash.set_memory_bytes(cx, Some(settings.memory_bytes as usize));
    if let Some(mut inner) = splash.borrow_mut() {
        inner.set_allow_net(settings.allow_net);
    }
    Applied {
        capabilities: settings.capabilities.len(),
        hosts: settings.hosts.len(),
        storage_quota: settings.storage_quota,
        instruction_budget: settings.instruction_budget,
        memory_bytes: settings.memory_bytes,
    }
}
