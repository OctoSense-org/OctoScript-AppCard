# Unified native runtime

Every AppCard uses the release of
[Octoscript-Makepad](https://github.com/OctoSense-org/Octoscript-Makepad)
selected by `native-runtime.lock.json`. That framework owns `runtime.json`,
which fixes the underlying Makepad and Octoscript commits. Applications do not
carry alternate Makepad branches or compatibility patches.

```text
octosense-org/
  Octosense-Service-AppCards/
    native-runtime.lock.json
    apps/{aircon,mail,school,health,reunion}/
  octoscript-makepad/       # shared UI framework; runtime.json owns engine pins
  octoscript/               # VM packages at the framework's revision
  makepad/                  # native platform at the framework's revision
  .appcard-native/          # build output or isolated copies of the same release
```

From AppCards, run `python3 tools/setup-native.py` to prepare the sibling
repositories. Use `--update` when updating clean checkouts to a new release.
The command preserves dirty source trees and custom Cargo configuration.
Each Cargo workspace declares only its required sibling source overrides;
generated WASM hosts receive equivalent absolute paths.
`--check` verifies the source set. Add `--cargo-manifest app/Cargo.toml` after
building to verify that Cargo resolves a single Makepad VM/platform/draw/widgets
source. The default is the AppCards parent directory; `OCTOSENSE_WORKSPACE`
selects another organization workspace. Git consumers set the same variable in
Cargo configuration so embedded framework resources come from that release.

Mail's `scripts/setup_native.py` calls this same setup. Its default runtime root
is the organization workspace. `OCTOS_MAIL_NATIVE_ROOT` may select an isolated
copy, but it must use the same AppCards runtime release and engine commits.
The WASM builder also consumes this release in both `existing` and `isolated`
modes. Neither mode applies application-specific runtime patches.

Update the framework first, verify its native and browser behavior, then update
AppCards' framework commit. CI prepares that exact release before compiling the
Android/desktop client and checks the resolved Makepad source graph. The old
`aichat` Makepad submodule is retired.

Native UI checks use standalone release binaries, Makepad's built-in HTTP
instrument and hidden Metal windows. They do not use Studio. Close owned test
instances through `/gq` and verify exit. See
[the instrument runbook](../lab/core/NATIVE-INSTRUMENT.md).
Historical evidence retains the source paths and hashes from its original run.
