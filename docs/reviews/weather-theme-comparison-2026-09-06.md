# Weather theme comparison on Mate 70 Air

The earlier run tested one theme per app, not multiple themes on Weather. Weather used Atro Dark, so its dark page and existing layout made the visual change subtle. The follow-up also found that the main app replaced `light` and `atro_light` with the generic `photo` palette whenever the card used a Photo root, discarding the requested kit.

[Compare Weather with Atro Dark, Atro Light and Taskplan Light](theme-phone-evidence/weather-themes/index.html). All three are actual phone captures using the same Weather exemplar and Cupertino sources. Weather's canonical default is now **Atro Light**, and the phone is left on that variant with an expanded forecast.

The host now preserves the selected kit on Photo pages. Light kits use an opaque overlay made from their own page colors, covering background photography while retaining readable dark text. The separate Satellite panel still displays its imagery. The shared Photo root also supplies the kit's base fill. These changes preserve source fonts, icon ink, forecast colors, spacing, panel shape and shadows.

Studio release runs: Atro Dark **47**, Taskplan Light **48**, Atro Light **49**. Every primary capture exposes **136 inner native widgets**. WidgetTreeDump, WidgetSnapshot and WidgetQuery are saved per variant, including element hierarchy, bounds, visibility, enabled state and text. Query bounds match within 1 logical pixel. Each variant loaded Cupertino weather and expanded the first forecast row through a native button.

The screenshots show Montserrat with purple bars in both Atro modes. Taskplan Light uses Plus Jakarta Sans and Inter, teal bars and flatter panels. Measured background samples are RGB `(5,5,6)`, `(254,254,254)` and `(255,255,255)` respectively. Atro Light and Taskplan Light differ in 11.1% of the recorded UI pixels at a 12-level RGB threshold, excluding satellite imagery; this is evidence of a visible difference, not a beauty or parity score.

The comparison selector is `builtin:weather@<theme>`. It changes only the bundled theme declaration, preserving the exemplar's sources, events and layout. A test checks that invariant and rejects unknown themes. Studio provides `octos-weather-atro-mate70`, `octos-weather-taskplan-mate70` and `octos-weather-atro-light-mate70` under mount `octos`. Clear the previous phone build before launching another. Select Cupertino through the native city editor after launching a variant.

Validation:

- Photo palette/font preservation and dark-image fallback: **2 tests pass**, covering the four light palettes and two dark kits.
- Bundled theme override: **1 test passes**.
- Shared `splash-makepad` L0 kit contract: **8 tests pass**.
- Saved phone evidence validator: **passes**; all three cards match after removing their theme line, native trees are complete, query bounds agree, and expanded condition labels appear.
- Broader L0 app regression suite: **50 passed, 5 failed, 2 ignored**. The previous light/Photo theme failure is addressed; the remaining failures concern accent coverage, helper auditing, two capability expectations and the nav line-count assertion. Logs are alongside the screenshots.

Run the saved-evidence check with `lab/sketch/.venv/bin/python docs/reviews/theme-phone-evidence/weather-themes/validate.py`. [Results](theme-phone-evidence/weather-themes/validation.json) include source and screenshot hashes and per-element records.

This is theming of the existing native Makepad Weather app. Its layout is still the existing app layout, and the separate six semantic kit components are not integrated into this backend. Weather unit conversion and the earlier unrelated app issues remain; no full-app pass is claimed.
