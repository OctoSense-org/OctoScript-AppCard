# Native kit components on Mate 70 Air

This run composes the existing Weather, Stocks and News apps from selected ported kit components. It keeps live L0 data, notification payloads and native Makepad controls. These are adaptive layouts, not copies of source Sketch artboards.

| App | Theme | Components used |
|---|---|---|
| Weather | Atro Light | KitButton, KitFormField containing native Button, TextInput and Label children |
| Stocks | Camo Dark | CamoTrackRow for ten movers, KitTabBar for five chart ranges, KitButton for add actions |
| News | Taskplan Light | Eight TaskplanProjectCard instances for the lead and feed; KitButton for story actions |

The kit class implementation is shared between `splash-makepad/crates/splash-widgets/src/kit_shared.rs` and Octos's Makepad widget crate. The app adapter is `app/app/src/app/l0_kit_components.rs`. It selects source recipes, maps data slots and event payloads, then emits real native widgets. Maps, charts, weather symbols and imagery continue to use the existing native app widgets.

`lab/sketch/export_app_recipes.py` extracts source component styles, IDs, source screen names and kit hashes into `splash-makepad/components/l0/native/app-recipes.json`. The beauty pipeline refreshes this file during promotion. Run the exporter with `--check` to reject stale recipes. The app adapter currently recognizes Weather, Stocks and News ledgers and the five Atro/Camo/Taskplan theme variants; other ledgers retain their existing composition.

Atro buttons use the source filled pill and native text-button composition; Camo quote rows adapt its title/subtitle and trailing lane; Taskplan story cards adapt the project title/status/metadata composition. Source artboard positions are replaced by flowing app layouts. Task dates, progress and avatars are not invented when a news story has no corresponding data. This is partial component adoption, not a claim that every screen element is a ported kit component.

Fixes made during this run:

- Registered shared native kit classes in Octos after the widget prelude is available.
- Preserved the L0 evaluation marker when a class name ends in `Card`, fixing blank News screens.
- Exposed native selection values to Studio snapshots.
- Kept live value IDs and original app action payloads through component composition.
- Sized the News feed and Weather foreground to their contents so the scroll canvas includes the added controls/cards.
- Preserved Atro input surface and ink in native focus/typing states.
- Adapted Camo's filled source tab surface and white ink together, and used its primary text-button recipe for add actions.

Validation uses Studio RunItem release builds on the Huawei Mate 70 Air, WidgetTreeDump, WidgetSnapshot and WidgetQuery. `validate.py` rejects host-only captures; checks source hashes, actual component classes, descendant binding paths, native control types, selection, hit targets and clipping; and writes component mappings plus per-element differences beside every screenshot. Tolerances are 1 logical pixel for query/bounds agreement and 2 for component/canvas containment. Native control height is at least 40 logical pixels (44 for ordinary buttons and tabs).

The comparison page shows the earlier theme-only phone captures beside the new component captures. Data may differ because both runs use live services. Visual approval remains with the user. This run does not validate unrelated behavior such as weather unit conversion, news swipe gestures, missing reading-list metadata or unavailable stock fields. Search is captured before choosing a location, so the weather header can still show unavailable location data at that step.

Use `python3 -m http.server 8170 --bind 127.0.0.1 --directory docs/reviews/theme-phone-evidence` and open `/components/`. Review notes are local to the browser and can be exported as JSON.
