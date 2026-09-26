# Old-kit migration validation — 2026-09-08

Taskplan, Atro V2 and Camo 2 are migrated: **475/475 artboards pass** current
Studio structural inspection, whole-source semantic review, visual review and
the reusable L0 component gate. The migration maps **100 chart/progress
regions** to inspected native numerical widgets. Studio inspected 69,654
widget instances across the screens, including repeated layout and graphics.

[Compare all old kits](http://127.0.0.1:8170/old-kits/) or
[open the 31 image designs](http://127.0.0.1:8170/ux-images/).
[validation.json](validation.json) records counts, build IDs, freshness checks,
test logs, code hashes and browser evidence.

| Kit | Accepted artboards | Native chart/progress regions | Studio builds | Generated cards |
|---|---:|---:|---|---|
| Taskplan | 79/79 | 32 | 17, 21 | L0 cards (`work/taskplan/native/l0/`) |
| Atro V2 | 150/150 | 38 | 20 | L0 cards (`work/atro/native/l0/`) |
| Camo 2 | 246/246 | 30 | 18, 19 | L0 cards (`work/camo/native/l0/`) |

All 475 captures passed a final input/runtime fingerprint check. Valid saved
checkpoints retain their original build IDs. Visual receipts bind exact source
and native screenshot hashes; changed screenshots received direct comparison.
No image-judge service was invoked for this migration.

Native replacements include LinePlot, BarPlot, DonutChart, RadarChart,
ScatterPlot and DesignProgressBar. Their actual arrays, values and paint/state
probes are checked. Original photos and illustrations remain Image/Svg assets;
text, controls, labels, axes and layout containers remain separate widgets.
The [migration inventory](semantic-migration-inventory.json) records each
source-to-native numerical mapping and preserves the earlier candidate list.

The migration repaired source-mask clipping around numerical curves, thin
progress tracks with oversized radii, translucent track and toggle colors,
source gradient/arc/bar geometry and retained password-control ownership.
Source review reuse now handles changing detached UUIDs and derived blank-row
counts while retaining original content and exact text spans in the hash.
Failed screenshots and per-element findings remain in each kit's
`native/migration-review` directory. Source review sheets and hierarchy
summaries have 43 durable, hash-verified artifacts across the three kits.

The shared runtime regression also exposed an image progress-probe race.
The capture loop now waits for the requested value and its painted value
before restoration and finalization, and fails on timeout. The failed round
remains intact. A fresh News 09 round verifies the repair, followed by all 31
image-design captures and gates. See the
probe repair receipt (`qa-work/old-kit-migration/image-progress-probe-repair.json`).

| Verification | Result |
|---|---|
| Regression tests | 239 passed: 185 Sketch, 38 image, 16 shared |
| Image designs on the updated runtime | 31/31 accepted; 914 inspected elements; Studio build 22 |
| Old-kit gallery | 475 comparisons, 950 image hashes, 3,788 evidence links verified |
| Image gallery | 31 comparisons, 62 image hashes, 373 evidence links verified |
| Browser behavior | Search, repair filters, comparison alignment and image filters pass; no browser errors |

Acceptance covers the source artboard sizes at the configured 9/10 visual
threshold. Minor glyph, stroke and shadow rasterization remains; a small
Taskplan “Wed” label fits one native line where Sketch wraps its final letter.
Some image designs retain documented flat-color/texture approximations.
Numerical arrays approximate source geometry, rather than recovering business
values or providing live feeds. Responsive layouts, complete application
workflows and Mate 70 native rendering remain unvalidated. Design preferences
are still for the user to review.

The temporary Studio and bridge were closed; the user's existing Studio and
the local galleries remain available. Cleanup evidence (`qa-work/old-kit-migration/cleanup.json`).
See [OLD-KIT-MIGRATION.md](OLD-KIT-MIGRATION.md) to repeat the migration and
audit. The previous validation report (`qa-work/old-kit-migration/previous-VALIDATION.md`)
is retained as historical evidence, including its earlier open migration work.
