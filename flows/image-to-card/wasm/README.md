# Reproducible Makepad service-card WASM host

This module packages the working browser host as a portable pipeline step. It mounts L0 source and native kits in memory, producing real Makepad `View`, `Label`, `Button`, `Svg` and `Image` widgets. It does not reproduce the design with a DOM overlay. Service events and navigation remain the enclosing flow controller's responsibility.

## Build interface

Requirements: Python 3.9+, Git, Cargo/Rustup with the nightly toolchain and its `rust-src` component, and the project inputs below. Node 18+ and Playwright are required only for the browser smoke. The compiler uses the pinned Makepad custom WASM target, release optimization, no LTO and no atomics; SharedArrayBuffer and COOP/COEP headers are unnecessary. The exact installed Rust toolchain is recorded, not claimed to be interchangeable across versions.

```sh
python3 flows/image-to-card/wasm/build.py \
  --workspace "$PIPELINE_ROOT" \
  --project "$SERVICE_PROJECT" \
  --output "$BUILD_ARTIFACTS/wasm-dist" \
  --build-dir "$BUILD_CACHE/service-card-wasm"
```

`--workspace` is the external `octosense-org` directory containing `makepad`, `octoscript` and `octoscript-makepad`. The default scratch directory is `$OCTOSENSE_WORKSPACE/.appcard-native/wasm/<app>/`; source clones stay outside AppCards. `--project` is an external service project. `--output` must be new; the tool refuses to overwrite an existing package. `--build-dir` is a reusable scratch directory, separate from output and shared source repositories.

For an existing publication directory, `--replace` builds and verifies a complete staged package before an OS atomic directory exchange (macOS `renamex_np` / Linux `renameat2`). The output path never disappears during exchange. The previous package is then archived beside it as `.<name>.previous-<build-id>`; interruption after exchange leaves the old package intact at the recorded staging path. Platforms without atomic exchange fail while retaining the previous output. Failed compilation or packaging leaves the published directory untouched. The flow orchestrator uses this option when refreshing its configured `outputs.wasm` location.

The default `--dependency-mode isolated` prepares the release from the AppCards
root `native-runtime.lock.json` in scratch. Octoscript-Makepad's `runtime.json`
owns the Makepad and Octoscript revisions. These are the same sources used by
Mail and Android; no app-specific patches are applied. Existing shared source
repositories are preserved. `--dependency-mode existing` verifies the same
release in the shared workspace before and after building.

`--cargo-makepad /path/to/cargo-makepad` reuses an existing compiler executable and records its SHA. Otherwise the tool builds `cargo-makepad` into scratch if no executable is present. `--target-dir /path/to/cargo-cache` symlinks the generated host's `target` directory to a caller-owned cache; do not share an active cache between concurrent builds. `--prepare-only` stages and verifies the dependency snapshot and generated Cargo manifest without compiling.

The automatic compiler build uses the bundled `toolchain/cargo-makepad.lock` with `--locked`, retains that lock and compiler log in the run evidence, and only writes to an isolated dependency checkout. Existing-dependency mode requires an existing compiler executable so it does not generate a lock inside the source submodule.

The project supplies:

- `fonts/NotoSansSC-{Regular,Medium,Bold}.ttf` and `fonts/OFL.txt`
- `cards/**/contract.json` and/or `service-cards/**/contract.json`
- Each exported card's `page.card`, `page.data.json`, `mapping.json`, native kit and `assets/` as produced by the image-to-AppCard pipeline

Contract IDs determine output `card-assets/<id>/assets/<file>` paths. IDs and flat artwork filenames must contain only letters, numbers, underscore, hyphen or dot. Conflicting duplicate IDs and assets outside the project are rejected. This initial host embeds the complete Noto Sans SC Regular font and retains four known fallback faces; other font sets require an explicit template/package change and renewed rendering checks.

Discovery stops descending once a card directory has `contract.json`, so earlier `rounds/` snapshots and nested evidence are preserved as history and are never accidentally shipped as current artwork.

## Shared runtime

