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
    "x": 26.231939431390863,
    "y": 40.51441753171857,
    "w": 162.1616856642987,
    "h": 35.773933102652826,
    "text": "Cupertino",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 33.80205649218386,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 27.52092107265002,
    "y": 84.81891580161476,
    "w": 147.6890848952591,
    "h": 18.320645905420992,
    "text": "Monday, September 7",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.234729686618078,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "units",
    "x": 329,
    "y": 37,
    "w": 51,
    "h": 47,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "units_surface",
    "x": 329,
    "y": 37,
    "w": 51,
    "h": 47,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "units_label",
    "x": 346.2620174118839,
    "y": 52.59746251441753,
    "w": 20.56229327453142,
    "h": 16.08304498269896,
    "text": "\u00b0C",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.68928865013669,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "units_control",
    "x": 329,
    "y": 37,
    "w": 51,
    "h": 47,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "current",
    "x": 26.5,
    "y": 119,
    "w": 353,
    "h": 244,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "current_kicker",
    "x": 51.79162261761062,
    "y": 150.60438292964244,
    "w": 118.59316427783902,
    "h": 12.95040369088812,
    "text": "CURRENT WEATHER",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 51.267916207276734,
    "y": 184.1683967704729,
    "w": 150.37486218302095,
    "h": 84.55363321799308,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 46.14027731298802,
    "y": 184.1683967704729,
    "w": 125.55068739279145,
    "h": 84.55363321799308,
    "text": "24",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 113.13712530617006,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 169.05060861514497,
    "y": 185.5109573241061,
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
    "x": 248.88202866593164,
    "y": 186.1683967704729,
    "w": 111.01212789415655,
    "h": 102.954796030871,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "3280c23a7620c14ca1181792c9cbc59e68048c44c1544894f341202119ba8726",
      "reference_sha256": "4151ef99fa08444701901ef37f66db47944ca3ca2f8e7d72b86d785c4ab2ca64",
      "method": "reference_svg",
      "crop_pixels": [
        556,
        416,
        248,
        230
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "condition",
    "x": 51.06913555254486,
    "y": 287.5455594002307,
    "w": 104.71664829106946,
    "h": 20.558246828143023,
    "text": "Partly cloudy",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 17.615156200152153,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "range",
    "x": 51.16334694975017,
    "y": 318.8719723183391,
    "w": 88.7454556743031,
    "h": 15.635524798154556,
    "text": "H 27\u00b0 \u00b7 L 17\u00b0",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 16.34202921089123,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title",
    "x": 26.258633832736667,
    "y": 388.6851211072664,
    "w": 99.34509371554574,
    "h": 19.66320645905421,
    "text": "This week",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 21.397823031494823,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title_detail",
    "x": 296.7632649314139,
    "y": 396.29296424452133,
    "w": 83.67805953693495,
    "h": 16.08304498269896,
    "text": "4-day outlook",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.854303173084002,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast",
    "x": 26,
    "y": 421,
    "w": 354,
    "h": 135,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 26,
    "y": 421,
    "w": 88.5,
    "h": 135,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 58.35680581574341,
    "y": 441.49250288350635,
    "w": 27.72436604189636,
    "h": 13.397923875432525,
    "text": "Now",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.039937735017487,
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
    "y": 456.0230680507497,
    "w": 62.22050716648291,
    "h": 64.01102535832415,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "40c2174a94d5cf1b368afe5239501c56eb22102d1434ae456b287ec6d7d9e16f",
      "reference_sha256": "4151ef99fa08444701901ef37f66db47944ca3ca2f8e7d72b86d785c4ab2ca64",
      "method": "reference_svg",
      "crop_pixels": [
        90,
        1019,
        139,
        143
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 59.050863761660565,
    "y": 522.0461361014994,
    "w": 27.276736493936053,
    "h": 15.635524798154556,
    "text": "24\u00b0",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.34202921089123,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 114.5,
    "y": 421,
    "w": 88.5,
    "h": 135,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 146.45793877166136,
    "y": 441.49250288350635,
    "w": 23.695700110253583,
    "h": 12.95040369088812,
    "text": "Tue",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.570791700685563,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 125.78390297684675,
    "y": 455.5755478662053,
    "w": 62.22050716648291,
    "h": 64.45865490628445,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "48bd8e21f061bde8b6d51ddd287abd270681dfacc83eed743ba27653e61f5f81",
      "reference_sha256": "4151ef99fa08444701901ef37f66db47944ca3ca2f8e7d72b86d785c4ab2ca64",
      "method": "reference_svg",
      "crop_pixels": [
        281,
        1018,
        139,
        144
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 144.97594318200282,
    "y": 522.0461361014994,
    "w": 26.82910694597574,
    "h": 16.08304498269896,
    "text": "25\u00b0",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.68928865013669,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 203,
    "y": 421,
    "w": 88.5,
    "h": 135,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 230.66943526011758,
    "y": 441.49250288350635,
    "w": 29.067254685777286,
    "h": 12.95040369088812,
    "text": "Wed",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.107283196128712,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_2",
    "x": 213.07166482910694,
    "y": 455.5755478662053,
    "w": 62.22050716648291,
    "h": 64.45865490628445,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "43903b4359eed31f30eda0744829016f9742759610c69dde2aa0eb396a1c6cf3",
      "reference_sha256": "4151ef99fa08444701901ef37f66db47944ca3ca2f8e7d72b86d785c4ab2ca64",
      "method": "reference_svg",
      "crop_pixels": [
        476,
        1018,
        139,
        144
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed smooth external cloud silhouette; closed tiny source texture holes, native SVG gradient fill."
    }
  },
  {
    "id": "day_temp_2",
    "x": 232.71133458222334,
    "y": 522.0461361014994,
    "w": 26.381477398015434,
    "h": 16.08304498269896,
    "text": "23\u00b0",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.68928865013669,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 291.5,
    "y": 421,
    "w": 88.5,
    "h": 135,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 319.7005342956702,
    "y": 441.49250288350635,
    "w": 24.14332965821389,
    "h": 12.95040369088812,
    "text": "Thu",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.22732744656847,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 299.9117971334068,
    "y": 455.5755478662053,
    "w": 62.22050716648291,
    "h": 64.45865490628445,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "d9409767344f45b0f41abf95ea9ee24418e89ba2a1dbabca13ce123c0a9f8e3f",
      "reference_sha256": "4151ef99fa08444701901ef37f66db47944ca3ca2f8e7d72b86d785c4ab2ca64",
      "method": "reference_svg",
      "crop_pixels": [
        670,
        1018,
        139,
        144
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 319.5712606745602,
    "y": 522.0461361014994,
    "w": 26.381477398015434,
    "h": 15.635524798154556,
    "text": "22\u00b0",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 16.34202921089123,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "details_title",
    "x": 26.277193550738325,
    "y": 579.3287197231833,
    "w": 68.3125358093768,
    "h": 19.215686274509803,
    "text": "Details",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 20.786456659166397,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity",
    "x": 26.5,
    "y": 613,
    "w": 171,
    "h": 84,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "humidity_label",
    "x": 42.468847717341724,
    "y": 629.0034602076124,
    "w": 51.44873208379272,
    "h": 16.08304498269896,
    "text": "Humidity",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.854303173084002,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity_value",
    "x": 42.07008813689444,
    "y": 654.959630911188,
    "w": 53.68687982359427,
    "h": 22.79584775086505,
    "text": "64%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.961115677990403,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind",
    "x": 208,
    "y": 613,
    "w": 171.5,
    "h": 84,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_label",
    "x": 222.10345772933167,
    "y": 629.0034602076124,
    "w": 30.857772877618523,
    "h": 13.397923875432525,
    "text": "Wind",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 12.369503918307077,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind_value",
    "x": 222.21799675711006,
    "y": 654.0645905420992,
    "w": 92.96055810582197,
    "h": 25.480968858131487,
    "text": "12 km/h",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 24.190280245643567,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 26.5,
    "y": 714,
    "w": 353,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 26.5,
    "y": 714,
    "w": 353,
    "h": 41,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 173.03575447215064,
    "y": 727.4579008073817,
    "w": 60.8489525909592,
    "h": 17.873125720876587,
    "text": "My cities",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.758644383911262,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 26.5,
    "y": 714,
    "w": 353,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
