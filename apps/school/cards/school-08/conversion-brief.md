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
    "y": 117.53009708737865,
    "w": 278.75728155339806,
    "h": 247.11456310679614,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 80.94951456310679,
    "y": 298.34563106796116,
    "w": 242.59417475728156,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 80.94951456310679,
    "y": 298.34563106796116,
    "w": 242.59417475728156,
    "h": 48.21747572815534,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 80.94951456310679,
    "y": 298.34563106796116,
    "w": 242.59417475728156,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_194",
    "x": 162.10226213182474,
    "y": 312.0963984909882,
    "w": 78.71546324352262,
    "h": 20.176925890140144,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.54547276587868,
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
    "y": 137.11844660194174,
    "w": 34.65631067961165,
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
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_190",
    "x": 125.68093198083574,
    "y": 141.49413047151452,
    "w": 116.68976739562251,
    "h": 19.36089272957709,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.606370518461716,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_191",
    "x": 74.89973096128223,
    "y": 184.68685569983532,
    "w": 116.93081295384927,
    "h": 24.06652382993603,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.57690734401724,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_192",
    "x": 78.65063399125098,
    "y": 219.26977461246958,
    "w": 188.50287863082562,
    "h": 19.70808466690786,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.096871736068966,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_193",
    "x": 78.89621853093573,
    "y": 247.96607620906335,
    "w": 169.5740099491248,
    "h": 19.159854547950268,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.196425799092165,
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
    "y": 384.2330097087379,
    "w": 278.75728155339806,
    "h": 253.14174757281555,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "reopen_payment",
    "x": 80.94951456310679,
    "y": 566.5553398058253,
    "w": 242.59417475728156,
    "h": 51.23106796116505,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reopen_payment_surface",
    "x": 80.94951456310679,
    "y": 566.5553398058253,
    "w": 242.59417475728156,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reopen_payment_control",
    "x": 80.94951456310679,
    "y": 566.5553398058253,
    "w": 242.59417475728156,
    "h": 51.23106796116505,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_198",
    "x": 161.81451296979728,
    "y": 584.9960512142865,
    "w": 78.7154575018819,
    "h": 20.407541583574346,
    "text": "\u91cd\u65b0\u6253\u5f00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.680540499541323,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_1",
    "x": 83.96310679611649,
    "y": 409.8485436893204,
    "w": 40.68349514563107,
    "h": 33.1495145631068,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_1.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "close_icon_2",
    "x": 141.22135922330096,
    "y": 415.87572815533986,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/close_icon_2.svg",
      "sha256": "2445798d461b7d64d4941676d83736f15789d860dc36c144c9d5e5f3ba07bd06",
      "method": "reference_svg",
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_195",
    "x": 173.7571601413657,
    "y": 417.25808824795877,
    "w": 159.70679611650488,
    "h": 19.837221562334975,
    "text": "\u652f\u4ed8 \u00b7 \u8bf7\u6c42\u5df2\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.047601251167894,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_196",
    "x": 81.06720607043727,
    "y": 471.12533093848793,
    "w": 78.71545750188204,
    "h": 20.482566775818793,
    "text": "\u5c1a\u672a\u6263\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.89638086408121,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_197",
    "x": 80.02830062601134,
    "y": 501.53334295684533,
    "w": 158.21668874010408,
    "h": 20.82294412995993,
    "text": "\u65e5\u5386\u5b89\u6392\u4e0d\u53d7\u5f71\u54cd",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.206649491298624,
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
    "y": 679.5650485436894,
    "w": 299.852427184466,
    "h": 96.43495145631069,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 73.41553398058251,
    "y": 688.6058252427185,
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
    "y": 688.6058252427185,
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
    "y": 688.6058252427185,
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
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 70.4019417475728,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 70.4019417475728,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_199",
    "x": 77.87928408049301,
    "y": 742.6464836796903,
    "w": 40.884939147062454,
    "h": 20.948629538075195,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.442469573531227,
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
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 171.35728155339805,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 171.35728155339805,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_200",
    "x": 178.5814748369412,
    "y": 743.5226172396732,
    "w": 39.01466027750784,
    "h": 19.196362560438402,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.50733013875392,
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
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 272.3126213592233,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 272.3126213592233,
    "y": 685.5922330097088,
    "w": 63.28543689320389,
    "h": 87.39417475728156,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_201",
    "x": 283.29667877411833,
    "y": 743.6738788813741,
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
    "y": 700.6601941747573,
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
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_4",
    "x": 187.93203883495144,
    "y": 700.6601941747573,
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
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_5",
    "x": 288.88737864077666,
    "y": 700.6601941747573,
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
      "reference_sha256": "6a396cf0da8686a143fd0e2e09c5e28819e1f3862fd7038de5e58f5bfd2780fd",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_187",
    "x": 63.513623639666314,
    "y": 25.61897167681822,
    "w": 71.1439157708422,
    "h": 19.58804407444913,
    "text": "9\u670824\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.958576122637243,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_188",
    "x": 128.05593770225425,
    "y": 25.35127513263904,
    "w": 40.85772875094102,
    "h": 20.123437162807495,
    "text": "\u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.363823647844526,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_189",
    "x": 62.15032112790149,
    "y": 59.87634517237752,
    "w": 109.28047868801988,
    "h": 34.573454321128054,
    "text": "09:47",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 40.281230989628526,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
