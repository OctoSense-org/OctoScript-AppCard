# Mate 70 Air theme review — 6 September 2026

[Open the review gallery](index.html): 15 variations and 30 original phone screenshots. Every app has Atro Dark, Atro Light, Camo Dark, Camo Light and Taskplan Light, in that order. Card codes are W1–W5 for Weather, S1–S5 for Stocks and N1–N5 for News.

The gallery supports overview/detail switching, full-resolution zoom, one preferred theme per app, flags, notes and JSON review export. Notes remain in the browser; no review is submitted automatically. Visual approval is pending the user's review.

| App | Studio builds in gallery order | Overview / detail inner widgets |
|---|---|---|
| Weather | 61, 65, 62, 63, 64 | 136 / 138 |
| Stocks | 51, 52, 53, 54, 55 | 111 / 74 |
| News | 56, 57, 58, 59, 60 | 138 / 24 |

All runs used the release Octos app on Huawei Mate 70 Air. The phone is left on Weather, Atro Light, with Cupertino's first forecast row expanded (build 65). Each app retains its existing native Makepad layout and widgets, sources and events; only its theme declaration varies. This does not integrate the separate host's six semantic kit components.

Each `<app>/<theme>/` folder contains the two original PNGs, WidgetSnapshot, WidgetTreeDump, WidgetQuery, per-element inspection, differences relative to Atro Light, generated Splash, reconstructed card source, build log and capture metadata. The original PNG bytes are preserved. `gallery-*.png` are browser screenshots of the comparison rows, not phone evidence.

Capture checks pass for all 30 screens. The validator rejects host-only trees, checks query bounds within 1 logical pixel and horizontal control overflow within 2 logical pixels, confirms source fonts and ink, and verifies same-app sources differ only by theme. Differences in dimensions across themes are recorded for review; they are not treated as parity failures. Viewport: 406 × 776 logical pixels; framebuffer: 1320 × 2523.

Gallery checks pass in desktop Chrome and at a 390px viewport: filters, both screen states, zoom, arrow navigation, persistent picks/notes, JSON download and horizontal rows. All 180 per-screen evidence links resolve. See [capture validation](validation.json) and [browser validation](gallery-check.json).

Review observations: Atro's panel shadows and gradient lead card are prominent; Camo uses larger text and plainer panels; Taskplan fits more content into the viewport. Long stock company names wrap into narrow columns. Check stock chart axis contrast in the light themes. News detail shows story metadata and an outbound link, not the article body.

Known app issues remain: Weather unit conversion, News swipe behavior and five broader L0 test failures. Some stock quote fields are unavailable. No full-app or visual approval is claimed.

To serve the saved page from the repository root:

```sh
python3 -m http.server 8170 --bind 127.0.0.1 --directory docs/reviews/theme-phone-evidence
```

Open `http://127.0.0.1:8170/variations/`. The HTML also works directly from disk. Recheck saved captures with:

```sh
lab/sketch/.venv/bin/python docs/reviews/theme-phone-evidence/variations/validate.py
python3 docs/reviews/theme-phone-evidence/variations/build_gallery.py
```

`capture.py` reuses the persistent Studio bridge at port 8168 and launches only declared `PhoneThemeReview` RunItems. It clears the previous phone run before each replacement. For example, `python3 capture.py news atro atro_light camo camo_light taskplan_light` captures five News variants. `check_gallery.py` uses Playwright and the installed Chrome executable.
