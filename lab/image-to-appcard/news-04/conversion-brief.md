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
    "x": 23.3698947808655,
    "y": 40.51441753171857,
    "w": 259.624209340653,
    "h": 43.82929642445213,
    "text": "Explore topics",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 41.7881142813924,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 24.854827278454703,
    "y": 91.97923875432525,
    "w": 246.0098615210562,
    "h": 18.320645905420992,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 15.024939966343336,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_0",
    "x": 24.0,
    "y": 130.0,
    "w": 174.0,
    "h": 187.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "topic_art_0",
    "x": 128.9173098125689,
    "y": 145.89158016147636,
    "w": 55.05843439911797,
    "h": 57.29658213891951,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/topic_art_0.svg",
      "sha256": "504b72f6e2f8410255c55918bcbba3bb4305b9f5a290d32fd5596d0df477223b",
      "reference_sha256": "d1e3b51d2b34c5cbd9fd34d15ca829a5aef9e1d2b23491169ba1d85ec1117c53",
      "method": "reference_svg",
      "crop_pixels": [
        288,
        326,
        123,
        128
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "topic_title_0",
    "x": 40.69873466553953,
    "y": 246.37370242214533,
    "w": 80.5096876751291,
    "h": 25.480968858131487,
    "text": "World",
    "font_src": "self:resources/ux/Roboto-Bold.ttf",
    "size": 28.27315181327332,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_count_0",
    "x": 42.28141278981959,
    "y": 283.517877739331,
    "w": 57.715545755237045,
    "h": 13.845444059976932,
    "text": "24 stories",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.478254969807994,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_1",
    "x": 209.0,
    "y": 132.0,
    "w": 172.0,
    "h": 184.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "topic_art_1",
    "x": 312.8930540242558,
    "y": 146.78662053056516,
    "w": 50.13450937155457,
    "h": 56.4013230429989,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/topic_art_1.svg",
      "sha256": "cec0bfbc5f536060f537b4c11d5eeb7df80107e5a36d19d68ad83d51b09b624b",
      "reference_sha256": "d1e3b51d2b34c5cbd9fd34d15ca829a5aef9e1d2b23491169ba1d85ec1117c53",
      "method": "reference_svg",
      "crop_pixels": [
        699,
        328,
        112,
        126
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "topic_title_1",
    "x": 224.98041135038682,
    "y": 245.92618223760093,
    "w": 101.58324145534729,
    "h": 25.928489042675892,
    "text": "Science",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 29.68244914699288,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_count_1",
    "x": 225.3225201938949,
    "y": 283.517877739331,
    "w": 55.02976846747519,
    "h": 13.845444059976932,
    "text": "12 stories",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.478254969807994,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_2",
    "x": 25.0,
    "y": 331.0,
    "w": 171.0,
    "h": 184.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "topic_art_2",
    "x": 128.9173098125689,
    "y": 346.8281430219146,
    "w": 54.16317530319735,
    "h": 56.4013230429989,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/topic_art_2.svg",
      "sha256": "969d295bac276e765e54eb5f7ce704ad23cee230d6b5149107023c8fc39f1ee8",
      "reference_sha256": "d1e3b51d2b34c5cbd9fd34d15ca829a5aef9e1d2b23491169ba1d85ec1117c53",
      "method": "reference_svg",
      "crop_pixels": [
        288,
        775,
        121,
        126
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "topic_title_2",
    "x": 40.16274015749607,
    "y": 443.7301038062284,
    "w": 98.52788764435778,
    "h": 26.3760092272203,
    "text": "Culture",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 29.451199805493044,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_count_2",
    "x": 41.34677598220802,
    "y": 482.2168396770473,
    "w": 55.92502756339581,
    "h": 13.845444059976932,
    "text": "18 stories",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.478254969807994,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_3",
    "x": 208.0,
    "y": 331.0,
    "w": 172.0,
    "h": 184.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "topic_art_3",
    "x": 310.2072767364939,
    "y": 346.8281430219146,
    "w": 58.63947078280044,
    "h": 58.191841234840126,
    "role": "icon",
    "native_candidates": [
      "Svg",
      "Icon",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/topic_art_3.svg",
      "sha256": "c39c11a2b2ed459adf410df538cad689cd9fa39e30a5db6c1bebe6c37a92bed3",
      "reference_sha256": "d1e3b51d2b34c5cbd9fd34d15ca829a5aef9e1d2b23491169ba1d85ec1117c53",
      "method": "reference_svg",
      "crop_pixels": [
        693,
        775,
        131,
        130
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Reviewed source geometry reconstructed as smooth SVG paths, circles and line segments; no raster tracing artifacts or embedded text."
    }
  },
  {
    "id": "topic_title_3",
    "x": 224.75908651034322,
    "y": 444.17762399077276,
    "w": 86.50962379803329,
    "h": 32.193771626297575,
    "text": "Design",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 30.089027770014297,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "topic_count_3",
    "x": 225.82927099109958,
    "y": 482.2168396770473,
    "w": 51.00110253583241,
    "h": 13.845444059976932,
    "text": "9 stories",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 13.478254969807994,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_section",
    "x": 26.438778193323607,
    "y": 538.156862745098,
    "w": 67.11576626240353,
    "h": 21.453287197231834,
    "text": "Latest",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 24.217027222175336,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest",
    "x": 25,
    "y": 569,
    "w": 356,
    "h": 131,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "latest_tag",
    "x": 40.805594620799695,
    "y": 585.594002306805,
    "w": 52.34399117971334,
    "h": 11.607843137254902,
    "text": "SCIENCE",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 10.41501520394254,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_title",
    "x": 40.65576122816325,
    "y": 607.9700115340254,
    "w": 186.63285556780593,
    "h": 26.823529411764707,
    "text": "The next chapter",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 23.945998071359693,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_title2",
    "x": 40.69590504771857,
    "y": 637.9538638985006,
    "w": 167.83241455347297,
    "h": 27.271049596309112,
    "text": "of clean energy",
    "font_src": "self:resources/ux/Roboto-Medium.ttf",
    "size": 23.901258562307454,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "latest_meta",
    "x": 41.257956650262834,
    "y": 673.3079584775086,
    "w": 53.23925027563396,
    "h": 12.502883506343714,
    "text": "4 min read",
    "font_src": "self:resources/ux/Roboto-Light.ttf",
    "size": 11.191455926087357,
    "weight": 300,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 25.0,
    "y": 712.0,
    "w": 356.0,
    "h": 43.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 25.0,
    "y": 712.0,
    "w": 356.0,
    "h": 43.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 152.53566623357216,
    "y": 726.1153402537485,
    "w": 104.26901874310914,
    "h": 17.873125720876587,
    "text": "Your reading list",
    "font_src": "self:resources/ux/Roboto-Regular.ttf",
    "size": 14.473846905937465,
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
    "y": 712.0,
    "w": 356.0,
    "h": 43.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "latest_art",
    "x": 260.07276736493935,
    "y": 587.1464821222606,
    "w": 111.01212789415655,
    "h": 111.90738699007717,
    "role": "illustration",
    "native_candidates": [
      "Svg",
      "Image"
    ],
    "asset": {
      "path": "repaired-assets/latest_art.png",
      "sha256": "6afb1d30fafdad7e3c84bdae26331c1ba1a2185e3fcd4a50d825f50b7aa5d2a2",
      "reference_sha256": "d1e3b51d2b34c5cbd9fd34d15ca829a5aef9e1d2b23491169ba1d85ec1117c53",
      "method": "source_crop",
      "crop_pixels": [
        581,
        1312,
        248,
        250
      ],
      "contains_ui": false,
      "fit": "contain",
      "clip": true,
      "notes": "Exact isolated illustration preserves thin turbine and solar-panel strokes after vector reconstruction lost fine detail."
    }
  }
]
```
