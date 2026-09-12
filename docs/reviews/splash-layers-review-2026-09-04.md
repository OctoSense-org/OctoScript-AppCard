**Splash L0–L3 design and implementation review — completed 2026-09-04**

Follow-up: [fixes and validation](splash-layers-fixes-2026-09-04.md). The findings and evidence below describe the original reviewed snapshot.

The separation between a constrained card language, theme components, a shared node model, and native rendering is useful. The current implementation does not preserve its advertised contracts across those boundaries. Two issues should block exposing this path to untrusted generated cards and external data: an admitted L1 expression can abort the host process, and a live value can change which declared event a tap dispatches. Other confirmed failures affect arithmetic, component composition, state identity, provenance, and completeness of rendering.

This completes the unfinished work in `/tmp/splash-layers-review-20260904` and `/tmp/splash-layers-vm-probe`. I read the earlier observations, rebuilt the probes against the current checkout, reproduced their principal results, and extended them through the actual theme kit, app node walker, backend translator, and local event dispatcher. The resulting [evidence JSON](splash-layers-review-2026-09-04-evidence.json) and [reproduction harness](splash-layers-probes/README.md) are retained here rather than depending on temporary files.

This is a continuation of the UI/layer review, separate from the [earlier workflow-language review](splash-language-review-2026-09-04.md). Its standalone VM fixes are present in the reviewed `splash/` checkout. They do not automatically fix the independently vendored app VM.

**Scope and the two meanings of “level.”**

The four-stage rendering stack under review is:

```text
card source → checker / realizer / kit::lower
            → trusted theme .splash functions
            → app VM and walker → shared splash_node::UiNode
            → backend translator → native widget DSL
```

The language's capability levels are a different axis. [The enum](../../splash/crates/splash-ui-l0/src/lib.rs#L63) contains L0, L1 and L2. L0 is admitted; explicitly declared L1 admits arithmetic; L2 is classified but refused. There is no defined L3 capability profile in the inspected specification or checker, and a `# level: L3` card is refused. This review covers the four rendering stages and the existing capability-level design; it does not invent an L3 language contract. The standalone workflow profile is also a sibling profile, not the implementation of UI L2.

| Area | Actual boundary reviewed |
| --- | --- |
| Card language | `splash-ui-l0`: checking, arithmetic, realization, identity, dispatch, patching, closure reports |
| Theme kit | `kit::lower`, default palette, derivation file, `_kit.splash`; actual emitted calls |
| Node production | App's `aichat` VM, `l0_eval` walker, shared `splash-node` attributes; reference evaluator build compatibility |
| Backend | Production `l0_widgets::to_dsl`, tap parsing and emitted field callbacks; host handling of realization reports |

The snapshot is octos-one `6e0c625`, `splash` **`de2233f`**, `splash-makepad` `b82cf19`, `aichat` `4e75fe9`, and `makepad` `2783fdc`. The evidence contains full revisions and source hashes. Production code was not changed. P1 denotes a blocker for the intended untrusted-input use; P2 denotes a correctness defect or an unresolved contract that consumers must account for. These are review priorities, not vulnerability scores.

| Priority | Finding | Confirmed consequence |
| --- | --- | --- |
| P1 | 1. Arithmetic tree depth is not bounded | A valid 40 KB L1 card aborts realization with stack overflow |
| P1 | 2. Event JSON contains unescaped live data | A row's value redirects `pick` to the declared `reset` event |
| P2 | 3. Lowering changes missing-value semantics | Missing and zero-division results become `NaN` and `inf` |
| P2 | 4. Component arguments discard operand semantics | Factoring an expression or predicate into a component changes its result |
| P2 | 5. L0's no-facts claim overlooks state provenance | A model-authored state initial renders as a measured value |
| P2 | 6. L1's sampling rule is not a constant detector | A valid polynomial is rejected; a constant partial formula is accepted |
| P2 | 7. Duplicate-key repair creates another collision | Toggling one row expands two rows |
| P2 | 8. Partial results become successful renders | Valid deep content disappears; host paths ignore truncation and runtime diagnostics |
| P2 | 9. The reference renderer is out of sync | Its current `Attrs` initializer does not compile |
| P2 | 10. Closure fingerprints omit semantic inputs | Changing a loop key changes identity without changing the digest; already documented debt |

