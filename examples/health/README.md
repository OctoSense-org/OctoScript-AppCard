# Health appointment flow

English | [简体中文](README.zh-CN.md)

One generated atlas supplies twelve measured native scenes and twelve independently mountable health/calendar service cards. The application invitation leads to a desktop appointment card, optional item choices, calendar-aware time selection, booking, calendar acknowledgement/undo/restore, draft edits, explicit cancellation, and a final summary.

The provider, appointment and existing calendar conflict are fictional local fixtures. Dental and vision checks are provider-offered options chosen by the user; the flow makes no medical recommendation, gives no clinical instructions, reports no examination results and creates no real appointment.

## Source and resolution

- `source/atlas.png` is the untouched original output of one built-in image-generation call
- `source/prompt.txt` is the exact complete prompt for all twelve screens
- Requested resolution: **2400 × 3456**, maximum supported detail
- Actual original PNG: **962 × 1635**; this remains a **draft-resolution source**
- Model identity was not exposed by the tool; no specific image model is claimed
- `source/generation-receipt.json` records these limits and the original generated-file location
- `pipeline-output/intake-v2` records immutable original bytes, lossless crops, and uniform transforms into 406 × 776 artboards

The 812 × 1552 reference images are derived layout references, not newly generated detail. The native scene uses real labels and buttons. The only raster shipped in the scene artwork is the first screen's inspected, text-free waiting-room photograph. Icons are traced vectors; the source landscape wallpaper is approximated with native flat surfaces. Screenshots and complete reference images are not shipped as UI.

## Files

- `image-to-appcard-flow.json`: reusable pipeline manifest
- `cards/health-01` through `cards/health-12`: measured native contracts, semantic maps, source measurements, compiled L0/kit/data/mapping, and control bindings
- `pipeline-output/service-cards`: twelve extracted service-owned native card subtrees
- `wizard/card-bundle`: portable compiled scene bundle and artwork provenance
- `wizard/service.mjs`: self-contained immutable bilingual browser service model
- `wizard/service.test.mjs`: behavior, scope, idempotency, localization and binding tests
- `route_test.json`: four complete native-click routes, including disabled controls, edits, cancellation, Back and Restart
- `evidence/contract-validation.json`: 126 bilingual route/contract binding checks across all twelve scenes

## Behavior

Saturday 09:00–10:00 conflicts with the existing personal event and is disabled. Sunday makes that offered slot available. Switching days clears the selection. Confirming creates one stable booking and one linked calendar event. Optional dental/vision items remain explicit user choices.

Calendar acknowledgement changes only acknowledgement state. Calendar undo removes only the linked event; the health booking remains active. Restore reuses the same event ID. Draft edits retain the booked slot until confirmation. Confirming changes updates the same booking and existing linked event; a previously removed calendar event stays removed until the user restores it.

Opening the cancellation card has no side effect. Confirming cancellation cancels the booking and removes its linked event while retaining unrelated personal events. Replayed event IDs have no repeated effect; using an ID for a different action or submitting a stale/disabled control is rejected. Back restores local simulation snapshots, and Restart creates a fresh local scenario. No timers advance the flow.

Native Studio and browser visual acceptance are performed separately by the parent integration workflow. Compiled artifacts and model tests do not claim visual approval.
