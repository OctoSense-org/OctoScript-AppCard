# Atro native Makepad validation — 2026-09-05

**Status: passed for fixed-artboard parity — all 150 screens pass structural,
native composition and visual gates against the saved capture evidence.**

The scope is all 150 mobile artboards from UI Part I and II in the user's Atro V2
archive. The original Sketch exports are the reference. Source artboards are
750×1624; templates use 375×812 logical points and Studio captures at 2× DPI.
Component sheets and the readme are outside this screen-template scope.

The [comparison gallery](../../lab/sketch/work/atro/native/captures/gallery.html),
[pipeline results](../../lab/sketch/work/atro/native/captures/pipeline-run.json),
and [validation summary](../../lab/sketch/work/atro/native/captures/validation-summary.json)
contain the saved evidence. Capture hashes determine freshness; an earlier
structural pass or screenshot score does not accept a changed implementation.
The current [acceptance scope](../../lab/sketch/work/atro/native/captures/acceptance.json)
also lists the unverified component, responsive layout and application workflow
requirements. The latest pipeline audit rechecks saved evidence; it does not
claim a new Studio capture or a new screenshot review.

The final visual scores are 145 screens at 9/10 and five at 10/10. Nine initial
findings were resolved through full-pair follow-up reviews supported by measured
crops; the initial verdicts and evidence remain visible in the gallery. The fill
heuristic flags zero screens, and the final pipeline exits successfully.

## Composition

The templates are saved in `lab/sketch/work/atro/native/designs/*.splash` and
configured by `lab/sketch/kits/atro-native-all.json`. They use the Splash native
design renderer with source coordinates. They are fixed-size templates, not a
claim of responsive L0–L3 composition or complete application workflows.

Makepad widgets are the first choice: View containers and surfaces, Label text,
TextInput fields, Button hit targets, CheckBox and Toggle selections, Slider
controls, GaussRoundedView glass, and Svg vector geometry. Image widgets hold
source photographs and individual graphics requiring unsupported masks or
effects. Each fallback has a source identity and reason in `composition.json`.
Screen screenshots and source text are not implementation images.

The saved manifests contain 3,009 Text widgets, 3,935 Svg widgets, 919 Image
widgets, and 382 controls (279 Buttons, 48 Inputs, 43 Checkboxes, five Toggles,
three Sliders and four RangeSliders). The source paint mapping also records
5,579 native surfaces. These are instance counts, not unique assets.

The source archive remains unchanged. It contains several Sketch documents; this
configuration explicitly selects `Atro Mobile UI Kit V2.sketch` from the Sketch
directory. Generated designs, purchased graphics and native capture evidence
remain in the ignored `lab/sketch/work/` directory.

## Gates

Every generated element is inspected through WidgetTreeDump, WidgetQuery and
WidgetSnapshot, plus nonce-bound native layout measurements. Source mappings
check hierarchy, visibility, text, bounds, clipping and control state. Host-only
inspection fails. Position, alignment and spacing tolerances are 4 points;
dimensions 6 points; clipping 2 points; inspection API agreement 1 point.
Single-line source text must stay on one line even inside a taller source box.

The latest full capture used Studio release build 51: all 150 screens pass,
26,746 nodes were inspected, and there are zero differences beyond the stated
tolerances.

The visual gate separately checks typography, colors, imagery and effects. It
requires an accepted review of the current screenshot pair scoring at least
9/10. Review inputs are frozen and hashed; partial reviews preserve prior rows
without making stale rows current. Input typing, selection changes and both
range-slider handles are exercised and restored where present.

The native composition gate audits actual Image/SVG nodes against source owners,
asset decisions and fallback reasons. It rejects flattened artboards, paint
containing text/controls, and semantic text/control nodes replaced by containers.
All 150 templates pass; all 919 Image instances are source-linked, comprising
572 source bitmap instances and 347 individual unsupported graphic/effect
instances. Passing this gate does not establish reusable component architecture.

