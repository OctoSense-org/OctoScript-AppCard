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
    "x": 27.32466456451891,
    "y": 37.38177623990773,
    "w": 214.25325671448698,
    "h": 39.80161476355248,
    "text": "Around you",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 38.08682421654519,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 28.597092583599228,
    "y": 84.81891580161476,
    "w": 243.48180815876515,
    "h": 16.530565167243367,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 13.330388475790816,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead",
    "x": 23.0,
    "y": 116.0,
    "w": 359.0,
    "h": 352.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "lead_art",
    "x": 41.1819184123484,
    "y": 137.83621683967704,
    "w": 323.6361631753032,
    "h": 186.21389195148842,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/lead_art.png",
      "sha256": "f84cc090179343c38691dec969fc74512035e19b6bdc9fad175e1383dce901e5",
      "reference_sha256": "cf35af84e9c0e4d6cff1180bee5f8e65d32c19629aa1eead1e4bdcfdb4bdfa23",
      "method": "source_crop",
      "crop_pixels": [
        92,
        308,
        723,
        416
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Original complex illustration pixels"
    }
  },
  {
    "id": "lead_tag",
    "x": 42.369040362161385,
    "y": 337.2202998846597,
    "w": 147.24145534729877,
    "h": 12.055363321799307,
    "text": "YOUR NEIGHBORHOOD",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 11.126192433424457,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title",
    "x": 41.8869621140181,
    "y": 359.59630911188003,
    "w": 195.58544652701212,
    "h": 38.01153402537486,
    "text": "A quieter city",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 36.182483005717934,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title2",
    "x": 41.81084049676563,
    "y": 392.71280276816606,
    "w": 321.81697905181915,
    "h": 26.3760092272203,
    "text": "starts with small streets",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 30.568318616421177,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_meta",
    "x": 42.204877732810345,
    "y": 437.01730103806227,
    "w": 125.30760749724365,
    "h": 14.740484429065743,
    "text": "The Daily \u00b7 6 min read",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 11.426047264963557,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 24.0,
    "y": 474.0,
    "w": 357.0,
    "h": 111.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 42.126118494031616,
    "y": 488.92964244521335,
    "w": 51.36424167870412,
    "h": 10.712802768166089,
    "text": "SCIENCE",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 9.271827027853716,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 41.96493074024611,
    "y": 508.62053056516726,
    "w": 159.77508269018742,
    "h": 22.79584775086505,
    "text": "The next chapter",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 19.995582713686225,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 41.55737371611127,
    "y": 531.444059976932,
    "w": 144.55567805953692,
    "h": 22.79584775086505,
    "text": "of clean energy",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 19.743537553429675,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 42.106632457556685,
    "y": 560.0853517877739,
    "w": 59.506063947078275,
    "h": 12.502883506343714,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 11.615961074240047,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1",
    "x": 24.0,
    "y": 591.0,
    "w": 357.0,
    "h": 110.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 42.079759358892346,
    "y": 605.7324106113033,
    "w": 51.89636163175303,
    "h": 11.160322952710496,
    "text": "CULTURE",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 9.88994882971063,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 42.48444916891515,
    "y": 625.8708189158016,
    "w": 121.72657111356119,
    "h": 22.348327566320645,
    "text": "Why we keep",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 19.51949741097941,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 42.128744779310146,
    "y": 648.6943483275663,
    "w": 195.13781697905182,
    "h": 22.348327566320645,
    "text": "making things by hand",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 19.273453325967065,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 42.106632457556685,
    "y": 676.4405997693194,
    "w": 59.506063947078275,
    "h": 12.502883506343714,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 11.615961074240047,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 24.0,
    "y": 709.0,
    "w": 358.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 24.0,
    "y": 709.0,
    "w": 358.0,
    "h": 49.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 141.99833392305584,
    "y": 724.7727797001153,
    "w": 126.20286659316427,
    "h": 20.558246828143023,
    "text": "Your reading list",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 17.393116416116623,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 24.0,
    "y": 709.0,
    "w": 358.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
