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
    "y": 7.0,
    "w": 406.0,
    "h": 762.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "app_detail",
    "x": 16.707818930041153,
    "y": 327.8421052631579,
    "w": 370.91358024691357,
    "h": 396.0394736842105,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "back_desktop",
    "x": 16.707818930041153,
    "y": 652.0263157894736,
    "w": 365.9012345679012,
    "h": 53.473684210526315,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_desktop_surface",
    "x": 16.707818930041153,
    "y": 652.0263157894736,
    "w": 365.9012345679012,
    "h": 53.473684210526315,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_desktop_control",
    "x": 16.707818930041153,
    "y": 652.0263157894736,
    "w": 365.9012345679012,
    "h": 53.473684210526315,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_198",
    "x": 158.29651975915453,
    "y": 665.8907153874683,
    "w": 88.13246451057607,
    "h": 26.402779449537977,
    "text": "\u8fd4\u56de\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.16250150458418,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_1",
    "x": 25.061728395061728,
    "y": 391.34210526315786,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_2",
    "x": 25.061728395061728,
    "y": 429.7763157894737,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/pin_icon_2.svg",
      "sha256": "2bf55d3cae2ca238d7cf5c17c98856c017509e3c05ad30cc2786bb71177e8dc1",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "person_icon_3",
    "x": 25.061728395061728,
    "y": 476.5657894736842,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/person_icon_3.svg",
      "sha256": "1cfecd555fd25b7cd666f786b88cff04775e5b9b15af6b2faa77d08c77ceb977",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "person_icon_4",
    "x": 25.061728395061728,
    "y": 513.328947368421,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/person_icon_4.svg",
      "sha256": "1cfecd555fd25b7cd666f786b88cff04775e5b9b15af6b2faa77d08c77ceb977",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "wallet_icon_5",
    "x": 25.061728395061728,
    "y": 553.4342105263158,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_5.svg",
      "sha256": "a55d6b3117a99886252fd0de5ba8487754bd95800b2e050040539e070b7b56e5",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "receipt_icon_6",
    "x": 25.061728395061728,
    "y": 591.8684210526316,
    "w": 21.720164609053498,
    "h": 23.394736842105264,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/receipt_icon_6.svg",
      "sha256": "636db1b293ebb51ff9c2ed0cff9d829f10b6a7fe1aec3f32f70b65416f424800",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_186",
    "x": 19.556534356224322,
    "y": 340.7927640073284,
    "w": 241.42230334563823,
    "h": 36.89884735088629,
    "text": "\u5341\u5e74\u540c\u7a97 \u518d\u805a\u4e00\u5802",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.608962615797665,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_187",
    "x": 63.38835017038164,
    "y": 391.6095178464016,
    "w": 186.6325341778699,
    "h": 30.7190893543394,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.04718041890546,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_188",
    "x": 63.38834996687207,
    "y": 428.34826465214155,
    "w": 190.28518715370333,
    "h": 26.107326862463054,
    "text": "\u6728\u5149\u9910\u5385 \u00b7 \u6842\u82b1\u8def8\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.896594176216748,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_190",
    "x": 63.38834886119237,
    "y": 476.0435857879859,
    "w": 62.442409408734285,
    "h": 26.44228662580959,
    "text": "\u7ec4\u7ec7\u8005",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.19805796322863,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_191",
    "x": 63.38834827226964,
    "y": 511.8454165817094,
    "w": 47.83180705655076,
    "h": 27.37920248829242,
    "text": "\u62a5\u540d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.04128223946318,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_192",
    "x": 154.70461750684967,
    "y": 476.0435857879859,
    "w": 44.17915726443387,
    "h": 26.44228662580959,
    "text": "\u738b\u5b81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.19805796322863,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_193",
    "x": 158.3572664406454,
    "y": 511.84541668614986,
    "w": 58.78976280033451,
    "h": 27.37920248829242,
    "text": "\u5df2\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.04128223946318,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_194",
    "x": 154.6685897810427,
    "y": 552.6260491491033,
    "w": 113.651579482461,
    "h": 26.29559869559423,
    "text": "\u00a5180\u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.066038826034806,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_195",
    "x": 63.38834549136901,
    "y": 556.4629940117111,
    "w": 58.78976280033451,
    "h": 26.180143683000882,
    "text": "\u51d1\u4efd\u5b50",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.962129314700793,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_196",
    "x": 63.38834772707435,
    "y": 596.6726976300907,
    "w": 44.17915726443406,
    "h": 26.049073406032903,
    "text": "\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.844166065429615,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_197",
    "x": 151.05196828705107,
    "y": 596.6726976017102,
    "w": 172.0219350094031,
    "h": 22.70918733627684,
    "text": "REU-20261024-001",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.83826860264916,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "venue_photo",
    "x": 1.5,
    "y": 99.0,
    "w": 401.0,
    "h": 219.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/venue_photo.png",
      "sha256": "298249433384b518aea1ccfeb94adad17d1fe34498cd4c067e7d5e2b70cad73f",
      "method": "source_crop",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "crop_pixels": [
        3,
        198,
        802,
        438
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "detail_back",
    "x": 10.024691358024691,
    "y": 48.776315789473685,
    "w": 38.42798353909465,
    "h": 43.44736842105263,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "detail_back_surface",
    "x": 10.024691358024691,
    "y": 48.776315789473685,
    "w": 38.42798353909465,
    "h": 43.44736842105263,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "detail_back_control",
    "x": 10.024691358024691,
    "y": 48.776315789473685,
    "w": 38.42798353909465,
    "h": 43.44736842105263,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 13.366255144032921,
    "y": 58.80263157894737,
    "w": 23.390946502057613,
    "h": 25.06578947368421,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "50ab5c7ac439e2ec3cf9c8fa99d327a907fa39d2910cd0a648214845de3efe4e",
      "method": "reference_svg",
      "reference_sha256": "3a2c0c9900a58bb546cabda734976a36c724098ca370f8ba5ef598df74dbdfe5",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_184",
    "x": 30.51449006116001,
    "y": 22.552107389620648,
    "w": 40.52650747231717,
    "h": 22.49558947135406,
    "text": "9:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.646030524218652,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_185",
    "x": 150.92670319396115,
    "y": 55.25721787338808,
    "w": 99.21944675079807,
    "h": 34.06779912345982,
    "text": "\u805a\u4f1a\u8be6\u60c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.06101921111384,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
