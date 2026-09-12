# Native Mac A2App cache and loading measurements

2026-09-09. Apple M3 Max, 128 GiB RAM, macOS 26.5. Native release app at
440 × 841 logical pixels, launched and driven through Makepad Studio's
`octos-macos-mobile` RunItem. Inference used the existing H100
`qwen3.8-27b` / SGLang + DFlash2 endpoint with a 262,144-token window.

Across five follow-ups, median time from submitting the request to the native
card appearing fell from **14.50 s to 6.76 s (53.4%)**. Server-reported token
reuse, weighted by input tokens, rose from **51.84% to 99.78%**. The baseline
compacted twice in six requests; the final run had no compaction through seven.
All six final generation/load checks completed in one model call each.

| Request, following initial Tokyo weather | Before: card appears | After: card appears | After: primary data ready | Before KV reuse | After KV reuse |
|---|---:|---:|---:|---:|---:|
| AAPL stock | 12.57 s | 6.76 s | 6.87 s | 60.48% | 99.97% |
| Technology news | 13.17 s | 6.06 s | 6.15 s | 71.99% | 99.93% |
| San Francisco weather | 16.84 s | 7.39 s | 9.18 s | 19.36% | 99.61% |
| NVDA stock | 14.50 s | 7.05 s | 7.48 s | 72.11% | 99.76% |
| News requested as business | 23.12 s | 6.32 s | 6.39 s | 19.44% | 99.65% |

Median first text fell from 7.71 s to 0.78 s. Uncached input over these five
requests fell from 388,383 tokens to 963. The initial Tokyo request still sent
the complete reference; it is excluded from the comparison because server
cache warmth differed. Its final card appeared at 7.30 s and primary data at
9.06 s. This measures generation/loading within the running app, not process
startup or a cold GPU.

## Changes

- [Session reference reuse](../../../../app/app/src/backend/app_prompt_cache.rs)
  prevents another approximately 203 KB copy of the complete A2App library
  from being appended on every request. Follow-ups send 573–607 bytes of
  request/theme guidance and retain the original library in conversation
  history. The backend and SGLang still own history and GPU KV caching.
- [Lifecycle integration](../../../../app/app/src/backend/octos_ui.rs)
  requires successful completion and intact normalization telemetry before
  reuse. It sends the full reference after reconnect/resume, compaction,
  changed reference text, failures, tool loops, missing window metadata or
  rising context pressure. Reuse is confined to local transports with the
  default compaction policy. Accounting includes the current submitted input:
  the backend's normalization event can describe history before that input.
  Structured metrics report reference hits, bytes, context estimates and usage.
- [Streaming admission](../../../../app/app/src/main.rs) holds an unclosed
  `runl0` fence before Markdown repair. Previously, repair supplied a closing
  fence and repeatedly sent incomplete ledgers through validation/rendering.
- [Native document evaluation](../../../../aichat/widgets/src/splash.rs) uses
  the existing explicit document-budget API for complete L0 cards. A measured
  repeat-news load exceeded the 64 ms frame deadline and left a blank card.
  Document loading now has a 2 s ceiling and retains the 1,000,000-instruction
  cap. Ticks and input handlers keep their existing frame budgets. A failed
  evaluation no longer starts a timer for a missing `tick()` function.

## Local live-data cache

After generating AAPL again, native clicks changed the chart from 1M → 1W →
1D → 1W. Studio observed the new bindings in 180, 208 and 179 ms respectively.
All three actions made **zero LLM requests**. The first 1W and 1D selections
each issued one chart-data request. Returning to 1W issued **zero new data
requests**, confirming reuse of the existing URL-keyed data cache. These tap
times include Studio polling and measure the binding update, not network
completion for a previously unseen range.

## Validation and scope

The measured final Studio build was 6. WidgetTreeDump, WidgetSnapshot and screenshots
confirmed native weather, stock and news cards, populated primary values and
a hidden generation overlay. The stock chart changed range and remained
rendered. No card-admission or script-budget errors occurred in this final run.
Five reference-cache regressions and eight focused generation/render/terminal
tests passed in release mode. The source tests include incomplete-fence
streaming and a large first input missing from lifecycle telemetry.

This is one baseline and one final six-request sequence against a warm shared
server, without forced KV eviction. Timing includes variable scheduling and
live API latency; it is not an isolated GPU benchmark. “Primary data ready”
requires a non-placeholder temperature, quote or headline, and does not wait
for satellite imagery or optional stock metadata. Earlier exploratory runs
exposed a stale saved-card runtime approval, a harness check that incorrectly
accepted `n/a`, and the renderer deadline failure; none are included in the
final timing table. Fresh test profiles preserved the user's normal app state.

Two existing product limitations remain visible: the news source is Hacker
News, so the business request does not establish business-specific coverage;
and the natural-language phrase “Atro light” currently produces an `atro`
theme hint, with the final news cards appearing dark. The load checks do not
claim category or theme correctness. Volume, market cap and P/E also remained
unavailable in the stock source.

## Evidence and reproduction

[Measurements and request hashes](measurements.json) include all twelve
baseline/final requests, server usage, reference-copy counts, native timing,
chart-cache observations and the final binary hash. Captures:
[weather](weather.png), [stock](stock.png), [news](news.png),
[stock range cache](stock-range-cache.png).

The private driver, Studio bridge, full snapshots and wire traces are in
`/tmp/octos-a2app-speed-20260909`. The sequence was Tokyo → AAPL → technology
news → San Francisco → NVDA → business news in one conversation. Studio
`Click`, `TypeText` and `Return` drove the actual native composer; a local
transparent proxy observed `/v1/chat/completions`. Cache percentages use
`usage.prompt_tokens_details.cached_tokens / usage.prompt_tokens`.

For a comparable rerun, use `tools/octos-macos.py` through the Studio RunItem
with a dedicated `state_dir`, the H100 `model_base_url`, and `skip_build: false`
after source edits. The launcher's optional `disable_reference_cache: true`
sets `OCTOS_A2APP_DISABLE_REFERENCE_CACHE` for diagnostic comparisons. Remote
transports and explicit compaction-threshold overrides already retain full
reference submission. No GPU serving settings were changed in this work.

After measurement, Studio build 7 relaunched the same verified binary directly
against the H100 tunnel at `http://127.0.0.1:30881/v1`. A fresh Tokyo weather
card displayed live data. The temporary request observer was stopped; the
native app remains running on the direct connection.

The subsequent [RTX PRO 6000 trial](rtx6000/README.md) repeated the native
sequence with reference reuse off/on using the same final release binary.
RTX median follow-up card time fell from 36.32 s to 11.45 s, with 99.64%
weighted KV reuse. That report includes server settings, local chart-cache
checks and restoration of the original RTX service.
