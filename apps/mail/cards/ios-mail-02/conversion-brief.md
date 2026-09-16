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
    "text": "Mailboxes",
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
    "id": "folders_surface",
    "x": 20,
    "y": 158,
    "w": 366,
    "h": 318,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_0",
    "x": 26,
    "y": 159,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_0_control",
    "x": 26,
    "y": 159,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_0_icon",
    "x": 36,
    "y": 173.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_0_label",
    "x": 66,
    "y": 173.78,
    "w": 306,
    "h": 22.44,
    "text": "Sent",
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
    "id": "folder_count_0",
    "x": 305,
    "y": 174.44,
    "w": 30,
    "h": 21.12,
    "text": "",
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
    "id": "folder_arrow_0",
    "x": 350,
    "y": 176,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_line_0",
    "x": 68,
    "y": 211,
    "w": 318,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_1",
    "x": 26,
    "y": 212,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_1_control",
    "x": 26,
    "y": 212,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_1_icon",
    "x": 36,
    "y": 226.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_1_label",
    "x": 66,
    "y": 226.78,
    "w": 306,
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
    "id": "folder_count_1",
    "x": 305,
    "y": 227.44,
    "w": 30,
    "h": 21.12,
    "text": "5",
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
    "id": "folder_arrow_1",
    "x": 350,
    "y": 229,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_line_1",
    "x": 68,
    "y": 264,
    "w": 318,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_2",
    "x": 26,
    "y": 265,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_2_control",
    "x": 26,
    "y": 265,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_2_icon",
    "x": 36,
    "y": 279.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_2_label",
    "x": 66,
    "y": 279.78,
    "w": 306,
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
    "id": "folder_count_2",
    "x": 305,
    "y": 280.44,
    "w": 30,
    "h": 21.12,
    "text": "2",
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
    "id": "folder_arrow_2",
    "x": 350,
    "y": 282,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_line_2",
    "x": 68,
    "y": 317,
    "w": 318,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_3",
    "x": 26,
    "y": 318,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_3_control",
    "x": 26,
    "y": 318,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_3_icon",
    "x": 36,
    "y": 332.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_3_label",
    "x": 66,
    "y": 332.78,
    "w": 306,
    "h": 22.44,
    "text": "Flagged",
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
    "id": "folder_count_3",
    "x": 305,
    "y": 333.44,
    "w": 30,
    "h": 21.12,
    "text": "1",
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
    "id": "folder_arrow_3",
    "x": 350,
    "y": 335,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_line_3",
    "x": 68,
    "y": 370,
    "w": 318,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_4",
    "x": 26,
    "y": 371,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_4_control",
    "x": 26,
    "y": 371,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_4_icon",
    "x": 36,
    "y": 385.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_4_label",
    "x": 66,
    "y": 385.78,
    "w": 306,
    "h": 22.44,
    "text": "Drafts",
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
    "id": "folder_count_4",
    "x": 305,
    "y": 386.44,
    "w": 30,
    "h": 21.12,
    "text": "1",
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
    "id": "folder_arrow_4",
    "x": 350,
    "y": 388,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_line_4",
    "x": 68,
    "y": 423,
    "w": 318,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "folder_5",
    "x": 26,
    "y": 424,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_5_control",
    "x": 26,
    "y": 424,
    "w": 350,
    "h": 52,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "folder_5_icon",
    "x": 36,
    "y": 438.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "folder_5_label",
    "x": 66,
    "y": 438.78,
    "w": 306,
    "h": 22.44,
    "text": "Archive",
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
    "id": "folder_count_5",
    "x": 305,
    "y": 439.44,
    "w": 30,
    "h": 21.12,
    "text": "",
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
    "id": "folder_arrow_5",
    "x": 350,
    "y": 441,
    "w": 7.65,
    "h": 17,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "account_surface",
    "x": 20,
    "y": 496,
    "w": 366,
    "h": 76,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "account_open",
    "x": 20,
    "y": 496,
    "w": 366,
    "h": 76,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "account_open_control",
    "x": 20,
    "y": 496,
    "w": 366,
    "h": 76,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "gmail_icon",
    "x": 34,
    "y": 518,
    "w": 30,
    "h": 30,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "account_name",
    "x": 80,
    "y": 506.28,
    "w": 160,
    "h": 22.44,
    "text": "Gmail",
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
    "id": "account_address",
    "x": 80,
    "y": 535.08,
    "w": 245,
    "h": 15.84,
    "text": "you@gmail.com",
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
    "id": "account_status",
    "x": 284,
    "y": 514.58,
    "w": 88,
    "h": 15.84,
    "text": "Sample",
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
    "id": "settings",
    "x": 20,
    "y": 590,
    "w": 366,
    "h": 56,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "settings_control",
    "x": 20,
    "y": 590,
    "w": 366,
    "h": 56,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "settings_surface",
    "x": 20,
    "y": 590,
    "w": 366,
    "h": 56,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "settings_icon",
    "x": 30,
    "y": 606.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "settings_label",
    "x": 60,
    "y": 606.78,
    "w": 322,
    "h": 22.44,
    "text": "Settings",
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
    "id": "new_mail_card",
    "x": 20,
    "y": 659,
    "w": 240,
    "h": 40,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "new_mail_card_control",
    "x": 20,
    "y": 659,
    "w": 240,
    "h": 40,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "new_mail_card_icon",
    "x": 30,
    "y": 667.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "new_mail_card_label",
    "x": 60,
    "y": 667.78,
    "w": 196,
    "h": 22.44,
    "text": "New Mail card",
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
    "id": "gmail_folders",
    "x": 20,
    "y": 709,
    "w": 280,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "gmail_folders_control",
    "x": 20,
    "y": 709,
    "w": 280,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "gmail_folders_icon",
    "x": 30,
    "y": 719.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  },
  {
    "id": "gmail_folders_label",
    "x": 60,
    "y": 719.78,
    "w": 236,
    "h": 22.44,
    "text": "Gmail folders",
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
    "id": "compose",
    "x": 338,
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
    "id": "compose_control",
    "x": 338,
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
    "id": "compose_icon",
    "x": 350.0,
    "y": 719.0,
    "w": 24,
    "h": 24,
    "role": "unknown",
    "native_candidates": []
  }
]
```
