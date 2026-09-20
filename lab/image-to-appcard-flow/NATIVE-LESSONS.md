# Native scene lessons from the Calendar port

Provenance: the Calendar app was built end-to-end through this flow's native
stages and survived two operator review rounds of the running app. Every rule
below is one the rounds earned the hard way; they belong in the flow proper
once the two flagged decisions are settled.

## Mounting: the create-time viewport is not the tile size

- The module's create-time viewport reported about 2x the real tile; a scene
  fitted to it culled every control right of x=206pt of the 406pt page. The
  mounted tree silently lost 107 widgets.
- Rule: draw first, measure the laid-out area, and mount (or refit) from a
  short timer; log the fitted viewport and origin with every mount.
- Acceptance: the live widget dump must match the emitted element count
  (164 vs 271 was the only visible signal of the culling).

## Scale: one uniform factor for both axes

- Separate x/y fits overflowed the page horizontally (the 六 header and the
  day-26 column cut at the screen edge) and pushed the tab bar below the
  tile bottom.
- Rule: one scale `min(tile_w/406, tile_h/740)`, centered horizontally,
  starting at the tile top.

## Per-crate lowering gate

- A test that builds every screen state and runs it through the same emitter
  the shell uses catches binding and emit errors inside the crate in seconds;
  the same error in the shell costs a full rebuild cycle.
- Rule: every native crate ships a lowering-gate test over all screen states;
  the pipeline should run it.

## Icon assets: policy contradiction (DECISION NEEDED)

- The design emitters admit only loopback-http SVG sources, while the native
  stage requires self-contained crates with no hand-started servers. Current
  workaround: redraw icons as bundled-font glyphs plus bordered-surface
  geometry.
- Decision for maintainers: (a) accept crate-packaged SVG/PNG artwork in the
  emitters, or (b) sanction a native icon vocabulary (bundled-font glyphs and
  simple geometry) as the approach.
- Either way: a `font miss U+XXXX` line in the host log is a failure — a
  missing glyph silently fell back to a cross on the sync icon. Verify icons
  by zoomed crops against the reference page, not by mean pixel diff: a
  12.49 mean diff hid both a clipped label and two wrong icons.

## Clicks: the real action shape

- On the current makepad rev, the kit re-emission (`KitAction::Activated`)
  never fired for composed kit buttons; the tap arrives as the bound
  control's own platform `Clicked` action under the child widget's uid.
- Workable wiring: at mount, index every live widget under its element root;
  on an action batch, resolve the uid through that index and ask the widget
  itself (`Button::clicked(actions)` — the kit's own `activated()` idiom).
- Naming: full-cell tap targets are `tap_<target>`; strip the prefix when
  mapping to service actions.

## Edit state: same screen, the event's own values

- Reviewer-visible bug: the edit sheet rendered as a new-event sheet (new
  title, add button, placeholder location) instead of carrying the event's
  values.
- Rule: a sheet editing an entity renders its title, button and every field
  from the draft state. The walkthrough must open the edit action and check
  the prefill, not just reach the screen.

## Verification discipline

- Refit the screenshot-compare transform from instrument anchors every round.
  The fit changed twice (viewport fix, uniform scale) and mean diffs are not
  comparable across fits; state the fit assumption in the script header.
- Attach one zoomed evidence crop per review defect; the mean diff is a
  regression signal, not an acceptance.
- The scripted walkthrough (snap -> click -> grab -> log, transcript plus
  per-step captures) is the fastest review instrument. Traps: snap matches
  widget ids too (`24` hits a widget whose text is `11`) — match exact text;
  tab-bar buttons must be located from the button snapshot by geometry
  (narrow width inside the tab band), not from their text labels, whose rect
  hugs the button's bottom edge.
- Stale binaries cost whole rounds: rebuild the crate and the shell, quit the
  previous host, read the port from the current run's log, and keep exactly
  one host alive (check before and after).

## Reference implementation

Eval workspace `Octoscript-AppCard-eval-glm`, branch `eval/calendar-glm`:
native crate under `apps/calendar/native` (11/11 tests including a
lowering-gate test over all eight screen states, six-screen comparisons, a
13-step walkthrough transcript and per-defect evidence crops). This is a
docs-only PR; the emitter/icon changes can follow as code PRs once the
icon-asset decision is made.
