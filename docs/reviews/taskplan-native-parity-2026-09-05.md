# Taskplan native parity work — 2026-09-05

**Status: passed for all 79 artboards through native Makepad Studio on macOS.**

Final verification on 2026-09-05: all 79 visual verdicts are accepted (43 at 9/10,
36 at 10/10). All structural checks pass within the explicit tolerances, with
14,740 inspected widgets and zero reported structural differences. All 97 input
typing/restoration checks and seven toggle click/restoration checks pass.

Review the [comparison gallery](../../lab/sketch/work/taskplan/native/captures/gallery.html)
and [verification summary](../../lab/sketch/work/taskplan/native/captures/validation-summary.json).
Per-screen screenshots, source mappings, widget dumps/queries/snapshots, state
checks and per-element findings are beside them. The 9/10 acceptance threshold
allows minor visual differences; this is not a claim of pixel-identical output.

This continues the failed L0 beauty-pipeline validation recorded in
[the earlier review](taskplan-beauty-pipeline-2026-09-05.md). It does not replace
or retroactively pass those captures.

## Scope and reference

- All 79 Hifi Design artboards from the user's Taskplan archive. There are 73
  393×852 artboards and six taller artboards.
- Two source artboards share the name `6 1 1 Edit Profile`. Their artifact names
  include the source UUID prefixes `ac615417` and `8424cb02` to prevent overwrite.
- Native Sketch CLI 2026.3 (233959) exports the original document as the visual
  reference. The previous `spec2png` reconstruction is not the reference for this
  path: it had incorrect font substitution and wrapping.
- Archive SHA-256:
  `0cbca109074d6e75ca2600474b962640738893968dedc8f4e376c19ea0a37372`.
- The original archive stays unchanged. Proprietary source, exports, captures,
  and generated designs remain under the ignored `lab/sketch/work/` directory.

## Implementation

`sketch_native.py` uses Sketch to detach symbols in a copy, preserving their
resolved resizing and overrides. It generates checked Splash trees with native
Views and Labels. Rich text uses individually inspected native Labels inside a
DesignText widget. Graphic assets contain individual icons, photos, paths and
backgrounds; compound Boolean shapes remain whole. Text and full-screen
screenshots are not flattened into implementation images.

Instance-qualified source identities survive through the portable VM's element
manifest. Compound paths retain their source ancestry and owning graphic ID.
The native host exposes the generated subtree through Studio's WidgetTreeDump,
WidgetQuery and WidgetSnapshot, with nonce-bound native clipping measurements.

The newer import also validates its cached source and detached document with
archive, tool-version and content hashes. It unpacks those verified documents
again rather than trusting an editable old JSON extraction.

The native host supports source-styled buttons with enforced enabled state,
native toggles, and native TextInput fields with value, placeholder, password
masking and actual keyboard focus. The login and code-input probes passed typing
and source-state restoration through Studio. Radio and tab state mapping passed
the six-screen probe. Search fields and multiline text areas are also native
inputs; all 97 input checks passed in the final full-kit validation. This is a visual port;
complete application workflows and tab navigation are outside this validation.

## Gates and repair

Structural tolerances are explicit: position, alignment and spacing 4 pt;
dimensions 6 pt; clipping 2 pt; agreement among inspection APIs 1 pt. A host-only
tree, missing query, inconsistent state/text, missing explicit source identity,
or stale capture fails inspection. Per-element differences and relation checks
are saved beside each PNG.

Visual acceptance independently requires a current screenshot review, verdict
`accept`, and at least 9/10. The review hash binds both PNGs and the review prompt.
An accepted 8/10 review, a high-scoring `rework`, or old pixels fails the visual
gate. The combined native stage exits unsuccessfully when either gate fails.

`captures/repair-feedback.json` carries the measured failures, visual findings,
screenshots and evidence hashes into the next native author run. Each generated
screen records that input in `.repair-input.json`. Regeneration is explicitly
unverified until new structural and visual checks pass.

## Failures found in the full-kit run

- Graphic-only Splashscreen was incorrectly rejected because it had no text.
  Validation now checks the actual nonempty element tree.
- Studio Click accepts integer coordinates. Floating-point coordinates were
  rejected in a text diagnostic that the bridge silently discarded. Coordinates
  are now integers and the diagnostic becomes a pipeline error. The native
  toggle click/restore test must prove the corrected path in a fresh run.
- macOS constrained a tall window to 1022 logical pixels. The screenshot gate
  rejected it. The dedicated embedded Studio RunItem and RunViewResize captured
  `3_1_8_Add_new_project_fill` at its full frame with complete inspection and zero
  structural differences (Studio build 13). The later screenshot review found
  that larger requests could still produce transparent readbacks when Studio's
  backing texture was smaller than the requested viewport. Full frame dimensions
  alone were insufficient evidence. Studio now accepts explicit minimum backing
  dimensions, and capture rejects blank/transparent frames. A fresh five-screen
  probe produced opaque 786×2638 and 786×2954 captures with visible full content.
- Some compound shapes reuse their object ID for their subpaths. A last-write
  lookup exported only a subpath, losing calendar numerals, icon pieces and
  progress-ring cutouts. The importer now retains the enclosing shape.
- Straight-alpha interpolation introduced dark graphic edges. DesignImage now
  interpolates premultiplied texels; a fresh native screenshot is required to
  establish the fix.