**1. P1 — Bound the resulting arithmetic tree, not only parser recursion.**

The probe generates this card with 20,000 occurrences of `a`:

```text
# level: L1
state a { shape: number, initial: 3 }
view root Surface { TextHero(value: a+a+a+…+a) }
```

The complete generated input is below the 256 KiB source limit. The release checker returns `valid=true`, level L1. Calling `realize` in a separate release process then terminates with `SIGABRT` and a stack-overflow diagnostic. The harness prints `checked: true` before the abort and never reaches its post-realization marker.

[`parse_additive` and `parse_term`](../../splash/crates/splash-ui-l0/src/lib.rs#L2484) build a left-deep `Operand::Expr` chain in a loop. Their depth counter is increased only while parsing each right operand, then decreased, so it does not measure the depth accumulating on the left. [Expression evaluation](../../splash/crates/splash-ui-l0/src/lib.rs#L2703) and several other traversals recurse through that tree. Realizer node/work limits count UI elements and loop iterations, not these native calls. This contradicts [§9.2 and §9.6](../../splash/docs/ui-profile-l0.md#L1440), which rely on a bounded expression tree.

Reject expressions exceeding an explicit AST depth/node budget, or represent and traverse them iteratively with charged work. Include validation, evaluation, dependency collection, lowering, and destruction in the bound. Keep a subprocess regression for long flat additive and multiplicative chains; nested-parenthesis tests alone do not cover this failure.

**2. P1 — Serialize event payloads as data at the moment they are available.**

The admitted `live_tap` fixture declares a text state, `pick { selected: set($value) }`, `reset { selected: clear }`, and a row with `on_tap: pick, value: q.name`. Its lowering concatenates `sys.stock("N", "name")` between JSON string delimiters. With the fixture adapter returning:

```text
x","e":"reset","v":"
```

the actual kit produces:

```text
l0:{"e":"pick","k":"root/Row#0","v":"x","e":"reset","v":""}
```

The production `parse_tap` returns event **`reset`**, not `pick`. Dispatching that parsed target through the real UI dispatcher changes seeded state `CURRENT` back to its declared initial `KEEP`; `applied=true`. The ordinary-value control dispatches `pick` and stores `Normal name`. An ordinary name containing quotes produces invalid JSON and an unreadable tap.

The cause is [live tap construction](../../splash/crates/splash-ui-l0/src/lib.rs#L10742) combined with [permissive JSON object parsing](../../app/app/src/app/l0_widgets.rs#L697). Field callbacks independently build their target through the same unsafe concatenation of typed text; see [`on_return` and `on_change`](../../app/app/src/app/l0_widgets.rs#L916). Evaluating the emitted `on_return` target expression reproduces all three cases: normal text preserves `pick`, quoted text is unreadable, and crafted text changes the parsed event to `reset`.

Use structured event arguments through the bridge, or serialize the complete envelope with a real JSON encoder after inserting the payload. Bind the event and instance to the control; external text must never supply envelope fields. Rejecting duplicate fields is useful defense in depth, but does not repair ordinary quoted or backslash-containing input. Tests must round-trip quotes, escapes, newlines, Unicode and duplicate-field-shaped strings through both live taps and fields.

This demonstrates redirection to **another event already declared by the card**, not acquisition of an arbitrary capability. The probe uses a deterministic local quote adapter and an in-memory state store; it performs no network or durable-store operation.

**3. P2 — Preserve the arithmetic contract through the kit and backend VM.**

With `q.last=4`, `q.open=3`, the admitted expression `q.last / (q.open - 3)` realizes to `Missing`. The actual lowered source, kit, app walker and translator produce text **`inf`**. With `q.open` absent, `q.last + q.open` realizes to `Missing` and the same path produces **`NaN`**. A finite conversion control produces the expected `39.2`, so the mismatch is not a general inability to execute the kit.

[`apply_op`](../../splash/crates/splash-ui-l0/src/lib.rs#L2719) rejects nonfinite answers and zero divisors. [`render_expr`](../../splash/crates/splash-ui-l0/src/lib.rs#L6832) emits raw VM operators instead. The real [`sys.num`](../../aichat/widgets/src/splash.rs#L1095) returns NaN for missing text, and [`text_prop`](../../app/app/src/app/l0_eval.rs#L302) formats nonfinite values as strings. Parenthesizing the expression preserves grouping, but does not preserve these semantics.

Carry an explicit numeric-or-missing value through lowering, or lower to bounded helpers implementing the same operations and missing propagation. Finite checks belong before numeric values become text or shader parameters. Add conformance cases for every operator, missing input, wrong type, zero divisor and overflow across realization and the actual rendering path.

**4. P2 — Component arguments must evaluate the same way as inline operands.**

Both of these L1 cards are accepted, but only the inline one realizes to 8 when `q.last=4`:

```text
component Hero(v: number) { view TextHero(value: v) }
view root Surface { Hero(v: q.last * 2) }
```

```text
view root Surface { TextHero(value: q.last * 2) }
```

The component form realizes to `Missing` and lowers to an em dash. [`component`](../../splash/crates/splash-ui-l0/src/lib.rs#L6080) sends the expression to `literal_of`, whose expression case returns JSON null. It also treats a predicate as a lookup of only its left path. At L0, passing `n == 2` into a boolean prop and guarding on that prop hides a `Rule` even when `n` is 2; the equivalent inline guard emits the rule.

Use a common typed operand resolver for arguments, props and guards, and retain any live-expression binding needed after component expansion. Test that extracting an inline subtree into a component preserves values, visibility and live dependencies. Component extraction should not change language semantics.

**5. P2 — State must carry provenance if no-facts is an enforced property.**

This L0 card is accepted and renders `1547` with no source or user input:

```text
state n { shape: number, initial: 1547 }
view root Surface { TextHero(value: n) }
```

The direct `TextHero(value: 1547)` control is refused. Routing the same literal through state therefore bypasses the stated structural no-facts guarantee. [State initialization](../../splash/crates/splash-ui-l0/src/lib.rs#L5754) preserves the literal, and an allowed path into a data argument no longer distinguishes it from a measured or user-entered value.

There are legitimate numeric initial states, such as a quantity input. That makes a blanket ban on numeric state the wrong repair. Distinguish authored defaults, user input and source-derived data, and decide which provenance each role accepts. Until that contract exists, describe the checker as rejecting direct literals in selected positions; it does not prove that a displayed number came from the world. A legal expression cannot establish that a formula is truthful either.

**6. P2 — Three fixed evaluations cannot prove dependence on inputs.**

The claim in [§9.3](../../splash/docs/ui-profile-l0.md#L1498) that five arithmetic operators cannot express a nonconstant answer equal at all three probes is false. The admitted operator set directly expresses:

```text
(q.last - 2) * (q.last - 5) * (q.last - 11)
```

It is zero at the checker's three assignments and varies elsewhere. The checker rejects it as ignoring its inputs. Conversely:

```text
(q.last - 2) / (q.last - 2) * 1547
```

is accepted and realizes to 1547 at `q.last=4`. It is constant wherever defined. [`expr_is_constant`](../../splash/crates/splash-ui-l0/src/lib.rs#L2773) returns false immediately on any missing probe result, and the first assignment makes this denominator zero.

Remove the proof claim. Use sound simplification or an explicitly limited symbolic analysis for cases it can establish, leaving unknown cases unknown. Sampling can be an advisory heuristic; it should neither certify provenance nor reject valid formulas as a proven fabrication. Fixing the early return alone would still leave the polynomial counterexample.

**7. P2 — Duplicate-key recovery must not reuse a valid input key.**

For three source rows keyed `A`, `A`, `A#1`, the realizer produces the same instance path for rows two and three:

```text
root/for#0[A#1]/Item#0/Item
```

The first duplicate receives a diagnostic and is renamed with `#<index>`. That generated name is not reserved against keys supplied by later rows. Dispatching `toggle` using the second row's actual instance key expands both rows; the tree grows from seven nodes to nine. See [key recovery](../../splash/crates/splash-ui-l0/src/lib.rs#L6236).

Prefer refusing or explicitly omitting duplicate-key instances. If recovery is required, encode identity as a typed tuple with a distinct recovery component, not a suffix in the user's key namespace. Validate uniqueness of the final identities. The host must also surface the runtime diagnostic; the current host behavior in finding 8 makes the failure appear to be an ordinary successful render.

**8. P2 — A partial tree must remain partial across every stage.**

An L0 card containing 40 nested `Col` elements and a final `TextRow(text: "END")` is valid. Realization emits all 42 nodes with `truncated=false`. Passing the actual lowering through the kit and app walker returns a tree and backend DSL, but **`END` is absent**. A shallow control preserves it. The walker has a [separate depth limit of 32](../../app/app/src/app/l0_eval.rs#L143) and [silently skips children that return `None`](../../app/app/src/app/l0_eval.rs#L271). That also discards unknown child tags without failing the parent.

The earlier UI work-budget fix is active: a valid 100-by-100 nested collection probe stops at 8,192 nodes and reports truncation. However, [initial rendering](../../app/app/src/app/l0_card.rs#L417) and [event rendering](../../app/app/src/app/l0_card.rs#L1070) check only for the presence of a root. Runtime diagnostics and `truncated` are ignored when a root exists. The event path then prunes state using the possibly incomplete live-key set.

The patch API has an additional mismatch: after realizing a four-node tree, patching it with `max_nodes=1` returns a four-node tree with `nodes=1`, `reused=4`, and `truncated=true`. [`carry_over`](../../splash/crates/splash-ui-l0/src/lib.rs#L10258) clones an old subtree over the bounded new result without charging or recounting it. This is a patch-limit contract failure, not a claim that the default fixed-budget host can create an arbitrarily large previous tree through this example.

Use a result type that distinguishes complete, partial and failed output at each stage, and propagate diagnostics. Budget the expanded kit/node tree, not just the semantic tree. Do not mount or prune from an incomplete result as if it were complete. Patch reuse must honor the caller's limits and report actual returned size. A renderer conformance test should compare content and failure status, not merely node counts.

**9. P2 — The shared node contract needs a buildable reference consumer.**

The checked-out reference [`splash-render` evaluator](../../splash-makepad/crates/splash-render/src/eval.rs#L54) does not initialize the ten newer `Attrs` fields: `texture`, `texture_alpha`, `texture_scale`, `shadowcolor`, `shadowblur`, `shadowdx`, `shadowdy`, `family`, `tracking`, and `gradient_across`. Compiling that unchanged file against the current shared model reports Rust E0063. This source-level incompatibility remains even when the evaluator is supplied the app VM dependency in a standalone harness; it is independent of a GPU backend.

Normal `cargo metadata` for the renderer workspace fails even earlier because its local `makepad-splash/platform/script` dependency is absent from this workspace. The compile probe bypasses only that missing checkout to expose the separate attribute mismatch. It is not a successful test of the reference renderer's intended VM lineage. The app walker builds, but source inspection also shows different policies for numeric text and numeric `variant` between the two walkers.

Keep a reproducible dependency configuration and require every node consumer to compile when `Attrs` changes. Share decoding policy or run a complete normalized-tree corpus through each real VM lineage. The current [count-based conformance test](../../app/app/src/app/l0_eval.rs#L488), plus selected text/tap checks, does not establish full tree equivalence.

**10. P2 — Treat the current closure digest as incomplete metadata.**

Changing only `key x.ticker` to `key x.name` inside component `Items` preserves its reported digest, `6085664523878831398`, while changing the realized path from `[N]` to `[Nvidia]`. [`definition_digest`](../../splash/crates/splash-ui-l0/src/lib.rs#L402) does not include `key_path`. The profile [already documents](../../splash/docs/ui-profile-l0.md#L1279) this omission, view-reference omissions, the non-adversarial FNV hash, and the lack of host pin storage/comparison. This is confirmed outstanding design debt, not a newly discovered escalation bypass.

Before approval caching or durable component pinning relies on it, hash a canonical representation covering all semantic fields and the transitive referenced definitions. Keep state-schema compatibility separate from whole-definition identity. Include the language profile, catalog, kit and node-contract versions in the host's approved artifact; a component digest alone cannot pin the full rendering behavior.

**Design conclusions beyond the numbered defects.**

The constrained frontend should remain independent of the VM. Its `serde_json`-only dependency and explicit source/event declarations make the small language reviewable. But “no expression form” is a property of card syntax and realization, not a claim that the whole rendering path performs no computation or effects. Source reads, durable-write requests, trusted kit functions, `sys.*` bindings and emitted widget callbacks still need explicit host contracts. The UI checker is not a substitute for per-host authorization.

The trusted kit/renderer entry point currently calls an unbudgeted `vm.eval`. A raw `while true {}` fixture exceeded an external two-second timeout. A raw undefined call followed by a valid text object logged errors and still rendered the trailing object. These confirm the recovered observations on the app VM. **Neither raw fixture is admitted as an L0 card**, so they are not evidence that a generated L0 card can inject arbitrary VM source. They establish that a trusted-kit failure can hang or partially execute this entry point, and that a successful root is not proof of successful evaluation. Budget that boundary and make failures explicit as defense in depth.

Keep the semantic role/kit/node/backend split, but make each boundary carry typed values, status, identity and bounded diagnostics. String concatenation currently transports both content and control, while the two evaluators implement different value policies. A shared Rust struct prevents some schema drift at compile time; it cannot by itself prevent semantic drift. That distinction is visible in findings 2, 3, 4 and 9.

L1 should remain a narrowly specified arithmetic extension until those contracts hold. L2 needs its own grammar, capability/effect model, scheduling/cancellation rules and resource accounting before admission. L3 needs a definition if it is intended as a capability level; if it names the native backend, document that separately. Changing a numeric level should not silently change the trust assumptions of an artifact.

**Validation, evidence limits, and handoff.**

`cargo test --locked --release -p splash-ui-l0` passed **267 tests**: one unit test and 266 profile tests, with no failures or ignored tests. The headless probes were built with Rust 1.95.0 on macOS ARM64 in release mode. Crash and hang cases ran in separate processes with core dumps disabled and external timeouts. The evidence records commands, inputs, outputs, statuses, revisions and source hashes.

The VM probe extracts the production app walker and `sys.num`, and compiles the production backend translator. It supplies a dummy host and a deterministic `sys.stock` adapter; it does not instantiate the app's `Cx`, register the full live capability module, or launch native widgets. Field probes evaluate the exact target expression extracted from the emitted callback; they do not send a GUI event. This establishes the language, serialization and translation failures without claiming on-device validation.

The earlier partial review's crash, no-facts, missing-value, duplicate-key, patch-budget, fingerprint and raw-VM observations were reproduced. Its simple nonfinite VM probes were strengthened into actual card → kit → app-node → backend-DSL comparisons. Newly completed coverage includes component argument equivalence, accepted-card depth loss, live-payload redirection through dispatch, and reference consumer compilation. The documented fingerprint limitation remains known debt.

This does not certify native pixels, GPU safety, live network adapters, async completion ordering, durable-store atomicity, or Android/OpenHarmony parity. The reference-renderer compile failure prevents claiming cross-VM conformance. No full app build, device session, sanitizer run, Miri run or sustained fuzz campaign was performed for this continuation.

The next implementation work should proceed in this order:

1. Bound expression ASTs and repair event serialization/routing, with process-survival and no-unintended-event regressions.
2. Unify operand semantics and missing-value propagation; propagate partial/failure status through realization, decoding, patching and mounting.
3. Repair instance identity recovery and replace overstated provenance/constant-detection guarantees with enforceable contracts.
4. Restore the reference consumer, add full semantic conformance fixtures, and finish artifact/version pinning before extending the profile levels.

The review is complete. The implementation defects remain open; this handoff supplies reproducible findings and repair criteria, not fixes or release approval.
