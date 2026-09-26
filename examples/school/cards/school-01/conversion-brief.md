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
    "id": "divider_0",
    "x": 71.47457627118644,
    "y": 454.49340866290015,
    "w": 263.0508474576271,
    "h": 1.4613935969868173,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "divider_1",
    "x": 71.47457627118644,
    "y": 688.3163841807909,
    "w": 263.0508474576271,
    "h": 1.4613935969868173,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "search_field",
    "x": 71.47457627118644,
    "y": 150.5235404896422,
    "w": 265.9736346516007,
    "h": 43.84180790960452,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "unread_dot",
    "x": 71.47457627118644,
    "y": 241.12994350282486,
    "w": 10.229755178907721,
    "h": 10.229755178907721,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "newsletter_dot",
    "x": 71.47457627118644,
    "y": 363.8870056497175,
    "w": 10.229755178907721,
    "h": 10.229755178907721,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_mail",
    "x": 67.090395480226,
    "y": 216.28625235404894,
    "w": 271.819209039548,
    "h": 115.45009416195856,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "open_mail_surface",
    "x": 67.090395480226,
    "y": 216.28625235404894,
    "w": 271.819209039548,
    "h": 115.45009416195856,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "open_mail_control",
    "x": 67.090395480226,
    "y": 216.28625235404894,
    "w": 271.819209039548,
    "h": 115.45009416195856,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_8",
    "x": 94.14423794317531,
    "y": 230.01815442561204,
    "w": 92.14500941619585,
    "h": 26.607758945386063,
    "text": "\u6797\u8001\u5e08",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 24.57365102759355,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_9",
    "x": 94.55492832278657,
    "y": 266.5407792194752,
    "w": 139.1479133814767,
    "h": 20.614560792320656,
    "text": "\u79cb\u5b63\u79d1\u5b66\u65e5\u5b89\u6392",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.86511913152759,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_10",
    "x": 93.9546808825638,
    "y": 297.2718211087591,
    "w": 186.5850394898124,
    "h": 18.699644818643094,
    "text": "\u660e\u5929\u4e0b\u5348\uff0c\u4e00\u8d77\u63a2\u7d22\u79d1\u5b66",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.376197509040892,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "dock_mail",
    "x": 71.47457627118644,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_mail_surface",
    "x": 71.47457627118644,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_mail_control",
    "x": 71.47457627118644,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_16",
    "x": 86.47303765525392,
    "y": 738.631472271808,
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
    "x": 170.84934086629002,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_calendar_surface",
    "x": 170.84934086629002,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_calendar_control",
    "x": 170.84934086629002,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_17",
    "x": 183.9888512987566,
    "y": 738.6593098989606,
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
    "x": 268.7627118644068,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "dock_payment_surface",
    "x": 268.7627118644068,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "dock_payment_control",
    "x": 268.7627118644068,
    "y": 695.623352165725,
    "w": 65.76271186440678,
    "h": 73.06967984934086,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "copy_18",
    "x": 285.5487949760359,
    "y": 740.6486861008486,
    "w": 36.045307553657,
    "h": 18.445060717980574,
    "text": "\u652f\u4ed8",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.67843059115113,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "search_icon_0",
    "x": 83.16572504708098,
    "y": 163.67608286252354,
    "w": 17.536723163841806,
    "h": 17.536723163841806,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/search_icon_0.svg",
      "sha256": "3d166945fce5c33014620729eb1e535bfc639e9e93be2869d3a0453b0db09bcf",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "mail_icon_1",
    "x": 89.01129943502825,
    "y": 705.8531073446327,
    "w": 29.227871939736346,
    "h": 24.843691148775893,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/mail_icon_1.svg",
      "sha256": "1a16bc4c293d40c64f1b8dd44559c4dfc50dd941fc312a54e7aa078aea90d8c1",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "calendar_icon_2",
    "x": 189.84745762711864,
    "y": 705.8531073446327,
    "w": 26.30508474576271,
    "h": 26.30508474576271,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/calendar_icon_2.svg",
      "sha256": "d1ce6830d28598a637e8f5f1d7e4e26efe008e434988d5f8dc8d0b187e9e1b30",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "wallet_icon_3",
    "x": 290.683615819209,
    "y": 705.8531073446327,
    "w": 27.76647834274953,
    "h": 24.843691148775893,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/wallet_icon_3.svg",
      "sha256": "5820d0ca044ea9d4d324308ed1fd7ddcebae65991c906369e4d1ec3317e931f8",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "chevron_icon_4",
    "x": 324.2956685499058,
    "y": 265.9736346516007,
    "w": 11.691148775894538,
    "h": 17.536723163841806,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/chevron_icon_4.svg",
      "sha256": "615cdf82883fb550a56f7f499ee8a3d41f66f75efa5adf4d0e2aa9e4fe182b8a",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "chevron_icon_5",
    "x": 324.2956685499058,
    "y": 390.1920903954802,
    "w": 11.691148775894538,
    "h": 17.536723163841806,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/chevron_icon_5.svg",
      "sha256": "615cdf82883fb550a56f7f499ee8a3d41f66f75efa5adf4d0e2aa9e4fe182b8a",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "status_icon_99",
    "x": 265.8399246704331,
    "y": 8.768361581920903,
    "w": 71.60828625235405,
    "h": 18.998116760828623,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "assets/status_icon_99.svg",
      "sha256": "3b6423e66479afccf6047b9070879d78bab3316da88a148ca834359918ba963e",
      "method": "reference_svg",
      "reference_sha256": "9abd36e11acf627aaeb1be069715a4159046f1a2985990765088cf8e0664c90b",
      "fit": "stretch",
      "clip": true,
      "notes": "Visually measured source icon reconstructed as vector paths; no text or embedded raster"
    }
  },
  {
    "id": "copy_2",
    "x": 65.17241926376128,
    "y": 12.371304919950376,
    "w": 94.7925197449062,
    "h": 16.745983216160088,
    "text": "9\u670824\u65e5 \u5468\u56db",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 14.517065166469349,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_3",
    "x": 156.69231567074456,
    "y": 11.826946550548342,
    "w": 50.73210781715202,
    "h": 17.834699768455195,
    "text": "09:41",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.227535926818437,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_5",
    "x": 67.1961879458194,
    "y": 50.951462310544414,
    "w": 58.07551073321682,
    "h": 28.857591221104684,
    "text": "\u90ae\u7bb1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 26.90215500119555,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_6",
    "x": 67.43553316935434,
    "y": 100.79387733279957,
    "w": 109.47932000840123,
    "h": 35.04571098616964,
    "text": "\u6536\u4ef6\u7bb1",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 33.56293079585907,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_7",
    "x": 110.20171242142118,
    "y": 161.069604519774,
    "w": 103.8361581920904,
    "h": 21.288286252354045,
    "text": "\u641c\u7d22\u90ae\u4ef6",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 18.73053765152118,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_11",
    "x": 94.17721376849954,
    "y": 352.116954606557,
    "w": 76.06967984934086,
    "h": 25.001495683307823,
    "text": "\u6821\u52a1\u5904",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 22.65533514919938,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_12",
    "x": 94.4828549682056,
    "y": 386.36250741627117,
    "w": 117.03639143173936,
    "h": 20.24244422942743,
    "text": "\u4e5d\u6708\u6821\u56ed\u7b80\u62a5",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 17.502633867917492,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_13",
    "x": 90.88960340739213,
    "y": 416.77706323472364,
    "w": 175.56993511571525,
    "h": 18.187765276585232,
    "text": "\u65b0\u5b66\u671f \u00b7 \u5171\u5efa\u7f8e\u597d\u6821\u56ed",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.206608013488998,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "copy_15",
    "x": 303.26250952596075,
    "y": 357.7951091039473,
    "w": 36.04530755365703,
    "h": 18.653758049627246,
    "text": "\u6628\u5929",
    "font_src": "self:resources/service/NotoSansSC-Regular.ttf",
    "size": 15.91070363694598,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  }
]
```
