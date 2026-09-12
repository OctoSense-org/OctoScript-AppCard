# Native macOS mobile preview validation

Studio RunItem `octos-macos-mobile`, release build **63**, runs a standalone
native Makepad window at **440 × 841 logical pixels**. It connects over stdio
to the current native Octos core, `2.0.3-rc.11`, and generates through the
dedicated `qwen3.8-27b` endpoint with DFlash2. The existing serving connection
called “H200” currently reaches an **H100 80GB** host.

The core, profile, user store and cursors are isolated under
`~/Library/Application Support/Octos One Mobile`. See the
[launch guide](../../../tools/OCTOS-MACOS.md) for reproducible setup.

| Request | Native UI inspected | Generation completion | Output tokens |
| --- | --- | ---: | ---: |
| Tokyo weather, Taskplan light | 318 widgets; forecast, imagery, native kit buttons | 11.394 s | 1,785 |
| AAPL stock, Camo | 252 widgets; native StockPlot and KitTabBar | 10.928 s | 2,015 |
| Technology news, Atro light | 316 widgets; headline rows and native kit buttons | 10.000 s | 1,611 |

These are individual end-to-end generation measurements from this session,
not an inference benchmark or latency guarantee. Screenshots and structured
widget trees are recorded for each app. The model reported usage cumulatively
within the session; the table uses each completed turn's token delta.
[Sanitized generation metrics](generation-metrics.json) retain the raw timing
events and exclude estimated cost and session identifiers.

## Interaction checks and repairs

- Weather: Studio opened the native KitFormField, typed `London`, and committed
  it. Five results remained visible, including two with the identical label
  `England, United Kingdom`. Selecting Add saved London, closed the editor,
  and displayed its live forecast. The earlier template keyed results by
  `label`, causing duplicate-key rejection and an empty card. It now declares
  and keys on each search result's stable `id`.
- macOS renderer: the SunArc shader's local `half` conflicted with Metal's
  scalar type. Renaming it to `half_span` removed the observed compilation
  error. Final-build logs contained no shader compilation errors.
- Stock: Studio switched 1M to 1W in build 62 and the chart data and selected
  tab changed. Build 63 retained the saved 1W preference and rendered the
  native StockPlot correctly.
- News: Studio opened a headline's detail page. The AI topic button added a
  feed in build 62; that saved topic remained present after the build 63
  restart. Opening the headline detail was repeated in build 63.
- Input: real macOS keyboard input preserved a complete English search with
  spaces. Pinyin had initially consumed Space as a composition commit; no
  keyboard workaround was added. Final interactions used Studio Click,
  TypeText, Return, WidgetQuery, WidgetTreeDump, WidgetSnapshot and Screenshot.
- Launcher: fixed the optional reapproval migration identifier to use the
  numeric Studio build ID. Temporary keyboard diagnostics were removed.

## Screenshots

[Weather](weather/screen.png) · [London search results](weather-london/screen.png) ·
[Saved London](weather-saved-london/screen.png) · [Stock](stock/screen.png) ·
[News](news/screen.png) · [News detail](news-reader/screen.png) ·
[Ready to test](ready-to-test/screen.png)

Each capture directory includes its widget dump, snapshot, query and generated
native widget source. `weather-london-before-fix` preserves the failed case.
`weather-initial`, `weather-city-edit` and `news-ai` are intermediate captures;
the primary weather, stock, news and detail captures are from build 63.

This validates the tested mobile layout and app workflows on macOS. It does
not establish exact Android behavior for system permissions, soft keyboards,
gestures, notifications or every generated card. Live stock fields unavailable
from the provider remain displayed as an em dash.

## Follow-up: news Read and Back

The build 63 news check above reached the generated story details only.
It did not verify the external article webview or the return path. Both were
reported broken afterward and have now been exercised in Studio build 67.

Those initial checks used Studio's direct Makepad event injection. A repeated
report that the webview Back still failed exposed a separate native-input
gap: the Cocoa mouse delegates used the cached last movement position for
clicks. WKWebView can consume movement events, leaving that position stale
when the user clicks the Makepad toolbar. The delegates now read each mouse
down/up event's actual location before drag queries or widget dispatch.
The launcher also offers AppKit-backed Studio clicks to exercise this path.

The macOS platform drains its pending operations in reverse order. A browser
layout update could therefore arrive before the browser was created and be
dropped, leaving the new webview unattached. The update path now creates the
browser if needed. The reader uses a WebCard whose native browser bounds
follow its layout, below a separate 56-point Makepad toolbar. Back explicitly
detaches the browser and restores the story details. Clearing the chat,
switching apps or submitting a new request also closes the reader.

Checks performed through the persistent Studio bridge:

- Opened an OpenAI news story and selected Read. WKWebView reported a
  completed navigation with its article title, no error, visible attachment,
  and a 433 × 740 logical-pixel viewport. Its native snapshot shows the
  actual article body.
- Clicked the reader's Back and verified the details and Read button returned.
- Reopened the same article, captured the native content again, and returned
  to details. This covers reattachment when the URL is already cached.
- Clicked the detail card's Back and verified Top Stories returned.
- Opened Read once more, submitted a new request through the composer, and
  verified that the reader overlay was hidden and the native browser detached.

Evidence: [actual article](news-webview-fixed/native-webview.png),
[reader toolbar](news-webview-fixed/screen.png),
[Back to details](news-back-to-detail/screen.png),
[Back to headlines](news-back-to-list/screen.png),
[reopened article](news-webview-reopened/native-webview.png), and
[native navigation and detach events](webview-events.json).
Each interaction capture includes the Studio widget snapshot, tree and query.

Studio's GPU screenshot does not include native WKWebView pixels. Browser
evidence is therefore retained separately using WebKit's native snapshot API;
an empty browser region in `screen.png` is not evidence of a blank web page.
The optional one-shot capture request is described in the
[launch guide](../../../tools/OCTOS-MACOS.md#native-browser-evidence).
