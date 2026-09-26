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
    "x": 27.388848706104,
    "y": 30.221453287197228,
    "w": 234.08158765159865,
    "h": 38.45905420991926,
    "text": "Plan your week",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 35.7689523679243,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 28.278562801364078,
    "y": 83.47635524798154,
    "w": 148.1367144432194,
    "h": 18.768166089965398,
    "text": "Monday, September 7",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.3295510148247,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 28.181120850911146,
    "y": 133.1510957324106,
    "w": 102.40711734881916,
    "h": 25.480968858131487,
    "text": "Cupertino",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 23.252126966941482,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature",
    "x": 282.6923925027563,
    "y": 110.7750865051903,
    "w": 102.47850055126791,
    "h": 59.04498269896194,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "temperature_number",
    "x": 279.07853334008075,
    "y": 110.7750865051903,
    "w": 77.85887541345093,
    "h": 59.04498269896194,
    "text": "24",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 74.65703613740003,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "temperature_degree",
    "x": 358.2458124087604,
    "y": 111.67012687427912,
    "w": 32.641790099443995,
    "h": 23.690888119953865,
    "text": "\u00b0",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 81.30431223722886,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "forecast_title",
    "x": 28.605522943253618,
    "y": 206.0968858131488,
    "w": 138.7364939360529,
    "h": 22.348327566320645,
    "text": "Five-day outlook",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 19.045805806297356,
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
    "y": 237.0,
    "w": 365.0,
    "h": 361.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_0",
    "x": 21.0,
    "y": 237.0,
    "w": 365.0,
    "h": 72.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_0",
    "x": 42.48294621879064,
    "y": 266.959630911188,
    "w": 55.92502756339581,
    "h": 18.768166089965398,
    "text": "Monday",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.3295510148247,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_0",
    "x": 182.18522601984563,
    "y": 246.1361014994233,
    "w": 61.7728776185226,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_0.svg",
      "sha256": "90485b9e6ad6f05fd44c512ff6230348499a43952faf27810dd7368cdaa3d36b",
      "reference_sha256": "bf1dfdb454c17b386b14017b56340dc7bef13ea9397ebf0e4b7e4603c02847a0",
      "method": "reference_svg",
      "crop_pixels": [
        407,
        550,
        138,
        135
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_0",
    "x": 315.79998750397067,
    "y": 260.69434832756633,
    "w": 48.76295479603087,
    "h": 28.166089965397923,
    "text": "24\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 32.77625976763904,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_1",
    "x": 21.0,
    "y": 309.2,
    "w": 365.0,
    "h": 72.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_1",
    "x": 42.583209722953846,
    "y": 338.11534025374857,
    "w": 59.05843439911797,
    "h": 18.768166089965398,
    "text": "Tuesday",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.3295510148247,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_1",
    "x": 182.18522601984563,
    "y": 317.2918108419838,
    "w": 61.7728776185226,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_1.svg",
      "sha256": "cefbbcc4fa11eccca0acafadf90e75369cdc37312eb5ec382993d22b99cace2d",
      "reference_sha256": "bf1dfdb454c17b386b14017b56340dc7bef13ea9397ebf0e4b7e4603c02847a0",
      "method": "reference_svg",
      "crop_pixels": [
        407,
        709,
        138,
        135
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_1",
    "x": 316.1897452905431,
    "y": 331.40253748558246,
    "w": 48.31532524807056,
    "h": 29.061130334486734,
    "text": "25\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 33.54587903596656,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_2",
    "x": 21.0,
    "y": 381.4,
    "w": 365.0,
    "h": 72.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_2",
    "x": 42.51584353197073,
    "y": 408.8235294117647,
    "w": 81.4399117971334,
    "h": 18.768166089965398,
    "text": "Wednesday",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.3295510148247,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_2",
    "x": 182.18522601984563,
    "y": 388.0,
    "w": 61.7728776185226,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_2.svg",
      "sha256": "b7dc2a592ee1b69aa3bb52fa13cdd6a0a84cc18012009a1b9d4b09da70a0fb67",
      "reference_sha256": "bf1dfdb454c17b386b14017b56340dc7bef13ea9397ebf0e4b7e4603c02847a0",
      "method": "reference_svg",
      "crop_pixels": [
        407,
        867,
        138,
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
    "x": 316.2347898058502,
    "y": 402.558246828143,
    "w": 48.31532524807056,
    "h": 28.61361014994233,
    "text": "23\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 32.94684548175287,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_3",
    "x": 21.0,
    "y": 453.6,
    "w": 365.0,
    "h": 72.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_3",
    "x": 42.59817998761676,
    "y": 478.18915801614764,
    "w": 65.32524807056228,
    "h": 18.768166089965398,
    "text": "Thursday",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.3295510148247,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_3",
    "x": 182.18522601984563,
    "y": 457.3656286043829,
    "w": 61.7728776185226,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_3.svg",
      "sha256": "ac0d8781bfd4ac06bf9d7893eb2d7ebab93630fbf2519b10d2878c702ae781af",
      "reference_sha256": "bf1dfdb454c17b386b14017b56340dc7bef13ea9397ebf0e4b7e4603c02847a0",
      "method": "reference_svg",
      "crop_pixels": [
        407,
        1022,
        138,
        135
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_3",
    "x": 316.20197592052716,
    "y": 471.92387543252596,
    "w": 48.31532524807056,
    "h": 28.61361014994233,
    "text": "22\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 33.38322754111383,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_4",
    "x": 21.0,
    "y": 525.8,
    "w": 365.0,
    "h": 72.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "day_label_4",
    "x": 42.602708336093954,
    "y": 548.4498269896194,
    "w": 43.391400220507165,
    "h": 18.768166089965398,
    "text": "Friday",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.3295510148247,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "day_icon_4",
    "x": 182.18522601984563,
    "y": 527.6262975778546,
    "w": 61.7728776185226,
    "h": 60.429988974641674,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/day_icon_4.svg",
      "sha256": "ed06acacdb252e48fc1841dcbdaedc1a35015110ab0e2be6526814fdd37fa949",
      "reference_sha256": "bf1dfdb454c17b386b14017b56340dc7bef13ea9397ebf0e4b7e4603c02847a0",
      "method": "reference_svg",
      "crop_pixels": [
        407,
        1179,
        138,
        135
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "day_temp_4",
    "x": 316.20197592052716,
    "y": 541.7370242214532,
    "w": 48.31532524807056,
    "h": 28.61361014994233,
    "text": "24\u00b0",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 33.38322754111383,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "note",
    "x": 28.38119579550176,
    "y": 621.3956170703575,
    "w": 215.728776185226,
    "h": 22.79584775086505,
    "text": "Best day outside: Tuesday",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 19.510337655231435,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "note_detail",
    "x": 28.462061954580715,
    "y": 654.5121107266435,
    "w": 217.96692392502754,
    "h": 18.320645905420992,
    "text": "Low wind and long sunny intervals.",
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
    "id": "primary",
    "x": 21.0,
    "y": 694.0,
    "w": 364.0,
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
    "y": 694.0,
    "w": 364.0,
    "h": 56.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 169.39319319474987,
    "y": 713.1372549019608,
    "w": 68.78703244684279,
    "h": 20.558246828143023,
    "text": "My cities",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 17.726758757991067,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 21.0,
    "y": 694.0,
    "w": 364.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
