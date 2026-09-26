# Unified native runtime

Every AppCard uses the release of
[Octoscript-Makepad](https://github.com/OctoSense-org/Octoscript-Makepad)
selected by `native-runtime.lock.json`. That framework owns `runtime.json`,
which fixes the underlying Makepad and Octoscript commits. Applications do not
carry alternate Makepad branches or compatibility patches.

```text
<workspace>/                  # this repository's parent, or $OCTOSENSE_WORKSPACE
  OctoScript-App-Design-Flow/ # this repository
    native-runtime.lock.json
    flows/  examples/  tools/
  octoscript-makepad/         # shared UI framework; runtime.json owns engine pins
  octoscript/                 # VM packages at the framework's revision
  makepad/                    # native platform at the framework's revision
```

From this repository's root, run `python3 tools/setup-native.py` to prepare the
sibling repositories. Use `--update` when updating clean checkouts to a new
release. The command preserves dirty source trees and custom Cargo
configuration and refuses a root inside this repository. `--check` verifies
the prepared source set without changing it; `--cargo-manifest <Cargo.toml>`
additionally checks that a Cargo workspace resolves a single Makepad
VM/platform/draw/widgets source (for example
`--cargo-manifest examples/calendar/native/Cargo.toml`). `--root` selects the
workspace; the default is this repository's parent directory, and
`OCTOSENSE_WORKSPACE` selects another one. `OCTOS_APPCARD_NATIVE_ROOT` overrides
where `flows/core/native_paths.py` looks for the prepared checkouts.

The WASM builder (`flows/image-to-card/wasm/build.py`) consumes this release in
both `existing` and `isolated` modes and applies no application-specific
runtime patches. Update the framework first, verify its native and browser
behavior, then update `native-runtime.lock.json` here.

Native UI checks use standalone release binaries, Makepad's built-in HTTP
instrument and hidden Metal windows. They do not use Studio. Close owned test
instances through `/gq` and verify exit. See
[the instrument runbook](../flows/core/NATIVE-INSTRUMENT.md).
Historical evidence retains the source paths and hashes from its original run.
