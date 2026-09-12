# Responses continuation and navigation reference size

9 September 2026. Native Mac app, Makepad Studio builds 27 and 28, H100
`qwen3.8-27b`, SGLang `0.0.0.dev1+g5f55db35e`.

## Response-ID continuation

The explicit `api_type: "responses"` route now enables session-scoped
`previous_response_id` continuation. The native Mac/SGLang launcher selects
that route by default; its request file can still select `api_type: "openai"`.
Custom Responses routes retain the live context-window probe: the app observed
262,144 tokens during both native runs.

The caller retains full history. The provider compares hashes of the normalized
input items and request settings against its last completed response in the same
session. An exact extension sends only the new input items and response ID.
Changed history, changed settings, compaction, a different session, anonymous
requests, and one-shot compaction calls cannot accidentally inherit that state.
Provider instances isolate endpoints and models. The local index is bounded at
128 sessions and stores hashes rather than copies of prompt text.

Only successfully completed text responses become checkpoints. Interrupted,
failed, cancelled, and truncated responses cannot publish a new ID. Tool-call
turns remain explicit because message repair can rewrite their IDs; an earlier
text checkpoint can still abbreviate their preceding history. Standard Responses
tool streaming events now preserve the association between parallel calls and
their argument deltas. Cached input and cache-write usage are accounted separately
from uncached input, matching the existing Chat Completions accounting contract.

A definite missing-response 400/404 retries once with the full history. Other
HTTP failures are returned without an automatic replay. These IDs identify
stored conversation state; SGLang independently matches token prefixes against
its available KV cache. An ID does not pin GPU memory.

## Native measurements

Studio drove converter → weather → stock → news → navigation against a local
transparent observer. A one-request proxy fault returned a missing-response 404
for the stock continuation; it did not delete or flush any state on the GPU.
The real app retried with full history and displayed the AAPL card. Its next
news request continued from the newly returned response ID.

| Observation | Result |
| --- | ---: |
| Stock continuation request body | 75,096 bytes |
| Full-history retry for the same stock request | 374,131 bytes |
| Body reduction from continuation | 79.93% |
| Stock retry server KV reuse | 98,304 / 98,414 tokens |
| Subsequent news request body | 75,101 bytes |
| Subsequent news server KV reuse | 100,352 / 100,514 tokens (99.84%) |

The roughly 75 KB remainder is primarily the tool schemas, which this SGLang
Responses path consumes from each request. It is not another copy of conversation
history. The app-to-backend reference reuse layer also remains active: stock,
news, and navigation follow-ups sent 387, 392, and 418 bytes respectively on that
hop. The first converter generation invoked a harmless shell echo before emitting
its card, which invalidated the app reference cache and caused weather to resend
the reference. Initial-session reference misses also appeared in the direct smoke
run. Response-ID continuation does not fix those separate reference-cache events.

This is a request-size and correctness check, not a controlled latency benchmark.
The observed news and navigation requests completed inference but showed long UI
delivery/presentation delays in the observer run. News reached L0 admission; a
fully rendered navigation screen was not verified before stopping that build.
No end-to-end loading-speed improvement is claimed from this trial.

Build 28 then connected directly to H100 without the observer and rendered both
Tokyo weather and AAPL stock with live values. See [weather](direct-weather.png)
and [stock](direct-stock.png). Generation completion telemetry was 8.27 s and
11.42 s, respectively; these are not times for every data source to finish loading.
The observer is stopped and the native app remains on the direct Responses route.

## Navigation is six host capabilities plus its UI

The measurements below describe the tested workspace, which also contained
independent, uncommitted navigation behavior changes. Those changes remain
separate from this commit. Applied to the tracked baseline alone, the comment
cleanup reduces the exemplar from 38,116 to 13,248 bytes without changing any
executable lines; that baseline has 16 source declarations and five maps.

The 41,392-byte navigation reference contained 24,001 bytes of full-line comments,
17,350 bytes on executable lines, and 41 bytes of blank lines. Most comments were
historical implementation discussions. The original annotated file is preserved
as [nav-before.card](nav-before.card).

The prompt exemplar now measures **17,412 bytes**, a **57.93% reduction**. Its
executable lines are identical; the level/model headers remain. All eleven card
files total **77,890 bytes**, and the first weather app prompt is **126,703 bytes**.
These are UTF-8 text bytes, not GPU KV-memory sizes or token counts.

The card uses six host capabilities:

| Capability | Runtime responsibility |
| --- | --- |
| `sys.gps` | Device position |
| `sys.search` | Place search and geocoding |
| `sys.route` | Route duration and distance |
| `sys.step` | Navigation instruction, remaining distance, ETA |
| `sys.locale` | Locale |
| `sys.prefs` | Saved mode, home, and work |

Its 20 source declarations bind these capabilities for the named/GPS origin,
direct/one-stop journey, and route legs. Eight guarded `Map` declarations cover
planning and driving variants; they do not all render simultaneously. The
remaining text declares endpoint editing, search results, preferences, controls,
copy, and layout. Geocoding, routing algorithms, GPS tracking, and map rendering
already belong to the shared runtime. This change does not introduce a new
navigation API or remove navigation controls.

## Validation

22 Responses adapter tests, 8 continuation/recovery integration tests, and 4
navigation profile tests passed in release mode. The native core built in release;
the UI built and ran through the persistent Studio RunItem. Non-comment navigation
lines have the same SHA-256 before and after. Touched-file whitespace checks and
launcher Python syntax validation passed.

[Measurements](measurements.json), [wire trace](wire.jsonl),
[navigation size and executable hash](nav-size.json), [test results](tests.json),
[observer app metrics](build27-metrics.json), [direct app metrics](build28-metrics.json).
