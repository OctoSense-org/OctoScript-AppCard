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
    "y": 113.98870056497175,
    "w": 270.3578154425612,
    "h": 229.4387947269303,
    "role": "card",
    "native_candidates": [
      "View",
      "TaskplanProjectCard",
      "CamoTrackRow"
    ]
  },
  {
    "id": "restore_calendar",
    "x": 84.62711864406779,
    "y": 276.20338983050846,
    "w": 235.2843691148776,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "restore_calendar_surface",
    "x": 84.62711864406779,
    "y": 276.20338983050846,
    "w": 235.2843691148776,
    "h": 46.76459510357815,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "restore_calendar_control",
    "x": 84.62711864406779,
    "y": 276.20338983050846,
    "w": 235.2843691148776,
    "h": 46.76459510357815,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_177",
    "x": 159.11574676253548,
    "y": 290.4320230756578,
    "w": 80.54911643796922,
    "h": 20.686341707990948,
    "text": "\u91cd\u65b0\u52a0\u5165",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.03928833296319,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "calendar_icon_0",
    "x": 86.08851224105462,
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
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "close_icon_1",
    "x": 131.39171374764595,
    "y": 138.83239171374763,
    "w": 20.459510357815443,
    "h": 20.459510357815443,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/close_icon_1.svg",
      "sha256": "2445798d461b7d64d4941676d83736f15789d860dc36c144c9d5e5f3ba07bd06",
      "method": "reference_svg",
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_174",
    "x": 158.8056957747735,
    "y": 140.61009416195856,
    "w": 165.21468926553672,
    "h": 21.288286252354045,
    "text": "\u65e5\u5386 \u00b7 \u5df2\u64a4\u9500",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.609565395429545,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_175",
    "x": 82.73939647887009,
    "y": 195.04637727771865,
    "w": 171.89823365768285,
    "h": 20.0617906947113,
    "text": "\u4ec5\u79fb\u9664\u5bb6\u5ead\u65e5\u5386\u8bb0\u5f55",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.2152097478149,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_176",
    "x": 82.0642212328458,
    "y": 226.2754104644087,
    "w": 153.6699990039335,
    "h": 20.161153352120408,
    "text": "\u5b66\u6821\u6d3b\u52a8\u4ecd\u7136\u6709\u6548",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.340293296266534,
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
    "y": 360.9642184557439,
    "w": 270.3578154425612,
    "h": 305.4312617702448,
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
    "y": 575.789077212806,
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
    "y": 575.789077212806,
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
    "y": 575.789077212806,
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
    "y": 588.7667914526835,
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
    "y": 575.789077212806,
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
    "y": 575.789077212806,
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
    "y": 575.789077212806,
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
    "y": 589.2108043953369,
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
    "y": 629.8606403013182,
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
    "y": 629.8606403013182,
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
    "y": 629.8606403013182,
    "w": 236.7457627118644,
    "h": 32.15065913370998,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_182",
    "x": 165.83113307815955,
    "y": 635.0597873421485,
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
    "id": "wallet_icon_2",
    "x": 87.54990583804144,
    "y": 382.8851224105461,
    "w": 35.07344632768361,
    "h": 32.15065913370998,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_2.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_178",
    "x": 137.57694073833284,
    "y": 390.8902274979837,
    "w": 113.35442141161646,
    "h": 18.549198412890036,
    "text": "\u652f\u4ed8 \u00b7 \u5f85\u786e\u8ba4",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.74020744272272,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_179",
    "x": 85.67676691268228,
    "y": 433.45164369276716,
    "w": 149.86803604675748,
    "h": 22.0529293981657,
    "text": "\u5b66\u6821\u6d3b\u52a8\u6750\u6599\u8d39",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 19.411752041038387,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_180",
    "x": 82.11677603480847,
    "y": 474.8055435684772,
    "w": 98.46421563430404,
    "h": 34.7394774342459,
    "text": "\u00a5120",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 40.49997026909868,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_181",
    "x": 82.135700551969,
    "y": 522.6318849447092,
    "w": 149.8680249094884,
    "h": 19.85015968978161,
    "text": "\u6536\u6b3e\u65b9\uff1a\u5317\u8fb0\u5c0f\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 16.95204244896429,
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
    "id": "copy_183",
    "x": 85.47313691079393,
    "y": 742.0259792025652,
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
    "id": "copy_184",
    "x": 179.3172492163314,
    "y": 742.3404077323204,
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
    "id": "copy_185",
    "x": 280.81448133971975,
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
    "id": "mail_icon_3",
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
      "path": "assets/mail_icon_3.svg",
      "sha256": "0b8e6410736b971fda104fea927b904dd52f3b48dd6a8e8e1a467eb71f417b36",
      "method": "reference_svg",
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_4",
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
      "path": "assets/calendar_icon_4.svg",
      "sha256": "47de054bde8cc43310b23b563a5ff6ef00ab96df7efa357fd475b485a536fefc",
      "method": "reference_svg",
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_5",
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
      "path": "assets/wallet_icon_5.svg",
      "sha256": "65a550bd8a2b24c2f7c0c6e0d74b4f32d8fb3401ffc0ebff32f3097d3e7efe47",
      "method": "reference_svg",
      "reference_sha256": "e78436046d55df6a1c9f3ca92b7e7a99d61bffb0780cc8c9bed96f7a3f92fff0",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_171",
    "x": 67.71660296502479,
    "y": 24.680357481424192,
    "w": 69.090615107314,
    "h": 19.118347831151226,
    "text": "9\u670824\u65e5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.417451418376988,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_172",
    "x": 130.3141379788511,
    "y": 24.42072749124331,
    "w": 39.71700622737203,
    "h": 19.63760854773225,
    "text": "\u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.810488095367027,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_173",
    "x": 66.15919148066817,
    "y": 57.59140023627514,
    "w": 106.55628805237188,
    "h": 33.59259106118856,
    "text": "09:44",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 38.98892102923393,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
