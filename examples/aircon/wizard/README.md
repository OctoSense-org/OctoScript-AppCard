# Interactive service wizard

The 12 air conditioner scenes run as Makepad widgets in a WebAssembly canvas. The Astro website provides the guide, language switch, history controls, and explicit service updates. Clicking a native card button changes the shared service state and mounts the next native scene.

## Flow

1. Buy the sample air conditioner in the shopping app and return to the desktop.
2. Show the delivery update, then mark the delivery as received.
3. Open installation times. Saturday morning conflicts with the existing meeting; Sunday morning is available.
4. Confirm a time. The installation card and linked calendar card use the same booking.
5. Confirm, undo, or restore the calendar entry. Undoing the calendar entry keeps the installation booking.
6. Show the technician’s departure, then the completion update.
7. Review the materials invoice. Cancel/reopen the request or explicitly pay ¥130 and open the receipt.

The guide never advances on a timer. Back restores a local demonstration snapshot; Restart clears the session. Reloading or changing language starts a new walkthrough. This is a deterministic demonstration with no real merchant, calendar, messaging, or payment API calls.

## Implementation

- `service.mjs`: immutable browser version of `service/controller.py`, including actor validation, integer money, stable service IDs, SHA-256 event fingerprints, and idempotent effects
- `render.mjs`: binds the approved L0 scenes and kit styles to current state and Chinese/English copy
- `wizard.mjs`: website controller and same-origin iframe transport
- `wasm-host/`: Rust Makepad + Splash host; lowers each L0/kit scene in memory and emits real native widget bounds, text layouts, readiness, and `KitAction` inputs
- `export-bundle.py`: exports the 12 approved scenes and only their artwork; source screenshots are not shipped
- `build-wasm.sh`: builds the single-threaded WebAssembly runtime and packages its resources and notices

The parent sends `octosense:render` with an ID and generation. The child returns `octosense:rendered` only when the native widgets, images, vectors, and text have rendered. `octosense:action` carries the actual source control ID and the same generation. Both ends check the sender and origin; the parent rejects stale generations and locks input during a redraw.

Only photographs and artwork are image assets. Labels, button hit areas, surfaces, and card structure are native widgets. The browser runtime does not depend on a local Studio process, an HTTP service controller, cross-origin isolation, or a screen-sized raster behind invisible hit areas.

## Build and integrate

The reusable pipeline now lives at
[`image-to-appcard-flow`](../../../flows/image-to-card/README.md).
`../image-to-appcard-flow.json` describes this project's atlas, twelve scenes,
fourteen standalone service cards, browser modules and checks. Its `plan`, `run`
and `status` commands retain failed stages and separate unrun visual/native gates.
The commands below remain available for the original project-specific workflow.

Run from the service card project, using the pinned Makepad/Splash checkouts at the repository root (`../../` from the app) and a Rust toolchain with the WASM target:

```sh
python3 wizard/export-bundle.py
bash wizard/build-wasm.sh
node --test wizard/service.test.mjs wizard/render.test.mjs
```

Then run from the sibling `Octosense-website` project:

```sh
npm run sync:wizard
npm run build
npm run dev
```

`npm run sync:wizard -- /absolute/path/to/wizard` also accepts an explicit source directory. A normal Astro build uses the packaged assets already in `public/wasm/service-cards/`; it does not require Rust or the sibling checkout.

Routes:

- `/experience/aircon/` — English
- `/cn/experience/aircon/` — Chinese

The routes and asset URLs respect Astro’s `BASE_PATH`. The packaged WASM permits `https://octosense.org/`, `https://octosense-org.github.io/`, and the GitHub Pages `/Octosense-website/` prefix; other HTTPS origins or prefixes require updating the asset allowlist and rebuilding. Static hosting is sufficient. WebGL and WebAssembly are required; startup failures provide a retry control.

## Verification

`service.test.mjs` compares all 12 complete states and event digests with Python fixtures, then checks cancellation, restoration, Sunday booking, history, and repeated-payment branches against the Python reducer. `render.test.mjs` checks translations, resolved font sizes, native enabled states, dynamic copy, dismissed trees, and receipt headers.

The website’s `tests/wizard.spec.ts` clicks actual native widget bounds in Chromium, covers all 12 frames in both languages, checks mobile scaling and Sunday booking, and exercises keyboard alternatives, locale links, Back, and Restart. It saves native snapshots and screenshots under `Octosense-website/artifacts/wizard/`.

`cards.provenance.json` records original scene and artwork hashes. `build.json` records the WASM hash and packaged runtime resources. Existing Studio/native evidence remains separate from the WebAssembly evidence in `wasm-host/smoke-evidence/`.
