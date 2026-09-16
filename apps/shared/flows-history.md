> Historical cross-app review. Projects moved from `flows/<name>/` to
> `apps/<name>/`; shared helpers moved to `apps/shared/`. Commands below record
> the old layout and Studio workflow. See [current app layout](../README.md).

# Additional image-to-AppCard flows

Each folder is an independent pipeline project with one generated 12-screen atlas, the exact prompt and original-image provenance, measured crop/OCR evidence, native L0/kit mappings, extracted service cards, a bilingual immutable reducer and its tests.

| Folder | App experience | Desktop services |
| --- | --- | --- |
| `school` | Mail inbox, teacher message, calendar details, school invoice and receipt | Authorized teacher calendar update; acknowledge, undo and restore; separate explicit school payment |
| `health` | Checkup invitation and provider details | Package/options, conflict-aware time selection, booking, calendar undo, changes and cancellation |
| `reunion` | Messages, group invitation, reunion details | Time voting and RSVP, explicit organizer update, linked calendar, separate contribution and receipt |

`shared/render.mjs` binds current service state to the measured native scene. `shared/wizard.mjs` sends it to the existing Makepad/WASM runtime. All card controls are native Makepad buttons; browser keyboard alternatives dispatch the same service actions. Provider events require an explicit update click. Back navigates through the local demonstration; Restart resets its sample state. Neither connects to or reverses real transactions.

## Reproduce

From the service project root, with Node.js on `PATH`:

```sh
source runtime/env.sh
flow=school
bash pipeline/tools/image-to-appcard-flow.sh run \
  --project "$PWD/flows/$flow" \
  --manifest "$PWD/flows/$flow/image-to-appcard-flow.json" \
  --stages intake,semantic,compile,bundle,service-test
```

Use `--stages extract` with a new output directory when re-extracting changed cards. To capture native evidence, start the three servers documented in `runtime/README.md`, then run `--stages capture --launch` for the first project and `--stages capture` for the remaining projects. Capture and service watchers must be serialized because Studio consumes one current request.

After scene capture, validate independent cards through the same caller-owned Studio RunItem:

```sh
"$BEAUTY_PYTHON" flows/shared/verify-standalone.py --build-id '[2]'
```

Use the actual current build ID from `pipeline/lab/image-to-appcard/studio-run.json`. The verifier stages immutable source copies, serves their declared native artwork locally, mounts each card at its own artboard size, and collects WidgetTreeDump, WidgetSnapshot, WidgetQuery, layout, screenshot and real Button/KitAction evidence. A missing local SVG is a failed mount, not a passed geometry check. Evidence and failed attempts remain under `flows/evidence/standalone/`.

From `Octosense-website`, `npm run sync:wizard` validates the original runtime and all four scene packages, then publishes an atomic package snapshot. Only declared artwork is included. It checks each bundle's hashes and source declarations, and records each flow separately in `public/wasm/service-cards/build.json`. A failed additional flow retains the previous website package. `npm run build` prepares the bilingual routes.

## Generation and visual status

The three new atlases were each generated in a single built-in image-generation call, requesting 2400×3456. The actual original outputs are smaller (school 907×1733, health 962×1635, reunion 1045×1505), and the tool did not expose a model identifier. These are **draft-resolution reference images**. Native compilation and interaction verification do not certify highest-resolution generation or pixel-perfect visual parity. Per-flow generation receipts and review notes preserve that distinction. No screen screenshot is used as the interactive runtime UI.
