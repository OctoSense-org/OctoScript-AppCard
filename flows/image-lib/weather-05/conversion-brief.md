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
    "x": 23.23629903138933,
    "y": 33.35409457900807,
    "w": 278.8445424476295,
    "h": 37.116493656286046,
    "text": "The daily weather",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 34.133155011612395,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 25.161894881032286,
    "y": 81.68627450980392,
    "w": 141.86990077177506,
    "h": 17.425605536332178,
    "text": "Monday, September 7",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.202293459921645,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 24.93048386596487,
    "y": 130.46597462514418,
    "w": 150.82249173098126,
    "h": 14.740484429065743,
    "text": "CUPERTINO, CALIFORNIA",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 11.619921875714022,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 23.514884233737597,
    "y": 173.87543252595157,
    "w": 212.59536934950384,
    "h": 141.38869665513263,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 9.319395488960375,
    "y": 173.87543252595157,
    "w": 196.83453592582742,
    "h": 141.38869665513263,
    "text": "24",
    "font_src": "self:resources/ux/Inter-200.ttf",
    "size": 186.33910645676266,
    "weight": 200,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 195.8108346897588,
    "y": 174.32295271049597,
    "w": 50.59238313800398,
    "h": 34.878892733564015,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Thin.ttf",
    "size": 132.57855831936917,
    "weight": 100,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 278.87320837927234,
    "y": 239.8708189158016,
    "w": 106.98346196251377,
    "h": 79.23042998897463,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "763fc1d1c8fad1b8a8e5a5a0f2f0c46b7436cee176b688441b49b260696f6835",
      "reference_sha256": "5c899b670d292ec7657cb40d164832325c55ccaa9fae44b78b88f2a596bc05bc",
      "method": "reference_svg",
      "crop_pixels": [
        623,
        536,
        239,
        177
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "condition",
    "x": 26.2954749325403,
    "y": 346.6182237600923,
    "w": 250.1962513781698,
    "h": 21.453287197231834,
    "text": "A softer kind of sunshine.",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 22.580121402356788,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "range",
    "x": 26.017831864651868,
    "y": 386.4475201845444,
    "w": 128.59606464164403,
    "h": 18.320645905420992,
    "text": "High 27\u00b0 / Low 17\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.64969171543566,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast",
    "x": 19.0,
    "y": 424.0,
    "w": 367.0,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 19.0,
    "y": 424.0,
    "w": 91.75,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 52.53762169225939,
    "y": 445.07266435986156,
    "w": 28.61962513781698,
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
    "x": 34.91510474090408,
    "y": 459.60322952710493,
    "w": 61.7728776185226,
    "h": 64.90628445424476,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "92c5d65109c949a9fdd3a4cdd6417e712dc9a88a5e7cdfce65c8da8680f7e2d4",
      "reference_sha256": "5c899b670d292ec7657cb40d164832325c55ccaa9fae44b78b88f2a596bc05bc",
      "method": "reference_svg",
      "crop_pixels": [
        78,
        1027,
        138,
        145
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 46.224035681674586,
    "y": 526.5213379469435,
    "w": 40.74605357991342,
    "h": 23.243367935409456,
    "text": "24\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 26.682747144020695,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 110.75,
    "y": 424.0,
    "w": 91.75,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 147.334970219616,
    "y": 445.07266435986156,
    "w": 23.248070562293275,
    "h": 13.397923875432525,
    "text": "Tue",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.19933128571984,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 126.67916207276735,
    "y": 459.60322952710493,
    "w": 61.7728776185226,
    "h": 64.90628445424476,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "4a1bd1a65e9d2fa5e9b002b9f06c4894036c15ba7f876e8086bb1e8ee214a8bf",
      "reference_sha256": "5c899b670d292ec7657cb40d164832325c55ccaa9fae44b78b88f2a596bc05bc",
      "method": "reference_svg",
      "crop_pixels": [
        283,
        1027,
        138,
        145
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 138.4239837710474,
    "y": 526.5213379469435,
    "w": 40.596134240167075,
    "h": 23.690888119953865,
    "text": "25\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 26.938502918948238,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 202.5,
    "y": 424.0,
    "w": 91.75,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 234.22407709191043,
    "y": 445.07266435986156,
    "w": 29.067254685777286,
    "h": 13.397923875432525,
    "text": "Wed",
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
    "id": "day_icon_2",
    "x": 216.6527012127894,
    "y": 459.60322952710493,
    "w": 61.7728776185226,
    "h": 64.90628445424476,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "ad1802ce08671a5bde10a06b09bf9efcb65630d274da95ce543262358ca36517",
      "reference_sha256": "5c899b670d292ec7657cb40d164832325c55ccaa9fae44b78b88f2a596bc05bc",
      "method": "reference_svg",
      "crop_pixels": [
        484,
        1027,
        138,
        145
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_2",
    "x": 228.84515245902975,
    "y": 526.5213379469435,
    "w": 39.92468991822661,
    "h": 23.690888119953865,
    "text": "23\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 26.938502918948238,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 294.25,
    "y": 424.0,
    "w": 91.75,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 327.438056144244,
    "y": 445.07266435986156,
    "w": 24.14332965821389,
    "h": 13.397923875432525,
    "text": "Thu",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.788669831817815,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 307.5214994487321,
    "y": 459.60322952710493,
    "w": 62.22050716648291,
    "h": 64.90628445424476,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "d1581450a4dc5a31cf78fe7b097c67443fe048e931343ba8608ccb1231af978a",
      "reference_sha256": "5c899b670d292ec7657cb40d164832325c55ccaa9fae44b78b88f2a596bc05bc",
      "method": "reference_svg",
      "crop_pixels": [
        687,
        1027,
        139,
        145
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 319.72568948542323,
    "y": 526.5213379469435,
    "w": 40.07460925797295,
    "h": 23.243367935409456,
    "text": "22\u00b0",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 26.682747144020695,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity",
    "x": 19.0,
    "y": 579.0,
    "w": 177.0,
    "h": 98.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "humidity_label",
    "x": 39.17981550121871,
    "y": 594.9919261822375,
    "w": 54.13450937155457,
    "h": 16.08304498269896,
    "text": "Humidity",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.593422964156474,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity_value",
    "x": 39.00716332751111,
    "y": 621.843137254902,
    "w": 79.85744553610968,
    "h": 33.536332179930795,
    "text": "64%",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 40.380779909544906,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wind",
    "x": 205.0,
    "y": 578.0,
    "w": 181.0,
    "h": 99.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wind_label",
    "x": 225.27148613270427,
    "y": 594.9919261822375,
    "w": 33.09592061742006,
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
    "x": 223.58481982297394,
    "y": 621.843137254902,
    "w": 128.26211461435392,
    "h": 33.536332179930795,
    "text": "12 km/h",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 33.90717954288019,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 20.0,
    "y": 692.0,
    "w": 365.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 20.0,
    "y": 692.0,
    "w": 365.0,
    "h": 56.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 165.54580541900614,
    "y": 711.3471741637832,
    "w": 74.27783902976846,
    "h": 21.00576701268743,
    "text": "My cities",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 17.625410345133528,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 20.0,
    "y": 692.0,
    "w": 365.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "forecast_separator_0",
    "x": 111,
    "y": 469,
    "w": 0.65,
    "h": 81,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "forecast_separator_1",
    "x": 204,
    "y": 469,
    "w": 0.65,
    "h": 81,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "forecast_separator_2",
    "x": 295,
    "y": 469,
    "w": 0.65,
    "h": 81,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  }
]
```
