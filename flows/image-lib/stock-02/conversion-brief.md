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
    "x": 21.067663057660013,
    "y": 34.67550432276657,
    "w": 165.14663726571112,
    "h": 32.17752161383285,
    "text": "Watchlist",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 36.202988873983486,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "subtitle",
    "x": 21.622705278478975,
    "y": 84.32161383285302,
    "w": 222.89084895259094,
    "h": 17.4178674351585,
    "text": "Design fixture \u00b7 Prices are illustrative",
    "font_src": "self:resources/ux/Inter-400.ttf",
    "size": 13.726170083518786,
    "weight": 400,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "summary",
    "x": 20.0,
    "y": 120.0,
    "w": 366.0,
    "h": 135.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "summary_label",
    "x": 42.64399467188203,
    "y": 143.80749279538904,
    "w": 69.80154355016538,
    "h": 16.523342939481267,
    "text": "S&P 500",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 16.73046727988104,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "summary_value",
    "x": 42.339286457743185,
    "y": 180.48299711815562,
    "w": 211.75811668753633,
    "h": 53.646109510086454,
    "text": "5,420.18",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 53.3728253420772,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "list_title",
    "x": 21.32784149971199,
    "y": 283.8005763688761,
    "w": 135.60308710033075,
    "h": 22.337752161383285,
    "text": "Your stocks",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 24.822020110054837,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0",
    "x": 20.0,
    "y": 319.0,
    "w": 366.0,
    "h": 79.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_0_symbol",
    "x": 39.32467818345307,
    "y": 337.4720461095101,
    "w": 59.506063947078275,
    "h": 19.654178674351584,
    "text": "AAPL",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 22.363112391930837,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_name",
    "x": 39.47568779564261,
    "y": 367.4386167146974,
    "w": 43.839029768467476,
    "h": 17.865129682997118,
    "text": "Apple",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 14.88248720690676,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_price",
    "x": 295.70671487247137,
    "y": 336.57752161383286,
    "w": 73.83020948180815,
    "h": 21.44322766570605,
    "text": "182.40",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 23.34884330677516,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_0_change",
    "x": 313.2724177391396,
    "y": 367.4386167146974,
    "w": 55.28797940625614,
    "h": 15.628818443804034,
    "text": "+1.24%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 15.454782720902442,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1",
    "x": 20.0,
    "y": 409.0,
    "w": 366.0,
    "h": 80.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_1_symbol",
    "x": 39.605994384729115,
    "y": 428.2662824207493,
    "w": 63.08710033076075,
    "h": 19.654178674351584,
    "text": "NVDA",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 21.51661605709533,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_name",
    "x": 39.69868164623827,
    "y": 458.6801152737752,
    "w": 52.34399117971334,
    "h": 14.287031700288184,
    "text": "NVIDIA",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 14.139490551805503,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_price",
    "x": 295.70671487247137,
    "y": 426.92449567723344,
    "w": 73.38257993384785,
    "h": 21.44322766570605,
    "text": "124.80",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 23.34884330677516,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_1_change",
    "x": 313.2724177391396,
    "y": 458.2328530259366,
    "w": 55.3694792370109,
    "h": 15.628818443804034,
    "text": "+2.16%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 15.454782720902442,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2",
    "x": 20.0,
    "y": 500.0,
    "w": 366.0,
    "h": 79.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_2_symbol",
    "x": 39.66962838098247,
    "y": 518.6132564841498,
    "w": 59.984560687882734,
    "h": 20.1014409221902,
    "text": "MSFT",
    "font_src": "self:resources/camo/DMSans-Bold.ttf",
    "size": 22.239559284793096,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_name",
    "x": 39.67542937613379,
    "y": 549.0270893371758,
    "w": 68.90628445424476,
    "h": 15.181556195965417,
    "text": "Microsoft",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 14.456961546298722,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_price",
    "x": 294.2156157974439,
    "y": 517.7187319884727,
    "w": 74.27783902976846,
    "h": 21.44322766570605,
    "text": "416.20",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 23.34884330677516,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_2_change",
    "x": 309.18947663530616,
    "y": 548.5798270893372,
    "w": 59.097303373730114,
    "h": 16.07608069164265,
    "text": "+0.83%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 16.049197440937153,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3",
    "x": 20.0,
    "y": 591.0,
    "w": 366.0,
    "h": 79.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "quote_3_symbol",
    "x": 39.29742046238472,
    "y": 609.4074927953891,
    "w": 81.58555511342811,
    "h": 20.1014409221902,
    "text": "GOOGL",
    "font_src": "self:resources/ux/Inter-700.ttf",
    "size": 21.55277843702322,
    "weight": 700,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_name",
    "x": 39.456465833209286,
    "y": 639.3740634005763,
    "w": 66.66813671444322,
    "h": 18.312391930835734,
    "text": "Alphabet",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 15.362567439387622,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_price",
    "x": 295.28656418156777,
    "y": 608.5129682997118,
    "w": 73.38257993384785,
    "h": 20.995965417867435,
    "text": "165.30",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 22.750155016857846,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "quote_3_change",
    "x": 309.24375180749684,
    "y": 639.3740634005763,
    "w": 59.4718891343145,
    "h": 15.628818443804034,
    "text": "+0.62%",
    "font_src": "self:resources/ux/Inter-600.ttf",
    "size": 15.454782720902442,
    "weight": 600,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary",
    "x": 20.0,
    "y": 692.0,
    "w": 366.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  },
  {
    "id": "primary_surface",
    "x": 20.0,
    "y": 692.0,
    "w": 366.0,
    "h": 54.0,
    "role": "layout",
    "native_candidates": [
      "View"
    ]
  },
  {
    "id": "primary_label",
    "x": 151.34163975554247,
    "y": 711.8305475504322,
    "w": 106.05953693495039,
    "h": 19.20691642651297,
    "text": "Add a symbol",
    "font_src": "self:resources/ux/Inter-500.ttf",
    "size": 16.254574551930354,
    "weight": 500,
    "role": "text",
    "native_candidates": [
      "Label",
      "TextFlow"
    ]
  },
  {
    "id": "primary_control",
    "x": 20.0,
    "y": 692.0,
    "w": 366.0,
    "h": 54.0,
    "role": "button",
    "native_candidates": [
      "Button",
      "KitButton"
    ]
  }
]
```
