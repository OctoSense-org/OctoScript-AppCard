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
    "text": "Mail Server",
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
    "id": "save_server",
    "x": 320,
    "y": 40,
    "w": 74,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "save_server_control",
    "x": 320,
    "y": 40,
    "w": 74,
    "h": 42,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "save_server_label",
    "x": 323,
    "y": 49.78,
    "w": 67,
    "h": 22.44,
    "text": "Save",
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
    "id": "incoming_heading",
    "x": 24,
    "y": 149.08,
    "w": 358,
    "h": 15.84,
    "text": "INCOMING MAIL \u00b7 POP3",
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
    "id": "incoming_surface",
    "x": 20,
    "y": 178,
    "w": 366,
    "h": 240,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "server_label_address",
    "x": 33,
    "y": 192.76,
    "w": 99,
    "h": 18.48,
    "text": "Email",
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
    "id": "server_address",
    "x": 136,
    "y": 183,
    "w": 237,
    "h": 38,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_address_input",
    "x": 136,
    "y": 183,
    "w": 237,
    "h": 38,
    "text": "you@gmail.com",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_rule_address",
    "x": 33,
    "y": 226,
    "w": 340,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "server_label_username",
    "x": 33,
    "y": 240.76,
    "w": 99,
    "h": 18.48,
    "text": "User Name",
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
    "id": "server_username",
    "x": 136,
    "y": 231,
    "w": 237,
    "h": 38,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_username_input",
    "x": 136,
    "y": 231,
    "w": 237,
    "h": 38,
    "text": "you@gmail.com",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_rule_username",
    "x": 33,
    "y": 274,
    "w": 340,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "server_label_host",
    "x": 33,
    "y": 288.76,
    "w": 99,
    "h": 18.48,
    "text": "Host Name",
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
    "id": "server_host",
    "x": 136,
    "y": 279,
    "w": 237,
    "h": 38,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_host_input",
    "x": 136,
    "y": 279,
    "w": 237,
    "h": 38,
    "text": "pop.gmail.com",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_rule_host",
    "x": 33,
    "y": 322,
    "w": 340,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "server_label_port",
    "x": 33,
    "y": 336.76,
    "w": 99,
    "h": 18.48,
    "text": "Port",
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
    "id": "server_port",
    "x": 136,
    "y": 327,
    "w": 237,
    "h": 38,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_port_input",
    "x": 136,
    "y": 327,
    "w": 237,
    "h": 38,
    "text": "995",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 15,
    "weight": 400,
    "role": "input",
    "native_candidates": [
      "TextInput",
      "KitFormField"
    ]
  },
  {
    "id": "server_rule_port",
    "x": 33,
    "y": 370,
    "w": 340,
    "h": 0.65,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "password_label",
    "x": 33,
    "y": 384.76,
    "w": 99,
    "h": 18.48,
    "text": "Password",
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
    "id": "server_password",
    "x": 138,
    "y": 370,
    "w": 235,
    "h": 48,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "server_password_control",
    "x": 138,
    "y": 370,
    "w": 235,
    "h": 48,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "server_password_label",
    "x": 141,
    "y": 384.76,
    "w": 228,
    "h": 18.48,
    "text": "Set Password",
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
    "id": "security_heading",
    "x": 24,
    "y": 438.08,
    "w": 358,
    "h": 15.84,
    "text": "CONNECTION SECURITY",
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
    "id": "security_surface",
    "x": 20,
    "y": 466,
    "w": 366,
    "h": 36,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "security_tls",
    "x": 22,
    "y": 468,
    "w": 180,
    "h": 32,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "security_tls_control",
    "x": 22,
    "y": 468,
    "w": 180,
    "h": 32,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "security_tls_surface",
    "x": 22,
    "y": 468,
    "w": 180,
    "h": 32,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "security_tls_label",
    "x": 25,
    "y": 474.76,
    "w": 173,
    "h": 18.48,
    "text": "SSL / TLS",
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
    "id": "security_starttls",
    "x": 204,
    "y": 468,
    "w": 180,
    "h": 32,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "security_starttls_control",
    "x": 204,
    "y": 468,
    "w": 180,
    "h": 32,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "security_starttls_label",
    "x": 207,
    "y": 474.76,
    "w": 173,
    "h": 18.48,
    "text": "STARTTLS",
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
    "id": "recent_surface",
    "x": 20,
    "y": 518,
    "w": 366,
    "h": 44,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "recent_label",
    "x": 33,
    "y": 530.1,
    "w": 243,
    "h": 19.8,
    "text": "Gmail recent mode",
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
    "id": "recent_toggle",
    "x": 299,
    "y": 518,
    "w": 76,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "recent_toggle_control",
    "x": 299,
    "y": 518,
    "w": 76,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "recent_toggle_label",
    "x": 302,
    "y": 530.1,
    "w": 69,
    "h": 19.8,
    "text": "On",
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
    "id": "outgoing_settings",
    "x": 24,
    "y": 566,
    "w": 358,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "outgoing_settings_control",
    "x": 24,
    "y": 566,
    "w": 358,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "outgoing_settings_label",
    "x": 27,
    "y": 573.76,
    "w": 351,
    "h": 18.48,
    "text": "Outgoing mail & Gmail sync",
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
    "id": "test_server",
    "x": 20,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "test_server_control",
    "x": 20,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "test_server_surface",
    "x": 20,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "test_server_label",
    "x": 23,
    "y": 620.76,
    "w": 171,
    "h": 18.48,
    "text": "Test Connection",
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
    "id": "sync",
    "x": 208,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sync_control",
    "x": 208,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "sync_surface",
    "x": 208,
    "y": 608,
    "w": 178,
    "h": 44,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "sync_label",
    "x": 211,
    "y": 620.76,
    "w": 171,
    "h": 18.48,
    "text": "Check for Mail",
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
    "id": "use_sample",
    "x": 23,
    "y": 709,
    "w": 175,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "use_sample_control",
    "x": 23,
    "y": 709,
    "w": 175,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "use_sample_label",
    "x": 26,
    "y": 717.42,
    "w": 168,
    "h": 17.16,
    "text": "Use sample mailbox",
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
    "id": "use_gmail",
    "x": 204,
    "y": 709,
    "w": 178,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "use_gmail_control",
    "x": 204,
    "y": 709,
    "w": 178,
    "h": 34,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "use_gmail_label",
    "x": 207,
    "y": 717.42,
    "w": 171,
    "h": 17.16,
    "text": "Open inbox",
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
    "id": "server_status_0",
    "x": 26,
    "y": 663.58,
    "w": 354,
    "h": 15.84,
    "text": "Changes apply when you tap Save.",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 12,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
