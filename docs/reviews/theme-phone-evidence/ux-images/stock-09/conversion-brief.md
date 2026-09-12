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
    "x": 22.796005232835803,
    "y": 32.45905420991926,
    "w": 152.37989574719163,
    "h": 39.80161476355248,
    "text": "Holdings",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 37.37090062984479,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 23.552253407341105,
    "y": 79.44867358708188,
    "w": 207.22381477398014,
    "h": 16.530565167243367,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.934776946831862,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "balance_label",
    "x": 23.857893856052108,
    "y": 128.22837370242215,
    "w": 114.56449834619625,
    "h": 13.397923875432525,
    "text": "TOTAL HOLDINGS",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.8656070166349,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "balance",
    "x": 22.62179872115878,
    "y": 158.21222606689733,
    "w": 286.6904326916542,
    "h": 58.59746251441753,
    "text": "$42,860.24",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 54.43797625585545,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "asset_header",
    "x": 24.506548513647335,
    "y": 254.87658592848902,
    "w": 42.04851157662624,
    "h": 13.397923875432525,
    "text": "ASSET",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 12.8656070166349,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "value_header",
    "x": 274.6499927609069,
    "y": 254.42906574394465,
    "w": 106.05953693495039,
    "h": 14.740484429065743,
    "text": "VALUE / CHANGE",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.739233048548808,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_0",
    "x": 17.0,
    "y": 282.0,
    "w": 372.0,
    "h": 86.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "holding_0_symbol",
    "x": 35.141433098705065,
    "y": 301.86620530565165,
    "w": 61.29658213891951,
    "h": 21.90080738177624,
    "text": "AAPL",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.17915763590504,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_0_name",
    "x": 35.13530599835821,
    "y": 334.98269896193773,
    "w": 38.467475192943766,
    "h": 18.320645905420992,
    "text": "Apple",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.024939966343336,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_0_price",
    "x": 303.32335688999007,
    "y": 302.3137254901961,
    "w": 70.42037033640634,
    "h": 21.453287197231834,
    "text": "182.40",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 23.893270173750533,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_0_change",
    "x": 323.5012397460528,
    "y": 334.98269896193773,
    "w": 50.553472987872105,
    "h": 15.18800461361015,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.295749965736707,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_1",
    "x": 17.0,
    "y": 376.0,
    "w": 372.0,
    "h": 88.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "holding_1_symbol",
    "x": 34.38031425883598,
    "y": 396.29296424452133,
    "w": 64.42998897464167,
    "h": 22.348327566320645,
    "text": "NVDA",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.808636576802666,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_1_name",
    "x": 34.38881105281516,
    "y": 430.7520184544406,
    "w": 46.52480705622933,
    "h": 15.18800461361015,
    "text": "NVIDIA",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.736973522440652,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_1_price",
    "x": 303.22284433517257,
    "y": 396.74048442906576,
    "w": 70.24917309812568,
    "h": 22.348327566320645,
    "text": "124.80",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.118566080096713,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_1_change",
    "x": 323.47793762696443,
    "y": 430.30449826989616,
    "w": 50.553472987872105,
    "h": 15.635524798154556,
    "text": "+2.16%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.907579964366175,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_2",
    "x": 16.0,
    "y": 472.0,
    "w": 373.0,
    "h": 87.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "holding_2_symbol",
    "x": 34.23759281221645,
    "y": 491.6147635524798,
    "w": 60.8489525909592,
    "h": 22.79584775086505,
    "text": "MSFT",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 25.077456803760015,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_2_name",
    "x": 34.61139568229069,
    "y": 526.073817762399,
    "w": 59.506063947078275,
    "h": 15.18800461361015,
    "text": "Microsoft",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 14.52950757683804,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_2_price",
    "x": 304.1856811442489,
    "y": 492.0622837370242,
    "w": 70.696802646086,
    "h": 22.348327566320645,
    "text": "416.20",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.118566080096713,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_2_change",
    "x": 321.68741943512316,
    "y": 525.6262975778546,
    "w": 52.34399117971334,
    "h": 15.635524798154556,
    "text": "+0.83%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.907579964366175,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_3",
    "x": 17.0,
    "y": 567.0,
    "w": 372.0,
    "h": 88.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "holding_3_symbol",
    "x": 33.9992336196442,
    "y": 586.4890426758939,
    "w": 80.09702315325248,
    "h": 23.243367935409456,
    "text": "GOOGL",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 26.343861986442892,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_3_name",
    "x": 35.14241313243653,
    "y": 621.3956170703575,
    "w": 57.267916207276734,
    "h": 17.873125720876587,
    "text": "Alphabet",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 14.555410592395106,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_3_price",
    "x": 303.6704738831329,
    "y": 587.3840830449827,
    "w": 69.80154355016538,
    "h": 22.348327566320645,
    "text": "165.30",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.118566080096713,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "holding_3_change",
    "x": 321.68741943512316,
    "y": 620.9480968858131,
    "w": 52.34399117971334,
    "h": 15.635524798154556,
    "text": "+0.62%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.907579964366175,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 22.0,
    "y": 689.0,
    "w": 362.0,
    "h": 66.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 22.0,
    "y": 689.0,
    "w": 362.0,
    "h": 66.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 145.66867180864327,
    "y": 713.5847750865051,
    "w": 117.6979051819184,
    "h": 17.873125720876587,
    "text": "View watchlist",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 18.259743879405686,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 22.0,
    "y": 689.0,
    "w": 362.0,
    "h": 66.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
