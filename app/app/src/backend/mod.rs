//! Agent implementations for octos-app.
//!
//! For M1 only `OctosUiAgent` is wired in (see `octos_ui.rs`). The aichat
//! `StatelessBackendAdapter` is intentionally not used — Octos serves all
//! LLMs server-side; the client picks a profile, not a backend.

mod app_prompt_cache;
pub mod octos_ui;

pub use octos_ui::OctosUiAgent;
