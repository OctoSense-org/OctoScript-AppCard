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
    "x": 53.93785310734464,
    "y": 0.0,
    "w": 298.1242937853107,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_card",
    "x": 74.39736346516008,
    "y": 349.2730696798493,
    "w": 263.0508474576271,
    "h": 172.44444444444443,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_calendar",
    "x": 84.62711864406779,
    "y": 474.9529190207156,
    "w": 239.66854990583803,
    "h": 35.07344632768361,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_calendar_surface",
    "x": 84.62711864406779,
    "y": 474.9529190207156,
    "w": 239.66854990583803,
    "h": 35.07344632768361,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_calendar_control",
    "x": 84.62711864406779,
    "y": 474.9529190207156,
    "w": 239.66854990583803,
    "h": 35.07344632768361,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_73",
    "x": 168.92741755544648,
    "y": 482.7227767796604,
    "w": 72.7623165653464,
    "h": 18.905011164924097,
    "text": "\u67e5\u770b\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.165955710329825,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_1",
    "x": 89.01129943502825,
    "y": 362.4256120527307,
    "w": 33.612052730696796,
    "h": 33.612052730696796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "08bc4917f66eb289bdc70744d0b7439699ec1d11a5a0b7396ad8849bb1ffe0ce",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_69",
    "x": 141.00688354219733,
    "y": 368.87677761388227,
    "w": 109.59963592625752,
    "h": 18.402928337227493,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.570733337543237,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_70",
    "x": 143.27705691476152,
    "y": 401.11381074526065,
    "w": 94.91339809485102,
    "h": 20.18861785799634,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.407115976340155,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_71",
    "x": 139.44232422096746,
    "y": 428.3055330089394,
    "w": 164.55483074161805,
    "h": 17.680202584282725,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.76060205562526,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_72",
    "x": 143.33409842811886,
    "y": 450.626928776449,
    "w": 146.19632345145607,
    "h": 17.032257769314263,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 13.923352317643447,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "payment_card",
    "x": 74.39736346516008,
    "y": 530.4858757062146,
    "w": 263.0508474576271,
    "h": 153.4463276836158,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_payment",
    "x": 84.62711864406779,
    "y": 638.6290018832391,
    "w": 239.66854990583803,
    "h": 33.612052730696796,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_payment_surface",
    "x": 84.62711864406779,
    "y": 638.6290018832391,
    "w": 239.66854990583803,
    "h": 33.612052730696796,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_payment_control",
    "x": 84.62711864406779,
    "y": 638.6290018832391,
    "w": 239.66854990583803,
    "h": 33.612052730696796,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_77",
    "x": 168.8613527061474,
    "y": 645.9704994388826,
    "w": 76.47992584652086,
    "h": 20.061212043964925,
    "text": "\u67e5\u770b\u8d39\u7528",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.363472479962084,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_2",
    "x": 87.54990583804144,
    "y": 545.0998116760828,
    "w": 33.612052730696796,
    "h": 29.227871939736346,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_2.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "08bc4917f66eb289bdc70744d0b7439699ec1d11a5a0b7396ad8849bb1ffe0ce",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_74",
    "x": 143.2795931270878,
    "y": 551.3137833596927,
    "w": 105.80761855036886,
    "h": 17.55422303440738,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.66378258320308,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_75",
    "x": 143.02355610235765,
    "y": 581.7334948797611,
    "w": 94.92719717123943,
    "h": 19.696807968949955,
    "text": "\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.06174779233691,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_76",
    "x": 143.15948779066218,
    "y": 607.7849023078174,
    "w": 61.74721219124925,
    "h": 22.916602325582257,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.92305971749968,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_badge",
    "x": 74.39736346516008,
    "y": 214.82485875706215,
    "w": 151.98493408662898,
    "h": 29.227871939736346,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "teacher_avatar",
    "x": 74.39736346516008,
    "y": 137.37099811676083,
    "w": 46.76459510357815,
    "h": 48.22598870056497,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_inbox",
    "x": 68.55178907721282,
    "y": 45.303201506591336,
    "w": 90.60640301318267,
    "h": 32.15065913370998,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_inbox_surface",
    "x": 68.55178907721282,
    "y": 45.303201506591336,
    "w": 90.60640301318267,
    "h": 32.15065913370998,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_inbox_control",
    "x": 68.55178907721282,
    "y": 45.303201506591336,
    "w": 90.60640301318267,
    "h": 32.15065913370998,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_60",
    "x": 92.25538783529292,
    "y": 50.003691148775886,
    "w": 62.91713747645951,
    "h": 21.288286252354048,
    "text": "\u6536\u4ef6\u7bb1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.690039191734108,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "show_desktop",
    "x": 72.93596986817326,
    "y": 701.4689265536723,
    "w": 264.5122410546139,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "show_desktop_surface",
    "x": 72.93596986817326,
    "y": 701.4689265536723,
    "w": 264.5122410546139,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "show_desktop_control",
    "x": 72.93596986817326,
    "y": 701.4689265536723,
    "w": 264.5122410546139,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_78",
    "x": 165.29120737620437,
    "y": 718.01806100261,
    "w": 76.43401245474428,
    "h": 19.711463129852262,
    "text": "\u8fd4\u56de\u684c\u9762",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.07767731505681,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 68.55178907721282,
    "y": 51.1487758945386,
    "w": 13.152542372881355,
    "h": 20.459510357815443,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "171f79537a16c28893fe9bd1e9c89f62c10cb6903e9823ae2f7dc718e2f12752",
      "method": "reference_svg",
      "reference_sha256": "08bc4917f66eb289bdc70744d0b7439699ec1d11a5a0b7396ad8849bb1ffe0ce",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "check_icon_3",
    "x": 87.54990583804144,
    "y": 220.6704331450094,
    "w": 17.536723163841806,
    "h": 17.536723163841806,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_3.svg",
      "sha256": "66dac3d5cf777af8f0a9d888b632fd35bdb1c74921628c119909111b32e8352c",
      "method": "reference_svg",
      "reference_sha256": "08bc4917f66eb289bdc70744d0b7439699ec1d11a5a0b7396ad8849bb1ffe0ce",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "status_icon_99",
    "x": 265.8399246704331,
    "y": 8.768361581920903,
    "w": 71.60828625235405,
    "h": 18.998116760828623,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/status_icon_99.svg",
      "sha256": "3b6423e66479afccf6047b9070879d78bab3316da88a148ca834359918ba963e",
      "method": "reference_svg",
      "reference_sha256": "08bc4917f66eb289bdc70744d0b7439699ec1d11a5a0b7396ad8849bb1ffe0ce",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_61",
    "x": 69.72305051818941,
    "y": 92.26088017943843,
    "w": 186.5850394898124,
    "h": 26.40346343478417,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.089745628800188,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_62",
    "x": 132.29446136528887,
    "y": 139.9096178985415,
    "w": 58.07551073321684,
    "h": 19.796237610773943,
    "text": "\u6797\u8001\u5e08",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.169823489971677,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_63",
    "x": 128.44157750333034,
    "y": 165.0788672895783,
    "w": 109.47932000840119,
    "h": 17.39692342915513,
    "text": "9\u670824\u65e5 09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.43424358197596,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_64",
    "x": 131.9240474760546,
    "y": 185.53818680263586,
    "w": 94.79251974490617,
    "h": 17.11046842593785,
    "text": "\u6536\u4ef6\u4eba\uff1aAlex",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.23503629309213,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_65",
    "x": 112.3933773726643,
    "y": 220.17001934894986,
    "w": 121.3728813559322,
    "h": 18.537550755960886,
    "text": "\u5df2\u6388\u6743\u540c\u6b65\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.716271087525284,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_66",
    "x": 73.46190682968228,
    "y": 260.296819107045,
    "w": 263.1280602636535,
    "h": 18.660599074045606,
    "text": "\u5bb6\u957f\u60a8\u597d\uff0c\u79cb\u5b63\u79d1\u5b66\u65e5\u5c06\u4e8e9\u670825\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.335354679964023,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_67",
    "x": 72.76674268251575,
    "y": 285.2880602636535,
    "w": 261.66666666666663,
    "h": 21.288286252354048,
    "text": "14:00\u201316:00 \u5728\u79d1\u5b66\u6559\u5ba4\u4e3e\u884c",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.529781620958254,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_68",
    "x": 73.708282821123,
    "y": 313.90550778216067,
    "w": 261.66666666666663,
    "h": 19.58634790083873,
    "text": "\u6d3b\u52a8\u6750\u6599\u8d39\u4e3a \u00a5120\uff0c\u8bf7\u786e\u8ba4\u7f34\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.406682000882878,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "teacher_initial",
    "x": 86.93579473892548,
    "y": 150.48420478126835,
    "w": 25.176244797101972,
    "h": 23.46096896853671,
    "text": "\u6797",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.176244797101972,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
