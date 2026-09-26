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
    "id": "screen",
    "x": 0.0,
    "y": 1.0,
    "w": 406.0,
    "h": 773.5,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "rsvp_card",
    "x": 24.95901639344262,
    "y": 208.9301075268817,
    "w": 357.74590163934425,
    "h": 410.8698924731182,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_registration",
    "x": 48.25409836065574,
    "y": 538.2913978494623,
    "w": 309.4918032786885,
    "h": 54.89354838709677,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_registration_surface",
    "x": 48.25409836065574,
    "y": 538.2913978494623,
    "w": 309.4918032786885,
    "h": 54.89354838709677,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_registration_control",
    "x": 48.25409836065574,
    "y": 538.2913978494623,
    "w": 309.4918032786885,
    "h": 54.89354838709677,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_78",
    "x": 159.89435498349005,
    "y": 556.6932126543209,
    "w": 91.30433700608033,
    "h": 29.53909098873084,
    "text": "\u67e5\u770b\u62a5\u540d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.985181889857756,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_0",
    "x": 53.24590163934426,
    "y": 238.87204301075266,
    "w": 53.24590163934426,
    "h": 53.23010752688172,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_0.svg",
      "sha256": "069b164f006121b3c09d4420711bcc543d3892e71f8566de5f52c83adfea84b9",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "warning_icon_1",
    "x": 53.24590163934426,
    "y": 475.0806451612903,
    "w": 26.62295081967213,
    "h": 28.278494623655913,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/warning_icon_1.svg",
      "sha256": "e4e325bc63825064c2781b8d5753db0ed0753e089a0a191e8333359242b87136",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_72",
    "x": 127.15522523361419,
    "y": 243.11569493017612,
    "w": 124.04346576136224,
    "h": 27.27270844935667,
    "text": "\u805a\u4f1a \u00b7 \u5df2\u62a5\u540d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.945437604421006,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_73",
    "x": 50.7639196274617,
    "y": 312.895162209623,
    "w": 309.5652017159638,
    "h": 40.610057201751694,
    "text": "\u5468\u516d10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 32.949051481576525,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_74",
    "x": 50.76393044418615,
    "y": 371.11559180579985,
    "w": 200.43475984901525,
    "h": 33.92205372060144,
    "text": "\u4f60\u7684\u65f6\u95f4\u504f\u597d\u5df2\u63d0\u4ea4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.929848348541295,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_75",
    "x": 50.763924106693835,
    "y": 400.22580685956325,
    "w": 178.60868669483645,
    "h": 33.1102138739847,
    "text": "\u738b\u5b81\u6b63\u5728\u786e\u8ba4\u573a\u5730",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.199192486586227,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_77",
    "x": 90.77841834901677,
    "y": 475.84277934862,
    "w": 207.71012602219204,
    "h": 33.92205372060144,
    "text": "\u573a\u5730\u786e\u8ba4\u540e\u518d\u52a0\u5165\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.929848348541295,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 0.0,
    "y": 661.3860215053763,
    "w": 406.0,
    "h": 113.11397849462365,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.278688524590166,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_message.svg",
      "sha256": "94781da8c43a880f37575b7fa2fe3999844efe8aa5d1370e3b505fdf8c7171f6",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.11475409836066,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_calendar.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.95081967213113,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_group.svg",
      "sha256": "a863d3bd8d66ea77c53543b8771a29cc3c5e135065d65081e155ae50be06d57e",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.78688524590166,
    "y": 676.3569892473117,
    "w": 36.60655737704918,
    "h": 38.259139784946235,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "a55d6b3117a99886252fd0de5ba8487754bd95800b2e050040539e070b7b56e5",
      "method": "reference_svg",
      "reference_sha256": "6bea0dbc890ef9df9f85117c3983780072eda736cdbb5a248293a454823f337e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_69",
    "x": 36.213199940517896,
    "y": 13.71328317697582,
    "w": 47.65217167370911,
    "h": 22.99605777638521,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.09645199874669,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_70",
    "x": 133.54787498096178,
    "y": 55.87694124155968,
    "w": 162.18569971656203,
    "h": 70.46688262436035,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 59.820194361924315,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_71",
    "x": 134.4305906213148,
    "y": 130.95631752542533,
    "w": 164.05795434848295,
    "h": 26.393216339073792,
    "text": "10\u670821\u65e5 \u661f\u671f\u4e09",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.15389470516641,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_79",
    "x": 32.57552096625535,
    "y": 727.7157259931934,
    "w": 44.01448858712081,
    "h": 22.193883671240542,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_80",
    "x": 130.79290485084687,
    "y": 727.715726038678,
    "w": 40.37680867120131,
    "h": 22.193883671240542,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_81",
    "x": 232.64797035602567,
    "y": 727.715726038678,
    "w": 40.37680867120131,
    "h": 22.193883671240542,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_82",
    "x": 330.86535495030495,
    "y": 727.715726038678,
    "w": 40.37680867120131,
    "h": 22.193883671240542,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.37449530411649,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
