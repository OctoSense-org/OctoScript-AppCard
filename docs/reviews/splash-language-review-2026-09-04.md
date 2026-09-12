**Splash language: critical design and implementation review — 2026-09-04**

**UI design continuation:** The separate, previously unfinished L0–L3 layer review is now [complete](splash-layers-review-2026-09-04.md), with reproduced and extended evidence against the post-fix local checkout. Its findings concern UI semantics and the card-to-native rendering path; the historical workflow findings below retain their original scope.

**Resolution follow-up:** The ten numbered findings were opened as GitHub issues #9–#18 and have fixes in [draft PR #19](https://github.com/splash-lang/Splash/pull/19). The fixes are also committed locally on `fix/language-review-20260904` (`544695e`, `de2233f`). Workspace and vendor tests, formatting, strict Clippy, and Linux ARM64/RISC-V and Windows GNU compile checks pass locally. All GitHub Actions checks pass on PR commit `f1e775f`, including Linux tests, fuzzing, AddressSanitizer, and Miri. The PR remains unmerged. The findings below preserve the original reviewed snapshot; the broader design recommendations remain review guidance.

Splash has a defensible purpose: small generated programs, host-controlled effects, bounded data transformation, and a separate declarative UI profile. However, the current workflow language is not ready to serve as an in-process boundary for untrusted generated programs. I reproduced a process abort, execution continuing after failed assertions, unintended execution through incorrect operator precedence, and an ambient logging path. The UI profile independently lacks an aggregate work budget for realization.

The central architectural problem is that the published canonical grammar validates source, but the inherited VM still independently determines its meaning. Passing both parsers does not establish that they agree on evaluation. Considerably more of the capability and workflow infrastructure is specified and tested than the language semantics beneath it.

This review targets the local `splash/` checkout at `a20753c6cff96ee86758744e227a04460234a832`, inside octos-one `ff029405c7ff93f18d455c60bd178fa763e543aa`. It covers the workflow grammar and VM, core modules, representative capability/workflow behavior, language tooling, and the UI profile's validation/realization path. It does not establish findings against the independent `makepad/` or `aichat/` VM lineages, and it is not a complete audit of worker containment, durable storage, network adapters, or platform backends.

