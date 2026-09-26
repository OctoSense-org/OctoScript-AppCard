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
    "x": 25.00133648098172,
    "y": 25.74625144175317,
    "w": 247.0628445424476,
    "h": 30.85121107266436,
    "text": "Your allocation",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 36.68198233970541,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 24.540869714435065,
    "y": 74.52595155709342,
    "w": 199.16648291069458,
    "h": 16.530565167243367,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.162358368953116,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "balance",
    "x": 23.90677954190196,
    "y": 112.11764705882352,
    "w": 267.46899867067907,
    "h": 47.40945790080738,
    "text": "$42,860.24",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 47.80777301851033,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "allocation_note",
    "x": 25.129255138545076,
    "y": 178.3506343713956,
    "w": 202.74751929437707,
    "h": 16.08304498269896,
    "text": "A balanced view of your investments",
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
    "id": "allocation",
    "x": 24.0,
    "y": 210.0,
    "w": 358.0,
    "h": 312.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "donut",
    "x": 71,
    "y": 235,
    "w": 263,
    "h": 263,
    "role": "chart.donut",
    "native_candidates": [
      "PieChart",
      "D3PieChart",
      "DonutChart"
    ],
    "data": {
      "path": "data/donut.json",
      "sha256": "0604053413a76e8d15b28b1a9043559922c7df95ad96d309537bb4dd120b4f4c",
      "origin": "fixture",
      "x_key": "x",
      "y_keys": [
        "value"
      ],
      "units": {
        "x": "category-index",
        "y": "percent"
      },
      "domain": {
        "x": [
          0,
          3
        ],
        "y": [
          0,
          100
        ]
      }
    }
  },
  {
    "id": "swatch_0",
    "x": 26.5,
    "y": 543.5,
    "w": 17.5,
    "h": 18,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "class_0",
    "x": 62.30876265093001,
    "y": 543.9746251441753,
    "w": 55.92502756339581,
    "h": 17.425605536332178,
    "text": "Stocks",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 18.340991169852703,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "share_0",
    "x": 330.4720863581195,
    "y": 541.7370242214532,
    "w": 50.66695522983113,
    "h": 21.00576701268743,
    "text": "64%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 23.488628470562748,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "swatch_1",
    "x": 26.5,
    "y": 588.5,
    "w": 17.5,
    "h": 18,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "class_1",
    "x": 62.20616246379473,
    "y": 588.7266435986159,
    "w": 50.105843439911794,
    "h": 17.425605536332178,
    "text": "Funds",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 18.340991169852703,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "share_1",
    "x": 331.6975318596476,
    "y": 586.4890426758939,
    "w": 49.56867877436167,
    "h": 21.00576701268743,
    "text": "28%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 23.488628470562748,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "swatch_2",
    "x": 26.5,
    "y": 633.5,
    "w": 17.5,
    "h": 18,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "class_2",
    "x": 62.008190248667894,
    "y": 633.9261822376009,
    "w": 42.98235725918534,
    "h": 16.978085351787776,
    "text": "Cash",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 17.315386840691442,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "share_2",
    "x": 345.01886510493375,
    "y": 630.79354094579,
    "w": 35.781697905181915,
    "h": 21.453287197231834,
    "text": "8%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 24.10675027241966,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 24.0,
    "y": 684.0,
    "w": 357.0,
    "h": 62.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 24.0,
    "y": 684.0,
    "w": 357.0,
    "h": 62.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 150.04037648950063,
    "y": 706.8719723183391,
    "w": 108.29768467475192,
    "h": 16.08304498269896,
    "text": "View watchlist",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 16.506892052867435,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 24.0,
    "y": 684.0,
    "w": 357.0,
    "h": 62.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
