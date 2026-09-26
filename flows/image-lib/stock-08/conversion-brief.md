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
    "x": 25.31350132353865,
    "y": 34.228242074927955,
    "w": 168.34420128486468,
    "h": 37.99193083573487,
    "text": "Compare",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 36.77521096227417,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 25.82911479450985,
    "y": 79.84899135446686,
    "w": 200.95700110253583,
    "h": 16.07608069164265,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.46563168169564,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "compare_0",
    "x": 24.0,
    "y": 115.0,
    "w": 173.0,
    "h": 153.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_0",
    "x": 43.634208739219176,
    "y": 137.99308357348704,
    "w": 67.56339581036383,
    "h": 22.337752161383285,
    "text": "AAPL",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.196788801976123,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_0",
    "x": 43.27098382951508,
    "y": 179.58847262247838,
    "w": 132.68334086379937,
    "h": 34.86109510086455,
    "text": "$182.40",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 33.21257108069921,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "change_0",
    "x": 44.75077365633344,
    "y": 231.4708933717579,
    "w": 58.61080485115766,
    "h": 16.07608069164265,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 16.520917339000768,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "compare_1",
    "x": 209.0,
    "y": 116.0,
    "w": 172.0,
    "h": 151.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "symbol_1",
    "x": 227.3555023213936,
    "y": 137.99308357348704,
    "w": 71.1790833900395,
    "h": 21.89048991354467,
    "text": "NVDA",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.164645153117778,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price_1",
    "x": 226.79909849324164,
    "y": 179.58847262247838,
    "w": 131.63887191855866,
    "h": 34.86109510086455,
    "text": "$124.80",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 33.21257108069921,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "change_1",
    "x": 228.27888832006,
    "y": 231.4708933717579,
    "w": 58.16317530319735,
    "h": 16.07608069164265,
    "text": "+2.16%",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 16.520917339000768,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "performance_title",
    "x": 25.439137729633696,
    "y": 293.64034582132564,
    "w": 197.3719179749978,
    "h": 22.7850144092219,
    "text": "Relative performance",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 19.499092503845137,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "comparison",
    "x": 25.0,
    "y": 326.0,
    "w": 356.0,
    "h": 261.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "comparison_chart",
    "x": 66,
    "y": 379,
    "w": 301,
    "h": 179,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/comparison_chart.json",
      "sha256": "869f248fc2492e45db6caa2235eb2d7241423bcfbf8c4b956fdd3a91835246f1",
      "origin": "measured_image",
      "approximate": true,
      "x_key": "x",
      "y_keys": [
        "y0",
        "y1"
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
    "id": "apple_return",
    "x": 25.0,
    "y": 598.0,
    "w": 171.0,
    "h": 82.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "apple_return_label",
    "x": 43.68164193717739,
    "y": 613.8801152737752,
    "w": 89.04961411245866,
    "h": 16.523342939481267,
    "text": "Apple / 1 month",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.139245051259035,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "apple_return_value",
    "x": 43.49788402556791,
    "y": 638.4795389048991,
    "w": 82.52682602701789,
    "h": 25.468587896253602,
    "text": "+4.2%",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 29.370519713779142,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "nvidia_return",
    "x": 207.0,
    "y": 598.0,
    "w": 174.0,
    "h": 82.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "nvidia_return_label",
    "x": 225.0517651651913,
    "y": 613.8801152737752,
    "w": 97.10694597574421,
    "h": 13.839769452449568,
    "text": "NVIDIA / 1 month",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.132358722827643,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "nvidia_return_value",
    "x": 225.06404817867318,
    "y": 638.4795389048991,
    "w": 81.16436984859176,
    "h": 25.468587896253602,
    "text": "+8.6%",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 29.350913225318678,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 53.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 53.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 155.11072066480403,
    "y": 714.514121037464,
    "w": 101.58324145534729,
    "h": 15.628818443804034,
    "text": "View watchlist",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.305797026292199,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 53.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "chart_annotation_0",
    "x": 44,
    "y": 344,
    "w": 56,
    "h": 15,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "chart_legend_line_0",
    "x": 44,
    "y": 349.5,
    "w": 18,
    "h": 2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "chart_legend_label_0",
    "x": 67.93495038588753,
    "y": 344.6282420749279,
    "w": 30.753031973539137,
    "h": 12.945244956772335,
    "text": "AAPL",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 12.582322576558889,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_1",
    "x": 36.557599487088765,
    "y": 372.8057636887608,
    "w": 24.14332965821389,
    "h": 12.497982708933717,
    "text": "20%",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 11.618069818355309,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_2",
    "x": 118,
    "y": 344,
    "w": 57,
    "h": 15,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "chart_legend_line_1",
    "x": 118,
    "y": 349.5,
    "w": 18,
    "h": 2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "chart_legend_label_1",
    "x": 143.1367144432194,
    "y": 344.6282420749279,
    "w": 30.753031973539137,
    "h": 12.945244956772335,
    "text": "NVDA",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 12.582322576558889,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_3",
    "x": 37.90386806983151,
    "y": 417.53198847262246,
    "w": 22.800441014332964,
    "h": 12.0507204610951,
    "text": "10%",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 10.7342939481268,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_4",
    "x": 42.739319873730686,
    "y": 461.81095100864553,
    "w": 17.87651598676957,
    "h": 12.497982708933717,
    "text": "0%",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 11.618069818355309,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_5",
    "x": 34.251905538111004,
    "y": 505.64265129682997,
    "w": 26.82910694597574,
    "h": 12.497982708933717,
    "text": "-10%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 11.618069818355309,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_6",
    "x": 32.39898560408134,
    "y": 549.4743515850143,
    "w": 28.61962513781698,
    "h": 12.497982708933717,
    "text": "-20%",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 11.618069818355309,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_7",
    "x": 68.78846195817493,
    "y": 561.1031700288185,
    "w": 32.20066152149945,
    "h": 12.945244956772335,
    "text": "Apr 20",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 9.67768709533531,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_8",
    "x": 134.6684117334221,
    "y": 561.1031700288185,
    "w": 31.30540242557883,
    "h": 11.156195965417867,
    "text": "Apr 27",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 7.746241721551686,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_9",
    "x": 198.76857325717413,
    "y": 561.1031700288185,
    "w": 27.276736493936053,
    "h": 12.945244956772335,
    "text": "May 4",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 9.67768709533531,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_10",
    "x": 261.96330719994234,
    "y": 561.1031700288185,
    "w": 30.20463853283167,
    "h": 12.945244956772335,
    "text": "May 11",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 9.636960374260779,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_annotation_11",
    "x": 325.9045045029214,
    "y": 561.1031700288185,
    "w": 31.753031973539137,
    "h": 12.945244956772335,
    "text": "May 18",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 9.576508976199552,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
