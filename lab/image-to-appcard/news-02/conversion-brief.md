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
    "x": 25.145440450240265,
    "y": 45.46451240623197,
    "w": 293.1686879823594,
    "h": 37.58338141950375,
    "text": "Your morning brief",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 34.15033026173966,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 25.498649827835848,
    "y": 92.92902481246394,
    "w": 276.1587651598677,
    "h": 18.77668782458165,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15.463800033082892,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "intro",
    "x": 25.661968014692587,
    "y": 137.7068667051356,
    "w": 272.6716574283772,
    "h": 21.911136757068668,
    "text": "Three stories to start your day.",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18.461000542766296,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 24.0,
    "y": 181.0,
    "w": 358.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_number",
    "x": 24.61648624598533,
    "y": 195.02250432775534,
    "w": 53.23545761442553,
    "h": 38.9267166762839,
    "text": "01",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 47.81411480817476,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 98.49748094087403,
    "y": 195.91806116560878,
    "w": 49.35113012185631,
    "h": 12.955568378534334,
    "text": "DESIGN",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 11.964125270214165,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 98.8190220107854,
    "y": 220.09809578765146,
    "w": 141.86990077177506,
    "h": 25.4933641084824,
    "text": "A quieter city",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 22.276523124580947,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 98.73478023188667,
    "y": 246.96480092325447,
    "w": 246.6152149944873,
    "h": 21.46335833814195,
    "text": "starts with small streets",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 22.707909762866485,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 99.03169690362313,
    "y": 284.5781881130987,
    "w": 68.01102535832415,
    "h": 14.298903635314483,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.47741510870547,
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
    "y": 334.0,
    "w": 358.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_number",
    "x": 24.617983431444003,
    "y": 343.68493941142526,
    "w": 52.87429904658284,
    "h": 38.9267166762839,
    "text": "02",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 47.78217485172307,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 98.34340475952907,
    "y": 345.0282746682054,
    "w": 57.267916207276734,
    "h": 13.40334679746105,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 12.562331533724873,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 98.43877577873778,
    "y": 370.5516445470283,
    "w": 178.12789415656007,
    "h": 25.4933641084824,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 23.07044533237524,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 99.29361330607647,
    "y": 397.4183496826313,
    "w": 163.3561190738699,
    "h": 25.941142527409117,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 22.44528466340353,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 99.03169690362313,
    "y": 435.03173687247545,
    "w": 68.01102535832415,
    "h": 14.298903635314483,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.47741510870547,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2",
    "x": 24.0,
    "y": 487.0,
    "w": 358.0,
    "h": 112.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_2_number",
    "x": 24.617983431444003,
    "y": 494.5862665897288,
    "w": 53.00561011349222,
    "h": 38.9267166762839,
    "text": "03",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 47.78217485172307,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_tag",
    "x": 98.74155029983966,
    "y": 495.92960184650894,
    "w": 60.4013230429989,
    "h": 13.40334679746105,
    "text": "CULTURE",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 12.570531489034092,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_title",
    "x": 99.2604976474327,
    "y": 521.0051933064051,
    "w": 141.42227122381476,
    "h": 25.4933641084824,
    "text": "Why we keep",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 22.974117794453004,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_title2",
    "x": 99.20497696366934,
    "y": 548.3196768609348,
    "w": 232.1190288477583,
    "h": 25.941142527409117,
    "text": "making things by hand",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 22.4340788298222,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_meta",
    "x": 99.07594474154513,
    "y": 585.4852856318522,
    "w": 68.01102535832415,
    "h": 14.298903635314483,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 13.391844219126387,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "edition",
    "x": 26.089169418746142,
    "y": 641.4575879976918,
    "w": 250.6438809261301,
    "h": 16.09001731102135,
    "text": "A considered read, in under 15 minutes.",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 12.889305285253371,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 26.0,
    "y": 691.0,
    "w": 354.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 26.0,
    "y": 691.0,
    "w": 354.0,
    "h": 55.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 140.14296662522494,
    "y": 709.072129255626,
    "w": 128.44101433296584,
    "h": 20.1200230813618,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 16.573196420998478,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 26.0,
    "y": 691.0,
    "w": 354.0,
    "h": 55.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
