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
    "x": 18.0,
    "y": 0.0,
    "w": 370.0,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "order_product",
    "x": 32.313346228239844,
    "y": 152.47970479704796,
    "w": 339.94197292069634,
    "h": 136.01476014760146,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "product_photo",
    "x": 47.5,
    "y": 179.5,
    "w": 89.5,
    "h": 87.5,
    "role": "photo",
    "native_candidates": [
      "Image"
    ],
    "asset": {
      "path": "assets/product_photo.png",
      "sha256": "6edcc850bc03a210ed4f7c620e56bd634f7f0f92bf4a33d3a6082a2180c5ad52",
      "method": "source_crop",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "crop_pixels": [
        95,
        359,
        179,
        175
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Artwork-only source region; product photography or technician portrait, visually reviewed"
    }
  },
  {
    "id": "text_48",
    "x": 146.97456348980177,
    "y": 192.91159957861913,
    "w": 121.61764166295183,
    "h": 25.788231740578563,
    "text": "1.5\u5339\u53d8\u9891\u7a7a\u8c03",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.263055518738064,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_49",
    "x": 294.3194493634483,
    "y": 243.3615384284558,
    "w": 67.67955259105456,
    "h": 21.97991834971318,
    "text": "\u00a52,799",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.721324065233258,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "order_details",
    "x": 32.313346228239844,
    "y": 289.21033210332104,
    "w": 339.94197292069634,
    "h": 211.18081180811808,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "divider_0",
    "x": 49.48936170212766,
    "y": 377.26199261992616,
    "w": 304.1586073500967,
    "h": 0.7158671586715867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "divider_1",
    "x": 49.48936170212766,
    "y": 435.9630996309963,
    "w": 304.1586073500967,
    "h": 0.7158671586715867,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "person_icon_2",
    "x": 53.06769825918762,
    "y": 308.53874538745384,
    "w": 22.901353965183752,
    "h": 23.62361623616236,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/person_icon_2.svg",
      "sha256": "045769d021ded6d01598f0dec76dc1e1c2d35e5cee0209d8bd466d6669ef3727",
      "method": "reference_svg",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 53.06769825918762,
    "y": 395.15867158671585,
    "w": 25.04835589941973,
    "h": 24.339483394833948,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "ae776c61fe98dc0aee57fc63b1343360e4030e6cc97db9fa23eca69d129b3b1d",
      "method": "reference_svg",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "wrench_icon_4",
    "x": 52.35203094777563,
    "y": 454.57564575645756,
    "w": 25.04835589941973,
    "h": 24.339483394833948,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_4.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_50",
    "x": 93.09416272413817,
    "y": 311.40221390316776,
    "w": 38.93308719952281,
    "h": 22.612546125461233,
    "text": "Alex",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.309667896678945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_51",
    "x": 93.09416550453307,
    "y": 344.0490859089764,
    "w": 121.5791806602847,
    "h": 22.179696691871946,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.90711792344091,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_53",
    "x": 93.09416632697615,
    "y": 401.5848277662805,
    "w": 211.41189592903768,
    "h": 21.979919715121163,
    "text": "\u5468\u4e94 9\u670818\u65e5 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.721325335062684,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_54",
    "x": 93.14506769825918,
    "y": 455.29151291512915,
    "w": 126.09477756286266,
    "h": 25.4760147601476,
    "text": "\u5230\u8d27\u540e\u9884\u7ea6\u5b89\u88c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.97269372693727,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "divider_2",
    "x": 50.20502901353965,
    "y": 531.8892988929889,
    "w": 1.4313346228239845,
    "h": 99.50553505535055,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back",
    "x": 32.313346228239844,
    "y": 47.96309963099631,
    "w": 28.626692456479688,
    "h": 37.22509225092251,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "back_surface",
    "x": 32.313346228239844,
    "y": 47.96309963099631,
    "w": 28.626692456479688,
    "h": 37.22509225092251,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "back_control",
    "x": 32.313346228239844,
    "y": 47.96309963099631,
    "w": 28.626692456479688,
    "h": 37.22509225092251,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_logistics",
    "x": 36.6073500967118,
    "y": 693.6752767527674,
    "w": 151.72147001934235,
    "h": 52.25830258302583,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_logistics_surface",
    "x": 36.6073500967118,
    "y": 693.6752767527674,
    "w": 151.72147001934235,
    "h": 52.25830258302583,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_logistics_control",
    "x": 36.6073500967118,
    "y": 693.6752767527674,
    "w": 151.72147001934235,
    "h": 52.25830258302583,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_61",
    "x": 71.4517216951702,
    "y": 706.9369294761832,
    "w": 82.21796994236963,
    "h": 26.188957214355458,
    "text": "\u67e5\u770b\u7269\u6d41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.635730209350577,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "support",
    "x": 217.67117988394583,
    "y": 693.6752767527674,
    "w": 149.5744680851064,
    "h": 51.54243542435424,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "support_surface",
    "x": 217.67117988394583,
    "y": 693.6752767527674,
    "w": 149.5744680851064,
    "h": 51.54243542435424,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "support_control",
    "x": 217.67117988394583,
    "y": 693.6752767527674,
    "w": 149.5744680851064,
    "h": 51.54243542435424,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_62",
    "x": 251.05059924223136,
    "y": 706.7098845972282,
    "w": 78.75777374798832,
    "h": 26.64304693862528,
    "text": "\u8054\u7cfb\u5ba2\u670d",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.05803365292151,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "back_icon_0",
    "x": 34.460348162475825,
    "y": 50.11070110701107,
    "w": 22.901353965183752,
    "h": 28.634686346863468,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/back_icon_0.svg",
      "sha256": "23c0f034fd6afc76d67644ec247b6d57b64452b91b3c7ff09c207f41e6661ace",
      "method": "reference_svg",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "check_icon_1",
    "x": 39.47001934235976,
    "y": 108.81180811808117,
    "w": 28.626692456479688,
    "h": 28.634686346863468,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/check_icon_1.svg",
      "sha256": "b454e45f1990ad3cdde19b68869cee12f252d1d1aea44d03fed3e590ce7ea897",
      "method": "reference_svg",
      "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "step_0",
    "x": 45.195357833655706,
    "y": 522.5830258302583,
    "w": 12.88201160541586,
    "h": 12.88560885608856,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_1",
    "x": 45.195357833655706,
    "y": 572.6937269372694,
    "w": 12.88201160541586,
    "h": 12.88560885608856,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "step_2",
    "x": 45.195357833655706,
    "y": 624.9520295202951,
    "w": 12.88201160541586,
    "h": 12.88560885608856,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "text_44",
    "x": 35.601222870781285,
    "y": 12.88560916757558,
    "w": 150.3256569720329,
    "h": 22.612546125461233,
    "text": "9\u670817\u65e5 \u5468\u56db 09:45",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.309667896678945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_46",
    "x": 161.3670283549304,
    "y": 52.77439264865479,
    "w": 85.64609892087012,
    "h": 32.834463323614244,
    "text": "\u8ba2\u5355\u8be6\u60c5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.81605089096125,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_47",
    "x": 82.3142375854623,
    "y": 113.82287809335513,
    "w": 60.49293624317163,
    "h": 25.659143314150597,
    "text": "\u5df2\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.143003282160056,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_55",
    "x": 75.12761853291586,
    "y": 520.2522960075872,
    "w": 38.9330871995229,
    "h": 25.659143314150324,
    "text": "\u4e0b\u5355",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.143003282159803,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_56",
    "x": 247.60643586576663,
    "y": 523.8482800850079,
    "w": 110.79925613846042,
    "h": 22.06315909804444,
    "text": "9\u670817\u65e5 09:40",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.79873796118133,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_57",
    "x": 75.12761960976069,
    "y": 570.5461255574636,
    "w": 56.89962806923016,
    "h": 25.625847151358343,
    "text": "\u5df2\u4ed8\u6b3e",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.11203785076326,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_58",
    "x": 247.60643586576663,
    "y": 574.1254612121359,
    "w": 110.79925613846042,
    "h": 22.046511358000856,
    "text": "9\u670817\u65e5 09:45",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.7832555629408,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_59",
    "x": 75.12762032842235,
    "y": 620.6568264814168,
    "w": 56.89962806923016,
    "h": 26.19188191881927,
    "text": "\u5f85\u53d1\u8d27",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 20.638450184501924,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_60",
    "x": 247.60643631493025,
    "y": 624.2361621630591,
    "w": 110.79925613846032,
    "h": 22.612546125461233,
    "text": "9\u670817\u65e5 09:45",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.309667896678945,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
