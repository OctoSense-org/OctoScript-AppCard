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
    "x": 0.0,
    "y": 69.5,
    "w": 406.0,
    "h": 637.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "payment_complete",
    "x": 14.0,
    "y": 150.95454545454544,
    "w": 358.9090909090909,
    "h": 296.54545454545456,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 33.72727272727273,
    "y": 294.77272727272725,
    "w": 311.8181818181818,
    "h": 0.6363636363636364,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "source_service_order",
    "x": 31.18181818181818,
    "y": 363.5,
    "w": 80.81818181818181,
    "h": 22.272727272727273,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "source_service_order_surface",
    "x": 31.18181818181818,
    "y": 363.5,
    "w": 80.81818181818181,
    "h": 22.272727272727273,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "source_service_order_control",
    "x": 31.18181818181818,
    "y": 363.5,
    "w": 80.81818181818181,
    "h": 22.272727272727273,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_203",
    "x": 32.4100287566441,
    "y": 363.7213610214123,
    "w": 80.20885051380506,
    "h": 25.40082966197606,
    "text": "\u5b89\u88c5\u670d\u52a1\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.902771585637737,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "view_payment_receipt",
    "x": 35.0,
    "y": 395.95454545454544,
    "w": 211.9090909090909,
    "h": 38.18181818181818,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_payment_receipt_surface",
    "x": 35.0,
    "y": 395.95454545454544,
    "w": 211.9090909090909,
    "h": 38.18181818181818,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_payment_receipt_control",
    "x": 35.0,
    "y": 395.95454545454544,
    "w": 211.9090909090909,
    "h": 38.18181818181818,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_204",
    "x": 102.92449026289891,
    "y": 406.2356965550121,
    "w": 73.37543764981362,
    "h": 23.484209754250376,
    "text": "\u67e5\u770b\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.12031507145285,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_0",
    "x": 33.09090909090909,
    "y": 167.5,
    "w": 30.545454545454547,
    "h": 27.363636363636363,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_0.svg",
      "sha256": "ad9266d4ebef2712804598eee5535322f54c6c4d15b3ba967f5616e33a3bb72d",
      "method": "reference_svg",
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "check_icon_1",
    "x": 318.1818181818182,
    "y": 172.5909090909091,
    "w": 21.0,
    "h": 21.636363636363637,
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
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_197",
    "x": 74.13231611017714,
    "y": 172.6144197137299,
    "w": 105.39874128861867,
    "h": 24.020631183277324,
    "text": "\u652f\u4ed8 \u00b7 \u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.619187000447912,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_198",
    "x": 32.67287747732892,
    "y": 211.39429211572389,
    "w": 146.78090459650215,
    "h": 26.37631988525406,
    "text": "\u7a7a\u8c03\u5b89\u88c5\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.809977493286276,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_199",
    "x": 29.078672940477933,
    "y": 248.5583276783753,
    "w": 96.45695634321737,
    "h": 38.35691694779828,
    "text": "\u00a5130",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 31.951932761452404,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_200",
    "x": 147.69760428810403,
    "y": 259.1363633408208,
    "w": 54.122097362171445,
    "h": 23.386892318725558,
    "text": "\u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.02980985641477,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_201",
    "x": 32.62868218228928,
    "y": 307.0621130352348,
    "w": 102.13746504350145,
    "h": 23.641101316972176,
    "text": "\u52a0\u957f\u94dc\u7ba1 2\u7c73",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.266224224784125,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_202",
    "x": 32.67288028118068,
    "y": 339.25898546271304,
    "w": 156.36629694158387,
    "h": 23.179703452370553,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5b89\u88c5\u670d\u52a1\u56e2\u961f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.837124210704616,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_215",
    "x": 297.86877284233515,
    "y": 307.2928120150411,
    "w": 47.73183579878364,
    "h": 23.29809735038061,
    "text": "\u00a5130",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.947230535853965,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "installation_complete",
    "x": 13.363636363636363,
    "y": 457.6818181818182,
    "w": 359.54545454545456,
    "h": 141.27272727272728,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_service_order",
    "x": 90.36363636363636,
    "y": 545.5,
    "w": 158.45454545454544,
    "h": 37.54545454545455,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_service_order_surface",
    "x": 90.36363636363636,
    "y": 545.5,
    "w": 158.45454545454544,
    "h": 37.54545454545455,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_service_order_control",
    "x": 90.36363636363636,
    "y": 545.5,
    "w": 158.45454545454544,
    "h": 37.54545454545455,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_207",
    "x": 122.09408763999781,
    "y": 556.4435165142456,
    "w": 86.15834461558948,
    "h": 23.55059857801951,
    "text": "\u67e5\u770b\u670d\u52a1\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.182056677558144,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_2",
    "x": 33.09090909090909,
    "y": 477.4090909090909,
    "w": 26.09090909090909,
    "h": 25.454545454545453,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_2.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_205",
    "x": 74.20959043362315,
    "y": 479.9101481139836,
    "w": 181.9273431951349,
    "h": 23.179703452370553,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u5b89\u88c5\u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.837124210704616,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_206",
    "x": 29.477752820351768,
    "y": 511.7727270423284,
    "w": 118.02471785111867,
    "h": 23.283297885548055,
    "text": "\u5bb6\uff0e\u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.933467033559694,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 8.272727272727273,
    "y": 610.4090909090909,
    "w": 371.6363636363636,
    "h": 95.45454545454545,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 31.690909090909088,
    "y": 617.4090909090909,
    "w": 66.88436363636363,
    "h": 66.88436363636363,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 41.236363636363635,
    "y": 629.5,
    "w": 47.793454545454544,
    "h": 45.88436363636364,
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
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 119.02545454545454,
    "y": 617.4090909090909,
    "w": 66.88436363636363,
    "h": 66.88436363636363,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 206.35999999999999,
    "y": 617.4090909090909,
    "w": 66.88436363636363,
    "h": 66.88436363636363,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 215.90545454545452,
    "y": 629.5,
    "w": 47.793454545454544,
    "h": 45.88436363636364,
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
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 293.6945454545454,
    "y": 617.4090909090909,
    "w": 66.88436363636363,
    "h": 66.88436363636363,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 303.23999999999995,
    "y": 629.5,
    "w": 47.793454545454544,
    "h": 45.88436363636364,
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
      "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_195",
    "x": 19.892354077623086,
    "y": 89.86363632587717,
    "w": 86.07341003417964,
    "h": 20.04228305816665,
    "text": "9\u670819\u65e5 \u5468\u516d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.919323244094985,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_196",
    "x": 19.827747660497877,
    "y": 115.31726909180352,
    "w": 73.422099720348,
    "h": 29.92994412508886,
    "text": "16:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.11484803633264,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_208",
    "x": 118.94142297607787,
    "y": 639.6818187276659,
    "w": 38.146443453702105,
    "h": 26.43551653081744,
    "text": "19",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.865030373660222,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_209",
    "x": 35.868010776966706,
    "y": 677.8636362811536,
    "w": 34.9513126720082,
    "h": 20.219872994856544,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.084481885216587,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_210",
    "x": 122.13655402915369,
    "y": 674.681817894965,
    "w": 34.9513126720082,
    "h": 23.401691176674575,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.043572794307355,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_211",
    "x": 214.79536004702888,
    "y": 674.681818342018,
    "w": 34.951310244473525,
    "h": 23.40169056979079,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.043572229905436,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_216",
    "x": 307.4541662090677,
    "y": 674.681818342018,
    "w": 34.951310244473525,
    "h": 23.40169056979079,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.043572229905436,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
