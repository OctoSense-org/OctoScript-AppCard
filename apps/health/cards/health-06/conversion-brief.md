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
    "x": 26.017543859649123,
    "y": 0.0,
    "w": 353.96491228070175,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wallpaper_upper",
    "x": 26.017543859649123,
    "y": 0.0,
    "w": 353.96491228070175,
    "h": 158.83040935672514,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wallpaper_lower",
    "x": 26.017543859649123,
    "y": 639.859649122807,
    "w": 353.96491228070175,
    "h": 136.140350877193,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "picker_card",
    "x": 38.11890838206628,
    "y": 105.8869395711501,
    "w": 331.27485380116957,
    "h": 527.9220272904483,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "selected_summary",
    "x": 59.2962962962963,
    "y": 178.495126705653,
    "w": 291.94541910331384,
    "h": 90.76023391812865,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "selected_day",
    "x": 77.13183552810929,
    "y": 195.04950320651733,
    "w": 150.67953033149826,
    "h": 31.382679571662543,
    "text": "\u5468\u516d 10\u670824\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.465892001646164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "selected_time",
    "x": 73.72082524478043,
    "y": 235.30626219814948,
    "w": 146.72237665425502,
    "h": 26.676189250632625,
    "text": "14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.088856003088342,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "conflict_slot",
    "x": 59.2962962962963,
    "y": 282.86939571150094,
    "w": 290.43274853801165,
    "h": 86.22222222222221,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "conflict_slot_surface",
    "x": 59.2962962962963,
    "y": 282.86939571150094,
    "w": 290.43274853801165,
    "h": 86.22222222222221,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "conflict_slot_control",
    "x": 59.2962962962963,
    "y": 282.86939571150094,
    "w": 290.43274853801165,
    "h": 86.22222222222221,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "morning_radio",
    "x": 80.47368421052632,
    "y": 313.12280701754383,
    "w": 24.202729044834307,
    "h": 24.202729044834307,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "morning_time",
    "x": 120.430594642287,
    "y": 300.3113376163422,
    "w": 135.94320244445206,
    "h": 25.665429296160767,
    "text": "09:00\u201310:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.148849245429513,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "morning_note",
    "x": 120.43059688662063,
    "y": 329.0345106863277,
    "w": 139.53625666746618,
    "h": 25.700586195483627,
    "text": "\u4e0e\u5df2\u6709\u65e5\u7a0b\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.181545161799775,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon",
    "x": 59.2962962962963,
    "y": 378.16764132553607,
    "w": 290.43274853801165,
    "h": 84.70955165692007,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "afternoon_surface",
    "x": 59.2962962962963,
    "y": 378.16764132553607,
    "w": 290.43274853801165,
    "h": 84.70955165692007,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "afternoon_control",
    "x": 59.2962962962963,
    "y": 378.16764132553607,
    "w": 290.43274853801165,
    "h": 84.70955165692007,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "afternoon_radio",
    "x": 80.47368421052632,
    "y": 408.4210526315789,
    "w": 24.202729044834307,
    "h": 24.202729044834307,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "afternoon_time",
    "x": 116.83754350032142,
    "y": 393.87259159001457,
    "w": 143.12931089048027,
    "h": 25.56874728237923,
    "text": "14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.058934972612686,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon_note",
    "x": 120.43059721140602,
    "y": 425.78625225769844,
    "w": 82.0473083139163,
    "h": 29.699681150717065,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.90070347016687,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirm_booking",
    "x": 59.2962962962963,
    "y": 485.5672514619883,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_booking_surface",
    "x": 59.2962962962963,
    "y": 485.5672514619883,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_booking_control",
    "x": 59.2962962962963,
    "y": 485.5672514619883,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_booking_text",
    "x": 156.20953163895615,
    "y": 501.2370639571398,
    "w": 93.12980833295256,
    "h": 33.71685951569015,
    "text": "\u786e\u8ba4\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.636679349591844,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_selection",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_selection_surface",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_selection_control",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 290.43274853801165,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_selection_text",
    "x": 181.5126075851249,
    "y": 573.6121539970487,
    "w": 42.52365415695815,
    "h": 25.56874728237923,
    "text": "\u8fd4\u56de",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.058934972612686,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 55.75552848104536,
    "y": 130.99579188460223,
    "w": 157.50155086405798,
    "h": 33.215369641326554,
    "text": "\u786e\u8ba4\u9884\u7ea6\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.170293766433698,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 36.606237816764136,
    "y": 680.7017543859648,
    "w": 334.3001949317739,
    "h": 89.2475633528265,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_icon_heart",
    "x": 89.54970760233917,
    "y": 694.3157894736842,
    "w": 40.84210526315789,
    "h": 40.84210526315789,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_heart.svg",
      "sha256": "2b22eedb8ac2a5c9900ec3322b642276bd7df7d765b7a57cdbd7a3cdf2b74bc3",
      "method": "reference_svg",
      "reference_sha256": "aa58dacee95641dc9fc99cf4e2c25ccebe38ce7bd08bdeb860c442eb18b5522e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_icon_calendar",
    "x": 180.30994152046782,
    "y": 694.3157894736842,
    "w": 40.84210526315789,
    "h": 40.84210526315789,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_calendar.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "aa58dacee95641dc9fc99cf4e2c25ccebe38ce7bd08bdeb860c442eb18b5522e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_icon_mail",
    "x": 271.0701754385965,
    "y": 694.3157894736842,
    "w": 40.84210526315789,
    "h": 40.84210526315789,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_mail.svg",
      "sha256": "15d753dccafef2720d25c32622d763eec99dd814785def83c52611c446bd8d9f",
      "method": "reference_svg",
      "reference_sha256": "aa58dacee95641dc9fc99cf4e2c25ccebe38ce7bd08bdeb860c442eb18b5522e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_health",
    "x": 94.08771929824562,
    "y": 742.7212475633528,
    "w": 39.304093567251456,
    "h": 22.152046783625728,
    "text": "\u5065\u5eb7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.88140350877193,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar",
    "x": 183.3352826510721,
    "y": 742.7212475633528,
    "w": 39.304093567251456,
    "h": 22.152046783625728,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.88140350877193,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_mail",
    "x": 274.09551656920075,
    "y": 742.7212475633528,
    "w": 39.304093567251456,
    "h": 22.152046783625728,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.88140350877193,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_time",
    "x": 52.16246926350621,
    "y": 20.01430245632719,
    "w": 64.08200834694428,
    "h": 25.78847808336352,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.263284617528072,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 52.16246542754389,
    "y": 48.77263240202937,
    "w": 103.60566827428275,
    "h": 21.973956308935033,
    "text": "10\u670822\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.715779367309583,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
