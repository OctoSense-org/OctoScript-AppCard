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
    "w": 140,
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
    "w": 140,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_icon",
    "x": 22,
    "y": 49.0,
    "w": 10.8,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "back_label",
    "x": 39,
    "y": 49.78,
    "w": 109,
    "h": 22.44,
    "text": "Inbox",
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
    "x": 324,
    "y": 40,
    "w": 68,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "top_action_control",
    "x": 324,
    "y": 40,
    "w": 68,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "top_action_label",
    "x": 327,
    "y": 49.78,
    "w": 61,
    "h": 22.44,
    "text": "Unread",
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
    "id": "reader_scroll",
    "x": 0,
    "y": 88,
    "w": 406,
    "h": 616,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reader_content",
    "x": 0,
    "y": 88,
    "w": 406,
    "h": 613,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "subject_0",
    "x": 22,
    "y": 92.18,
    "w": 364,
    "h": 35.64,
    "text": "Weekend plans",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 27,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "avatar",
    "x": 22,
    "y": 178,
    "w": 44,
    "h": 44,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "initials",
    "x": 22,
    "y": 188.78,
    "w": 44,
    "h": 22.44,
    "text": "AM",
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
    "id": "sender",
    "x": 80,
    "y": 179.28,
    "w": 228,
    "h": 22.44,
    "text": "Alex Morgan",
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
    "id": "recipient",
    "x": 80,
    "y": 205.58,
    "w": 280,
    "h": 15.84,
    "text": "To: you@gmail.com",
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
    "id": "date",
    "x": 292,
    "y": 182.08,
    "w": 90,
    "h": 15.84,
    "text": "9:24 AM",
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
    "id": "message_rule",
    "x": 20,
    "y": 235,
    "w": 366,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "body_0",
    "x": 23,
    "y": 256.1,
    "w": 360,
    "h": 19.8,
    "text": "Hi there,",
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
    "id": "body_1",
    "x": 23,
    "y": 280.1,
    "w": 360,
    "h": 19.8,
    "text": "",
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
    "id": "body_2",
    "x": 23,
    "y": 304.1,
    "w": 360,
    "h": 19.8,
    "text": "Let's meet by the water on Saturday. I found a",
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
    "id": "body_3",
    "x": 23,
    "y": 328.1,
    "w": 360,
    "h": 19.8,
    "text": "quiet spot with great coffee and a view of the",
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
    "id": "body_4",
    "x": 23,
    "y": 352.1,
    "w": 360,
    "h": 19.8,
    "text": "boats.",
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
    "id": "body_5",
    "x": 23,
    "y": 376.1,
    "w": 360,
    "h": 19.8,
    "text": "",
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
    "id": "body_6",
    "x": 23,
    "y": 400.1,
    "w": 360,
    "h": 19.8,
    "text": "How does 10:30 sound?",
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
    "id": "body_7",
    "x": 23,
    "y": 424.1,
    "w": 360,
    "h": 19.8,
    "text": "",
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
    "id": "body_8",
    "x": 23,
    "y": 448.1,
    "w": 360,
    "h": 19.8,
    "text": "See you soon,",
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
    "id": "body_9",
    "x": 23,
    "y": 472.1,
    "w": 360,
    "h": 19.8,
    "text": "Alex",
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
    "id": "reply_primary",
    "x": 22,
    "y": 641,
    "w": 122,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reply_primary_control",
    "x": 22,
    "y": 641,
    "w": 122,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reply_primary_surface",
    "x": 22,
    "y": 641,
    "w": 122,
    "h": 42,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reply_primary_icon",
    "x": 32,
    "y": 650.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "reply_primary_label",
    "x": 62,
    "y": 650.78,
    "w": 78,
    "h": 22.44,
    "text": "Reply",
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
    "id": "toolbar_surface",
    "x": 0,
    "y": 704,
    "w": 406,
    "h": 49,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "toolbar_separator",
    "x": 0,
    "y": 704,
    "w": 406,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "tool_archive",
    "x": 8,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_archive_control",
    "x": 8,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_archive_icon",
    "x": 23.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_flag",
    "x": 74,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_flag_control",
    "x": 74,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_flag_icon",
    "x": 89.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_attachments",
    "x": 140,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_attachments_control",
    "x": 140,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_attachments_icon",
    "x": 155.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_move",
    "x": 206,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_move_control",
    "x": 206,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_move_icon",
    "x": 221.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_reply",
    "x": 272,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_reply_control",
    "x": 272,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_reply_icon",
    "x": 287.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_compose",
    "x": 338,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_compose_control",
    "x": 338,
    "y": 708,
    "w": 54,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_compose_icon",
    "x": 353.0,
    "y": 718.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  }
]
```
