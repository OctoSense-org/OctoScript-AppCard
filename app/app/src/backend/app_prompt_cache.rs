//! Reuse the complete A2App reference already accepted in a local session.
//! The backend still owns history and KV caching; this avoids appending another
//! copy of the same library to that history for every user request.
use std::collections::HashMap;
use makepad_widgets::log;

use octos_core::{ui_protocol::TurnId, SessionKey};

const HEADER: &str = "You ARE the app agent and you OWN the whole flow:";
const END: &str = "===== END REFERENCE =====";
const RESPONSE_RESERVE: usize = 32_768;
const FOLLOWUP: &str = "Use the complete A2App framework, language, catalog, L0 app cards and page compositions already provided in this conversation. Pick the ONE app for the current request and emit exactly one complete ```runl0 fenced block, with no prose. Keep every required section and bind live values through declared sources; never invent facts or styling primitives.\n\n";

#[derive(Default)]
struct SessionReference {
    reference: Option<String>,
    context_tokens: Option<usize>,
    window: Option<usize>,
    threshold: Option<usize>,
}

struct PendingReference {
    session: SessionKey,
    reference: Option<String>,
    normalized: bool,
    input_estimate: usize,
}

#[derive(Default)]
pub(super) struct AppPromptCache {
    sessions: HashMap<SessionKey, SessionReference>,
    pending: HashMap<TurnId, PendingReference>,
}

impl AppPromptCache {
    pub fn clear(&mut self) {
        self.sessions.clear();
        self.pending.clear();
    }

    pub fn forget(&mut self, session: &SessionKey) {
        self.sessions.remove(session);
        self.pending.retain(|_, p| &p.session != session);
    }

    pub fn prepare(
        &mut self,
        session: &SessionKey,
        turn: &TurnId,
        text: &str,
        enabled: bool,
    ) -> (String, bool) {
        if self.sessions.len() >= 64 && !self.sessions.contains_key(session) {
            self.clear();
        }
        let state = self.sessions.entry(session.clone()).or_default();
        let parts = text
            .starts_with(HEADER)
            .then(|| text.split_once(END))
            .flatten();
        let (sent, hit, reference) = if let Some((reference, request)) = parts {
            let followup = format!("{FOLLOWUP}{request}");
            // Use half the reported window, below the backend's default 70%
            // threshold, and reserve another 32K for output/runtime updates.
            // An observed tighter compaction threshold takes precedence.
            let budget = state
                .window
                .map(|window| (window / 2).min(state.threshold.unwrap_or(usize::MAX)));
            let fits = state
                .context_tokens
                .zip(budget)
                .is_some_and(|(tokens, budget)| {
                    tokens
                        .saturating_add(followup.len())
                        .saturating_add(RESPONSE_RESERVE)
                        < budget
                });
            let hit = enabled && fits && state.reference.as_deref() == Some(reference);
            if !hit {
                log::info!("A2App reference miss: enabled={enabled} fits={fits} reference_matches={} context_tokens={:?} window={:?} threshold={:?}",
                    state.reference.as_deref() == Some(reference), state.context_tokens, state.window, state.threshold);
            }
            if hit {
                (followup, true, None)
            } else {
                (text.to_owned(), false, Some(reference.to_owned()))
            }
        } else {
            (text.to_owned(), false, None)
        };
        self.pending.insert(
            turn.clone(),
            PendingReference {
                session: session.clone(),
                reference,
                normalized: false,
                // Lifecycle telemetry can describe history BEFORE this input.
                // Bytes/3 exceeds the backend's character heuristic for this text.
                input_estimate: sent.len().div_ceil(3).saturating_add(4),
            },
        );
        (sent, hit)
    }

    pub fn context(&mut self, session: &SessionKey, tokens: usize, intact: bool) {
        let state = self.sessions.entry(session.clone()).or_default();
        state.context_tokens = Some(tokens);
        if !intact {
            state.reference = None;
        }
        for pending in self.pending.values_mut().filter(|p| &p.session == session) {
            pending.normalized = intact;
            if !intact {
                pending.reference = None;
            }
        }
    }

    pub fn window(&mut self, session: &SessionKey, window: usize) {
        let state = self.sessions.entry(session.clone()).or_default();
        if state.window.is_some_and(|old| old != window) {
            state.reference = None;
        }
        state.window = (window > 0).then_some(window);
    }

    pub fn compacting(&mut self, session: &SessionKey, threshold: usize) {
        self.invalidate(session);
        self.sessions.entry(session.clone()).or_default().threshold = Some(threshold);
    }

    pub fn invalidate(&mut self, session: &SessionKey) {
        let state = self.sessions.entry(session.clone()).or_default();
        state.reference = None;
        state.context_tokens = None;
    }

