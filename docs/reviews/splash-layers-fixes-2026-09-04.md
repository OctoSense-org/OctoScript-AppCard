Follow-up: the remaining gaps are addressed in the [state, approval and native-rendering report](splash-layers-gaps-2026-09-05.md). This file preserves the earlier validation snapshot.

**Splash layer review fixes — 2026-09-04**

Implemented the runtime repairs from the [completed review](splash-layers-review-2026-09-04.md) and corrected the specification where it claimed guarantees the checker does not establish. The [original evidence](splash-layers-review-2026-09-04-evidence.json) is preserved; [post-fix evidence](splash-layers-fixes-2026-09-04-evidence.json) records the repaired behavior.

| Finding | Resolution |
| --- | --- |
| 1. Unbounded arithmetic AST | Bound the resulting AST, including flat additive/multiplicative chains. Component substitution also charges every copied expression node to the realization work budget and bounds expanded depth. |
| 2. Event redirection | Encode runtime values with a JSON string serializer. Field callbacks reconstruct routing metadata from parsed fields, including keys containing `$$`. Reject duplicate envelope fields and invalid field types. |
| 3. Arithmetic lowering | Emit finite-or-missing operations at every expression join. Missing inputs, zero divisors and intermediate overflow propagate an em dash. Numeric widget attributes reject nonfinite values. |
| 4. Component operands | Resolve expressions and both predicate operands in the caller's scope. Preserve scalar live bindings and expression shape through component parameters. |
| 5. State provenance | Correct §4: selected positions require bindings, while numeric authored defaults remain legal. State does not currently distinguish authored, user-entered and measured values; acceptance is not a factual-provenance proof. |
| 6. Constant sampling | Replace fixed samples with limited structural constant analysis. Accept the varying polynomial and reject the reproduced constant partial formula. Unknown expressions remain unknown. |
| 7. Duplicate identity | Omit duplicate items from the diagnostic tree without inventing suffixes. Hosts reject the diagnostic result. Authored suffixes therefore cannot collide with repair-generated keys. |
| 8. Partial success | Gate mounting, capture and pruning on `complete_root()`. Reject failed children throughout both walkers. Patch reuse preserves budgets and changed content. |
| 9. Reference renderer | Restore the complete attribute mapping, align coercion/limits with the app, use the pinned sibling `makepad` checkout, and correct case-sensitive `splash` paths. Update capability fixtures and the stale padding expectation to match the checked-in theme. |
| 10. Fingerprints | Include loop keys, reference identity and transitive view/component definitions in versioned component digests. Preserve independence from file locations and top-level declaration order. |

Both VM lineages now expose bounded document evaluation that rejects uncaught runtime errors even when execution later produces a node. The original raw infinite-loop and error-followed-by-valid-node probes both return failure. Existing general VM recovery behavior is preserved; document evaluators opt into the checked API.

Validation completed in release mode:

- **275 UI-core tests passed**, including eight new boundary regressions.
- **47 portable renderer/translator tests passed**, including the documentation example and tests on the reference's native VM.
- **All subprocess boundary assertions passed**, including **16 app/reference comparisons** of complete attributes and generated DSL. Payload tests include quotes, backslashes, control characters, Unicode, duplicate-field-shaped text, both Field callbacks and escaped routing keys.
- `git diff --check` passed in the parent and all four affected submodules.

The [reproduction instructions](splash-layers-probes/README.md) include the commands. Runtime fixtures use no network and send no notifications. The app evaluator is compiled with a dummy host type and fixture capabilities; this does not validate a full native app build, widget mounting or real capability providers.

The changes span the app plus `splash`, `splash-makepad`, `aichat` and `makepad` and must ship together because generated code uses the new pure helpers and evaluators use the checked VM API. Fingerprints remain 64-bit change detectors; complete-artifact approval pinning and state provenance enforcement remain explicitly outside the implemented contract. VM instruction limits cover bytecode execution; parsing and native capability work require their own host limits.
