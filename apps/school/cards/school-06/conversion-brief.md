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
    "id": "calendar_detail",
    "x": 70.4019417475728,
    "y": 150.67961165048544,
    "w": 271.2233009708738,
    "h": 417.38252427184466,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "status_badge",
    "x": 127.66019417475728,
    "y": 512.3106796116505,
    "w": 159.72038834951456,
    "h": 37.66990291262136,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "date_tile",
    "x": 148.75533980582523,
    "y": 167.25436893203886,
    "w": 113.00970873786409,
    "h": 120.54368932038835,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "clock_icon_1",
    "x": 88.48349514563105,
    "y": 357.1106796116505,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clock_icon_1.svg",
      "sha256": "e4e7b16c2e7527a08c8e3d60957a79a07ef3541ad359823e6bd7de72d3cca0b8",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "pin_icon_2",
    "x": 88.48349514563105,
    "y": 391.7669902912622,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/pin_icon_2.svg",
      "sha256": "5162cd02b3aa7c9bf0322d205107357b4f6ef67567f49d6baac722d7b3a862b6",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 86.9766990291262,
    "y": 432.45048543689325,
    "w": 22.601941747572816,
    "h": 22.601941747572816,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_4",
    "x": 86.9766990291262,
    "y": 473.1339805825243,
    "w": 22.601941747572816,
    "h": 19.58834951456311,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_4.svg",
      "sha256": "1a16bc4c293d40c64f1b8dd44559c4dfc50dd941fc312a54e7aa078aea90d8c1",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "check_icon_5",
    "x": 145.74174757281554,
    "y": 519.8446601941748,
    "w": 24.10873786407767,
    "h": 24.10873786407767,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_5.svg",
      "sha256": "66dac3d5cf777af8f0a9d888b632fd35bdb1c74921628c119909111b32e8352c",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_82",
    "x": 182.5877945312659,
    "y": 177.11436137421185,
    "w": 40.19633934366752,
    "h": 24.20477334424656,
    "text": "9\u6708",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.27738864544535,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_83",
    "x": 162.29984133424315,
    "y": 204.51232154283673,
    "w": 74.92968950718242,
    "h": 49.22299217254023,
    "text": "25",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 59.582334878182124,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_84",
    "x": 179.17251350813103,
    "y": 257.90549828010757,
    "w": 44.64350248728116,
    "h": 21.392747316930425,
    "text": "\u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.809507194681576,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_85",
    "x": 84.51408931634725,
    "y": 311.85113867879716,
    "w": 116.74555317628405,
    "h": 24.03389420459713,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.541821725373257,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_86",
    "x": 120.92557800912385,
    "y": 356.10939497017193,
    "w": 152.17281553398058,
    "h": 23.097714914025033,
    "text": "14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.161679728623234,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_88",
    "x": 122.50146810925867,
    "y": 392.5366231017798,
    "w": 165.7882362127845,
    "h": 18.815312327877052,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.828325136620782,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_90",
    "x": 118.09024876716201,
    "y": 433.15415040179556,
    "w": 78.87498898764562,
    "h": 20.54195816269255,
    "text": "\u5bb6\u5ead\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.767946469057517,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_91",
    "x": 118.67826959609363,
    "y": 471.55387588418677,
    "w": 131.716284069004,
    "h": 19.625476004925353,
    "text": "\u6765\u81ea\u6797\u8001\u5e08\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.92900975614881,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_92",
    "x": 181.80911042039196,
    "y": 520.5690804341131,
    "w": 94.91456310679612,
    "h": 19.64630515119149,
    "text": "\u5df2\u52a0\u5165\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.231613602633804,
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
    "y": 682.5786407766991,
    "w": 299.852427184466,
    "h": 93.42135922330098,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 73.41553398058251,
    "y": 691.6194174757281,
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
    "y": 691.6194174757281,
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
    "y": 691.6194174757281,
    "w": 55.751456310679615,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop",
    "x": 62.867961165048534,
    "y": 46.71067961165049,
    "w": 73.83300970873786,
    "h": 34.65631067961165,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "show_desktop_surface",
    "x": 62.867961165048534,
    "y": 46.71067961165049,
    "w": 73.83300970873786,
    "h": 34.65631067961165,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop_control",
    "x": 62.867961165048534,
    "y": 46.71067961165049,
    "w": 73.83300970873786,
    "h": 34.65631067961165,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "desktop_label",
    "x": 89.27340025327142,
    "y": 53.1261359223301,
    "w": 49.71067961165049,
    "h": 21.825398058252432,
    "text": "\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.375432672013513,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "undo_calendar",
    "x": 71.90873786407766,
    "y": 583.1300970873787,
    "w": 120.54368932038835,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "undo_calendar_surface",
    "x": 71.90873786407766,
    "y": 583.1300970873787,
    "w": 120.54368932038835,
    "h": 48.21747572815534,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "undo_calendar_control",
    "x": 71.90873786407766,
    "y": 583.1300970873787,
    "w": 120.54368932038835,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_93",
    "x": 92.03186396134772,
    "y": 596.4577094682766,
    "w": 78.96225618405086,
    "h": 20.344548677891254,
    "text": "\u64a4\u9500\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.593701483198338,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "return_mail",
    "x": 206.01359223300972,
    "y": 583.1300970873787,
    "w": 132.5980582524272,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_mail_surface",
    "x": 206.01359223300972,
    "y": 583.1300970873787,
    "w": 132.5980582524272,
    "h": 48.21747572815534,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "return_mail_control",
    "x": 206.01359223300972,
    "y": 583.1300970873787,
    "w": 132.5980582524272,
    "h": 48.21747572815534,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_94",
    "x": 224.6501512503813,
    "y": 597.0728960598381,
    "w": 93.85855244724274,
    "h": 19.503791473314134,
    "text": "\u67e5\u770b\u539f\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.815392053486047,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_mail",
    "x": 70.4019417475728,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 70.4019417475728,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 70.4019417475728,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_95",
    "x": 79.98527769578077,
    "y": 739.0417985382512,
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
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 171.35728155339805,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 171.35728155339805,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_97",
    "x": 180.18834513092193,
    "y": 738.2262591334696,
    "w": 42.905175791480886,
    "h": 20.884846293502704,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.452587895740443,
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
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 272.3126213592233,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 272.3126213592233,
    "y": 688.6058252427185,
    "w": 63.28543689320389,
    "h": 84.38058252427184,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_99",
    "x": 285.24591363951384,
    "y": 739.2217623807652,
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
    "id": "back_icon_0",
    "x": 65.88155339805824,
    "y": 54.24466019417476,
    "w": 13.56116504854369,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "171f79537a16c28893fe9bd1e9c89f62c10cb6903e9823ae2f7dc718e2f12752",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_6",
    "x": 86.9766990291262,
    "y": 703.673786407767,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_6.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_7",
    "x": 187.93203883495144,
    "y": 703.673786407767,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_7.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_8",
    "x": 288.88737864077666,
    "y": 703.673786407767,
    "w": 27.12233009708738,
    "h": 27.12233009708738,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_8.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "status_icon_99",
    "x": 267.79223300970875,
    "y": 9.040776699029127,
    "w": 73.83300970873786,
    "h": 19.58834951456311,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/status_icon_99.svg",
      "sha256": "3b6423e66479afccf6047b9070879d78bab3316da88a148ca834359918ba963e",
      "method": "reference_svg",
      "reference_sha256": "706e8de54afb388399f260f45d3c64bf848f88371a0be5ada574f28cd8efc7b3",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_80",
    "x": 61.791514019607824,
    "y": 15.5755412147149,
    "w": 146.85936753108345,
    "h": 17.484368544108996,
    "text": "9\u670824\u65e5 \u5468\u56db 09:46",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.358050733609334,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_81",
    "x": 64.90332592800246,
    "y": 106.03342727906214,
    "w": 62.35776516234634,
    "h": 29.327270080458312,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.17888258117317,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