- Group shadows were lost when only leaf graphics were exported. For groups with
  an opaque background matching their bounds, the exporter transfers the group
  shadow to that background and retains effect provenance. Remaining effects
  require screenshot review.

The first broad run reached the tall-artboard failure after many complete
structural passes. Its visual reviews included real rework (e.g. Onboarding 1
6/10 and Project Details 7/10). Those results are repair evidence, not acceptance.
The shared fixes and regenerated assets invalidate earlier acceptance evidence.

The second broad run captured all 79 artboards with geometry/hierarchy passes
and seven verified toggle click/restore checks, but its visual median was only
7/10 (39 accepted verdicts, 35 rework, 5 rejected; accepted verdicts below 9 also
fail the visual gate). These are **failed baseline** results.

That review exposed a Makepad font-cache defect: FontFamily used a script-object
index as its cache identity. GC reused indices across dynamically mounted screens,
causing incorrect weights and glyph metrics. The cache identity now includes the
ordered font resource paths, weights and metrics, and the family retains resource
roots until it is dropped. Its regression test and a fresh multi-screen native
probe passed. The next full run must validate the complete sequence.

Another 49 stroked dividers have zero-height Sketch frames. The importer now gives
their native widgets the visible stroke extent, while retaining the original
source frame. The structural gate requires these lines rather than excluding them
as invisible. A regression test confirms that omitting one fails the gate.

The third full screenshot review had median 9/10: 65 of 79 met the 9/10 accepted
threshold; 14 failed (67 accepted verdicts, 11 rework, one rejection). This remains
a failed baseline. It exposed an asynchronous image-decoding race: HTTP delivery
was being mistaken for texture readiness, allowing missing surfaces and icons.
Native layout evidence now waits for every Image's decoded texture dimensions.
The new gate rejects the old evidence lacking this readiness proof.

The Help & Support heading also wrapped its final word outside a one-line label.
Single-line source frames now disable wrapping. Labels expose their actual text
layout extent, and the structural gate rejects text overflowing the frame beyond
the 2 pt clipping tolerance. Sketch's SVG line count independently establishes
intentional source text overflow, such as the cropped description in Edit Project.
Isolated graphic exports now retain their ancestor/sibling mask chains; the
Forgot Password illustration probe confirms its correct clipped shape.
The fourth repair round regenerated all source controls and consumed the third
round's saved repair findings. Its final native captures and screenshot reviews
passed after the additional fixes recorded below.

The first fourth-round capture stopped on Register Focus. Studio's panel could
later replace a requested artboard viewport with its own 398×600 geometry.
RunViewResize now retains its per-build/window geometry through subsequent
bootstrap messages, and clears it when the build stops. The regression test and
a fresh three-screen probe (Register Focus, multiline Edit Project, tallest
Project Details) passed. The complete rerun uses that corrected Studio build.

The readiness check then stopped at a Share Statistic chart graphic. All exported
PNGs passed Makepad's native decoder. The underlying defect was cache eviction:
the 512-entry image cache could remove a decoded texture before its waiting Image
widget cloned it. Insertion now protects the new texture, and resource-backed
images retry delivery if another completion evicts it within the same event batch.
Decode errors are also reported instead of silently discarded. A regression test
exercises an over-capacity cache with pending consumers. The final repeated-screen
run completed and verified that every required texture was delivered.

The corrected run now has 79 current structural passes, 14,740 inspected native
nodes, all 97 text-input typing/restoration checks, and all seven toggle
click/restoration checks. It also checks the source state of 166 buttons, 84 tabs,
and five radio controls. One eye-open password variant required a final importer
fix: masking follows the displayed source glyphs, rather than the field label.
All 79 final screenshots were then accepted at 9–10/10, and the visual gate
verified their current hashes. The final repair-feedback file has no screens
requiring repair under the defined gates.

Validation completed so far: 56 Splash native/portable Rust tests, 41 Python
pipeline/gate tests, and Makepad regression tests for font-family cache identity,
image-cache delivery, and Studio viewport persistence. All pass.

## Reproduce

From the repository root, with Studio running and the `splashref` mount pointing
to this checkout's `splash-makepad`:

For this kit's 2x captures, start the patched dev Studio with
`MAKEPAD_RUNVIEW_MIN_ALLOC_WIDTH=2048` and `MAKEPAD_RUNVIEW_MIN_ALLOC_HEIGHT=4096`.
These are physical texture-allocation dimensions; each artboard still renders at
its own requested logical size and 2x DPI. The settings support the tall artboards
without depending on the desktop panel's visible size.

```sh
export SKETCHTOOL=/tmp/taskplan-sketch-cli/Sketch.app/Contents/MacOS/sketchtool
export CARGO_MAKEPAD=/tmp/octos-makepad-dev-studio-20260904/target/release/cargo-makepad
lab/sketch/.venv/bin/python lab/sketch/run_kit.py --kit taskplan-native-all --stages author
lab/sketch/.venv/bin/python lab/sketch/run_kit.py --kit taskplan-native-all --stages splash-makepad
```

The native UI builds only through Studio RunItem in release mode. The five-screen
`taskplan-native` configuration remains useful for focused diagnosis; it cannot
establish acceptance for the 79-screen configuration.

Evidence lives in `lab/sketch/work/taskplan/native/{specs,targets,designs,assets,captures}`.
Check the current capture hashes and `visual-gate.json` rather than assuming a
PNG or an earlier score is current. Every configured artboard has current
structural, control and visual evidence in the final verification summary.
