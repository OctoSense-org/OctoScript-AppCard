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
evidence. Inspect through Makepad's built-in HTTP instrument with a standalone
release binary; hidden windows support automated tests. See
`lab/core/NATIVE-INSTRUMENT.md`. Run semantic, geometry and visual checks;
legacy Studio capture/gate adapters require their own evidence schema.

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
    "id": "clock",
    "x": 28,
    "y": 12.76,
    "w": 60,
    "h": 18.48,
    "text": "9:41",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 14,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "signal",
    "x": 310,
    "y": 13.08,
    "w": 30,
    "h": 15.84,
    "text": "\u2022\u2022\u2022",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 12,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "battery",
    "x": 354,
    "y": 17,
    "w": 23,
    "h": 10,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "battery_tip",
    "x": 378,
    "y": 20,
    "w": 2,
    "h": 4,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "home_indicator",
    "x": 137,
    "y": 762,
    "w": 132,
    "h": 5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back",
    "x": 12,
    "y": 40,
    "w": 84,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_control",
    "x": 12,
    "y": 40,
    "w": 84,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_label",
    "x": 15,
    "y": 49.78,
    "w": 77,
    "h": 22.44,
    "text": "Cancel",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "top_action",
    "x": 314,
    "y": 40,
    "w": 82,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "top_action_control",
    "x": 314,
    "y": 40,
    "w": 82,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "top_action_label",
    "x": 317,
    "y": 51.1,
    "w": 75,
    "h": 19.8,
    "text": "Send",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "compose_title",
    "x": 102,
    "y": 49.78,
    "w": 198,
    "h": 22.44,
    "text": "New Message",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 17,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "to_label",
    "x": 22,
    "y": 114.44,
    "w": 45,
    "h": 21.12,
    "text": "To:",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 16,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "to",
    "x": 70,
    "y": 105,
    "w": 314,
    "h": 40,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "to_input",
    "x": 70,
    "y": 105,
    "w": 314,
    "h": 40,
    "text": "",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "to_rule",
    "x": 20,
    "y": 153,
    "w": 366,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "subject_label",
    "x": 22,
    "y": 172.44,
    "w": 74,
    "h": 21.12,
    "text": "Subject:",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 16,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subject",
    "x": 101,
    "y": 163,
    "w": 283,
    "h": 40,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "subject_input",
    "x": 101,
    "y": 163,
    "w": 283,
    "h": 40,
    "text": "Coffee next week?",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "subject_rule",
    "x": 20,
    "y": 210,
    "w": 366,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "body",
    "x": 23,
    "y": 235,
    "w": 359,
    "h": 360,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "body_input",
    "x": 23,
    "y": 235,
    "w": 359,
    "h": 360,
    "text": "Hi Jamie,\n\nWould you like to grab coffee next week?\n\nBest,",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "save_draft",
    "x": 208,
    "y": 623,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "save_draft_control",
    "x": 208,
    "y": 623,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "save_draft_surface",
    "x": 208,
    "y": 623,
    "w": 178,
    "h": 44,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "save_draft_label",
    "x": 211,
    "y": 635.1,
    "w": 171,
    "h": 19.8,
    "text": "Save Draft",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "send_status_0",
    "x": 26,
    "y": 682.42,
    "w": 354,
    "h": 17.16,
    "text": "Sends with your outgoing mail server",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
