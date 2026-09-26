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
    "id": "booking_card",
    "x": 38.11890838206628,
    "y": 89.2475633528265,
    "w": 331.27485380116957,
    "h": 314.63547758284597,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_booking",
    "x": 59.2962962962963,
    "y": 326.7368421052631,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_booking_surface",
    "x": 59.2962962962963,
    "y": 326.7368421052631,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_booking_control",
    "x": 59.2962962962963,
    "y": 326.7368421052631,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_booking_text",
    "x": 163.83116962315117,
    "y": 343.54551433735304,
    "w": 82.0473083139163,
    "h": 25.770899273273713,
    "text": "\u67e5\u770b\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.246936324144553,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "heart_icon_0",
    "x": 63.834307992202724,
    "y": 110.42495126705653,
    "w": 31.766081871345026,
    "h": 31.766081871345026,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/heart_icon_0.svg",
      "sha256": "2b22eedb8ac2a5c9900ec3322b642276bd7df7d765b7a57cdbd7a3cdf2b74bc3",
      "method": "reference_svg",
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_icon_1",
    "x": 63.834307992202724,
    "y": 242.02729044834308,
    "w": 21.177387914230017,
    "h": 21.177387914230017,
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
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "location_icon_2",
    "x": 65.34697855750487,
    "y": 276.81871345029236,
    "w": 21.177387914230017,
    "h": 24.202729044834307,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/location_icon_2.svg",
      "sha256": "8d619793a1efb90d858f56d3f5a75b9dd0607a6468b3bdce234d1da9c8297ba5",
      "method": "reference_svg",
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "booking_title",
    "x": 102.65246966128323,
    "y": 112.94513349411484,
    "w": 139.72963365104928,
    "h": 30.231021698656402,
    "text": "\u5065\u5eb7 \u00b7 \u9884\u7ea6\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.394850179750456,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_title",
    "x": 59.58902737035548,
    "y": 167.2559927345927,
    "w": 110.8786209433632,
    "h": 36.642623439004396,
    "text": "\u5e74\u5ea6\u4f53\u68c0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.35763979827409,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "package_summary",
    "x": 63.023782100548,
    "y": 202.7021872511216,
    "w": 82.4507559912014,
    "h": 30.456476822240806,
    "text": "\u57fa\u7840\u5957\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.60452344468395,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_time",
    "x": 99.15610704027328,
    "y": 242.864991981541,
    "w": 247.3280333877771,
    "h": 25.595114776657745,
    "text": "\u5468\u516d 10\u670824\u65e5 14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.083456742291705,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "provider_name",
    "x": 99.0668407064756,
    "y": 278.35459113339755,
    "w": 118.15642073186984,
    "h": 26.53810916071555,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.960441519465462,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_card",
    "x": 38.11890838206628,
    "y": 422.03508771929825,
    "w": 331.27485380116957,
    "h": 232.9512670565302,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_restore",
    "x": 59.2962962962963,
    "y": 580.8654970760233,
    "w": 291.94541910331384,
    "h": 54.45614035087719,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_restore_surface",
    "x": 59.2962962962963,
    "y": 580.8654970760233,
    "w": 291.94541910331384,
    "h": 54.45614035087719,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_restore_control",
    "x": 59.2962962962963,
    "y": 580.8654970760233,
    "w": 291.94541910331384,
    "h": 54.45614035087719,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_restore_text",
    "x": 156.6450510617977,
    "y": 591.5861094292369,
    "w": 89.23342830070514,
    "h": 33.21536964132683,
    "text": "\u91cd\u65b0\u52a0\u5165",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.170293766433954,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_3",
    "x": 62.32163742690058,
    "y": 443.21247563352824,
    "w": 27.228070175438596,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_title",
    "x": 102.69778475279368,
    "y": 443.9480852231134,
    "w": 143.23206982231503,
    "h": 33.261497257895755,
    "text": "\u65e5\u5386\u8bb0\u5f55\u5df2\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.21319244984305,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_note",
    "x": 56.039387061800255,
    "y": 487.3371637802842,
    "w": 164.68767085084664,
    "h": 33.15384452686844,
    "text": "\u4ec5\u79fb\u9664\u65e5\u5386\u63d0\u9192",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.113075409987648,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "booking_note",
    "x": 56.039388354736076,
    "y": 522.5379929883861,
    "w": 186.24603081121316,
    "h": 34.2349190008436,
    "text": "\u4f53\u68c0\u9884\u7ea6\u4ecd\u7136\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 28.118474670784547,
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
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
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
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
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
      "reference_sha256": "cd13b608950538160bebf6692d4dbba377a459d0d7c6c2347461399b9be5ec78",
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
    "x": 48.85326718353358,
    "y": 20.014302755892984,
    "w": 64.08200834694428,
    "h": 25.788478083363792,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.263284617528328,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 48.85326618708838,
    "y": 48.772632615053816,
    "w": 107.19872249729686,
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
