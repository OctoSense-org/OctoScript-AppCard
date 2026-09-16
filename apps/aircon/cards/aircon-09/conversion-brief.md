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
    "x": 3.5,
    "y": 0.0,
    "w": 398.5,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "installation_booking",
    "x": 17.509765625,
    "y": 99.62688064192578,
    "w": 363.4755859375,
    "h": 259.9638916750251,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "reschedule",
    "x": 39.302734375,
    "y": 291.09729187562687,
    "w": 140.09765625,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "reschedule_surface",
    "x": 39.302734375,
    "y": 291.09729187562687,
    "w": 140.09765625,
    "h": 49.035105315947845,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "reschedule_control",
    "x": 39.302734375,
    "y": 291.09729187562687,
    "w": 140.09765625,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_32",
    "x": 89.62000234707617,
    "y": 305.7046490581637,
    "w": 42.078844614326975,
    "h": 27.531058377464102,
    "text": "\u6539\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.883884291041618,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_booking",
    "x": 214.4248046875,
    "y": 291.09729187562687,
    "w": 137.7626953125,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_booking_surface",
    "x": 214.4248046875,
    "y": 291.09729187562687,
    "w": 137.7626953125,
    "h": 49.035105315947845,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_booking_control",
    "x": 214.4248046875,
    "y": 291.09729187562687,
    "w": 137.7626953125,
    "h": 49.035105315947845,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_33",
    "x": 241.69365574992253,
    "y": 304.5404291878745,
    "w": 81.82536468654868,
    "h": 29.787094651875293,
    "text": "\u53d6\u6d88\u9884\u7ea6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 23.981998026244025,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wrench_icon_0",
    "x": 40.0810546875,
    "y": 118.30692076228686,
    "w": 30.3544921875,
    "h": 30.35506519558676,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wrench_icon_0.svg",
      "sha256": "1210670333e1f913e6fb26259e8d8a0ba51c7e5c5f2aed5300f46ecdf0fef01d",
      "method": "reference_svg",
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "check_icon_1",
    "x": 337.3994140625,
    "y": 120.641925777332,
    "w": 22.5712890625,
    "h": 24.906720160481445,
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
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_28",
    "x": 89.62000122714919,
    "y": 121.9451849311148,
    "w": 182.76268166303635,
    "h": 27.603460925990674,
    "text": "\u5b89\u88c5\u670d\u52a1 \u00b7 \u9884\u7ea6\u6210\u529f",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.95121866117133,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_29",
    "x": 38.81750742260823,
    "y": 168.86249464897907,
    "w": 65.5261478200555,
    "h": 27.45865434438071,
    "text": "\u738b\u5e08\u5085",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.816548540274063,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_30",
    "x": 38.817503899456305,
    "y": 207.81544607938756,
    "w": 233.5651838183403,
    "h": 23.69368619163167,
    "text": "\u5468\u516d 9\u670819\u65e5 14:00-16:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.315128158217455,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_31",
    "x": 38.817508669822985,
    "y": 242.8405216115756,
    "w": 131.96017950773236,
    "h": 24.236710130391153,
    "text": "\u5bb6 \u00b7 \u6d77\u68e0\u8def18\u53f7",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.820140421263773,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_undone",
    "x": 17.509765625,
    "y": 379.049147442327,
    "w": 364.25390625,
    "h": 196.14042126379138,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "restore_calendar",
    "x": 97.6767578125,
    "y": 507.47442326980945,
    "w": 181.3486328125,
    "h": 48.2567703109328,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "restore_calendar_surface",
    "x": 97.6767578125,
    "y": 507.47442326980945,
    "w": 181.3486328125,
    "h": 48.2567703109328,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "restore_calendar_control",
    "x": 97.6767578125,
    "y": 507.47442326980945,
    "w": 181.3486328125,
    "h": 48.2567703109328,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "text_36",
    "x": 140.4224989388565,
    "y": 520.7061181362594,
    "w": 85.06557309627533,
    "h": 27.494856732061386,
    "text": "\u91cd\u65b0\u52a0\u5165",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.85021676081709,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_2",
    "x": 35.4111328125,
    "y": 400.0641925777332,
    "w": 35.0244140625,
    "h": 36.581745235707125,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "ae776c61fe98dc0aee57fc63b1343360e4030e6cc97db9fa23eca69d129b3b1d",
      "method": "reference_svg",
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_34",
    "x": 81.8042402536705,
    "y": 407.0692077322718,
    "w": 151.4995988458395,
    "h": 28.12838515546649,
    "text": "\u65e5\u5386\u8bb0\u5f55\u5df2\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.439398194583838,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_35",
    "x": 34.909623525126776,
    "y": 450.36635483285744,
    "w": 147.59171497821808,
    "h": 27.639663313671353,
    "text": "\u5b89\u88c5\u9884\u7ea6\u4ecd\u7136\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 21.98488688171436,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 14.396484375,
    "y": 657.6930792377132,
    "w": 376.70703125,
    "h": 117.52858575727181,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_0",
    "x": 37.20126953125,
    "y": 666.3481644934805,
    "w": 69.66278125000001,
    "h": 69.6640962888666,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 48.87607421875,
    "y": 681.1365295887663,
    "w": 46.313171875,
    "h": 43.979041123370116,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_mail.svg",
      "sha256": "9b7cff617690a90aac7b12cb3fef04594954830e1bc22fcd9518a5cf98ca1e93",
      "method": "reference_svg",
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_1",
    "x": 125.72742187499999,
    "y": 666.3481644934805,
    "w": 69.66278125000001,
    "h": 69.6640962888666,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_tile_2",
    "x": 214.25357421874997,
    "y": 666.3481644934805,
    "w": 69.66278125000001,
    "h": 69.6640962888666,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_bag",
    "x": 225.92837890624997,
    "y": 681.1365295887663,
    "w": 46.313171875,
    "h": 43.979041123370116,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_bag.svg",
      "sha256": "2f675e8ba88bad04e7dcdce9b85424e2d8458a97463597bfa7b814452887fb40",
      "method": "reference_svg",
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "dock_tile_3",
    "x": 302.7797265625,
    "y": 666.3481644934805,
    "w": 69.66278125000001,
    "h": 69.6640962888666,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_wallet",
    "x": 314.45453125,
    "y": 681.1365295887663,
    "w": 46.313171875,
    "h": 43.979041123370116,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/dock_wallet.svg",
      "sha256": "ad9266d4ebef2712804598eee5535322f54c6c4d15b3ba967f5616e33a3bb72d",
      "method": "reference_svg",
      "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
      "fit": "stretch",
      "clip": true,
      "notes": "Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI"
    }
  },
  {
    "id": "text_27",
    "x": 19.27808425670877,
    "y": 51.37011033807827,
    "w": 88.97345696389677,
    "h": 35.47731546078667,
    "text": "15:29",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.273903378531603,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_37",
    "x": 124.79096227050387,
    "y": 688.826479816024,
    "w": 42.078844614326975,
    "h": 35.31440768533652,
    "text": "18",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 29.122399147362962,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_38",
    "x": 38.81750599074731,
    "y": 735.526579606723,
    "w": 42.078841645270586,
    "h": 23.80229038556096,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.416130058571692,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_39",
    "x": 128.69884730977313,
    "y": 735.526579606723,
    "w": 38.17095777764915,
    "h": 23.80229038556096,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.416130058571692,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_41",
    "x": 226.39595766542163,
    "y": 735.526579606723,
    "w": 38.17095777764913,
    "h": 23.80229038556096,
    "text": "\u8d2d\u7269",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.416130058571692,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_42",
    "x": 320.1851825131045,
    "y": 735.5265800449075,
    "w": 38.17096074670552,
    "h": 23.80229038556096,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.416130058571692,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "text_217",
    "x": 26.0712890625,
    "y": 23.350050150451356,
    "w": 100.2900390625,
    "h": 21.90170511534604,
    "text": "9\u670818\u65e5 \u5468\u4e94",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.648585757271817,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
