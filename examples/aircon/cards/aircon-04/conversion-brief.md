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
    "y": 42.0,
    "w": 406.0,
    "h": 692.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "logistics_card",
    "x": 17.846153846153847,
    "y": 187.28176795580112,
    "w": 364.57142857142856,
    "h": 384.23204419889504,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 67.56043956043956,
    "y": 358.05156537753226,
    "w": 251.75824175824175,
    "h": 1.9116022099447516,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "courier",
    "x": 38.879120879120876,
    "y": 503.33333333333337,
    "w": 138.94505494505495,
    "h": 43.32965009208103,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "courier_surface",
    "x": 38.879120879120876,
    "y": 503.33333333333337,
    "w": 138.94505494505495,
    "h": 43.32965009208103,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "courier_control",
    "x": 38.879120879120876,
    "y": 503.33333333333337,
    "w": 138.94505494505495,
    "h": 43.32965009208103,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_169",
    "x": 64.68615513692295,
    "y": 514.4442418608744,
    "w": 89.50961706140542,
    "h": 23.685245099427668,
    "text": "\u8054\u7cfb\u914d\u9001\u5458",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.30727794246773,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "delivery_time",
    "x": 210.96703296703296,
    "y": 503.33333333333337,
    "w": 130.65934065934064,
    "h": 43.32965009208103,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "delivery_time_surface",
    "x": 210.96703296703296,
    "y": 503.33333333333337,
    "w": 130.65934065934064,
    "h": 43.32965009208103,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "delivery_time_control",
    "x": 210.96703296703296,
    "y": 503.33333333333337,
    "w": 130.65934065934064,
    "h": 43.32965009208103,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_170",
    "x": 240.74706934001378,
    "y": 514.6843977733517,
    "w": 70.20309012276778,
    "h": 23.234571130236183,
    "text": "\u4fee\u6539\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.88815115111965,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "truck_icon_0",
    "x": 36.967032967032964,
    "y": 212.1325966850829,
    "w": 36.967032967032964,
    "h": 26.762430939226522,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/truck_icon_0.svg",
      "sha256": "fe8dbdcd8a05c9c057c5e4b60db01df603fb870e182257e44814e162c0665eca",
      "method": "reference_svg",
      "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "home_icon_1",
    "x": 37.6043956043956,
    "y": 428.78084714548805,
    "w": 19.758241758241756,
    "h": 19.753222836095766,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/home_icon_1.svg",
      "sha256": "35f5c9ea4be301e43dab353017cb4b03c55ecca63d0fc1663c199edceda6095e",
      "method": "reference_svg",
      "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "step_0",
    "x": 59.912087912087905,
    "y": 351.6795580110497,
    "w": 14.659340659340659,
    "h": 14.655616942909761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_1",
    "x": 182.9230769230769,
    "y": 350.4051565377532,
    "w": 18.483516483516482,
    "h": 18.478821362799266,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_2",
    "x": 312.30769230769226,
    "y": 351.6795580110497,
    "w": 14.659340659340659,
    "h": 14.655616942909761,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_162",
    "x": 87.10397050127496,
    "y": 216.80804065657705,
    "w": 108.67692515614264,
    "h": 23.604698676430637,
    "text": "\u7269\u6d41 \u00b7 \u914d\u9001\u4e2d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.232369769080492,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_163",
    "x": 39.13780704497709,
    "y": 265.02025822539974,
    "w": 214.20970069969096,
    "h": 29.606578496718626,
    "text": "\u5468\u4e94 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.814118001948323,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_164",
    "x": 39.13779747057246,
    "y": 300.06629846159217,
    "w": 140.60632693112552,
    "h": 26.568760494281374,
    "text": "\u7a7a\u8c03\u6b63\u5728\u9001\u5f80\u4f60\u5bb6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.98894725968168,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_165",
    "x": 45.538095431237096,
    "y": 380.2498610857986,
    "w": 51.00220514653794,
    "h": 20.033748514305366,
    "text": "\u5df2\u53d1\u8d27",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.91138611830399,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_166",
    "x": 167.14368649289503,
    "y": 380.2498610857986,
    "w": 51.00220514653811,
    "h": 20.033748514305366,
    "text": "\u914d\u9001\u4e2d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.91138611830399,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_167",
    "x": 68.19780219780219,
    "y": 428.1436464088398,
    "w": 127.92307692307692,
    "h": 23.116022099447516,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.77790055248619,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_168",
    "x": 35.91274379171097,
    "y": 460.14528529406016,
    "w": 99.05423342526628,
    "h": 23.455199187192644,
    "text": "\u6765\u81ea\u8d2d\u7269\u8ba2\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.09333524408916,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_212",
    "x": 295.1495718209559,
    "y": 380.2498610857986,
    "w": 51.00220514653811,
    "h": 20.033748514305366,
    "text": "\u5df2\u9001\u8fbe",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.91138611830399,
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
    "y": 633.3222836095765,
    "w": 406.0,
    "h": 100.67771639042358,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 25.988461538461536,
    "y": 640.9432044198895,
    "w": 72.25907692307692,
    "h": 72.24072191528546,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 35.5489010989011,
    "y": 653.0500184162063,
    "w": 53.1381978021978,
    "h": 51.21309760589319,
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
      "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 121.39846153846153,
    "y": 640.9432044198895,
    "w": 72.25907692307692,
    "h": 72.24072191528546,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 216.8084615384615,
    "y": 640.9432044198895,
    "w": 72.25907692307692,
    "h": 72.24072191528546,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 226.36890109890106,
    "y": 653.0500184162063,
    "w": 53.1381978021978,
    "h": 51.21309760589319,
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
      "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 312.2184615384615,
    "y": 640.9432044198895,
    "w": 72.25907692307692,
    "h": 72.24072191528546,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 321.77890109890103,
    "y": 653.0500184162063,
    "w": 53.1381978021978,
    "h": 51.21309760589319,
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
      "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_160",
    "x": 19.93691842753186,
    "y": 66.56927477342165,
    "w": 95.80426360748623,
    "h": 20.211572668170266,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.076762581398349,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_161",
    "x": 16.619827992733956,
    "y": 98.25955022749369,
    "w": 89.63785594898262,
    "h": 36.64411916434213,
    "text": "14:20",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.359030822838182,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_171",
    "x": 42.33794605895452,
    "y": 703.4143643873492,
    "w": 35.00147171858906,
    "h": 23.32348290332795,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.970839100094995,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_172",
    "x": 128.7419189754104,
    "y": 665.1230462466767,
    "w": 35.00147171858906,
    "h": 29.60657849671887,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.81411800194855,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_173",
    "x": 131.94206578859732,
    "y": 703.4143643873492,
    "w": 35.00147171858906,
    "h": 23.32348290332795,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.970839100094995,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_174",
    "x": 224.74633363528227,
    "y": 703.414364706957,
    "w": 38.2016184041787,
    "h": 23.323482295645846,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.970838534950637,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_213",
    "x": 320.7507466474873,
    "y": 703.4143643873492,
    "w": 35.00147171858906,
    "h": 23.32348290332795,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.970839100094995,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
