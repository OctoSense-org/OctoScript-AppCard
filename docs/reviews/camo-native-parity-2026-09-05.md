# Camo 2 native Makepad validation

Status: passed for fixed-artboard parity on 2026-09-06. All 246 screens pass
current structural, native composition and visual gates.

The [side-by-side gallery](../../lab/sketch/work/camo/native/captures/gallery.html),
[pipeline audit](../../lab/sketch/work/camo/native/captures/pipeline-run.json),
and [acceptance scope](../../lab/sketch/work/camo/native/captures/acceptance.json)
contain the saved results. Studio release build 63 captured all 246 screens;
29,929 generated nodes were inspected, with zero structural differences beyond
the stated tolerances. The final audit verifies those saved captures and reviews;
it does not claim to perform another capture.

All screenshot pairs have accepted, current reviews: 175 at 9/10 and 71 at
10/10. The frame-fill check flags zero screens. Fifteen initial visual failures
and the two subsequently discovered missing Family emoji cases were repaired.
The final scores require no manual overrides or follow-up score promotions.

The scope is all 246 mobile artboards from the supplied Camo 2 archive: 123 light
and 123 dark screens across Finance, Food Delivery, Medical, Music, Taxi, Video
and Onboarding. Scroll and state variants are included. Component sheets and
marketing pages are outside this screen-template scope. Sketch page IDs preserve
both themes even though their page names are identical.

The configuration is [camo-native-all.json](../../lab/sketch/kits/camo-native-all.json).
Templates are saved under `lab/sketch/work/camo/native/designs/`, with source
mappings, original Sketch exports and native captures in adjacent directories.
Artboards use 375×812 logical points; Studio captures at 2× DPI.

These are source-mapped, fixed-size templates. Responsive layout, reusable L0–L3
component architecture and complete application workflows require separate work
and evidence. Native control interaction checks establish only the behavior
actually recorded in their capture artifacts.

The renderer uses native View, Label, TextInput, Button, CheckBox, Toggle,
RadioButton and Svg widgets. Image widgets are reserved for source photographs
and individual unsupported graphics or effects, with explicit source ownership
and fallback reasons. Full-screen screenshots and source text are not assets.

The generated manifests contain 29,929 widget nodes: 19,239 containers, 4,672
Text widgets (including 50 shadow labels), 3,835 Svg widgets, 1,213 Image widgets,
844 Buttons, 80 Inputs, 24 Checkboxes, 16 Toggles and six RadioButtons. These are
instances, not unique components or assets.

Every generated element must be inspected with WidgetTreeDump, WidgetQuery and
WidgetSnapshot, plus nonce-bound native layout measurements. Position, alignment
and spacing tolerances are 4 points; dimensions 6 points; clipping 2 points;
inspection API agreement 1 point. Host-only inspection fails. Visual review is
separate and requires a current accepted screenshot pair scoring at least 9/10.

Repairs discovered during the Camo import:

- Preserve duplicate page names using page IDs and explicit artboard names.
- Verify exact font registration before Sketch resolves symbols and exports.
  Archive DM Sans fonts are bundled byte-for-byte. SF Pro Text and Helvetica
  use local font files; platform font files are not embedded in the application.
- Preserve inherited SVG text fill opacity separately from group opacity.
- Recognize inner styling groups as part of their source symbol's native control.
- Map password-circle shapes to editable TextInput masking, preserving circle
  ink, count and spacing through measured source-font bullet geometry.
- Propagate outer button shadows through transparent full-size wrappers to the
  opaque background while keeping labels, icons and hit targets inspectable.
- Resume completed imports only when source, code, configuration and generated
  output hashes match.
- Fit empty keyboard-label line boxes to their source frames, preserving native
  text widgets without inventing overflow from a fallback line-height multiplier.
- Preserve zero-alpha source graphics as inspectable layout containers. Save the
  original graphic export's hash and alpha evidence, and retain compound operand
  bounds as child Views. Empty geometry must not stall Studio inspection.
- Give empty verification-code fields native font metrics and a foreground color
  suited to their artboard background, so typed input remains readable.
- Add native Button hit targets to 370 bottom-navigation items across 74 screens,
  and require those source navigation symbols in the structural gate.
- Distinguish code-cell and dropdown styling prototypes from separate controls.
  Code cells require TextInput; a dropdown's sized inner styling shares its
  owning native Button. A preflight across all 246 source trees found no missing
  mappings for the named control variants recognized by the pipeline.
- Preserve ancestor Multiply/Soft Light blends on individual illustration
  graphics. Unsupported backdrop-dependent paints carry explicit fallback
  receipts; text and controls cannot be flattened into those assets.
- Honor SVG `nonzero` and `evenodd` fill rules in native tessellation. A
  regression checks equal-winding overlaps, opposite-winding holes and path
  reuse, covering the Collection icon found during visual review.
- Measure Apple Color Emoji's optical sizing with CoreText, then retain the
  source baseline and line box in native Labels. Shadowed emoji use native
  CachedView alpha blurring and a separate inspectable foreground Label.
- Match the source's filled unchecked CheckBox and RadioButton styling while
  preserving their native selection state and interaction checks.
- Select an available native font bitmap when an emoji is missing at the
  preferred size. Camo's Family chip exposed a sparse Apple Color Emoji strike;
  a portable font-parser regression verifies fallback without replacing text
  with an image asset.
- Correct the preflight test runner to execute the native import and graphics
  test files separately, instead of passing one filename as a test argument.

Validation checks pass: 137 Python regressions, 49 Splash-Makepad backend tests,
six native SVG tests and 38 font-parser tests. The pipeline doctor also passes
its gate fault-injection checks and tool/input preflight.
The [completion receipt](../../lab/sketch/work/camo/native/completion.json) records
capture counts and validation log hashes. The
[font repair receipt](../../lab/sketch/work/camo/native/native-font-repair.json)
retains the two affected Sketch element IDs, prior findings and final reviews.

The source archive remains unchanged. Purchased source files, generated graphics
and captures remain in the ignored local work directory.
