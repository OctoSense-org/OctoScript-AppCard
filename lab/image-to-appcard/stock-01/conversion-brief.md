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
    "x": 22.115577840175657,
    "y": 31.116493656286046,
    "w": 154.90836377326912,
    "h": 34.431372549019606,
    "text": "Portfolio",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 41.572913318332795,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 23.680396851346682,
    "y": 81.68627450980392,
    "w": 199.16648291069458,
    "h": 16.08304498269896,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.692274141490506,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "portfolio",
    "x": 22.0,
    "y": 116.0,
    "w": 362.0,
    "h": 336.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "balance_label",
    "x": 42.591673574245775,
    "y": 139.8638985005767,
    "w": 86.3638368246968,
    "h": 13.845444059976932,
    "text": "TOTAL VALUE",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 13.598679640852117,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "balance",
    "x": 39.97905699548759,
    "y": 171.19031141868513,
    "w": 250.1962513781698,
    "h": 48.30449826989619,
    "text": "$42,860.24",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 48.7935002972425,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "gain",
    "x": 42.435608558991156,
    "y": 234.73817762399077,
    "w": 176.78500551267916,
    "h": 20.110726643598614,
    "text": "+$842.16  (2.01%) today",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.626311002520477,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "portfolio_chart",
    "x": 41,
    "y": 270,
    "w": 321,
    "h": 167,
    "role": "chart.area",
    "native_candidates": [
      "AreaChart",
      "LinePlot",
      "D3AreaChart"
    ],
    "data": {
      "path": "data/portfolio_chart.json",
      "sha256": "d8d187017da8f7aa6e90c4340c69e4c9acf84dae2eefd00ca11781ba8144cc34",
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
    "id": "watchlist_title",
    "x": 23.59119753614467,
    "y": 478.18915801614764,
    "w": 100.68798235942668,
    "h": 21.00576701268743,
    "text": "Watchlist",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 23.231922148480095,
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
    "y": 514.0,
    "w": 358.0,
    "h": 74.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_0_symbol",
    "x": 39.79648955724894,
    "y": 531.444059976932,
    "w": 51.89636163175303,
    "h": 18.320645905420992,
    "text": "AAPL",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 19.68367974114241,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_name",
    "x": 39.90103022123526,
    "y": 558.7427912341407,
    "w": 36.67695700110254,
    "h": 16.08304498269896,
    "text": "Apple",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.854303173084002,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_price",
    "x": 301.071831087354,
    "y": 530.9965397923876,
    "w": 66.66813671444322,
    "h": 19.215686274509803,
    "text": "182.40",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 21.016141263135086,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_change",
    "x": 324.20021834884443,
    "y": 559.1903114186852,
    "w": 43.391400220507165,
    "h": 12.95040369088812,
    "text": "+1.24%",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1",
    "x": 24.0,
    "y": 597.0,
    "w": 358.0,
    "h": 75.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_1_symbol",
    "x": 39.6706157012187,
    "y": 614.6828143021914,
    "w": 55.02976846747519,
    "h": 18.768166089965398,
    "text": "NVDA",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 20.77280504962166,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_name",
    "x": 39.693484778047676,
    "y": 642.4290657439446,
    "w": 44.28665931642778,
    "h": 13.845444059976932,
    "text": "NVIDIA",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.064920085681333,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_price",
    "x": 301.5194606353143,
    "y": 614.2352941176471,
    "w": 66.22050716648292,
    "h": 19.215686274509803,
    "text": "124.80",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 21.016141263135086,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_change",
    "x": 324.16127667532743,
    "y": 642.876585928489,
    "w": 42.943770672546854,
    "h": 13.397923875432525,
    "text": "+2.16%",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.980557838995201,
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
    "y": 694.0,
    "w": 360.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 23.0,
    "y": 694.0,
    "w": 360.0,
    "h": 54.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 150.0134763691182,
    "y": 712.2422145328719,
    "w": 110.53583241455347,
    "h": 16.978085351787776,
    "text": "View watchlist",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 17.72962479752428,
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
    "y": 694.0,
    "w": 360.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
