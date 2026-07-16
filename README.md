# octos-one

An **agent-OS phone client**: a native Android app where a routing brain (the
**AMA**) dispatches every request to a concurrent **app agent** that generates a
live, full-screen interactive card. Cards are written in the **Splash DSL** and
bind **real data at render time** (open-meteo, Yahoo Finance, Hacker News,
OpenStreetMap) — the LLM writes the *layout and the data bindings*, never the
numbers. When a request spans domains that no app covers, the AMA **composes a
new app on the fly** — writing its spec into memory and spinning up a fresh peer
agent to build it.

<p align="center"><em>You type "TSLA" → the AMA routes <code>stock</code> → the stock
agent takes the screen with a live quote + chart. You type "Shanghai" → the weather
agent takes over. You ask for "weather plus today's headlines in one card" → no app
covers that, so the AMA <b>writes</b> a <code>weather-news</code> app and a peer agent
builds it. One OS, many app agents, one routing brain that can grow the app set.</em></p>

## What's here

```
octos-one/
  app/          The Android client (Makepad + Rust). The AMA (router + composer),
                the multi-agent routing (decision → activation → composition), the
                Splash card renderer, and the post-generation card validator.
  a2app/        The "app-card memory" — the ONLY thing that teaches an agent an app.
                Requirements-only specs, reusable widget patterns, live-data helper
                docs, a global design system, and per-app lint rules. NO exemplars:
                every app is ASSEMBLED from the widget patterns, not copied from a
                template. octos assembles this tree at inject time (deployed as
                `app-cards/` under the profile memory dir) — no build step, no artifact.
  tools/        llm-qr/ — Rust dev tool: encode an LLM config as a QR to scan.
  docs/
    ARCHITECTURE.md        How it all fits together (read this first).
    ADDING-AN-APP-CARD.md  Add a new app type end-to-end (e.g. crypto, sports).
    BUILDING-ANDROID.md    Build the APK + deploy + run on a device.
    PROVISIONING-LLM.md    Bring-your-own-key: encode an LLM config as a QR to scan.
```

## Dependent projects (referenced, not vendored)

The app compiles against a Makepad fork and is built with the `cargo-makepad`
tool. These are large and live in their own repos:

| Dependency | Repo / branch | Why |
|---|---|---|
| **Framework fork** (the Splash engine + `sys.*` live-data helpers, the vendored plot widget, Android JNI) | [`octos-org/makepad`](https://github.com/octos-org/makepad) branch **`octos-one-framework`** | `app/` path-deps `../aichat` — this is that crate tree. |
| **Build tool** (`cargo-makepad`, native composer Java) | [`octos-org/makepad`](https://github.com/octos-org/makepad) branch **`octos-one-buildtool`** | Builds/signs the APK; bakes the Android SDK/NDK. |
| **octos kernel** (`liboctos.so serve --stdio`) | [`octos-org/octos`](https://github.com/octos-org/octos) | The agent runtime, bundled into the APK. |

See **[docs/BUILDING-ANDROID.md](docs/BUILDING-ANDROID.md)** for exactly where to
clone each and how to build.

## The idea in one diagram

```
 user intent ─▶ AMA (router + composer)
                    │  reads the injected routing list of apps
                    │
        ┌───────────┴────────── does an app cover this intent? ──────────┐
        ▼ yes                                                            ▼ no (multi-domain)
   route_to_app(id)                                          AMA COMPOSES a new app:
        │ activate + foreground                              writes apps/<a>-<b>/app.md
        ▼                                                     + lint.json into memory,
  ┌─────────────┬─────────────┬──────────┬──────────────┐    replies `compose <a>-<b>`
  ▼             ▼             ▼          ▼              ▼           │
weather      stock          news     activity   weather-activity  ▼
agent        agent          agent    agent      agent      spawn a NEW peer agent
  │            │              │         │           │       (fresh session injects
  └── runsplash DSL ── sys.weather / sys.stock / sys.news / sys.places ─┘  the new spec)
                              │                                            │
                   live fetch at render                                   ▼
                              ▼                                    it builds the app
                    full-screen live card  ◀── card validator (lint → one-shot repair)
```

Each app agent is its own octos session (dedicated context); the AMA's decision
picks which one takes the screen — or authors a new one. A composed app persists
as ordinary app-card memory, so the next matching request routes to it directly.
See **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

## What works (verified on-device, OnePlus 6)

- **Five built-in apps** — weather (immersive photo card: conditions, 7-day
  forecast, satellite + air-quality maps, detail grid), stock (top-movers list →
  tap → detail with a real line/area **chart** and client-side range switching),
  news (Hacker News list → tap → detail), activity (nearby places), and the
  composed **weather-activity** (what to do given the live weather). Data is live
  and matches the source APIs to the cent/point.
- **Assembled, not templated.** Every card is generated by the on-device model
  (glm-5.2) from a requirements spec + shared widget patterns — there are no
  full-card exemplars anywhere in memory. This generalizes: the model composes
  novel apps from the same pieces.
- **Dynamic composition.** A multi-domain intent no app covers makes the AMA
  author a new app spec (merging the parents' named design blocks, inheriting the
  primary parent's visual identity) into the app-cards tree; a fresh peer agent
  then builds it, and it persists for future requests.
- **A self-correcting pipeline.** Each app ships machine-checkable `lint.json`
  rules; a completed card that violates them triggers one automatic repair turn.
- **Live-data plane.** `sys.weather`/`sys.airquality`/`sys.stock`/`sys.stockbar`/
  `sys.stockrange`/`sys.movers`/`sys.news`/`sys.places` (+ numeric `sys.weathernum`/
  `sys.aqinum` so cards can *branch* on live values), plus a vendored **StockPlot**
  chart widget — all sharing one deduped fetch cache with bounded retries.
- **Guardrails.** A security gate refuses cards that use the low-level `net.*`
  API (cards may only read via `sys.*` + image `http_resource`); the AMA's
  spec-authoring is confined to the `apps/` subtree.

The AMA routes correctly in English and Chinese and composes new apps for
combined requests.
