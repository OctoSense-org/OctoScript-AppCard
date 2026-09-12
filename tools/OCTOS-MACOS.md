# Native macOS mobile preview

The `octos-macos-mobile` Studio RunItem opens Octos One in a native Makepad
window at the Mate 70 Air's 440 × 841 logical viewport. It uses the same app
cards, theme kits, L0 generation, approval gate, and stdio core protocol as
the phone. Keyboard, window management, permissions, and other OS services
remain native macOS behavior; this is not an Android emulator.

## Prerequisites

Build the native core and its bundled command-line tools from this checkout:

```sh
cargo build --manifest-path octos/Cargo.toml -p octos-cli --bin octos \
  --release --no-default-features --features api,git,ast
cargo build --manifest-path octos/Cargo.toml --release \
  -p news_fetch -p deep-search -p deep-crawl -p send-email \
  -p account-manager -p clock -p weather -p smart-home
```

Provide a reachable OpenAI-compatible inference endpoint. By default the
launcher expects `http://127.0.0.1:30881/v1`, model `qwen3.8-27b`, through
an existing local tunnel to the dedicated GPU server. Tunnel credentials
belong in the operator's SSH configuration, not this launcher. This local
endpoint must accept unauthenticated requests; the profile's API key is
only a non-secret placeholder. The launcher checks `/v1/models` before
starting the UI and configures no fallback provider.

Optional overrides go in `/tmp/octos-macos-request.json`:

```json
{
  "model_base_url": "http://127.0.0.1:30881/v1",
  "model": "qwen3.8-27b",
  "window_size": "440x841"
}
```

## Launch and use

Mount this repository's `app` directory in Makepad Studio as `octos`.
Using the persistent Studio remote connection, clear the previous build
of this target, then send:

```json
{"RunItem":{"mount":"octos","name":"octos-macos-mobile"}}
```

Studio builds the release UI and opens a standalone native window. Use
the bottom `+` to open the composer, type a request, and press Return or
the send button. Examples:

- `Weather in Tokyo. Use the Taskplan light theme.`
- `Stock price for AAPL. Use the Camo theme.`
- `Latest technology news. Use the Atro light theme.`

For news, select a headline, then **Read ↗** to open the article in the
native webview. The reader's **‹ Back** returns to the story details; the
detail card's Back returns to the headlines. The reader toolbar remains
outside the native browser bounds so the web page cannot cover its button.

Select an English keyboard input source for English typing. With a Pinyin
input method active, Space may commit a composition instead of inserting
a literal space, as it does in other native text fields.

The `state_dir` override defaults to
`~/Library/Application Support/Octos One Mobile`. The core, sessions,
profile, user store, and reconnect cursors live there, independently of
the ordinary desktop configuration. Private process logs default to
`/tmp/octos-macos-generation`; do not publish them without review.

After changing UI/runtime code, clear the previous build and run the
same Studio item again. `skip_build: true` can be used only when the
existing release binary already matches the source. An optional `prompt`
automatically submits a test request on launch. `reapprove_cards: true`
forces saved cards through the current native approval gate again after
a renderer change; remove it after that validation run.

## Native browser evidence

Studio's Screenshot captures the Makepad surface, which excludes the
native WKWebView overlay. To verify the actual web page as well, set the
optional `browser_capture_dir` request field to an existing output directory
before running the Studio item. Write the exact expected final article URL
to `<browser_capture_dir>/capture-next`, then open Read through Studio.
Once that URL is loaded and attached visibly, WebKit saves `webview.png` and
consumes the request file. Redirected URLs must match their final canonical
URL. Each capture needs a new request file; leaving the app running does
not continuously capture browsing.

Retain both images together with WidgetSnapshot, WidgetTreeDump and
WidgetQuery evidence for the toolbar and browser bounds. Test Back and
reopening the same article, including after a previous reader was detached.

Set `native_clicks: true` in the launch request for macOS browser interaction
QA. Studio's primary Click then enters AppKit's event queue and native hit
testing before reaching Makepad. Ordinary Studio input goes directly to
Makepad and cannot detect a native view intercepting the click or a fault in
the Cocoa mouse delegate. Native click checks also cover a click arriving
without a preceding mouse-move event, as can happen when leaving WKWebView.
