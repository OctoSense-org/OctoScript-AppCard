# Old-kit migration

Scope: all 79 Taskplan, 150 Atro V2 and 246 Camo 2 artboards. Each screen has
a source-image/hierarchy review and a semantic manifest, including screens
without numerical content. Review named candidates and anonymous data shapes;
a parent card classification cannot excuse an unclassified child chart.

Completed on 2026-09-08: all 475 artboards pass the current structural,
semantic, visual and reusable L0 gates. See [validation results](VALIDATION.md)
and [source/native comparisons](http://127.0.0.1:8170/old-kits/).

The reviewed mappings contain 100 native numerical/progress replacements:
32 Taskplan, 38 Atro and 30 Camo. Data comes from the source Sketch geometry
or its resolved vector export, with explicit units, domains and hashes.
These are approximate design samples, not recovered business data or live
feeds. Original photos and illustrations remain Image/Svg assets; source text,
controls, labels, axes and layout containers remain independent widgets.

## Repeat a migration

Run from the repository root, using the Sketch Python environment. Preserve
the original `native/semantic-source` snapshots and the reviewed
`native/source-semantic-review.json`. Detached Sketch UUIDs can change on
re-export; stable original instance paths preserve element identity. Review
reuse requires matching original content and reference-image hashes.

```sh
lab/sketch-to-appcard/.venv/bin/python lab/sketch-to-appcard/migrate_legacy.py --kit taskplan \
  --review lab/sketch-to-appcard/work/taskplan/native/source-semantic-review.json
lab/sketch-to-appcard/.venv/bin/python lab/sketch-to-appcard/sketch_native.py --kit taskplan-native-all
lab/sketch-to-appcard/.venv/bin/python lab/sketch-to-appcard/promote_l0.py --kit taskplan-native-all
lab/sketch-to-appcard/.venv/bin/python lab/sketch-to-appcard/render_splash_makepad.py \
  --kit taskplan-l0-all --studio 127.0.0.1:8002
```

Substitute `atro` or `camo` for the other kits. Set `SKETCHTOOL`,
`CARGO_MAKEPAD` and `BEAUTY_BRIDGE` as described in the shared loop guide.
Studio must launch the release RunItem. Serialize captures because they use
one host request file. Do not modify a kit's inputs during its capture run.

Review the exact source/native screenshot pairs and append current hash-bound
visual receipts. Then run the existing audit, which does not invoke an image
judge or create a new review:

```sh
lab/sketch-to-appcard/.venv/bin/python lab/sketch-to-appcard/run_kit.py --kit taskplan-l0-all --stages audit
```

The audit checks Studio hierarchy, bounds, visibility, text, state and
clipping, L0 tree/component parity, semantic coverage, actual native data and
interaction receipts, capture freshness and visual acceptance. Host-only
inspection fails. A widget's existence and value do not prove its paint is
visible; the visual review remains required. Save failed screenshot pairs and
per-element findings under `native/migration-review` and in repair feedback.

The unchanged structural tolerances are 4 logical points for position,
alignment and spacing, 6 for dimensions, 2 for clipping and 1 for agreement
between inspection methods. Every `.structure.json` records its tolerances
and element differences. Visual acceptance requires a current source/capture
receipt scoring at least 9/10; matching screenshot hashes can retain an
earlier direct review, while changed pixels require another comparison.

## Repairs exercised by this migration

- Preserve stable source identity across repeated Sketch detachment.
- Reuse an original text review when only a derived blank-row count changes;
  retain exact exported text spans, positions and styles in the source hash.
- Bind sibling password-circle masks to the same retained ID as their native
  TextInput, including after repeated imports.
- Convert curved paths, flipped/rotated arcs, bars and bubble sizes to native
  numeric data; preserve source gradients, outlines, caps and radial axes.
- Keep chart paint above its card background and below labels/markers.
- Preserve source masks around numerical curves without clipping tooltips.
- Preserve translucent progress tracks and source toggle colors.
- Clamp native progress corner radii to the track dimensions; a thin track
  with an oversized Sketch radius must remain visible.
- Require finite, build-specific runtime error receipts from Studio.

Final acceptance is recorded by each kit's current audit and screenshot
receipts. Generated outputs alone are not acceptance. Fixed-artboard parity
does not establish responsive layout, full navigation, live data or phone
parity; those require separate validation.

Source review sheets and hierarchy summaries have durable, hash-indexed copies
under each kit's `native/migration-review/source`. Their index maps the original
reviewed temporary paths to those copies. Native comparison sheets and exact
source/capture hashes are retained under `native/l0-captures/migration-review`.
