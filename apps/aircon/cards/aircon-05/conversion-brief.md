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
    "x": 8.5,
    "y": 0.0,
    "w": 389.0,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_card",
    "x": 21.416015625,
    "y": 116.28599412340843,
    "w": 354.05078125,
    "h": 515.3065621939276,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "product_photo",
    "x": 36.5,
    "y": 336.0,
    "w": 122.5,
    "h": 111.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/product_photo.png",
      "sha256": "b4b7d6304af1b83e3b50300b2652034acef6e3b607aa99b24cc0b8a5aafcaf30",
      "method": "source_crop",
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "crop_pixels": [
        73,
        672,
        245,
        222
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Artwork-only source region; product photography or technician portrait, visually reviewed"
    }
  },
  {
    "id": "choose_time",
    "x": 37.37109375,
    "y": 557.8687561214496,
    "w": 154.232421875,
    "h": 51.68266405484819,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_time_surface",
    "x": 37.37109375,
    "y": 557.8687561214496,
    "w": 154.232421875,
    "h": 51.68266405484819,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "choose_time_control",
    "x": 37.37109375,
    "y": 557.8687561214496,
    "w": 154.232421875,
    "h": 51.68266405484819,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_19",
    "x": 69.67861848054935,
    "y": 569.2693434930404,
    "w": 94.55334606766702,
    "h": 34.75507385373484,
    "text": "\u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 28.602218683973405,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "defer",
    "x": 211.357421875,
    "y": 558.6287952987268,
    "w": 134.478515625,
    "h": 50.92262487757101,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "defer_surface",
    "x": 211.357421875,
    "y": 558.6287952987268,
    "w": 134.478515625,
    "h": 50.92262487757101,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "defer_control",
    "x": 211.357421875,
    "y": 558.6287952987268,
    "w": 134.478515625,
    "h": 50.92262487757101,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_20",
    "x": 237.52642079882926,
    "y": 573.0695393412476,
    "w": 79.29445698857312,
    "h": 27.137006380415368,
    "text": "\u6682\u4e0d\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.517415933786292,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_0",
    "x": 39.650390625,
    "y": 139.84720861900098,
    "w": 33.4296875,
    "h": 34.20176297747307,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_0.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "check_icon_1",
    "x": 38.890625,
    "y": 513.026444662096,
    "w": 19.75390625,
    "h": 19.761018609206662,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_1.svg",
      "sha256": "b454e45f1990ad3cdde19b68869cee12f252d1d1aea44d03fed3e590ce7ea897",
      "method": "reference_svg",
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_13",
    "x": 89.03515625,
    "y": 142.12732615083252,
    "w": 157.9921875,
    "h": 34.40156709108717,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u5f85\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 28.273457394711073,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_14",
    "x": 35.31435272073934,
    "y": 206.64568506608927,
    "w": 151.83771032094953,
    "h": 38.63683484233439,
    "text": "\u7a7a\u8c03\u5df2\u9001\u8fbe",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.21225640337098,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_15",
    "x": 35.34611043328773,
    "y": 256.13320241075087,
    "w": 182.29196986556053,
    "h": 27.561214495592644,
    "text": "\u8bf7\u9009\u62e9\u4e0a\u95e8\u5b89\u88c5\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.91192948090116,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_16",
    "x": 39.16083437078392,
    "y": 294.59472066842034,
    "w": 193.73613667488095,
    "h": 27.101655704151007,
    "text": "\u738b\u5e08\u5085 \u00b7 \u5b89\u88c5\u670d\u52a1\u56e2\u961f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.484539804860436,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_17",
    "x": 39.16083583210856,
    "y": 470.21679626495325,
    "w": 159.40363624691963,
    "h": 27.048630052168587,
    "text": "\u5bb6 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.435225948516788,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_18",
    "x": 70.041015625,
    "y": 512.2664054848188,
    "w": 173.1875,
    "h": 26.80117531831538,
    "text": "\u5df2\u9001\u8fbe \u00b7 \u5468\u4e94 15:20",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.205093046033305,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 17.6171875,
    "y": 658.9539666993145,
    "w": 370.765625,
    "h": 117.04603330068561,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 40.10625,
    "y": 667.6792164544564,
    "w": 68.47615625,
    "h": 68.50081096963761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 51.502734375,
    "y": 682.1199608227229,
    "w": 45.6831875,
    "h": 43.4195181194907,
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
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 127.236171875,
    "y": 667.6792164544564,
    "w": 68.47615625,
    "h": 68.50081096963761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 214.36609374999998,
    "y": 667.6792164544564,
    "w": 68.47615625,
    "h": 68.50081096963761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.76257812499998,
    "y": 682.1199608227229,
    "w": 45.6831875,
    "h": 43.4195181194907,
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
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 301.496015625,
    "y": 667.6792164544564,
    "w": 68.47615625,
    "h": 68.50081096963761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 312.8925,
    "y": 682.1199608227229,
    "w": 45.6831875,
    "h": 43.4195181194907,
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
      "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_11",
    "x": 27.71666646019041,
    "y": 23.525864501906106,
    "w": 109.81223514676094,
    "h": 23.089355035346806,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.75310018287253,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_12",
    "x": 23.901944578800972,
    "y": 57.762978091284424,
    "w": 94.55334606766701,
    "h": 38.484566937931554,
    "text": "15:25",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.070647252276345,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_21",
    "x": 50.605002254015716,
    "y": 733.4378063878388,
    "w": 37.33250622451305,
    "h": 23.301459817765,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.950357630521452,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_22",
    "x": 134.52890392765588,
    "y": 691.6356516794557,
    "w": 37.33250622451307,
    "h": 30.742773909760345,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.87077973607712,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_23",
    "x": 134.52890499532157,
    "y": 733.4378059599544,
    "w": 37.33250332623719,
    "h": 23.30145981776471,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.95035763052118,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_24",
    "x": 229.89697608036823,
    "y": 733.4378063507203,
    "w": 37.332503326237216,
    "h": 23.30145909293501,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.95035695642956,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_25",
    "x": 321.4503224740236,
    "y": 733.4378063745819,
    "w": 33.517781056463726,
    "h": 23.301459817765,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.950357630521452,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
