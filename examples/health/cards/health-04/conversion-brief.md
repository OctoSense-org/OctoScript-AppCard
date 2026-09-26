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
    "id": "package_card",
    "x": 38.11890838206628,
    "y": 146.72904483430798,
    "w": 329.76218323586744,
    "h": 461.364522417154,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "basic_package",
    "x": 56.27095516569201,
    "y": 220.84990253411306,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "basic_package_surface",
    "x": 56.27095516569201,
    "y": 220.84990253411306,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "basic_package_control",
    "x": 56.27095516569201,
    "y": 220.84990253411306,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "basic_checkbox",
    "x": 310.3996101364522,
    "y": 246.5653021442495,
    "w": 25.71539961013645,
    "h": 25.71539961013645,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "basic_name",
    "x": 124.30751688110493,
    "y": 236.90004070375454,
    "w": 78.4542483205218,
    "h": 25.58632609246931,
    "text": "\u57fa\u7840\u5957\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.07528326599646,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "basic_note",
    "x": 124.30751471818053,
    "y": 265.658370618549,
    "w": 53.30283413714125,
    "h": 22.52767729306173,
    "text": "\u5df2\u5305\u542b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.230739882547407,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "toggle_dental",
    "x": 56.27095516569201,
    "y": 305.5594541910331,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "toggle_dental_surface",
    "x": 56.27095516569201,
    "y": 305.5594541910331,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "toggle_dental_control",
    "x": 56.27095516569201,
    "y": 305.5594541910331,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dental_checkbox",
    "x": 310.3996101364522,
    "y": 329.76218323586744,
    "w": 25.71539961013645,
    "h": 25.71539961013645,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dental_name",
    "x": 124.2376173785199,
    "y": 319.33396795515057,
    "w": 78.59404732330493,
    "h": 26.06128988409308,
    "text": "\u7259\u79d1\u68c0\u67e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.516999592206563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dental_note",
    "x": 120.71445696502548,
    "y": 347.6793780526489,
    "w": 38.93059416356389,
    "h": 26.6761892506329,
    "text": "\u53ef\u9009",
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
    "id": "toggle_vision",
    "x": 56.27095516569201,
    "y": 390.26900584795317,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "toggle_vision_surface",
    "x": 56.27095516569201,
    "y": 390.26900584795317,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "toggle_vision_control",
    "x": 56.27095516569201,
    "y": 390.26900584795317,
    "w": 291.94541910331384,
    "h": 75.6335282651072,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "vision_checkbox",
    "x": 310.3996101364522,
    "y": 414.4717348927875,
    "w": 25.71539961013645,
    "h": 25.71539961013645,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "vision_name",
    "x": 117.12139730471225,
    "y": 402.10223226816424,
    "w": 85.64036830731064,
    "h": 29.699681150717065,
    "text": "\u89c6\u529b\u68c0\u67e5",
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
    "id": "vision_note",
    "x": 120.71445648595096,
    "y": 430.82540507821903,
    "w": 38.93059416356373,
    "h": 25.762109868228812,
    "text": "\u53ef\u9009",
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
    "id": "cancel_items",
    "x": 56.27095516569201,
    "y": 530.9473684210526,
    "w": 133.1150097465887,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_items_surface",
    "x": 56.27095516569201,
    "y": 530.9473684210526,
    "w": 133.1150097465887,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_items_control",
    "x": 56.27095516569201,
    "y": 530.9473684210526,
    "w": 133.1150097465887,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_items_text",
    "x": 99.15609988542026,
    "y": 549.6468790286162,
    "w": 46.116711265162415,
    "h": 25.770899273273713,
    "text": "\u53d6\u6d88",
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
    "id": "choose_time",
    "x": 199.9746588693957,
    "y": 530.9473684210526,
    "w": 151.2670565302144,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_time_surface",
    "x": 199.9746588693957,
    "y": 530.9473684210526,
    "w": 151.2670565302144,
    "h": 57.48148148148148,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "choose_time_control",
    "x": 199.9746588693957,
    "y": 530.9473684210526,
    "w": 151.2670565302144,
    "h": 57.48148148148148,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "choose_time_text",
    "x": 235.6216086655549,
    "y": 549.3855417565851,
    "w": 82.1888095788788,
    "h": 26.091420970903023,
    "text": "\u9009\u62e9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.54502150293981,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "clinic_icon_0",
    "x": 72.91033138401559,
    "y": 240.51461988304092,
    "w": 33.278752436647174,
    "h": 34.79142300194932,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clinic_icon_0.svg",
      "sha256": "aee44823e6d8dcb6ddb99ad40d85b6ffc23aa7f22f28e68b59ab5c7f4a36cce0",
      "method": "reference_svg",
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "tooth_icon_1",
    "x": 72.91033138401559,
    "y": 325.224171539961,
    "w": 36.304093567251456,
    "h": 37.8167641325536,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/tooth_icon_1.svg",
      "sha256": "4585014506330a6ea301edef04f3c13a0c40c18ec427045080dc322813cbe6ef",
      "method": "reference_svg",
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "eye_icon_2",
    "x": 72.91033138401559,
    "y": 412.95906432748535,
    "w": 36.304093567251456,
    "h": 30.253411306042885,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/eye_icon_2.svg",
      "sha256": "0a2f7902f63dbd5863da4b632ea5a8468395d0748fb1b4810cb73350c97b0959",
      "method": "reference_svg",
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "title",
    "x": 55.93773085872611,
    "y": 175.29769487474934,
    "w": 157.70486444246473,
    "h": 37.33491109128245,
    "text": "\u9009\u62e9\u4f53\u68c0\u9879\u76ee",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 31.00146731489268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "choice_note",
    "x": 55.99379064001051,
    "y": 481.1086530778823,
    "w": 114.47603757386088,
    "h": 26.04313006354906,
    "text": "\u7528\u6237\u81ea\u4e3b\u9009\u62e9",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.500110959100628,
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
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
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
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
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
      "reference_sha256": "d74dec3abdb1024365fd062360fc470eba7b34d4ae81b73f8d54bb38141459c3",
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
    "x": 52.44632843131588,
    "y": 21.142252404904188,
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
    "x": 48.85326922621795,
    "y": 49.86542534976338,
    "w": 107.19872249729669,
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
