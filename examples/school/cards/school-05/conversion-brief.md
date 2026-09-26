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
    "x": 49.30679611650484,
    "y": 0.0,
    "w": 307.3864077669903,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wallpaper_lower",
    "x": 49.30679611650484,
    "y": 426.8,
    "w": 307.3864077669903,
    "h": 349.20000000000005,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_card",
    "x": 62.867961165048534,
    "y": 116.02330097087379,
    "w": 278.75728155339806,
    "h": 239.58058252427185,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 79.44271844660193,
    "y": 289.30485436893207,
    "w": 120.54368932038835,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 79.44271844660193,
    "y": 289.30485436893207,
    "w": 120.54368932038835,
    "h": 46.71067961165049,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 79.44271844660193,
    "y": 289.30485436893207,
    "w": 120.54368932038835,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_26",
    "x": 102.39878604200432,
    "y": 304.2569084791825,
    "w": 79.03429080778281,
    "h": 20.24504473479652,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.619354376135053,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "undo_calendar",
    "x": 213.54757281553398,
    "y": 289.30485436893207,
    "w": 113.00970873786409,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "undo_calendar_surface",
    "x": 213.54757281553398,
    "y": 289.30485436893207,
    "w": 113.00970873786409,
    "h": 46.71067961165049,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "undo_calendar_control",
    "x": 213.54757281553398,
    "y": 289.30485436893207,
    "w": 113.00970873786409,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_27",
    "x": 231.15061212328402,
    "y": 304.1994071606783,
    "w": 79.03429080778278,
    "h": 20.360048130819923,
    "text": "\u64a4\u9500\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.6103855014208,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 83.96310679611649,
    "y": 134.10485436893205,
    "w": 33.1495145631068,
    "h": 34.65631067961165,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_0.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "check_icon_1",
    "x": 127.66019417475728,
    "y": 140.13203883495146,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_1.svg",
      "sha256": "66dac3d5cf777af8f0a9d888b632fd35bdb1c74921628c119909111b32e8352c",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_22",
    "x": 154.57293398152555,
    "y": 142.46979493297246,
    "w": 168.747572815534,
    "h": 20.94002178454052,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u91cd\u65b0\u52a0\u5165",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.31353706436813,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_23",
    "x": 83.67246231221864,
    "y": 187.27429795526248,
    "w": 109.09892801032147,
    "h": 22.687101514075977,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.09365754201718,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_24",
    "x": 79.69784498118737,
    "y": 223.08324825521478,
    "w": 184.7171048944854,
    "h": 19.387511450906537,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.727547754500616,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_25",
    "x": 79.92718498891858,
    "y": 249.66243317858783,
    "w": 169.57400994912464,
    "h": 19.159854547950253,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.19642579909215,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "payment_card",
    "x": 62.867961165048534,
    "y": 373.6854368932039,
    "w": 278.75728155339806,
    "h": 302.86601941747574,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "pay_fee",
    "x": 80.94951456310679,
    "y": 580.1165048543689,
    "w": 162.73398058252428,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_surface",
    "x": 80.94951456310679,
    "y": 580.1165048543689,
    "w": 162.73398058252428,
    "h": 48.21747572815534,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee_control",
    "x": 80.94951456310679,
    "y": 580.1165048543689,
    "w": 162.73398058252428,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_label",
    "x": 113.36294937157136,
    "y": 593.559546138592,
    "w": 100.94174757281554,
    "h": 22.838189276213853,
    "text": "\u652f\u4ed8 \u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.44665985117278,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_payment",
    "x": 254.23106796116505,
    "y": 580.1165048543689,
    "w": 70.81941747572816,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_surface",
    "x": 254.23106796116505,
    "y": 580.1165048543689,
    "w": 70.81941747572816,
    "h": 48.21747572815534,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_payment_control",
    "x": 254.23106796116505,
    "y": 580.1165048543689,
    "w": 70.81941747572816,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_label",
    "x": 268.64308991839397,
    "y": 594.0173536581046,
    "w": 43.68349514563107,
    "h": 21.922574237188662,
    "text": "\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.29232964175314,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "view_payment",
    "x": 80.94951456310679,
    "y": 635.8679611650485,
    "w": 244.10097087378642,
    "h": 33.1495145631068,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_payment_surface",
    "x": 80.94951456310679,
    "y": 635.8679611650485,
    "w": 244.10097087378642,
    "h": 33.1495145631068,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_payment_control",
    "x": 80.94951456310679,
    "y": 635.8679611650485,
    "w": 244.10097087378642,
    "h": 33.1495145631068,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_32",
    "x": 164.67637216408298,
    "y": 641.2907710265648,
    "w": 79.84660194174758,
    "h": 20.79709872356947,
    "text": "\u67e5\u770b\u8d39\u7528",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.15902564710213,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_2",
    "x": 82.45631067961165,
    "y": 396.2873786407767,
    "w": 36.16310679611651,
    "h": 31.642718446601943,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_2.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_28",
    "x": 132.78936070494254,
    "y": 403.56080274303685,
    "w": 116.7833216885516,
    "h": 19.00126684684126,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.229282560592782,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_29",
    "x": 79.2469506824677,
    "y": 447.0914834973715,
    "w": 158.21668874010408,
    "h": 23.079140694371834,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.51520504771165,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_30",
    "x": 79.43390361421605,
    "y": 487.11615540628947,
    "w": 97.64432618358292,
    "h": 34.4754730311137,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 40.15213838091397,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_31",
    "x": 79.43831867756944,
    "y": 535.714509039183,
    "w": 150.64514126742367,
    "h": 19.934026946649848,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.041740049892887,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 52.32038834951455,
    "y": 678.0582524271845,
    "w": 299.852427184466,
    "h": 97.94174757281554,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 73.41553398058251,
    "y": 687.0990291262136,
    "w": 55.751456310679615,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_tile",
    "x": 174.37087378640774,
    "y": 687.0990291262136,
    "w": 55.751456310679615,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_tile",
    "x": 275.326213592233,
    "y": 687.0990291262136,
    "w": 55.751456310679615,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 70.4019417475728,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 70.4019417475728,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 70.4019417475728,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_33",
    "x": 82.85278251444626,
    "y": 743.4939147542012,
    "w": 37.1964471902925,
    "h": 19.253767483939406,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.59822359514625,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar",
    "x": 171.35728155339805,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 171.35728155339805,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 171.35728155339805,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_35",
    "x": 183.39821364554226,
    "y": 743.5226172528517,
    "w": 39.014660277507886,
    "h": 19.196362560438423,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.507330138753943,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_payment",
    "x": 272.3126213592233,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 272.3126213592233,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 272.3126213592233,
    "y": 684.0854368932039,
    "w": 63.28543689320389,
    "h": 88.9009708737864,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_36",
    "x": 284.3276445617039,
    "y": 743.6738788681956,
    "w": 37.0719578854211,
    "h": 18.893839303393566,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.165527463885926,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "mail_icon_3",
    "x": 86.9766990291262,
    "y": 699.1533980582525,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_3.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_4",
    "x": 187.93203883495144,
    "y": 699.1533980582525,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_4.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_5",
    "x": 288.88737864077666,
    "y": 699.1533980582525,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_5.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "1e0ef5976cd60b535a5f22f5808e09005fa47dcb428de303f4b37824d4f517c6",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_20",
    "x": 64.62348688802503,
    "y": 26.316327556028774,
    "w": 105.21586791462268,
    "h": 18.19333231602802,
    "text": "9\u670824\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.16552655584057,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_21",
    "x": 63.39288049341343,
    "y": 60.42414280104309,
    "w": 105.21586791462265,
    "h": 33.47786129851805,
    "text": "09:45",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 38.837761921631156,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
