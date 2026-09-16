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
    "id": "details_provider",
    "x": 48.707602339181285,
    "y": 133.1150097465887,
    "w": 310.0974658869396,
    "h": 80.17153996101364,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "clinic_icon_1",
    "x": 68.37231968810916,
    "y": 158.83040935672514,
    "w": 33.278752436647174,
    "h": 31.766081871345026,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/clinic_icon_1.svg",
      "sha256": "aee44823e6d8dcb6ddb99ad40d85b6ffc23aa7f22f28e68b59ab5c7f4a36cce0",
      "method": "reference_svg",
      "reference_sha256": "4f959c862b54b127d429e7dbb6996786fa0c74d9ec9611e2a47f7610553c663e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "provider_name",
    "x": 123.83099356672739,
    "y": 160.5008592310778,
    "w": 118.36323116071972,
    "h": 30.98066935571078,
    "text": "\u5b89\u5fc3\u4f53\u68c0\u4e2d\u5fc3",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 25.092022500811026,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "details_package",
    "x": 48.707602339181285,
    "y": 226.90058479532163,
    "w": 310.0974658869396,
    "h": 80.17153996101364,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "package_icon_2",
    "x": 69.8849902534113,
    "y": 252.61598440545808,
    "w": 28.74074074074074,
    "h": 33.278752436647174,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/package_icon_2.svg",
      "sha256": "bea33ddde09ec253eaa9f98cf68c8b325907c847379ea0b5fb05d5cf33adfa6e",
      "method": "reference_svg",
      "reference_sha256": "4f959c862b54b127d429e7dbb6996786fa0c74d9ec9611e2a47f7610553c663e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "basic_name",
    "x": 123.8843291867493,
    "y": 254.2235630384609,
    "w": 118.2565599110624,
    "h": 30.464406245311043,
    "text": "\u57fa\u7840\u4f53\u68c0\u5957\u9910",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.611897808139272,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "details_options",
    "x": 48.707602339181285,
    "y": 320.68615984405454,
    "w": 310.0974658869396,
    "h": 80.17153996101364,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "tooth_icon_3",
    "x": 68.37231968810916,
    "y": 343.3762183235867,
    "w": 36.304093567251456,
    "h": 36.304093567251456,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/tooth_icon_3.svg",
      "sha256": "4585014506330a6ea301edef04f3c13a0c40c18ec427045080dc322813cbe6ef",
      "method": "reference_svg",
      "reference_sha256": "4f959c862b54b127d429e7dbb6996786fa0c74d9ec9611e2a47f7610553c663e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "optional_note",
    "x": 122.82846003898635,
    "y": 350.93957115009744,
    "w": 205.69785575048732,
    "h": 26.690058479532162,
    "text": "\u53ef\u81ea\u9009\u7259\u79d1\u4e0e\u89c6\u529b\u9879\u76ee",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.101754385964913,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "details_edit",
    "x": 48.707602339181285,
    "y": 414.4717348927875,
    "w": 310.0974658869396,
    "h": 80.17153996101364,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "sliders_icon_4",
    "x": 68.37231968810916,
    "y": 440.1871345029239,
    "w": 34.79142300194932,
    "h": 34.79142300194932,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/sliders_icon_4.svg",
      "sha256": "fb2e9fc8d0fc7a056cfa477e9ce4a17097150be35659a625730ffe74f94a4ec8",
      "method": "reference_svg",
      "reference_sha256": "4f959c862b54b127d429e7dbb6996786fa0c74d9ec9611e2a47f7610553c663e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "edit_note",
    "x": 122.82846003898635,
    "y": 444.7251461988304,
    "w": 210.23586744639374,
    "h": 28.202729044834307,
    "text": "\u9884\u7ea6\u524d\u53ef\u968f\u65f6\u4fee\u6539",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.508538011695908,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "arrange_desktop",
    "x": 53.24561403508772,
    "y": 608.093567251462,
    "w": 301.0214424951267,
    "h": 71.09551656920078,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "arrange_desktop_surface",
    "x": 53.24561403508772,
    "y": 608.093567251462,
    "w": 301.0214424951267,
    "h": 71.09551656920078,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "arrange_desktop_control",
    "x": 53.24561403508772,
    "y": 608.093567251462,
    "w": 301.0214424951267,
    "h": 71.09551656920078,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "arrange_desktop_text",
    "x": 141.96092883574215,
    "y": 632.2079657021143,
    "w": 125.22007016782413,
    "h": 32.996552165708536,
    "text": "\u5728\u684c\u9762\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.966793514108936,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 50.22027290448343,
    "y": 65.0448343079922,
    "w": 21.177387914230017,
    "h": 27.228070175438596,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "f58bea810b249d89bb18d727fbce8550ba48c6264e1175b0f44e016c9fd6ecb9",
      "method": "reference_svg",
      "reference_sha256": "4f959c862b54b127d429e7dbb6996786fa0c74d9ec9611e2a47f7610553c663e",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector tracing of visible source symbol; shape approximation, no raster or text"
    }
  },
  {
    "id": "status_time",
    "x": 62.94164567890637,
    "y": 21.142252244522112,
    "w": 38.93059416356373,
    "h": 19.117459500421937,
    "text": "9:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.0592373353924,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "title",
    "x": 152.69992887823446,
    "y": 64.11907082139965,
    "w": 100.14901430007312,
    "h": 33.220310392755835,
    "text": "\u4f53\u68c0\u8be6\u60c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 27.174888665262923,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
