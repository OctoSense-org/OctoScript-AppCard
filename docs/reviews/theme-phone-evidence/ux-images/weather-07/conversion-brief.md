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
    "x": 24.034688993264975,
    "y": 30.687824581650318,
    "w": 197.19827842372487,
    "h": 33.10559723023658,
    "text": "Rain watch",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 39.76174485004998,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 24.94786693881077,
    "y": 81.73456433929601,
    "w": 146.34619625137816,
    "h": 17.4333525678015,
    "text": "Monday, September 7",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.290800604044149,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "location",
    "x": 24.954535979092658,
    "y": 117.55683785343335,
    "w": 106.07160698763336,
    "h": 24.597807270628966,
    "text": "Cupertino",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 21.912560926201028,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "radar",
    "x": 25.0,
    "y": 151.0,
    "w": 355.0,
    "h": 339.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "rain_radar",
    "x": 47.00110253583241,
    "y": 164.78245816503173,
    "w": 311.99779492833517,
    "h": 314.2359426681367,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/rain_radar.png",
      "sha256": "524dab3707b58995c2456a36bef9b5419138c89e18fe2e2810c821feea7dec12",
      "reference_sha256": "5afe6ba275c2b322435a93e42f05a09c6cafb62ff284ddde8ec6c24b0c5a8de0",
      "method": "source_crop",
      "crop_pixels": [
        105,
        368,
        697,
        702
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Original complex illustration pixels"
    }
  },
  {
    "id": "rain_headline",
    "x": 24.599305770135683,
    "y": 508.467397576457,
    "w": 270.4104722125876,
    "h": 27.284477784189267,
    "text": "Rain in 35 minutes",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 31.809395880039983,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "rain_note",
    "x": 25.514201657861857,
    "y": 548.3196768609348,
    "w": 229.15766262403528,
    "h": 16.537795729948066,
    "text": "A short shower, then clearer skies.",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.943737461201511,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chance",
    "x": 22.0,
    "y": 577.0,
    "w": 176.0,
    "h": 103.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "chance_label",
    "x": 43.3647136865786,
    "y": 593.9930755914598,
    "w": 71.5920617420066,
    "h": 13.40334679746105,
    "text": "Rain chance",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.846102182323838,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "chance_value",
    "x": 43.264482530960066,
    "y": 620.4120023081362,
    "w": 98.11179263600292,
    "h": 38.478938257357186,
    "text": "80%",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 47.1380944933695,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity",
    "x": 206.0,
    "y": 577.0,
    "w": 177.0,
    "h": 103.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "humidity_label",
    "x": 231.40321871266084,
    "y": 593.9930755914598,
    "w": 54.13450937155457,
    "h": 15.642238892094634,
    "text": "Humidity",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.38536052350493,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "humidity_value",
    "x": 229.1561414146227,
    "y": 620.4120023081362,
    "w": 92.55214334027741,
    "h": 38.478938257357186,
    "text": "64%",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 47.1380944933695,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 51.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 51.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 164.75152139752126,
    "y": 711.7587997691863,
    "w": 78.30650496141124,
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
    "x": 25.0,
    "y": 696.0,
    "w": 356.0,
    "h": 51.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
