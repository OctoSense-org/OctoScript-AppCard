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
    "id": "saturday",
    "x": 62.32163742690058,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_surface",
    "x": 62.32163742690058,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_control",
    "x": 62.32163742690058,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_name",
    "x": 107.71296064354007,
    "y": 192.56428149970347,
    "w": 49.70977125855683,
    "h": 29.16353969753692,
    "text": "\u5468\u516d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.402091918709335,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "saturday_date",
    "x": 86.041437636783,
    "y": 224.45731030649637,
    "w": 89.45975415562562,
    "h": 26.488933762260665,
    "text": "10\u670824\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.91470839890242,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunday",
    "x": 212.07602339181287,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_surface",
    "x": 212.07602339181287,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_control",
    "x": 212.07602339181287,
    "y": 178.495126705653,
    "w": 139.16569200779728,
    "h": 81.68421052631578,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_name",
    "x": 262.214516880539,
    "y": 192.5642820564907,
    "w": 42.52365415695815,
    "h": 25.577536687424132,
    "text": "\u5468\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.067109119304444,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunday_date",
    "x": 236.93090545640374,
    "y": 220.86347450541194,
    "w": 89.49781558388156,
    "h": 30.081811582175206,
    "text": "10\u670825\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.25608477142294,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "conflict_slot",
    "x": 60.80896686159844,
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
    "x": 60.80896686159844,
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
    "x": 60.80896686159844,
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
    "x": 122.08520101813522,
    "y": 300.31133787955474,
    "w": 139.53625666746618,
    "h": 22.140951400506374,
    "text": "09:00\u201310:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.87108480247093,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "morning_note",
    "x": 125.67825540749698,
    "y": 329.0345111982976,
    "w": 135.94320244445206,
    "h": 25.70058547462716,
    "text": "\u4e0e\u5df2\u6709\u65e5\u7a0b\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.181544491403262,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon",
    "x": 60.80896686159844,
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
    "x": 60.80896686159844,
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
    "x": 60.80896686159844,
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
    "x": 122.08519594127314,
    "y": 393.87259161135165,
    "w": 135.94320244445203,
    "h": 22.307946492077168,
    "text": "14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.026390237631766,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "afternoon_note",
    "x": 125.63855457294942,
    "y": 422.49167080100483,
    "w": 78.53365452340704,
    "h": 25.847248804589896,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.317941388268604,
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
    "w": 291.94541910331384,
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
    "w": 291.94541910331384,
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
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_booking_text",
    "x": 161.60885475391487,
    "y": 505.3111200817862,
    "w": 89.2334225303248,
    "h": 25.762110589085555,
    "text": "\u786e\u8ba4\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.238762847849568,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "return_items",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_items_surface",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "return_items_control",
    "x": 59.2962962962963,
    "y": 556.6627680311891,
    "w": 291.94541910331384,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_items_text",
    "x": 165.12390777309852,
    "y": 573.3236848737314,
    "w": 82.20331631487572,
    "h": 26.145684896398993,
    "text": "\u8fd4\u56de\u9879\u76ee",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.595486953651065,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 57.410128630252316,
    "y": 130.99579188460223,
    "w": 157.50155086405792,
    "h": 33.215369641326554,
    "text": "\u9009\u62e9\u9884\u7ea6\u65f6\u95f4",
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
      "reference_sha256": "aa08d79d89018fde6067326ec560516461f6173d57345c0fb7915461e4c57ef9",
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
      "reference_sha256": "aa08d79d89018fde6067326ec560516461f6173d57345c0fb7915461e4c57ef9",
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
      "reference_sha256": "aa08d79d89018fde6067326ec560516461f6173d57345c0fb7915461e4c57ef9",
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
    "x": 50.22400841943909,
    "y": 20.014302815806385,
    "w": 64.08200834694428,
    "h": 25.78847736250705,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.263283947131555,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 50.224007168485734,
    "y": 48.772632615053816,
    "w": 107.19872249729684,
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
