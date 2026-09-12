# Live news in the native Mac app

Update: [Chinese queries and composer routing](chinese-search.md) were fixed and
validated in release build 37. The original build-36 observations follow.

Validated 2026-09-09 Los Angeles / 2026-09-10 UTC through Makepad Studio,
release build 36, `octos-macos-news`. The Mac app uses RTX PRO 6000 through
`http://127.0.0.1:30881/v1`; H100 is off.

Click **Search**, enter a person, place or topic, and press Return or the search
button. **English / 中文** selects the summary language; source headlines retain
their original language. **Read article** opens the original publisher page in
the native reader, with **Back** returning to the results.

Coverage is BBC and The Guardian, preceding 72 hours, up to three usable articles.
Tech / World / Business use RSS feeds. Other queries use parallel Bing News RSS
searches restricted to those publishers. Bing tracking URLs are decoded and
validated as publisher article URLs. Search can return no results; it does not
search arbitrary publishers or older archives. Publication timestamps can reflect
publisher updates. Exact URL/title deduplication does not merge related stories.

The L0 card contains layout, actions and source declarations. The host fetches
the workflow dataset asynchronously through a loopback bridge. Source discovery
and article retrieval run in parallel where dependencies permit; a single RTX
call produces summaries in the requested language. The model does not select
tools or generate source links. Failed/partial/empty results remain explicit.

## Observed interactions

| Interaction | Submission to observed results | Result |
|---|---:|---|
| Type `Apple`, Return | 3.38 s | Three articles; relevant Apple headlines |
| Type `climate change`, Return | 4.50 s | Three articles |
| Select 中文 for climate query | 3.66 s | Three Chinese summaries |
| Read first BBC article, Back | Functional check | Reader URL matched source; Back closed reader |
| Return to cached English climate result | 0.21 s | Ready result, zero new pipeline runs |

These are individual observations on an already-open app, polled through Studio,
not medians or a cold app-launch benchmark. Fresh searches include retrieval,
model inference, validation, delivery and UI update. The time printed inside
the card is the pipeline duration of that dataset; cached display retains that
original value. It is not the duration of the latest click.

The loopback bridge caches/coalesces by query and language for 60 seconds, with
at most 32 entries and one active workflow/GPU slot. Native fetch caching also
expires lazily after 60 seconds. There is no automatic periodic refresh while
the user leaves the screen untouched. These result-cache checks do not measure
SGLang KV-cache hit rate.

Screenshots from the tested build: [English](english.png), [Chinese](chinese.png).
Private detailed query evidence and Studio snapshots are under
`/tmp/octos-live-news-native`; published pipeline evidence omits article bodies.

## Launch through Studio

With the RTX tunnel listening, write `/tmp/octos-macos-news-request.json`:

```json
{
  "model_base_url": "http://127.0.0.1:30881/v1",
  "model": "qwen3.8-27b",
  "live_news": true,
  "state_dir": "~/Library/Application Support/Octos One Live News",
  "evidence_dir": "/tmp/octos-live-news-native",
  "window_size": "440x841",
  "native_clicks": false,
  "reapprove_cards": true
}
```

Use the existing persistent Studio bridge to clear the previous build, then send
`{"RunItem":{"mount":"octos","name":"octos-macos-news"}}`. This named runnable
sets its own request path so another Studio launch profile cannot replace it.
The launcher builds the release UI and standalone workflow, starts the loopback
service on port 8767, and stops that service when the app exits. The separate
state directory preserves the user's normal profile. `reapprove_cards` requests
normal local card admission against the current runtime fingerprint after a
framework rebuild.

QA used Studio's direct input dispatch. The optional AppKit click-injection path
did not activate controls in this session and was disabled for this run. The
current native WebSocket dispatch uses window-local input coordinates while
WidgetSnapshot reports desktop coordinates; the QA driver subtracts the Window
origin. This is a Studio automation limitation, separate from user mouse input.

Validation: 14 standalone Rust tests, two L0 source/lowering tests, release
Clippy with warnings denied for the standalone tool, Python syntax checks,
and the live native interactions above. The L0 tests cover query/language
invalidation, quoted input escaping and denied endpoint/field/row access.
