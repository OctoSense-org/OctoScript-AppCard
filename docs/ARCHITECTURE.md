# Architecture

octos-one is an **agent operating system on a phone**. Instead of hand-coded
screens, a routing agent (the **AMA**) dispatches each user intent to one of
several concurrent **app agents**, and the chosen agent *generates* a live,
full-screen card as its answer. This doc explains the moving parts and how a
single request flows through them.

- [1. The mental model](#1-the-mental-model)
- [2. Decision → activation (the control plane)](#2-decision--activation-the-control-plane)
- [3. The a2app memory (how an agent knows an app)](#3-the-a2app-memory-how-an-agent-knows-an-app)
- [4. The Splash card + live data binding](#4-the-splash-card--live-data-binding)
- [5. Transport: the embedded octos kernel](#5-transport-the-embedded-octos-kernel)
- [6. Component map (where things live)](#6-component-map-where-things-live)

---

## 1. The mental model

Three kinds of actor, all running at once as independent **octos sessions**
(each is a stateful server-side conversation with its own context window):

| Actor | Role | Renders UI? |
|---|---|---|
| **AMA** (Activity Management Agent) | Classifies each intent into a *domain* and decides which app agent takes the screen. | No — its answer is a one-line routing decision. |
| **App agent** — one per domain (weather, stock, news) | Owns generation for its domain. Emits a `runsplash` card as its streamed answer. | Yes — when activated, its card is the screen. |

Why separate sessions per app? Each agent's context stays **dedicated** to its
domain (the weather agent never sees stock chatter), which keeps generations
focused and lets the AMA prune/route without cross-talk. They share one *display
surface* (the phone screen); the AMA's decision selects whose card is on it.

This lives on top of a **Layer-3 multi-session client** (`app/src/main.rs`:
`App.apps: Vec<AppRecord>`, `App.foreground`) — a small window-manager over N
sessions, where `foreground` indexes the visible one.

---

## 2. Decision → activation (the control plane)

The end-to-end flow for one request (all identifiers are real code in
`app/src/main.rs`):

```
 clear_chat()
   └─ creates 3 domain app agents (AppRecord{domain:"weather"/"stock"/"news"})
      + the AMA session (ama_session).                      // all concurrent

 submit_prompt(text)                                         // user hits send
   └─ splash mode: send text ONLY to the AMA (router prompt),
      hold it in `pending_intent`. No app agent runs yet.

 AMA streams its decision  ──▶  ama_text accumulates
 AgentEvent::TurnComplete for ama_prompt
   └─ parse the leading token → app_id  ("weather" | "stock" | "news")
   └─ route_to_app(app_id, decision):
        • find apps[i] where domain == app_id
        • foreground = i                       // this agent takes the screen
        • send app_splash_router_for(domain, intent) to apps[i].session
        • apps[i].current_prompt = pid

 apps[i] streams its runsplash card  ──▶  CHAT_DATA (the shared surface)
 AgentEvent::TurnComplete for that pid  →  card committed, is_streaming=false
```

Key pieces:

- **`AMA_SYSTEM_PROMPT`** primes the AMA as a *router* ("reply one line: the app
  id + a brief reason; do NOT generate UI or fetch anything"). Because
  `session/open` carries no per-session system-prompt field, the persona is
  **inlined into the AMA's message** each turn (`submit_prompt`).
- **`route_to_app()`** is the activation hook — "the AMA decided X, so make X's
  agent the foreground and hand it the intent". Unknown domain (`none`) → nothing
  renders. If the AMA turn errors, the held intent falls back to weather.
- **`app_splash_router_for(domain, intent)`** is the domain-locked generation
  prompt: "generate a *{domain}* card, follow `apps/{domain}/app.md`, bind live
  data with the matching `sys.*` helper, do NOT generate any other type."
- **Foreground guard**: streaming `AgentEvent`s carry a `prompt_id`, not a session
  id. `app_of_prompt(prompt_id)` maps it back to an app; a *background* app's
  events are badged, never written to the visible `CHAT_DATA`.

> **Latency note.** This serializes: AMA (~7 s) then generation (~30 s). A
> speculative fan-out (fire all agents immediately, AMA prunes losers) would cut
> that, but a domain agent can't generate for an out-of-domain intent (a weather
> agent has no city for "TSLA"), so AMA-first dispatch was chosen. Because we
> *don't* speculate, the user never briefly sees the wrong app's output.
>
> Three cuts to that latency (roadmap): **(1)** route on the AMA's *first line*
> instead of waiting for the full turn (the app id is the leading token); **(2)**
> when an app is already foreground and the input just *refines* the current card
> ("make it dark", "change to Tokyo"), send it **straight to the foreground agent**
> and skip the AMA entirely; **(3)** a two-tier AMA — a cheap local rules/embedding
> classifier for the confident majority ("AAPL", "top news"), falling back to the
> LLM AMA only on ambiguous input.

---

## 3. The a2app memory (how an agent knows an app)

An app agent has **no app-specific code**. Everything it knows — the framework
rules, the widget vocabulary, and each app's spec + a known-good exemplar — is
**injected into its context as memory** by the octos kernel every turn.

- The source of truth is **`a2app/`** in this repo:
  ```
  a2app/
    framework.md                     global rules + which app types exist
    widgets/{sys-helpers,containers,weather-icon}.md    widget + sys.* reference
    apps/<domain>/app.md             the app spec (mandatory sections)
    apps/<domain>/exemplars/<domain>-canonical.splash   a full known-good card
  ```
- **octos assembles the tree itself.** The kernel's memory store looks for an
  `app-cards/` directory under the profile memory dir and, when present,
  concatenates the tree (in a fixed order — framework → widget helpers → each
  app's `app.md` + exemplars — with `===== <relpath> =====` delimiters) into the
  injected long-term memory *at inject time*. There is no build step and no
  generated `MEMORY.md` artifact; the `a2app/` tree is the on-disk source of
  truth. See `octos/crates/octos-memory/src/memory_store.rs` → `assemble_app_cards`.
- On the device, the tree is deployed to
  `…/octos-home/.octos/profiles/_main/data/memory/app-cards/`. The memory provider
  assembles + prepends it to the model prompt, up to
  `config.memory.max_inject_tokens` (in `_main.json`).

**Why injection and not file-reading?** An earlier design had the agent `read_file`
the specs (via `OCTOS_SKILLS_PATH`), and a sub-agent relay that copied the result
— the copy truncated long cards. Direct injection + direct generation (the app
agent emits the card itself) removed both failure modes.

> ⚠️ **Token budget.** The assembled tree grows with each app. If it exceeds
> `max_inject_tokens`, octos truncates the *tail* — silently dropping the last
> app. Keep the cap above the tree's token estimate (we run 16000).

---

## 4. The Splash card + live data binding

A card is a **`runsplash` fenced block** of Makepad **Splash DSL** — a declarative
widget tree (`View`, `RoundedView`, `Label`, `Image`, `GradientYView`, …). The
renderer is the `Splash` widget (`aichat/widgets/src/splash.rs` in the framework
fork), which evaluates the DSL in an isolated script VM and builds live widgets.

### Live data is bound by the DSL, not written by the LLM

The card calls **data helpers** as a `Label`'s text; the *runtime* fetches the
real value at render time:

```
Label{ text: "$" + sys.stock("AAPL", "price") }        // Yahoo Finance
Label{ text: sys.weather(48.85, 2.35, "current.temperature_2m") + "°" }  // open-meteo
Label{ width: Fill text: sys.news(0, "title") }         // Hacker News
```

The LLM writes `sys.stock("AAPL", "price")` — it never types `317.31`. The value
is correct to the cent because it was fetched, not recalled.

### How a helper works (framework: `platform/src/script/res.rs`, `widgets/src/splash.rs`)

1. The `sys.*` helper builds a URL and calls **`Cx::script_data_fetch(url)`**.
2. `script_data_fetch` is a **URL-keyed side-table** (`data_fetches`): if the URL
   is already loaded it returns the bytes; otherwise it fires ONE async HTTP
   request (deduped by URL, with a browser `User-Agent`) and returns `None`.
3. The response is routed in `platform/src/script/std.rs`
   (`handle_script_network_events`): store the bytes, `redraw_all()`.
4. Back in the helper, **`json_pluck(bytes, path)`** navigates the JSON (dot-path,
   numeric segments index arrays) and returns the field as a string — or `"—"`
   while still loading.

### The one non-obvious part: re-evaluation on data arrival

A `Label` bakes its text **once**, at eval time. So the first render bakes `"—"`,
and a plain `redraw_all()` won't change it (unlike an `Image`, which re-polls its
resource handle every repaint). The fix:

- A global **`DATA_FETCH_EPOCH`** is bumped whenever any fetch newly loads.
- The `Splash` widget records the epoch at eval time and, on its per-frame pump,
  **re-evaluates the whole body** when the epoch changes — so `sys.*` re-runs and
  now returns the loaded value. `eval_body` never bumps the epoch, so it settles
  (≤1 re-eval per fetch) and can't loop.
- `body_binds_live_data()` gates this to cards that actually call a `sys.*` data
  helper (keep it in sync when you add a helper).

That's why a card shows `—` for a moment, then fills in with real numbers.

### Two ways to extend — and only one needs a rebuild

There are **two distinct extension axes**, and conflating them causes a card to silently render
`—`:

| Axis | What it is | Rebuild? |
|---|---|---|
| **App package** — `a2app/apps/<domain>/` (spec + exemplars) | Teaches an agent a new card *using capabilities that already exist*. Pure content. | **No.** Regenerate `MEMORY.md`, redeploy. |
| **Data capability** — a `sys.*` helper in `widgets/src/splash.rs` (framework fork) | A shared, native primitive that fetches a live data source (e.g. `sys.stock`, `sys.stockbar`). | **Yes** — it is native code compiled into the APK. |

So a new card that reuses `sys.weather`/`sys.stock`/`sys.news` is content-only. But a card that
needs a *new* live data source (or a new shaping of one — e.g. the intraday chart needed a new
`sys.stockbar` helper) is a **framework change**: add the helper, keep `body_binds_live_data()`
in sync, rebuild. Think of the `sys.*` helpers as a **shared standard library**, not per-app glue.
See **[ADDING-AN-APP-CARD.md](ADDING-AN-APP-CARD.md)** for the content path.

---

## 5. Transport: the embedded octos kernel

On Android there is **no separate server process**. The octos kernel is bundled
into the APK as `liboctos.so` and run **in-process over stdio**:

- `app/src/main.rs::stdio_spawn()` execs `liboctos.so serve --stdio` (NDJSON
  JSON-RPC on stdin/stdout) from the app's `nativeLibraryDir` (the only
  exec-able location on Android), with `HOME` = the app data dir.
- The app talks the **octos ui-protocol** (`session/open`, `turn/start`, streamed
  `UiNotification`s) via `crates/octos-app-transport` (stdio transport).
- Each app agent / the AMA is a `session/open` on this one kernel; concurrency is
  the kernel's (per-session turn actors).
- The `app-cards/` memory tree, the per-profile config (`_main.json`, incl. the
  LLM provider + key), and the skill read-zone all live under `octos-home/` in the
  app's data dir.

Desktop builds instead talk to a normal `octos serve` over WebSocket (same
protocol); Android is stdio.

---

## 6. Component map (where things live)

| Concern | Location |
|---|---|
| AMA persona / routing prompt | `app/src/main.rs` — `AMA_SYSTEM_PROMPT` |
| Domain agents + activation | `app/src/main.rs` — `clear_chat`, `submit_prompt`, `route_to_app`, `app_splash_router_for`, `AppRecord.domain` |
| Multi-session window manager | `app/src/main.rs` — `App.apps`, `foreground`, `app_of_prompt`, `focus_session`, `switch_to_app` |
| App-agent generation prompt | `app/src/main.rs` — `APP_SPLASH_ROUTER` |
| Transport (stdio/ws, ui-protocol) | `app/crates/octos-app-transport`, `app/src/backend/octos_ui.rs` |
| Splash renderer + `sys.*` helpers | **framework fork** `widgets/src/splash.rs` |
| Async data-fetch engine | **framework fork** `platform/src/script/res.rs` (`script_data_fetch`, `DataFetch`, `DATA_FETCH_EPOCH`), `std.rs` (response routing) |
| App-card definitions (memory) | `a2app/` → deployed as `app-cards/`; octos assembles it in `octos-memory/src/memory_store.rs` (`assemble_app_cards`) |
| Agent runtime | `liboctos.so` from [`octos-org/octos`](https://github.com/octos-org/octos) |

Next: **[ADDING-AN-APP-CARD.md](ADDING-AN-APP-CARD.md)** to add a new app type, or
**[BUILDING-ANDROID.md](BUILDING-ANDROID.md)** to build and run.