## Pipeline repairs

- Restored foreground labels, icons and controls above deferred glass surfaces.
  Fullscreen glass retains its photo in the scene capture. Nested tints compose,
  including keyboard backgrounds extending beyond the artboard clip.
- Corrected native blur for Retina sampling and calibrated the reconstruction
  kernel against the source Gaussian. The latest change-password probe scores
  9/10; its sampled backdrop regions have mean RGB error 0.39/255.
- Preserved checkbox outline transparency and checked cutouts, and supplied a
  native font fallback for the registration arrow.
- Preserved source mask chains and rotation/reflection order. The radial menu
  now clips to its circle and keeps the bell clapper on the correct side; its
  latest native probe scores 9/10 with zero measured structural differences.
- Fixed SVG strokes joining separate subpaths, which drew lines between alert
  dots. Unpainted source mask outlines retain layout without waiting for
  nonexistent SVG draw areas.
- Prevented unintended wrapping inside oversized single-line source boxes.
  The shop price probe now scores 9/10.
- Added screenshot cleanup after successful evidence copies, content-hash
  caching with file-change invalidation, and stale-state labels in the gallery.
- Bundled the exact five Montserrat styles embedded in the Sketch document
  (version 7.200), with hashes and version receipts. Native text now preserves
  explicit paragraph leading and vertical alignment. The Gallery label needed
  a −5 source-pixel leading adjustment, body copy +6 pixels, and the shop price
  +19 pixels to center it in its source frame. The album and price probes pass.
- Preserved opaque foreground group tints on native text. Onboarding 5's muted
  red subtitle now matches without turning the paragraph into an image.
- Fixed scientific-notation coordinates: Sketch's near-zero gradient endpoint
  was being parsed as a large negative coordinate. Twenty-four artboards contain
  affected gradient values. The plant and primary-button gradient probes pass.
- Added native dashed SVG strokes and fractional Gaussian reconstruction for
  SVG glass. Preserved individual effects over foreground photographs that
  cannot enter Window's shared Gauss scene texture.
- Retained backdrop context for Overlay shadows and unsupported SVG pattern
  paints. The chart markers now score 10/10 and the donut tick ring 9/10.
- Added evidence-informed follow-up review for disputed screenshot findings.
  The original verdict remains intact; crops, measurements and follow-up are
  hash-bound to the full pair. Touch ID's sampled backdrop error is 0.36–0.64
  RGB levels out of 255, with 95th-percentile error of 1–2; the follow-up
  confirms 9/10 parity. This does not override structural failures.

The latest 121 Python regression checks pass, including injected native
composition failures and acceptance-scope checks. Release native SVG/drawing tests
passed (5 SVG and 48 drawing tests), as did 59 release Splash library/doctest
checks. Logs are saved under `captures/validation-tests/`.
UI builds and captures use Studio release RunItems. The final full cycle passes
after the shared fixes; future template, asset or renderer changes must refresh
the affected evidence before claiming acceptance.

## Reproduce

With the patched Makepad dev Studio running on port 8001 and its `splashref`
mount pointing to this checkout's `splash-makepad`, run from `lab/sketch`:

```sh
SKETCHTOOL=/tmp/taskplan-sketch-cli/Sketch.app/Contents/MacOS/sketchtool \
  .venv/bin/python sketch_native.py --kit atro-native-all
CARGO_MAKEPAD=/tmp/octos-makepad-dev-studio-20260904/target/release/cargo-makepad \
  .venv/bin/python run_kit.py --kit atro-native-all --stages splash-makepad
```

Studio uses `MAKEPAD_RUNVIEW_MIN_ALLOC_WIDTH=2048` and
`MAKEPAD_RUNVIEW_MIN_ALLOC_HEIGHT=4096`. Selected repairs can use repeated
`--only` arguments in the importer, renderer and screenshot reviewer. Pass
`--repair-feedback` to the importer to bind saved findings to the next repair.
