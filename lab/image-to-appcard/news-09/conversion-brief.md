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
    "x": 27.354477281502895,
    "y": 44.989619377162626,
    "w": 236.5892412070117,
    "h": 39.35409457900807,
    "text": "Reading room",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 37.136653969546295,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 27.62661200985093,
    "y": 94.21683967704729,
    "w": 251.986769570011,
    "h": 16.978085351787776,
    "text": "Independent stories. Fresh perspectives.",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.806473778497633,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "collection",
    "x": 27.656714335865363,
    "y": 144.33910034602076,
    "w": 192.89966923925027,
    "h": 12.95040369088812,
    "text": "SAVED FOR A SLOWER MOMENT",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0",
    "x": 27.0,
    "y": 173.0,
    "w": 352.0,
    "h": 160.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_0_tag",
    "x": 46.08628226908417,
    "y": 192.67128027681662,
    "w": 47.069227543907665,
    "h": 12.95040369088812,
    "text": "DESIGN",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title",
    "x": 46.33267877083204,
    "y": 213.70472895040368,
    "w": 152.16538037486217,
    "h": 28.166089965397923,
    "text": "A quieter city",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.708606346168004,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_title2",
    "x": 45.97400703032066,
    "y": 244.5836216839677,
    "w": 262.28224917309814,
    "h": 22.79584775086505,
    "text": "starts with small streets",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.677387637793785,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_0_meta",
    "x": 46.04726163158417,
    "y": 280.83275663206456,
    "w": 67.11576626240353,
    "h": 14.292964244521338,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.06142656355374,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "progress_0",
    "x": 46.5,
    "y": 309,
    "w": 314,
    "h": 4,
    "role": "progress",
    "native_candidates": [
      "ProgressBar",
      "Slider",
      "DesignProgressBar"
    ],
    "behavior": {
      "event": "value_change",
      "target": "progress_0",
      "property": "value",
      "value": 0.6942675159235668,
      "probe_value": 0.45
    }
  },
  {
    "id": "story_1",
    "x": 27.0,
    "y": 342.0,
    "w": 352.0,
    "h": 163.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_1_tag",
    "x": 46.009525802238024,
    "y": 361.83391003460207,
    "w": 54.13450937155457,
    "h": 12.95040369088812,
    "text": "SCIENCE",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title",
    "x": 46.26793116966392,
    "y": 384.2099192618224,
    "w": 195.58544652701212,
    "h": 28.61361014994233,
    "text": "The next chapter",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 26.184691648874818,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_title2",
    "x": 45.75725966996634,
    "y": 415.9838523644752,
    "w": 175.88974641675853,
    "h": 28.166089965397923,
    "text": "of clean energy",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.38454828298101,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_1_meta",
    "x": 46.04726163158417,
    "y": 452.6805074971165,
    "w": 67.11576626240353,
    "h": 14.292964244521338,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.06142656355374,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "progress_1",
    "x": 46.5,
    "y": 481,
    "w": 314,
    "h": 4,
    "role": "progress",
    "native_candidates": [
      "ProgressBar",
      "Slider",
      "DesignProgressBar"
    ],
    "behavior": {
      "event": "value_change",
      "target": "progress_1",
      "property": "value",
      "value": 0.31210191082802546,
      "probe_value": 0.75
    }
  },
  {
    "id": "story_2",
    "x": 27.0,
    "y": 513.0,
    "w": 352.0,
    "h": 159.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "story_2_tag",
    "x": 46.42006804208691,
    "y": 532.7866205305652,
    "w": 56.82028665931642,
    "h": 12.95040369088812,
    "text": "CULTURE",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 12.362436037138288,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_title",
    "x": 45.91075782921791,
    "y": 553.8200692041522,
    "w": 148.5843439911797,
    "h": 28.166089965397923,
    "text": "Why we keep",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.708606346168004,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_title2",
    "x": 45.716471705592994,
    "y": 583.8039215686274,
    "w": 247.0628445424476,
    "h": 28.61361014994233,
    "text": "making things by hand",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 25.854632510443622,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "story_2_meta",
    "x": 46.04726163158417,
    "y": 620.0530565167243,
    "w": 67.11576626240353,
    "h": 14.292964244521338,
    "text": "4 min read",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.06142656355374,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "progress_2",
    "x": 46.5,
    "y": 648,
    "w": 314,
    "h": 4,
    "role": "progress",
    "native_candidates": [
      "ProgressBar",
      "Slider",
      "DesignProgressBar"
    ],
    "behavior": {
      "event": "value_change",
      "target": "progress_2",
      "property": "value",
      "value": 0.12738853503184713,
      "probe_value": 0.75
    }
  },
  {
    "id": "primary",
    "x": 27.0,
    "y": 689.0,
    "w": 352.0,
    "h": 51.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 27.0,
    "y": 689.0,
    "w": 352.0,
    "h": 51.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 144.3028729023455,
    "y": 706.4244521337947,
    "w": 120.38368246968025,
    "h": 18.768166089965398,
    "text": "Continue reading",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 15.512779506266174,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 27.0,
    "y": 689.0,
    "w": 352.0,
    "h": 51.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
