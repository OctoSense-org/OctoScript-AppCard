# 老同学，慢慢聚 / A reunion, all arranged

This is a deterministic, bilingual service AppCard demonstration. Familiar Messages screens hold the original invitation and event details. The desktop holds separately owned reunion, calendar and contribution cards. Every text label and control is a native Makepad widget. No email, calendar or payment operation reaches a real service.

| Scene | Surface | Interaction |
| --- | --- | --- |
| 01 | Messages app | Open Wang Ning’s reunion invitation |
| 02 | Messages app | Read the invitation and venue photo; open the time poll or event details |
| 03 | Desktop reunion card | Start choosing a time |
| 04 | Expanded poll card | Friday conflicts with a work meeting and is disabled; choose Saturday or Sunday |
| 05 | Expanded poll card | Confirm the selected preference or choose again |
| 06 | Desktop RSVP card | RSVP recorded; wait for an explicit organizer update before adding a calendar event |
| 07 | Separate reunion and calendar cards | Organizer confirms the venue and time; acknowledge or undo the calendar entry |
| 08 | Separate reunion and calendar cards | Restore the same calendar event; RSVP remains confirmed |
| 09 | Separate payment and RSVP cards | Review ¥180, recipient Wang Ning and the reunion purpose; explicitly pay or cancel |
| 10 | Payment cancellation card | Reopen the payment request; RSVP remains confirmed |
| 11 | Immutable payment receipt | Review the fixed receipt and open event details |
| 12 | Reunion app details | Read invitation, RSVP and payment records together; return to the desktop |

The organizer fixture confirms Saturday 24 October 2026 at 18:30 at 木光餐厅, 桂花路8号. A Sunday preference remains recorded, and the organizer’s later Saturday decision is called out explicitly. Calendar undo and restore retain event ID `calendar-reunion-2016`. The contribution is a second explicit organizer update. A payment receipt is created only by `pay_contribution`, with ID `REU-20261024-001`; cancellation never changes RSVP or calendar facts. Back changes the visible surface while retaining service facts. Restart begins a fresh demo session.

## Source and reconstruction

`source/atlas.png` is the original result of **one** built-in image generation call covering all 12 screens. The prompt requested the highest supported quality and 2400×3456. The tool returned **1045×1505** and exposed neither its model identifier nor a size/quality parameter. `source/generation.json` records that limitation and the original hashes. The normalized 812×1552 frame references are enlarged review inputs, not newly generated high-resolution images.

`source/crops.json` records measured crop rectangles. `source/atlas.ocr.json` preserves the source OCR. `scripts/author.py` contains measured card, button, icon and photograph rectangles in original panel pixels. It declares OCR corrections and intentional UX refinements, including the two separate calendar actions in scene 07. Each scene keeps its source measurements, reference hash, semantic map and compiled L0/kit/data/mapping.

Native reconstruction uses 410 nodes including 178 Labels. Noto Sans SC glyph metrics fit source text in both width and height. Browser copy covers every current-scene label in English and Chinese, with dynamic native text, enabled states and selection styles. Native Views approximate the decorative botanical desktop backdrop with a pale sage surface. SVG line icons are reconstructed vectors. Raster crops contain only contact portraits and venue photography; there are no full-screen rasters, rasterized UI labels or screenshot hotspots in the browser bundle.

## Outputs

- `cards/reunion-01` through `cards/reunion-12`: measured native scene sources and compiled outputs
- `service-cards/catalogue.json`: 14 independently sized native subtrees, explicitly owned by reunion, calendar or payment
- `wizard/service.mjs`: self-contained immutable service reducer and bilingual view model
- `wizard/card-bundle/`: 12 compiled scene payloads, referenced artwork and source-hash provenance
- `route_test.json`: two click-through routes in the shared runner schema, including disabled controls and all 12 scenes
- `pipeline-output/intake/`: immutable source intake receipt and unaltered atlas/prompt copies

The bundle contains 83 declared artwork files, primarily SVG icons. Its exporter checks asset declarations and excludes known reference and atlas hashes. The intake’s “native mapping not started” status describes the intake operation itself; native reconstruction was performed separately by `author.py`.

## Reproduce in the service project

Run from this directory, with the existing pinned pipeline and its Python virtual environment installed two levels above:

```sh
../../flows/image-lib/.venv/bin/python scripts/author.py
python3 scripts/build_service.py
node --test wizard/service.test.mjs
../../flows/image-lib/.venv/bin/python scripts/export.py
```

The author and exporter redirect the compiler’s artwork publication into this project’s `artwork/` directory. They never write the shared Studio request. Existing standalone extraction is retained only if its source scene hashes still match; after changing native source, preserve the earlier extraction and select a new output directory with the reusable `extract.py` tool. Use the parent project’s shared renderer and host for browser integration; this folder does not build or modify the shared WASM runtime.

## Validation status

All 12 scenes passed semantic preflight and native source compilation. All 14 standalone subtrees compiled. Nine Node service tests passed, including both locale routes, all 12 states, disabled and stale controls, event idempotency, explicit organizer updates, independent calendar/payment behavior, receipt immutability, complete label localization and readable dock-label geometry. The shared native payload adapter accepted all 24 scene/locale fixtures.

The parent subsequently captured all 12 static fixtures through Studio. `pipeline-output/gate-review.json` contains every gate result and a visual review bound to each screenshot hash. Native structure and semantic checks passed for all 12; image checks failed because observed reference measurements are absent. Overall acceptance remains false. The review records dock-label omissions and rendering/typography polish. These static fixtures do not prove browser dynamic copy, translated layout or independent card mounts; those checks remain separate.

Noto Sans SC fonts are distributed under the SIL Open Font License in `fonts/OFL.txt`. Generated references are review inputs; the shipped bundle contains only the declared artwork crops and vector assets.
