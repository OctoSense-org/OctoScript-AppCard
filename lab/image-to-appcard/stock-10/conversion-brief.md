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
    "x": 28.74650604243559,
    "y": 45.884659746251444,
    "w": 214.72616135777054,
    "h": 39.80161476355248,
    "text": "Opening bell",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 37.60673819700891,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 29.43000850916623,
    "y": 95.55940023068051,
    "w": 206.32855567805953,
    "h": 16.978085351787776,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 13.63244259641573,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "briefing",
    "x": 22.0,
    "y": 133.0,
    "w": 362.0,
    "h": 261.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "briefing_tag",
    "x": 44.73659428538282,
    "y": 162.239907727797,
    "w": 146.79382579933846,
    "h": 13.397923875432525,
    "text": "MONDAY MARKET BRIEF",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 12.980557838995201,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "headline",
    "x": 45.47656803314929,
    "y": 198.9365628604383,
    "w": 241.2436604189636,
    "h": 42.93425605536332,
    "text": "A steady start.",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 41.4194213354929,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "headline2",
    "x": 45.88706292749846,
    "y": 248.61130334486737,
    "w": 314.6549062844542,
    "h": 44.27681660899654,
    "text": "A wider perspective.",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 42.84767724361334,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "briefing_meta",
    "x": 45.33817561933331,
    "y": 351.9884659746251,
    "w": 165.14663726571112,
    "h": 17.425605536332178,
    "text": "Your watchlist, in context.",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 16.00191363090844,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index",
    "x": 22.0,
    "y": 404.0,
    "w": 177.0,
    "h": 115.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "index_label",
    "x": 44.15163233399438,
    "y": 429.8569780853518,
    "w": 58.16317530319735,
    "h": 14.292964244521338,
    "text": "S&P 500",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.21680144270903,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "index_value",
    "x": 44.88712597348176,
    "y": 465.21107266435985,
    "w": 119.98188315413394,
    "h": 29.508650519031143,
    "text": "+0.82%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 35.232942705844124,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tech",
    "x": 206.0,
    "y": 404.0,
    "w": 178.0,
    "h": 115.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "tech_label",
    "x": 228.2432824456965,
    "y": 429.8569780853518,
    "w": 59.05843439911797,
    "h": 15.635524798154556,
    "text": "NASDAQ",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 13.868325146787313,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "tech_value",
    "x": 228.41524063720834,
    "y": 465.21107266435985,
    "w": 102.28511475876441,
    "h": 29.508650519031143,
    "text": "+1.16%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 35.232942705844124,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "watchlist_title",
    "x": 27.443795253611516,
    "y": 548.0023068050749,
    "w": 152.16538037486217,
    "h": 28.61361014994233,
    "text": "On your radar",
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
    "id": "quote",
    "x": 22.0,
    "y": 584.0,
    "w": 362.0,
    "h": 89.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_symbol",
    "x": 43.74186009730437,
    "y": 605.7324106113033,
    "w": 62.191841234840126,
    "h": 21.453287197231834,
    "text": "AAPL",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 24.933267424616908,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_name",
    "x": 43.87256591655322,
    "y": 637.9538638985006,
    "w": 37.57221609702315,
    "h": 17.873125720876587,
    "text": "Apple",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 14.758644383911262,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_price",
    "x": 288.8992962401657,
    "y": 605.2848904267589,
    "w": 75.62072767364938,
    "h": 21.90080738177624,
    "text": "182.40",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 24.724872074276576,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_change",
    "x": 315.136365465304,
    "y": 637.9538638985006,
    "w": 49.65821389195148,
    "h": 14.740484429065743,
    "text": "+1.24%",
    "font_src": "self:resources/camo/DMSans-Medium.ttf",
    "size": 14.834923244565944,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 23.0,
    "y": 688.0,
    "w": 360.0,
    "h": 52.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 23.0,
    "y": 688.0,
    "w": 360.0,
    "h": 52.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 149.5792968813491,
    "y": 705.5294117647059,
    "w": 109.64057331863285,
    "h": 16.530565167243367,
    "text": "View watchlist",
    "font_src": "self:resources/camo/DMSans-Regular.ttf",
    "size": 17.118258425195858,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 23.0,
    "y": 688.0,
    "w": 360.0,
    "h": 52.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
