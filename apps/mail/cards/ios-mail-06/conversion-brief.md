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
    "text": "Mailboxes",
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
    "id": "heading",
    "x": 22,
    "y": 91.56,
    "w": 364,
    "h": 44.88,
    "text": "Unread",
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
    "text": "Edit",
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
    "id": "search_surface",
    "x": 20,
    "y": 146,
    "w": 366,
    "h": 40,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "search_icon",
    "x": 31,
    "y": 157,
    "w": 20,
    "h": 20,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "search_field",
    "x": 61,
    "y": 149,
    "w": 278,
    "h": 34,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "search_field_input",
    "x": 61,
    "y": 149,
    "w": 278,
    "h": 34,
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
    "id": "segments",
    "x": 20,
    "y": 198,
    "w": 366,
    "h": 33,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "all_mail",
    "x": 22,
    "y": 200,
    "w": 181,
    "h": 29,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "all_mail_control",
    "x": 22,
    "y": 200,
    "w": 181,
    "h": 29,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "all_mail_label",
    "x": 25,
    "y": 205.26,
    "w": 174,
    "h": 18.48,
    "text": "All Mail",
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
    "id": "unread_mail",
    "x": 204,
    "y": 200,
    "w": 180,
    "h": 29,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "unread_mail_control",
    "x": 204,
    "y": 200,
    "w": 180,
    "h": 29,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "unread_mail_surface",
    "x": 204,
    "y": 200,
    "w": 180,
    "h": 29,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "unread_mail_label",
    "x": 207,
    "y": 205.26,
    "w": 173,
    "h": 18.48,
    "text": "Unread",
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
    "id": "list_scroll",
    "x": 0,
    "y": 242,
    "w": 406,
    "h": 462,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "list_content",
    "x": 0,
    "y": 242,
    "w": 406,
    "h": 462,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_0",
    "x": 0,
    "y": 242,
    "w": 406,
    "h": 88,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_0_open",
    "x": 0,
    "y": 242,
    "w": 406,
    "h": 88,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "message_0_open_control",
    "x": 0,
    "y": 242,
    "w": 406,
    "h": 88,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "message_0_unread",
    "x": 17,
    "y": 260,
    "w": 9,
    "h": 9,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_0_sender",
    "x": 38,
    "y": 251.78,
    "w": 224,
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
    "id": "message_0_time",
    "x": 269,
    "y": 255.08,
    "w": 108,
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
    "id": "message_0_subject",
    "x": 38,
    "y": 276.1,
    "w": 338,
    "h": 19.8,
    "text": "Weekend plans",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 15,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "message_0_preview",
    "x": 38,
    "y": 300.92,
    "w": 338,
    "h": 17.16,
    "text": "Hi there, Let's meet by the water on Saturday. I\u2026",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "message_0_separator",
    "x": 38,
    "y": 329,
    "w": 368,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_1",
    "x": 0,
    "y": 330,
    "w": 406,
    "h": 88,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_1_open",
    "x": 0,
    "y": 330,
    "w": 406,
    "h": 88,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "message_1_open_control",
    "x": 0,
    "y": 330,
    "w": 406,
    "h": 88,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "message_1_unread",
    "x": 17,
    "y": 348,
    "w": 9,
    "h": 9,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "message_1_sender",
    "x": 38,
    "y": 339.78,
    "w": 224,
    "h": 22.44,
    "text": "Studio Team",
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
    "id": "message_1_time",
    "x": 269,
    "y": 343.08,
    "w": 108,
    "h": 15.84,
    "text": "8:40 AM",
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
    "id": "message_1_subject",
    "x": 38,
    "y": 364.1,
    "w": 338,
    "h": 19.8,
    "text": "September design review",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 15,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "message_1_preview",
    "x": 38,
    "y": 388.92,
    "w": 338,
    "h": 17.16,
    "text": "The updated screens are ready for a look. Please\u2026",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "message_1_separator",
    "x": 38,
    "y": 417,
    "w": 368,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "list_footer",
    "x": 22,
    "y": 436.08,
    "w": 362,
    "h": 15.84,
    "text": "All messages loaded",
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
    "id": "tool_filter",
    "x": 14,
    "y": 709,
    "w": 48,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_filter_control",
    "x": 14,
    "y": 709,
    "w": 48,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_filter_icon",
    "x": 26.0,
    "y": 719.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "tool_compose",
    "x": 344,
    "y": 709,
    "w": 48,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_compose_control",
    "x": 344,
    "y": 709,
    "w": 48,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "tool_compose_icon",
    "x": 356.0,
    "y": 719.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "sync_status",
    "x": 72,
    "y": 711.74,
    "w": 262,
    "h": 14.52,
    "text": "Sample mailbox",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "message_count",
    "x": 72,
    "y": 729.74,
    "w": 262,
    "h": 14.52,
    "text": "2 messages",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 11,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
