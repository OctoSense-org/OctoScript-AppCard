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
    "x": 21.848838007214038,
    "y": 27.536332179930795,
    "w": 173.20396912899668,
    "h": 42.03921568627451,
    "text": "The Daily",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 38.99114801075585,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 23.38819220372919,
    "y": 75.42099192618224,
    "w": 229.6052921719956,
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
    "x": 19.0,
    "y": 105.0,
    "w": 368.0,
    "h": 360.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "lead_art",
    "x": 38.943770672546854,
    "y": 127.99077277970011,
    "w": 328.1124586549063,
    "h": 188.00441014332964,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/lead_art.png",
      "sha256": "438d5a388c6850e81c2cc2a6eda4738438b80393225b1bddd001af247d0a43cc",
      "reference_sha256": "1d30f2d3042e6f572bebc6d99531ef4ccbbc5b8dc9180db100096ec96d1a9608",
      "method": "source_crop",
      "crop_pixels": [
        87,
        286,
        733,
        420
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Original complex illustration pixels"
    }
  },
  {
    "id": "lead_tag",
    "x": 40.99857955390145,
    "y": 330.50749711649365,
    "w": 112.62811169019356,
    "h": 11.160322952710496,
    "text": "DESIGN & CULTURE",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 9.572024417200454,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title",
    "x": 39.51839393455225,
    "y": 355.12110726643596,
    "w": 201.40463065049613,
    "h": 35.32641291810842,
    "text": "A quieter city",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 32.110357185328354,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_title2",
    "x": 40.06508322155941,
    "y": 392.2652825836217,
    "w": 330.76957001102534,
    "h": 26.823529411764707,
    "text": "starts with small streets",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 29.324082958151894,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "lead_meta",
    "x": 42.01146838143895,
    "y": 437.01730103806227,
    "w": 113.66923925027562,
    "h": 14.292964244521338,
    "text": "The Daily \u00b7 6 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 10.727730673170331,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 19.0,
    "y": 473.0,
    "w": 368.0,
    "h": 116.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 41.60571951868049,
    "y": 488.03460207612454,
    "w": 50.105843439911794,
    "h": 11.607843137254902,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 10.16364171239272,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 41.76557076829943,
    "y": 510.8581314878893,
    "w": 147.6890848952591,
    "h": 21.453287197231834,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18.733926719041296,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 42.17664646583894,
    "y": 534.1291810841984,
    "w": 132.9173098125689,
    "h": 21.90080738177624,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18.312114644294574,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 42.42340225637796,
    "y": 564.560553633218,
    "w": 52.791620727673646,
    "h": 11.160322952710496,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 9.370186202652457,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1",
    "x": 19.0,
    "y": 593.0,
    "w": 368.0,
    "h": 116.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 42.5328086763289,
    "y": 608.8650519031141,
    "w": 54.62152132714648,
    "h": 11.160322952710496,
    "text": "CULTURE",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 9.578276555944543,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 42.516975038499865,
    "y": 631.6885813148789,
    "w": 118.14553472987872,
    "h": 21.453287197231834,
    "text": "Why we keep",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18.655705730652816,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 42.603557305625856,
    "y": 654.5121107266435,
    "w": 192.45203969128997,
    "h": 22.348327566320645,
    "text": "making things by hand",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18.76054660800034,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 42.87103180433827,
    "y": 685.3910034602076,
    "w": 52.34399117971334,
    "h": 11.160322952710496,
    "text": "4 min read",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 9.370186202652457,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 19.0,
    "y": 717.0,
    "w": 368.0,
    "h": 42.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 19.0,
    "y": 717.0,
    "w": 368.0,
    "h": 42.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 142.3928099713205,
    "y": 730.1430219146482,
    "w": 126.65049614112458,
    "h": 19.66320645905421,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 16.10353756432883,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 19.0,
    "y": 717.0,
    "w": 368.0,
    "h": 42.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
