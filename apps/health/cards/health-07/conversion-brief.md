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
    "h": 313.12280701754383,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "edit_booking",
    "x": 60.80896686159844,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "edit_booking_surface",
    "x": 60.80896686159844,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "edit_booking_control",
    "x": 60.80896686159844,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "edit_booking_text",
    "x": 86.43846246450556,
    "y": 343.54551420663324,
    "w": 85.64036830731081,
    "h": 25.770899273273713,
    "text": "\u4fee\u6539\u9884\u7ea6",
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
    "id": "view_booking",
    "x": 209.05068226120858,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_booking_surface",
    "x": 209.05068226120858,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_booking_control",
    "x": 209.05068226120858,
    "y": 326.7368421052631,
    "w": 139.16569200779728,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_booking_text",
    "x": 237.2662741428369,
    "y": 343.2469955338611,
    "w": 82.20867699814582,
    "h": 26.16578526302481,
    "text": "\u67e5\u770b\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.614180294613075,
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_icon_1",
    "x": 65.34697855750487,
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "booking_title",
    "x": 104.33031111624382,
    "y": 113.07547129704743,
    "w": 139.68315900836066,
    "h": 29.97034551950775,
    "text": "\u5065\u5eb7 \u00b7 \u9884\u7ea6\u6210\u529f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.152421333142208,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_title",
    "x": 61.18573573162788,
    "y": 167.030515395215,
    "w": 107.40134363007132,
    "h": 33.4987859641273,
    "text": "\u5e74\u5ea6\u4f53\u68c0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.43387094663839,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "package_summary",
    "x": 64.88010766278762,
    "y": 203.3486566364701,
    "w": 96.41954251711351,
    "h": 29.910621104942965,
    "text": "\u57fa\u7840\u5957\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.09687762759696,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_time",
    "x": 99.7602304684095,
    "y": 242.8649919455933,
    "w": 248.3785080342729,
    "h": 25.59511477665747,
    "text": "\u5468\u516d 10\u670824\u65e5 14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.08345674229145,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "provider_name",
    "x": 97.08878897233501,
    "y": 278.1094989562934,
    "w": 121.8286676536992,
    "h": 27.028293119493792,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.416312601129228,
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
    "y": 420.52241715399606,
    "w": 331.27485380116957,
    "h": 237.48927875243663,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_confirm",
    "x": 62.32163742690058,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_confirm_surface",
    "x": 62.32163742690058,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_confirm_control",
    "x": 62.32163742690058,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_confirm_text",
    "x": 104.40376141026135,
    "y": 598.1252902222698,
    "w": 56.89588836015544,
    "h": 29.81393981201845,
    "text": "\u786e\u8ba4",
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
    "id": "calendar_undo",
    "x": 209.05068226120858,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_undo_surface",
    "x": 209.05068226120858,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_undo_control",
    "x": 209.05068226120858,
    "y": 580.8654970760233,
    "w": 137.65302144249512,
    "h": 55.968810916179336,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "calendar_undo_text",
    "x": 233.75390014542802,
    "y": 598.1252902222698,
    "w": 89.23342830070514,
    "h": 29.81393981201845,
    "text": "\u64a4\u9500\u65e5\u7a0b",
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_title",
    "x": 104.32135916620577,
    "y": 443.8068635021697,
    "w": 121.73576453136417,
    "h": 29.949148009071354,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.132707648436362,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_event_title",
    "x": 57.693990704911336,
    "y": 487.3371635549177,
    "w": 110.79177672031103,
    "h": 36.35312164442559,
    "text": "\u5e74\u5ea6\u4f53\u68c0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.0884031293158,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_note",
    "x": 61.2870510890002,
    "y": 522.53799288423,
    "w": 182.6529650474385,
    "h": 29.910622546656448,
    "text": "\u540c\u4e00\u9884\u7ea6\u5df2\u52a0\u5165\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.0968789683905,
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
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
      "reference_sha256": "b3e9cc02937b34ee485d1bf5df3d141fc224f57193251bb9b80f9b0365fe48ad",
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
    "x": 50.50786889801603,
    "y": 48.772632615053816,
    "w": 110.79177672031103,
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
