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
    "id": "screen",
    "x": 0.0,
    "y": 2.0,
    "w": 406.0,
    "h": 771.5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "payment_card",
    "x": 21.991666666666667,
    "y": 59.52412280701754,
    "w": 365.4,
    "h": 441.58223684210526,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "pay_contribution",
    "x": 42.291666666666664,
    "y": 421.5877192982456,
    "w": 164.09166666666667,
    "h": 57.52412280701754,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_contribution_surface",
    "x": 42.291666666666664,
    "y": 421.5877192982456,
    "w": 164.09166666666667,
    "h": 57.52412280701754,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_contribution_control",
    "x": 42.291666666666664,
    "y": 421.5877192982456,
    "w": 164.09166666666667,
    "h": 57.52412280701754,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_46",
    "x": 75.17581382222498,
    "y": 439.65290582695246,
    "w": 103.9548776395918,
    "h": 26.662663035550747,
    "text": "\u652f\u4ed8 \u00a5180",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.396396731995672,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_payment",
    "x": 213.15,
    "y": 421.5877192982456,
    "w": 155.63333333333333,
    "h": 57.52412280701754,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_surface",
    "x": 213.15,
    "y": 421.5877192982456,
    "w": 155.63333333333333,
    "h": 57.52412280701754,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_payment_control",
    "x": 213.15,
    "y": 421.5877192982456,
    "w": 155.63333333333333,
    "h": 57.52412280701754,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_47",
    "x": 252.61847056681137,
    "y": 439.43049437334037,
    "w": 81.91736694883589,
    "h": 27.10748678301093,
    "text": "\u53d6\u6d88\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.79673810470984,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_0",
    "x": 49.05833333333333,
    "y": 81.51864035087719,
    "w": 42.291666666666664,
    "h": 42.297149122807014,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_0.svg",
      "sha256": "a55d6b3117a99886252fd0de5ba8487754bd95800b2e050040539e070b7b56e5",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_36",
    "x": 108.47347913739922,
    "y": 88.1088608380671,
    "w": 126.11896280759153,
    "h": 30.261650200713976,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.63548518064258,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_37",
    "x": 41.941300789394425,
    "y": 139.4809003975383,
    "w": 159.32897753894824,
    "h": 31.05220136072552,
    "text": "2016\u5c4a\u540c\u5b66\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.346981224652968,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_38",
    "x": 41.687690862948905,
    "y": 183.83466509588092,
    "w": 141.34464812962548,
    "h": 57.169074891860284,
    "text": "\u00a5180",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 47.852167402674255,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_39",
    "x": 45.639609098883895,
    "y": 257.834279151711,
    "w": 66.87125066437488,
    "h": 31.052199748288665,
    "text": "\u6536\u6b3e\u4eba",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.3469797734598,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_40",
    "x": 41.94130055006085,
    "y": 295.0310535109565,
    "w": 48.37970786827092,
    "h": 34.43372562382048,
    "text": "\u7528\u9014",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.390353061438432,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_41",
    "x": 45.63961061910013,
    "y": 332.22782985414284,
    "w": 44.681396730239406,
    "h": 26.530393232045352,
    "text": "\u6d3b\u52a8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.277353908840816,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_42",
    "x": 130.70071546318175,
    "y": 262.23321064183756,
    "w": 48.379704644757524,
    "h": 30.03479324182292,
    "text": "\u738b\u5b81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.43131391764063,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_43",
    "x": 137.81051097181341,
    "y": 294.6549944569168,
    "w": 82.23813232044418,
    "h": 31.681444342820345,
    "text": "\u805a\u4f1a\u9910\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.91329990853831,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_44",
    "x": 138.09733019226326,
    "y": 332.22783002631945,
    "w": 185.21714261111518,
    "h": 26.530394038263776,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.277354634437398,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_45",
    "x": 45.63961178791164,
    "y": 376.1876565401814,
    "w": 174.12220919702065,
    "h": 31.052199748288665,
    "text": "\u5df2\u62a5\u540d \u00b7 \u6728\u5149\u9910\u5385",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.3469797734598,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "rsvp_summary",
    "x": 21.991666666666667,
    "y": 516.3333333333333,
    "w": 365.4,
    "h": 108.28070175438596,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_reunion",
    "x": 21.991666666666667,
    "y": 516.3333333333333,
    "w": 365.4,
    "h": 108.28070175438596,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_reunion_surface",
    "x": 21.991666666666667,
    "y": 516.3333333333333,
    "w": 365.4,
    "h": 108.28070175438596,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_reunion_control",
    "x": 21.991666666666667,
    "y": 516.3333333333333,
    "w": 365.4,
    "h": 108.28070175438596,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "group_icon_1",
    "x": 47.36666666666667,
    "y": 540.0197368421052,
    "w": 42.291666666666664,
    "h": 42.297149122807014,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/group_icon_1.svg",
      "sha256": "a863d3bd8d66ea77c53543b8771a29cc3c5e135065d65081e155ae50be06d57e",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_48",
    "x": 115.90748465597336,
    "y": 543.5092519466791,
    "w": 140.83742184879065,
    "h": 26.206002389508896,
    "text": "\u805a\u4f1a\u62a5\u540d\u4ecd\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.985402150558006,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_49",
    "x": 115.90748579111258,
    "y": 576.81825688089,
    "w": 181.51881857903007,
    "h": 26.550053674001834,
    "text": "\u4f60\u5df2\u786e\u8ba4\u53c2\u52a0\u672c\u6b21\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.29504830660165,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 0.0,
    "y": 661.8355263157895,
    "w": 406.0,
    "h": 111.66447368421052,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.833333333333336,
    "y": 677.0625,
    "w": 37.21666666666667,
    "h": 38.91337719298245,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_message.svg",
      "sha256": "94781da8c43a880f37575b7fa2fe3999844efe8aa5d1370e3b505fdf8c7171f6",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.07777777777775,
    "y": 677.0625,
    "w": 37.21666666666667,
    "h": 38.91337719298245,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_calendar.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.3222222222222,
    "y": 677.0625,
    "w": 37.21666666666667,
    "h": 38.91337719298245,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_group.svg",
      "sha256": "a863d3bd8d66ea77c53543b8771a29cc3c5e135065d65081e155ae50be06d57e",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 331.56666666666666,
    "y": 677.0625,
    "w": 37.21666666666667,
    "h": 38.91337719298245,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "a55d6b3117a99886252fd0de5ba8487754bd95800b2e050040539e070b7b56e5",
      "method": "reference_svg",
      "reference_sha256": "b48d6d27efc8b83d1f9e168c3c6ac70e368bd875c82d119e8fa2c25f072cc508",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_34",
    "x": 34.54468264893412,
    "y": 17.74599849909887,
    "w": 52.07801578278904,
    "h": 19.21686281191024,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 13.695176530719216,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_50",
    "x": 34.544683390550695,
    "y": 727.8662628518019,
    "w": 40.98308881572129,
    "h": 27.670675485193705,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.303607936674336,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_51",
    "x": 230.55505554826075,
    "y": 727.8662632219028,
    "w": 40.98308881572128,
    "h": 27.670675485193705,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.303607936674336,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_52",
    "x": 330.4093974770221,
    "y": 727.8662628518019,
    "w": 40.98308881572128,
    "h": 27.670675485193705,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.303607936674336,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar_label",
    "x": 133.64166666666665,
    "y": 727.8190789473683,
    "w": 41.21666666666667,
    "h": 27.686403508771928,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.317763157894735,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
