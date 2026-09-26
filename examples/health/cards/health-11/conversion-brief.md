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
    "id": "cancel_card",
    "x": 38.11890838206628,
    "y": 140.6783625730994,
    "w": 331.27485380116957,
    "h": 461.364522417154,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "cancel_summary",
    "x": 56.27095516569201,
    "y": 308.5847953216374,
    "w": 294.9707602339181,
    "h": 137.65302144249512,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "clinic_icon_0",
    "x": 69.8849902534113,
    "y": 331.27485380116957,
    "w": 30.253411306042885,
    "h": 33.278752436647174,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clinic_icon_0.svg",
      "sha256": "aee44823e6d8dcb6ddb99ad40d85b6ffc23aa7f22f28e68b59ab5c7f4a36cce0",
      "method": "reference_svg",
      "reference_sha256": "f808ffade5130b530e88eeb26b40854937948dde60993678f53ea2646aa8adb1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_icon_1",
    "x": 69.8849902534113,
    "y": 385.7309941520468,
    "w": 24.202729044834307,
    "h": 25.71539961013645,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "f808ffade5130b530e88eeb26b40854937948dde60993678f53ea2646aa8adb1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "provider_name",
    "x": 107.7017543859649,
    "y": 335.812865497076,
    "w": 166.36842105263156,
    "h": 28.202729044834307,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.508538011695908,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_time",
    "x": 107.99682494091832,
    "y": 392.0239255657392,
    "w": 229.36273919118543,
    "h": 26.676189250632625,
    "text": "\u5468\u65e5 10\u670825\u65e5 10:00\u201311:00",
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
    "id": "keep_booking",
    "x": 59.2962962962963,
    "y": 523.3840155945419,
    "w": 139.16569200779728,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "keep_booking_surface",
    "x": 59.2962962962963,
    "y": 523.3840155945419,
    "w": 139.16569200779728,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "keep_booking_control",
    "x": 59.2962962962963,
    "y": 523.3840155945419,
    "w": 139.16569200779728,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "keep_booking_text",
    "x": 86.39529840213845,
    "y": 539.9366834570405,
    "w": 85.72669319613865,
    "h": 33.006501429091635,
    "text": "\u4fdd\u7559\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.976046329055222,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirm_cancel",
    "x": 209.05068226120858,
    "y": 523.3840155945419,
    "w": 137.65302144249512,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_cancel_surface",
    "x": 209.05068226120858,
    "y": 523.3840155945419,
    "w": 137.65302144249512,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_cancel_control",
    "x": 209.05068226120858,
    "y": 523.3840155945419,
    "w": 137.65302144249512,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_cancel_text",
    "x": 237.34695995608115,
    "y": 540.060770100517,
    "w": 85.64036830731081,
    "h": 29.81393981201845,
    "text": "\u786e\u8ba4\u53d6\u6d88",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.00696402517716,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 61.287047379206015,
    "y": 172.82076257492602,
    "w": 161.0946166278326,
    "h": 33.32962830262794,
    "text": "\u53d6\u6d88\u4f53\u68c0\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.27655432144398,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_note",
    "x": 64.88011427415842,
    "y": 223.71914033926723,
    "w": 265.293327584369,
    "h": 29.16353681411022,
    "text": "\u8fd9\u4f1a\u53d6\u6d88\u9884\u7ea6\u5e76\u79fb\u9664\u5173\u8054\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.402089237122507,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "scope_note",
    "x": 64.88010879311685,
    "y": 255.9667904093241,
    "w": 240.1419249417489,
    "h": 32.86379920638113,
    "text": "\u4ec5\u64a4\u9500\u65e5\u5386\u4e0d\u4f1a\u53d6\u6d88\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.84333326193445,
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
      "reference_sha256": "f808ffade5130b530e88eeb26b40854937948dde60993678f53ea2646aa8adb1",
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
      "reference_sha256": "f808ffade5130b530e88eeb26b40854937948dde60993678f53ea2646aa8adb1",
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
      "reference_sha256": "f808ffade5130b530e88eeb26b40854937948dde60993678f53ea2646aa8adb1",
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
    "x": 50.50786758724882,
    "y": 18.62267576187692,
    "w": 64.08200834694428,
    "h": 25.76211058908528,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.238762847849312,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 50.507872491075446,
    "y": 47.34584902317861,
    "w": 110.79177672031088,
    "h": 22.20247579410775,
    "text": "10\u670822\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.92830248852021,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
