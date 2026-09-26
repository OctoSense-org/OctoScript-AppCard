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
    "id": "heading",
    "x": 23.541436353663418,
    "y": 27.536332179930795,
    "w": 245.75819520882618,
    "h": 36.22145328719723,
    "text": "Evening forecast",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 33.27762800412503,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 24.433396022937938,
    "y": 71.84083044982698,
    "w": 152.16538037486217,
    "h": 18.320645905420992,
    "text": "Monday, September 7",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 14.865019165890619,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 24.395974408960676,
    "y": 118.3829296424452,
    "w": 79.20176405733186,
    "h": 13.845444059976932,
    "text": "CUPERTINO",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 13.478254969807994,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 23.962513781697904,
    "y": 151.49942329873124,
    "w": 171.86108048511576,
    "h": 100.66435986159169,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 15.335835810158684,
    "y": 151.49942329873124,
    "w": 148.11196730274727,
    "h": 100.66435986159169,
    "text": "24",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 131.10503907055616,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 163.23142449166096,
    "y": 151.94694348327565,
    "w": 38.117084864528096,
    "h": 29.508650519031143,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 80.24841207830382,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 277.08269018743107,
    "y": 143.20645905420992,
    "w": 102.954796030871,
    "h": 113.6979051819184,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "6bb73c032675387ceb88b95662d545a20b8d5fec76c420053c7c0ed27ed2aa20",
      "reference_sha256": "d0df5f63b41474363486cee6da3263a757e52ececb282d691186d4adaa56cfd2",
      "method": "reference_svg",
      "crop_pixels": [
        619,
        320,
        230,
        254
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "condition",
    "x": 25.250430125703204,
    "y": 280.3852364475202,
    "w": 183.05181918412347,
    "h": 21.90080738177624,
    "text": "A calm, clear evening",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 18.675931491532214,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title",
    "x": 25.005639159708917,
    "y": 330.50749711649365,
    "w": 128.08504123046825,
    "h": 22.79584775086505,
    "text": "Next few days",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 19.304862684940634,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast",
    "x": 20.0,
    "y": 361.0,
    "w": 366.0,
    "h": 308.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 20.0,
    "y": 361.0,
    "w": 366.0,
    "h": 77.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 38.05261090438415,
    "y": 388.6851211072664,
    "w": 40.257993384785,
    "h": 17.425605536332178,
    "text": "Now",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 18.85618755102834,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_0",
    "x": 172.78500551267916,
    "y": 367.41407151095734,
    "w": 62.22050716648291,
    "h": 59.98235942668136,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "a435b3527f6e30c49e74e07f15edee5613d1807a57f85084125e6b7b703a81d7",
      "reference_sha256": "d0df5f63b41474363486cee6da3263a757e52ececb282d691186d4adaa56cfd2",
      "method": "reference_svg",
      "crop_pixels": [
        386,
        821,
        139,
        134
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 313.8129899880333,
    "y": 381.97231833910035,
    "w": 55.32116040647295,
    "h": 31.74625144175317,
    "text": "24\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 38.472798207657746,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 20.0,
    "y": 438.0,
    "w": 366.0,
    "h": 77.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 37.96816787315775,
    "y": 464.31603229527104,
    "w": 33.543550165380374,
    "h": 17.425605536332178,
    "text": "Tue",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 18.85618755102834,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 172.78500551267916,
    "y": 443.0449826989619,
    "w": 62.22050716648291,
    "h": 59.98235942668136,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "ade0dbcfe0097ad8a93f2414a97159f473fd499a602c4278359c3743375d4d21",
      "reference_sha256": "d0df5f63b41474363486cee6da3263a757e52ececb282d691186d4adaa56cfd2",
      "method": "reference_svg",
      "crop_pixels": [
        386,
        990,
        139,
        134
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 314.07753113380653,
    "y": 458.05074971164936,
    "w": 54.86253959841957,
    "h": 31.74625144175317,
    "text": "25\u00b0",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 37.95879956760888,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 20.0,
    "y": 515.0,
    "w": 366.0,
    "h": 77.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 38.01965331911391,
    "y": 539.9469434832756,
    "w": 40.257993384785,
    "h": 17.873125720876587,
    "text": "Wed",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 18.766288953999503,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_2",
    "x": 172.78500551267916,
    "y": 518.6758938869665,
    "w": 62.22050716648291,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "53c632fd22c3f300f5f8004151d4f3c6ad082f6eb16be377a67b7b8c868c192f",
      "reference_sha256": "d0df5f63b41474363486cee6da3263a757e52ececb282d691186d4adaa56cfd2",
      "method": "reference_svg",
      "crop_pixels": [
        386,
        1159,
        139,
        135
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_2",
    "x": 313.80848092265757,
    "y": 533.2341407151096,
    "w": 55.26357388537103,
    "h": 32.193771626297575,
    "text": "23\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 38.57103827031225,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 20.0,
    "y": 592.0,
    "w": 366.0,
    "h": 77.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 37.6927471762688,
    "y": 615.5778546712803,
    "w": 33.991179713340685,
    "h": 17.425605536332178,
    "text": "Thu",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 18.28167562394169,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 172.78500551267916,
    "y": 594.3068050749712,
    "w": 62.22050716648291,
    "h": 59.98235942668136,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "19e21dd50ddf4bf3f9ac82ea45d332055d3c9faba9cb4c4c81b9951ca3a87368",
      "reference_sha256": "d0df5f63b41474363486cee6da3263a757e52ececb282d691186d4adaa56cfd2",
      "method": "reference_svg",
      "crop_pixels": [
        386,
        1328,
        139,
        134
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 313.8129899880333,
    "y": 608.8650519031141,
    "w": 55.32116040647295,
    "h": 31.74625144175317,
    "text": "22\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 38.472798207657746,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 21.0,
    "y": 690.0,
    "w": 363.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 21.0,
    "y": 690.0,
    "w": 363.0,
    "h": 56.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 166.88544144825215,
    "y": 709.1095732410611,
    "w": 72.52734261922052,
    "h": 20.110726643598614,
    "text": "My cities",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 17.247657169937252,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 21.0,
    "y": 690.0,
    "w": 363.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
