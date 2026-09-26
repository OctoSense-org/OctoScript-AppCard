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
    "x": 23.809971180924254,
    "y": 30.221453287197228,
    "w": 217.37105133885643,
    "h": 36.66897347174164,
    "text": "Hour by hour",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 33.910824972187974,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 25.260154816916124,
    "y": 75.42099192618224,
    "w": 131.574421168688,
    "h": 17.425605536332178,
    "text": "Monday, September 7",
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
    "id": "current",
    "x": 21.0,
    "y": 106.0,
    "w": 364.0,
    "h": 127.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature",
    "x": 45.44873208379272,
    "y": 127.33333333333334,
    "w": 141.42227122381476,
    "h": 81.86851211072664,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 38.88835260671946,
    "y": 127.33333333333334,
    "w": 122.31247935698153,
    "h": 81.86851211072664,
    "text": "24",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 105.61239258461468,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 151.61474168800095,
    "y": 127.78085351787774,
    "w": 43.0517745116704,
    "h": 30.85121107266436,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 110.86951668713026,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "condition",
    "x": 224.2872284150835,
    "y": 151.05190311418684,
    "w": 113.66923925027562,
    "h": 21.453287197231834,
    "text": "Partly cloudy",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 18.116742108429193,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 224.4642290431645,
    "y": 182.37831603229526,
    "w": 62.63947078280044,
    "h": 16.978085351787776,
    "text": "Cupertino",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 13.923058564935234,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "hourly_title",
    "x": 23.769640096068027,
    "y": 257.5617070357555,
    "w": 162.46085997794927,
    "h": 21.453287197231834,
    "text": "Temperature trend",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 18.31164558398094,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "hourly_title_detail",
    "x": 316.4458358068331,
    "y": 262.48442906574394,
    "w": 69.35391400220507,
    "h": 12.502883506343714,
    "text": "Next 12 hours",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 11.191455926087357,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "timeline",
    "x": 21.0,
    "y": 289.0,
    "w": 364.0,
    "h": 266.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_chart",
    "x": 31,
    "y": 341,
    "w": 344,
    "h": 175,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/temperature_chart.json",
      "sha256": "7cc2fd9c393e77b24597d8b323ec4188d40e27b2e54f6cb00b56e1b7e6b3a08c",
      "origin": "measured_image",
      "approximate": true,
      "x_key": "x",
      "y_keys": [
        "y0"
      ],
      "units": {
        "x": "normalized image plot position",
        "y": "normalized image plot height"
      },
      "domain": {
        "x": [
          0,
          1
        ],
        "y": [
          0,
          1
        ]
      }
    }
  },
  {
    "id": "hour_0",
    "x": 49.2012660598827,
    "y": 523.836216839677,
    "w": 33.09592061742006,
    "h": 12.055363321799307,
    "text": "12 PM",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 11.177089487157845,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "hour_1",
    "x": 144.47566391746878,
    "y": 523.836216839677,
    "w": 28.17199558985667,
    "h": 12.055363321799307,
    "text": "3 PM",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 11.126192433424457,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "hour_2",
    "x": 241.03024832003356,
    "y": 523.836216839677,
    "w": 28.17199558985667,
    "h": 12.055363321799307,
    "text": "6 PM",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 10.782603975846392,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "hour_3",
    "x": 332.7941892995577,
    "y": 523.836216839677,
    "w": 28.17199558985667,
    "h": 12.055363321799307,
    "text": "9 PM",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 11.126192433424457,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity",
    "x": 21.0,
    "y": 568.0,
    "w": 176.0,
    "h": 109.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "humidity_label",
    "x": 36.83161051728476,
    "y": 585.1464821222606,
    "w": 55.02976846747519,
    "h": 16.978085351787776,
    "text": "Humidity",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.471423619088373,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity_value",
    "x": 35.88410320745119,
    "y": 614.6828143021914,
    "w": 78.99334260604843,
    "h": 32.193771626297575,
    "text": "64%",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 38.5452899136565,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind",
    "x": 208.0,
    "y": 568.0,
    "w": 177.0,
    "h": 109.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_label",
    "x": 223.01744286722217,
    "y": 585.1464821222606,
    "w": 34.43880926130099,
    "h": 13.845444059976932,
    "text": "Wind",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.450060191225317,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind_value",
    "x": 222.71003307607495,
    "y": 614.2352941176471,
    "w": 107.40242557883131,
    "h": 32.193771626297575,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_value_number",
    "x": 223.71003307607495,
    "y": 614.2352941176471,
    "w": 35.67695700110254,
    "h": 32.193771626297575,
    "text": "12",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 34.762699753556554,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind_value_unit",
    "x": 266.6824696802646,
    "y": 622.7381776239907,
    "w": 63.429988974641674,
    "h": 23.690888119953865,
    "text": "km/h",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 34.762699753556554,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 21.0,
    "y": 692.0,
    "w": 364.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 21.0,
    "y": 692.0,
    "w": 364.0,
    "h": 55.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 168.6759596400934,
    "y": 711.3471741637832,
    "w": 71.01659289485448,
    "h": 20.110726643598614,
    "text": "My cities",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 17.247657169937252,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 21.0,
    "y": 692.0,
    "w": 364.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "chart_annotation_0",
    "x": 145.5773854560603,
    "y": 317.9769319492503,
    "w": 27.72436604189636,
    "h": 16.530565167243367,
    "text": "27\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 17.374812093780918,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_1",
    "x": 51.22431528949849,
    "y": 346.17070357554786,
    "w": 29.962513781697904,
    "h": 16.978085351787776,
    "text": "24\u00b0",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 18.227647965994066,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_2",
    "x": 242.68451605177012,
    "y": 365.41407151095734,
    "w": 28.17199558985667,
    "h": 16.978085351787776,
    "text": "22\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 17.99534109713024,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_3",
    "x": 334.78268720737947,
    "y": 420.45905420991926,
    "w": 27.06320422475882,
    "h": 16.978085351787776,
    "text": "18\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 17.7549223783977,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
