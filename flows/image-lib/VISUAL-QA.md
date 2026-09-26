# Weather, News and Stock repair / visual QA

All **31 prototypes pass** the structural, semantic, measured-image and Codex
screenshot-review gates: 11 Weather, 10 News and 10 Stock designs.

[Open the reference / Makepad comparison gallery](http://127.0.0.1:8170/ux-images/).
The original generated image appears on the left and the native capture on the
right. Each design exposes its screenshot QA findings, element differences,
widget tree, runtime data and interaction evidence. User preferences and
shortlists remain separate from the agent QA result.

## Scope and evidence

Validation used release Studio builds **53** (original 30) and **55** (new
Weather 11), the `octos-ux-image-studio` RunItem, at **406 × 776 logical pixels**,
captured as **812 × 1552** PNGs. The original 30 pages
were recaptured after the last native change. Their baseline pixels are identical
to the individually reviewed repair captures; the updated stock selection
screenshots were reviewed separately.

| Check | Result |
|---|---:|
| WidgetTreeDump + WidgetQuery + WidgetSnapshot | 31 / 31 |
| Native hierarchy, bounds, visibility, text, state and clipping | 31 / 31 |
| Semantic widget/data/asset mapping | 31 / 31 |
| Measured reference geometry and text ink | 31 / 31 |
| Screenshot review: typography, colors, imagery and effects | 31 / 31 |
| Native button activation | 37 / 37 |
| Range changes, indicator and selected-label styling | 4 / 4 |
| Progress value changes, painted fills and restoration | 3 / 3 |
| Image pipeline regression tests | 36 passed |

Tolerances remain **1 logical pixel** for native geometry/clipping, **3 logical
pixels** for reference geometry/text ink and **16 per RGB channel** for text
color. Source text, widget roles, data arrays and provenance hashes use exact
checks. Artwork crops must match the original decoded pixels exactly.

## Repairs

- Stock and temperature trends use numerical `LinePlot` series with measured
  curves, domains, colors, markers, guides and appropriate area fills. The
  allocation screen uses `DonutChart`; the audio waveform uses numeric samples.
- Progress is a reusable native value widget. QA checks painted fill widths in
  baseline and changed screenshots, catching state updates that fail to repaint.
- Stock range selection now changes the plot viewport, underline and label
  colors together. The tests exercise fixture viewports; these prototypes have
  no historical market feed.
- Missing banners and illustrations were restored with isolated source crops.
  Geometric icons use native SVG assets. Missing chart labels, legend swatches,
  card borders and forecast dividers were restored and measured.
- Crowded or widely spaced text was repaired with better font choices. Number,
  degree and smaller unit text use separate native Labels where required.
- Host-only, stale, missing-element, wrong-widget, wrong-series and unpainted
  state evidence fails the gate. Current visual findings feed `repair.json`.

The final inspected composition contains **914 native elements**: 567 Labels,
220 Views, 33 KitButtons, 37 Buttons, 11 LinePlots, one DonutChart, three progress
widgets, 36 SVG widgets and six Image widgets. The source page is never used
as a screen-sized bitmap.

Weather 11 is a fresh generated input. Two declarative repairs corrected its
font choices and numeric curve sampling; the botanical region uses an exact
isolated source crop. Crowded axis labels use independently measured native
Label regions for OCR verification. Round 004 was deliberately interrupted;
round 003 remained the latest accepted evidence. Resumed round 005 passed all
gates and is pixel-identical to rounds 002 and 003. The original generation
image was preserved throughout. Fine source grain remains a recorded visual
approximation.

## Fidelity limits

The QA pass covers these design prototypes at the stated artboard size. Bundled
font faces approximate the generated lettering; the large “6” in Weather 10
has a different glyph shape. Fine image grain, subtle lighting and some vector
stroke details also differ. Per-design reviews record those approximations.
Weather 07's rain-pattern region is a declared static illustration with an exact
source crop; it supplies no quantitative radar data.

Responsive app layouts, Mate 70 rendering, live feeds and complete navigation
workflows require their own validation. This review does not establish those
capabilities.

## Saved artifacts

- [validation.json](validation.json): design rounds, build, hashes and widget counts.
- [summary.json](summary.json): current gate totals and gallery URL.
- `<design>/page.card`, `page.data.json`, `kit/`: the generated L0 composition.
- `<design>/visual-review.json`: screenshot-specific reviewer, criteria and findings.
- `<design>/rounds/<round>/`: native screenshots, all three Studio inspection
  outputs, per-element differences, data/state exports and interaction captures.
- [qa-work/final-build-comparison.json](qa-work/final-build-comparison.json): exact
  pixel comparison between reviewed captures and the final native build.
- [qa-work/gallery-qa.json](qa-work/gallery-qa.json): browser and published-artifact checks.
