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
    "id": "payment_receipt",
    "x": 66.83396226415095,
    "y": 144.9509433962264,
    "w": 270.86792452830184,
    "h": 510.988679245283,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 81.47547169811321,
    "y": 535.8792452830188,
    "w": 245.97735849056602,
    "h": 42.46037735849056,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 81.47547169811321,
    "y": 535.8792452830188,
    "w": 245.97735849056602,
    "h": 42.46037735849056,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 81.47547169811321,
    "y": 535.8792452830188,
    "w": 245.97735849056602,
    "h": 42.46037735849056,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_163",
    "x": 165.9967201285069,
    "y": 546.6840728218159,
    "w": 76.66970004694544,
    "h": 19.739840013595153,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.07140999305331,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "return_mail",
    "x": 81.47547169811321,
    "y": 592.9811320754717,
    "w": 245.97735849056602,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_mail_surface",
    "x": 81.47547169811321,
    "y": 592.9811320754717,
    "w": 245.97735849056602,
    "h": 48.31698113207547,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "return_mail_control",
    "x": 81.47547169811321,
    "y": 592.9811320754717,
    "w": 245.97735849056602,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_164",
    "x": 165.89041122968342,
    "y": 605.6698467643474,
    "w": 77.01213100846492,
    "h": 19.785668207362697,
    "text": "\u8fd4\u56de\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.177005666335905,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_1",
    "x": 170.78867924528302,
    "y": 163.98490566037734,
    "w": 65.88679245283018,
    "h": 64.42264150943396,
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
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "clock_icon_2",
    "x": 87.33207547169812,
    "y": 434.8528301886792,
    "w": 20.498113207547167,
    "h": 20.498113207547167,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clock_icon_2.svg",
      "sha256": "e4e7b16c2e7527a08c8e3d60957a79a07ef3541ad359823e6bd7de72d3cca0b8",
      "method": "reference_svg",
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "receipt_icon_3",
    "x": 87.33207547169812,
    "y": 475.84905660377353,
    "w": 20.498113207547167,
    "h": 20.498113207547167,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/receipt_icon_3.svg",
      "sha256": "bd45a6046ecf4bb69272f0e62d491e67308cca66355c8574720ddcc38171c12a",
      "method": "reference_svg",
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_157",
    "x": 168.48861353411166,
    "y": 239.08971771517946,
    "w": 65.53668518446884,
    "h": 22.32631621150919,
    "text": "\u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.89108127153675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_158",
    "x": 142.904369167866,
    "y": 283.3232544298981,
    "w": 107.07311392755506,
    "h": 37.51154268467273,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 44.15223015108397,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_159",
    "x": 80.88449682024174,
    "y": 350.0463460719181,
    "w": 150.14513439044984,
    "h": 22.086990157536338,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.448376513479936,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_160",
    "x": 84.74580842939318,
    "y": 388.3676860364841,
    "w": 142.78787599718476,
    "h": 19.086062188255283,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.134825869791747,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_161",
    "x": 121.88602737201298,
    "y": 435.60747045605547,
    "w": 205.05283018867922,
    "h": 18.988832672794594,
    "text": "\u652f\u4ed8\u65f6\u95f4\uff1a9\u670824\u65e5 09:50",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.268631699849415,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_162",
    "x": 122.0029897189538,
    "y": 475.7875528325094,
    "w": 196.26792452830188,
    "h": 20.621120750075423,
    "text": "\u51ed\u8bc1\u53f7\uff1aSC-120-0924",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.027245932836685,
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
    "y": 682.2943396226415,
    "w": 291.36603773584903,
    "h": 93.70566037735848,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 77.08301886792454,
    "y": 691.0792452830188,
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
    "y": 691.0792452830188,
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
    "y": 691.0792452830188,
    "w": 54.17358490566038,
    "h": 49.781132075471696,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop",
    "x": 66.83396226415095,
    "y": 45.388679245283015,
    "w": 71.74339622641509,
    "h": 33.675471698113206,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "show_desktop_surface",
    "x": 66.83396226415095,
    "y": 45.388679245283015,
    "w": 71.74339622641509,
    "h": 33.675471698113206,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop_control",
    "x": 66.83396226415095,
    "y": 45.388679245283015,
    "w": 71.74339622641509,
    "h": 33.675471698113206,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "desktop_label",
    "x": 92.49207760459393,
    "y": 51.56596226415094,
    "w": 48.388679245283015,
    "h": 21.32090566037736,
    "text": "\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.827071369975393,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_mail",
    "x": 74.15471698113208,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 74.15471698113208,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 74.15471698113208,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_165",
    "x": 80.52815581927948,
    "y": 740.1863682253042,
    "w": 39.84102577497577,
    "h": 20.468951343601365,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.920512887487885,
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
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 172.25283018867924,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 172.25283018867924,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_167",
    "x": 178.04760981035577,
    "y": 740.2173571623057,
    "w": 41.80408591058991,
    "h": 20.40697328519602,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.902042955294956,
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
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 270.3509433962264,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 270.3509433962264,
    "y": 688.1509433962264,
    "w": 61.494339622641505,
    "h": 84.92075471698112,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_169",
    "x": 280.06901968958294,
    "y": 740.3806689738245,
    "w": 39.78628359761235,
    "h": 20.080349662158238,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.453346232443817,
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
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_4",
    "x": 90.26037735849059,
    "y": 702.7924528301886,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_4.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_5",
    "x": 188.35849056603774,
    "y": 702.7924528301886,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_5.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_6",
    "x": 286.4566037735849,
    "y": 702.7924528301886,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_6.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
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
      "reference_sha256": "cf4c98d53c8bef5e1c22d506754ff7d772be56afb54d11e88f84fb36bc6be532",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_155",
    "x": 63.001165809151125,
    "y": 15.07579701499256,
    "w": 142.7878759971849,
    "h": 17.11196491714379,
    "text": "9\u670824\u65e5 \u5468\u56db 09:50",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.933900816792473,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_156",
    "x": 66.26120627307371,
    "y": 101.60371105416087,
    "w": 117.28162600657022,
    "h": 28.458286183966848,
    "text": "\u652f\u4ed8\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.48911861079442,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
