# Visual checks for a compiled scene

A compiled scene passes `intake`, `semantic`, `compile`, `bundle` and
`service-test` without anyone having looked at it. Every one of the fifteen
defects found in the first calendar build — a white page where the reference is
`#E9EDF3`, every text line clipped at the bottom, `9月` drawn as `9F`, a `+`
drawn twice, tab icons stretched, taps reaching nothing — was found by a person
looking at a screenshot, not by a stage. These rules make *you* that person.

You can see. `view_image` shows you any PNG/JPEG in the workspace; `view_video`
shows you an MP4/MOV. Use them on your own output. A number is where to look; an
image is what you decide on.

## The loop, per scene

1. **Render it fresh.** One host process per scene, a new request nonce, then
   `/g`. Never trust a live reload; a stale grab reported a defect that did not
   exist, twice. `flows/image-to-card/compare_screens.py` does this for
   every scene and writes `<design_id>-compare.png` (page on the left, your
   render on the right), per-band numbers, and an ink probe.
2. **Look at the side-by-side with `view_image`.** Compare region by region:
   status bar, navigation, body, list, tab bar. Name each difference in words
   before touching code: *what* (text / icon / colour / position / size),
   *where* (the element id), *how much* (points or a colour).
3. **Check what the numbers cannot.** For every text widget the host placed
   (`/snap`), the probe reports whether any ink is inside its rect. A widget
   with the right text and rect and no ink is drawing nothing — `alignx` out of
   range, a zero-height box — and `/snap` will never tell you.
4. **Fix, recompile, go to 1.** Do not reuse a measurement taken before a
   layout change: re-measure. Calibrate on invariants (left edge, centre y),
   not on an edge the fix moves.
5. **Keep the evidence.** Each defect you fix gets a crop before and after in
   `apps/<app>/evidence/`, named for the element. The report cites them.

## Rules that decide pass or fail

| Rule | Why |
| --- | --- |
| A text box is at least its line box tall (`line_height`, else 1.45 × size) and wide enough for its text | otherwise the renderer clips the glyphs; preflight now refuses the first case |
| `alignx` / `aligny` are in 0..1 | `2` is 200 %: the label draws outside its own box while `/snap` reports it fine |
| Every asset name is URL-safe (`#`, `?`, spaces encoded) | `check-#0A84FF.svg` was requested as `check-` — the `#` began a URL fragment |
| A `font miss U+XXXX`, `HTTP load failed`, `HTTP request error` or `BEAUTY_ERROR` line in the host log is a failure | an icon that did not load or a glyph that fell back to a box is a wrong render, whatever the mean diff says |
| The page background is sampled at fixed points and matches the reference | the single most visible defect of the first build hid behind a whole-page mean for an hour |
| Icon boxes keep the asset's aspect ratio | stretched tab icons |
| Two widgets with identical text must not overlap | the `+` drawn twice |
| One artwork port, read from the manifest (`artwork.source_prefix`) | compile now writes what bundle checks; do not hard-code another |
| No scene is reported as matching until you have viewed its side-by-side | a green stage is not a seen screen |
| Every text element has the page's **colour and weight**, not only its position | round 2: a date header drawn red and bold where the page has grey regular passed every band number and every presence probe; `compare_screens.py` now reports `wrong_ink_text_widgets` per element — an entry there is a defect until explained |
| The **diff regions** list is empty or every region is explained | a missing event dot or badge is a few dozen pixels a band mean never shows; the script lists the largest regions with their rect and the two colours — look at each one |

## What "looking" missed in round 2, and the rule for it

Three agents looked at every side-by-side and still shipped these. Each is
now a number the script reports, but the rule is what you do with it:

- **A header in the wrong colour and weight** (red bold vs grey regular). The
  per-element probe reports colour distance and ink coverage; compare the
  element, not the band.
- **Event dots missing in the running app** that were present in the scene.
  Diff regions name them; a small region with a coloured page colour and a
  background native colour is a missing element.
- **The page's mock status bar drawn inside the app**, under the shell's real
  one. The shell provides the status bar and the home indicator; the app must
  not draw the artboard's. In the running app, `/snap?q=09:41` must find no
  widget: `compare_screens.py --app-grab ... --port <app port> --forbid-text 09:41`
  reports it.

## For the running app (Part 2)

- Every declared control, when tapped through the instrument, produces an
  observed action and a state change. A control that does nothing is a defect
  even when the screen looks right.
- The walk-through covers **empty states** (an empty day, the list after a
  delete, a hidden calendar) and **round trips** (leave a screen one way, come
  back through the entry point) and asserts the entry view shows the *current*
  state, not the residual one. Both were missed by a 16/16 green walk-through.
- After a delete or hide, assert *no ghost shells*: the region where a card was
  must contain background, not tinted surfaces with empty text.
- Each step asserts where it landed by a screen-unique text, so a mis-tap
  fails instead of being compared as the wrong screen.
- Grab the screen after every step and look at it. A tap that "worked" in the
  log and drew the previous screen is the failure mode.
- Compare every app screen with its page through
  `compare_screens.py --app-grab <grab.png> --app-crop x,y,w,h --port <port> --forbid-text 09:41 <scene>`:
  the artboard cropped out of the shell frame, the same bands and diff
  regions, and the status-bar check. Do not write your own; the report
  carries its regions table per screen.

## Reporting

For each scene: the per-band table, the count of blank text widgets, the host
log problems, and the path of the side-by-side you looked at. State plainly
what still differs. A difference you saw and could not fix is a finding; a
difference you did not look for is a defect the reviewer will find.
