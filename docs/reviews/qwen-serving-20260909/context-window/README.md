# Qwen context-window correction and H100 retry

Date: 2026-09-09. Model: the H100's `qwen3.8-27b`, serving
Qwen3.8-27B-FP8 with DFlash2. `/v1/models` reports `max_model_len: 262144`.

## Cause and correction

Octos Code delegates compaction to the `octos` backend. The Qwen profile uses
the `openai` provider family with a custom SGLang URL. That factory previously
skipped the runtime context probe already used by the `local` family.
The embedded catalog consequently matched the broad `qwen3` alias and budgeted
131,072 tokens. With the existing 70% policy, compaction began at 91,750
estimated tokens. Without that catalog alias, the fallback was 128,000 and
the threshold was 89,600.

The custom OpenAI registry and custom-provider factory now use the existing
authenticated runtime probe. Session opening also waits for provider readiness
before reading saved history or taking the compaction writer lock. Turns
already waited for readiness. The H100's 262,144-token window therefore gives
a threshold of 183,500 estimated tokens. The 70% policy is unchanged.

Server metadata can lower or raise the catalog budget. Explicit context
overrides retain precedence; endpoints without context metadata retain their
catalog fallback. This corrects the client's premature history rewrite;
SGLang continues to manage the GPU KV cache.

Sources:

- [OpenAI registry](../../../../octos/crates/octos-llm/src/registry/openai.rs)
- [Custom-provider factory](../../../../octos/crates/octos-cli/src/commands/chat.rs)
- [Session opening](../../../../octos/crates/octos-cli/src/api/ui_protocol_transport.rs)
- [Provider regressions](../../../../octos/crates/octos-llm/tests/openai_context_probe.rs)
- [Session-open regression](../../../../octos/crates/octos-cli/src/api/ui_protocol_tests.rs)

## Live retry

The retry uses isolated profiles and workspaces through `octos serve --solo
--stdio`, forwarding OpenAI requests to the existing H100 tunnel at
`http://127.0.0.1:30881`. It supplies two large synthetic reference blocks,
checks responses, and records server token usage and AppUI compaction events.
The corrected run additionally checks a short follow-up and backend restart.
No threshold or context-window override is supplied.

The original backend reproduced compaction on turn 2 at an estimated 125,440
tokens, with a reported threshold of 91,750. It dropped seven context items,
reducing the estimate to 62,775. The resulting request contained 83,569 prompt
tokens and reused only 3,072 cached tokens; the preceding request had reused
83,456. This is one functional comparison, not a controlled throughput benchmark.

The corrected backend retained the full history:

| Measurement | Original | Corrected |
| --- | ---: | ---: |
| Compaction threshold, estimated tokens | 91,750 | 183,500 |
| Compactions through turn 2 | 1 | 0 |
| Turn 2 request, server prompt tokens | 83,569 | 147,542 |
| Turn 2 request, cached tokens | 3,072 | 87,424 |
| Short follow-up, server prompt tokens | Not tested | 147,595 |
| Short follow-up, cached tokens | Not tested | 147,520 (99.95%) |

All three corrected turns returned the requested marker and passphrase.
After restarting the backend, the saved context still contained 125,311
estimated tokens, its transcript hash was identical, recovery was `exact`,
and the compaction count remained zero. Server prompt tokens and the client's
context estimates are different measures; the threshold applies to the latter.

Evidence: [original run](before.json), [corrected run](after.json),
[server model metadata](models.json), and [retry harness](retry.mjs).
The runs use the same reference-block inputs but have different isolated
workspace paths and generated system prompts; the original model also made
an extra request on turn 1. Compare retention and compaction, not timing.

To repeat against the existing tunnel, use a fresh label and run from the
repository root:

```sh
node docs/reviews/qwen-serving-20260909/context-window/retry.mjs \
  "$PWD/octos/target/release/octos" retry-001 --expect-full-context
```

`OCTOS_CONTEXT_RETRY_UPSTREAM` and `OCTOS_CONTEXT_RETRY_ROOT` optionally change
the upstream URL and temporary output root. The harness creates only isolated
test profiles, uses synthetic input, and checks history after a process restart.

## Local installation

The verified release executable was installed atomically at
`~/.local/bin/octos`, the `octos` resolved from this shell and
used by a normal Octos Code stdio launch. It reports `2.0.3-rc.11
(02e773ea 2026-09-09)` and matches the tested workspace executable byte for
byte. The desktop launcher also points to that workspace executable.

The previous installed executable is backed up at
`~/.local/share/octos/backups/20260909-context-window/octos`.
See [installation hashes](installation.json) and [original binary hashes](binary-before.json).
Existing processes were left running; restart Octos Code to load the new
backend. The live retry above used a fresh process and separately verified
reopening its saved session.

## Validation

- `cargo test -p octos-llm --release --all-targets`: passed, including the three
  new integration tests (which failed against the original factory).
- `cargo test -p octos-cli --release --lib custom_provider_tests`: four passed.
- `cargo test -p octos-cli --release --lib session_open_snapshot`: four passed,
  including the actual open RPC with delayed provider readiness and over 100K
  of saved history.
- `cargo build -p octos-cli --release --bin octos`: release executable built.

The source workspace had existing changes. They were preserved; no commit or
GPU-service configuration change was made for this correction.
