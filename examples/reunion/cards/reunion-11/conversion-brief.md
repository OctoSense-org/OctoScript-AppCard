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
    "y": 8.5,
    "w": 406.0,
    "h": 759.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "payment_receipt",
    "x": 23.295081967213115,
    "y": 55.10526315789474,
    "w": 361.07377049180326,
    "h": 422.7763157894737,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "view_reunion",
    "x": 48.25409836065574,
    "y": 406.3092105263158,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_reunion_surface",
    "x": 48.25409836065574,
    "y": 406.3092105263158,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_reunion_control",
    "x": 48.25409836065574,
    "y": 406.3092105263158,
    "w": 309.4918032786885,
    "h": 54.92763157894737,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_139",
    "x": 140.48073170851413,
    "y": 420.50922430256657,
    "w": 127.94549385715065,
    "h": 34.27266947092583,
    "text": "\u67e5\u770b\u805a\u4f1a\u8be6\u60c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.245402523833246,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "check_icon_0",
    "x": 48.25409836065574,
    "y": 78.40789473684211,
    "w": 49.91803278688524,
    "h": 49.93421052631579,
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
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_129",
    "x": 111.51145619328535,
    "y": 89.74712265178682,
    "w": 124.04346576136224,
    "h": 29.729021241030104,
    "text": "\u652f\u4ed8 \u00b7 \u5df2\u5b8c\u6210",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.156119116927094,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_130",
    "x": 38.757839264192356,
    "y": 143.75340720574002,
    "w": 160.42027126189444,
    "h": 30.613895296008923,
    "text": "2016\u5c4a\u540c\u5b66\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.95250576640803,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_131",
    "x": 42.22763106521341,
    "y": 187.25800200445832,
    "w": 208.04589986082232,
    "h": 49.28662818449028,
    "text": "\u00a5180\u5df2\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 40.757965366041255,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_132",
    "x": 46.03319932707111,
    "y": 253.53572571947433,
    "w": 62.20289133738682,
    "h": 25.90424112514919,
    "text": "\u6536\u6b3e\u4eba",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.713817012634273,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_133",
    "x": 46.0332003775183,
    "y": 286.36307597921876,
    "w": 47.65216850304031,
    "h": 26.06380822661764,
    "text": "\u7528\u9014",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.857427403955874,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_134",
    "x": 42.3955175175165,
    "y": 322.7734379082039,
    "w": 47.652171673709205,
    "h": 33.12828829317295,
    "text": "\u51ed\u8bc1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.215459463855655,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_135",
    "x": 46.03320089279528,
    "y": 366.46587233527,
    "w": 138.59418542503985,
    "h": 25.846216219879782,
    "text": "\u652f\u4ed8\u8bb0\u5f55\u5df2\u4fdd\u5b58",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.661594597891803,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_136",
    "x": 133.33754083218977,
    "y": 253.53572549535332,
    "w": 44.01448858712062,
    "h": 29.545277954951686,
    "text": "\u738b\u5b81",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.990750159456518,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_137",
    "x": 136.9752217165563,
    "y": 286.3630752836847,
    "w": 171.33332052165966,
    "h": 26.06380901977355,
    "text": "2016\u5c4a\u540c\u5b66\u805a\u4f1a\u9910\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.857428117796196,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_138",
    "x": 136.9752229477331,
    "y": 326.4144739165812,
    "w": 174.97100360824803,
    "h": 22.606517062360737,
    "text": "REU-20261024-001",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.745865356124664,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "confirmed_summary",
    "x": 23.295081967213115,
    "y": 489.5328947368421,
    "w": 361.07377049180326,
    "h": 144.80921052631578,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "calendar_icon_1",
    "x": 46.59016393442623,
    "y": 506.1776315789474,
    "w": 29.950819672131146,
    "h": 29.960526315789473,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_1.svg",
      "sha256": "267a117ea0a845aaab47937fbf902f76e448fe8840980d1602126f726e265098",
      "method": "reference_svg",
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_2",
    "x": 49.91803278688524,
    "y": 552.7828947368421,
    "w": 19.9672131147541,
    "h": 21.638157894736842,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/pin_icon_2.svg",
      "sha256": "2bf55d3cae2ca238d7cf5c17c98856c017509e3c05ad30cc2786bb71177e8dc1",
      "method": "reference_svg",
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "pin_icon_3",
    "x": 49.91803278688524,
    "y": 591.0657894736842,
    "w": 19.9672131147541,
    "h": 21.638157894736842,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/pin_icon_3.svg",
      "sha256": "2bf55d3cae2ca238d7cf5c17c98856c017509e3c05ad30cc2786bb71177e8dc1",
      "method": "reference_svg",
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_140",
    "x": 96.87802635034058,
    "y": 511.68611325655667,
    "w": 113.29583664049235,
    "h": 26.68862867441569,
    "text": "\u805a\u4f1a \u00b7 \u5df2\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.41976580697412,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_141",
    "x": 96.9607371844324,
    "y": 552.158717365903,
    "w": 182.24635709874906,
    "h": 26.407120200475767,
    "text": "\u5468\u516d 10\u670824\u65e5 18:30",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.166408180428192,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_142",
    "x": 96.96073822680593,
    "y": 587.8727851037105,
    "w": 178.60867401216086,
    "h": 27.287158384007807,
    "text": "\u6728\u5149\u9910\u5385 \u00b7 \u6842\u82b1\u8def8\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
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
    "y": 657.6447368421053,
    "w": 406.0,
    "h": 109.85526315789474,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_message",
    "x": 33.278688524590166,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_calendar",
    "x": 133.11475409836066,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_group",
    "x": 232.95081967213113,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "dock_wallet",
    "x": 332.78688524590166,
    "y": 672.625,
    "w": 36.60655737704918,
    "h": 38.2828947368421,
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
      "reference_sha256": "628520310c71b8b81259619bac2f3aab3a0984948e7422e8283d24451db2a5b7",
      "fit": "stretch",
      "clip": true,
      "notes": "Native SVG reconstruction of a reviewed line symbol; no embedded raster or text"
    }
  },
  {
    "id": "text_128",
    "x": 31.482474130376485,
    "y": 20.56743476148777,
    "w": 51.28985158962852,
    "h": 22.39376013391403,
    "text": "10:12",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.554384120522627,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_143",
    "x": 31.482474556695397,
    "y": 722.6056303116322,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u6d88\u606f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_144",
    "x": 129.69986006039488,
    "y": 722.6056299475277,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_145",
    "x": 231.5549255655735,
    "y": 722.6056299475277,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u805a\u4f1a",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_148",
    "x": 326.1346289154995,
    "y": 722.6056297654761,
    "w": 40.37680867120131,
    "h": 27.287158384007807,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.958442545607028,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
