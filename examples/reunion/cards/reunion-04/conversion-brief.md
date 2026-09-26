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
    "y": 7.0,
    "w": 406.0,
    "h": 762.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "poll_card",
    "x": 23.390946502057613,
    "y": 187.4736842105263,
    "w": 360.88888888888886,
    "h": 436.14473684210526,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "friday",
    "x": 41.76954732510288,
    "y": 254.31578947368422,
    "w": 324.13168724279836,
    "h": 75.19736842105263,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "friday_surface",
    "x": 41.76954732510288,
    "y": 254.31578947368422,
    "w": 324.13168724279836,
    "h": 75.19736842105263,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "friday_control",
    "x": 41.76954732510288,
    "y": 254.31578947368422,
    "w": 324.13168724279836,
    "h": 75.19736842105263,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_155",
    "x": 114.5254603751409,
    "y": 270.8177118713715,
    "w": 172.0219350094033,
    "h": 26.350050659310277,
    "text": "\u5468\u4e94 10\u670823\u65e518:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.11504559337925,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_156",
    "x": 114.49410089808674,
    "y": 296.6600760094658,
    "w": 117.29488506535797,
    "h": 26.258795723188737,
    "text": "\u4e0e\u5de5\u4f5c\u4f8b\u4f1a\u51b2\u7a81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.032916150869863,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "saturday",
    "x": 41.76954732510288,
    "y": 342.88157894736844,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "saturday_surface",
    "x": 41.76954732510288,
    "y": 342.88157894736844,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_control",
    "x": 41.76954732510288,
    "y": 342.88157894736844,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_157",
    "x": 114.52546537977894,
    "y": 358.9654608489095,
    "w": 179.32722822620246,
    "h": 26.06849095941311,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.8616418634718,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_158",
    "x": 114.52545824658499,
    "y": 387.71372372528236,
    "w": 73.4003619688011,
    "h": 22.77229577827044,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.895066200443395,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunday",
    "x": 41.76954732510288,
    "y": 436.4605263157895,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sunday_surface",
    "x": 41.76954732510288,
    "y": 436.4605263157895,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_control",
    "x": 41.76954732510288,
    "y": 436.4605263157895,
    "w": 324.13168724279836,
    "h": 78.53947368421052,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_159",
    "x": 114.52546464924868,
    "y": 454.0065792090384,
    "w": 179.32722822620266,
    "h": 26.21412539677941,
    "text": "\u5468\u65e510\u670825\u65e5 12:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.99271285710147,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_160",
    "x": 114.52545824658499,
    "y": 479.5605912818556,
    "w": 73.4003619688011,
    "h": 25.966546614369012,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.76989195293211,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirm_attendance",
    "x": 41.76954732510288,
    "y": 545.078947368421,
    "w": 158.72427983539094,
    "h": 56.81578947368421,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_attendance_surface",
    "x": 41.76954732510288,
    "y": 545.078947368421,
    "w": 158.72427983539094,
    "h": 56.81578947368421,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_attendance_control",
    "x": 41.76954732510288,
    "y": 545.078947368421,
    "w": 158.72427983539094,
    "h": 56.81578947368421,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_161",
    "x": 81.65160157485874,
    "y": 563.0577427094969,
    "w": 88.01096750470174,
    "h": 34.05897462780483,
    "text": "\u786e\u8ba4\u53c2\u52a0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.053077165024344,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_poll",
    "x": 210.5185185185185,
    "y": 545.078947368421,
    "w": 155.3827160493827,
    "h": 56.81578947368421,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_poll_surface",
    "x": 210.5185185185185,
    "y": 545.078947368421,
    "w": 155.3827160493827,
    "h": 56.81578947368421,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_poll_control",
    "x": 210.5185185185185,
    "y": 545.078947368421,
    "w": 155.3827160493827,
    "h": 56.81578947368421,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_162",
    "x": 267.9367925789658,
    "y": 563.0577422059106,
    "w": 47.83180705655076,
    "h": 30.7190893543394,
    "text": "\u8fd4\u56de",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.04718041890546,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 45.11111111111111,
    "y": 207.52631578947367,
    "w": 26.732510288065843,
    "h": 30.07894736842105,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "warning_icon_1",
    "x": 60.148148148148145,
    "y": 271.0263157894737,
    "w": 33.415637860082306,
    "h": 33.421052631578945,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/warning_icon_1.svg",
      "sha256": "e4e325bc63825064c2781b8d5753db0ed0753e089a0a191e8333359242b87136",
      "method": "reference_svg",
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 61.818930041152264,
    "y": 364.60526315789474,
    "w": 30.074074074074073,
    "h": 31.75,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 61.818930041152264,
    "y": 458.1842105263158,
    "w": 30.074074074074073,
    "h": 31.75,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "friday_dot",
    "x": 329.14403292181066,
    "y": 281.05263157894734,
    "w": 23.390946502057613,
    "h": 23.394736842105264,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "saturday_dot",
    "x": 327.4732510288066,
    "y": 369.61842105263156,
    "w": 25.061728395061728,
    "h": 25.06578947368421,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunday_dot",
    "x": 327.4732510288066,
    "y": 463.1973684210526,
    "w": 25.061728395061728,
    "h": 25.06578947368421,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_154",
    "x": 88.81646743177811,
    "y": 208.3289394278068,
    "w": 139.42895120510684,
    "h": 31.115969493669766,
    "text": "\u805a\u4f1a \u00b7 \u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.40437254430279,
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
    "y": 665.3947368421052,
    "w": 406.0,
    "h": 103.60526315789474,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.415637860082306,
    "y": 680.4342105263157,
    "w": 36.757201646090536,
    "h": 38.43421052631579,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.10562414266116,
    "y": 680.4342105263157,
    "w": 36.757201646090536,
    "h": 38.43421052631579,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.79561042524003,
    "y": 680.4342105263157,
    "w": 36.757201646090536,
    "h": 38.43421052631579,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.4855967078189,
    "y": 680.4342105263157,
    "w": 36.757201646090536,
    "h": 38.43421052631579,
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
      "reference_sha256": "8db6656d0e2ae602b90eb09f8a0d8389e9a853294be5899240c39a22f64e0cf0",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_150",
    "x": 34.16713962035302,
    "y": 21.996199129730204,
    "w": 47.83181024026768,
    "h": 19.29162946042006,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 13.762466514378056,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_152",
    "x": 136.36255199158222,
    "y": 69.99153966050807,
    "w": 157.56895529921525,
    "h": 66.53254530989253,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 56.279290778903274,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_153",
    "x": 136.4413643356773,
    "y": 138.89221192599823,
    "w": 161.06397608190247,
    "h": 27.37920248829242,
    "text": "10\u670821\u65e5 \u661f\u671f\u4e09",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.04128223946318,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_163",
    "x": 34.167140213136975,
    "y": 731.7219890705788,
    "w": 40.52650747231736,
    "h": 22.374227572930586,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.536804815637527,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_164",
    "x": 132.7887123023505,
    "y": 731.721989344736,
    "w": 36.87385449648375,
    "h": 22.374227572930586,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.536804815637527,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_165",
    "x": 231.41028324183904,
    "y": 728.163651394688,
    "w": 40.52650747231717,
    "h": 25.93256490059105,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.739308410531944,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_166",
    "x": 330.03185479914566,
    "y": 731.721989136345,
    "w": 44.17915726443387,
    "h": 26.029655056362333,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.8266895507261,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
