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
    "x": 16.0,
    "y": 0.0,
    "w": 373.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "order_card",
    "x": 35.9961759082218,
    "y": 167.7644894204232,
    "w": 324.9378585086042,
    "h": 376.9346826126955,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "product_photo",
    "x": 55.5,
    "y": 246.5,
    "w": 98.5,
    "h": 98.5,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/product_photo.png",
      "sha256": "c009f411fcd98950f99993e4c904b516ed3c85d2e7cae7fe35c839264ad7e7de",
      "method": "source_crop",
      "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
      "crop_pixels": [
        111,
        493,
        197,
        197
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Artwork-only source region; product photography or technician portrait, visually reviewed"
    }
  },
  {
    "id": "view_order",
    "x": 56.70650095602294,
    "y": 469.7405703771849,
    "w": 133.54588910133842,
    "h": 48.544618215271385,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_order_surface",
    "x": 56.70650095602294,
    "y": 469.7405703771849,
    "w": 133.54588910133842,
    "h": 48.544618215271385,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_order_control",
    "x": 56.70650095602294,
    "y": 469.7405703771849,
    "w": 133.54588910133842,
    "h": 48.544618215271385,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_110",
    "x": 84.70772069535553,
    "y": 482.9558634057616,
    "w": 78.2994075505274,
    "h": 25.765387814968346,
    "text": "\u67e5\u770b\u8ba2\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.241810667920564,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "collapse",
    "x": 220.96080305927342,
    "y": 469.7405703771849,
    "w": 114.26386233269598,
    "h": 48.544618215271385,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "collapse_surface",
    "x": 220.96080305927342,
    "y": 469.7405703771849,
    "w": 114.26386233269598,
    "h": 48.544618215271385,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "collapse_control",
    "x": 220.96080305927342,
    "y": 469.7405703771849,
    "w": 114.26386233269598,
    "h": 48.544618215271385,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_111",
    "x": 256.8206529607217,
    "y": 482.95586311887683,
    "w": 38.85685827353714,
    "h": 25.765387814968623,
    "text": "\u6536\u8d77",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.24181066792082,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "order_icon_0",
    "x": 60.27724665391969,
    "y": 191.32290708371664,
    "w": 32.136711281070745,
    "h": 32.12511499540018,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/order_icon_0.svg",
      "sha256": "21092ea107db3e4f3ae713f29e2e667d7a8ba0dd71c2f1d90f4d8145fbf4d17b",
      "method": "reference_svg",
      "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_105",
    "x": 109.37863106124426,
    "y": 196.82695436220286,
    "w": 118.59974272164528,
    "h": 27.5907375472558,
    "text": "\u8ba2\u5355 \u00b7 \u5df2\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.939385918947895,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_106",
    "x": 163.5928150822641,
    "y": 267.70929168453813,
    "w": 121.3276342096566,
    "h": 25.599366469677047,
    "text": "1.5\u5339\u53d8\u9891\u7a7a\u8c03",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.087410816799654,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_107",
    "x": 163.592815323429,
    "y": 310.54277825007335,
    "w": 74.71371654707447,
    "h": 26.130634774609096,
    "text": "\u00a52,799",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.58149034038646,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_108",
    "x": 48.7493612676626,
    "y": 374.8421468613613,
    "w": 132.28769203900845,
    "h": 30.166287531848425,
    "text": "\u9884\u8ba1\u5468\u4e94\u9001\u8fbe",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.334647404619037,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_109",
    "x": 48.8508610843653,
    "y": 414.77092935440515,
    "w": 117.74194865472916,
    "h": 25.566162200618898,
    "text": "\u6765\u81ea\u8d2d\u7269\u8ba2\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.056530846575576,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 16.0,
    "y": 661.7773689052437,
    "w": 373.5,
    "h": 114.22263109475621,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 39.01345602294455,
    "y": 670.486844526219,
    "w": 68.26408795411089,
    "h": 68.23945538178472,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 49.7256931166348,
    "y": 684.0507819687213,
    "w": 46.839613766730395,
    "h": 44.681037718491254,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_mail.svg",
      "sha256": "9b7cff617690a90aac7b12cb3fef04594954830e1bc22fcd9518a5cf98ca1e93",
      "method": "reference_svg",
      "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 126.78595602294455,
    "y": 670.486844526219,
    "w": 68.26408795411089,
    "h": 68.23945538178472,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 214.5584560229445,
    "y": 670.486844526219,
    "w": 68.26408795411089,
    "h": 68.23945538178472,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.27069311663476,
    "y": 684.0507819687213,
    "w": 46.839613766730395,
    "h": 44.681037718491254,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_bag.svg",
      "sha256": "2f675e8ba88bad04e7dcdce9b85424e2d8458a97463597bfa7b814452887fb40",
      "method": "reference_svg",
      "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 302.3309560229445,
    "y": 670.486844526219,
    "w": 68.26408795411089,
    "h": 68.23945538178472,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 313.04319311663477,
    "y": 684.0507819687213,
    "w": 46.839613766730395,
    "h": 44.681037718491254,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "ad9266d4ebef2712804598eee5535322f54c6c4d15b3ba967f5616e33a3bb72d",
      "method": "reference_svg",
      "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_103",
    "x": 38.093802532954385,
    "y": 27.52632659383382,
    "w": 110.57057754487415,
    "h": 22.16272564337916,
    "text": "9\u670817\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.89133484834262,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_104",
    "x": 38.033095725794595,
    "y": 63.19737432468388,
    "w": 103.52062137815294,
    "h": 36.653624617954726,
    "text": "09:46",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.367870894697898,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_112",
    "x": 48.85086039508454,
    "y": 737.4498622849605,
    "w": 42.44254655272742,
    "h": 25.632570738735474,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.11829078702399,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_113",
    "x": 134.90732626721825,
    "y": 698.1194244665589,
    "w": 35.27117271860969,
    "h": 25.516355456621497,
    "text": "17",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.010210574657993,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_114",
    "x": 134.90732646739025,
    "y": 737.4498616872842,
    "w": 42.44254655272742,
    "h": 25.632570738735474,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.11829078702399,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_115",
    "x": 220.96379244361944,
    "y": 737.4498616872842,
    "w": 49.61391766258213,
    "h": 25.632570738735474,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.11829078702399,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_116",
    "x": 307.02025671779313,
    "y": 737.4498617470516,
    "w": 38.856860997799785,
    "h": 25.632570738735197,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.118290787023735,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
