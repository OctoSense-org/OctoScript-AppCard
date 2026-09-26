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
    "x": 2.5,
    "y": 0.0,
    "w": 400.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "payment_due",
    "x": 16.498058252427185,
    "y": 97.97194388777555,
    "w": 356.95048543689325,
    "h": 356.8977955911824,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 39.050485436893204,
    "y": 265.14629258517033,
    "w": 311.06796116504853,
    "h": 0.7775551102204409,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "source_service_order",
    "x": 35.93980582524272,
    "y": 350.67735470941886,
    "w": 98.76407766990292,
    "h": 26.43687374749499,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "source_service_order_surface",
    "x": 35.93980582524272,
    "y": 350.67735470941886,
    "w": 98.76407766990292,
    "h": 26.43687374749499,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "source_service_order_control",
    "x": 35.93980582524272,
    "y": 350.67735470941886,
    "w": 98.76407766990292,
    "h": 26.43687374749499,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_146",
    "x": 37.495147101194576,
    "y": 352.2324650622216,
    "w": 92.80623077096284,
    "h": 27.471314049913605,
    "text": "\u5b89\u88c5\u670d\u52a1\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.828322066419656,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "pay_materials",
    "x": 35.1621359223301,
    "y": 390.3326653306613,
    "w": 168.75436893203883,
    "h": 45.875751503006015,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_materials_surface",
    "x": 35.1621359223301,
    "y": 390.3326653306613,
    "w": 168.75436893203883,
    "h": 45.875751503006015,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_materials_control",
    "x": 35.1621359223301,
    "y": 390.3326653306613,
    "w": 168.75436893203883,
    "h": 45.875751503006015,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_148",
    "x": 68.7320974982273,
    "y": 402.7735467436905,
    "w": 96.71084898420902,
    "h": 27.70638933353767,
    "text": "\u652f\u4ed8 \u00a5130",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.046942080190032,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "withdraw_payment_request",
    "x": 224.1359223300971,
    "y": 389.5551102204409,
    "w": 131.426213592233,
    "h": 45.875751503006015,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "withdraw_payment_request_surface",
    "x": 224.1359223300971,
    "y": 389.5551102204409,
    "w": 131.426213592233,
    "h": 45.875751503006015,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "withdraw_payment_request_control",
    "x": 224.1359223300971,
    "y": 389.5551102204409,
    "w": 131.426213592233,
    "h": 45.875751503006015,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_149",
    "x": 263.9630342500376,
    "y": 402.7735467436905,
    "w": 45.95080627885843,
    "h": 27.70638933353767,
    "text": "\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.046942080190032,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_0",
    "x": 39.828155339805825,
    "y": 115.85571142284569,
    "w": 34.21747572815534,
    "h": 31.879759519038075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_0.svg",
      "sha256": "ad9266d4ebef2712804598eee5535322f54c6c4d15b3ba967f5616e33a3bb72d",
      "method": "reference_svg",
      "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_141",
    "x": 84.30512925935938,
    "y": 121.58630125676562,
    "w": 124.13406047635877,
    "h": 27.908536043339186,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.234938520305445,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_142",
    "x": 33.590528548753355,
    "y": 168.69329336198803,
    "w": 178.7078433286796,
    "h": 35.246865893652426,
    "text": "\u7a7a\u8c03\u5b89\u88c5\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.059585281096762,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_143",
    "x": 33.59053027309028,
    "y": 215.38276557719905,
    "w": 116.23394005043983,
    "h": 43.239407740040726,
    "text": "\u00a5130",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 36.49264919823788,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_144",
    "x": 37.32828478279406,
    "y": 277.25347416187293,
    "w": 112.6630496867651,
    "h": 29.042848514411393,
    "text": "\u52a0\u957f\u94dc\u7ba1 2\u7c73",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.289849118402596,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_145",
    "x": 33.590524781227245,
    "y": 321.0217649342458,
    "w": 186.51707975517195,
    "h": 27.435148678705275,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5b89\u88c5\u670d\u52a1\u56e2\u961f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.794688271195906,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_147",
    "x": 299.1046024593449,
    "y": 281.96318285937406,
    "w": 53.76004270535079,
    "h": 23.72819998364639,
    "text": "\u00a5130",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.347225984791145,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "installation_complete",
    "x": 16.498058252427185,
    "y": 468.86573146292585,
    "w": 356.95048543689325,
    "h": 171.06212424849699,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "report_installation_issue",
    "x": 103.59708737864078,
    "y": 571.503006012024,
    "w": 177.30873786407767,
    "h": 45.098196392785574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "report_installation_issue_surface",
    "x": 103.59708737864078,
    "y": 571.503006012024,
    "w": 177.30873786407767,
    "h": 45.098196392785574,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "report_installation_issue_control",
    "x": 103.59708737864078,
    "y": 571.503006012024,
    "w": 177.30873786407767,
    "h": 45.098196392785574,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_152",
    "x": 146.69101318006963,
    "y": 586.0444335292209,
    "w": 85.26390898621209,
    "h": 24.6806711797007,
    "text": "\u53cd\u9988\u95ee\u9898",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.23302419712165,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_1",
    "x": 36.71747572815534,
    "y": 489.85971943887773,
    "w": 29.55145631067961,
    "h": 31.879759519038075,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_1.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_150",
    "x": 84.35056706634181,
    "y": 496.7853845351406,
    "w": 202.13556447445765,
    "h": 23.52929155429994,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u5b89\u88c5\u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.162241145498946,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_151",
    "x": 33.590524485115665,
    "y": 535.7354707119287,
    "w": 135.75704298297183,
    "h": 23.63778766792612,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.26314253117129,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 12.609708737864079,
    "y": 658.5891783567134,
    "w": 378.7252427184466,
    "h": 115.85571142284569,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 35.570412621359225,
    "y": 667.0489779559118,
    "w": 69.96851650485436,
    "h": 69.9581883767535,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 47.23546116504854,
    "y": 681.8225250501002,
    "w": 46.638419417475724,
    "h": 44.29886973947895,
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
      "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 124.57084466019418,
    "y": 667.0489779559118,
    "w": 69.96851650485436,
    "h": 69.9581883767535,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 213.5712766990291,
    "y": 667.0489779559118,
    "w": 69.96851650485436,
    "h": 69.9581883767535,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.23632524271844,
    "y": 681.8225250501002,
    "w": 46.638419417475724,
    "h": 44.29886973947895,
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
      "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 302.57170873786407,
    "y": 667.0489779559118,
    "w": 69.96851650485436,
    "h": 69.9581883767535,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 314.23675728155337,
    "y": 681.8225250501002,
    "w": 46.638419417475724,
    "h": 44.29886973947895,
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
      "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_139",
    "x": 25.781289250655263,
    "y": 24.10420832187359,
    "w": 104.52008541070148,
    "h": 23.601621555183296,
    "text": "9\u670819\u65e5 \u5468\u516d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.229508046320465,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_140",
    "x": 21.876669808950837,
    "y": 55.20641233114492,
    "w": 88.90161255771676,
    "h": 31.55799951343136,
    "text": "16:10",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.628939547491164,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_153",
    "x": 123.39675810189755,
    "y": 692.0240480160163,
    "w": 42.04618806561225,
    "h": 35.30111357969827,
    "text": "19",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.110035629119395,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_154",
    "x": 37.49514752928884,
    "y": 738.6773545486162,
    "w": 42.046185099036926,
    "h": 23.800530726063943,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.41449357523947,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_155",
    "x": 127.30137641739049,
    "y": 738.6773546218506,
    "w": 38.14156985236607,
    "h": 23.800531467598137,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.414494264866267,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_157",
    "x": 224.91684667865735,
    "y": 738.6773549392015,
    "w": 42.046185099036926,
    "h": 23.800530726063943,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.41449357523947,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_158",
    "x": 322.5323143626825,
    "y": 738.6773546354129,
    "w": 38.14156985236607,
    "h": 23.800531467598137,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.414494264866267,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
