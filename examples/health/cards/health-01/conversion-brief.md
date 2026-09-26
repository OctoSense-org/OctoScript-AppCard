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
    "x": 26.017543859649123,
    "y": 0.0,
    "w": 353.96491228070175,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_details",
    "x": 50.22027290448343,
    "y": 615.6569200779727,
    "w": 304.046783625731,
    "h": 65.0448343079922,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_details_surface",
    "x": 50.22027290448343,
    "y": 615.6569200779727,
    "w": 304.046783625731,
    "h": 65.0448343079922,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_details_control",
    "x": 50.22027290448343,
    "y": 615.6569200779727,
    "w": 304.046783625731,
    "h": 65.0448343079922,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_details_text",
    "x": 154.34444240262513,
    "y": 635.6564256238672,
    "w": 100.16918754949435,
    "h": 33.28921563752257,
    "text": "\u67e5\u770b\u8be6\u60c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.238970542895988,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "clinic_photo",
    "x": 33.5,
    "y": 110.5,
    "w": 339.0,
    "h": 326.5,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/clinic_photo.png",
      "sha256": "00c1c550ccfedb37d953fa923fa444ddad3f50f21546958e2a3f0aa909a4c61f",
      "method": "source_crop",
      "reference_sha256": "431906c484527746531cb4cc2777454d79c734e413c39a236dad1b1e1f465c37",
      "crop_pixels": [
        67,
        221,
        678,
        653
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Visually inspected empty waiting-room photograph; no UI, text, diagnostics or people"
    }
  },
  {
    "id": "dock",
    "x": 26.017543859649123,
    "y": 701.8791423001949,
    "w": 353.96491228070175,
    "h": 74.12085769980506,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_icon_heart",
    "x": 62.32163742690058,
    "y": 712.46783625731,
    "w": 27.228070175438596,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_heart.svg",
      "sha256": "2b22eedb8ac2a5c9900ec3322b642276bd7df7d765b7a57cdbd7a3cdf2b74bc3",
      "method": "reference_svg",
      "reference_sha256": "431906c484527746531cb4cc2777454d79c734e413c39a236dad1b1e1f465c37",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_icon_calendar",
    "x": 150.05653021442492,
    "y": 712.46783625731,
    "w": 27.228070175438596,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_calendar.svg",
      "sha256": "eb7e019ef6117f168130e94bb240953b38c1f8fd95434029322b0c38ad998550",
      "method": "reference_svg",
      "reference_sha256": "431906c484527746531cb4cc2777454d79c734e413c39a236dad1b1e1f465c37",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_icon_mail",
    "x": 233.25341130604286,
    "y": 712.46783625731,
    "w": 27.228070175438596,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_mail.svg",
      "sha256": "15d753dccafef2720d25c32622d763eec99dd814785def83c52611c446bd8d9f",
      "method": "reference_svg",
      "reference_sha256": "431906c484527746531cb4cc2777454d79c734e413c39a236dad1b1e1f465c37",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_icon_person",
    "x": 314.9376218323587,
    "y": 712.46783625731,
    "w": 27.228070175438596,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_icon_person.svg",
      "sha256": "116613922fc64787b76123a875f9cba58961c066f1d17c9dfaa04f10d0789e6c",
      "method": "reference_svg",
      "reference_sha256": "431906c484527746531cb4cc2777454d79c734e413c39a236dad1b1e1f465c37",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "dock_health",
    "x": 61.00318742801903,
    "y": 743.7568170058678,
    "w": 31.744474176774943,
    "h": 22.1409514005061,
    "text": "\u5065\u5eb7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.871084802470673,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar",
    "x": 147.23661461739164,
    "y": 743.7568170058678,
    "w": 31.74447417677495,
    "h": 22.1409514005061,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.871084802470673,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_mail",
    "x": 229.87698225660807,
    "y": 743.7568169609327,
    "w": 35.33753417016935,
    "h": 22.1409514005061,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.871084802470673,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_profile",
    "x": 316.1104094459806,
    "y": 743.7568169609327,
    "w": 35.33753417016935,
    "h": 22.1409514005061,
    "text": "\u6211\u7684",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.871084802470673,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 175.98108882555522,
    "y": 60.44764672042622,
    "w": 53.30283413714135,
    "h": 33.065953359845565,
    "text": "\u5065\u5eb7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.03133662465638,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "heading",
    "x": 89.74766140990383,
    "y": 470.13079918946346,
    "w": 225.76968496817133,
    "h": 47.84063255122344,
    "text": "\u5e74\u5ea6\u4f53\u68c0\u9080\u8bf7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 40.77178827263781,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "provider_name",
    "x": 132.82755771047277,
    "y": 527.9225542412745,
    "w": 139.60989826046236,
    "h": 36.664275089126015,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 30.377775832887195,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tagline",
    "x": 114.89908249062991,
    "y": 563.8590486165476,
    "w": 179.05991082442432,
    "h": 29.699681150716792,
    "text": "\u4e3a\u81ea\u5df1\u7559\u4e00\u70b9\u65f6\u95f4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.90070347016662,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "status_time",
    "x": 62.32163742690058,
    "y": 19.664717348927873,
    "w": 43.84210526315789,
    "h": 19.126705653021443,
    "text": "9:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.067836257309942,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
