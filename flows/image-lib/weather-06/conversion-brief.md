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
    "x": 26.30142947879966,
    "y": 40.96193771626297,
    "w": 185.73759647188533,
    "h": 33.08881199538639,
    "text": "Your cities",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 39.73881420134753,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 26.660892289129706,
    "y": 93.32179930795847,
    "w": 144.1080485115766,
    "h": 17.873125720876587,
    "text": "Monday, September 7",
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
    "id": "featured",
    "x": 23.0,
    "y": 128.0,
    "w": 360.0,
    "h": 216.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "location",
    "x": 45.010956607102024,
    "y": 159.55478662053056,
    "w": 157.08930540242557,
    "h": 36.22145328719723,
    "text": "Cupertino",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 34.27814179489067,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "condition",
    "x": 45.21472111666054,
    "y": 210.12456747404843,
    "w": 101.58324145534729,
    "h": 21.00576701268743,
    "text": "Partly cloudy",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 18.091241502858967,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 265.23484013230427,
    "y": 162.239907727797,
    "w": 100.24035281146637,
    "h": 62.17762399077278,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 260.8391543161001,
    "y": 162.239907727797,
    "w": 83.34765642057111,
    "h": 62.17762399077278,
    "text": "24",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 78.9058105517236,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 342.3286339163847,
    "y": 162.239907727797,
    "w": 28.213642407227432,
    "h": 21.453287197231834,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 72.06518584663466,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 268.1300992282249,
    "y": 239.8708189158016,
    "w": 87.73539140022051,
    "h": 76.09702315325248,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "2a02d691c0a158d93dbef061f173d0e797f4f396e21eaa64e7ed272beb05d5df",
      "reference_sha256": "d1dd8a25bb6d8adb9a2edd608f7362e263fac48163de0af97e817fc3546d854a",
      "method": "reference_svg",
      "crop_pixels": [
        599,
        536,
        196,
        170
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "city_0",
    "x": 24.0,
    "y": 357.0,
    "w": 358.0,
    "h": 100.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_name_0",
    "x": 46.26573815333722,
    "y": 382.4198385236447,
    "w": 168.7276736493936,
    "h": 24.13840830449827,
    "text": "San Francisco",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 27.511486754779057,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_note_0",
    "x": 46.701642376807385,
    "y": 419.56401384083046,
    "w": 103.37375964718854,
    "h": 15.635524798154556,
    "text": "Coastal clouds",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.895525680539011,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_0",
    "x": 300.5975744211687,
    "y": 386.4475201845444,
    "w": 59.506063947078275,
    "h": 41.1441753171857,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_temp_0_number",
    "x": 299.8543511384098,
    "y": 386.4475201845444,
    "w": 44.04977556988832,
    "h": 41.1441753171857,
    "text": "19",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 49.71788746097518,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_0_degree",
    "x": 343.42927984559816,
    "y": 386.4475201845444,
    "w": 20.18233932407748,
    "h": 16.08304498269896,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 49.891282509208615,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_1",
    "x": 24.0,
    "y": 467.0,
    "w": 358.0,
    "h": 101.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_name_1",
    "x": 46.728891106100015,
    "y": 492.5098039215686,
    "w": 74.72546857772878,
    "h": 29.061130334486734,
    "text": "Tokyo",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 26.66077695158163,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_note_1",
    "x": 46.7136297154571,
    "y": 530.5490196078431,
    "w": 65.32524807056228,
    "h": 19.215686274509803,
    "text": "Light rain",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.982863733728786,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_1",
    "x": 291.1973539140022,
    "y": 496.0899653979239,
    "w": 69.35391400220507,
    "h": 42.03921568627451,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_temp_1_number",
    "x": 289.0702233232038,
    "y": 496.0899653979239,
    "w": 54.657843554079285,
    "h": 42.03921568627451,
    "text": "28",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 50.91785210816353,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_1_degree",
    "x": 343.8769093935585,
    "y": 496.53748558246826,
    "w": 20.18233932407748,
    "h": 16.08304498269896,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 49.891282509208615,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_2",
    "x": 24.0,
    "y": 577.0,
    "w": 358.0,
    "h": 101.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_name_2",
    "x": 46.17292349045919,
    "y": 603.0472895040369,
    "w": 153.9558985667034,
    "h": 30.403690888119954,
    "text": "Copenhagen",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 27.73496942029407,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_note_2",
    "x": 46.67290815730795,
    "y": 640.638985005767,
    "w": 76.51598676957,
    "h": 16.08304498269896,
    "text": "Clear skies",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 16.506892052867435,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_2",
    "x": 300.14994487320837,
    "y": 606.1799307958478,
    "w": 59.953693495038586,
    "h": 41.5916955017301,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "city_temp_2_number",
    "x": 299.3735647479172,
    "y": 606.1799307958478,
    "w": 44.490228418684545,
    "h": 41.5916955017301,
    "text": "16",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 50.31881855394983,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "city_temp_2_degree",
    "x": 343.42927984559816,
    "y": 606.1799307958478,
    "w": 20.18233932407748,
    "h": 16.08304498269896,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 49.891282509208615,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 24.0,
    "y": 693.0,
    "w": 358.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 24.0,
    "y": 693.0,
    "w": 358.0,
    "h": 55.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 160.20387900293574,
    "y": 711.7946943483275,
    "w": 88.15435501653803,
    "h": 21.90080738177624,
    "text": "Add a city",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 19.043412108272594,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 24.0,
    "y": 693.0,
    "w": 358.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
