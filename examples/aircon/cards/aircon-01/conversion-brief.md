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
    "x": 19.5,
    "y": 0.0,
    "w": 366.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "product_photo",
    "x": 19.5,
    "y": 91.0,
    "w": 366.5,
    "h": 303.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/product_photo.png",
      "sha256": "34e6c30fb0dc826e373a2b685b906e089d23514e035fb6fdb9d466a8d93b730e",
      "method": "source_crop",
      "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
      "crop_pixels": [
        39,
        182,
        733,
        606
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Artwork-only source region; product photography or technician portrait, visually reviewed"
    }
  },
  {
    "id": "divider_0",
    "x": 32.384765625,
    "y": 569.830258302583,
    "w": 337.8671875,
    "h": 0.7158671586715867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "buy",
    "x": 36.6796875,
    "y": 700.8339483394834,
    "w": 331.4248046875,
    "h": 50.82656826568265,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "buy_surface",
    "x": 36.6796875,
    "y": 700.8339483394834,
    "w": 331.4248046875,
    "h": 50.82656826568265,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "buy_control",
    "x": 36.6796875,
    "y": 700.8339483394834,
    "w": 331.4248046875,
    "h": 50.82656826568265,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_9",
    "x": 152.50846283125455,
    "y": 714.0634659397556,
    "w": 89.47216634452342,
    "h": 29.915802156793387,
    "text": "\u7acb\u5373\u8d2d\u4e70",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.10169600581785,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 35.9638671875,
    "y": 50.11070110701107,
    "w": 22.90625,
    "h": 28.634686346863468,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "23c0f034fd6afc76d67644ec247b6d57b64452b91b3c7ff09c207f41e6661ace",
      "method": "reference_svg",
      "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "share_icon_1",
    "x": 340.9033203125,
    "y": 50.82656826568265,
    "w": 25.76953125,
    "h": 25.055350553505534,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/share_icon_1.svg",
      "sha256": "e6189ac8c3d7183502d5a247262139654cfcef01c4f6f251ec154e72b2642e89",
      "method": "reference_svg",
      "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "truck_icon_2",
    "x": 37.3955078125,
    "y": 597.0332103321033,
    "w": 27.9169921875,
    "h": 24.339483394833948,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/truck_icon_2.svg",
      "sha256": "fe8dbdcd8a05c9c057c5e4b60db01df603fb870e182257e44814e162c0665eca",
      "method": "reference_svg",
      "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 37.3955078125,
    "y": 645.7121771217712,
    "w": 27.201171875,
    "h": 26.487084870848708,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "ae776c61fe98dc0aee57fc63b1343360e4030e6cc97db9fa23eca69d129b3b1d",
      "method": "reference_svg",
      "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_1",
    "x": 37.605163522332816,
    "y": 12.885609054652727,
    "w": 150.3571534305811,
    "h": 22.612546125461233,
    "text": "9\u670817\u65e5 \u5468\u56db 09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.309667896678945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_2",
    "x": 177.77416056466694,
    "y": 52.774392468855595,
    "w": 46.12892202287914,
    "h": 32.834463323614244,
    "text": "\u597d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.81605089096125,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_4",
    "x": 37.605162002228205,
    "y": 415.9188187664583,
    "w": 175.5156880915165,
    "h": 36.41379911697228,
    "text": "1.5\u5339\u53d8\u9891\u7a7a\u8c03",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.14483317878422,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_5",
    "x": 37.495043425185116,
    "y": 462.40447150447307,
    "w": 114.63662102818489,
    "h": 44.17998589096916,
    "text": "\u00a52,799",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 37.367386878601316,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_6",
    "x": 44.793316400011676,
    "y": 520.2522960435473,
    "w": 294.1202195584774,
    "h": 25.659143314150597,
    "text": "\u4e00\u7ea7\u80fd\u6548 \u00b7 \u51b7\u6696\u4e24\u7528 \u00b7 \u5b89\u9759\u7761\u7720",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.143003282160056,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_7",
    "x": 77.4814453125,
    "y": 595.6014760147601,
    "w": 178.3759765625,
    "h": 25.4760147601476,
    "text": "\u9001\u8d27\u4e0a\u95e8 \u00b7 \u4e13\u4e1a\u5b89\u88c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.97269372693727,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_8",
    "x": 77.14001039698863,
    "y": 649.7077154235473,
    "w": 150.35714250802994,
    "h": 22.196343749211813,
    "text": "\u5468\u4e94 9\u670818\u65e5\u9001\u8fbe",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.922599686766986,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
