# Makepad service-card browser host

This crate mounts the reviewed L0 cards as real Makepad widgets. Browser messages carry the card source, JSON data, native kit and mapping in memory. `splash-ui-l0::realize` and `kit_pack::lower` feed `splash_makepad::design::prepare`; checked Makepad evaluation builds Label, Button, View, Svg and Image widgets. The JavaScript bridge does not draw card controls or place image hotspots.

Build from the project root with `bash wizard/build-wasm.sh`. The existing `cargo-makepad` executable and nightly `rust-src` are required. Output is `wizard/wasm-dist/`; copy that whole directory under the Astro public directory. The build uses release optimization without LTO or atomics. It requires WebAssembly and WebGL, but no SharedArrayBuffer or COOP/COEP headers.

The card kit's complete Noto Sans SC Regular font is embedded in WASM and placed in Makepad's resource table before the first mount. Other used fallback fonts and verified photo/SVG assets remain normal static files. The no-atomics Makepad branch uses SDF/SLUG and does not launch an unavailable MSDF worker. `build.json` records the binary, dependency revisions, changed font source, embedded font hash, generated browser focus patch and all shipped files. Licenses are included in the output.

The package stamps the WASM SHA into the index-to-bridge and bridge-to-WASM request URLs so an existing browser cache can load a new release. HTTPS artwork is allowed only at the explicit `https://octosense.org/wasm/service-cards/card-assets/`, `https://octosense-org.github.io/wasm/service-cards/card-assets/`, and `https://octosense-org.github.io/Octosense-website/wasm/service-cards/card-assets/` bases. The bridge additionally enforces the iframe's exact origin and sibling `card-assets` directory, rejecting cross-origin, traversal, query and fragment URLs. The WASM build supports HTTP `127.0.0.1` and `localhost` development addresses; native/lab asset restrictions are unchanged. Other hosting prefixes require an explicit renderer policy update.

## Same-origin iframe protocol

The iframe accepts messages only from its same-origin parent. It emits `octosense:ready` after native startup. The parent may send `octosense:ping` to repeat the ready event after its listener is installed.

Send `{type:'octosense:render', id, generation, card, data, kit, mapping, width, height, updates}`. `mapping` accepts either its full mapping.json object or its elements array. Each mount needs a unique id/generation pair. `updates` contains `{id, text?, enabled?}`, where id is a source or native widget ID. For enabled updates use the Button source ID ending in `_control`. Asset URLs in data must point to the published `card-assets/<card-id>/assets/` directory. A complete scene uses its original 406 × 776 logical canvas; a standalone card uses its exported artboard.

`octosense:rendered` echoes id/generation and reports measured native widget bounds, clipping, enabled state, text and text layout. It waits for the mapped CJK font, nonempty Label layouts and loaded Image/Svg data. `octosense:inspect` requests the same data as `octosense:snapshot`. These are runtime geometry receipts, not an image-parity gate.

Actual KitAction activation emits `{type:'octosense:action', id, generation, sourceId, control, nativeId, action:'activated'}`. `sourceId`/`control` refer to the KitButton wrapper such as `confirm_booking`; disabled Buttons emit no activation. The parent must reject events from old id/generation pairs before invoking the service reducer. The host has no payment/network-service side effects.

Browser input focus stays within the canvas only during direct interaction: the generated web bridge does not recapture blur in an iframe, and textarea focus uses `preventScroll`. There is no page-wide error suppression.

## Local runtime checks

Serve `wizard/wasm-dist` on port 8494, then run `node wizard/wasm-host/smoke.cjs` using the workspace's Playwright install. Evidence is written to timestamped `smoke-evidence/` folders. The check inspects actual widget areas, clicks disabled and enabled controls, mounts the product photo scene, remounts the appointment card, and confirms native text/enabled updates. Canvas captures contain only the application's drawable.

To verify the hosted policy without deployment, run `OCTOSENSE_TEST_ORIGIN=https://octosense.org node wizard/wasm-host/smoke.cjs`. Playwright intercepts that origin and serves the local package under `/wasm/service-cards/`. The same check can target `http://localhost:4321`. These runs verify native photos/actions and reject foreign-origin, out-of-directory and encoded traversal artwork; the report binds the tested WASM SHA. They do not claim that the public deployment has been updated.

`OCTOSENSE_CHROMIUM_EXECUTABLE` selects an explicit Chromium executable for comparisons; `OCTOSENSE_DEBUG=1` prints browser resource and runtime messages. Chromium 1243 has intermittently stalled when this isolated smoke cold-mounts appointment scene 7. The retained HTTPS run passed on 1243, and the localhost comparison passed on 1234. The integrated wizard's normal scene-1 start and complete flows were separately checked on 1243; these isolated checks do not replace that coverage.
