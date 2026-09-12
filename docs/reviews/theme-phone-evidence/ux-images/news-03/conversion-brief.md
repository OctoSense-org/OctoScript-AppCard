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
    "x": 22.93757225499378,
    "y": 30.221453287197228,
    "w": 216.3722165961168,
    "h": 34.431372549019606,
    "text": "Field Notes",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 39.09877727753585,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 23.835821751689497,
    "y": 74.52595155709342,
    "w": 236.4671114026858,
    "h": 16.08304498269896,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 12.801901771633457,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead",
    "x": 22.0,
    "y": 104.0,
    "w": 362.0,
    "h": 374.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "lead_art",
    "x": 38.04851157662624,
    "y": 126.20069204152249,
    "w": 329.9029768467475,
    "h": 207.70011025358323,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/lead_art.png",
      "sha256": "71aada455bb2a8ba3597605e3554bc4927900ee9144542a3443280bf85cec9fc",
      "reference_sha256": "79804418b2cbad65718916b0e35e58ca0c55fac2d7acdee9af1e7d7307016ec6",
      "method": "source_crop",
      "crop_pixels": [
        85,
        282,
        737,
        464
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Original complex illustration pixels"
    }
  },
  {
    "id": "lead_tag",
    "x": 40.66745244956177,
    "y": 351.9884659746251,
    "w": 120.38368246968025,
    "h": 12.95040369088812,
    "text": "DESIGN & CULTURE",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 11.94164609702858,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title",
    "x": 39.129574015415194,
    "y": 373.916955017301,
    "w": 191.10915104740903,
    "h": 32.193771626297575,
    "text": "A quieter city",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 29.059307645021356,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title2",
    "x": 39.043547692693316,
    "y": 408.37600922722027,
    "w": 324.9557926910073,
    "h": 26.3760092272203,
    "text": "starts with small streets",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 28.93059778872928,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_meta",
    "x": 40.15399297114679,
    "y": 449.1003460207612,
    "w": 129.33627342888644,
    "h": 15.635524798154556,
    "text": "The Daily \u00b7 6 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12.12699989140994,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 22.0,
    "y": 484.0,
    "w": 361.0,
    "h": 104.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 41.01147448067734,
    "y": 498.3275663206459,
    "w": 55.02976846747519,
    "h": 12.95040369088812,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 11.94164609702858,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 40.74295136828677,
    "y": 517.123414071511,
    "w": 163.3561190738699,
    "h": 22.79584775086505,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 20.174998005121395,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 40.79396831504048,
    "y": 539.0519031141869,
    "w": 148.1367144432194,
    "h": 22.79584775086505,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 19.227720376509303,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 40.97756967228235,
    "y": 564.560553633218,
    "w": 59.506063947078275,
    "h": 12.502883506343714,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11.127096115649794,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1",
    "x": 23.0,
    "y": 594.0,
    "w": 360.0,
    "h": 104.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 41.05787889950361,
    "y": 608.4175317185698,
    "w": 57.715545755237045,
    "h": 12.502883506343714,
    "text": "CULTURE",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 11.36677899542554,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 41.15072939125023,
    "y": 627.2133794694348,
    "w": 127.9933847850055,
    "h": 22.348327566320645,
    "text": "Why we keep",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 19.61240858863501,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 40.7822064700167,
    "y": 648.6943483275663,
    "w": 213.21543023302624,
    "h": 22.79584775086505,
    "text": "making things by hand",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 19.218120915512543,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 40.86818245153835,
    "y": 674.2029988465974,
    "w": 59.506063947078275,
    "h": 12.95040369088812,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-300.ttf",
    "size": 11.902874518791473,
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
    "y": 705.0,
    "w": 358.0,
    "h": 46.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 24.0,
    "y": 705.0,
    "w": 358.0,
    "h": 46.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 146.90596048263384,
    "y": 720.7450980392157,
    "w": 115.45975744211687,
    "h": 17.873125720876587,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14.342332900734602,
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
    "y": 705.0,
    "w": 358.0,
    "h": 46.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
