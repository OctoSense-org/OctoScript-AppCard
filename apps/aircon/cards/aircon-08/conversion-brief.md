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
    "y": 62.0,
    "w": 406.0,
    "h": 651.5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_booking",
    "x": 17.818181818181817,
    "y": 156.162109375,
    "w": 364.0,
    "h": 229.04296875,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "reschedule",
    "x": 37.54545454545455,
    "y": 326.671875,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reschedule_surface",
    "x": 37.54545454545455,
    "y": 326.671875,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reschedule_control",
    "x": 37.54545454545455,
    "y": 326.671875,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_182",
    "x": 82.52225269972304,
    "y": 338.6418857245792,
    "w": 41.341574235396,
    "h": 20.024129627738148,
    "text": "\u6539\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.90244055379648,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_booking",
    "x": 211.9090909090909,
    "y": 326.671875,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_booking_surface",
    "x": 211.9090909090909,
    "y": 326.671875,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_booking_control",
    "x": 211.9090909090909,
    "y": 326.671875,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_183",
    "x": 239.08368351756573,
    "y": 335.4459376197396,
    "w": 76.48801768909794,
    "h": 26.401230076327874,
    "text": "\u53d6\u6d88\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.833143970984924,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_0",
    "x": 38.81818181818182,
    "y": 174.61279296875,
    "w": 28.0,
    "h": 29.2666015625,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_0.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "check_icon_1",
    "x": 336.6363636363636,
    "y": 179.06640625,
    "w": 20.363636363636363,
    "h": 20.99560546875,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_1.svg",
      "sha256": "b454e45f1990ad3cdde19b68869cee12f252d1d1aea44d03fed3e590ce7ea897",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_178",
    "x": 78.9090909090909,
    "y": 180.3388671875,
    "w": 163.36363636363637,
    "h": 24.99560546875,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u9884\u7ea6\u6210\u529f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.5259130859375,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_179",
    "x": 37.790415604954475,
    "y": 223.58774322338053,
    "w": 54.122097362171445,
    "h": 23.175689842552117,
    "text": "\u738b\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.83339155357347,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_180",
    "x": 37.79042260544026,
    "y": 255.41406230880477,
    "w": 207.48838944868592,
    "h": 23.30885472614293,
    "text": "\u5468\u516d 9\u670819\u65e5 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.957234895312926,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_181",
    "x": 34.595284649944624,
    "y": 287.2255860972975,
    "w": 118.0247178511185,
    "h": 20.541992187499982,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.384052734374984,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_updated",
    "x": 17.818181818181817,
    "y": 396.02099609375,
    "w": 364.0,
    "h": 215.68212890625,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "acknowledge_calendar",
    "x": 35.63636363636363,
    "y": 555.07861328125,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "acknowledge_calendar_surface",
    "x": 35.63636363636363,
    "y": 555.07861328125,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "acknowledge_calendar_control",
    "x": 35.63636363636363,
    "y": 555.07861328125,
    "w": 134.9090909090909,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_188",
    "x": 79.32712019306655,
    "y": 565.2583005286629,
    "w": 41.34157423539584,
    "h": 23.72314453125007,
    "text": "\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.342524414062567,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "undo_calendar",
    "x": 211.9090909090909,
    "y": 555.07861328125,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "undo_calendar_surface",
    "x": 211.9090909090909,
    "y": 555.07861328125,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "undo_calendar_control",
    "x": 211.9090909090909,
    "y": 555.07861328125,
    "w": 133.0,
    "h": 40.08251953125,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_189",
    "x": 238.86905690095392,
    "y": 564.775013065034,
    "w": 70.52700736305934,
    "h": 24.734107911586616,
    "text": "\u64a4\u9500\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.282720357775553,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_2",
    "x": 36.90909090909091,
    "y": 410.654296875,
    "w": 28.0,
    "h": 29.90283203125,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "ae776c61fe98dc0aee57fc63b1343360e4030e6cc97db9fa23eca69d129b3b1d",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_184",
    "x": 76.00588115188775,
    "y": 417.8672912782607,
    "w": 102.30128479003919,
    "h": 24.522298870608182,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.08573794966561,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_185",
    "x": 28.160791156566575,
    "y": 456.747734592026,
    "w": 86.16186939586298,
    "h": 29.856069718487625,
    "text": "\u7a7a\u8c03\u5b89\u88c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.04614483819349,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_186",
    "x": 31.40015560867819,
    "y": 488.8514604240139,
    "w": 162.75655850497165,
    "h": 23.175689842552117,
    "text": "9\u670819\u65e5 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.83339155357347,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_187",
    "x": 31.400149881524488,
    "y": 517.5410156995626,
    "w": 111.63446599786924,
    "h": 20.053722363431053,
    "text": "\u5df2\u52a0\u5165\u5bb6\u5ead\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.92996179799088,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 8.272727272727273,
    "y": 623.1552734375,
    "w": 371.6363636363636,
    "h": 89.70849609375,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 31.690909090909088,
    "y": 629.4666796875,
    "w": 66.88436363636363,
    "h": 66.8703671875,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 41.236363636363635,
    "y": 641.55505859375,
    "w": 47.793454545454544,
    "h": 45.87476171875,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_mail.svg",
      "sha256": "9b7cff617690a90aac7b12cb3fef04594954830e1bc22fcd9518a5cf98ca1e93",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 119.02545454545454,
    "y": 629.4666796875,
    "w": 66.88436363636363,
    "h": 66.8703671875,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 206.35999999999999,
    "y": 629.4666796875,
    "w": 66.88436363636363,
    "h": 66.8703671875,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 215.90545454545452,
    "y": 641.55505859375,
    "w": 47.793454545454544,
    "h": 45.87476171875,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_bag.svg",
      "sha256": "2f675e8ba88bad04e7dcdce9b85424e2d8458a97463597bfa7b814452887fb40",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 293.6945454545454,
    "y": 629.4666796875,
    "w": 66.88436363636363,
    "h": 66.8703671875,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 303.23999999999995,
    "y": 641.55505859375,
    "w": 47.793454545454544,
    "h": 45.87476171875,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "ad9266d4ebef2712804598eee5535322f54c6c4d15b3ba967f5616e33a3bb72d",
      "method": "reference_svg",
      "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_176",
    "x": 18.598182861079625,
    "y": 79.66604667657376,
    "w": 95.70169206099072,
    "h": 23.38372667739158,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.02686580997417,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_177",
    "x": 18.61962829027915,
    "y": 111.62597708001232,
    "w": 79.683148470792,
    "h": 32.86710691172645,
    "text": "15:28",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.8464094279056,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_190",
    "x": 37.790415094575685,
    "y": 686.7783205005187,
    "w": 34.951310244473525,
    "h": 20.201682401355356,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.067564633260481,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_191",
    "x": 124.05895821649905,
    "y": 651.7856443382818,
    "w": 31.756179462779624,
    "h": 23.234874707180897,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.888433477678234,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_192",
    "x": 124.05895798503037,
    "y": 686.7783202208731,
    "w": 34.9513126720082,
    "h": 20.201682401355356,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.067564633260481,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_193",
    "x": 213.52263162423307,
    "y": 686.7783203985675,
    "w": 38.146443453702105,
    "h": 23.397631112951775,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.03979693504515,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_214",
    "x": 309.37657059096205,
    "y": 686.7783205791978,
    "w": 34.951310244473525,
    "h": 23.397630506195238,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.03979637076157,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
