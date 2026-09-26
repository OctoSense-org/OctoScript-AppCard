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
    "x": 23.866348638642133,
    "y": 39.17185697808535,
    "w": 279.73980154355013,
    "h": 40.24913494809689,
    "text": "The Sunday edit",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 37.62707976366063,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 26.69394909689605,
    "y": 89.74163783160323,
    "w": 230.98144928610273,
    "h": 17.873125720876587,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 14.555410592395106,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead",
    "x": 20.0,
    "y": 133.0,
    "w": 366.0,
    "h": 244.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "lead_tag",
    "x": 44.811335788712704,
    "y": 168.9527104959631,
    "w": 121.89391594311897,
    "h": 12.502883506343714,
    "text": "DESIGN & CULTURE",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 11.640311110288721,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title",
    "x": 45.06179364127965,
    "y": 201.1741637831603,
    "w": 227.36714443219404,
    "h": 40.24913494809689,
    "text": "A quieter city",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 38.09041989415209,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title2",
    "x": 44.3891719744161,
    "y": 257.11418685121106,
    "w": 307.9404630650496,
    "h": 26.823529411764707,
    "text": "starts with small streets",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 30.040223801602906,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_meta",
    "x": 45.73158682333892,
    "y": 319.7670126874279,
    "w": 140.97464167585446,
    "h": 18.768166089965398,
    "text": "The Daily \u00b7 6 min read",
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
    "id": "story_0",
    "x": 24.0,
    "y": 418.0,
    "w": 358.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 45.70738295474258,
    "y": 411.5086505190311,
    "w": 55.4773980154355,
    "h": 12.055363321799307,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 11.02766315711563,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 45.57945699333702,
    "y": 438.8073817762399,
    "w": 192.45203969128997,
    "h": 29.061130334486734,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 26.293644941100837,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 45.27633762141825,
    "y": 473.26643598615914,
    "w": 172.30871003307607,
    "h": 29.061130334486734,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 25.739816913254177,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 45.69513725512425,
    "y": 511.75317185697804,
    "w": 59.953693495038586,
    "h": 13.397923875432525,
    "text": "4 min read",
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
    "id": "story_1",
    "x": 24.0,
    "y": 542.0,
    "w": 358.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 45.643077076735615,
    "y": 559.1903114186852,
    "w": 59.10052536667154,
    "h": 12.055363321799307,
    "text": "CULTURE",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 11.020296648660642,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 45.70910568765611,
    "y": 586.0415224913495,
    "w": 146.34619625137816,
    "h": 26.3760092272203,
    "text": "Why we keep",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 23.214826189132307,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 45.692548075249675,
    "y": 616.9204152249134,
    "w": 232.73869900771774,
    "h": 27.271049596309112,
    "text": "making things by hand",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 24.1434192366976,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 45.80097750442525,
    "y": 653.6170703575548,
    "w": 58.61080485115766,
    "h": 12.95040369088812,
    "text": "4 min read",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 11.780479922197216,
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
    "y": 692.0,
    "w": 366.0,
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
    "w": 366.0,
    "h": 56.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 140.32646040403856,
    "y": 710.4521337946943,
    "w": 127.0981256890849,
    "h": 22.79584775086505,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 19.55990660252623,
    "weight": 300,
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
    "w": 366.0,
    "h": 56.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
