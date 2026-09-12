# GLM-5.3-Flash coding-plan cache test

9 September 2026, native Mac app through Makepad Studio build 29.

GLM's automatic prefix cache works with Octos. An unchanged-input control reused
197,440 of 197,478 input tokens (99.98%). Weather, stock, and news all rendered
native L0 cards during the test. The application still has a reference-retention
problem: history-normalization events invalidate its reference cache, causing
additional copies of the full reference to accumulate in the conversation.

## Route and method

The supplied credential successfully authenticated a small coding request for the
exact model `glm-5.3-flash`; the response reported the same model. The native app
then used the documented coding-plan Chat Completions endpoint:
`https://open.bigmodel.cn/api/coding/paas/v4/chat/completions`.
See [the official endpoint instructions](https://docs.bigmodel.cn/cn/coding-plan/quick-start).

A localhost observer forwarded request bodies unchanged and added authentication
only for the upstream request. It recorded sizes, timing, and the provider's raw
usage counters. Its local model listing contains the model ID verified by the
access probe, without fabricated context-window metadata. Octos reported a
1,000,000-token window through its own configuration/catalog; the server's maximum
was not independently measured.

The UI was rebuilt through the existing Studio RunItem from the working checkout,
which includes uncommitted changes. A dedicated temporary profile isolated this
test from the normal app profile. The original 126,703-byte reference prompt and
70 tool schemas were used. Weather, stock, and news were requested twice in one
session, in that order. Each native request retained the app's default sampling
settings and 16,384-token output allowance, including the model's reasoning.

This exercised Chat Completions automatic caching, not the newly added
`previous_response_id` adapter. No response ID or `prompt_cache_key` was sent.
No production provider or cache implementation was changed for this test.

## Native results

| Request | Input tokens | Cached tokens | Hit rate | LLM request | App generation | Native card |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Weather 1 | 57,543 | 0 | 0.00% | 70.55 s | 72.13 s | Rendered |
| Stock 1 | 59,584 | 57,536 | 96.56% | 48.69 s | 55.84 s | Rendered |
| News 1 | 94,209 | 59,584 | 63.25% | 42.59 s | 56.62 s | Code view after 150 s |
| Weather 2 | 128,653 | 94,208 | 73.23% | 75.85 s | 79.34 s | Rendered |
| Stock 2 | 162,853 | 128,640 | 78.99% | 36.96 s | 44.25 s | Rendered |
| News 2 | 197,478 | 162,816 | 82.45% | 51.77 s | 56.73 s | Rendered |

LLM request time is measured from the Mac observer sending the upstream request
until the response stream finishes. It includes network, server waiting, prefill,
reasoning, and output streaming. It is not GPU-only inference time. App generation
uses the app's submitted/completed lifecycle telemetry. Neither measurement means
every data source or image has finished loading. The driver also collected a
heuristic live-label readiness time; that can match a city or company name and
is deliberately not presented as complete data-loading latency.

The first request is the first observed request for this native reference, with
zero cached tokens reported; no provider cache was flushed. The sequence is a
functional/cache test, not a controlled comparison with H100 or RTX 6000. Output
length, reasoning length, and server wait times vary substantially.

## Unchanged-prefix control

After News 2 completed, its messages and tools were replayed exactly, with only
`max_tokens` reduced to 32. Hashes confirm identical messages and tools. GLM
reported 197,440 cached tokens out of 197,478 (99.9808%); the observer measured
8.59 seconds. The response intentionally ended with `finish_reason: "length"`.
This demonstrates prefix reuse, and is not a complete app-generation latency.

## Reference duplication remains

Stock 1 reused the app reference and sent only 387 bytes from app to backend.
During that turn, the backend emitted a history-normalization event reporting one
dropped message. The app then invalidated its reference state. Later normalization
events continued to report dropped messages, and subsequent requests resent the
entire reference despite it still appearing in the provider request history.

| Native request | Full reference copies in history | HTTP request body |
| --- | ---: | ---: |
| Weather 1 | 1 | 234,301 bytes |
| Stock 1 | 1 | 243,593 bytes |
| News 1 | 2 | 383,860 bytes |
| Weather 2 | 3 | 523,502 bytes |
| Stock 2 | 4 | 662,743 bytes |
| News 2 | 5 | 803,010 bytes |

The system-message hash stayed identical throughout. The provider reused the old
prefix, but each newly appended reference added roughly 32K tokens of repeated
material that had to be processed in its new position. This is separate from
provider support for caching and from the Responses continuation implementation.
The app's normalization/invalidation contract needs a follow-up fix that can
establish whether the retained reference was actually removed.

## Native presentation evidence

[Weather](weather.png) shows a temperature and forecast;
[stock](stock.png) shows the AAPL quote and chart;
[news](news.png) shows runtime-loaded headlines. Optional weather imagery and some
stock fundamentals were not populated in these captures, so they do not establish
that every source loaded successfully.

The first news response remained a CodeView after the 150-second observation
window, despite a complete `runl0` fence and successful model completion. The second
news response rendered, and its output was byte-for-byte identical to the first.
This points to an intermittent presentation/admission issue; its root cause was
not established by this cache test. The first-attempt widget tree and result are
retained alongside the successful second capture.

The model copied an older `# model: glm-5.2` comment from the reference cards.
That comment is generated source text, not evidence of a provider fallback: the
configured requests target `glm-5.3-flash`, and the access probe returned that
exact model. No fallback provider was configured.

## Artifacts

- [Measurements and source/binary hashes](measurements.json)
- [Provider wire metadata and raw usage](wire.jsonl)
- [App generation telemetry](app-metrics.json)
- [Reference copies and prefix hashes](reference-analysis.json)
- [Reference invalidation and L0 admission events](reference-and-admission-events.json)
- [First news attempt](news-first-attempt.result.json), [widget tree](news-first-attempt.tree.json)

Eight model calls were made: one access probe, six native app generations, and one
32-token cache control. Credentials and raw request histories are excluded from
this report. The supplied credential was kept in a restricted temporary file for
the observer; the observer is now stopped and that file was removed. Both launch
configuration files were restored byte-for-byte. Reopening the previous H100 app
failed because its localhost:30881 tunnel was no longer listening, so the test
app is stopped. See [restoration status](restoration.json).
