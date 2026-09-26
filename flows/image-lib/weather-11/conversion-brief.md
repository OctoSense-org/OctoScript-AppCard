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
    "x": 0.0,
    "y": 0.0,
    "w": 406.0,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "label_0",
    "x": 26.99169168738396,
    "y": 29.325581557310386,
    "w": 101.2188339569495,
    "h": 11.398755338640212,
    "text": "FIELD / WEATHER",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 11.398755338640212,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_1",
    "x": 26.886146922145652,
    "y": 80.71279901745734,
    "w": 194.7761832081799,
    "h": 42.72556517005937,
    "text": "Portland",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 42.72556517005937,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_2",
    "x": 30.36565548407129,
    "y": 147.68166098514504,
    "w": 150.7035935859848,
    "h": 17.00576701268746,
    "text": "Monday, September 7",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17.00576701268746,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 33.12458654906284,
    "y": 204.06920415224914,
    "w": 146.82249173098126,
    "h": 98.90196078431373,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 33.12458654906284,
    "y": 204.06920415224914,
    "w": 100.71664829106946,
    "h": 98.90196078431373,
    "text": "21",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 98.90196078431373,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 152.19404630650496,
    "y": 206.30680507497115,
    "w": 27.753031973539137,
    "h": 28.641291810841984,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 28.641291810841984,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_4",
    "x": 30.365652917170866,
    "y": 339.5000006080042,
    "w": 124.83656324479023,
    "h": 15.831025674681253,
    "text": "Clear until evening",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.831025674681253,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_22",
    "x": 29.240998471591006,
    "y": 658.6976742995008,
    "w": 219.3074803961531,
    "h": 20.302325819602903,
    "text": "A good day to get outside.",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 20.302325819602903,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "botanical_art",
    "x": 226.5005512679162,
    "y": 179.4555940023068,
    "w": 162.04189636163176,
    "h": 154.39446366782008,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "method": "unrecorded",
      "note": "Record the exact reference-derived artwork or source crop; generic artwork is not fidelity evidence."
    }
  },
  {
    "id": "temperature_card",
    "x": 21.933847850055127,
    "y": 374.57439446366783,
    "w": 358.10363836824695,
    "h": 260.00922722029986,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_curve",
    "x": 71.17309812568908,
    "y": 432.7520184544406,
    "w": 282.4542447629548,
    "h": 143.20645905420992,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ]
  },
  {
    "id": "label_5",
    "x": 41.61218868580807,
    "y": 396.9504038569881,
    "w": 120.33794749255746,
    "h": 10.292964244521267,
    "text": "TODAY'S TEMPERATURE",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 10.292964244521267,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_6",
    "x": 41.61218883298922,
    "y": 427.4767441687911,
    "w": 14.620497783375209,
    "h": 10.151162909801451,
    "text": "26",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 10.151162909801451,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_7",
    "x": 41.61218890328007,
    "y": 455.6744187666127,
    "w": 14.620497783375203,
    "h": 11.279069330728097,
    "text": "24",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728097,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_8",
    "x": 41.612188780626795,
    "y": 483.87209318521735,
    "w": 15.745151721433396,
    "h": 11.279069330728012,
    "text": "22",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728012,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_9",
    "x": 41.61218876969266,
    "y": 512.0697674549423,
    "w": 15.745151721433404,
    "h": 12.40697660523164,
    "text": "20",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.40697660523164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_10",
    "x": 41.612188795500764,
    "y": 541.3953489145778,
    "w": 14.620497783375203,
    "h": 11.279069330728012,
    "text": "18",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728012,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_11",
    "x": 41.612188794684954,
    "y": 569.5930234286826,
    "w": 15.745151721433391,
    "h": 12.40697660523164,
    "text": "16",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.40697660523164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_12",
    "x": 113.59002788652451,
    "y": 565.0813957081824,
    "w": 5.623268411022962,
    "h": 11.279069330728012,
    "text": "1",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728012,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_13",
    "x": 66.35457065119428,
    "y": 565.0813952942447,
    "w": 8.997229798774882,
    "h": 12.40697660523164,
    "text": "0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.40697660523164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_14",
    "x": 58.238644064699514,
    "y": 599.4692958603915,
    "w": 34.22631308265719,
    "h": 15.81722248081789,
    "text": "08:00",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.81722248081789,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_15",
    "x": 158.57617738737017,
    "y": 565.0813954544034,
    "w": 7.87257586071671,
    "h": 11.279069330728097,
    "text": "2",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728097,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_16",
    "x": 206.9362881766361,
    "y": 565.0813954262057,
    "w": 7.872575860716688,
    "h": 11.279069330728012,
    "text": "3",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728012,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_17",
    "x": 253.04709158426903,
    "y": 565.0813955107988,
    "w": 8.997229798774903,
    "h": 11.279069330728012,
    "text": "4",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728012,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_18",
    "x": 301.40720220412976,
    "y": 565.0813951623957,
    "w": 6.747922349081155,
    "h": 10.151162909801451,
    "text": "5",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 10.151162909801451,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_19",
    "x": 347.51800564221793,
    "y": 565.0813954544034,
    "w": 7.872575860716688,
    "h": 11.279069330728097,
    "text": "6",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.279069330728097,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_20",
    "x": 189.9403262829036,
    "y": 599.7621547178863,
    "w": 32.867269961319295,
    "h": 15.2315047636989,
    "text": "14:00",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.2315047636989,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "label_21",
    "x": 319.28484847177583,
    "y": 599.7505737775632,
    "w": 33.97323976424298,
    "h": 14.126759301419904,
    "text": "20:00",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.126759301419904,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 21.933847850055127,
    "y": 697.2364475201846,
    "w": 358.10363836824695,
    "h": 57.28258362168397,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 21.933847850055127,
    "y": 697.2364475201846,
    "w": 358.10363836824695,
    "h": 57.28258362168397,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 124.83656699118258,
    "y": 718.2698966086406,
    "w": 154.07755881154063,
    "h": 19.381265862452864,
    "text": "See weekly forecast",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 19.381265862452864,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 21.933847850055127,
    "y": 697.2364475201846,
    "w": 358.10363836824695,
    "h": 57.28258362168397,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
