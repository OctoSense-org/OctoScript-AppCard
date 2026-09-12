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
    "x": 21.266395331330493,
    "y": 28.431372549019606,
    "w": 247.95810363836824,
    "h": 29.95617070357555,
    "text": "Market overview",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 33.55949343492596,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 21.639521807749006,
    "y": 75.86851211072664,
    "w": 193.34729878721058,
    "h": 16.08304498269896,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.366854634966254,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_0",
    "x": 21.0,
    "y": 112.0,
    "w": 115.0,
    "h": 141.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "index_label_0",
    "x": 34.652995246188496,
    "y": 133.59861591695503,
    "w": 47.867695700110254,
    "h": 13.397923875432525,
    "text": "S&P 500",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.530565167243367,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_value_0",
    "x": 34.29245911731735,
    "y": 166.71510957324105,
    "w": 68.90628445424476,
    "h": 28.61361014994233,
    "text": "5,420",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 26.798869530612382,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_gain_0",
    "x": 34.06193841868833,
    "y": 211.46712802768167,
    "w": 49.83360060152334,
    "h": 14.292964244521338,
    "text": "+0.82%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.661692010874724,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_1",
    "x": 147.0,
    "y": 114.0,
    "w": 112.0,
    "h": 138.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "index_label_1",
    "x": 159.86506522905094,
    "y": 133.59861591695503,
    "w": 48.31532524807056,
    "h": 14.740484429065743,
    "text": "NASDAQ",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.323144827817469,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_value_1",
    "x": 159.47677879324232,
    "y": 166.71510957324105,
    "w": 68.90628445424476,
    "h": 28.61361014994233,
    "text": "17,132",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 26.62898763184463,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_gain_1",
    "x": 159.39821184757477,
    "y": 211.46712802768167,
    "w": 49.29644514397097,
    "h": 14.292964244521338,
    "text": "+0.82%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.661692010874724,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_2",
    "x": 272.0,
    "y": 114.0,
    "w": 112.0,
    "h": 138.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "index_label_2",
    "x": 284.9736172863778,
    "y": 133.59861591695503,
    "w": 29.067254685777286,
    "h": 13.397923875432525,
    "text": "DOW",
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
    "id": "index_value_2",
    "x": 284.64479768396205,
    "y": 166.71510957324105,
    "w": 83.67805953693495,
    "h": 28.61361014994233,
    "text": "39,420",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 26.614113379054636,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_gain_2",
    "x": 284.7344852764612,
    "y": 211.46712802768167,
    "w": 49.29644514397097,
    "h": 14.292964244521338,
    "text": "+0.82%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.661692010874724,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "trend_title",
    "x": 21.619582543246867,
    "y": 279.4901960784314,
    "w": 116.97800768078623,
    "h": 19.215686274509803,
    "text": "Market trend",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 20.56879570309972,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "trend",
    "x": 22.0,
    "y": 310.0,
    "w": 362.0,
    "h": 270.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "market_chart",
    "x": 66,
    "y": 336,
    "w": 300,
    "h": 204,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/market_chart.json",
      "sha256": "f3cbbf8468caa58f5c75c79a20c34ca3d2044eca3a4a4999cd522f422a0729fd",
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
    "id": "quote",
    "x": 22.0,
    "y": 596.0,
    "w": 362.0,
    "h": 80.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_symbol",
    "x": 37.35805186332916,
    "y": 613.7877739331026,
    "w": 53.23925027563396,
    "h": 20.110726643598614,
    "text": "AAPL",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 23.01532377656945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_name",
    "x": 37.69481113726934,
    "y": 644.2191464821223,
    "w": 35.33406835722161,
    "h": 16.978085351787776,
    "text": "Apple",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.930355765440964,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_price",
    "x": 297.4852076504821,
    "y": 612.4452133794695,
    "w": 72.93495038588753,
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
    "id": "quote_change",
    "x": 317.6894027989793,
    "y": 643.7716262975779,
    "w": 52.756987756042065,
    "h": 15.635524798154556,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.443651838380124,
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
    "y": 696.0,
    "w": 364.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 21.0,
    "y": 696.0,
    "w": 364.0,
    "h": 49.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 152.67295435533507,
    "y": 712.2422145328719,
    "w": 103.82138919514884,
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
    "x": 21.0,
    "y": 696.0,
    "w": 364.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "chart_annotation_0",
    "x": 35.417781647577456,
    "y": 330.50749711649365,
    "w": 25.933847850055127,
    "h": 13.397923875432525,
    "text": "5.4K",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.746323242970735,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_1",
    "x": 35.42876480754096,
    "y": 369.88927335640136,
    "w": 26.381477398015434,
    "h": 13.397923875432525,
    "text": "5.3K",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.579704638487458,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_2",
    "x": 35.389277732434095,
    "y": 409.7185697808535,
    "w": 25.933847850055127,
    "h": 13.845444059976932,
    "text": "5.2K",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.178738192701148,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_3",
    "x": 36.535530334284914,
    "y": 449.54786620530564,
    "w": 25.03858875413451,
    "h": 13.397923875432525,
    "text": "5.1K",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 12.98714446483523,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_4",
    "x": 35.42876480754096,
    "y": 489.8246828143022,
    "w": 25.933847850055127,
    "h": 13.397923875432525,
    "text": "5.0K",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.579704638487458,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_5",
    "x": 34.55810615677465,
    "y": 529.2064590542099,
    "w": 27.276736493936053,
    "h": 13.397923875432525,
    "text": "4.9K",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.57922453831902,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_6",
    "x": 61.54967530668488,
    "y": 548.0023068050749,
    "w": 23.695700110253583,
    "h": 13.845444059976932,
    "text": "9:30",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.469251459474119,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_7",
    "x": 118.78994212973092,
    "y": 548.0023068050749,
    "w": 26.381477398015434,
    "h": 13.845444059976932,
    "text": "11:00",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.178738192701148,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_8",
    "x": 174.74363562476952,
    "y": 548.0023068050749,
    "w": 27.72436604189636,
    "h": 13.845444059976932,
    "text": "12:30",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.178738192701148,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_9",
    "x": 231.1449586677684,
    "y": 548.0023068050749,
    "w": 28.17199558985667,
    "h": 13.845444059976932,
    "text": "14:00",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.178738192701148,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_10",
    "x": 288.0269634030763,
    "y": 548.0023068050749,
    "w": 27.72436604189636,
    "h": 13.397923875432525,
    "text": "15:30",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.579704638487458,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_11",
    "x": 345.7381229456074,
    "y": 548.0023068050749,
    "w": 27.72436604189636,
    "h": 13.845444059976932,
    "text": "16:00",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.178738192701148,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