    pub fn complete(&mut self, turn: &TurnId, success: bool, output_tokens: Option<usize>) {
        let Some(pending) = self.pending.remove(turn) else {
            return;
        };
        let state = self.sessions.entry(pending.session).or_default();
        if !success || !pending.normalized || output_tokens.is_none() {
            state.reference = None;
            state.context_tokens = None;
            return;
        }
        if let Some(reference) = pending.reference {
            state.reference = Some(reference);
        }
        // Include submitted input as well as output. If a backend reports an
        // input-inclusive projection, double counting only causes a cache miss.
        state.context_tokens = state.context_tokens.map(|tokens| {
            tokens
                .saturating_add(pending.input_estimate)
                .saturating_add(output_tokens.unwrap().saturating_mul(2))
        });
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn prompt(reference: &str, request: &str) -> String {
        format!("{HEADER}\n{reference}\n{END}\nUser request: {request}")
    }
    fn seed(cache: &mut AppPromptCache, session: &SessionKey) {
        let turn = TurnId::new();
        assert!(
            !cache
                .prepare(session, &turn, &prompt("full library", "Tokyo"), true)
                .1
        );
        cache.context(session, 55_000, true);
        cache.window(session, 262_144);
        cache.complete(&turn, true, Some(2_000));
    }

    #[test]
    fn app_prompt_cache_reuses_confirmed_reference_across_app_requests() {
        let mut cache = AppPromptCache::default();
        let session = SessionKey("one".into());
        seed(&mut cache, &session);
        let (sent, hit) = cache.prepare(
            &session,
            &TurnId::new(),
            &prompt("full library", "AAPL, Camo theme"),
            true,
        );
        assert!(hit);
        assert!(sent.contains("AAPL, Camo theme"));
        assert!(sent.contains("```runl0"));
        assert!(!sent.contains("full library"));
        assert!(
            !cache
                .prepare(
                    &SessionKey("two".into()),
                    &TurnId::new(),
                    &prompt("full library", "News"),
                    true
                )
                .1
        );
    }

    #[test]
    fn app_prompt_cache_resends_after_changes_pressure_compaction_or_reconnect() {
        let session = SessionKey("one".into());
        for case in [
            "changed",
            "pressure",
            "compacted",
            "reconnect",
            "missing_telemetry",
            "disabled",
        ] {
            let mut cache = AppPromptCache::default();
            seed(&mut cache, &session);
            let mut text = prompt("full library", "News");
            match case {
                "changed" => text = prompt("updated library", "News"),
                "pressure" => cache.context(&session, 100_000, true),
                "compacted" => cache.compacting(&session, 183_500),
                "reconnect" => cache.forget(&session),
                "missing_telemetry" => cache.window(&session, 0),
                _ => {}
            }
            let (sent, hit) = cache.prepare(&session, &TurnId::new(), &text, case != "disabled");
            assert!(!hit, "{case}");
            assert_eq!(sent, text, "{case}");
        }
    }

    #[test]
    fn app_prompt_cache_never_trusts_failed_or_truncated_reference() {
        let session = SessionKey("one".into());
        for (success, intact) in [(false, true), (true, false)] {
            let mut cache = AppPromptCache::default();
            let turn = TurnId::new();
            let text = prompt("full library", "Tokyo");
            cache.prepare(&session, &turn, &text, true);
            cache.context(&session, 55_000, intact);
            cache.window(&session, 262_144);
            cache.complete(&turn, success, Some(2_000));
            assert!(!cache.prepare(&session, &TurnId::new(), &text, true).1);
        }
    }

    #[test]
    fn app_prompt_cache_preserves_tighter_backend_threshold_and_plain_chat() {
        let session = SessionKey("one".into());
        let mut cache = AppPromptCache::default();
        cache.compacting(&session, 80_000);
        seed(&mut cache, &session);
        let text = prompt("full library", "News");
        assert!(!cache.prepare(&session, &TurnId::new(), &text, true).1);
        let ordinary = "Explain this code. ===== END REFERENCE =====";
        assert_eq!(
            cache.prepare(&session, &TurnId::new(), ordinary, true),
            (ordinary.into(), false)
        );
    }

    #[test]
    fn app_prompt_cache_accounts_for_input_missing_from_lifecycle_projection() {
        for (bytes, expected_hit) in [(203_000, true), (400_000, false)] {
            let mut cache = AppPromptCache::default();
            let session = SessionKey("one".into());
            let turn = TurnId::new();
            let text = prompt(&"x".repeat(bytes), "Tokyo");
            cache.prepare(&session, &turn, &text, true);
            cache.context(&session, 1, true);
            cache.window(&session, 262_144);
            cache.complete(&turn, true, Some(2_000));
            assert_eq!(
                cache.prepare(&session, &TurnId::new(), &text, true).1,
                expected_hit
            );
        }
    }
}
