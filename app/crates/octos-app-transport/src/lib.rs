//! octos-app-transport
//!
//! WebSocket + REST transport for UI Protocol v1. Runtime async loops live
//! behind `todo!()` for now — this pass locks the public API. See `STATUS.md`.
//!
//! Wire contract: `~/home/octos-app/03-PROTOCOL-CONTRACT.md`
//! Workstream: `~/home/octos-app/workstreams/W01-protocol-client.md`
//! Source of truth for app-facing types: `octos_core::app_ui`

pub mod capability;
pub mod cursor;
pub mod jsonrpc;
/// Transport-agnostic JSON-RPC core shared by `ws` and `stdio`.
mod proto;
pub mod rest;
pub mod stdio;
#[cfg(target_env = "ohos")]
pub mod embedded;
pub mod ws;

/// Install a logcat backend for the real `log` facade on Android. The app
/// shell's `log::` macros route through makepad's shim (visible in logcat as
/// tag `Makepad`), but this crate and `octos-app-store` log via the `log`
/// crate — which drops every record silently until a logger is installed.
/// Idempotent; no-op off Android.
#[cfg(target_os = "android")]
pub fn install_android_logger() {
    android_logger::init_once(
        android_logger::Config::default()
            .with_max_level(log::LevelFilter::Info)
            .with_tag("OctosApp"),
    );
}
#[cfg(not(target_os = "android"))]
pub fn install_android_logger() {}

use std::collections::BTreeMap;

use octos_core::app_ui::{
    AppUiBackendEvent as UiNotification, AppUiGetDiffPreview as DiffPreviewGetParams,
    AppUiInterruptTurn as TurnInterruptParams, AppUiOpenSession as SessionOpenParams,
    AppUiReadTaskOutput as TaskOutputReadParams, AppUiRespondApproval as ApprovalRespondParams,
    AppUiSubmitPrompt as TurnStartParams,
};
use octos_core::ui_protocol::{
    ApprovalRespondResult, DiffPreviewGetResult, RpcError, SessionOpenResult,
    TaskOutputReadResult, TurnInterruptResult, TurnStartResult, UiCursor,
};
use serde::{Deserialize, Serialize};
use tokio::sync::oneshot;
use url::Url;

pub use capability::{
    Capabilities, APPROVAL_TYPED_V1, PANE_SNAPSHOTS_V1, SESSION_WORKSPACE_CWD_V1,
};

/// Bearer token wrapper. Local newtype rather than pulling `secrecy` in for
/// one field — `Debug` redacts; the inner string is only reachable via
/// `expose()`.
#[derive(Clone, Serialize, Deserialize)]
pub struct SecretString(String);

impl SecretString {
    pub fn new(s: impl Into<String>) -> Self {
        Self(s.into())
    }
    pub fn expose(&self) -> &str {
        &self.0
    }
}

impl std::fmt::Debug for SecretString {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str("SecretString(***)")
    }
}

/// Tenant / profile id (`X-Profile-Id` header; mirrors `profile_id` on
/// `SessionOpenParams`, see octos-core ui_protocol.rs:546).
#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct ProfileId(pub String);

impl ProfileId {
    pub fn new(s: impl Into<String>) -> Self {
        Self(s.into())
    }
}

/// Opaque server-issued file handle for `/api/files/{handle}`.
#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct FileHandle(pub String);

/// Top-level transport configuration. `base_url` is the http(s) origin; the
/// transport derives the WS URL by swapping the scheme. The server's actual
/// granted capabilities arrive via `TransportEvent::CapabilityNegotiated`.
#[derive(Debug, Clone)]
pub struct TransportConfig {
    pub base_url: Url,
    pub bearer: SecretString,
    pub profile_id: ProfileId,
    /// Last-applied cursor; `None` means "subscribe live, no replay".
    pub cursor: Option<UiCursor>,
    /// When set, per-session replay cursors are persisted to this JSON file via
    /// [`cursor::FileCursorPersist`], so they survive a transport re-spawn / app
    /// restart (W08/W04). `None` = in-memory only (cursors reset on reconnect).
    pub cursor_file: Option<std::path::PathBuf>,
    pub requested_capabilities: Capabilities,
    /// Per-session workspace cwd to request during `session/open`.
    pub workspace_cwd: Option<String>,
    /// When set, the agent uses the **stdio** transport — it spawns this
    /// `octos` binary as `<program> <args…>` (typically `serve --stdio`) and
    /// speaks NDJSON JSON-RPC over the child's stdin/stdout instead of dialing
    /// a WebSocket. `base_url` / `bearer` are then unused; the child is a
    /// trusted local process and capabilities default to `stdio_defaults`
    /// server-side. `None` selects the WebSocket transport.
    pub stdio: Option<StdioSpawn>,
}

/// How to launch the local `octos` process for the stdio transport.
#[derive(Debug, Clone)]
pub struct StdioSpawn {
    /// Path to the `octos` executable (on Android, the bundled native lib —
    /// the only location `untrusted_app` may exec from).
    pub program: std::path::PathBuf,
    /// Arguments, e.g. `["serve", "--stdio"]`.
    pub args: Vec<String>,
    /// Extra environment for the child (e.g. `HOME` pointing at a config/auth
    /// dir that resolves the LLM key — so the app never holds the secret).
    pub env: Vec<(String, String)>,
    /// Working directory for the child, if any.
    pub cwd: Option<std::path::PathBuf>,
}

