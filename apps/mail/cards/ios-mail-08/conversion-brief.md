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
    "id": "heading",
    "x": 22,
    "y": 91.56,
    "w": 364,
    "h": 44.88,
    "text": "Today",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 34,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "new_mail_card",
    "x": 20,
    "y": 158,
    "w": 366,
    "h": 405,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "card_mail_icon",
    "x": 40,
    "y": 178,
    "w": 34,
    "h": 34,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "card_service",
    "x": 85,
    "y": 183.12,
    "w": 200,
    "h": 23.76,
    "text": "Mail",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 18,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_time",
    "x": 278,
    "y": 186.08,
    "w": 84,
    "h": 15.84,
    "text": "Just now",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_title",
    "x": 38,
    "y": 229.84,
    "w": 326,
    "h": 34.32,
    "text": "2 new messages",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 26,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_dot_0",
    "x": 39,
    "y": 296,
    "w": 9,
    "h": 9,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "card_sender_0",
    "x": 62,
    "y": 287.94,
    "w": 296,
    "h": 21.12,
    "text": "Alex Morgan",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 16,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_subject_0",
    "x": 62,
    "y": 315.76,
    "w": 296,
    "h": 18.48,
    "text": "Weekend plans",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_dot_1",
    "x": 39,
    "y": 371,
    "w": 9,
    "h": 9,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "card_sender_1",
    "x": 62,
    "y": 362.94,
    "w": 296,
    "h": 21.12,
    "text": "Studio Team",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 16,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_subject_1",
    "x": 62,
    "y": 390.76,
    "w": 296,
    "h": 18.48,
    "text": "September design review",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 14,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "card_rule",
    "x": 20,
    "y": 445,
    "w": 366,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "card_open",
    "x": 24,
    "y": 447,
    "w": 180,
    "h": 57,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "card_open_control",
    "x": 24,
    "y": 447,
    "w": 180,
    "h": 57,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "card_open_label",
    "x": 27,
    "y": 464.28,
    "w": 173,
    "h": 22.44,
    "text": "Open Inbox",
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
    "id": "card_dismiss",
    "x": 205,
    "y": 447,
    "w": 177,
    "h": 57,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "card_dismiss_control",
    "x": 205,
    "y": 447,
    "w": 177,
    "h": 57,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "card_dismiss_label",
    "x": 208,
    "y": 464.28,
    "w": 170,
    "h": 22.44,
    "text": "Dismiss",
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
    "id": "card_source_rule",
    "x": 20,
    "y": 505,
    "w": 366,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "card_source_icon",
    "x": 39,
    "y": 522,
    "w": 21,
    "h": 21,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "card_source",
    "x": 71,
    "y": 524.08,
    "w": 290,
    "h": 15.84,
    "text": "Gmail",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "open_mail",
    "x": 20,
    "y": 676,
    "w": 366,
    "h": 56,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_mail_control",
    "x": 20,
    "y": 676,
    "w": 366,
    "h": 56,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_mail_surface",
    "x": 20,
    "y": 676,
    "w": 366,
    "h": 56,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_mail_icon",
    "x": 30,
    "y": 692.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "open_mail_label",
    "x": 60,
    "y": 692.78,
    "w": 322,
    "h": 22.44,
    "text": "Open Mail",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 17,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
