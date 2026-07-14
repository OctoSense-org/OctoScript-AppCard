# octos-one

An **agent-OS phone client**: a native Android app where a routing brain (the
**AMA**) dispatches every request to one of several concurrent **app agents**
(weather, stock, news, …), each of which generates a live, full-screen interactive
card. Cards are written in the **Splash DSL** and bind **real data at render time**
(open-meteo, Yahoo Finance, Hacker News) — the LLM writes the *layout and the data
bindings*, never the numbers.

<p align="center"><em>You type "TSLA" → the AMA routes <code>stock</code> → the stock
agent takes the screen with a live quote. You type "Shanghai" → the weather agent
takes over. One OS, many app agents, one routing brain.</em></p>

## What's here

```
octos-one/
  app/          The Android client (Makepad + Rust). The AMA, the multi-agent
                routing (decision → activation), the Splash card renderer.
  a2app/        The "app-card memory": the framework rules, widget docs, and one
                spec + exemplar per app (weather / stock / news). octos assembles
                this tree itself at inject time (deployed as `app-cards/` under the
                profile memory dir) — no build step, no generated artifact.
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
| **Framework fork** (the Splash engine + `sys.*` live-data helpers, Android JNI) | [`octos-org/makepad`](https://github.com/octos-org/makepad) branch **`octos-one-framework`** | `app/` path-deps `../aichat` — this is that crate tree. |
| **Build tool** (`cargo-makepad`, native composer Java) | [`octos-org/makepad`](https://github.com/octos-org/makepad) branch **`octos-one-buildtool`** | Builds/signs the APK; bakes the Android SDK/NDK. |
| **octos kernel** (`liboctos.so serve --stdio`) | [`octos-org/octos`](https://github.com/octos-org/octos) | The agent runtime, bundled into the APK. |

See **[docs/BUILDING-ANDROID.md](docs/BUILDING-ANDROID.md)** for exactly where to
clone each and how to build.

## The idea in one diagram

```
 user intent ─▶ AMA (router)  ── classifies domain ──▶  route_to_app()
                                                            │ activate + foreground
                        ┌───────────────┬───────────────────┴──────────┐
                        ▼               ▼                              ▼
                  weather agent    stock agent                    news agent
                  (own session)    (own session)                  (own session)
                        │               │                              │
                  runsplash DSL ── sys.weather/stock/news ─▶ live fetch at render
                        └───────────────┴──────────────────────────────┘
                                         ▼
                              full-screen live card
```

Each app agent is its own octos session (dedicated context); the AMA's decision
picks which one takes the screen. See **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

## Status

Weather, stock, and news app cards are implemented and verified on-device
(OnePlus 6). Data is live (values match the source APIs to the cent/point). The
AMA routes weather / stock / news correctly in English and Chinese and activates
the matching agent.