The AppCards root `native-runtime.lock.json` selects Octoscript-Makepad; its
`runtime.json` selects Makepad and Octoscript. Generated Cargo configuration
resolves every Makepad crate to that source, including transitive dependencies.
The framework owns native/WebView compatibility and the no-atomics SDF path.
Cargo locks in `template/` and `toolchain/` record package resolution only.

Generated `makepad_platform/web.js` receives exact-match packaging patches for
iframe focus behavior. The dependency source remains unchanged. The index and
bridge URLs carry the WASM SHA to avoid stale modules after publication.
`patches/image-to-appcard.patch` is retained as historical lab evidence; the WASM
build never applies it or starts Studio.

## Browser transport and artwork policy

The iframe accepts messages only from its actual same-origin parent. Send `{type:'octosense:render', id, generation, card, data, kit, mapping, width, height, updates}`. `updates` contains `{id,text?,enabled?}` entries keyed by source or native widget IDs; Button IDs usually end with `_control`. Width and height are the requested card's logical artboard, not a fixed screenshot size.

After checked L0/kit lowering and a real draw, `octosense:rendered` echoes the request ID/generation and actual widget areas, text layouts, image readiness and enabled state. It waits for the mapped font and image/vector resources. `octosense:inspect` returns the corresponding `octosense:snapshot`. Actual `KitAction::Activated` events produce `octosense:action` with the same request ID/generation and source control ID. The parent must reject stale generations and own the service reducer; the host does not perform payment or other external service actions.

Asset URLs must stay inside the iframe's same-origin sibling `card-assets/` directory. The bridge rejects traversal, foreign origins, query/fragment components and noncanonical URL forms. The locked WASM renderer permits HTTP `127.0.0.1`/`localhost` development addresses and exactly these HTTPS bases:

- `https://octosense.org/wasm/service-cards/card-assets/`
- `https://octosense-org.github.io/wasm/service-cards/card-assets/`
- `https://octosense-org.github.io/Octosense-website/wasm/service-cards/card-assets/`

Other domains or deployment prefixes require a framework policy change and rebuild. Native/lab rendering retains its original loopback-only policy. This restriction is intentionally not an arbitrary remote-resource bypass.

## Evidence and browser smoke

Every run gets a new `runs/<build-id>/receipt.json` and compiler log in scratch. Failed builds retain their actual failure and any incomplete package. Successful `build.json` records the WASM SHA, compiler/toolchain, the shared runtime revision and its exact dependency revisions, pipeline/template sources, generated Cargo/native sources, project font/card/artwork hashes, generated JavaScript patches and every shipped file's hash except `build.json` itself. The run receipt also hashes the final package receipt. Pipeline hashes live in `pipeline_sources`; `sources` contains only paths relative to `--project`, preserving the site publisher's input-verification contract.

```sh
node flows/image-to-card/wasm/smoke.cjs \
  --dist "$BUILD_ARTIFACTS/wasm-dist" \
  --card "$SERVICE_PROJECT/cards/product" \
  --playwright "$PLAYWRIGHT_MODULE" \
  --origin https://octosense.org \
  --activate buy_control --expected-action buy \
  --output "$BUILD_ARTIFACTS/browser-smoke"
```

The smoke intercepts the chosen origin and serves the local package under `/wasm/service-cards/`; it does not deploy or contact live services. `--base-path` can select another permitted deployment prefix, and `--asset-prefix` sets the source lab artwork URL prefix to rewrite. `--disabled` optionally names a disabled native control to click. `--browser` selects an explicit Chromium executable. The test uses the selected contract's artboard, saves only the canvas drawable, checks actual widget bounds and native actions, and rejects foreign/traversal artwork. Its report binds the binary and fixture hashes. This is a native mount/action smoke, not a full image-parity gate or a complete service-flow test.

Chromium 1243 intermittently stalled when cold-mounting a text-heavy appointment card directly in the original host. A hosted-origin run passed on 1243, a localhost comparison passed on 1234, and complete integrated flows beginning with the product scene passed on 1243. Failed attempts were retained. Do not infer universal browser compatibility from the build, or silently replace a failed runtime test with a screenshot. Retest the actual deployment, browser and intended start sequence.
