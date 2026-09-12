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
    "x": 24.177228650811806,
    "y": 35.5916955017301,
    "w": 240.348401323043,
    "h": 34.878892733564015,
    "text": "Today\u2019s movers",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 33.00624860038575,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 24.388259992926503,
    "y": 80.7912341407151,
    "w": 217.07166482910694,
    "h": 16.530565167243367,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.818480251006202,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "summary",
    "x": 24.0,
    "y": 115.0,
    "w": 358.0,
    "h": 144.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "summary_label",
    "x": 48.02831330569027,
    "y": 143.89158016147636,
    "w": 113.66923925027562,
    "h": 14.292964244521338,
    "text": "LEADING TODAY",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.777771746914837,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "summary_value",
    "x": 47.98047454293511,
    "y": 186.85351787773934,
    "w": 272.50813687217624,
    "h": 35.32641291810842,
    "text": "NVIDIA +2.16%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 41.63302638305389,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "list_title",
    "x": 24.443262105084578,
    "y": 282.6228373702422,
    "w": 123.51708930540242,
    "h": 27.718569780853517,
    "text": "Top gainers",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 24.38535688312651,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0",
    "x": 24.0,
    "y": 318.0,
    "w": 358.0,
    "h": 86.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_0_symbol",
    "x": 44.13131202127391,
    "y": 339.0103806228374,
    "w": 59.506063947078275,
    "h": 21.00576701268743,
    "text": "AAPL",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 24.293952875267756,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_name",
    "x": 43.949428241839286,
    "y": 370.3367935409458,
    "w": 40.257993384785,
    "h": 17.425605536332178,
    "text": "Apple",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.410712860800997,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_price",
    "x": 294.7994303627203,
    "y": 338.56286043829294,
    "w": 68.90628445424476,
    "h": 21.453287197231834,
    "text": "182.40",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 23.362308614333852,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_change",
    "x": 314.1930278871152,
    "y": 369.88927335640136,
    "w": 50.105843439911794,
    "h": 15.18800461361015,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 14.859295362304533,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1",
    "x": 24.0,
    "y": 408.0,
    "w": 358.0,
    "h": 86.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_1_symbol",
    "x": 43.963722973412125,
    "y": 429.8569780853518,
    "w": 62.63947078280044,
    "h": 20.558246828143023,
    "text": "NVDA",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 23.290720813212165,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_name",
    "x": 43.913076157929545,
    "y": 461.1833910034602,
    "w": 48.76295479603087,
    "h": 14.740484429065743,
    "text": "NVIDIA",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.762759805856806,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_price",
    "x": 294.7994303627203,
    "y": 428.961937716263,
    "w": 68.90628445424476,
    "h": 21.453287197231834,
    "text": "124.80",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 23.362308614333852,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_change",
    "x": 313.7453983391549,
    "y": 460.73587081891577,
    "w": 50.626065508573966,
    "h": 15.18800461361015,
    "text": "+2.16%",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 14.859295362304533,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2",
    "x": 24.0,
    "y": 499.0,
    "w": 358.0,
    "h": 86.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_2_symbol",
    "x": 43.902747974677844,
    "y": 519.361014994233,
    "w": 59.506063947078275,
    "h": 21.90080738177624,
    "text": "MSFT",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 24.724872074276576,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_name",
    "x": 43.93922018335366,
    "y": 551.1349480968858,
    "w": 63.53472987872106,
    "h": 15.18800461361015,
    "text": "Microsoft",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.46529889436464,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_price",
    "x": 295.4779492908321,
    "y": 519.361014994233,
    "w": 68.45865490628445,
    "h": 21.453287197231834,
    "text": "416.20",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 23.362308614333852,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_change",
    "x": 309.29724446567093,
    "y": 551.1349480968858,
    "w": 55.02976846747519,
    "h": 15.18800461361015,
    "text": "+0.83%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 14.868937993947819,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3",
    "x": 24.0,
    "y": 590.0,
    "w": 358.0,
    "h": 85.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_3_symbol",
    "x": 43.58799493896232,
    "y": 610.6551326412917,
    "w": 80.54465270121278,
    "h": 21.453287197231834,
    "text": "GOOGL",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 23.362308614333852,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_name",
    "x": 43.949428241839286,
    "y": 642.4290657439446,
    "w": 61.29658213891951,
    "h": 17.425605536332178,
    "text": "Alphabet",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.410712860800997,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_price",
    "x": 295.24705991068055,
    "y": 610.2076124567474,
    "w": 68.45865490628445,
    "h": 21.453287197231834,
    "text": "165.30",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 23.362308614333852,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_change",
    "x": 308.3184116266351,
    "y": 641.9815455594002,
    "w": 56.07008944469703,
    "h": 15.635524798154556,
    "text": "+0.62%",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 15.453667176796712,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 26.0,
    "y": 700.0,
    "w": 354.0,
    "h": 52.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 26.0,
    "y": 700.0,
    "w": 354.0,
    "h": 52.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 149.0919179716526,
    "y": 718.0599769319492,
    "w": 110.08820286659316,
    "h": 16.530565167243367,
    "text": "View watchlist",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 16.3978258546418,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 26.0,
    "y": 700.0,
    "w": 354.0,
    "h": 52.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
