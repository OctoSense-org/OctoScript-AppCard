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
    "x": 25.11482281738195,
    "y": 27.519308357348702,
    "w": 118.59316427783902,
    "h": 47.38443804034582,
    "text": "Apple",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 45.51809892757594,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 25.381485246549538,
    "y": 83.87435158501441,
    "w": 210.3572216097023,
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
    "id": "symbol",
    "x": 25.85069821973825,
    "y": 127.70605187319885,
    "w": 102.03087100330761,
    "h": 14.734293948126801,
    "text": "AAPL \u00b7 NASDAQ",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 12.722126160742876,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "price",
    "x": 24.146745193697516,
    "y": 157.22536023054755,
    "w": 261.7643826680004,
    "h": 71.98386167146974,
    "text": "$182.40",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 73.12549826847166,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "gain",
    "x": 26.32720963806211,
    "y": 244.88876080691642,
    "w": 158.8798235942668,
    "h": 20.1014409221902,
    "text": "+2.24  (1.24%) today",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 15.74773209581926,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chart_panel",
    "x": 23,
    "y": 279,
    "w": 359,
    "h": 274,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "price_chart",
    "x": 35,
    "y": 307,
    "w": 337,
    "h": 200,
    "role": "chart.line",
    "native_candidates": [
      "LineChart",
      "LinePlot",
      "D3LineChart"
    ],
    "data": {
      "path": "data/price_chart.json",
      "sha256": "3a72ae40d47bbe91f18b72780ca4f98dd9ea7485f71c7d17cf74187cce4a73d4",
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
    "id": "period_0",
    "x": 57.110239963768976,
    "y": 521.7440922190202,
    "w": 19.16128994837169,
    "h": 13.839769452449568,
    "text": "1D",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.524730093031353,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "period_1",
    "x": 145.67317439739597,
    "y": 521.7440922190202,
    "w": 22.352811466372657,
    "h": 13.839769452449568,
    "text": "1W",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.764923387033276,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "period_2",
    "x": 237.88486127721956,
    "y": 521.7440922190202,
    "w": 20.56229327453142,
    "h": 13.839769452449568,
    "text": "1M",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.764923387033276,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "period_3",
    "x": 331.4572816718047,
    "y": 521.7440922190202,
    "w": 18.32414553472988,
    "h": 13.839769452449568,
    "text": "1Y",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 13.793188116780778,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "open",
    "x": 22.0,
    "y": 569.0,
    "w": 174.0,
    "h": 107.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_label",
    "x": 40.74824646677193,
    "y": 590.1752161383286,
    "w": 33.543550165380374,
    "h": 16.970605187319883,
    "text": "Open",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 13.777904265368841,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "open_value",
    "x": 40.03993470866799,
    "y": 617.4582132564841,
    "w": 108.74531422271224,
    "h": 33.966570605187314,
    "text": "$180.16",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 32.23294989465526,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "volume",
    "x": 207.0,
    "y": 569.0,
    "w": 176.0,
    "h": 107.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "volume_label",
    "x": 229.00293953632004,
    "y": 590.6224783861671,
    "w": 46.07717750826902,
    "h": 13.839769452449568,
    "text": "Volume",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.951059022247247,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "volume_value",
    "x": 227.45125685669683,
    "y": 620.5890489913545,
    "w": 87.70672546857773,
    "h": 27.704899135446684,
    "text": "48.2M",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 32.45162662392701,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 23.0,
    "y": 693.0,
    "w": 359.0,
    "h": 53.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 23.0,
    "y": 693.0,
    "w": 359.0,
    "h": 53.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 148.8272352643272,
    "y": 711.3832853025937,
    "w": 110.98346196251377,
    "h": 16.523342939481267,
    "text": "View watchlist",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 16.483166028314677,
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
    "y": 693.0,
    "w": 359.0,
    "h": 53.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "range_control_0",
    "x": 45.33656409527834,
    "y": 515.7440922190202,
    "w": 42.77996350420294,
    "h": 28.839769452449566,
    "role": "range_option",
    "native_candidates": [
      "RadioButton",
      "Button"
    ],
    "behavior": {
      "event": "click",
      "target": "price_chart",
      "property": "viewport",
      "value": [
        0,
        1
      ],
      "indicator": "range_indicator",
      "indicator_bounds": [
        53.0,
        542,
        22,
        2
      ],
      "label": "period_0",
      "active_color": "#c74714",
      "inactive_color": "#795c50"
    }
  },
  {
    "id": "range_control_1",
    "x": 134.41484413937977,
    "y": 515.7440922190202,
    "w": 46.35281146637266,
    "h": 28.839769452449566,
    "role": "range_option",
    "native_candidates": [
      "RadioButton",
      "Button"
    ],
    "behavior": {
      "event": "click",
      "target": "price_chart",
      "property": "viewport",
      "value": [
        0.15,
        0.9
      ],
      "indicator": "range_indicator",
      "indicator_bounds": [
        144.5,
        542,
        22,
        2
      ],
      "label": "period_1",
      "active_color": "#c74714",
      "inactive_color": "#795c50"
    }
  },
  {
    "id": "range_control_2",
    "x": 226.62653101920336,
    "y": 515.7440922190202,
    "w": 44.589841386444476,
    "h": 28.839769452449566,
    "role": "range_option",
    "native_candidates": [
      "RadioButton",
      "Button"
    ],
    "behavior": {
      "event": "click",
      "target": "price_chart",
      "property": "viewport",
      "value": [
        0.3,
        0.85
      ],
      "indicator": "range_indicator",
      "indicator_bounds": [
        236.0,
        542,
        22,
        2
      ],
      "label": "period_2",
      "active_color": "#c74714",
      "inactive_color": "#795c50"
    }
  },
  {
    "id": "range_control_3",
    "x": 320.1811065429079,
    "y": 515.7440922190202,
    "w": 42.32414553472988,
    "h": 28.839769452449566,
    "role": "range_option",
    "native_candidates": [
      "RadioButton",
      "Button"
    ],
    "behavior": {
      "event": "click",
      "target": "price_chart",
      "property": "viewport",
      "value": [
        0.5,
        0.8
      ],
      "indicator": "range_indicator",
      "indicator_bounds": [
        327.5,
        542,
        22,
        2
      ],
      "label": "period_3",
      "active_color": "#c74714",
      "inactive_color": "#795c50"
    }
  },
  {
    "id": "range_indicator",
    "x": 53,
    "y": 542,
    "w": 22,
    "h": 2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  }
]
```
