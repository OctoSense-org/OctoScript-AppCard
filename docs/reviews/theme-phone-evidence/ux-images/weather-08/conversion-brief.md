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
    "x": 20.59146943610733,
    "y": 34.228242074927955,
    "w": 205.49673684274578,
    "h": 33.519308357348706,
    "text": "Conditions",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 40.32692398544905,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 21.392703794286312,
    "y": 87.45244956772333,
    "w": 143.3664459161148,
    "h": 17.4178674351585,
    "text": "Monday, September 7",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.274327058679257,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "current",
    "x": 20.0,
    "y": 114.0,
    "w": 366.0,
    "h": 149.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 38.98675496688742,
    "y": 160.11988472622477,
    "w": 77.07726269315673,
    "h": 52.87858719646799,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "05bcb9f29e1e3c7a68ea6ab0191921f56d45d670b80bf490288324ac0bacca00",
      "reference_sha256": "53eae5d41ca0ce5b8637d7bdec19e9e0545daa2a43e8ad78a71ee653dc762145",
      "method": "reference_svg",
      "crop_pixels": [
        87,
        358,
        172,
        118
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "temperature",
    "x": 132.88520971302427,
    "y": 148.72737752161382,
    "w": 124.54525386313466,
    "h": 74.66743515850143,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 127.11647180818238,
    "y": 148.72737752161382,
    "w": 107.68112423739271,
    "h": 74.66743515850143,
    "text": "24",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 95.84563391033836,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 229.85994683803483,
    "y": 149.17463976945245,
    "w": 31.631099701413778,
    "h": 25.021325648414987,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 63.9697992985942,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 281.95617425988195,
    "y": 165.72334293948126,
    "w": 78.83664459161147,
    "h": 20.54870317002882,
    "text": "Cupertino",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 17.605003372371087,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "condition",
    "x": 282.0656107673318,
    "y": 195.68991354466857,
    "w": 48.81236203090508,
    "h": 18.312391930835734,
    "text": "Cloudy",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 15.225948862591206,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_0",
    "x": 20.0,
    "y": 275.0,
    "w": 178.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "metric_0_label",
    "x": 37.043247931064215,
    "y": 294.0876080691643,
    "w": 60.4635761589404,
    "h": 17.865129682997118,
    "text": "Humidity",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.750137960635232,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_0_value",
    "x": 36.65191466108102,
    "y": 327.1850144092219,
    "w": 84.4741139161113,
    "h": 34.41383285302594,
    "text": "64%",
    "font_src": "self:resources/ux/RobotoCondensed-500.ttf",
    "size": 41.58046040253479,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_1",
    "x": 207.0,
    "y": 275.0,
    "w": 179.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "metric_1_label",
    "x": 225.06670302847826,
    "y": 294.0876080691643,
    "w": 36.264900662251655,
    "h": 14.734293948126801,
    "text": "Wind",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 13.905018346466596,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_1_value",
    "x": 223.8543046357616,
    "y": 327.1850144092219,
    "w": 129.4746136865342,
    "h": 37.544668587896254,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "metric_1_value_number",
    "x": 224.8543046357616,
    "y": 327.1850144092219,
    "w": 38.40176600441501,
    "h": 33.966570605187314,
    "text": "12",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 39.050836540042205,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_1_value_unit",
    "x": 277.7328918322296,
    "y": 328.07953890489915,
    "w": 75.59602649006622,
    "h": 36.65014409221902,
    "text": "km/h",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 39.050836540042205,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_2",
    "x": 20.0,
    "y": 397.0,
    "w": 178.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "metric_2_label",
    "x": 36.960131826677184,
    "y": 416.63746397694524,
    "w": 60.911699779249446,
    "h": 15.181556195965417,
    "text": "Feels like",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.275349994488275,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_2_value",
    "x": 36.96999409979856,
    "y": 449.73487031700284,
    "w": 70.33660176445089,
    "h": 35.30835734870317,
    "text": "25\u00b0",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 43.2435874982088,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_3",
    "x": 207.0,
    "y": 397.0,
    "w": 179.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "metric_3_label",
    "x": 224.81558083613638,
    "y": 416.63746397694524,
    "w": 59.11920529801324,
    "h": 15.181556195965417,
    "text": "UV index",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.275349994488275,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "metric_3_value",
    "x": 223.56156030757947,
    "y": 450.6293948126801,
    "w": 28.911222502406876,
    "h": 33.966570605187314,
    "text": "4",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 41.188950737868204,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title",
    "x": 20.843798512096072,
    "y": 532.4783861671469,
    "w": 224.81929470198673,
    "h": 26.363112391930834,
    "text": "Today into tomorrow",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 23.79054509779876,
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
    "y": 563.0,
    "w": 366.0,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 20.0,
    "y": 563.0,
    "w": 91.5,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 53.929839225678165,
    "y": 580.7827089337176,
    "w": 30.975331290042103,
    "h": 15.181556195965417,
    "text": "Now",
    "font_src": "self:resources/ux/RobotoCondensed-400.ttf",
    "size": 15.514788000905945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_0",
    "x": 37.19426048565121,
    "y": 597.0951008645533,
    "w": 62.28918322295806,
    "h": 57.3598233995585,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "cea46fc88ca9db97eac1e67430de444954dafa8f48c195dcee2239eb3547bed2",
      "reference_sha256": "53eae5d41ca0ce5b8637d7bdec19e9e0545daa2a43e8ad78a71ee653dc762145",
      "method": "reference_svg",
      "crop_pixels": [
        83,
        1335,
        139,
        128
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 49.804610993896425,
    "y": 656.3700288184438,
    "w": 38.05739514348786,
    "h": 21.89048991354467,
    "text": "24\u00b0",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 25.12709257520319,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 111.5,
    "y": 563.0,
    "w": 91.5,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 146.074313456267,
    "y": 580.7827089337176,
    "w": 25.509933774834437,
    "h": 15.181556195965417,
    "text": "Tue",
    "font_src": "self:resources/ux/RobotoCondensed-400.ttf",
    "size": 15.514788000905945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 126.37086092715232,
    "y": 597.0951008645533,
    "w": 61.841059602649004,
    "h": 57.3598233995585,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "c2d544b95260d41c4898541d61da38d19c2d863b7bcb07606d9c6939a7ef0469",
      "reference_sha256": "53eae5d41ca0ce5b8637d7bdec19e9e0545daa2a43e8ad78a71ee653dc762145",
      "method": "reference_svg",
      "crop_pixels": [
        282,
        1335,
        138,
        128
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 139.29467065640083,
    "y": 656.3700288184438,
    "w": 38.2490564910062,
    "h": 21.89048991354467,
    "text": "25\u00b0",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 24.475433094815955,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 203.0,
    "y": 563.0,
    "w": 91.5,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 230.3453129630468,
    "y": 580.7827089337176,
    "w": 31.783664459161148,
    "h": 15.181556195965417,
    "text": "Wed",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 14.71711252528096,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_2",
    "x": 214.20309050772627,
    "y": 597.0951008645533,
    "w": 62.28918322295806,
    "h": 57.3598233995585,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "53d16e82eb2607892e3c7f980ff9eba659ad8752ded0e5bbdd98de8242192f9d",
      "reference_sha256": "53eae5d41ca0ce5b8637d7bdec19e9e0545daa2a43e8ad78a71ee653dc762145",
      "method": "reference_svg",
      "crop_pixels": [
        478,
        1335,
        139,
        128
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_2",
    "x": 227.99894691508456,
    "y": 656.3700288184438,
    "w": 38.05739514348786,
    "h": 22.337752161383285,
    "text": "23\u00b0",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.087318922186352,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 294.5,
    "y": 563.0,
    "w": 91.5,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 321.7625315060932,
    "y": 580.7827089337176,
    "w": 26.087416134276022,
    "h": 15.181556195965417,
    "text": "Thu",
    "font_src": "self:resources/ux/RobotoCondensed-400.ttf",
    "size": 14.71711252528096,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 302.4834437086093,
    "y": 597.0951008645533,
    "w": 61.841059602649004,
    "h": 57.3598233995585,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "cfc9eb938ff9c7aae1cc11a8e09126dee6da9dbe7c0f1e715dfdb5b212ae1ece",
      "reference_sha256": "53eae5d41ca0ce5b8637d7bdec19e9e0545daa2a43e8ad78a71ee653dc762145",
      "method": "reference_svg",
      "crop_pixels": [
        675,
        1335,
        138,
        128
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 315.5419178371635,
    "y": 656.3700288184438,
    "w": 37.16114790286976,
    "h": 21.89048991354467,
    "text": "22\u00b0",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 25.12709257520319,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 20.0,
    "y": 711.0,
    "w": 366.0,
    "h": 44.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 20.0,
    "y": 711.0,
    "w": 366.0,
    "h": 44.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 169.0546254813733,
    "y": 724.3538904899135,
    "w": 68.08167770419426,
    "h": 19.654178674351584,
    "text": "My cities",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 16.65338156845913,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 20.0,
    "y": 711.0,
    "w": 366.0,
    "h": 44.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
