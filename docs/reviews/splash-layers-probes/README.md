**Splash layer regressions**

Run from the octos-one root, with the `splash`, `splash-makepad`, `aichat` and `makepad` checkouts present:

```sh
cargo test --locked --release --manifest-path splash/Cargo.toml -p splash-ui-l0
cargo test --locked --release --manifest-path splash-makepad/Cargo.toml -p splash-render -p splash-makepad
python3 docs/reviews/splash-layers-probes/run.py --assert-fixed
```

The runner creates two temporary Cargo projects and builds them in release mode. It writes `docs/reviews/splash-layers-fixes-2026-09-04-evidence.json`; the [original review evidence](../splash-layers-review-2026-09-04-evidence.json) remains a separate historical snapshot. `--output /path/to/result.json` chooses another output. `--work-dir /path/printed/by/previous/run` reuses compilation artifacts.

`ui.rs` exercises the public checker, realizer, patcher and dispatcher. The VM project copies the production app evaluator and translator, replacing only the evaluator's `Cx` type with a dummy integer host. It copies the pure numeric/event helpers and registers a deterministic `sys.stock` adapter. Actual `kit::lower` output runs with the checked-in palette, derivation and theme kit. Field probes evaluate the exact emitted `on_return` and `on_change` target expressions, including escaped payloads and routing keys containing `$$`.

`--assert-fixed` rejects crashed/timed-out probes and asserts the repaired behavior, including event dispatch, missing arithmetic, complete deep rendering, patch bounds, closure changes and duplicate-key failure. The same scripts run through the reference evaluator for comparison of all node attributes and generated backend DSL. That comparison uses the app VM to isolate evaluator differences; the Cargo renderer tests above also exercise the reference's own `makepad` VM.

Python 3 and Rust supporting edition 2024 are required. The Unix subprocess limits were tested on macOS ARM64. Cargo may fetch dependencies; runtime probes make no network requests, launch no UI, and send no notifications. Event dispatch uses only in-memory state. These tests do not validate native widget mounting or real capability providers.

The original findings, generated inputs, lowered source and before-fix outcomes are retained in the [review](../splash-layers-review-2026-09-04.md). Current probes and inputs also remain in the printed temporary directory.

The follow-up [gap report](../splash-layers-gaps-2026-09-05.md) adds enforced state
origins, durable approvals and native evidence. Preserve previous evidence with
`--output docs/reviews/splash-layers-gaps-2026-09-04-evidence.json`. The runner now
compiles the actual host approval persistence module in a separate CLI test crate,
and Field callbacks also pass through the real VM outer-payload JSON serializer.

For the native fixtures, build Studio from upstream Makepad `dev` in a separate
checkout. Start it with `--mounts=octos:/absolute/path/to/octos-one/app`, then use the
persistent bridge and `RunItem` for `octos-splash-native-review` or
`octos-splash-native-l1`. Both are declared in `app/makepad.splash`; Studio builds
`octos-app --release`. They disable transport setup, use only local state/data and
store approvals in `/tmp/octos-splash-native-approvals`. Clear the preceding build
before rerunning. A changed runtime deliberately rejects a saved pin: retain the
old test record as evidence before explicitly readmitting the fixture. Never remove
a user's production approvals as part of this test.

The source-lock regression runs independently:

```sh
cargo test --release --manifest-path aichat/Cargo.toml -p makepad-platform --lib approved_sources_ignore_file_changes_but_keep_manual_layout_refresh
```
