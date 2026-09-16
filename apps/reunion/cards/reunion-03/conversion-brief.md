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
    "id": "poll_card",
    "x": 23.295081967213115,
    "y": 196.58552631578948,
    "w": 359.40983606557376,
    "h": 391.1513157894737,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "choose_time",
    "x": 48.25409836065574,
    "y": 436.26973684210526,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_time_surface",
    "x": 48.25409836065574,
    "y": 436.26973684210526,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "choose_time_control",
    "x": 48.25409836065574,
    "y": 436.26973684210526,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_106",
    "x": 162.4389908856765,
    "y": 453.74671089810903,
    "w": 91.30433700608043,
    "h": 33.12828829317323,
    "text": "\u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.215459463855904,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "view_invite",
    "x": 48.25409836065574,
    "y": 504.5131578947368,
    "w": 309.4918032786885,
    "h": 56.5921052631579,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_invite_surface",
    "x": 48.25409836065574,
    "y": 504.5131578947368,
    "w": 309.4918032786885,
    "h": 56.5921052631579,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_invite_control",
    "x": 48.25409836065574,
    "y": 504.5131578947368,
    "w": 309.4918032786885,
    "h": 56.5921052631579,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_107",
    "x": 166.07667006150578,
    "y": 522.4476957603431,
    "w": 80.39129408765322,
    "h": 26.32491911059611,
    "text": "\u67e5\u770b\u9080\u8bf7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.0924271995365,
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
    "y": 218.22368421052633,
    "w": 38.27049180327869,
    "h": 38.2828947368421,
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
      "reference_sha256": "7d1f29f0044924d301bea42cc93f40831bcd1bb0bf6c55e39b75236c0b63e59a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_102",
    "x": 104.23609509863724,
    "y": 228.0024675134668,
    "w": 149.50723468480504,
    "h": 33.12828829317323,
    "text": "\u805a\u4f1a \u00b7 \u65f6\u95f4\u6295\u7968",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.215459463855904,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_103",
    "x": 49.67088214481328,
    "y": 286.2493748394984,
    "w": 276.8260666193441,
    "h": 40.59410603201227,
    "text": "\u5341\u5e74\u540c\u7a97 \u518d\u805a\u4e00\u5802",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.93469542881105,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_104",
    "x": 49.670881261662934,
    "y": 332.82369218208,
    "w": 204.07244293560368,
    "h": 33.940632208010044,
    "text": "\u738b\u5b81\u9080\u8bf7\u4f60\u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.946568987209037,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_105",
    "x": 53.308561997050646,
    "y": 387.71485134557736,
    "w": 174.97100360824803,
    "h": 26.33942434546871,
    "text": "3\u4e2a\u65f6\u6bb5 \u00b7 18\u4f4d\u540c\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.10548191092184,
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
    "y": 664.3026315789474,
    "w": 406.0,
    "h": 103.19736842105263,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.278688524590166,
    "y": 679.2828947368421,
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
      "reference_sha256": "7d1f29f0044924d301bea42cc93f40831bcd1bb0bf6c55e39b75236c0b63e59a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.11475409836066,
    "y": 679.2828947368421,
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
      "reference_sha256": "7d1f29f0044924d301bea42cc93f40831bcd1bb0bf6c55e39b75236c0b63e59a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.95081967213113,
    "y": 679.2828947368421,
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
      "reference_sha256": "7d1f29f0044924d301bea42cc93f40831bcd1bb0bf6c55e39b75236c0b63e59a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.78688524590166,
    "y": 679.2828947368421,
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
      "reference_sha256": "7d1f29f0044924d301bea42cc93f40831bcd1bb0bf6c55e39b75236c0b63e59a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_99",
    "x": 136.8319189427584,
    "y": 71.0597449844253,
    "w": 157.0692039630005,
    "h": 63.01291100502397,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 53.111619904521575,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_100",
    "x": 136.97522776897847,
    "y": 136.54621457102547,
    "w": 160.42027126189467,
    "h": 30.61389450285301,
    "text": "10\u670821\u65e5 \u661f\u671f\u4e09",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.95250505256771,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_108",
    "x": 35.120156377014574,
    "y": 730.3687528476228,
    "w": 40.37680867120131,
    "h": 22.301888094297002,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.471699284867302,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_109",
    "x": 133.33753985994554,
    "y": 730.3687528703792,
    "w": 36.73912875528181,
    "h": 22.301888094297002,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.471699284867302,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_110",
    "x": 231.55492492897946,
    "y": 730.3687528931357,
    "w": 40.37680867120112,
    "h": 22.301888094297002,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.471699284867302,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_146",
    "x": 333.4099899366681,
    "y": 730.3687528830218,
    "w": 36.73912875528181,
    "h": 22.301888094297002,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.471699284867302,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
