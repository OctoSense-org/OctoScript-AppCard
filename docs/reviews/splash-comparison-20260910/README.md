# Standalone Splash and Makepad Splash

Checked September 10, 2026. `ymote/Splash` redirects to
[`splash-lang/Splash`](https://github.com/splash-lang/Splash). They share VM
ancestry, but expose different source contracts and host APIs.

## Versions and evidence

- Standalone upstream `main`: `8feae2589f55822491d9a2585caaa5510098f047`.
- Makepad upstream `dev`: `4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a`.
- Local standalone HEAD: `de2233f`; local Makepad/aichat HEAD: `4e75fe92`.
  These workspaces contain additional changes. The standalone core runtime,
  capability runtime, vendored parser, grammar and language-profile files
  checked here are byte-identical to their pinned upstream counterparts.
  The local UI-profile documentation differs from upstream.
- [Downloaded source manifest](sources.json), [17 syntax probes](syntax-results.md),
  [full probe output](probes.json), [dependency experiment](dependencies.json).

The probes execute the local standalone release runtime and its inherited
parser. The compatibility column is **not** execution in current upstream
Makepad, and parser acceptance does not establish binding availability or
semantic equivalence. Current Makepad capabilities below were checked in pinned
upstream source; no new native UI build or render was performed for this review.
The upstream compatibility document links an `examples/ddgo/app.splash` file
that was absent at the pinned Makepad revision; the current widget host and
manual were used instead.

## Syntax

| Construct | Standalone workflow v0.2 | Makepad Splash |
|---|---|---|
| Core computation | `let`, `fn`, closures, arrays, records, loops | Shared language ancestry |
| Pattern selection | `if` / `elif` / `else` | Also `match x { 1 => value, _ => fallback }` |
| Destructuring | Explicit bindings and field/index access | Also `let [a, b] = pair`, `let {a, b} = record` |
| Typed numeric literals | Canonical finite numbers with binary64 arithmetic | Also suffixed forms such as `1f`, `2i` in the broader VM/shader language |
| Statement boundaries | Newline or `;`; preflight lowers boundaries explicitly | Streaming parser; whitespace and explicit separators |
| Record fields | `{a: 1, b: 2}` or fields on separate lines | Also accepts `{a: 1 b: 2}` |
| Array elements | `[1, 2]` | Also accepts `[1 2]` |
| Array mutation | `array.push(items, value)` after `use mod.std.array` | `items.push(value)` |
| Indexed loop | `array.range(0, n)` | Inherited range operators |
| Recovery | `try { ... } catch { ... }`, cross-function recovery, no error object | Inherited `try protected fallback` with optional `ok` branch |
| UI construction | Rejected by workflow grammar | `View{...}`, `child := Label{...}`, prototype overrides, `+:` |
| Effects | Registered `tool.*` or reviewed module facades | Bindings supplied by the UI/platform host |

The array-method distinction is observable: `items.push(42)` passes workflow
syntax checking but fails at runtime with a missing-method error. Parsing does
not resolve imports or approve effects. `array.push(items, 42)` succeeds.
Canonical recovery returned 42 after an intentional missing-method failure;
the bounded range helper produced 3 for the sum of 0, 1 and 2.

Sources: [canonical grammar](https://github.com/splash-lang/Splash/blob/8feae2589f55822491d9a2585caaa5510098f047/docs/grammar.md),
[Makepad guide](https://github.com/makepad/makepad/blob/4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a/splash.md),
[Makepad parser](https://github.com/makepad/makepad/blob/4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a/platform/script/src/parser.rs).

## Capabilities

| Area | Standalone Splash | Makepad Splash |
|---|---|---|
| Workflow tools | Named capabilities, JSON contracts, call budgets, direct module facades | Application supplies bindings and policies |
| Async | Deferred tool promises and explicit host completion/resume | Promises, `.await()`, HTTP callbacks and UI event-loop integration |
| Parallel I/O | Host dispatches multiple pending external operations | Host networking/event loop can service independent requests |
| Recovery across restarts | Workflow plans, leases, checkpoints, operation ledgers and optional worker infrastructure | Application-specific orchestration |
| Native UI | L0/L1 realization to `UiNode`, Makepad DSL lowering, and component/backend integration | Direct widget DSL, layout, styling, callbacks and dynamic list rendering |
| Storage and services | Explicit bounded tools; no ambient filesystem/network APIs | Gated network, per-app jailed storage, brokered `host.request` |
| Generated-code boundary | Narrow documented grammar and bounded capability calls | Depends on installed bindings and isolate configuration |

Makepad now exposes more than the old local skill notes describe. The current
widget host enables networking per isolate, installs private storage only under
a host-assigned root, and queues service requests for the host to answer. It
also bounds widget evaluation. This review is not an OS-containment audit of
either project.

Sources: [standalone positioning](https://github.com/splash-lang/Splash/blob/8feae2589f55822491d9a2585caaa5510098f047/docs/positioning.md),
[Makepad isolate setup](https://github.com/makepad/makepad/blob/4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a/widgets/src/widget_async.rs#L393),
[private storage](https://github.com/makepad/makepad/blob/4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a/widgets/src/splash_storage.rs),
[host bridge](https://github.com/makepad/makepad/blob/4b25a1bf1ed3a1dbb1a7cfea1a030ab8c290fc5a/widgets/src/splash_host.rs).

## Three source profiles in Octos

1. Workflow Splash: `use mod.composition`, `let`, tool promises and `.await()`.
2. L0 cards: `theme`, `source`, `state`, `event`, `view`, semantic roles such as
   `Surface` and `TextTitle`. These have a dedicated parser and realizer; they
   are not raw Makepad source and L0 does not execute general script expressions.
   L1 separately adds bounded expressions.
3. Makepad Splash: native widget construction, properties, callbacks and host
   rendering. Theme/component adapters connect the semantic card tree to it.

The Splash project **does support Makepad UI through `UiNode`**. In
`splash-ui-l0`, realization creates a semantic `UiNode`; `makepad::lower`
can emit native Makepad DSL directly, while `kit::lower` emits theme-role
calls. The local `splash-makepad` integration evaluates those calls into the
renderer node model and provides `to_makepad_ui` / `to_makepad_l0_ui` to emit
native component source. A host mounts the result. This is implemented UI
integration, not merely parser compatibility. The semantic and renderer
`UiNode` types are currently distinct.

Consequently, the narrower syntax comparison above applies specifically to
the **canonical workflow entry point**, not to the entire Splash project or
its UI capabilities. Many excluded forms remain in the inherited parser;
this is a profile boundary rather than proof of a missing VM feature.

The standalone CLI does not itself install a native Makepad widget runtime. Its
Makepad compatibility entry point is intentionally separate from the workflow
grammar. The existence of the L0 UI profile does not change that boundary.
Sources: [UI profile](https://github.com/splash-lang/Splash/blob/8feae2589f55822491d9a2585caaa5510098f047/docs/ui-profile-l0.md),
[Makepad compatibility](https://github.com/splash-lang/Splash/blob/8feae2589f55822491d9a2585caaa5510098f047/docs/makepad-ui-compatibility.md).

## Parallelism and deterministic research

The existing [composition template](../../../tools/splash-research/templates/composition.splash)
starts every admitted fetch before awaiting results. In a fixture experiment,
all three requests were emitted before any reply. Replies arrived in order
C, B, A; synthesis received evidence in order A, B, C and ran only after all
three completed. No network or model was used, and this is not a latency test.

The VM expresses dependencies; the host performs I/O concurrently. The 20-app
study's [Python dispatcher](../../../tools/splash-research/composition/run.py)
uses asyncio with a four-request limit around the Rust VM bridge. The earlier
research runner uses Rust futures. Standalone `pump_up_to(n)` itself loops over
queued synchronous handlers; batching alone does not parallelize blocking I/O.

This makes scheduling and permitted tool choices predictable. News retrieval,
model summaries and translations remain variable unless their inputs and
outputs are recorded and replayed. The high-level workflow draft format also
describes ordered steps, not an automatic DOT-style parallel DAG scheduler.

## Recommendation for Octos

Keep workflow Splash for bounded orchestration, generated L0 cards for data
binding and state, and Makepad components for presentation. Supply separate
language contracts to the model; raw Makepad compatibility acceptance must
not be used to admit generated workflow code.

For the oil app, appearance is primarily a template/component/theme issue.
Switching workflow syntax would not improve typography, spacing or hierarchy.
Makepad offers more direct presentation control, while the L0 component catalog
keeps generated cards small and predictable. Improve the reusable components
and templates before widening every generated card to raw widget code.

To repeat the syntax experiment:

```sh
cargo run --release --manifest-path tools/splash-research/Cargo.toml --bin splash-syntax-compare
```
