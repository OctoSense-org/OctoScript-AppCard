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
    "x": 2.5,
    "y": 0.0,
    "w": 400.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "poll_card",
    "x": 24.193749999999998,
    "y": 188.5763440860215,
    "w": 362.11875,
    "h": 457.2559139784946,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "friday",
    "x": 44.21875,
    "y": 248.6537634408602,
    "w": 320.4,
    "h": 73.4279569892473,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "friday_surface",
    "x": 44.21875,
    "y": 248.6537634408602,
    "w": 320.4,
    "h": 73.4279569892473,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "friday_control",
    "x": 44.21875,
    "y": 248.6537634408602,
    "w": 320.4,
    "h": 73.4279569892473,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_19",
    "x": 116.83730225160993,
    "y": 261.2430282350062,
    "w": 171.81759798868663,
    "h": 26.455896417383336,
    "text": "\u5468\u4e9410\u670823\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.210306775645,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_20",
    "x": 116.83730962133568,
    "y": 287.3494625985688,
    "w": 117.09446046753548,
    "h": 22.921710783517135,
    "text": "\u4e0e\u5de5\u4f5c\u4f8b\u4f1a\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.029539705165423,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "saturday",
    "x": 44.21875,
    "y": 333.76344086021504,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_surface",
    "x": 44.21875,
    "y": 333.76344086021504,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_control",
    "x": 44.21875,
    "y": 333.76344086021504,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_21",
    "x": 116.8373024644221,
    "y": 349.40860277691155,
    "w": 171.81759798868669,
    "h": 25.90322491875751,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.712902426881758,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_22",
    "x": 116.83730453389434,
    "y": 377.98266433221943,
    "w": 73.31596189805701,
    "h": 22.882926832652583,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.994634149387323,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunday",
    "x": 44.21875,
    "y": 428.88602150537633,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_surface",
    "x": 44.21875,
    "y": 428.88602150537633,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_control",
    "x": 44.21875,
    "y": 428.88602150537633,
    "w": 320.4,
    "h": 78.43440860215053,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_23",
    "x": 116.837306659862,
    "y": 444.3225808781383,
    "w": 171.81759798868663,
    "h": 22.71324714702382,
    "text": "\u5468\u65e5 10\u670825\u65e5 12:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.84192243232144,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_24",
    "x": 116.83730626679342,
    "y": 469.7066646617125,
    "w": 73.31596189805701,
    "h": 26.072904604386828,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.865614143948147,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirm_attendance",
    "x": 44.21875,
    "y": 570.7354838709678,
    "w": 156.86249999999998,
    "h": 51.73333333333333,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_attendance_surface",
    "x": 44.21875,
    "y": 570.7354838709678,
    "w": 156.86249999999998,
    "h": 51.73333333333333,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_attendance_control",
    "x": 44.21875,
    "y": 570.7354838709678,
    "w": 156.86249999999998,
    "h": 51.73333333333333,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_26",
    "x": 87.65163357988072,
    "y": 586.4463011914352,
    "w": 80.61238362604527,
    "h": 26.150472506115655,
    "text": "\u786e\u8ba4\u53c2\u52a0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.93542525550409,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "reset_selection",
    "x": 214.43125,
    "y": 570.7354838709678,
    "w": 150.1875,
    "h": 51.73333333333333,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reset_selection_surface",
    "x": 214.43125,
    "y": 570.7354838709678,
    "w": 150.1875,
    "h": 51.73333333333333,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reset_selection_control",
    "x": 214.43125,
    "y": 570.7354838709678,
    "w": 150.1875,
    "h": 51.73333333333333,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_27",
    "x": 251.578729613125,
    "y": 585.813351657826,
    "w": 81.09697294280815,
    "h": 27.663619152309245,
    "text": "\u91cd\u65b0\u9009\u62e9",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.29725723707832,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 49.225,
    "y": 200.25806451612902,
    "w": 26.7,
    "h": 30.03870967741935,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_0.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "warning_icon_1",
    "x": 59.2375,
    "y": 263.67311827956985,
    "w": 33.375,
    "h": 33.376344086021504,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/warning_icon_1.svg",
      "sha256": "e4e325bc63825064c2781b8d5753db0ed0753e089a0a191e8333359242b87136",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 62.574999999999996,
    "y": 357.1268817204301,
    "w": 30.037499999999998,
    "h": 31.70752688172043,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 62.574999999999996,
    "y": 450.5806451612903,
    "w": 30.037499999999998,
    "h": 31.70752688172043,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "friday_dot",
    "x": 324.56874999999997,
    "y": 273.68602150537635,
    "w": 23.3625,
    "h": 23.363440860215054,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_dot",
    "x": 322.9,
    "y": 360.46451612903223,
    "w": 25.03125,
    "h": 25.032258064516128,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_dot",
    "x": 322.9,
    "y": 452.24946236559134,
    "w": 25.03125,
    "h": 25.032258064516128,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_18",
    "x": 91.2619246415212,
    "y": 199.53469353332514,
    "w": 139.05955859785098,
    "h": 29.957494498759555,
    "text": "\u805a\u4f1a \u00b7 \u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.3617450488836,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_25",
    "x": 47.52134124953355,
    "y": 528.076482897891,
    "w": 149.9283455241023,
    "h": 26.11168855525138,
    "text": "\u5df2\u9009\u62e9 \u5468\u516d\u665a\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.900519699726242,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 2.5,
    "y": 662.5204301075269,
    "w": 400.5,
    "h": 113.47956989247311,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 35.875,
    "y": 677.5397849462365,
    "w": 36.7125,
    "h": 38.38279569892473,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_message.svg",
      "sha256": "94781da8c43a880f37575b7fa2fe3999844efe8aa5d1370e3b505fdf8c7171f6",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.77499999999998,
    "y": 677.5397849462365,
    "w": 36.7125,
    "h": 38.38279569892473,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_calendar.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 231.67499999999995,
    "y": 677.5397849462365,
    "w": 36.7125,
    "h": 38.38279569892473,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_group.svg",
      "sha256": "a863d3bd8d66ea77c53543b8771a29cc3c5e135065d65081e155ae50be06d57e",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 329.575,
    "y": 677.5397849462365,
    "w": 36.7125,
    "h": 38.38279569892473,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "a55d6b3117a99886252fd0de5ba8487754bd95800b2e050040539e070b7b56e5",
      "method": "reference_svg",
      "reference_sha256": "830d66fea2585ceee2587d7d1804f1064399a5c7847079ffe99bcfd60b753fe9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_15",
    "x": 36.5767137829495,
    "y": 12.75437319066011,
    "w": 51.42671261331776,
    "h": 23.05745421393009,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.151708792537082,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_16",
    "x": 135.07835184451113,
    "y": 61.01612984654478,
    "w": 160.87296539670422,
    "h": 66.05913726981377,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 55.853223542832396,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_17",
    "x": 135.0783528295226,
    "y": 130.37634442131588,
    "w": 164.52117626069835,
    "h": 29.801010787801207,
    "text": "10\u670821\u65e5 \u661f\u671f\u4e09",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.220909709021086,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_28",
    "x": 36.57671290322741,
    "y": 729.0645164076411,
    "w": 40.48208638102556,
    "h": 22.252687432298206,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.427418689068386,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_30",
    "x": 135.07834681852367,
    "y": 729.0645163975008,
    "w": 36.83387869687655,
    "h": 22.252687432298206,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.427418689068386,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_31",
    "x": 229.93177306217277,
    "y": 729.0645166814312,
    "w": 44.130294065174574,
    "h": 22.252687432298206,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.427418689068386,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_32",
    "x": 328.43340703827255,
    "y": 729.0645166814312,
    "w": 40.4820863810256,
    "h": 22.252687432298206,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.427418689068386,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
