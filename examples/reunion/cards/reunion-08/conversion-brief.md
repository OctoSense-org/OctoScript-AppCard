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
    "y": 0.0,
    "w": 405.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirmed_card",
    "x": 23.362139917695472,
    "y": 53.402150537634405,
    "w": 362.11316872427983,
    "h": 340.43870967741935,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_reunion",
    "x": 48.39300411522634,
    "y": 320.4129032258064,
    "w": 315.3888888888889,
    "h": 50.064516129032256,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_reunion_surface",
    "x": 48.39300411522634,
    "y": 320.4129032258064,
    "w": 315.3888888888889,
    "h": 50.064516129032256,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_reunion_control",
    "x": 48.39300411522634,
    "y": 320.4129032258064,
    "w": 315.3888888888889,
    "h": 50.064516129032256,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_175",
    "x": 108.46707818930041,
    "y": 335.43225806451613,
    "w": 194.23456790123456,
    "h": 29.032258064516128,
    "text": "\u67e5\u770b\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.529032258064515,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 51.73045267489712,
    "y": 81.77204301075268,
    "w": 31.70576131687243,
    "h": 33.376344086021504,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_1",
    "x": 53.39917695473251,
    "y": 195.2516129032258,
    "w": 21.69341563786008,
    "h": 25.032258064516128,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/pin_icon_1.svg",
      "sha256": "2bf55d3cae2ca238d7cf5c17c98856c017509e3c05ad30cc2786bb71177e8dc1",
      "method": "reference_svg",
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_2",
    "x": 53.39917695473251,
    "y": 233.63440860215053,
    "w": 21.69341563786008,
    "h": 25.032258064516128,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_170",
    "x": 103.40225134240733,
    "y": 82.74595676546605,
    "w": 120.81629675991292,
    "h": 29.900558726886203,
    "text": "\u805a\u4f1a \u00b7 \u5df2\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.310502854197583,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_171",
    "x": 45.06951728665693,
    "y": 137.67741988598158,
    "w": 273.9632903398327,
    "h": 40.8447358263053,
    "text": "\u5341\u5e74\u540c\u7a97 \u518d\u805a\u4e00\u5802",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 33.16026224367477,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_172",
    "x": 88.84735530915206,
    "y": 196.08602176669618,
    "w": 204.6483777183249,
    "h": 25.903224918758067,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.71290242688226,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_173",
    "x": 85.19920369240886,
    "y": 232.59139818475674,
    "w": 204.6483777183249,
    "h": 29.553762405217373,
    "text": "\u6728\u5149\u9910\u5385 \u00b7 \u6842\u82b1\u8def8\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.998386164695635,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_174",
    "x": 45.06952160696971,
    "y": 276.25240945947326,
    "w": 197.35208116804867,
    "h": 34.01876365505744,
    "text": "\u6765\u81ea\u738b\u5b81\u7684\u6700\u65b0\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.016887289551697,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_card",
    "x": 23.362139917695472,
    "y": 405.52258064516127,
    "w": 362.11316872427983,
    "h": 243.64731182795697,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "restore_calendar",
    "x": 55.0679012345679,
    "y": 572.4043010752688,
    "w": 298.701646090535,
    "h": 50.064516129032256,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "restore_calendar_surface",
    "x": 55.0679012345679,
    "y": 572.4043010752688,
    "w": 298.701646090535,
    "h": 50.064516129032256,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "restore_calendar_control",
    "x": 55.0679012345679,
    "y": 572.4043010752688,
    "w": 298.701646090535,
    "h": 50.064516129032256,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_179",
    "x": 161.61455910044577,
    "y": 589.7714608952075,
    "w": 88.29918664687857,
    "h": 34.3495520841074,
    "text": "\u91cd\u65b0\u52a0\u5165",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.314596875696665,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_3",
    "x": 51.73045267489712,
    "y": 422.210752688172,
    "w": 36.711934156378604,
    "h": 38.38279569892473,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_4",
    "x": 51.73045267489712,
    "y": 525.6774193548387,
    "w": 23.362139917695472,
    "h": 25.032258064516128,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_4.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_176",
    "x": 114.33537253083415,
    "y": 444.0537528851694,
    "w": 142.72787743575847,
    "h": 30.091419248078854,
    "text": "\u65e5\u5386\u8bb0\u5f55\u5df2\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.482277323270967,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_177",
    "x": 110.7362629225588,
    "y": 476.37750095607123,
    "w": 128.03718126572517,
    "h": 27.347927287266682,
    "text": "\u62a5\u540d\u4ecd\u7136\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.013134558540013,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_178",
    "x": 96.14365699123873,
    "y": 524.6344088634708,
    "w": 193.7039265333183,
    "h": 25.903224918757786,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.712902426882007,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 0.0,
    "y": 662.5204301075269,
    "w": 405.5,
    "h": 113.47956989247311,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.37448559670782,
    "y": 677.5397849462365,
    "w": 36.711934156378604,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 132.94170096021946,
    "y": 677.5397849462365,
    "w": 36.711934156378604,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.5089163237311,
    "y": 677.5397849462365,
    "w": 36.711934156378604,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.0761316872428,
    "y": 677.5397849462365,
    "w": 36.711934156378604,
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
      "reference_sha256": "b93dec82533d38982f833db84f09bd087c33309da9a0a95c22dd3dea6a102e67",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_168",
    "x": 30.4769093003182,
    "y": 12.754373555713807,
    "w": 51.42598163332953,
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
    "id": "text_180",
    "x": 34.12506251505668,
    "y": 729.0645169379329,
    "w": 40.48152408873077,
    "h": 26.48498418172526,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.236485763552736,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_181",
    "x": 132.62517820314451,
    "y": 729.0645163848253,
    "w": 36.83337263379648,
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
    "id": "text_182",
    "x": 333.2735636732707,
    "y": 729.0645168466696,
    "w": 40.48152408873077,
    "h": 26.48498418172526,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.236485763552736,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
