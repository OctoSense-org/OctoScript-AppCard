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
    "x": 29.156780209594547,
    "y": 27.536332179930795,
    "w": 292.7210584343991,
    "h": 35.773933102652826,
    "text": "Weather at a glance",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 33.375980149845404,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 29.17051801489004,
    "y": 73.63091118800462,
    "w": 159.3274531422271,
    "h": 20.110726643598614,
    "text": "Monday, September 7",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 17.139070897445336,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "current",
    "x": 22.0,
    "y": 109.0,
    "w": 203.0,
    "h": 351.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "location",
    "x": 44.160816251522654,
    "y": 134.94117647058823,
    "w": 106.05953693495039,
    "h": 25.928489042675892,
    "text": "Cupertino",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 23.32817983263393,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 44.105843439911794,
    "y": 180.14071510957325,
    "w": 139.63175303197355,
    "h": 83.65859284890426,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 37.34867363003225,
    "y": 180.14071510957325,
    "w": 122.68063555657298,
    "h": 83.65859284890426,
    "text": "24",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 108.04026367851387,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 154.96599632665115,
    "y": 180.58823529411765,
    "w": 34.95224108429413,
    "h": 25.480968858131487,
    "text": "\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-300.ttf",
    "size": 88.51715135101264,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 64.90628445424476,
    "y": 285.9653979238754,
    "w": 132.05071664829106,
    "h": 107.8787210584344,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "ffdd5d124941252f78533cc28ecfe2297077f548c6657da4b326bee4daf57ac6",
      "reference_sha256": "a7c5a773b95cf7b380380d0c4e06d897df620bebfb46a7e59f772abdfebf7e36",
      "method": "reference_svg",
      "crop_pixels": [
        145,
        639,
        295,
        241
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "condition",
    "x": 44.441339858232865,
    "y": 416.4313725490196,
    "w": 100.68798235942668,
    "h": 20.110726643598614,
    "text": "Partly cloudy",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 17.139070897445336,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity",
    "x": 242,
    "y": 110,
    "w": 141,
    "h": 167,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "humidity_label",
    "x": 260.84160649717177,
    "y": 137.17877739331027,
    "w": 53.23925027563396,
    "h": 16.978085351787776,
    "text": "Humidity",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.806473778497633,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity_value",
    "x": 259.8080285185506,
    "y": 172.53287197231833,
    "w": 88.74224003498622,
    "h": 35.773933102652826,
    "text": "64%",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 43.43992990269225,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind",
    "x": 241.0,
    "y": 293.0,
    "w": 142.0,
    "h": 167.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_label",
    "x": 260.6342204215686,
    "y": 320.6620530565167,
    "w": 32.20066152149945,
    "h": 13.397923875432525,
    "text": "Wind",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.838693818896893,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind_value",
    "x": 260.3109151047409,
    "y": 355.5686274509804,
    "w": 105.61190738699007,
    "h": 36.22145328719723,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_value_number",
    "x": 261.3109151047409,
    "y": 355.5686274509804,
    "w": 37.01984564498346,
    "h": 34.878892733564015,
    "text": "12",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 37.5104229187395,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind_value_unit",
    "x": 305.17861080485113,
    "y": 366.7566320645905,
    "w": 60.74421168687982,
    "h": 25.03344867358708,
    "text": "km/h",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 37.5104229187395,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title",
    "x": 26.672026863846583,
    "y": 482.2168396770473,
    "w": 157.53693495038587,
    "h": 20.558246828143023,
    "text": "The week ahead",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 22.620555776151672,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast",
    "x": 21.0,
    "y": 513.0,
    "w": 362.0,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 21.0,
    "y": 513.0,
    "w": 90.5,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 56.957825549815915,
    "y": 531.444059976932,
    "w": 27.72436604189636,
    "h": 13.845444059976932,
    "text": "Now",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.660887150970703,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_0",
    "x": 40.28665931642778,
    "y": 546.4221453287197,
    "w": 62.22050716648291,
    "h": 69.83020948180815,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "97452f6f5244356be163182b1cb5ea9cf93f5eced6ea30b29bf6934671a9bd22",
      "reference_sha256": "a7c5a773b95cf7b380380d0c4e06d897df620bebfb46a7e59f772abdfebf7e36",
      "method": "reference_svg",
      "crop_pixels": [
        90,
        1221,
        139,
        156
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 54.47497986582938,
    "y": 618.2629757785467,
    "w": 40.073511137246555,
    "h": 22.348327566320645,
    "text": "24\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 25.441689137322058,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 111.5,
    "y": 513.0,
    "w": 90.5,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 149.08165532894046,
    "y": 531.444059976932,
    "w": 23.248070562293275,
    "h": 13.845444059976932,
    "text": "Tue",
    "font_src": "self:resources/ux/RobotoCondensed-300.ttf",
    "size": 13.651638073685008,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 128.4696802646086,
    "y": 546.4221453287197,
    "w": 62.22050716648291,
    "h": 69.83020948180815,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "563a205d0624fab3f1a5c9c9643f7ad377e02cb9cdf7a37e0332c7c29ef64e8a",
      "reference_sha256": "a7c5a773b95cf7b380380d0c4e06d897df620bebfb46a7e59f772abdfebf7e36",
      "method": "reference_svg",
      "crop_pixels": [
        287,
        1221,
        139,
        156
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 141.7765170565164,
    "y": 618.2629757785467,
    "w": 40.25557795958683,
    "h": 22.348327566320645,
    "text": "25\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 25.10178681083813,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 202.0,
    "y": 513.0,
    "w": 90.5,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 233.72428180454054,
    "y": 531.444059976932,
    "w": 28.61962513781698,
    "h": 13.845444059976932,
    "text": "Wed",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 12.958527914416939,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_2",
    "x": 215.30981256890848,
    "y": 546.4221453287197,
    "w": 62.22050716648291,
    "h": 69.83020948180815,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "d9d81fd414a56276293a4b137e4e86ee1c80287ae3c7f4a535c590d14109a985",
      "reference_sha256": "a7c5a773b95cf7b380380d0c4e06d897df620bebfb46a7e59f772abdfebf7e36",
      "method": "reference_svg",
      "crop_pixels": [
        481,
        1221,
        139,
        156
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_2",
    "x": 228.6166493608163,
    "y": 618.2629757785467,
    "w": 39.584133637646374,
    "h": 22.348327566320645,
    "text": "23\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 25.10178681083813,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 292.5,
    "y": 513.0,
    "w": 90.5,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 324.2023971483968,
    "y": 531.444059976932,
    "w": 23.695700110253583,
    "h": 13.845444059976932,
    "text": "Thu",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 12.958527914416939,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 303.4928335170893,
    "y": 546.4221453287197,
    "w": 62.22050716648291,
    "h": 69.83020948180815,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "23ceb25ceba4fc38b95f7b0383cafd3744e304bc5a6885c14f6aa722517ed6a1",
      "reference_sha256": "a7c5a773b95cf7b380380d0c4e06d897df620bebfb46a7e59f772abdfebf7e36",
      "method": "reference_svg",
      "crop_pixels": [
        678,
        1221,
        139,
        156
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 316.78589497057027,
    "y": 618.2629757785467,
    "w": 39.4020668153061,
    "h": 22.348327566320645,
    "text": "22\u00b0",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 25.441689137322058,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "note",
    "x": 29.967484811621247,
    "y": 675.5455594002307,
    "w": 195.13781697905182,
    "h": 18.768166089965398,
    "text": "A little sunshine, a slower day.",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.710814989324891,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 22.0,
    "y": 708.0,
    "w": 359.0,
    "h": 47.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 22.0,
    "y": 708.0,
    "w": 359.0,
    "h": 47.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 169.36378579565118,
    "y": 723.4302191464822,
    "w": 67.56339581036383,
    "h": 19.66320645905421,
    "text": "My cities",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.662985594738522,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 22.0,
    "y": 708.0,
    "w": 359.0,
    "h": 47.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
