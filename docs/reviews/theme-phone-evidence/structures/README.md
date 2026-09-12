# App structure variations on Mate 70 Air

Six page recipes change the actual L0 view composition. The review gallery
compares each pair with its previous native kit component layout, using one
theme per app so structure is the variable.

| App / theme | Recipe | Main change |
| --- | --- | --- |
| Weather / Atro Light | `dashboard` | Horizontal conditions card; metrics before forecast |
| Weather / Atro Light | `forecast` | Full week before conditions; sun and moon before metrics |
| Stocks / Camo Dark | `tiles` | Two-column quote cards; detail metrics before chart |
| Stocks / Camo Dark | `chart` | Live leading mover chart on overview; chart before detail summary |
| News / Taskplan Light | `magazine` | Full-width lead plus two-column feed; article actions at bottom |
| News / Taskplan Light | `compact` | Topics first; horizontal story cards; article actions below title |

Open `http://127.0.0.1:8170/structures/`. Select an app and state, inspect bounds,
zoom original screenshots, choose a structure, and export review notes.
Mobile browsers can swipe horizontally between the three comparison columns.

## Reuse

Authored view fragments live at
`splash-makepad/components/l0/pages/{weather,stock,news}/`.
`app/app/src/app/l0_page_recipes.rs` replaces only named top-level view
declarations in a bundled card and appends new named views. Original sources,
state, event declarations, copy and component definitions remain intact.
The materializer is for these bundled, unindented source files; it is not a
parser for arbitrary user-supplied formatting or a new L0 language feature.
Each evidence folder also saves a fully materialized `source.card` that can be
loaded as a standalone L0 card.

The bundled selector accepts, for example,
`builtin:weather@atro_light/dashboard`, `builtin:stock@camo/chart`, and
`builtin:news@taskplan_light/compact`. Theme-only selectors keep their old
behavior. The selector chooses the recipe before normal L0 checking and
rendering. This adds interchangeable authored page compositions; it does not
automatically invent a page layout for every app/kit pair.

The native composer retains Atro KitButton/KitFormField, CamoTrackRow and
KitTabBar, and TaskplanProjectCard. Quotes can flow vertically within grid
cells; story cards can flow horizontally for the compact feed. Native child
Buttons, Labels and TextInputs own controls and values. WeatherIcon and
TempBar are kit shader prototypes extending native View. StockPlot is the
native data-fetching chart widget. No whole-screen bitmap is used.

## Validation

Launch UI exclusively through Studio RunItems in `app/makepad.splash`, named
`octos-{app}-{layout}-mate70`. The capture helper uses the persistent Studio
bridge on port 8168 and requires the Mate 70 Air device connection:

```sh
python3 docs/reviews/theme-phone-evidence/structures/capture.py weather dashboard
python3 docs/reviews/theme-phone-evidence/structures/validate.py
python3 docs/reviews/theme-phone-evidence/structures/build_gallery.py
```

Every state saves the original screenshot, WidgetTreeDump, WidgetSnapshot,
WidgetQuery, generated Splash, per-element measurements, component bindings,
and differences from the previous component layout. Difference matching uses
live source expressions or literal text plus occurrence, because view
reordering changes generated element IDs. Live data differences are recorded
and do not establish parity with an older screenshot.

The gate rejects host-only inspection and checks native types and descendants,
source kit hashes, bindings, visibility, enabled/selected state, control bounds,
scroll containment, expected section order and number of cards, two-column
geometry, compact-feed density, and final-story reachability. Tolerances are
1 logical pixel for query/snapshot agreement and 2 for containment, horizontal
overflow and grid alignment. Kit controls retain the established 40/44 logical
pixel minimum heights. PNG hashes bind captures to each manifest.

Phone interactions exercise city search/add and forecast expansion, opening a
quote and changing 1D/1M, and story open/Back/scroll. Three release regression
tests cover source/state/event preservation for all six recipes, native compound
flow and control bindings, and textual live ticker lowering.

Two defects found during this run were repaired: live chart tickers were being
numerically coerced, producing empty symbols; magazine grid rows inherited
centered alignment and needed top alignment. Rejected observations are under
`rejected/`; final results are in `validation.json`.

Visual preference is pending user review. These are app adaptations, not Sketch
artboard reproductions. Existing unrelated limitations remain: Weather's unit
switch does not convert numeric values, some stock metrics return no data,
and saved news metadata may be unavailable. Scrolling evidence uses Studio's
native Scroll event; it does not certify the earlier touch-swipe behavior.
