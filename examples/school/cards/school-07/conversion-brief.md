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
    "id": "payment_detail",
    "x": 64.37475728155339,
    "y": 150.67961165048544,
    "w": 277.2504854368932,
    "h": 501.7631067961165,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 85.46990291262135,
    "y": 455.05242718446607,
    "w": 239.58058252427185,
    "h": 1.5067961165048545,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee",
    "x": 80.94951456310679,
    "y": 522.8582524271845,
    "w": 244.10097087378642,
    "h": 51.23106796116505,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_surface",
    "x": 80.94951456310679,
    "y": 522.8582524271845,
    "w": 244.10097087378642,
    "h": 51.23106796116505,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee_control",
    "x": 80.94951456310679,
    "y": 522.8582524271845,
    "w": 244.10097087378642,
    "h": 51.23106796116505,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_148",
    "x": 153.19943245376922,
    "y": 538.1742215221043,
    "w": 102.0308764904786,
    "h": 23.04767315010411,
    "text": "\u652f\u4ed8 \u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.674030191864084,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_payment",
    "x": 77.93592233009707,
    "y": 589.1572815533981,
    "w": 108.48932038834953,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_surface",
    "x": 77.93592233009707,
    "y": 589.1572815533981,
    "w": 108.48932038834953,
    "h": 46.71067961165049,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_payment_control",
    "x": 77.93592233009707,
    "y": 589.1572815533981,
    "w": 108.48932038834953,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_149",
    "x": 111.9902020675505,
    "y": 604.0462116041476,
    "w": 40.85772875094102,
    "h": 20.67772032764879,
    "text": "\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.95233619768438,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "return_mail",
    "x": 198.47961165048542,
    "y": 589.1572815533981,
    "w": 129.58446601941748,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_mail_surface",
    "x": 198.47961165048542,
    "y": 589.1572815533981,
    "w": 129.58446601941748,
    "h": 46.71067961165049,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "return_mail_control",
    "x": 198.47961165048542,
    "y": 589.1572815533981,
    "w": 129.58446601941748,
    "h": 46.71067961165049,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_150",
    "x": 218.0220965441662,
    "y": 602.8942767283582,
    "w": 90.07277871090245,
    "h": 18.8578000394593,
    "text": "\u67e5\u770b\u539f\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.114750585096854,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_1",
    "x": 85.46990291262135,
    "y": 171.7747572815534,
    "w": 48.21747572815534,
    "h": 42.19029126213592,
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
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 85.46990291262135,
    "y": 372.17864077669907,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "clock_icon_3",
    "x": 85.46990291262135,
    "y": 408.34174757281556,
    "w": 21.09514563106796,
    "h": 21.09514563106796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clock_icon_3.svg",
      "sha256": "e4e7b16c2e7527a08c8e3d60957a79a07ef3541ad359823e6bd7de72d3cca0b8",
      "method": "reference_svg",
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_4",
    "x": 85.46990291262135,
    "y": 474.6407766990292,
    "w": 21.09514563106796,
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
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_141",
    "x": 149.81309596152207,
    "y": 184.4708296855676,
    "w": 74.92968950718249,
    "h": 24.498576052123916,
    "text": "\u5f85\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.24881626496807,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_142",
    "x": 80.81103224753319,
    "y": 239.57734940129419,
    "w": 113.35954691260099,
    "h": 39.53577410585752,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 46.81920172049739,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_143",
    "x": 84.89099539905787,
    "y": 297.6073778163746,
    "w": 150.72056345914558,
    "h": 22.157721547636147,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.524431771651773,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_144",
    "x": 81.27485195900697,
    "y": 334.89868716235213,
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
    "id": "copy_145",
    "x": 120.76606727215784,
    "y": 371.12792233009714,
    "w": 195.86990291262137,
    "h": 23.196582524271843,
    "text": "\u6d3b\u52a8\uff1a\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.641486585238543,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_146",
    "x": 120.75338193808389,
    "y": 408.2129919232627,
    "w": 207.9242718446602,
    "h": 21.352656930173694,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.991540242135592,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_147",
    "x": 119.59654185237551,
    "y": 475.3624704687475,
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
    "id": "copy_139",
    "x": 81.61986808749786,
    "y": 55.14201282935949,
    "w": 44.64350248728116,
    "h": 21.26935020061968,
    "text": "\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.771032826760525,
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
    "id": "copy_151",
    "x": 80.90354738877878,
    "y": 739.0417985145299,
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
    "id": "copy_152",
    "x": 181.44897878014694,
    "y": 739.0705007522428,
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
    "id": "copy_153",
    "x": 286.1641834981397,
    "y": 739.2217630145032,
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
    "x": 64.37475728155339,
    "y": 55.751456310679615,
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
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_5",
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
      "path": "assets/mail_icon_5.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_6",
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
      "path": "assets/calendar_icon_6.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_7",
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
      "path": "assets/wallet_icon_7.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
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
      "reference_sha256": "cf98697ef81f0c1e9a215138ba2351e5fa7d551aec2841ffb710c05c079321d2",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_137",
    "x": 58.924002269629185,
    "y": 17.477649091638774,
    "w": 146.85937901436483,
    "h": 17.484369620471284,
    "text": "9\u670824\u65e5 \u5468\u56db 09:46",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.358051959534492,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_140",
    "x": 66.20137309348412,
    "y": 107.92497733129495,
    "w": 59.78659456182164,
    "h": 28.823064669043493,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.942544865097858,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
