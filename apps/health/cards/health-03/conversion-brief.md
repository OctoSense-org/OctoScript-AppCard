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
    "id": "appointment_card",
    "x": 42.656920077972714,
    "y": 192.10916179337232,
    "w": 319.1734892787524,
    "h": 366.0662768031189,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "choose_items",
    "x": 68.37231968810916,
    "y": 405.39571150097464,
    "w": 270.7680311890838,
    "h": 62.01949317738791,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_items_surface",
    "x": 68.37231968810916,
    "y": 405.39571150097464,
    "w": 270.7680311890838,
    "h": 62.01949317738791,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "choose_items_control",
    "x": 68.37231968810916,
    "y": 405.39571150097464,
    "w": 270.7680311890838,
    "h": 62.01949317738791,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_items_text",
    "x": 158.22325728956352,
    "y": 423.59925464769185,
    "w": 89.38621642947429,
    "h": 33.21818963251289,
    "text": "\u9009\u62e9\u9879\u76ee",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.172916358236986,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "defer",
    "x": 68.37231968810916,
    "y": 478.0038986354776,
    "w": 270.7680311890838,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "defer_surface",
    "x": 68.37231968810916,
    "y": 478.0038986354776,
    "w": 270.7680311890838,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "defer_control",
    "x": 68.37231968810916,
    "y": 478.0038986354776,
    "w": 270.7680311890838,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "defer_text",
    "x": 161.8927110486056,
    "y": 495.7250109589688,
    "w": 85.64036830731064,
    "h": 29.80515112783029,
    "text": "\u7a0d\u540e\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.99879054888217,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "heart_icon_0",
    "x": 68.37231968810916,
    "y": 213.28654970760232,
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
      "reference_sha256": "da3f995d3b49d7eb37463d7c27707265e57fcce00fdd44b33b8b019274b5a745",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "card_status",
    "x": 111.46564329985024,
    "y": 218.26738016154547,
    "w": 114.63331505847952,
    "h": 26.886156048391065,
    "text": "\u5065\u5eb7 \u00b7 \u5f85\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.28412512500369,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_title",
    "x": 64.62050025513722,
    "y": 275.467327282681,
    "w": 122.09016974674103,
    "h": 38.303954350982096,
    "text": "\u5e74\u5ea6\u4f53\u68c0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 31.90267754641335,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "appointment_note",
    "x": 64.88010218226479,
    "y": 326.5149344645911,
    "w": 225.76968496817125,
    "h": 25.82363498268666,
    "text": "\u9009\u62e9\u9879\u76ee\u548c\u9002\u5408\u4f60\u7684\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.295980533898593,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "provider_name",
    "x": 64.83057889527578,
    "y": 355.317013572582,
    "w": 125.2630710415906,
    "h": 33.18060416716047,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.137961875459233,
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
      "reference_sha256": "da3f995d3b49d7eb37463d7c27707265e57fcce00fdd44b33b8b019274b5a745",
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
      "reference_sha256": "da3f995d3b49d7eb37463d7c27707265e57fcce00fdd44b33b8b019274b5a745",
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
      "reference_sha256": "da3f995d3b49d7eb37463d7c27707265e57fcce00fdd44b33b8b019274b5a745",
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
    "y": 21.14225276438333,
    "w": 64.08200834694428,
    "h": 25.639061081025783,
    "text": "09:41",
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
    "id": "status_date",
    "x": 50.507872041943,
    "y": 49.86542534976338,
    "w": 110.79177672031103,
    "h": 22.140951400506374,
    "text": "10\u670822\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.87108480247093,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
