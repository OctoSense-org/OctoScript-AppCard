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
    "y": 8.5,
    "w": 406.0,
    "h": 759.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "payment_card",
    "x": 23.295081967213115,
    "y": 61.76315789473684,
    "w": 359.40983606557376,
    "h": 437.75657894736844,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "reopen_payment",
    "x": 48.25409836065574,
    "y": 417.9605263157895,
    "w": 309.4918032786885,
    "h": 58.256578947368425,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reopen_payment_surface",
    "x": 48.25409836065574,
    "y": 417.9605263157895,
    "w": 309.4918032786885,
    "h": 58.256578947368425,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reopen_payment_control",
    "x": 48.25409836065574,
    "y": 417.9605263157895,
    "w": 309.4918032786885,
    "h": 58.256578947368425,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_91",
    "x": 141.54765018738635,
    "y": 434.95761904373245,
    "w": 127.99774648095254,
    "h": 34.504169466152916,
    "text": "\u91cd\u65b0\u6253\u5f00\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.453752519537627,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "warning_icon_0",
    "x": 48.25409836065574,
    "y": 85.0657894736842,
    "w": 44.92622950819672,
    "h": 46.60526315789474,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/warning_icon_0.svg",
      "sha256": "e4e325bc63825064c2781b8d5753db0ed0753e089a0a191e8333359242b87136",
      "method": "reference_svg",
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_85",
    "x": 108.96682183451001,
    "y": 93.38815822915892,
    "w": 127.68114884795062,
    "h": 29.487252256526645,
    "text": "\u652f\u4ed8 \u00b7 \u5df2\u53d6\u6d88",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.93852703087398,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_86",
    "x": 43.48856366204132,
    "y": 148.00370122195423,
    "w": 160.42027126189453,
    "h": 26.363601323234594,
    "text": "2016\u5c4a\u540c\u5b66\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.127241190911136,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_87",
    "x": 46.99867223130757,
    "y": 187.70688668200705,
    "w": 142.4870185809603,
    "h": 55.67093028122837,
    "text": "\u00a5180",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 46.50383725310554,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_88",
    "x": 46.851795284637696,
    "y": 259.3355549469565,
    "w": 139.14309162847397,
    "h": 32.56778723576819,
    "text": "\u6536\u6b3e\u4eba \u738b\u5b81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.711008512191377,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_89",
    "x": 47.126243920256904,
    "y": 311.753621520919,
    "w": 149.50723468480504,
    "h": 29.58396096074636,
    "text": "\u672c\u6b21\u652f\u4ed8\u5df2\u53d6\u6d88",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.025564864671725,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_90",
    "x": 47.1262413700348,
    "y": 340.9786185127385,
    "w": 171.33332052165966,
    "h": 29.666162050625736,
    "text": "\u805a\u4f1a\u62a5\u540d\u4e0d\u53d7\u5f71\u54cd",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.099545845563163,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "rsvp_summary",
    "x": 23.295081967213115,
    "y": 514.5,
    "w": 359.40983606557376,
    "h": 106.52631578947368,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_reunion",
    "x": 23.295081967213115,
    "y": 514.5,
    "w": 359.40983606557376,
    "h": 106.52631578947368,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_reunion_surface",
    "x": 23.295081967213115,
    "y": 514.5,
    "w": 359.40983606557376,
    "h": 106.52631578947368,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_reunion_control",
    "x": 23.295081967213115,
    "y": 514.5,
    "w": 359.40983606557376,
    "h": 106.52631578947368,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "group_icon_1",
    "x": 46.59016393442623,
    "y": 537.8026315789474,
    "w": 41.59836065573771,
    "h": 41.61184210526316,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/group_icon_1.svg",
      "sha256": "a863d3bd8d66ea77c53543b8771a29cc3c5e135065d65081e155ae50be06d57e",
      "method": "reference_svg",
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_92",
    "x": 108.96682049338851,
    "y": 544.6252052172846,
    "w": 145.86955159821676,
    "h": 26.097656947276796,
    "text": "\u805a\u4f1a\u62a5\u540d\u4ecd\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.887891252549117,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_93",
    "x": 108.9668236652085,
    "y": 577.6459706553763,
    "w": 185.88404018533745,
    "h": 25.870393990801574,
    "text": "\u4f60\u5df2\u786e\u8ba4\u53c2\u52a0\u672c\u6b21\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.683354591721418,
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
    "y": 657.6447368421053,
    "w": 406.0,
    "h": 109.85526315789474,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.278688524590166,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.11475409836066,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.95081967213113,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.78688524590166,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "de5449fe63be0236bffe4f6b2b8fa7ce0b3af2a445403820fdfae2e5f4d33ff4",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_84",
    "x": 32.57552001213269,
    "y": 20.567434289114154,
    "w": 51.28985158962852,
    "h": 25.84621621988006,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.661594597892055,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_94",
    "x": 32.57551919557714,
    "y": 722.6056302509481,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_95",
    "x": 130.79290391111275,
    "y": 722.6056297654761,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_96",
    "x": 229.01028853570602,
    "y": 722.6056303116322,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_97",
    "x": 330.8653543254963,
    "y": 722.6056299839385,
    "w": 36.739128755281904,
    "h": 27.287158384008087,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.95844254560728,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
