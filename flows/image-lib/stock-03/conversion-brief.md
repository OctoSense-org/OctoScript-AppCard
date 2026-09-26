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
    "x": 23.251833491766895,
    "y": 34.67550432276657,
    "w": 207.7488478290042,
    "h": 32.62478386167147,
    "text": "Market tiles",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 37.00982155852473,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 23.298625695175186,
    "y": 81.1907780979827,
    "w": 223.78610804851158,
    "h": 17.4178674351585,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.733029738732938,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tile_0",
    "x": 23.0,
    "y": 120.0,
    "w": 175.0,
    "h": 259.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_0",
    "x": 39.349142527881824,
    "y": 143.36023054755043,
    "w": 55.4773980154355,
    "h": 18.312391930835734,
    "text": "AAPL",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 19.672334680772874,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_0",
    "x": 38.278519167074435,
    "y": 177.79942363112391,
    "w": 115.09728002681365,
    "h": 32.17752161383285,
    "text": "$182.40",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 30.15024256276368,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_0",
    "x": 39,
    "y": 230,
    "w": 139,
    "h": 90,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/chart_0.json",
      "sha256": "dc4d03cd2f54e86df1c31a5960c8f58669bfec9bb69dfdfcd3afa0a10312ff6a",
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
    "id": "gain_0",
    "x": 38.81704194990686,
    "y": 343.7337175792507,
    "w": 53.83548068939442,
    "h": 15.628818443804034,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.434750598127454,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tile_1",
    "x": 206.0,
    "y": 120.0,
    "w": 175.0,
    "h": 259.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_1",
    "x": 223.57273331625817,
    "y": 143.36023054755043,
    "w": 57.715545755237045,
    "h": 18.312391930835734,
    "text": "NVDA",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 19.672334680772874,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_1",
    "x": 223.17429248422783,
    "y": 178.24668587896252,
    "w": 116.39404476110859,
    "h": 31.730259365994236,
    "text": "$124.80",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 29.671667283989652,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_1",
    "x": 224,
    "y": 228,
    "w": 141,
    "h": 88,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/chart_1.json",
      "sha256": "3369f7be2f28d27df3375f7427f5a1ea1fc17dd179b1356932bd4bb8b370d030",
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
    "id": "gain_1",
    "x": 222.7927861615937,
    "y": 343.7337175792507,
    "w": 49.21058434399118,
    "h": 15.628818443804034,
    "text": "+2.16%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.434750598127454,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tile_2",
    "x": 23.0,
    "y": 388.0,
    "w": 175.0,
    "h": 255.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_2",
    "x": 39.28686421426947,
    "y": 411.71757925072046,
    "w": 55.25965084861485,
    "h": 18.759654178674353,
    "text": "MSFT",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 20.386262677727004,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_2",
    "x": 38.72614871503474,
    "y": 446.1567723342939,
    "w": 113.52812297593152,
    "h": 32.17752161383285,
    "text": "$416.20",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 30.15024256276368,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_2",
    "x": 39,
    "y": 506,
    "w": 139,
    "h": 77,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/chart_2.json",
      "sha256": "56e188a5db947e93964a95dd0a5c1b1d37a2bbce7f8c5789f26d474a8bf8a5a1",
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
    "id": "gain_2",
    "x": 38.87356569477304,
    "y": 609.4074927953891,
    "w": 54.58143212663035,
    "h": 15.181556195965417,
    "text": "+0.83%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.84110634435332,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tile_3",
    "x": 206.0,
    "y": 388.0,
    "w": 176.0,
    "h": 255.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_3",
    "x": 222.82115020211288,
    "y": 411.71757925072046,
    "w": 78.78254663162126,
    "h": 18.759654178674353,
    "text": "GOOGL",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 19.756713567271287,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_3",
    "x": 221.806633830801,
    "y": 446.1567723342939,
    "w": 111.65265115828215,
    "h": 32.17752161383285,
    "text": "$165.30",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 30.15024256276368,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_3",
    "x": 222,
    "y": 514,
    "w": 143,
    "h": 70,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/chart_3.json",
      "sha256": "5ca2417c77e56f3ec50bcd5a2dac3b8d0eff2fb045b3615f57e6655faea1023b",
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
    "id": "gain_3",
    "x": 221.95405081053931,
    "y": 609.4074927953891,
    "w": 52.451651544709605,
    "h": 15.181556195965417,
    "text": "+0.62%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.84110634435332,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "note",
    "x": 24.563819373536262,
    "y": 667.9988472622479,
    "w": 228.71003307607495,
    "h": 19.20691642651297,
    "text": "Four companies. One clear view.",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.914034155083577,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 23.0,
    "y": 701.0,
    "w": 358.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 23.0,
    "y": 701.0,
    "w": 358.0,
    "h": 55.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 148.19689884751702,
    "y": 719.8812680115274,
    "w": 111.43109151047409,
    "h": 16.523342939481267,
    "text": "View watchlist",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 16.388374658183793,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 23.0,
    "y": 701.0,
    "w": 358.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
