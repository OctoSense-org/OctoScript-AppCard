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
    "id": "invitation",
    "x": 14.975409836065573,
    "y": 414.63157894736844,
    "w": 376.04918032786884,
    "h": 236.35526315789474,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_icon_1",
    "x": 34.94262295081967,
    "y": 437.9342105263158,
    "w": 33.278688524590166,
    "h": 33.28947368421053,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 38.27049180327869,
    "y": 511.17105263157896,
    "w": 21.631147540983605,
    "h": 23.30263157894737,
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
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 38.27049180327869,
    "y": 559.4407894736842,
    "w": 21.631147540983605,
    "h": 23.30263157894737,
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
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "calendar_icon_4",
    "x": 38.27049180327869,
    "y": 611.0394736842105,
    "w": 21.631147540983605,
    "h": 23.30263157894737,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_4.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_61",
    "x": 83.50305083549007,
    "y": 431.9004941195782,
    "w": 189.52172327192585,
    "h": 29.675832207207197,
    "text": "\u5341\u5e74\u540c\u7a97 \u518d\u805a\u4e00\u5802",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.108248986486476,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_62",
    "x": 83.50305974512011,
    "y": 460.903063127572,
    "w": 134.95650233845166,
    "h": 25.971936187000612,
    "text": "2016\u5c4a\u540c\u5b66\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.77474256830055,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_63",
    "x": 83.50305833128736,
    "y": 512.0032897343241,
    "w": 182.24635709874906,
    "h": 26.08798520438324,
    "text": "\u5468\u4e9410\u670823\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.879186683944916,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_64",
    "x": 83.50305804676411,
    "y": 559.0418021714187,
    "w": 185.88404018533745,
    "h": 26.14117423820615,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.927056814385537,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_65",
    "x": 83.50305804676411,
    "y": 610.3112666473241,
    "w": 185.88404018533745,
    "h": 25.918747153177705,
    "text": "\u5468\u65e5 10\u670825\u65e5 12:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.726872437859935,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "invitation_message",
    "x": 83.19672131147541,
    "y": 146.6513157894737,
    "w": 307.827868852459,
    "h": 48.26973684210526,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "organizer_avatar",
    "x": 11.5,
    "y": 116.5,
    "w": 63.0,
    "h": 63.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/organizer_avatar.png",
      "sha256": "53612e957295f0a7813e85a1705342cf42a1e4e4bae15beaab272b58012b8307",
      "method": "source_crop",
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "crop_pixels": [
        23,
        233,
        126,
        126
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "venue_photo",
    "x": 73.0,
    "y": 205.0,
    "w": 313.0,
    "h": 201.5,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/venue_photo.png",
      "sha256": "baf62e354e3b10ef79e55891051c1dc0fa82b630b122726501e06a23c971219e",
      "method": "source_crop",
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "crop_pixels": [
        146,
        410,
        626,
        403
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "back_messages",
    "x": 11.647540983606557,
    "y": 56.76973684210526,
    "w": 36.60655737704918,
    "h": 36.61842105263158,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_messages_surface",
    "x": 11.647540983606557,
    "y": 56.76973684210526,
    "w": 36.60655737704918,
    "h": 36.61842105263158,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_messages_control",
    "x": 11.647540983606557,
    "y": 56.76973684210526,
    "w": 36.60655737704918,
    "h": 36.61842105263158,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_poll",
    "x": 16.639344262295083,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_poll_surface",
    "x": 16.639344262295083,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_poll_control",
    "x": 16.639344262295083,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_66",
    "x": 72.59000850001264,
    "y": 683.1319909038862,
    "w": 69.47825751056371,
    "h": 33.12828829317323,
    "text": "\u53bb\u6295\u7968",
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
    "id": "group_info",
    "x": 209.65573770491804,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "group_info_surface",
    "x": 209.65573770491804,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "group_info_control",
    "x": 209.65573770491804,
    "y": 664.3026315789474,
    "w": 179.70491803278688,
    "h": 59.921052631578945,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_67",
    "x": 265.38709796945056,
    "y": 683.1319908778789,
    "w": 65.84057442397531,
    "h": 33.12828829317295,
    "text": "\u7fa4\u8d44\u6599",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.215459463855655,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 14.975409836065573,
    "y": 61.76315789473684,
    "w": 23.295081967213115,
    "h": 23.30263157894737,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "50ab5c7ac439e2ec3cf9c8fa99d327a907fa39d2910cd0a648214845de3efe4e",
      "method": "reference_svg",
      "reference_sha256": "cc7ba1dddc2fec80795f6233cec20d3494968ca1b68c584f63ddf1afb66faaa1",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_54",
    "x": 32.57552025656739,
    "y": 23.43715897360336,
    "w": 40.37680867120131,
    "h": 22.872462231474444,
    "text": "9:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.985216008327,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_56",
    "x": 123.331717949809,
    "y": 59.37733550564095,
    "w": 153.5165708995227,
    "h": 31.762188318599513,
    "text": "2016\u5c4a\u540c\u5b66\u7fa4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.985969486739563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_57",
    "x": 87.14073392005595,
    "y": 118.24916086478582,
    "w": 40.37680867120131,
    "h": 26.368437194681373,
    "text": "\u738b\u5b81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.131593475213236,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_58",
    "x": 345.41607736695323,
    "y": 122.41241799760176,
    "w": 47.65217167370911,
    "h": 18.564144146586614,
    "text": "09:24",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 13.107729731927952,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_59",
    "x": 98.05378548416469,
    "y": 162.46381623216533,
    "w": 262.27533427299056,
    "h": 26.32008323914933,
    "text": "\u597d\u4e45\u4e0d\u89c1\uff0c\u627e\u4e2a\u5468\u672b\u4e00\u8d77\u5403\u996d\u5427",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.088074915234397,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
