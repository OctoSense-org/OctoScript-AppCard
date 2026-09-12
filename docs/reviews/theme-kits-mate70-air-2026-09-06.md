# Existing apps with theme kits on Mate 70 Air

Follow-up: [Weather now has a same-app comparison across three themes](weather-theme-comparison-2026-09-06.md). Its default is Atro Light, and the light-theme Photo fallback is fixed. The results below describe the earlier run.

The existing Weather, Stocks and News apps render with three different theme kits on the connected Huawei Mate 70 Air. The theme integration and native inspection checks pass. Full app validation does **not** pass: Weather unit conversion, News scrolling and six broader L0 tests remain open.

[Open the side-by-side phone comparison](theme-phone-evidence/index.html). [Machine-readable results](theme-phone-evidence/validation.json) include font hashes, widget counts, bounds differences and the final release package hash.

| Existing app | Theme | Source typefaces | Final Studio build | Inner native widgets |
|---|---|---|---:|---:|
| Weather | `atro` | Montserrat | 46 | 136 |
| Stocks | `camo` | DM Sans | 45 | 111 |
| News | `taskplan_light` | Plus Jakarta Sans body, Inter headings | 44 | 138 |

These are the real Octos app's existing L0 layouts, sources and events. They use native Makepad Labels, Buttons, TextInput, layout Views, StockPlot and weather widgets. Kit palettes supply colors, shapes and spacing; the new typography bridge reads the native kit token registries for source fonts and body scale. This is not a migration to the six semantic kit component classes in the separate `splash-makepad` host, nor a claim of Sketch artboard parity. Atro Light and Camo Light are registered but were not exercised on this phone in this run.

**Changes made**

- Added the chosen theme declarations to the canonical Weather, Stocks and News exemplar cards.
- Added [l0_pack_theme.rs](../../app/app/src/app/l0_pack_theme.rs) and connected it to palette assembly and native text style emission. Explicit card theme axes retain precedence. The existing mode-aware palette exports remain responsible for colors and shapes.
- Bundled the kits' source fonts under [the Makepad widget resources](../../aichat/widgets/resources/theme-kits/). All 17 TTF files in the signed release HAP match both the widget resources and the original kit resources byte for byte; source license files are included in the resource directory.
- Fixed the app's shared-node decoder to read the newly introduced `kit` and `kit_index` attributes. The first fresh main-app build exposed the missing fields.
- Fixed the font resource namespace. The isolated Splash VM registers `makepad_widgets`, so application-crate resource references produced a blank screen. The earlier failed capture is retained and is rejected by the saved-evidence validator.
- Fixed Label wrapping on reload in [label.rs](../../aichat/widgets/src/label.rs). An omitted `flow` was reset from Flow's non-wrapping type default during complete reload. Making wrapping explicit in the Label script prototype preserves its initial behavior. This also lets long stock company captions wrap after updates.
- Added the three phone RunItems to [app/makepad.splash](../../app/makepad.splash), using [theme-apps-ohos.sh](../../tools/theme-apps-ohos.sh) and the existing device release/install path. Each app uses a separate review user store.

**Phone validation**

Studio on port 8002 launched the signed release app `dev.makepad.octos_app`. Each replacement run cleared the previous phone build. The framebuffer is 1320 × 2523, with a logical viewport of 406 × 776. Screenshots are unmodified device captures.

WidgetTreeDump confirms inner descendants of Splash, independently of the surrounding chat host. WidgetSnapshot supplies text, visibility, enabled state and bounds. WidgetQuery resolves a live content label in each app. The saved-evidence check requires at least 20 inner descendants and rejects a missing or host-only tree. Query/snapshot bounds may differ by at most 1 logical pixel; visible text/control bounds may extend beyond the phone's horizontal viewport by at most 2 logical pixels. Vertical overflow is expected for the scrolling app body and is not counted as a layout pass. These checks do not measure glyph clipping; the screenshots were also inspected.

Per-element inspection is saved beside each primary capture:

- [Weather elements](theme-phone-evidence/weather/final-ready.elements.json), [query](theme-phone-evidence/weather/final-place.query.json), [actions](theme-phone-evidence/weather/actions.json).
- [Stocks elements](theme-phone-evidence/stock/final-movers.elements.json), [query](theme-phone-evidence/stock/final-ticker.query.json), [actions](theme-phone-evidence/stock/actions.json).
- [News elements](theme-phone-evidence/news/fixed-feed.elements.json), [query](theme-phone-evidence/news/fixed-lead.query.json), [actions](theme-phone-evidence/news/actions.json).

News' lead headline was 45 logical pixels high on initial load, then clipped to 24 after returning before the repair. On build 44 it remains 45 before and after the transition, with identical x/y/width/height within a 1 px tolerance. [The per-element difference record](theme-phone-evidence/news/headline-reload.differences.json) and before/after screenshots are in the comparison page.

| Interaction | Observed result |
|---|---|
| Weather city editor → search Cupertino → select California | Native TextInput and search results work; live weather loads |
| Weather forecast row expansion | Reveals “Partly Cloudy” and moves subsequent rows down |
| Weather unit toggle | **Fails:** event changes `units`, but 25°, high 26° and low 13° remain unchanged |
| Stocks mover → quote → 1D chart range | Quote loads; selected chip becomes Camo blue and the native chart changes |
| Stocks add/remove watchlist and Back | Actions and visible state changes work across builds 42 and 45 |
| News open story → Save → Back | Story opens, append event succeeds, and inspection confirms the saved reading-list row |
| News native swipe over feed | **Fails:** gesture opened a story and changed the scroll position; reading-list access by scrolling is not validated |

Weather GPS behavior was not validated; the city was selected manually. Some quote fields were unavailable and display em dashes. On initial restore, a stock watchlist row rendered empty; opening its quote loaded the correct data. News' Save label is static in the existing card; it does not become a selected-state indicator. These observations prevent a blanket app-level pass.

**Checks run**

- `cargo test -p octos-app --release --lib l0_pack_theme::tests -- --nocapture`: **1 passed**. [Log](theme-phone-evidence/theme-tests.log).
- `cargo test -p makepad-widgets --release --lib label::tests::label_keeps_wrapping_after_complete_reload -- --nocapture`: **1 passed**. [Log](theme-phone-evidence/label-reload-tests.log). The test also emits shader-registration diagnostics from the headless VM; phone rendering was checked separately.
- `cargo test -p octos-app --release --lib l0_ -- --nocapture`: **49 passed, 6 failed, 2 ignored**. [Log](theme-phone-evidence/l0-app-tests.log).
- `python3 docs/reviews/theme-phone-evidence/validate.py`: passes the recorded native inspection, font packaging and headline reload checks; records whole-app validation as not passed.
- Shell syntax checks and root/aichat `git diff --check`: pass.

The six broader failures are `l0_theme_axes_are_all_answered` (accent coverage), `light_is_the_only_mood_that_inverts_the_ink` (light-theme/Photo fallback coverage), `every_call_the_lowering_emits_has_a_helper` (helper audit), `a_live_source_without_its_capability_is_visibly_wrong` (error/placeholder expectation), `a_watch_row_reveals_its_own_remove` (bare-VM capability setup), and `nav_is_generated_from_an_l0_spec` (line-count expectation). This run did not establish a clean baseline for that broader suite.

To repeat the device check, use Studio mount `octos` and RunItem `octos-weather-mate70`, `octos-stock-mate70` or `octos-news-mate70`. Clear the previous phone build first. The current phone is left on Weather with Atro and an expanded Cupertino forecast.
