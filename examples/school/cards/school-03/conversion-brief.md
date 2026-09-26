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
    "x": 53.93785310734464,
    "y": 0.0,
    "w": 298.1242937853107,
    "h": 776.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "wallpaper_lower",
    "x": 53.93785310734464,
    "y": 426.8,
    "w": 298.1242937853107,
    "h": 349.2,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "calendar_card",
    "x": 67.090395480226,
    "y": 112.52730696798493,
    "w": 270.3578154425612,
    "h": 257.20527306967983,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "ack_calendar",
    "x": 84.62711864406779,
    "y": 306.8926553672316,
    "w": 109.6045197740113,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "ack_calendar_surface",
    "x": 84.62711864406779,
    "y": 306.8926553672316,
    "w": 109.6045197740113,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "ack_calendar_control",
    "x": 84.62711864406779,
    "y": 306.8926553672316,
    "w": 109.6045197740113,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_126",
    "x": 118.33069876081369,
    "y": 319.6752281702715,
    "w": 43.38870768540451,
    "h": 21.56877442845087,
    "text": "\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.01382513901609,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "undo_calendar",
    "x": 208.84557438794727,
    "y": 306.8926553672316,
    "w": 112.52730696798493,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "undo_calendar_surface",
    "x": 208.84557438794727,
    "y": 306.8926553672316,
    "w": 112.52730696798493,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "undo_calendar_control",
    "x": 208.84557438794727,
    "y": 306.8926553672316,
    "w": 112.52730696798493,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_127",
    "x": 224.8683147887342,
    "y": 320.16432439542643,
    "w": 80.10571391277654,
    "h": 20.590582714360437,
    "text": "\u64a4\u9500\u65e5\u7a0b",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.85853898208874,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 87.54990583804144,
    "y": 130.06403013182674,
    "w": 33.612052730696796,
    "h": 33.612052730696796,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_0.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "328838618c28457807f71dec4b16a2e9fc6b1263dff646020d887b1d4e546ce5",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_121",
    "x": 127.15188914584304,
    "y": 136.72416254584664,
    "w": 113.20361165102287,
    "h": 18.889870001163484,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u66f4\u65b0",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.097156758014577,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_122",
    "x": 77.93760798936391,
    "y": 177.98313702132768,
    "w": 120.63115663497659,
    "h": 24.718261781515235,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.277700840338962,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_123",
    "x": 81.50690340603987,
    "y": 210.17366198574928,
    "w": 182.91333803178003,
    "h": 19.23477138127599,
    "text": "9\u670825\u65e5 14:00\u201316:00",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.55157993234561,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_124",
    "x": 81.75722617928247,
    "y": 238.34857157960846,
    "w": 160.8831292835857,
    "h": 18.3688999036849,
    "text": "\u5317\u8fb0\u5c0f\u5b66 \u00b7 \u79d1\u5b66\u6559\u5ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.35138878598814,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_125",
    "x": 81.71251776770241,
    "y": 273.01225464681863,
    "w": 124.21535256985821,
    "h": 18.714902599219684,
    "text": "\u6765\u81ea\u6797\u8001\u5e08\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.942473021906485,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "payment_card",
    "x": 67.090395480226,
    "y": 385.80790960451975,
    "w": 270.3578154425612,
    "h": 289.35593220338984,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "pay_fee",
    "x": 84.62711864406779,
    "y": 571.4048964218456,
    "w": 157.83050847457628,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_surface",
    "x": 84.62711864406779,
    "y": 571.4048964218456,
    "w": 157.83050847457628,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "pay_fee_control",
    "x": 84.62711864406779,
    "y": 571.4048964218456,
    "w": 157.83050847457628,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "pay_fee_label",
    "x": 116.06387745077072,
    "y": 584.382610661723,
    "w": 97.99058380414313,
    "h": 22.270560220810047,
    "text": "\u652f\u4ed8 \u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.83056463908471,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "cancel_payment",
    "x": 252.68738229755178,
    "y": 571.4048964218456,
    "w": 68.68549905838042,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_surface",
    "x": 252.68738229755178,
    "y": 571.4048964218456,
    "w": 68.68549905838042,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "cancel_payment_control",
    "x": 252.68738229755178,
    "y": 571.4048964218456,
    "w": 68.68549905838042,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "cancel_payment_label",
    "x": 266.66514370616363,
    "y": 584.8266236043764,
    "w": 42.45762711864407,
    "h": 21.38253433550313,
    "text": "\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.711016507538353,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "view_payment",
    "x": 84.62711864406779,
    "y": 626.9378531073446,
    "w": 236.7457627118644,
    "h": 32.15065913370998,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "view_payment_surface",
    "x": 84.62711864406779,
    "y": 626.9378531073446,
    "w": 236.7457627118644,
    "h": 32.15065913370998,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "view_payment_control",
    "x": 84.62711864406779,
    "y": 626.9378531073446,
    "w": 236.7457627118644,
    "h": 32.15065913370998,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_132",
    "x": 165.83113307815955,
    "y": 632.1370001481749,
    "w": 77.53107344632768,
    "h": 20.290971455062664,
    "text": "\u67e5\u770b\u8d39\u7528",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.61186103250018,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "wallet_icon_1",
    "x": 87.54990583804144,
    "y": 406.2674199623352,
    "w": 33.612052730696796,
    "h": 29.227871939736346,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_1.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "328838618c28457807f71dec4b16a2e9fc6b1263dff646020d887b1d4e546ce5",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_128",
    "x": 133.15509030544658,
    "y": 411.6337521121725,
    "w": 105.80761855036886,
    "h": 17.55422303440738,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.66378258320308,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_129",
    "x": 81.04874344392336,
    "y": 455.16802694746394,
    "w": 153.61180677299777,
    "h": 22.51311141205345,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.906571410810162,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_130",
    "x": 81.19277691491618,
    "y": 493.79587581473595,
    "w": 94.93712604662305,
    "h": 33.603754587012624,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 39.00362923190069,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_131",
    "x": 84.96850993649082,
    "y": 535.9565612079311,
    "w": 142.52462199342372,
    "h": 19.05765152500058,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.10444013369046,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock",
    "x": 56.86064030131827,
    "y": 679.54802259887,
    "w": 290.81732580037664,
    "h": 96.45197740112994,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_tile",
    "x": 77.32015065913372,
    "y": 688.3163841807909,
    "w": 54.071563088512235,
    "h": 49.687382297551785,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_tile",
    "x": 175.23352165725046,
    "y": 688.3163841807909,
    "w": 54.071563088512235,
    "h": 49.687382297551785,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_tile",
    "x": 273.1468926553672,
    "y": 688.3163841807909,
    "w": 54.071563088512235,
    "h": 49.687382297551785,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail",
    "x": 74.39736346516008,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 74.39736346516008,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 74.39736346516008,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_133",
    "x": 84.58253654467248,
    "y": 742.0259795016544,
    "w": 36.19617759510478,
    "h": 18.794143604950644,
    "text": "\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.09808879755239,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_calendar",
    "x": 172.31073446327684,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 172.31073446327684,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 172.31073446327684,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_134",
    "x": 182.09835066243664,
    "y": 740.5019818735126,
    "w": 37.95960460059612,
    "h": 18.738468396658718,
    "text": "\u65e5\u5386",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.97980230029806,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_payment",
    "x": 270.2241054613936,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 270.2241054613936,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 270.2241054613936,
    "y": 685.3935969868173,
    "w": 61.378531073446325,
    "h": 87.68361581920904,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_135",
    "x": 279.9238813637165,
    "y": 741.398017746148,
    "w": 39.717006227372174,
    "h": 20.05006651778512,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.42047740714738,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "mail_icon_2",
    "x": 90.47269303201506,
    "y": 700.0075329566855,
    "w": 26.30508474576271,
    "h": 26.30508474576271,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_2.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "328838618c28457807f71dec4b16a2e9fc6b1263dff646020d887b1d4e546ce5",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_3",
    "x": 188.38606403013182,
    "y": 700.0075329566855,
    "w": 26.30508474576271,
    "h": 26.30508474576271,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_3.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "328838618c28457807f71dec4b16a2e9fc6b1263dff646020d887b1d4e546ce5",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_4",
    "x": 286.2994350282486,
    "y": 700.0075329566855,
    "w": 26.30508474576271,
    "h": 26.30508474576271,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_4.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "328838618c28457807f71dec4b16a2e9fc6b1263dff646020d887b1d4e546ce5",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_119",
    "x": 66.90251984359406,
    "y": 25.35670112221449,
    "w": 102.13591709233653,
    "h": 17.765661285789893,
    "text": "9\u670824\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.678429710466848,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_120",
    "x": 69.10757794227739,
    "y": 56.15908294831896,
    "w": 102.65758677597913,
    "h": 32.77612818156396,
    "text": "09:43",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 37.91321236042683,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
