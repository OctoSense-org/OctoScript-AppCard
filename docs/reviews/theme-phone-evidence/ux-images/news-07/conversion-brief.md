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
    "x": 25.158186098633916,
    "y": 32.90657439446367,
    "w": 230.05054304137275,
    "h": 43.38177623990773,
    "text": "Listen today",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 40.8788027061992,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 26.284606368002805,
    "y": 85.26643598615917,
    "w": 270.4557247919725,
    "h": 19.66320645905421,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 16.433528088188023,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "episode",
    "x": 25.0,
    "y": 124.0,
    "w": 355.0,
    "h": 320.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "episode_tag",
    "x": 45.38838554538795,
    "y": 144.78662053056516,
    "w": 119.04079382579933,
    "h": 13.845444059976932,
    "text": "THE DAILY AUDIO",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 13.478254969807994,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "waveform",
    "x": 44,
    "y": 175,
    "w": 316,
    "h": 96,
    "role": "waveform",
    "native_candidates": [
      "LinePlot",
      "AudioWaveform"
    ],
    "data": {
      "path": "data/waveform.json",
      "sha256": "66a8f171c48c203c0c918ad844e4f43d7b1e7f0a0bce5fec923f181001a220f2",
      "origin": "measured_image",
      "approximate": true,
      "x_key": "x",
      "y_keys": [
        "amplitude"
      ],
      "units": {
        "x": "normalized sample position",
        "y": "normalized amplitude"
      },
      "domain": {
        "x": [
          0,
          1
        ],
        "y": [
          -1,
          1
        ]
      }
    }
  },
  {
    "id": "episode_title",
    "x": 44.971225028313896,
    "y": 292.02076124567475,
    "w": 301.2023896037832,
    "h": 36.22145328719723,
    "text": "The world, in focus.",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 34.31593152999476,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "episode_meta",
    "x": 44.98817763937385,
    "y": 339.9054209919262,
    "w": 189.31863285556778,
    "h": 19.215686274509803,
    "text": "A 12-minute morning briefing",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.706514864010119,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "play",
    "x": 44.0,
    "y": 375.0,
    "w": 180.0,
    "h": 47.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "play_surface",
    "x": 44.0,
    "y": 375.0,
    "w": 180.0,
    "h": 47.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "play_label",
    "x": 83.9639256434295,
    "y": 389.5801614763552,
    "w": 102.92613009922822,
    "h": 21.90080738177624,
    "text": "Play episode",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 18.581273957363273,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "play_control",
    "x": 44.0,
    "y": 375.0,
    "w": 180.0,
    "h": 47.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "up_next",
    "x": 25.407744719962647,
    "y": 470.5813148788927,
    "w": 103.14875397685519,
    "h": 32.193771626297575,
    "text": "Up next",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 30.844468103983672,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "next",
    "x": 25.0,
    "y": 509.0,
    "w": 355.0,
    "h": 136.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "next_tag",
    "x": 46.536231969801655,
    "y": 528.3114186851211,
    "w": 56.37265711135612,
    "h": 13.397923875432525,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 12.8656070166349,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "next_title",
    "x": 46.413044506449005,
    "y": 549.7923875432526,
    "w": 195.58544652701212,
    "h": 29.508650519031143,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 26.763174315049067,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "next_title2",
    "x": 46.461225157014695,
    "y": 580.6712802768166,
    "w": 174.54685777287762,
    "h": 28.61361014994233,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 25.280177325517496,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "next_meta",
    "x": 46.650506710022874,
    "y": 615.5778546712803,
    "w": 62.63947078280044,
    "h": 14.292964244521338,
    "text": "4 min read",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 13.5475519105268,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "queue_note",
    "x": 27.38330370544346,
    "y": 668.8327566320646,
    "w": 191.10915104740903,
    "h": 18.768166089965398,
    "text": "New episodes every weekday.",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 15.3295510148247,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 25.0,
    "y": 698.0,
    "w": 355.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 25.0,
    "y": 698.0,
    "w": 355.0,
    "h": 49.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 138.1841633773215,
    "y": 713.1372549019608,
    "w": 129.78390297684675,
    "h": 21.453287197231834,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 18.20903320424391,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 25.0,
    "y": 698.0,
    "w": 355.0,
    "h": 49.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
