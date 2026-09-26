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
    "y": 1.0,
    "w": 406.0,
    "h": 773.5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirmed_card",
    "x": 23.295081967213115,
    "y": 52.56666666666666,
    "w": 361.07377049180326,
    "h": 329.3612903225806,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_reunion",
    "x": 49.91803278688524,
    "y": 307.0731182795699,
    "w": 307.827868852459,
    "h": 53.23010752688172,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_reunion_surface",
    "x": 49.91803278688524,
    "y": 307.0731182795699,
    "w": 307.827868852459,
    "h": 53.23010752688172,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_reunion_control",
    "x": 49.91803278688524,
    "y": 307.0731182795699,
    "w": 307.827868852459,
    "h": 53.23010752688172,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_118",
    "x": 111.48360655737704,
    "y": 323.7075268817204,
    "w": 197.01639344262296,
    "h": 27.28817204301075,
    "text": "\u67e5\u770b\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.959354838709675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 51.58196721311475,
    "y": 82.50860215053763,
    "w": 31.614754098360656,
    "h": 33.26881720430107,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_1",
    "x": 53.24590163934426,
    "y": 192.29569892473117,
    "w": 21.631147540983605,
    "h": 24.951612903225804,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_2",
    "x": 53.24590163934426,
    "y": 230.5548387096774,
    "w": 21.631147540983605,
    "h": 24.951612903225804,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_113",
    "x": 100.43926618906235,
    "y": 82.98177347116037,
    "w": 124.36176287290536,
    "h": 34.45110285641465,
    "text": "\u805a\u4f1a \u00b7 \u5df2\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.405992570773183,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_114",
    "x": 46.033204780228985,
    "y": 134.59509466969547,
    "w": 269.5507004461673,
    "h": 44.36481173637122,
    "text": "\u5341\u5e74\u540c\u7a97 \u518d\u805a\u4e00\u5802",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 36.3283305627341,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_115",
    "x": 89.68537432026038,
    "y": 192.81552445402653,
    "w": 185.88404018533745,
    "h": 26.0404532378786,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.836407914090742,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_116",
    "x": 89.85245901639344,
    "y": 228.89139784946235,
    "w": 253.59016393442622,
    "h": 32.27849462365592,
    "text": "\u6728\u5149\u9910\u5385 \u00b7 \u6842\u82b1\u8def8\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.45064516129032,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_117",
    "x": 49.670882128525015,
    "y": 272.8686158518762,
    "w": 171.33332052165966,
    "h": 25.832660405488593,
    "text": "\u6765\u81ea\u738b\u5b81\u7684\u6700\u65b0\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.649394364939734,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_card",
    "x": 23.295081967213115,
    "y": 393.5720430107527,
    "w": 361.07377049180326,
    "h": 251.1795698924731,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "ack_calendar",
    "x": 46.59016393442623,
    "y": 583.2043010752687,
    "w": 141.4344262295082,
    "h": 48.239784946236554,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "ack_calendar_surface",
    "x": 46.59016393442623,
    "y": 583.2043010752687,
    "w": 141.4344262295082,
    "h": 48.239784946236554,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "ack_calendar_control",
    "x": 46.59016393442623,
    "y": 583.2043010752687,
    "w": 141.4344262295082,
    "h": 48.239784946236554,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "ack_label",
    "x": 91.51639344262294,
    "y": 596.5118279569892,
    "w": 65.5655737704918,
    "h": 27.28817204301075,
    "text": "\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.959354838709675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "undo_calendar",
    "x": 201.3360655737705,
    "y": 583.2043010752687,
    "w": 158.0737704918033,
    "h": 48.239784946236554,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "undo_calendar_surface",
    "x": 201.3360655737705,
    "y": 583.2043010752687,
    "w": 158.0737704918033,
    "h": 48.239784946236554,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "undo_calendar_control",
    "x": 201.3360655737705,
    "y": 583.2043010752687,
    "w": 158.0737704918033,
    "h": 48.239784946236554,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_123",
    "x": 224.6311475409836,
    "y": 596.5118279569892,
    "w": 127.1311475409836,
    "h": 27.28817204301075,
    "text": "\u64a4\u9500\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.959354838709675,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_3",
    "x": 51.58196721311475,
    "y": 421.85053763440857,
    "w": 31.614754098360656,
    "h": 33.26881720430107,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_119",
    "x": 100.55563047779266,
    "y": 421.867838329125,
    "w": 116.85366960099893,
    "h": 29.852697294536632,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.26742756508297,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_120",
    "x": 46.03319826060673,
    "y": 469.1934343301682,
    "w": 127.68114884795062,
    "h": 40.5713989918462,
    "text": "\u540c\u5b66\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.91425909266158,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_121",
    "x": 86.52459016393442,
    "y": 511.67634408602146,
    "w": 246.9344262295082,
    "h": 33.941935483870964,
    "text": "10\u670824\u65e5 18:30\u201321:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.947741935483872,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_122",
    "x": 86.04768797129569,
    "y": 545.6609045444147,
    "w": 127.68114884795062,
    "h": 25.948638205859794,
    "text": "\u5df2\u52a0\u5165\u4e2a\u4eba\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.753774385273815,
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
    "y": 661.3860215053763,
    "w": 406.0,
    "h": 113.11397849462365,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.278688524590166,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.11475409836066,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.95081967213113,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.78688524590166,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
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
      "reference_sha256": "57f1791d70a55e488ba70376912efbb7ec1b9e14f99b572e7e8c908a2443f7f9",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_112",
    "x": 35.12015637163219,
    "y": 13.713283389237782,
    "w": 47.65216850304031,
    "h": 22.99605777638521,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.09645199874669,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_124",
    "x": 35.120156377014574,
    "y": 727.7157260669297,
    "w": 40.37680867120131,
    "h": 26.412545444026403,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.171290899623763,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_126",
    "x": 133.33754042833317,
    "y": 727.715726038678,
    "w": 36.739128755281996,
    "h": 22.193883671240542,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_147",
    "x": 329.7723093413748,
    "y": 727.7157259477091,
    "w": 40.37680867120131,
    "h": 22.193883671240542,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
