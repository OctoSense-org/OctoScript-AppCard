# Conversion brief

This is an implementation brief, not a claim that these instructions were used
to generate the existing reference. Keep the submitted image prompt unchanged.

Apply MAPPING-RULES.md and mapping-rules.json. Resolve every needs_review/unknown
region. Prefer a matching native kit component, then built-in Makepad widgets,
then a reusable custom widget for missing behavior. Use SVG or cropped Image
assets only for artwork. Never substitute a chart or control with an asset.

For new image generation, include the exact text, font files/family/weights,
layout hierarchy, dimensions, spacing, colors, chart samples/units/domains and
selected control states. Preserve a separate machine-readable manifest. Request
complex illustrations as separate assets, or clearly bounded artwork-only regions
with no overlaid UI text. Do not invent missing numerical values from a mockup.

After generation, measure the actual reference. Requested layout is not measured
evidence. Inspect through Studio and run semantic, geometry and visual gates.

```json
[
  {
    "id": "page",
    "x": 0,
    "y": 0,
    "w": 406,
    "h": 776,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "heading",
    "x": 21.259020330177766,
    "y": 42.30449826989619,
    "w": 280.18743109151046,
    "h": 29.95617070357555,
    "text": "The business brief",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 33.70845757826425,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 20.91867398880378,
    "y": 86.60899653979239,
    "w": 230.9481808158765,
    "h": 16.08304498269896,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 12.677293096602188,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "briefing",
    "x": 19.0,
    "y": 122.0,
    "w": 367.0,
    "h": 259.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "lead_tag",
    "x": 44.46680173272942,
    "y": 147.919261822376,
    "w": 106.05953693495039,
    "h": 13.845444059976932,
    "text": "THE BIG PICTURE",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 13.478254969807994,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title",
    "x": 43.90055044288306,
    "y": 185.0634371395617,
    "w": 253.32965821389195,
    "h": 38.01153402537486,
    "text": "A new season",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 47.192155612444246,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title2",
    "x": 44.14573450346011,
    "y": 236.9757785467128,
    "w": 319.1312017640573,
    "h": 37.56401384083045,
    "text": "for small business",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 43.588522730514114,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_meta",
    "x": 44.11798994115032,
    "y": 341.2479815455594,
    "w": 124.41234840132304,
    "h": 17.425605536332178,
    "text": "Analysis \u00b7 7 min read",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.935955468022454,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "markets",
    "x": 19.0,
    "y": 391.0,
    "w": 179.0,
    "h": 120.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "markets_label",
    "x": 42.11303689205876,
    "y": 413.2987312572088,
    "w": 50.105843439911794,
    "h": 14.292964244521338,
    "text": "Markets",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 13.538850849569492,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "markets_value",
    "x": 42.176370208743954,
    "y": 442.8350634371395,
    "w": 84.97528334166759,
    "h": 21.90080738177624,
    "text": "In focus",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 23.247212122940862,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "ideas",
    "x": 206.0,
    "y": 391.0,
    "w": 180.0,
    "h": 120.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "ideas_label",
    "x": 228.42341025225826,
    "y": 413.2987312572088,
    "w": 33.09592061742006,
    "h": 14.292964244521338,
    "text": "Ideas",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.5475519105268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "ideas_value",
    "x": 228.78367543333732,
    "y": 442.8350634371395,
    "w": 133.3649393605292,
    "h": 21.90080738177624,
    "text": "What is next",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 23.560959844394432,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest",
    "x": 19.0,
    "y": 521.0,
    "w": 367.0,
    "h": 150.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "latest_tag",
    "x": 41.33339489700726,
    "y": 540.3944636678201,
    "w": 85.02094818081588,
    "h": 13.845444059976932,
    "text": "TECHNOLOGY",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 13.478254969807994,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_title",
    "x": 41.127870212598864,
    "y": 563.6655132641291,
    "w": 211.7722769338067,
    "h": 26.3760092272203,
    "text": "Better tools for",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 29.05901515367608,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_title2",
    "x": 41.8961653038028,
    "y": 597.677047289504,
    "w": 258.2535832414553,
    "h": 33.08881199538639,
    "text": "everyday creativity",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 30.19457018071532,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_meta",
    "x": 41.77231157278247,
    "y": 639.7439446366782,
    "w": 59.506063947078275,
    "h": 12.95040369088812,
    "text": "4 min read",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 11.780479922197216,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 19.0,
    "y": 684.0,
    "w": 367.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 19.0,
    "y": 684.0,
    "w": 367.0,
    "h": 55.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 141.38524611919416,
    "y": 703.7393310265282,
    "w": 126.20286659316427,
    "h": 20.110726643598614,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 16.816905283430152,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 19.0,
    "y": 684.0,
    "w": 367.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
