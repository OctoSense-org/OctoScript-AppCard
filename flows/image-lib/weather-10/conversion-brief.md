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
    "x": 19.798951110777338,
    "y": 33.37449509521062,
    "w": 230.0529217199559,
    "h": 38.478938257357186,
    "text": "Outside today",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 36.67972155037999,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 20.43774989777811,
    "y": 83.07789959607616,
    "w": 142.3175303197354,
    "h": 17.881130986728216,
    "text": "Monday, September 7",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.767160624178954,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "comfort",
    "x": 20.0,
    "y": 120.0,
    "w": 366.0,
    "h": 323.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "comfort_kicker",
    "x": 41.394377267253695,
    "y": 146.21465666474322,
    "w": 144.1080485115766,
    "h": 14.7466820542412,
    "text": "OUTDOOR COMFORT",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.84348350033315,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "comfort_score",
    "x": 33.81258822585657,
    "y": 195.47028274668205,
    "w": 189.31863285556778,
    "h": 156.24466243508365,
    "text": "86",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 208.42050044588993,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "weather_symbol",
    "x": 256.0441014332966,
    "y": 215.82919792267742,
    "w": 106.08820286659316,
    "h": 111.01212789415655,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/weather_symbol.svg",
      "sha256": "69fb5be26b0ba24bffa09438eebaeba12783b546a0887919daf790375b14fd4d",
      "reference_sha256": "15454cd1d40ed6b3f8a40f2419eeb2f757f40f6745e2111865b5fee7304ccd1c",
      "method": "reference_svg",
      "crop_pixels": [
        572,
        482,
        237,
        248
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reference-colored vector contours; native SVG paths, no embedded bitmap/text."
    }
  },
  {
    "id": "comfort_label",
    "x": 41.40456916891481,
    "y": 391.1494518176572,
    "w": 292.7210584343991,
    "h": 28.627813040969418,
    "text": "A great day to get outside.",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.86955151362334,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunrise",
    "x": 20.0,
    "y": 460.0,
    "w": 178.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunrise_label",
    "x": 40.52432032444373,
    "y": 482.0484708597807,
    "w": 50.553472987872105,
    "h": 15.194460473167917,
    "text": "Sunrise",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 15.292978788480761,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunrise_value",
    "x": 40.1796855341431,
    "y": 514.736295441431,
    "w": 132.15461895899,
    "h": 30.418926716676282,
    "text": "6:42 AM",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 36.49023027165232,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunset",
    "x": 208.0,
    "y": 460.0,
    "w": 178.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sunset_label",
    "x": 226.30991102536217,
    "y": 482.4962492787074,
    "w": 46.97243660418963,
    "h": 14.7466820542412,
    "text": "Sunset",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.84348350033315,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "sunset_value",
    "x": 225.9629445985419,
    "y": 514.736295441431,
    "w": 122.1742006615215,
    "h": 30.418926716676282,
    "text": "7:28 PM",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 36.49023027165232,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "activity",
    "x": 20.30499432312691,
    "y": 600.7097518753607,
    "w": 285.11135611907383,
    "h": 28.627813040969418,
    "text": "Try a late afternoon walk.",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.199801107414277,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "activity_detail",
    "x": 20.508349254879853,
    "y": 642.800923254472,
    "w": 247.0628445424476,
    "h": 18.77668782458165,
    "text": "24\u00b0 and a gentle breeze in Cupertino.",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.521730908174003,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 20.0,
    "y": 686.0,
    "w": 365.0,
    "h": 62.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 20.0,
    "y": 686.0,
    "w": 365.0,
    "h": 62.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 165.64678049344187,
    "y": 707.728793998846,
    "w": 76.0683572216097,
    "h": 21.46335833814195,
    "text": "My cities",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 18.578040785257397,
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
    "y": 686.0,
    "w": 365.0,
    "h": 62.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
