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
    "x": 7.0,
    "y": 0.0,
    "w": 392.0,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_card",
    "x": 20.647969052224372,
    "y": 109.9902248289345,
    "w": 363.9458413926499,
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
    "x": 41.11992263056093,
    "y": 543.8826979472141,
    "w": 316.936170212766,
    "h": 0.7585532746823069,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "close",
    "x": 330.76015473887816,
    "y": 125.16129032258064,
    "w": 40.94390715667312,
    "h": 40.961876832844574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "close_surface",
    "x": 330.76015473887816,
    "y": 125.16129032258064,
    "w": 40.94390715667312,
    "h": 40.961876832844574,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "close_control",
    "x": 330.76015473887816,
    "y": 125.16129032258064,
    "w": 40.94390715667312,
    "h": 40.961876832844574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday",
    "x": 39.603481624758224,
    "y": 217.70478983382208,
    "w": 156.19342359767893,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_surface",
    "x": 39.603481624758224,
    "y": 217.70478983382208,
    "w": 156.19342359767893,
    "h": 46.271749755620725,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_control",
    "x": 39.603481624758224,
    "y": 217.70478983382208,
    "w": 156.19342359767893,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_69",
    "x": 64.47565355508135,
    "y": 230.6001955294935,
    "w": 109.59501296731453,
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
    "x": 214.752417794971,
    "y": 217.70478983382208,
    "w": 149.36943907156675,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_surface",
    "x": 214.752417794971,
    "y": 217.70478983382208,
    "w": 149.36943907156675,
    "h": 46.271749755620725,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_control",
    "x": 214.752417794971,
    "y": 217.70478983382208,
    "w": 149.36943907156675,
    "h": 46.271749755620725,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_70",
    "x": 235.78907416459504,
    "y": 230.6001952119597,
    "w": 109.59501296731442,
    "h": 27.021209612386773,
    "text": "\u5468\u65e5 9\u670820\u65e5",
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
    "id": "conflict_slot",
    "x": 39.603481624758224,
    "y": 283.6989247311828,
    "w": 326.0348162475822,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "conflict_slot_surface",
    "x": 39.603481624758224,
    "y": 283.6989247311828,
    "w": 326.0348162475822,
    "h": 91.02639296187684,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "conflict_slot_control",
    "x": 39.603481624758224,
    "y": 283.6989247311828,
    "w": 326.0348162475822,
    "h": 91.02639296187684,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_71",
    "x": 53.05475900798358,
    "y": 306.9671061247673,
    "w": 140.0507276523966,
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
    "id": "text_72",
    "x": 56.86172724575768,
    "y": 337.45036296928765,
    "w": 132.43679898112615,
    "h": 23.069675837094287,
    "text": "\u4e0e\u9879\u76ee\u4f8b\u4f1a\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.734798528497688,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon",
    "x": 39.603481624758224,
    "y": 386.10361681329425,
    "w": 326.0348162475822,
    "h": 91.78494623655914,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "afternoon_surface",
    "x": 39.603481624758224,
    "y": 386.10361681329425,
    "w": 326.0348162475822,
    "h": 91.78494623655914,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "afternoon_control",
    "x": 39.603481624758224,
    "y": 386.10361681329425,
    "w": 326.0348162475822,
    "h": 91.78494623655914,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_73",
    "x": 56.86172844446524,
    "y": 409.618768188396,
    "w": 140.0507276523966,
    "h": 23.28136522399375,
    "text": "14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.93166965831419,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_74",
    "x": 56.861723523770344,
    "y": 439.9608994894349,
    "w": 79.13929249746893,
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
    "id": "confirm_booking",
    "x": 38.845261121856865,
    "y": 598.4985337243402,
    "w": 325.2765957446809,
    "h": 53.857282502443795,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_booking_surface",
    "x": 38.845261121856865,
    "y": 598.4985337243402,
    "w": 325.2765957446809,
    "h": 53.857282502443795,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_booking_control",
    "x": 38.845261121856865,
    "y": 598.4985337243402,
    "w": 325.2765957446809,
    "h": 53.857282502443795,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_77",
    "x": 152.03584421186062,
    "y": 615.6100840959664,
    "w": 90.56019128913799,
    "h": 23.299007091354543,
    "text": "\u786e\u8ba4\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.948076594959726,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "close_icon_0",
    "x": 342.13346228239845,
    "y": 137.29814271749754,
    "w": 18.197292069632496,
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
      "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "home_icon_1",
    "x": 41.87814313346229,
    "y": 504.4379276637341,
    "w": 21.230174081237912,
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
      "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "step_0",
    "x": 319.38684719535786,
    "y": 313.28250244379274,
    "w": 26.537717601547392,
    "h": 26.549364613880744,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_1",
    "x": 319.38684719535786,
    "y": 415.6871945259042,
    "w": 26.537717601547392,
    "h": 26.549364613880744,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_66",
    "x": 41.63386475599906,
    "y": 135.49878431384715,
    "w": 136.2437633167614,
    "h": 27.038850032922003,
    "text": "\u9009\u62e9\u5b89\u88c5\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.426130530617463,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_67",
    "x": 41.63386387458895,
    "y": 177.41326312402262,
    "w": 63.91143515492778,
    "h": 26.862442210505932,
    "text": "\u738b\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.26207125577052,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_75",
    "x": 69.93230174081239,
    "y": 505.1964809384164,
    "w": 134.17214700193423,
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
    "id": "text_76",
    "x": 41.633867622948905,
    "y": 562.0879767864812,
    "w": 258.06664519614367,
    "h": 23.228442515562495,
    "text": "\u5468\u516d 9\u670819\u65e5 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.88245153947312,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 20.647969052224372,
    "y": 676.6295210166178,
    "w": 365.46228239845266,
    "h": 99.37047898338221,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 42.75009671179884,
    "y": 683.2441055718475,
    "w": 67.62720309477756,
    "h": 67.65688367546431,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 54.12340425531915,
    "y": 697.6566177908113,
    "w": 44.88058800773694,
    "h": 42.624625610948186,
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
      "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 128.6337330754352,
    "y": 683.2441055718475,
    "w": 67.62720309477756,
    "h": 67.65688367546431,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 214.51736943907153,
    "y": 683.2441055718475,
    "w": 67.62720309477756,
    "h": 67.65688367546431,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.89067698259186,
    "y": 697.6566177908113,
    "w": 44.88058800773694,
    "h": 42.624625610948186,
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
      "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 300.4010058027079,
    "y": 683.2441055718475,
    "w": 67.62720309477756,
    "h": 67.65688367546431,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 311.77431334622827,
    "y": 697.6566177908113,
    "w": 44.88058800773694,
    "h": 42.624625610948186,
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
      "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_64",
    "x": 26.318031162574677,
    "y": 20.76912253005107,
    "w": 109.77096232962109,
    "h": 27.697335788581377,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.038522283380683,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_65",
    "x": 22.34521150252609,
    "y": 58.60251106324123,
    "w": 94.87480910280918,
    "h": 39.66992429134789,
    "text": "15:26",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 33.17302959095354,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_78",
    "x": 37.826898601392045,
    "y": 744.899315962193,
    "w": 41.069646248734415,
    "h": 23.31664678847685,
    "text": "\u90ae\u4ef6",
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
    "id": "text_79",
    "x": 129.1940553763332,
    "y": 703.17888540043,
    "w": 37.26268191309923,
    "h": 26.933006062885053,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.3276956384831,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_80",
    "x": 129.1940567053554,
    "y": 744.8993157081659,
    "w": 41.069646248734415,
    "h": 23.31664678847685,
    "text": "\u65e5\u5386",
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
    "id": "text_81",
    "x": 228.17514213448862,
    "y": 744.8993154541387,
    "w": 41.069646248734514,
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
    "id": "text_82",
    "x": 319.5422988425646,
    "y": 744.8993158406405,
    "w": 41.069646248734415,
    "h": 27.127054305836356,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.508160504427813,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
