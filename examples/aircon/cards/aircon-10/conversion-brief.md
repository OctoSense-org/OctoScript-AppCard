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
    "y": 0.0,
    "w": 405.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_arriving",
    "x": 16.344529750479847,
    "y": 99.62688064192578,
    "w": 372.03262955854126,
    "h": 491.1293881644935,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "technician_portrait",
    "x": 37.5,
    "y": 236.0,
    "w": 124.0,
    "h": 136.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/technician_portrait.png",
      "sha256": "f1a4dc8a0925358c62a41fe1d60db59a20440f55eba47466e16bfda96873290a",
      "method": "source_crop",
      "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
      "crop_pixels": [
        75,
        472,
        248,
        272
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Artwork-only source region; product photography or technician portrait, visually reviewed"
    }
  },
  {
    "id": "divider_0",
    "x": 79.3877159309021,
    "y": 410.96088264794383,
    "w": 105.85028790786947,
    "h": 2.3350050150451356,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "divider_1",
    "x": 203.1391554702495,
    "y": 410.96088264794383,
    "w": 110.52015355086371,
    "h": 2.3350050150451356,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "contact_technician",
    "x": 38.13723608445297,
    "y": 519.9277833500502,
    "w": 150.21401151631477,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "contact_technician_surface",
    "x": 38.13723608445297,
    "y": 519.9277833500502,
    "w": 150.21401151631477,
    "h": 49.035105315947845,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "contact_technician_control",
    "x": 38.13723608445297,
    "y": 519.9277833500502,
    "w": 150.21401151631477,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_95",
    "x": 71.223812162081,
    "y": 531.4650414590957,
    "w": 85.61775502591121,
    "h": 29.471866955847947,
    "text": "\u8054\u7cfb\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.68883626893859,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "view_booking",
    "x": 214.8138195777351,
    "y": 519.1494483450351,
    "w": 146.32245681381957,
    "h": 49.81344032096289,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_booking_surface",
    "x": 214.8138195777351,
    "y": 519.1494483450351,
    "w": 146.32245681381957,
    "h": 49.81344032096289,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_booking_control",
    "x": 214.8138195777351,
    "y": 519.1494483450351,
    "w": 146.32245681381957,
    "h": 49.81344032096289,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_96",
    "x": 247.2631859176959,
    "y": 532.168859083875,
    "w": 81.33653418162037,
    "h": 28.06423154350741,
    "text": "\u67e5\u770b\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.379735335461895,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_0",
    "x": 39.69385796545105,
    "y": 118.30692076228686,
    "w": 30.35412667946257,
    "h": 31.133400200601805,
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
      "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "step_0",
    "x": 61.48656429942418,
    "y": 403.1775325977934,
    "w": 16.344529750479847,
    "h": 17.90170511534604,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_1",
    "x": 183.6813819577735,
    "y": 401.6208625877633,
    "w": 20.236084452975046,
    "h": 21.01504513540622,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_2",
    "x": 312.8809980806142,
    "y": 402.39919759277836,
    "w": 17.901151631477926,
    "h": 19.45837512537613,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_86",
    "x": 83.22392009560919,
    "y": 121.94518454013745,
    "w": 202.29968926545067,
    "h": 27.603461668268935,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u5e08\u5085\u5728\u8def\u4e0a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.95121935149011,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_87",
    "x": 32.42202509022825,
    "y": 172.7722710614994,
    "w": 229.65455882242676,
    "h": 39.187981516571064,
    "text": "\u7ea620\u5206\u949f\u540e\u5230\u8fbe",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.72482281041109,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_88",
    "x": 184.82768251532013,
    "y": 258.40722153115604,
    "w": 65.52539492294108,
    "h": 28.12838515546649,
    "text": "\u738b\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.439398194583838,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_89",
    "x": 184.82767989413446,
    "y": 297.885096969836,
    "w": 155.40565940285833,
    "h": 23.67558499779118,
    "text": "\u4eca\u5929 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.2982940479458,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_90",
    "x": 180.91984482795507,
    "y": 333.0730796584969,
    "w": 135.86646346899454,
    "h": 27.45865434438101,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.81654854027434,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_91",
    "x": 36.32986427245561,
    "y": 434.72725171086284,
    "w": 77.24890535760983,
    "h": 27.712066604476483,
    "text": "\u9884\u7ea6\u6210\u529f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.05222194216313,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_93",
    "x": 161.32523077437105,
    "y": 434.56014189572323,
    "w": 73.45192583783346,
    "h": 27.79287396797322,
    "text": "\u6b63\u5728\u524d\u5f80",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.127372790215098,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_94",
    "x": 286.4314553799452,
    "y": 434.7272516717646,
    "w": 77.24890535760971,
    "h": 27.712066604476483,
    "text": "\u5b89\u88c5\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.05222194216313,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 6.226487523992322,
    "y": 656.9147442326981,
    "w": 389.15547024952014,
    "h": 118.30692076228686,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 29.96497120921305,
    "y": 665.6632296890672,
    "w": 71.6046065259117,
    "h": 71.60682046138416,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 41.63963531669865,
    "y": 680.4515947843531,
    "w": 48.2552783109405,
    "h": 45.92176529588767,
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
      "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 121.41650671785028,
    "y": 665.6632296890672,
    "w": 71.6046065259117,
    "h": 71.60682046138416,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 212.86804222648746,
    "y": 665.6632296890672,
    "w": 71.6046065259117,
    "h": 71.60682046138416,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 224.54270633397306,
    "y": 680.4515947843531,
    "w": 48.2552783109405,
    "h": 45.92176529588767,
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
      "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 304.3195777351247,
    "y": 665.6632296890672,
    "w": 71.6046065259117,
    "h": 71.60682046138416,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 315.9942418426103,
    "y": 680.4515947843531,
    "w": 48.2552783109405,
    "h": 45.92176529588767,
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
      "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_84",
    "x": 20.698513249590196,
    "y": 20.23670994267461,
    "w": 108.511605788101,
    "h": 23.60318096470809,
    "text": "9\u670819\u65e5 \u5468\u516d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.230958297178525,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_85",
    "x": 24.60634985372708,
    "y": 51.37010982478326,
    "w": 85.06458491876349,
    "h": 31.567539241871145,
    "text": "13:40",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.637811494940166,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_97",
    "x": 32.422025847938144,
    "y": 739.4182546033289,
    "w": 42.07837108458309,
    "h": 23.820390837123185,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.432963478524563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_98",
    "x": 122.30228285197175,
    "y": 688.8264797378284,
    "w": 42.07837405360357,
    "h": 35.31440768533652,
    "text": "19",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.122399147362962,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_99",
    "x": 126.2101210794014,
    "y": 739.4182549454342,
    "w": 38.17053427302684,
    "h": 23.820390837123185,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.432963478524563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_100",
    "x": 227.81389236235097,
    "y": 739.4182546766368,
    "w": 34.26269746147049,
    "h": 23.820391579401146,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.432964168843068,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_101",
    "x": 321.6019887040103,
    "y": 739.4182546522011,
    "w": 42.07837405360357,
    "h": 23.820390837123185,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.432963478524563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
