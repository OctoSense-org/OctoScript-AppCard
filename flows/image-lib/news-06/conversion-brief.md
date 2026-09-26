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
    "x": 20.334732146875773,
    "y": 29.773933102652826,
    "w": 227.48640840945603,
    "h": 30.85121107266436,
    "text": "News timeline",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 36.68198233970541,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 22.255057434327227,
    "y": 73.1833910034602,
    "w": 244.37706725468576,
    "h": 16.978085351787776,
    "text": "Independent stories. Fresh perspectives.",
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
    "id": "timeline_label",
    "x": 22.488931130021378,
    "y": 116.14532871972318,
    "w": 147.24145534729877,
    "h": 15.18800461361015,
    "text": "TODAY / SEPTEMBER 7",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 12.599104294606025,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "time_0",
    "x": 22.66479591009771,
    "y": 150.15686274509804,
    "w": 41.60088202866593,
    "h": 13.845444059976932,
    "text": "09:42",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 13.598679640852117,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 22.0,
    "y": 170.0,
    "w": 362.0,
    "h": 145.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 39.97770777891523,
    "y": 188.64359861591694,
    "w": 46.19963856957795,
    "h": 12.055363321799307,
    "text": "DESIGN",
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
    "id": "story_0_title",
    "x": 39.593479115686655,
    "y": 211.91464821222607,
    "w": 159.77508269018742,
    "h": 29.061130334486734,
    "text": "A quieter city",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.66077695158163,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 39.658284049090064,
    "y": 244.1361014994233,
    "w": 273.02535832414554,
    "h": 23.690888119953865,
    "text": "starts with small streets",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.900120382450634,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 39.80245714954367,
    "y": 283.0703575547866,
    "w": 65.32524807056228,
    "h": 13.845444059976932,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.450060191225317,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "time_1",
    "x": 22.66479591009771,
    "y": 334.5351787773933,
    "w": 42.49614112458655,
    "h": 13.845444059976932,
    "text": "08:30",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 13.598679640852117,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1",
    "x": 22.0,
    "y": 355.0,
    "w": 362.0,
    "h": 146.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 40.22928335227099,
    "y": 373.0219146482122,
    "w": 53.23925027563396,
    "h": 12.502883506343714,
    "text": "SCIENCE",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 11.744314235281374,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 39.57967264190816,
    "y": 397.63552479815456,
    "w": 200.50937155457552,
    "h": 28.61361014994233,
    "text": "The next chapter",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 26.184691648874818,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 39.421343617085014,
    "y": 430.7520184544406,
    "w": 182.15656008820287,
    "h": 29.508650519031143,
    "text": "of clean energy",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.79480096536885,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 39.824466338947495,
    "y": 469.2387543252595,
    "w": 64.87761852260198,
    "h": 13.397923875432525,
    "text": "4 min read",
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
    "id": "time_2",
    "x": 22.66479591009771,
    "y": 518.9134948096886,
    "w": 37.57221609702315,
    "h": 13.845444059976932,
    "text": "07:15",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 13.598679640852117,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2",
    "x": 22.0,
    "y": 539.0,
    "w": 362.0,
    "h": 143.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_2_tag",
    "x": 39.78598065692368,
    "y": 557.4002306805074,
    "w": 54.13450937155457,
    "h": 12.055363321799307,
    "text": "CULTURE",
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
    "id": "story_2_title",
    "x": 39.64394415777358,
    "y": 581.5663206459054,
    "w": 156.64167585446526,
    "h": 28.166089965397923,
    "text": "Why we keep",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 25.708606346168004,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_title2",
    "x": 39.501367299169566,
    "y": 613.3402537485582,
    "w": 253.77728776185225,
    "h": 28.61361014994233,
    "text": "making things by hand",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 25.854632510443622,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_meta",
    "x": 39.80245714954367,
    "y": 650.4844290657439,
    "w": 65.32524807056228,
    "h": 13.845444059976932,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.450060191225317,
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
    "y": 699.0,
    "w": 361.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 22.0,
    "y": 699.0,
    "w": 361.0,
    "h": 54.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 142.44596347101614,
    "y": 717.1649365628605,
    "w": 123.51708930540242,
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
    "x": 22.0,
    "y": 699.0,
    "w": 361.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
