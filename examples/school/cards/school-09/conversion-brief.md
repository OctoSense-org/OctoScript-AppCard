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
    "id": "payment_detail",
    "x": 68.29811320754717,
    "y": 143.48679245283017,
    "w": 269.40377358490565,
    "h": 481.70566037735847,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 87.33207547169812,
    "y": 427.5320754716981,
    "w": 234.2641509433962,
    "h": 1.4641509433962263,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee",
    "x": 82.93962264150944,
    "y": 491.95471698113204,
    "w": 238.6566037735849,
    "h": 51.24528301886792,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_surface",
    "x": 82.93962264150944,
    "y": 491.95471698113204,
    "w": 238.6566037735849,
    "h": 51.24528301886792,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee_control",
    "x": 82.93962264150944,
    "y": 491.95471698113204,
    "w": 238.6566037735849,
    "h": 51.24528301886792,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_51",
    "x": 156.51609288118257,
    "y": 508.4217596944553,
    "w": 99.20221746072299,
    "h": 22.503606748176868,
    "text": "\u652f\u4ed8 \u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.083509495126847,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_payment",
    "x": 82.93962264150944,
    "y": 559.3056603773584,
    "w": 238.6566037735849,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_surface",
    "x": 82.93962264150944,
    "y": 559.3056603773584,
    "w": 238.6566037735849,
    "h": 48.31698113207547,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_payment_control",
    "x": 82.93962264150944,
    "y": 559.3056603773584,
    "w": 238.6566037735849,
    "h": 48.31698113207547,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_52",
    "x": 178.87808290622846,
    "y": 574.2647230950793,
    "w": 47.143541990877345,
    "h": 23.446851987320372,
    "text": "\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.933102246846474,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_1",
    "x": 87.33207547169812,
    "y": 163.98490566037734,
    "w": 45.388679245283015,
    "h": 39.53207547169811,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 88.79622641509435,
    "y": 349.9320754716981,
    "w": 20.498113207547167,
    "h": 20.498113207547167,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "clock_icon_3",
    "x": 88.79622641509435,
    "y": 385.0716981132075,
    "w": 20.498113207547167,
    "h": 20.498113207547167,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_4",
    "x": 88.79622641509435,
    "y": 445.1018867924528,
    "w": 20.498113207547167,
    "h": 19.033962264150944,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_43",
    "x": 149.69445659199877,
    "y": 174.6004110299811,
    "w": 168.53828037361205,
    "h": 18.92247726408069,
    "text": "\u5f85\u4ed8\u6b3e \u00b7 \u5df2\u91cd\u65b0\u6253\u5f00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.080255672500744,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_44",
    "x": 82.80933007061778,
    "y": 224.3530860209921,
    "w": 106.00159518914313,
    "h": 37.166513650904086,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 43.6976464438789,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_45",
    "x": 86.43209146092718,
    "y": 278.3468998431009,
    "w": 146.57336806813416,
    "h": 21.647950820052568,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.9762912043576,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_46",
    "x": 86.63987685274583,
    "y": 314.8152629427053,
    "w": 142.78787599718487,
    "h": 19.08606218825529,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.134825869791758,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_47",
    "x": 123.09344272671943,
    "y": 350.3186415094339,
    "w": 177.23396226415093,
    "h": 22.653283018867924,
    "text": "\u6d3b\u52a8\uff1a\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.05729356867519,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_49",
    "x": 119.98960616614758,
    "y": 388.5904599564822,
    "w": 175.89553876687694,
    "h": 18.640515454672034,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.86695328879267,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_50",
    "x": 120.188903586445,
    "y": 445.46883184505504,
    "w": 124.39474117230542,
    "h": 18.736679426630218,
    "text": "\u6765\u81ea\u6797\u8001\u5e08\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.966066551061992,
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
    "y": 685.222641509434,
    "w": 291.36603773584903,
    "h": 90.77735849056603,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 77.08301886792454,
    "y": 694.0075471698112,
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
    "y": 694.0075471698112,
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
    "y": 694.0075471698112,
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
    "id": "copy_40",
    "x": 89.56377571780149,
    "y": 50.10181132075471,
    "w": 54.24528301886792,
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
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 74.15471698113208,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 74.15471698113208,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_53",
    "x": 86.25317463445924,
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
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 172.25283018867924,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 172.25283018867924,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_55",
    "x": 183.9529809386341,
    "y": 739.2170799385053,
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
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 270.3509433962264,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 270.3509433962264,
    "y": 691.0792452830188,
    "w": 61.494339622641505,
    "h": 81.99245283018867,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_57",
    "x": 281.9630886034193,
    "y": 740.3806693488799,
    "w": 39.78628359761246,
    "h": 20.080349662158287,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.45334623244387,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 69.76226415094341,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_5",
    "x": 90.26037735849059,
    "y": 705.7207547169811,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_6",
    "x": 188.35849056603774,
    "y": 705.7207547169811,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_7",
    "x": 286.4566037735849,
    "y": 705.7207547169811,
    "w": 26.354716981132075,
    "h": 26.354716981132075,
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
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
      "reference_sha256": "f17abee00f8aa6c4b052c842420fe0aca95fb2272a42d2b7b70fe06e20fe6c46",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_39",
    "x": 68.5740982003273,
    "y": 15.078104819803162,
    "w": 142.78787599718487,
    "h": 17.10734856991325,
    "text": "9\u670824\u65e5 \u5468\u56db 09:48",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.928643018124427,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_42",
    "x": 72.02993236021653,
    "y": 102.21716396209611,
    "w": 54.500797594571566,
    "h": 26.512489770902015,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.434684990125195,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