The standalone fork explicitly distinguishes itself from Makepad in [positioning.md](~/home/octos-one/splash/docs/positioning.md:12). The [upstream Makepad guide](https://github.com/makepad/makepad/blob/dev/splash.md) describes a different UI-host surface; upstream examples should not be treated as the standalone workflow specification.

P1 below means a release blocker for the intended untrusted execution or UI-host use. P2 means an important correctness problem or an unresolved language contract with reproducible consequences. These priorities are review judgments, not vulnerability scores. In particular, the capability examples below use an explicitly granted echo tool; they demonstrate incorrect control flow, not acquisition of an ungranted capability.

| Priority | Finding | Observed consequence |
| --- | --- | --- |
| P1 | Recursive equality has no graph/work bound | Canonical source aborts the host process; a small shared graph also exceeds the runtime deadline |
| P1 | Uncaught errors do not terminate execution | A failed assertion can precede an allowed effect; a workflow advances to the next step |
| P1 | `~` reaches the VM logging opcode | Script data is written to the process log without a tool grant |
| P1 | Mixed logical precedence is wrong | A branch that the published grammar short-circuits executes |
| P1 | UI limits count output, not aggregate work | Nested loops with false guards consume large CPU time while producing one node |
| P2 | Logical negation depends on number representation | `!1` and `!(1 + 0)` have different types and opposite truthiness |
| P2 | Canonical conditional blocks lose their values | Valid `let x = if ...` produces operand-stack underflow diagnostics |
| P2 | Array indices are silently coerced | Negative, fractional, string, and nil indices can select or overwrite item zero |
| P2 | Numeric coercion depends on string storage | Short and long numeric strings compare differently; invalid long strings become zero |
| P2 | JSON integers silently lose precision | A valid input identifier changes during parse/stringify |

**1. P1 — Equality escapes the runtime's resource limits.**

This complete canonical program aborts both debug and optimized probe processes with `SIGABRT` and `fatal runtime error: stack overflow, aborting`:

```splash
let a = [nil]
a[0] = a
let b = [nil]
b[0] = b
a == b
```

The same failure occurs with two records whose `self` fields point back to themselves. The identity fast path protects `a == a`; it does not protect two distinct cyclic graphs.

The equality opcode calls recursive `ScriptHeap::deep_eq`, which follows object fields and array elements without a visited-pair set or a work/depth limit. VM call-frame and operand-stack bounds do not measure these Rust calls. Instruction and time sampling happen around VM instructions, so they cannot interrupt work inside this equality operation. See [opcodes_ops.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/opcodes_ops.rs:104), [heap.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/heap.rs:595), and [vm.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/vm.rs:692).

Cycles are only one manifestation. Starting with two `[0]` arrays and repeatedly replacing each with `[previous, previous]` constructs a small shared graph. Comparing two such graphs revisits the same pairs exponentially. At depth 20 the debug probe completed successfully after approximately 0.288 seconds despite the default 64 ms hard timeout. At depth 29 the optimized probe was still running when an external two-second timeout killed it. Those are subprocess observations, not performance benchmarks; the structural lack of an internal work bound is the finding.

Use an iterative comparison with a visited-pair set and a charged work budget. Specify the equality result for cyclic graphs. Merely detecting cycles will not fix repeated work on acyclic shared graphs, and merely lowering the Splash call-frame limit will not fix native recursion. Add subprocess regressions for distinct cycles, long chains, and shared DAGs, asserting bounded termination and process survival.

**2. P1 — Uncaught errors are diagnostics rather than terminal failures.**

```splash
use mod.std
std.assert(false)
42
```

The optimized runtime reports `completed=true`, returns `42`, and includes an assertion diagnostic. An unknown variable or calling `nil` followed by `42` behaves similarly. Errors inside a returned array can also leave the outer evaluation marked successful even though JSON conversion subsequently rejects the embedded error value.

This is consequential at an effect boundary:

```splash
use mod.std
use mod.tool
std.assert(false)
tool.call("text.echo", "called after failed assertion")
```

With the CLI's explicit `--allow-echo` grant, the tool audit records `Allowed` and the CLI exits zero. A separate two-step workflow reproduced the larger consequence: step `guard` contains `std.assert(false); 42`; step `effect` calls its separately granted echo tool. The CLI reports both steps `succeeded`, the workflow `completed`, and an allowed tool event. Thus this is not just misleading result formatting: the next step's authority becomes active after a failed guard.

In [vm.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/vm.rs:652), `handle_errors` unwinds to a `try` when one exists, but otherwise only drains diagnostics. [Evaluation::succeeded](~/home/octos-one/splash/crates/splash-core/src/lib.rs:780) checks the final value alone. The workflow relies on that predicate before handling output and advancing; see [splash-workflow](~/home/octos-one/splash/crates/splash-workflow/src/lib.rs:6946).

Terminate the current evaluation at the first uncaught runtime error. Represent completion, suspension, and failure explicitly. Changing only `succeeded()` to inspect diagnostics is insufficient: an effect may already have executed by the time that predicate is checked. Preserve the existing distinction between recoverable `try/catch` errors and uncatchable resource stops. Regression tests should assert that no later effect occurs, no later step activates, and a caught error can still recover deliberately.

**3. P1 — Canonical `~value` bypasses the removal of direct-output APIs.**

```splash
~"private input sample"
```

This passes canonical preflight and writes a Makepad JSON log record containing the string directly to stdout. The same behavior occurs in an optimized runtime with an empty host and in the standalone CLI. The source value is also returned normally.

The grammar permits `~`, and [operator_to_unary](~/home/octos-one/splash/vendor/makepad/platform/script/src/parser.rs:633) maps it to `Opcode::LOG`. The opcode reaches [handle_log](~/home/octos-one/splash/vendor/makepad/platform/script/src/opcodes_vars.rs:655), bypassing the masked `std.log`, `print`, and `println` members. Its formatter also uses an ordinary growing `String`; see [the logging implementation](~/home/octos-one/splash/vendor/makepad/platform/script/src/opcodes_vars.rs:737).

Consequently, removing module members is not a complete audit of source-reachable effects. Script-visible input can enter process logs outside capability audits or a host's chosen output policy. Where stdout carries another protocol, these records can also interfere with framing. This is a logging/output boundary breach; no arbitrary filesystem, network, or secret-store access was demonstrated.

Remove `~` from the canonical workflow grammar or replace its opcode behavior with an explicitly configured, bounded host sink. Audit all admitted opcodes for direct I/O and allocation outside the VM budget. Test stdout and stderr capture as part of the no-ambient-output contract, using both direct and computed values.

**4. P1 — The execution parser disagrees with published precedence.**

```splash
let n = 0
true || false && (n = 1)
n
```

The result is `1`. Under the published grammar, `&&` binds more tightly than `||`, so the entire right-hand side should be skipped and `n` should remain `0`. A granted `tool.call` in place of the assignment actually executes. This reproduces in an optimized build.

The pure-value difference is equally direct:

```splash
true || false && false       // observed: false
true || (false && false)     // observed: true
```

The canonical parser expresses the expected hierarchy in [profile.rs](~/home/octos-one/splash/crates/splash-core/src/profile.rs:2600). The inherited parser's short-circuit handling patches an existing `ShortCircuitEnd` without checking its originating operator's precedence; see [parser.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/parser.rs:3634).

There is a second precedence mismatch in ordinary comparisons: `true == 2 > 1` yields `false`, while `true == (2 > 1)` yields `true`. The workflow grammar assigns comparisons higher precedence than equality, whereas the VM's [operator table](~/home/octos-one/splash/vendor/makepad/platform/script/src/parser.rs:518) groups them together.

Treat precedence and associativity as executable contracts. Generate tests for every pair of operators, plus side-effect counters on both sides of logical operators. The durable fix is to derive execution from the canonical parse tree or otherwise share its binding-power rules. Admission plus a second parser's acceptance is not sufficient.

**5. P1 — UI realization has no aggregate traversal budget.**

The independent UI profile avoids the workflow VM, which is a useful containment property. It still performs computation while traversing declarations and host data.

```text
source movers sys.movers()
state show {shape: bool, initial: false}
view root Panel {
  for a in movers key a.id {
    for b in movers key b.id {
      for c in movers key c.id {
        for d in movers key d.id {
          when show { Rule() }
        }
      }
    }
  }
}
```

This card passes UI validation. With 128 distinct `{id: ...}` items in host-supplied `movers`, all four loops remain below the default per-collection limit of 512, and nesting remains below 64. Because `show` is false, the traversal would produce only the root panel. The optimized probe nevertheless exceeded the external two-second timeout. A smaller three-loop example completed with `nodes=1`, `truncated=false`, and no diagnostics.

[RealizeLimits](~/home/octos-one/splash/crates/splash-ui-l0/src/lib.rs:5532) bounds output nodes, depth, and each collection. [Realizer::element](~/home/octos-one/splash/crates/splash-ui-l0/src/lib.rs:5836) checks the node counter, but only constructors increment it. [iteration](~/home/octos-one/splash/crates/splash-ui-l0/src/lib.rs:6053) does not consume a shared traversal budget. False guards therefore avoid the output counter while retaining the cross-product work.

Add a shared visit/iteration budget charged before every element visit and iteration, including false guards, references, slots, and component expansion. Stop remaining loops once it is exhausted. Bound materialization and cloning as well as output. A node cap alone cannot provide predictable UI latency.

**6. P2 — `!` changes meaning with the VM's numeric representation.**

```splash
[!1, !(1 + 0)]
```

Observed optimized result: `[false, 1.8446744073709552e+19]`. The second value is truthy; consequently `if !1 1 else 0` returns `0`, while `if !(1 + 0) 1 else 0` returns `1`.

[handle_not](~/home/octos-one/splash/vendor/makepad/platform/script/src/opcodes_ops.rs:14) bitwise-complements values represented as `f64`, but applies boolean conversion to other values. Arithmetic constructs `f64` values while small integer literals can use another representation. An internal storage optimization has become observable language behavior.

Define `!` as logical negation with a boolean result for every admitted operand, or reject non-boolean operands consistently. If bitwise operations are wanted, give them a separately specified integer operation. Add representation-invariance tests: a numeric literal, an arithmetic result with the same value, a variable, and a host-data value must not acquire unrelated meanings because of storage tags.

**7. P2 — Valid conditional blocks can underflow the operand stack.**

```splash
let x = if true {
    1
} else {
    2
}
x
```

This passes canonical checking but fails at execution with `pop_stack_value on empty stack` and missing-`x` diagnostics. The compact legal version using `1;` and `2;` behaves the same. `let x = if true 1 else 2; x` succeeds and returns `1`.

Canonical newline lowering inserts VM semicolons. The inherited conditional-block code preserves its tail only when `last_was_sep` is false; see [IfTrueBlock](~/home/octos-one/splash/vendor/makepad/platform/script/src/parser.rs:3152). Canonical `try/catch` received special tail-preservation handling, but this conditional path did not. The authoring guide explicitly recommends conditional values, making this more than an undocumented style preference; see [authoring-for-llms.md](~/home/octos-one/splash/docs/authoring-for-llms.md:89).

Specify whether each block context produces a value, then preserve it during lowering. Every valid expression branch should leave exactly one operand. Empty or statement-only branches must either yield a specified `nil` or be rejected in value position. Test `if`, `elif`, and `else` inside assignments, arrays, calls, and `try`; test LF, CRLF, and explicit semicolons. Function blocks also need an explicit return rule: current canonical tails are discarded unless `return` is used.

**8. P2 — Invalid array indices silently become valid writes.**

```splash
let a = [10, 20]
a[-1] = 99
a
```

Observed result: `[99, 20]`, with no diagnostic. Reads with `0.9`, `-1`, `"x"`, and `nil` each return the first item.

[ScriptValue::as_index](~/home/octos-one/splash/vendor/makepad/platform/script/src/value.rs:1111) casts numeric values and returns zero for unsupported types. Floating-point-to-integer conversion truncates fractions and saturates negative values to zero. [Array indexing](~/home/octos-one/splash/vendor/makepad/platform/script/src/opcodes_vars.rs:545) calls it without validating the operand. Splash's standard array helpers already perform more explicit index checks, so the core syntax and standard module have different contracts.

Validate finite, integral, nonnegative indices before accessing or mutating storage. If negative indexing is desired, specify and implement it deliberately; selecting zero is not a coherent negative-index policy. Invalid writes must leave the array unchanged. Prefer a checked conversion shared by indexing syntax and standard helpers.

**9. P2 — String coercion exposes inline-versus-heap storage.**

```splash
["2" > 1, "00000002" > 1]
```

Observed result: `[false, true]`. Individually, `"2" - 1` yields `NaN`, `"12345678" - 1` yields `12345677`, and `"abcdefgh" - 1` yields `-1`.

[cast_to_f64](~/home/octos-one/splash/vendor/makepad/platform/script/src/heap.rs:506) parses heap strings and substitutes zero on parsing failure, but does not handle inline strings through the same path. Thus semantically related input changes behavior when its representation changes. An invalid string can participate in arithmetic as zero without an error; a short string can instead create a non-finite result that fails much later at a JSON boundary.

For a small generated-dataflow language, strict numeric operands are easier to audit. Provide an explicit conversion with a defined invalid-input result if string-to-number conversion is needed. If coercion is retained, it must be uniform across string representations and must have a published failure policy. Do not preserve a storage accident as the language contract.

**10. P2 — JSON admits integer values that the runtime silently changes.**

```splash
"{\"id\":9007199254740993}".parse_json().to_json()
```

Observed returned string: `{"id":9007199254740992}`. Numeric source literals also collapse those distinct integers to the same value. This reproduces in optimized execution.

The numeric tokenizer converts through `f64`; see [tokenizer.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/tokenizer.rs:369). The VM JSON parser likewise uses floating-point values, and [write_script_json](~/home/octos-one/splash/crates/splash-core/src/lib.rs:2140) emits the resulting number. Byte limits, depth limits, and JSON syntax validation do not preserve integer identity.

Using floating-point arithmetic is a reasonable design choice; presenting a general JSON tool/dataflow boundary without a clear precision policy is the problem. A schema accepting an integer can still accept the changed identifier. Support exact integer values where required, reject unrepresentable values at ingress, or publish a restricted numeric domain and require string identifiers beyond it. Rejection must happen before the rounded value is passed to a tool. Add boundary tests covering positive and negative integers around the safe range and host injection as well as script parsing.

**Language-design decisions that need a written contract.**

The ten findings above should not be addressed only as isolated regressions. Several choices are currently inherited or scattered across implementation and tooling documentation:

- **Assignments as expressions.** `let a = 0; let b = 0; a = b = 3; [a, b]` returns `[nil, 3]`. `set_scope_value` returns `nil`, and assignment forwards that value. The grammar admits nested assignment expressions but does not clearly state the value contract. For this language, either make assignment statement-only and reject chaining, or make assignment expressions consistently return the assigned value. The current behavior silently creates data loss. See [object_heap.rs](~/home/octos-one/splash/vendor/makepad/platform/script/src/object_heap.rs:645).
- **Truthiness and equality.** A nonempty array is false in a condition: `if [1] 1 else 0` returns `0`. Records are truthy. `==` performs recursive comparison, while array membership helpers deliberately use reference identity for containers. These are not automatically invalid choices, but they need a complete operand/result table. For generated workflows, boolean-only conditions and clearly named structural versus identity operations would reduce ambiguity.
- **Missing values and function arguments.** `record.missing` raises a catchable error while `record["missing"]` yields `nil`. Missing function arguments become `nil`, extra arguments are ignored, and duplicate parameter names are accepted. I observed `fn f(a, a) { return a; }; f(1, 2)` returning `1`. Publish these policies or reject ambiguous forms during checking. A generator should not learn argument mistakes through distant dataflow failures.
- **Recovery without error classification.** `try/catch` intentionally discards the error. That is sufficient for a literal fallback, but it does not let source distinguish missing optional data, a programmer error, authorization denial, timeout, or indeterminate adapter failure. Keep retries and effect reconciliation host-owned, as the design already intends. If source-level recovery grows, expose a small bounded error code/category rather than raw host messages or stack objects. Do not encourage blanket fallback around effectful calls.
- **Profile identity and documentation.** `language-profile.md` still says the UI profile is proposed and unimplemented, while `ui-profile-l0.md` marks it implemented and the crate now also admits explicitly declared L1 expressions. The `Level::L1` documentation says it is not accepted, contradicting the checker. The authoring guide claims measured examples but recommends an `if` block without the terminator that its own Rule 0 requires. Generate capability/profile metadata from the implementation and execute documentation examples. Keep workflow v0.2, UI L0, UI L1, and the broader Makepad syntax explicitly distinguishable. See [language-profile.md](~/home/octos-one/splash/docs/language-profile.md:12), [UI checker](~/home/octos-one/splash/crates/splash-ui-l0/src/lib.rs:230), and [Level](~/home/octos-one/splash/crates/splash-ui-l0/src/lib.rs:63).
- **Syntax cost for generated code.** The mandatory terminator before `}`, prohibition of trailing commas, contextual `catch`, separate record/block rules, and inherited `**/` comment exception all require special producer knowledge. None is individually fatal, but their cumulative cost deserves measurement. Record first-attempt acceptance, semantic correctness, repair turns, token cost, and accidental effect execution against representative tasks. Do not treat a shorter surface syntax or a large fixture suite as evidence that LLM generation is more reliable.

**Architecture, tooling, and strengths worth preserving.**

The strongest parts are the separation of source review from authority, deny-by-default tool registration, host-owned schemas and grants, explicit deferred completion, bounded JSON serialization with cycle detection, uncatchable resource-stop intent, and the independent UI crate's lack of VM dependency. The inspected tests exercise many of these boundaries. Nothing in this review argues for adding ambient filesystem access, arbitrary imports, or an unrestricted async runtime.

The canonical frontend should become the owner of semantics. Currently the workflow path parses for canonical admission and newline insertion, then parses again in the VM; tooling reparses for lexical symbols and other projections. This duplicates language knowledge and makes semantic drift easy. A shared canonical AST with source spans would support validation, formatting, editor features, bytecode generation, and meaningful differential execution tests. It can remain separate from the broader Makepad compatibility frontend.

The LSP is deliberately lexical and advisory, which is an honest boundary. Keep capability suggestions advisory. But further completion and metadata features should follow basic semantic stabilization. Runtime diagnostics currently expose formatted internal VM/Rust locations, and the block-value defect produces stack-underflow and missing-binding errors rather than a useful explanation. Structured runtime diagnostics should carry a stable code, the original source span, and a bounded message. Recoverable errors and internal invariants should not share an undifferentiated string channel.

Implementation size also increases review cost. In this checkout, core `lib.rs` is 9,506 lines; the LSP entry point is 18,351; the UI module is 11,435; capability and workflow modules exceed 10,000 each. These totals include tests and are not themselves defects. They make it harder, however, to trace a compact language invariant across its many copies. Separate the semantic frontend, bytecode boundary, core data operations, diagnostics, and host orchestration along invariants rather than continuing to expand single files.

**Validation and limits of the evidence.**

All selected existing suites passed on macOS with Rust `1.95.0`:

| Command | Passed | Failed |
| --- | ---: | ---: |
| `cargo test --locked -p splash-core -p splash-cli -p splash-lsp` | 279 | 0 |
| `cargo test --locked -p splash-capabilities -p splash-workflow` | 223 | 0 |
| `cargo test --locked -p splash-ui-l0` | 266 | 0 |
| `cargo test --manifest-path vendor/makepad/Cargo.toml -p makepad-script` | 27 | 0 |
| Total | 795 | 0 |

The targeted probes used a fresh standalone Rust harness depending on the local `splash-core`, with default runtime limits and no installed host capabilities. Separate CLI probes explicitly enabled only the echo demo tool. Process-abort probes disabled core dumps; expensive operations ran in disposable subprocesses with external timeouts. The principal failures were repeated in an optimized build. UI probes used supplied JSON only and did not fetch source data or launch an application.

The companion [evidence JSON](~/home/octos-one/docs/reviews/splash-language-review-2026-09-04-evidence.json) records sources and observed results. The temporary [probe implementation](/tmp/splash-language-review-20260904/src/main.rs) and Cargo project remain available in this workspace session. Production implementation and tests were not edited.

This review did not run the full all-features workspace gate, cross-platform checks, Miri, sanitizers, or a sustained fuzz campaign. It does not claim complete memory-safety coverage. The existing [syntax fuzz target](~/home/octos-one/splash/fuzz/fuzz_targets/syntax.rs:67) usefully checks canonical-to-VM acceptance and formatter invariants, but that is not an execution oracle. Replay of the same VM can establish repeatability while repeating the same wrong semantics.

**Recommended order of work.**

1. Fix process survival and effect sequencing: bounded graph equality; immediate termination for uncaught errors; closure of the logging opcode path; correct short-circuit precedence; aggregate UI traversal fuel.
2. Establish scalar, index, block-value, assignment, and numeric-boundary contracts. Turn each decision into table-driven semantic tests, including negative cases and unchanged-state checks for rejected writes.
3. Add an independent oracle for the pure expression subset and trace-based tests for effects. Exercise equivalent numeric representations, operator pairs, nested block contexts, cyclic/shared values, and exception paths before/after `await` and workflow transitions.
4. Make canonical parsing drive execution, preserve original source spans, and generate profile/producer documentation from tested examples. Keep the compatibility parser an explicitly separate path.
5. Reassess readiness with adversarial tests that assert no unintended effect, bounded host work, process survival, and accurate failure propagation. Passing the current suites is valuable evidence of covered behavior, but it does not resolve the reproduced failures.

I would prioritize these semantic and execution-boundary fixes over expanding the language or adding more workflow/editor surface. The constrained-language idea remains useful; its safety and usability depend on making the small core predictable.
