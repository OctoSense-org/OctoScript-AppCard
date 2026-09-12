# Theme KV-cache and generation verification

Four fresh generations on Mate 70 Air used **Z.ai / glm-5.3-flash**, the same
installed release package, embedded Octos core, and thinking disabled throughout.
Runtime source hashes still match the installed-build evidence. Every launch
used Studio RunItem; no runtime code or provider settings changed for this test.

**Cache reuse is verified across theme and app changes.** The identical weather
repeat reused **73,280 of 73,339 input tokens (99.92%)**. Its complete normalized
input hash matches the initial request, and the system/tool prefix hash matches
across all four contexts, including the news repair turn. This is provider-side
prompt caching. Theme and app references remain in the shared prefix; the
context and theme hint follow it. See [runs and hashes](runs.json),
[verification assertions](verification.json), and [the four captures](index.html).

| Fresh run | First streamed text | Completion including repair | Cached input | Output tokens | Repairs |
|---|---:|---:|---:|---:|---:|
| Taskplan weather, initial | 15.031 s | 35.838 s | 0 / 73,339 (0%) | 1,874 | 0 |
| Camo night weather | 10.540 s | 30.831 s | 65,536 / 73,340 (89.36%) | 1,904 | 0 |
| Atro light news | 10.795 s | 49.097 s | 138,752 / 148,298 (93.56%, both turns) | 3,080 | 1 |
| Identical Taskplan weather repeat | 11.322 s | 33.032 s | 73,280 / 73,339 (99.92%) | 1,938 | 0 |

The fixed-settings weather pair improved **24.7% to first streamed text** and
**7.8% to completion**. That is one observed pair, not an isolated causal estimate
of cache speedup: provider load, network and generated output vary. The repeat
generated 64 more tokens. Completion means the model turn completed, not that
every external weather or news source finished loading. Screenshots were taken
after a settling interval.

The earlier **105.3 → 30.2 s** comparison also changed inference from provider
default to fast mode and substantially reduced output length. It establishes
an observed improvement for the combined changes, not a 3.5× cache-only speedup.
The news repair demonstrates that high cache reuse does not guarantee a short
overall generation: an undeclared `copy.comments` required another turn.

## Native theme and layout variety

The [existing six-variation gallery](../index.html) and its
[extracted component, font and geometry evidence](existing-variety.json) verify
three kit families and five IDs: `taskplan_light`, `atro`, `atro_light`, `camo`,
and `camo_light`. The reference exposes 11 IDs; this report does not claim device
coverage for all 11.

| Kit | Native font resources | Native component examples |
|---|---|---|
| Taskplan | Inter, Plus Jakarta Sans | TaskplanKitButtonfae5516b7e |
| Atro | Montserrat | AtroKitButtone46863901c, AtroKitTabBara3c64e36b6 |
| Camo | DM Sans | CamoKitButton72b9f6e0d5, CamoKitTabBare5ef89ec55 |

Layout evidence goes beyond palette changes. The existing Atro stock page puts
the native StockPlot at **y=142**, before metrics whose Open label is at **y=400**.
The Camo stock page puts Open at **y=145** and StockPlot at **y=462**. Those are
Studio logical coordinates. Both retain a real StockPlot and KitTabBar.
News includes a large lead with story cards and a compact list with topics near
the top. In this fresh test the identical Taskplan input itself produced two
arrangements: metrics before forecast initially, forecast before metrics on
repeat. Cache reuse preserves the ability to generate different arrangements.

These observations verify working font, component and structural variety. No
controlled before/after diversity score was measured. Kit exposure and prompt
composition enable that variety; caching reuses the common input computation.

## Native and visual checks

All **four** fresh runs passed completed-turn, hidden-loader, inner-widget,
expected-kit, horizontal-bounds (2 logical pixel tolerance), and numeric-wrap
checks. Studio inspected **110–132 inner native descendants** per page with
WidgetTreeDump, WidgetSnapshot and WidgetQuery. Each capture retains the native
source and per-element differences. A host-only tree would fail.

Screenshot review found readable native Taskplan weather pages, a dark Camo
dashboard, and an Atro magazine page with a lead and two-column stories. Camo
still duplicates the condition label. The news cards have uneven heights and
no article imagery. Structural passes therefore do not imply unrestricted visual
acceptance. These remaining findings are saved in each capture's visual review.

## Reproduce

Use [the generic phone instructions](../../../../tools/OCTOS-OHOS.md),
[these ordered contexts](contexts.json), and the same installed package and
inference settings. Launch each in a fresh session, retain all repair turns,
and capture each completed result with `tools/octos-ohos-capture.py`.
Call a request cold only when its provider cache counters are zero.
Generate this gallery with `tools/octos-ohos-gallery.py` pointed at this folder.
Raw device logs and credentials remain outside the report.
