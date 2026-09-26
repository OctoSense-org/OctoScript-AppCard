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
    "y": 2.0,
    "w": 406.0,
    "h": 771.5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "inbox_list",
    "x": 10.15,
    "y": 159.3453947368421,
    "w": 382.31666666666666,
    "h": 338.3771929824561,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "selected_chat",
    "x": 10.15,
    "y": 169.49671052631578,
    "w": 385.7,
    "h": 106.58881578947368,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "group_avatar",
    "x": 22.0,
    "y": 188.0,
    "w": 71.0,
    "h": 73.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/group_avatar.png",
      "sha256": "7367d1e9ce52b99fea4a91bac83c0d12af0661a2ca2f831230a26f26c7a92cfd",
      "method": "source_crop",
      "reference_sha256": "98182f50a8ae453063c23ed64a5d4365a01baaf307cca883c52898e6d383becb",
      "crop_pixels": [
        44,
        376,
        142,
        146
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "teacher_avatar",
    "x": 22.0,
    "y": 294.5,
    "w": 71.0,
    "h": 74.5,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/teacher_avatar.png",
      "sha256": "8554135ca20e3619c3264f2f4d7bf7a5d23c99975eb8ab6882a57e37efd15279",
      "method": "source_crop",
      "reference_sha256": "98182f50a8ae453063c23ed64a5d4365a01baaf307cca883c52898e6d383becb",
      "crop_pixels": [
        44,
        589,
        142,
        149
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "family_avatar",
    "x": 22.0,
    "y": 403.0,
    "w": 71.0,
    "h": 71.0,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/family_avatar.png",
      "sha256": "f71de02dd5eb002957b9296c2d0a23601f329454c9c2089e2b230f705b9ca420",
      "method": "source_crop",
      "reference_sha256": "98182f50a8ae453063c23ed64a5d4365a01baaf307cca883c52898e6d383becb",
      "crop_pixels": [
        44,
        806,
        142,
        142
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork"
    }
  },
  {
    "id": "text_5",
    "x": 108.40776594961288,
    "y": 194.9532676454123,
    "w": 141.04362355409117,
    "h": 31.019382628226317,
    "text": "2016\u5c4a\u540c\u5b66\u7fa4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.317444365403688,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_6",
    "x": 112.20917956365432,
    "y": 228.52847684937552,
    "w": 233.2951358293104,
    "h": 30.196989066200363,
    "text": "\u738b\u5b81\uff1a\u597d\u4e45\u4e0d\u89c1\uff0c\u4e00\u8d77\u805a\u805a\u5427",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.577290159580325,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_7",
    "x": 319.3144707430535,
    "y": 199.2104580212856,
    "w": 52.07801578278904,
    "h": 23.17344331206843,
    "text": "09:24",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.256098980861587,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_8",
    "x": 108.510862454797,
    "y": 302.8384741060415,
    "w": 74.2678664934111,
    "h": 33.608003186011764,
    "text": "\u6797\u8001\u5e08",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.647202867410588,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_9",
    "x": 112.2091703747873,
    "y": 336.14747833510773,
    "w": 59.47463483533866,
    "h": 26.56971330974018,
    "text": "\u660e\u5929\u89c1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.312741978766162,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_10",
    "x": 326.71108762636396,
    "y": 306.30355304685577,
    "w": 40.98308881572128,
    "h": 26.441923661896016,
    "text": "\u6628\u5929",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.197731295706415,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_11",
    "x": 108.51086095481728,
    "y": 413.8684903683598,
    "w": 52.07801578278904,
    "h": 33.60800318601205,
    "text": "\u5bb6\u4eba",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.647202867410844,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_12",
    "x": 112.05482600354648,
    "y": 446.37850129344116,
    "w": 115.25795331405487,
    "h": 27.803990147748145,
    "text": "\u5468\u672b\u4e00\u8d77\u5403\u996d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.423591132973332,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "search_field",
    "x": 21.991666666666667,
    "y": 103.51315789473684,
    "w": 365.4,
    "h": 49.06469298245614,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_invite",
    "x": 20.3,
    "y": 668.6030701754386,
    "w": 367.09166666666664,
    "h": 62.59978070175438,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_invite_surface",
    "x": 20.3,
    "y": 668.6030701754386,
    "w": 367.09166666666664,
    "h": 62.59978070175438,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_invite_control",
    "x": 20.3,
    "y": 668.6030701754386,
    "w": 367.09166666666664,
    "h": 62.59978070175438,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_13",
    "x": 152.69289280775763,
    "y": 687.0613534041656,
    "w": 104.24969372831384,
    "h": 34.970357491833866,
    "text": "\u67e5\u770b\u9080\u8bf7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.873321742650482,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "search_icon_0",
    "x": 33.833333333333336,
    "y": 117.04824561403508,
    "w": 20.3,
    "h": 20.302631578947366,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/search_icon_0.svg",
      "sha256": "b27d8e715fcb2ed5f947ea42296c9ed09037e40a1b0cb9924e569767c6ed540e",
      "method": "reference_svg",
      "reference_sha256": "98182f50a8ae453063c23ed64a5d4365a01baaf307cca883c52898e6d383becb",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_1",
    "x": 38.24299247072778,
    "y": 17.183159569198395,
    "w": 40.9830888157213,
    "h": 23.183273533047096,
    "text": "9:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.264946179742388,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_2",
    "x": 19.751448005138265,
    "y": 54.379935519138456,
    "w": 55.77632369730714,
    "h": 37.81525069313387,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.433725623820482,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "search_label",
    "x": 67.66666666666667,
    "y": 113.66447368421052,
    "w": 207.0,
    "h": 31.07017543859649,
    "text": "\u641c\u7d22",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.36315789473684,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
