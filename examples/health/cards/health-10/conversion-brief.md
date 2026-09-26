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
    "id": "review_card",
    "x": 38.11890838206628,
    "y": 131.60233918128654,
    "w": 331.27485380116957,
    "h": 484.05458089668616,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "old_time_surface",
    "x": 56.27095516569201,
    "y": 211.7738791423002,
    "w": 293.45808966861597,
    "h": 98.32358674463937,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "old_label",
    "x": 70.12776659462551,
    "y": 245.2878869343183,
    "w": 64.08200834694428,
    "h": 25.56874728237923,
    "text": "\u539f\u65f6\u95f4",
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
    "id": "current_day",
    "x": 167.14037347490603,
    "y": 230.26710913157925,
    "w": 132.3501366806774,
    "h": 26.676189250632625,
    "text": "\u5468\u516d 10\u670824\u65e5",
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
    "id": "current_time",
    "x": 163.54731433205745,
    "y": 263.26184314266794,
    "w": 132.3501366806774,
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
    "id": "new_time_surface",
    "x": 56.27095516569201,
    "y": 356.990253411306,
    "w": 293.45808966861597,
    "h": 98.32358674463937,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "new_label",
    "x": 66.53470664025008,
    "y": 389.0004336656552,
    "w": 67.67506834033863,
    "h": 32.83743315381583,
    "text": "\u65b0\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.818812833048725,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_day",
    "x": 167.0135155095703,
    "y": 377.6283300146347,
    "w": 132.60384876035573,
    "h": 30.497205222555593,
    "text": "\u5468\u65e5 10\u670825\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.642400856976703,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_time",
    "x": 163.54731039299747,
    "y": 410.1648766840233,
    "w": 128.75708245766327,
    "h": 26.676189250632625,
    "text": "10:00\u201311:00",
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
    "id": "discard_changes",
    "x": 57.783625730994146,
    "y": 532.4600389863548,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "discard_changes_surface",
    "x": 57.783625730994146,
    "y": 532.4600389863548,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "discard_changes_control",
    "x": 57.783625730994146,
    "y": 532.4600389863548,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "discard_changes_text",
    "x": 88.09306263476631,
    "y": 550.7572507225067,
    "w": 82.0473083139163,
    "h": 29.699681150717065,
    "text": "\u653e\u5f03\u4fee\u6539",
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
    "id": "confirm_changes",
    "x": 207.53801169590642,
    "y": 532.4600389863548,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_changes_surface",
    "x": 207.53801169590642,
    "y": 532.4600389863548,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "confirm_changes_control",
    "x": 207.53801169590642,
    "y": 532.4600389863548,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "confirm_changes_text",
    "x": 231.8154406846889,
    "y": 550.7572508566199,
    "w": 89.23342830070507,
    "h": 32.84622183800427,
    "text": "\u786e\u8ba4\u4fee\u6539",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.82698630934397,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "arrow_down_icon_0",
    "x": 192.41130604288497,
    "y": 319.1734892787524,
    "w": 25.71539961013645,
    "h": 25.71539961013645,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/arrow_down_icon_0.svg",
      "sha256": "270cb748167b7f60734ca4641858aa8ca6aca2c6b6acd5bb6ff942cc59864483",
      "method": "reference_svg",
      "reference_sha256": "81c78db057c65b13466f14f108eb165900e3f618f477529df1a48bc32fbcce25",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "title",
    "x": 55.75552923205875,
    "y": 166.20247948847665,
    "w": 110.79177672031098,
    "h": 33.294472124161544,
    "text": "\u786e\u8ba4\u4fee\u6539",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.243859075470233,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "change_note",
    "x": 55.75552688904298,
    "y": 475.1699534893151,
    "w": 236.5488707187348,
    "h": 29.699681150717065,
    "text": "\u540c\u4e00\u9884\u7ea6\u4e0e\u65e5\u5386\u5c06\u540c\u6b65\u66f4\u65b0",
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
      "reference_sha256": "81c78db057c65b13466f14f108eb165900e3f618f477529df1a48bc32fbcce25",
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
      "reference_sha256": "81c78db057c65b13466f14f108eb165900e3f618f477529df1a48bc32fbcce25",
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
      "reference_sha256": "81c78db057c65b13466f14f108eb165900e3f618f477529df1a48bc32fbcce25",
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
    "x": 52.162468320328074,
    "y": 22.410829943536097,
    "w": 64.08200834694428,
    "h": 21.973956308935033,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.715779367309583,
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
    "y": 47.345849169633695,
    "w": 103.60566827428275,
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
