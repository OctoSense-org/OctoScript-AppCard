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
    "id": "edit_card",
    "x": 38.11890838206628,
    "y": 90.76023391812865,
    "w": 331.27485380116957,
    "h": 550.6120857699805,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "current_summary",
    "x": 57.783625730994146,
    "y": 160.34307992202727,
    "w": 291.94541910331384,
    "h": 96.81091617933723,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "current_label",
    "x": 68.18930553132085,
    "y": 172.82076261087374,
    "w": 89.23342830070507,
    "h": 33.32962974434115,
    "text": "\u5f53\u524d\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.276555662237268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "current_day",
    "x": 71.78236537853343,
    "y": 216.52955703690535,
    "w": 128.75708245766322,
    "h": 25.56874728237923,
    "text": "\u5468\u516d 10\u670824\u65e5",
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
    "id": "current_time",
    "x": 197.53944846628747,
    "y": 219.68488746705543,
    "w": 135.9431909036915,
    "h": 22.41341719004686,
    "text": "14:00\u201315:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.12447798674358,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_day_surface",
    "x": 56.27095516569201,
    "y": 313.12280701754383,
    "w": 137.65302144249512,
    "h": 80.17153996101364,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "draft_weekday",
    "x": 107.71296008152731,
    "y": 323.9953577759373,
    "w": 38.930594163563754,
    "h": 29.699681150717065,
    "text": "\u5468\u65e5",
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
    "id": "draft_date",
    "x": 82.56154649698999,
    "y": 356.72641542608994,
    "w": 89.23342253032483,
    "h": 25.691796790439003,
    "text": "10\u670825\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.173371015108273,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "new_slot_surface",
    "x": 57.783625730994146,
    "y": 406.9083820662768,
    "w": 291.94541910331384,
    "h": 86.22222222222221,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "draft_radio",
    "x": 74.42300194931774,
    "y": 437.16179337231966,
    "w": 24.202729044834307,
    "h": 24.202729044834307,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "draft_time",
    "x": 114.89907614368545,
    "y": 425.0274491982527,
    "w": 128.75708245766327,
    "h": 22.395838379957333,
    "text": "10:00\u201311:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.108129693360322,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_availability",
    "x": 118.34102956351232,
    "y": 453.2201379062388,
    "w": 82.34952621013797,
    "h": 26.700029421521453,
    "text": "\u65e5\u5386\u7a7a\u95f2",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.11102736201495,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "keep_booking",
    "x": 57.783625730994146,
    "y": 564.2261208576998,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "keep_booking_surface",
    "x": 57.783625730994146,
    "y": 564.2261208576998,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "keep_booking_control",
    "x": 57.783625730994146,
    "y": 564.2261208576998,
    "w": 139.16569200779728,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "keep_booking_text",
    "x": 75.32664944757097,
    "y": 579.3661577585009,
    "w": 107.29627654612877,
    "h": 26.04337515480751,
    "text": "\u4fdd\u7559\u539f\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.500338893970987,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "select_new_time",
    "x": 207.53801169590642,
    "y": 564.2261208576998,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "select_new_time_surface",
    "x": 207.53801169590642,
    "y": 564.2261208576998,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "select_new_time_control",
    "x": 207.53801169590642,
    "y": 564.2261208576998,
    "w": 140.6783625730994,
    "h": 58.994152046783626,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "select_new_time_text",
    "x": 226.06426849334306,
    "y": 578.6639865501681,
    "w": 107.63803308795534,
    "h": 31.042510205378598,
    "text": "\u9009\u62e9\u65b0\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.149534491002097,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 53.75113970517789,
    "y": 115.65513839722786,
    "w": 110.92364145022385,
    "h": 36.793648672512155,
    "text": "\u4fee\u6539\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.498093265436307,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_label",
    "x": 53.81706903235347,
    "y": 274.04621645099564,
    "w": 67.67506834033868,
    "h": 32.78469816525936,
    "text": "\u65b0\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.7697692936912,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "draft_note",
    "x": 57.41012798514304,
    "y": 514.4753474690027,
    "w": 186.24603081121316,
    "h": 26.676189250632625,
    "text": "\u786e\u8ba4\u4fee\u6539\u524d\u4fdd\u7559\u539f\u9884\u7ea6",
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
      "reference_sha256": "2b3480bbf3b1badaa7d08aa3a1bcc86e80b79d59ece12f41d69288d947b752dd",
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
      "reference_sha256": "2b3480bbf3b1badaa7d08aa3a1bcc86e80b79d59ece12f41d69288d947b752dd",
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
      "reference_sha256": "2b3480bbf3b1badaa7d08aa3a1bcc86e80b79d59ece12f41d69288d947b752dd",
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
    "x": 50.15240534994738,
    "y": 22.150586881045236,
    "w": 67.81827763786093,
    "h": 22.4944421975478,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.199831243719455,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_date",
    "x": 50.22401020761511,
    "y": 47.34584906811421,
    "w": 107.19872249729686,
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
