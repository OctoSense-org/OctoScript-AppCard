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
    "x": 53.65660377358492,
    "y": 0.0,
    "w": 298.68679245283016,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_card",
    "x": 74.15471698113208,
    "y": 303.07924528301885,
    "w": 263.5471698113207,
    "h": 159.59245283018868,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 85.8679245283019,
    "y": 417.2830188679245,
    "w": 237.19245283018867,
    "h": 33.675471698113206,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 85.8679245283019,
    "y": 417.2830188679245,
    "w": 237.19245283018867,
    "h": 33.675471698113206,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 85.8679245283019,
    "y": 417.2830188679245,
    "w": 237.19245283018867,
    "h": 33.675471698113206,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_216",
    "x": 163.29043715910362,
    "y": 425.1756979067929,
    "w": 72.89393799859245,
    "h": 18.9331326354925,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.1964562207077,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_1",
    "x": 85.8679245283019,
    "y": 313.3283018867924,
    "w": 33.675471698113206,
    "h": 33.675471698113206,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "39a377426da1f014860eb8bd3ec1fc9f8a22801f9b234a076b046049a347d424",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_212",
    "x": 128.11789924140183,
    "y": 318.7965569582398,
    "w": 106.00159518914313,
    "h": 17.916788563476924,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.04517682538046,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_213",
    "x": 130.2767790987611,
    "y": 349.46217385941264,
    "w": 91.36156551940373,
    "h": 19.563037023740137,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.734448412623806,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_214",
    "x": 130.11845100462912,
    "y": 373.2797060185581,
    "w": 153.82376358708225,
    "h": 16.77151311987184,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.71372479247908,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_215",
    "x": 130.3158918268012,
    "y": 393.3753515859104,
    "w": 139.1092468005525,
    "h": 16.38726488458581,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 13.23425735532672,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "payment_card",
    "x": 74.15471698113208,
    "y": 471.45660377358485,
    "w": 263.5471698113207,
    "h": 131.77358490566036,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_receipt",
    "x": 85.8679245283019,
    "y": 556.377358490566,
    "w": 237.19245283018867,
    "h": 35.13962264150943,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_receipt_surface",
    "x": 85.8679245283019,
    "y": 556.377358490566,
    "w": 237.19245283018867,
    "h": 35.13962264150943,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_receipt_control",
    "x": 85.8679245283019,
    "y": 556.377358490566,
    "w": 237.19245283018867,
    "h": 35.13962264150943,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_219",
    "x": 163.25959251861588,
    "y": 565.0751976425692,
    "w": 76.57256719522485,
    "h": 19.75719750393094,
    "text": "\u67e5\u770b\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.05324405187331,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_2",
    "x": 85.8679245283019,
    "y": 483.16981132075466,
    "w": 32.21132075471698,
    "h": 32.21132075471698,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_2.svg",
      "sha256": "66dac3d5cf777af8f0a9d888b632fd35bdb1c74921628c119909111b32e8352c",
      "method": "reference_svg",
      "reference_sha256": "39a377426da1f014860eb8bd3ec1fc9f8a22801f9b234a076b046049a347d424",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_217",
    "x": 130.09774752281245,
    "y": 488.39826894539095,
    "w": 109.91689156383337,
    "h": 18.294071818931204,
    "text": "\u652f\u4ed8 \u00b7 \u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.271444250994877,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_218",
    "x": 130.23118738266027,
    "y": 522.7101700222387,
    "w": 124.39474117230542,
    "h": 22.94619687181866,
    "text": "\u00a5120 \u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.563889513551366,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_badge",
    "x": 101.97358490566039,
    "y": 616.4075471698113,
    "w": 206.4452830188679,
    "h": 36.60377358490566,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "teacher_avatar",
    "x": 74.15471698113208,
    "y": 134.70188679245283,
    "w": 46.85283018867924,
    "h": 46.85283018867924,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_inbox",
    "x": 68.29811320754717,
    "y": 45.388679245283015,
    "w": 90.77735849056603,
    "h": 32.21132075471698,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_inbox_surface",
    "x": 68.29811320754717,
    "y": 45.388679245283015,
    "w": 90.77735849056603,
    "h": 32.21132075471698,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_inbox_control",
    "x": 68.29811320754717,
    "y": 45.388679245283015,
    "w": 90.77735849056603,
    "h": 32.21132075471698,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_205",
    "x": 92.04643573686896,
    "y": 48.637660377358486,
    "w": 65.95849056603774,
    "h": 21.32090566037736,
    "text": "\u6536\u4ef6\u7bb1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.725303416624175,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "show_desktop",
    "x": 74.15471698113208,
    "y": 670.5811320754716,
    "w": 263.5471698113207,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "show_desktop_surface",
    "x": 74.15471698113208,
    "y": 670.5811320754716,
    "w": 263.5471698113207,
    "h": 48.31698113207547,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop_control",
    "x": 74.15471698113208,
    "y": 670.5811320754716,
    "w": 263.5471698113207,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_221",
    "x": 163.3259923414248,
    "y": 683.2665175913174,
    "w": 76.57256719522485,
    "h": 19.74110739990857,
    "text": "\u8fd4\u56de\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.10989934772671,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 68.29811320754717,
    "y": 51.24528301886792,
    "w": 13.177358490566037,
    "h": 20.498113207547167,
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
      "reference_sha256": "39a377426da1f014860eb8bd3ec1fc9f8a22801f9b234a076b046049a347d424",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "check_icon_3",
    "x": 125.4,
    "y": 623.7283018867925,
    "w": 20.498113207547167,
    "h": 20.498113207547167,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_3.svg",
      "sha256": "66dac3d5cf777af8f0a9d888b632fd35bdb1c74921628c119909111b32e8352c",
      "method": "reference_svg",
      "reference_sha256": "39a377426da1f014860eb8bd3ec1fc9f8a22801f9b234a076b046049a347d424",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "status_icon_99",
    "x": 265.95849056603777,
    "y": 8.784905660377358,
    "w": 71.74339622641509,
    "h": 19.033962264150944,
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
      "reference_sha256": "39a377426da1f014860eb8bd3ec1fc9f8a22801f9b234a076b046049a347d424",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_203",
    "x": 69.11523905352449,
    "y": 12.774642820906466,
    "w": 140.63018867924526,
    "h": 16.911091716677632,
    "text": "9\u670824\u65e5 \u5468\u56db 09:52",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.705115850430104,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_206",
    "x": 67.5481745294285,
    "y": 88.30001514472757,
    "w": 179.68419979013973,
    "h": 25.56133212435404,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.184228090703268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_207",
    "x": 126.5883571506092,
    "y": 137.40219403016283,
    "w": 58.17942679120404,
    "h": 19.826041832681057,
    "text": "\u6797\u8001\u5e08",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.20221938334898,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_208",
    "x": 129.8958746774564,
    "y": 181.36216193788354,
    "w": 94.96571317838712,
    "h": 17.135205158816976,
    "text": "\u6536\u4ef6\u4eba\uff1aAlex",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.261894852135697,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_209",
    "x": 73.21749533313451,
    "y": 218.33134140724695,
    "w": 263.6188679245283,
    "h": 18.688260581732486,
    "text": "\u5bb6\u957f\u60a8\u597d\uff0c\u79cb\u5b63\u79d1\u5b66\u65e5\u5c06\u4e8e9\u670825\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.364289311435654,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_210",
    "x": 72.52101955550164,
    "y": 244.8338867924528,
    "w": 262.1547169811321,
    "h": 21.320905660377356,
    "text": "14:00\u201316:00 \u5728\u79d1\u5b66\u6559\u5ba4\u4e3e\u884c",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.564743473073268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_211",
    "x": 73.46433618493644,
    "y": 272.04117855156096,
    "w": 262.1547169811321,
    "h": 19.615756104425223,
    "text": "\u6d3b\u52a8\u6750\u6599\u8d39\u4e3a \u00a5120\uff0c\u8bf7\u786e\u8ba4\u7f34\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.43763800465813,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_220",
    "x": 155.79261435862145,
    "y": 624.101259745358,
    "w": 162.59245283018868,
    "h": 21.21634843381202,
    "text": "\u65e5\u7a0b\u4e0e\u7f34\u8d39\u5df2\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.652598519839675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "teacher_initial",
    "x": 86.71680567239515,
    "y": 147.84360894123301,
    "w": 25.216199975964425,
    "h": 23.497687777911306,
    "text": "\u6797",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.216199975964425,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "mail_date",
    "x": 131.9737065644028,
    "y": 160.47289811080321,
    "w": 120.1320754716981,
    "h": 18.737222646318077,
    "text": "9\u670824\u65e5 09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.978367104053085,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
