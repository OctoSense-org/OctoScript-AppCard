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
    "x": 5.5,
    "y": 0.0,
    "w": 394.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_card",
    "x": 19.15576923076923,
    "y": 109.9902248289345,
    "w": 366.4298076923077,
    "h": 561.3294232649072,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 40.39807692307692,
    "y": 543.1241446725318,
    "w": 317.8759615384615,
    "h": 0.7585532746823069,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "close",
    "x": 332.4798076923077,
    "y": 125.16129032258064,
    "w": 40.96730769230769,
    "h": 40.961876832844574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "close_surface",
    "x": 332.4798076923077,
    "y": 125.16129032258064,
    "w": 40.96730769230769,
    "h": 40.961876832844574,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "close_control",
    "x": 332.4798076923077,
    "y": 125.16129032258064,
    "w": 40.96730769230769,
    "h": 40.961876832844574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday",
    "x": 38.122115384615384,
    "y": 217.70478983382208,
    "w": 157.79999999999998,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_surface",
    "x": 38.122115384615384,
    "y": 217.70478983382208,
    "w": 157.79999999999998,
    "h": 46.271749755620725,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_control",
    "x": 38.122115384615384,
    "y": 217.70478983382208,
    "w": 157.79999999999998,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_123",
    "x": 59.4437807304166,
    "y": 230.60019559300036,
    "w": 113.46507497934192,
    "h": 27.021209612386773,
    "text": "\u5468\u516d 9\u670819\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.409724939519702,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunday",
    "x": 213.37115384615385,
    "y": 217.70478983382208,
    "w": 151.73076923076923,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_surface",
    "x": 213.37115384615385,
    "y": 217.70478983382208,
    "w": 151.73076923076923,
    "h": 46.271749755620725,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_control",
    "x": 213.37115384615385,
    "y": 217.70478983382208,
    "w": 151.73076923076923,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_124",
    "x": 234.664251941953,
    "y": 234.39296162485388,
    "w": 109.65593486199029,
    "h": 23.228443962388056,
    "text": "\u5468\u65e5 9\u670820\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.882452885020893,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "conflict_slot",
    "x": 38.122115384615384,
    "y": 283.6989247311828,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "conflict_slot_surface",
    "x": 38.122115384615384,
    "y": 283.6989247311828,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "conflict_slot_control",
    "x": 38.122115384615384,
    "y": 283.6989247311828,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_125",
    "x": 55.634645611345334,
    "y": 306.9671057437265,
    "w": 140.1290558008048,
    "h": 23.21080209502726,
    "text": "09:00-11:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.866045948375355,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_126",
    "x": 55.63463681454135,
    "y": 337.4503623607474,
    "w": 132.51078714224,
    "h": 23.069676560507506,
    "text": "\u4e0e\u9879\u76ee\u4f8b\u4f1a\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.734799201271983,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon",
    "x": 38.122115384615384,
    "y": 386.10361681329425,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "afternoon_surface",
    "x": 38.122115384615384,
    "y": 386.10361681329425,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "afternoon_control",
    "x": 38.122115384615384,
    "y": 386.10361681329425,
    "w": 327.73846153846154,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_127",
    "x": 55.63464139296544,
    "y": 409.61876852180666,
    "w": 136.31991568345293,
    "h": 23.28136522399346,
    "text": "14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.93166965831392,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_128",
    "x": 55.63463888308389,
    "y": 439.9608992487777,
    "w": 79.1828139231754,
    "h": 23.72238514173996,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.341818181818162,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_selection",
    "x": 38.122115384615384,
    "y": 597.7399804496579,
    "w": 138.83365384615385,
    "h": 50.82306940371456,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_selection_surface",
    "x": 38.122115384615384,
    "y": 597.7399804496579,
    "w": 138.83365384615385,
    "h": 50.82306940371456,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_selection_control",
    "x": 38.122115384615384,
    "y": 597.7399804496579,
    "w": 138.83365384615385,
    "h": 50.82306940371456,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_131",
    "x": 86.1077652848986,
    "y": 611.7996773379758,
    "w": 44.90054707893964,
    "h": 27.109413885301127,
    "text": "\u53d6\u6d88",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.49175491333005,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirm_booking",
    "x": 195.92211538461538,
    "y": 597.7399804496579,
    "w": 169.1798076923077,
    "h": 50.82306940371456,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_booking_surface",
    "x": 195.92211538461538,
    "y": 597.7399804496579,
    "w": 169.1798076923077,
    "h": 50.82306940371456,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_booking_control",
    "x": 195.92211538461538,
    "y": 597.7399804496579,
    "w": 169.1798076923077,
    "h": 50.82306940371456,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_132",
    "x": 234.4461297247972,
    "y": 611.06570629711,
    "w": 91.04647528575006,
    "h": 32.140791698168755,
    "text": "\u786e\u8ba4\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.170936279296946,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "close_icon_0",
    "x": 343.8596153846154,
    "y": 137.29814271749754,
    "w": 18.207692307692305,
    "h": 18.205278592375365,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/close_icon_0.svg",
      "sha256": "c7b16dd64182b7f4dee11b0174d568d350f32c81055609166b80d830333734b7",
      "method": "reference_svg",
      "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "home_icon_1",
    "x": 40.39807692307692,
    "y": 504.4379276637341,
    "w": 21.24230769230769,
    "h": 20.480938416422287,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/home_icon_1.svg",
      "sha256": "35f5c9ea4be301e43dab353017cb4b03c55ecca63d0fc1663c199edceda6095e",
      "method": "reference_svg",
      "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "step_0",
    "x": 319.5826923076923,
    "y": 313.28250244379274,
    "w": 26.552884615384613,
    "h": 26.549364613880744,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_1",
    "x": 312.7548076923077,
    "y": 407.3431085043988,
    "w": 38.691346153846155,
    "h": 40.961876832844574,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_120",
    "x": 40.39808212538422,
    "y": 135.4987839328065,
    "w": 136.31991568345273,
    "h": 27.03885075633493,
    "text": "\u9009\u62e9\u5b89\u88c5\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.42613120339149,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_121",
    "x": 40.398079053214325,
    "y": 177.41326278515055,
    "w": 63.94624766569862,
    "h": 23.05203541655935,
    "text": "\u738b\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.718392937400196,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_129",
    "x": 68.46826923076924,
    "y": 505.1964809384164,
    "w": 134.24711538461537,
    "h": 26.75659824046921,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.163636363636364,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_130",
    "x": 40.39808711916173,
    "y": 558.2952100597753,
    "w": 254.40327089749854,
    "h": 23.21080209502726,
    "text": "\u5468\u516d 9\u670819\u65e5 \u00b7 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.866045948375355,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 19.15576923076923,
    "y": 676.6295210166178,
    "w": 367.94711538461536,
    "h": 99.37047898338221,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 41.44122596153846,
    "y": 683.2441055718475,
    "w": 68.02090384615384,
    "h": 68.01188660801564,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 52.82103365384615,
    "y": 697.6566177908113,
    "w": 45.261288461538456,
    "h": 42.97962854349951,
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
      "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 127.90879807692306,
    "y": 683.2441055718475,
    "w": 68.02090384615384,
    "h": 68.01188660801564,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 214.3763701923077,
    "y": 683.2441055718475,
    "w": 68.02090384615384,
    "h": 68.01188660801564,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.75617788461537,
    "y": 697.6566177908113,
    "w": 45.261288461538456,
    "h": 42.97962854349951,
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
      "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 300.84394230769226,
    "y": 683.2441055718475,
    "w": 68.02090384615384,
    "h": 68.01188660801564,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 312.22374999999994,
    "y": 697.6566177908113,
    "w": 45.261288461538456,
    "h": 42.97962854349951,
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
      "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_118",
    "x": 25.124629692634144,
    "y": 21.0134510856823,
    "w": 109.72970959590023,
    "h": 27.208678416142902,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.5840709270129,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_119",
    "x": 21.106820453059555,
    "y": 58.625712301120636,
    "w": 94.9104805139394,
    "h": 39.62352170226376,
    "text": "15:27",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 33.1298751831053,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_133",
    "x": 40.39807716914968,
    "y": 744.8993153960929,
    "w": 41.0914069615878,
    "h": 27.127054305836356,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.508160504427813,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_134",
    "x": 131.81745390563242,
    "y": 703.1788857428025,
    "w": 37.28226395020115,
    "h": 26.93300533947213,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.32769496570908,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_135",
    "x": 131.81745183962974,
    "y": 744.899315665828,
    "w": 37.28226684423596,
    "h": 23.316647511889485,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.96448218605722,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_136",
    "x": 230.85511080939818,
    "y": 744.8993156287821,
    "w": 37.28226395020115,
    "h": 23.31664678847685,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.96448151328347,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_137",
    "x": 322.2744843706785,
    "y": 744.8993156525971,
    "w": 37.282266844235764,
    "h": 23.316647511889485,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.96448218605722,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