/// Commands the rest of the app sends to the transport.
/// Lifecycle commands report through `TransportEvent`; the rest carry a
/// `oneshot` reply.
#[derive(Debug)]
pub enum OutboundCommand {
    /// Open / resume a session (see octos-core ui_protocol.rs:543).
    OpenSession(SessionOpenParams),
    /// Open a session WITHOUT the reconnect-replay cursor bracket. Used when
    /// switching to a *different* session (sidebar resume): the connection's
    /// in-memory cursor belongs to the previous session and the server
    /// rejects a `session/open` whose `after` cursor references another
    /// session. Also resets the shared cursor so later replays track the
    /// newly-opened session.
    OpenSessionFresh(SessionOpenParams),
    /// Fetch the session list over the wire (`session/list` — the M12 D-5
    /// replacement for the retired `GET /api/sessions`). The reply surfaces
    /// as `TransportEvent::SessionsListed`.
    ListSessions,
    /// Reload an existing session's chat history (`session/hydrate`,
    /// UPCR-2026-009; include=["messages"]). The reply surfaces as
    /// `TransportEvent::SessionHydrated` with the raw result value.
    HydrateSession { session_id: String },
    /// Begin a turn (see octos-core ui_protocol.rs:552).
    StartTurn(TurnStartParams),
    /// Abort a turn; idempotent on already-completed turns
    /// (see octos-core ui_protocol.rs:559).
    InterruptTurn(TurnInterruptParams),
    /// Send an approval decision (see octos-core ui_protocol.rs:572).
    SendApprovalResponse {
        params: ApprovalRespondParams,
        reply: oneshot::Sender<Result<ApprovalRespondResult, RpcError>>,
    },
    /// Fetch a parsed unified diff preview (see octos-core ui_protocol.rs:628).
    FetchDiffPreview {
        params: DiffPreviewGetParams,
        reply: oneshot::Sender<Result<DiffPreviewGetResult, RpcError>>,
    },
    /// Read task output (see octos-core ui_protocol.rs:634).
    RequestTaskOutput {
        params: TaskOutputReadParams,
        reply: oneshot::Sender<Result<TaskOutputReadResult, RpcError>>,
    },
    /// Voluntary disconnect — the task drains and exits.
    Disconnect,
}

/// Events the transport emits.
#[derive(Debug)]
pub enum TransportEvent {
    /// Connection state machine transition.
    ConnectionState(ConnectionState),
    /// Durable, cursor-bearing notification (W01 § "Ephemeral vs durable
    /// routing"). The store treats these as commits.
    DurableNotification {
        payload: UiNotification,
        cursor: Option<UiCursor>,
    },
    /// Ephemeral notification — currently just `message/delta`
    /// (see octos-core ui_protocol.rs:1304). Never replayed, never committed.
    EphemeralNotification { payload: UiNotification },
    /// Lifecycle RPC reply (`OpenSession` / `StartTurn` / `InterruptTurn`).
    /// Mirrors octos-core's `UiRpcResult` (see octos-core ui_protocol.rs:970).
    RpcResult(LifecycleResult),
    /// RPC error for a request we issued. `request_id` is the JSON-RPC id
    /// we generated.
    RpcError {
        request_id: String,
        method: String,
        error: RpcError,
    },
    /// Capability negotiation result, emitted once per `session/open`.
    CapabilityNegotiated(Capabilities),
    /// Reply to `OutboundCommand::ListSessions` — the raw JSON array from
    /// `session/list` (same rows the retired `GET /api/sessions` returned).
    SessionsListed { sessions: serde_json::Value },
    /// Reply to `OutboundCommand::HydrateSession` — the raw
    /// `SessionHydrateResult` JSON (decoded by the backend, which owns the
    /// session-key context for routing it into the chat store).
    SessionHydrated {
        session_id: String,
        result: serde_json::Value,
    },
}

/// Typed lifecycle RPC results.
#[derive(Debug, Clone)]
pub enum LifecycleResult {
    SessionOpen(SessionOpenResult),
    TurnStart(TurnStartResult),
    TurnInterrupt(TurnInterruptResult),
}

/// Connection state machine (W01 § Architecture & implementation plan).
/// `Idle → Dialing → Handshaking → Live ↔ Reconnecting → ReplayApplying → Live`,
/// terminating in `Failed` once the cumulative reconnect budget runs out.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum ConnectionState {
    Idle,
    Dialing,
    /// Socket up, `session/open` sent, awaiting response.
    Handshaking,
    Live,
    /// Socket dropped, backoff in progress.
    Reconnecting { attempt: u32 },
    /// Server is replaying ledgered notifications.
    ReplayApplying,
    /// Cumulative reconnect budget exhausted. Task exits.
    Failed,
}

/// Per-session capability request (re-exported for tests).
#[derive(Debug, Clone, Default)]
pub struct CapabilityRequest {
    pub flags: BTreeMap<String, bool>,
}
