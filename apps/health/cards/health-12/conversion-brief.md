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
    "id": "summary_card",
    "x": 38.11890838206628,
    "y": 86.22222222222221,
    "w": 331.27485380116957,
    "h": 535.485380116959,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "booking_status_surface",
    "x": 56.27095516569201,
    "y": 388.75633528265104,
    "w": 293.45808966861597,
    "h": 62.01949317738791,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_icon_5",
    "x": 71.39766081871345,
    "y": 408.4210526315789,
    "w": 34.79142300194932,
    "h": 33.278752436647174,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_5.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "check_icon_7",
    "x": 311.9122807017544,
    "y": 420.52241715399606,
    "w": 18.152046783625728,
    "h": 18.152046783625728,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_7.svg",
      "sha256": "c3793081e2c58cd466d16deb9ff8d50c89fe1cf69372fcdefd3b92bc7da06326",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "booking_label",
    "x": 116.77777777777777,
    "y": 412.95906432748535,
    "w": 46.86744639376218,
    "h": 28.202729044834307,
    "text": "\u9884\u7ea6",
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
    "id": "booking_status",
    "x": 242.87848057852452,
    "y": 414.243075292811,
    "w": 56.89588836015544,
    "h": 25.62148299179245,
    "text": "\u5df2\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.107979182366982,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_status_surface",
    "x": 56.27095516569201,
    "y": 450.77582846003895,
    "w": 293.45808966861597,
    "h": 63.53216374269005,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_icon_6",
    "x": 71.39766081871345,
    "y": 464.38986354775824,
    "w": 34.79142300194932,
    "h": 33.278752436647174,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_6.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "check_icon_8",
    "x": 311.9122807017544,
    "y": 474.97855750487327,
    "w": 18.152046783625728,
    "h": 18.152046783625728,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_8.svg",
      "sha256": "c3793081e2c58cd466d16deb9ff8d50c89fe1cf69372fcdefd3b92bc7da06326",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_label",
    "x": 117.12139609741425,
    "y": 467.61122323330136,
    "w": 42.523654156958074,
    "h": 26.6761892506329,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.088856003088598,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_status",
    "x": 242.87848057852452,
    "y": 467.61122293373523,
    "w": 56.89588836015544,
    "h": 26.676189250632625,
    "text": "\u5df2\u540c\u6b65",
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
    "id": "return_booking",
    "x": 57.783625730994146,
    "y": 541.5360623781676,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_booking_surface",
    "x": 57.783625730994146,
    "y": 541.5360623781676,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "return_booking_control",
    "x": 57.783625730994146,
    "y": 541.5360623781676,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "return_booking_text",
    "x": 81.09627492905128,
    "y": 557.7080177187099,
    "w": 89.42248326946653,
    "h": 29.816952992784845,
    "text": "\u8fd4\u56de\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.009766283289906,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_booking",
    "x": 207.53801169590642,
    "y": 541.5360623781676,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_booking_surface",
    "x": 207.53801169590642,
    "y": 541.5360623781676,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_booking_control",
    "x": 207.53801169590642,
    "y": 541.5360623781676,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_booking_text",
    "x": 239.17123351985617,
    "y": 557.6099331223561,
    "w": 82.27567688345219,
    "h": 26.418331620957098,
    "text": "\u53d6\u6d88\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.849048407490102,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_0",
    "x": 177.28460038986353,
    "y": 108.91228070175438,
    "w": 51.4307992202729,
    "h": 51.4307992202729,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_0.svg",
      "sha256": "c3793081e2c58cd466d16deb9ff8d50c89fe1cf69372fcdefd3b92bc7da06326",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "clinic_icon_1",
    "x": 63.834307992202724,
    "y": 225.38791423001948,
    "w": 22.690058479532162,
    "h": 22.690058479532162,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clinic_icon_1.svg",
      "sha256": "aee44823e6d8dcb6ddb99ad40d85b6ffc23aa7f22f28e68b59ab5c7f4a36cce0",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "package_icon_2",
    "x": 63.834307992202724,
    "y": 264.7173489278752,
    "w": 22.690058479532162,
    "h": 22.690058479532162,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/package_icon_2.svg",
      "sha256": "bea33ddde09ec253eaa9f98cf68c8b325907c847379ea0b5fb05d5cf33adfa6e",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 63.834307992202724,
    "y": 305.5594541910331,
    "w": 22.690058479532162,
    "h": 22.690058479532162,
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
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "location_icon_4",
    "x": 66.85964912280701,
    "y": 340.3508771929824,
    "w": 19.664717348927873,
    "h": 22.690058479532162,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/location_icon_4.svg",
      "sha256": "8d619793a1efb90d858f56d3f5a75b9dd0607a6468b3bdce234d1da9c8297ba5",
      "method": "reference_svg",
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "title",
    "x": 142.2728144733501,
    "y": 172.82076257492602,
    "w": 121.57096247087438,
    "h": 33.32962830262794,
    "text": "\u9884\u7ea6\u5df2\u5c31\u7eea",
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
    "id": "appointment_title",
    "x": 88.37692160942919,
    "y": 227.24361722688715,
    "w": 92.82648252371918,
    "h": 25.639061081025783,
    "text": "\u5e74\u5ea6\u4f53\u68c0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.12432680535398,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "package_summary",
    "x": 88.13151054191403,
    "y": 265.9912269862197,
    "w": 89.72424530564685,
    "h": 30.894353981308868,
    "text": "\u57fa\u7840\u5957\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.01174920261725,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_time",
    "x": 99.15610143642913,
    "y": 305.8544062838879,
    "w": 243.7349791647631,
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
    "id": "provider_name",
    "x": 98.94363251995395,
    "y": 341.15489952014997,
    "w": 118.40283905088782,
    "h": 27.953448464213654,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.2767070717187,
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
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
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
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
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
      "reference_sha256": "20b4793c46c12ecbfe45b0a0d6fa7d0765d84e9392e4f3318ae20af9fba0389c",
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
    "x": 48.853267219369876,
    "y": 18.622676033384657,
    "w": 67.67506834033863,
    "h": 25.762109868228812,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.238762177452795,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 48.85326922621795,
    "y": 47.34584906811421,
    "w": 107.19872249729669,
    "h": 22.202475794107478,
    "text": "10\u670822\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.928302488519957,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
