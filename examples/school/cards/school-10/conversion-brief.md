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
    "id": "wallpaper_lower",
    "x": 53.65660377358492,
    "y": 426.79999999999995,
    "w": 298.68679245283016,
    "h": 349.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_card",
    "x": 66.83396226415095,
    "y": 114.20377358490565,
    "w": 270.86792452830184,
    "h": 221.08679245283017,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 84.40377358490568,
    "y": 278.188679245283,
    "w": 235.72830188679242,
    "h": 42.46037735849056,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 84.40377358490568,
    "y": 278.188679245283,
    "w": 235.72830188679242,
    "h": 42.46037735849056,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 84.40377358490568,
    "y": 278.188679245283,
    "w": 235.72830188679242,
    "h": 42.46037735849056,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_107",
    "x": 165.01283458295075,
    "y": 288.1152839134524,
    "w": 80.46816362164265,
    "h": 20.551397667896772,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.951624368651597,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 87.33207547169812,
    "y": 131.77358490566036,
    "w": 33.675471698113206,
    "h": 33.675471698113206,
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
      "reference_sha256": "97c8799369c86b8d2118a1eda679d568045dbb69a03d1e397ee1bfbb8686b156",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_103",
    "x": 133.56229260689116,
    "y": 134.28193309742227,
    "w": 109.74439567012308,
    "h": 18.422487167789104,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.591878019231464,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_104",
    "x": 87.80243307100494,
    "y": 174.4815613944566,
    "w": 110.013700825353,
    "h": 22.848219564723465,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.266902757767166,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_105",
    "x": 84.0640235116471,
    "y": 211.23588003763115,
    "w": 183.25279716014185,
    "h": 19.26351623293877,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.584696120897203,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_106",
    "x": 87.99344579071425,
    "y": 239.30868667423252,
    "w": 161.1810219803471,
    "h": 18.39601103557864,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.380353670489997,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "payment_card",
    "x": 66.83396226415095,
    "y": 355.788679245283,
    "w": 270.86792452830184,
    "h": 260.6188679245283,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_receipt",
    "x": 84.40377358490568,
    "y": 551.9849056603773,
    "w": 235.72830188679242,
    "h": 46.85283018867924,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_receipt_surface",
    "x": 84.40377358490568,
    "y": 551.9849056603773,
    "w": 235.72830188679242,
    "h": 46.85283018867924,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_receipt_control",
    "x": 84.40377358490568,
    "y": 551.9849056603773,
    "w": 235.72830188679242,
    "h": 46.85283018867924,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_113",
    "x": 161.41363956229918,
    "y": 564.287337588138,
    "w": 83.92982558848979,
    "h": 21.33291761279311,
    "text": "\u67e5\u770b\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.75856884501419,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_1",
    "x": 85.8679245283019,
    "y": 373.3584905660377,
    "w": 38.06792452830189,
    "h": 38.06792452830189,
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
      "reference_sha256": "97c8799369c86b8d2118a1eda679d568045dbb69a03d1e397ee1bfbb8686b156",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_109",
    "x": 135.6797600687901,
    "y": 384.6474962762514,
    "w": 117.18081092152767,
    "h": 19.265209152491035,
    "text": "\u652f\u4ed8 \u00b7 \u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.30898413727675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_110",
    "x": 83.59081165320343,
    "y": 429.32745853900724,
    "w": 150.30271166006472,
    "h": 22.106359459391832,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.469203719776164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_111",
    "x": 80.37607841300608,
    "y": 471.27041029588213,
    "w": 172.29175933122582,
    "h": 30.421531691503628,
    "text": "\u00a5120 \u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 28.677494600040117,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_112",
    "x": 83.87942300439443,
    "y": 514.095770685476,
    "w": 139.1092579588352,
    "h": 18.689061660866937,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.710226375258756,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 56.58490566037737,
    "y": 680.8301886792452,
    "w": 291.36603773584903,
    "h": 95.1698113207547,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 77.08301886792454,
    "y": 689.6150943396226,
    "w": 54.17358490566038,
    "h": 49.781132075471696,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_tile",
    "x": 175.1811320754717,
    "y": 689.6150943396226,
    "w": 54.17358490566038,
    "h": 49.781132075471696,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_tile",
    "x": 273.2792452830189,
    "y": 689.6150943396226,
    "w": 54.17358490566038,
    "h": 49.781132075471696,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 74.15471698113208,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 74.15471698113208,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 74.15471698113208,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_114",
    "x": 83.46682644023983,
    "y": 741.0098152631783,
    "w": 36.25692510000121,
    "h": 18.822057083450556,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.128462550000606,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar",
    "x": 172.25283018867924,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 172.25283018867924,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 172.25283018867924,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_116",
    "x": 181.1666327597422,
    "y": 741.0377053911058,
    "w": 38.02367932625762,
    "h": 18.76627682759581,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.01183966312881,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_payment",
    "x": 270.3509433962264,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 270.3509433962264,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 270.3509433962264,
    "y": 686.6867924528301,
    "w": 61.494339622641505,
    "h": 86.38490566037736,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_117",
    "x": 279.2395703250966,
    "y": 741.1846860301417,
    "w": 36.10765719055069,
    "h": 18.472315549523934,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.708012535662736,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "mail_icon_2",
    "x": 90.26037735849059,
    "y": 701.3283018867924,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_2.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "97c8799369c86b8d2118a1eda679d568045dbb69a03d1e397ee1bfbb8686b156",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 188.35849056603774,
    "y": 701.3283018867924,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "97c8799369c86b8d2118a1eda679d568045dbb69a03d1e397ee1bfbb8686b156",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_4",
    "x": 286.4566037735849,
    "y": 701.3283018867924,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_4.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "97c8799369c86b8d2118a1eda679d568045dbb69a03d1e397ee1bfbb8686b156",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_101",
    "x": 69.4576793707465,
    "y": 26.22351654726701,
    "w": 98.6443367958782,
    "h": 17.280832849004305,
    "text": "9\u670824\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.126233313216748,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_102",
    "x": 68.16968265730914,
    "y": 56.4121091364964,
    "w": 106.00159518914313,
    "h": 33.65492779541029,
    "text": "09:50",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 39.071051113847545,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
