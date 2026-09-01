// FROZEN compile of ⟶ [Stats] Data visualization #4 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffff }
    RoundedShadowView{ width: 345.0 height: 430.0 margin: Inset{left: 15.0 right: 0 top: 105.0 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    RoundedShadowView{ width: 105.0 height: 35.0 margin: Inset{left: 240.0 right: 0 top: 123.0 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 105.0 height: 35.0 margin: Inset{left: 240.0 right: 0 top: 123.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 21.0 height: 15.0 margin: Inset{left: 308.6 right: 0 top: 133.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.4 height: 4.0 margin: Inset{left: 313.4 right: 0 top: 138.5 bottom: 0} draw_bg.color: #939da7eb draw_bg.border_radius: 0.8 }
    View{ width: 77.2 height: 17.0 margin: Inset{left: 255.4 right: 0 top: 135.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "6 months" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 150.5 height: 797.0 margin: Inset{left: 1269.5 right: 0 top: 5172.0 bottom: 0} draw_bg.color: #d8d8d8ff draw_bg.border_size: 0.5 draw_bg.border_color: #979797ff }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 35.0 right: 0 top: 508.0 bottom: 0} draw_bg.color: #dfe5eeff draw_bg.border_radius: 5.0 }
    View{ width: 59.0 height: 15.0 margin: Inset{left: 50.0 right: 0 top: 508.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Income" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 107.5 right: 0 top: 508.0 bottom: 0} draw_bg.color: #ffb69eff draw_bg.border_radius: 5.0 }
    View{ width: 73.0 height: 15.0 margin: Inset{left: 122.5 right: 0 top: 508.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Spendings" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 194.0 right: 0 top: 508.0 bottom: 0} draw_bg.color: #6b999fff draw_bg.border_radius: 5.0 }
    View{ width: 59.5 height: 15.0 margin: Inset{left: 209.0 right: 0 top: 508.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Savings" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 267.0 right: 0 top: 508.0 bottom: 0} draw_bg.color: #ffdf9dff draw_bg.border_radius: 5.0 }
    View{ width: 81.5 height: 15.0 margin: Inset{left: 282.0 right: 0 top: 508.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Investments" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 345.0 height: 1.0 margin: Inset{left: 15.0 right: 0 top: 492.5 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 49.5 height: 17.0 margin: Inset{left: 321.0 right: 0 top: 456.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "JAN" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 48.5 height: 17.0 margin: Inset{left: 217.0 right: 0 top: 455.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "OCT" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 58.0 height: 17.0 margin: Inset{left: 247.0 right: 0 top: 460.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "NOV" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 58.0 height: 17.0 margin: Inset{left: 282.0 right: 0 top: 460.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "DEC" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 50.5 height: 17.0 margin: Inset{left: 181.0 right: 0 top: 456.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "SEP" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 50.5 height: 17.0 margin: Inset{left: 111.0 right: 0 top: 456.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "Jul" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 50.5 height: 17.0 margin: Inset{left: 146.0 right: 0 top: 456.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "AUG" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 51.0 height: 17.0 margin: Inset{left: 75.5 right: 0 top: 456.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "Jun" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 35.5 right: 0 top: 448.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 378.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "100" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 423.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "0" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 333.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "200" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 288.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "300" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 243.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "400" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 54.0 height: 17.0 margin: Inset{left: 31.0 right: 0 top: 198.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "500" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 12.5 height: 54.5 margin: Inset{left: 180.5 right: 0 top: 379.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 379.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 40.5 margin: Inset{left: 180.5 right: 0 top: 386.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 54.5 margin: Inset{left: 193.0 right: 0 top: 379.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 379.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 40.5 margin: Inset{left: 193.0 right: 0 top: 386.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 180.5 right: 0 top: 372.0 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 180.5 right: 0 top: 367.0 bottom: 0} draw_bg.color: #e68868eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 367.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 180.5 right: 0 top: 374.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 374.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 193.0 right: 0 top: 367.0 bottom: 0} draw_bg.color: #ffb69eeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 367.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 193.0 right: 0 top: 374.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 374.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 180.5 right: 0 top: 360.0 bottom: 0} draw_bg.color: #ffe0d5ff }
    RoundedView{ width: 12.5 height: 54.5 margin: Inset{left: 180.5 right: 0 top: 314.5 bottom: 0} draw_bg.color: #417c83eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 314.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 40.5 margin: Inset{left: 180.5 right: 0 top: 321.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 361.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 54.5 margin: Inset{left: 193.0 right: 0 top: 314.5 bottom: 0} draw_bg.color: #6b999feb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 314.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 40.5 margin: Inset{left: 193.0 right: 0 top: 321.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 361.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 180.5 right: 0 top: 307.5 bottom: 0} draw_bg.color: #95b6baff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 180.5 right: 0 top: 298.5 bottom: 0} draw_bg.color: #e6b653eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 298.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 180.5 right: 0 top: 305.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 180.5 right: 0 top: 309.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 193.0 right: 0 top: 298.5 bottom: 0} draw_bg.color: #ffdf9deb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 298.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 193.0 right: 0 top: 305.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 193.0 right: 0 top: 309.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 180.5 right: 0 top: 291.5 bottom: 0} draw_bg.color: #ffebbeff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 110.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 110.5 right: 0 top: 405.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 123.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 123.0 right: 0 top: 405.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 110.5 right: 0 top: 391.0 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 110.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #417c83eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 110.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 123.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #6b999feb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 123.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 110.5 right: 0 top: 378.5 bottom: 0} draw_bg.color: #95b6baff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 110.5 right: 0 top: 369.5 bottom: 0} draw_bg.color: #e68868eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 369.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 110.5 right: 0 top: 376.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 380.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 123.0 right: 0 top: 369.5 bottom: 0} draw_bg.color: #ffb69eeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 369.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 123.0 right: 0 top: 376.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 380.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 110.5 right: 0 top: 362.5 bottom: 0} draw_bg.color: #ffe0d5ff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 110.5 right: 0 top: 336.5 bottom: 0} draw_bg.color: #987b7ceb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 336.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 110.5 right: 0 top: 343.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 110.5 right: 0 top: 364.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 123.0 right: 0 top: 336.5 bottom: 0} draw_bg.color: #b19c9ceb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 336.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 123.0 right: 0 top: 343.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 123.0 right: 0 top: 364.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 110.5 right: 0 top: 329.5 bottom: 0} draw_bg.color: #cbbdbdff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 145.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 145.5 right: 0 top: 405.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 158.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 158.0 right: 0 top: 405.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 145.5 right: 0 top: 391.0 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 145.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #e68868eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 145.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 158.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #ffb69eeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 158.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 145.5 right: 0 top: 378.5 bottom: 0} draw_bg.color: #ffe0d5ff }
    RoundedView{ width: 12.5 height: 33.0 margin: Inset{left: 145.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #417c83eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 19.0 margin: Inset{left: 145.5 right: 0 top: 361.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 145.5 right: 0 top: 380.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 33.0 margin: Inset{left: 158.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #6b999feb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 19.0 margin: Inset{left: 158.0 right: 0 top: 361.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 158.0 right: 0 top: 380.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 145.5 right: 0 top: 347.5 bottom: 0} draw_bg.color: #95b6baff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 285.5 right: 0 top: 419.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 419.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 285.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 298.0 right: 0 top: 419.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 419.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 298.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 285.5 right: 0 top: 412.0 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 285.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #e68868eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 285.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 413.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 298.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #ffb69eeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 298.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 413.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 285.5 right: 0 top: 378.5 bottom: 0} draw_bg.color: #ffe0d5ff }
    RoundedView{ width: 12.5 height: 33.0 margin: Inset{left: 285.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #417c83eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 19.0 margin: Inset{left: 285.5 right: 0 top: 361.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 285.5 right: 0 top: 380.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 33.0 margin: Inset{left: 298.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #6b999feb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 19.0 margin: Inset{left: 298.0 right: 0 top: 361.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 298.0 right: 0 top: 380.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 285.5 right: 0 top: 347.5 bottom: 0} draw_bg.color: #95b6baff }
    RoundedView{ width: 12.5 height: 79.0 margin: Inset{left: 75.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 75.5 right: 0 top: 354.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 65.0 margin: Inset{left: 75.5 right: 0 top: 361.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 75.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 79.0 margin: Inset{left: 88.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 88.0 right: 0 top: 354.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 65.0 margin: Inset{left: 88.0 right: 0 top: 361.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 88.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 75.5 right: 0 top: 347.5 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 79.0 margin: Inset{left: 75.5 right: 0 top: 277.5 bottom: 0} draw_bg.color: #e6b653eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 75.5 right: 0 top: 277.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 65.0 margin: Inset{left: 75.5 right: 0 top: 284.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 75.5 right: 0 top: 349.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 79.0 margin: Inset{left: 88.0 right: 0 top: 277.5 bottom: 0} draw_bg.color: #ffdf9deb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 88.0 right: 0 top: 277.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 65.0 margin: Inset{left: 88.0 right: 0 top: 284.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 88.0 right: 0 top: 349.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 75.5 right: 0 top: 270.5 bottom: 0} draw_bg.color: #ffebbeff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 215.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 398.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 215.5 right: 0 top: 405.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 228.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 398.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 228.0 right: 0 top: 405.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 215.5 right: 0 top: 391.0 bottom: 0} draw_bg.color: #f8fafeff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 215.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #417c83eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 385.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 215.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 392.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 14.5 margin: Inset{left: 228.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #6b999feb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 385.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 1.0 margin: Inset{left: 228.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 392.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 215.5 right: 0 top: 378.5 bottom: 0} draw_bg.color: #95b6baff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 215.5 right: 0 top: 369.5 bottom: 0} draw_bg.color: #e68868eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 369.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 215.5 right: 0 top: 376.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 380.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 18.0 margin: Inset{left: 228.0 right: 0 top: 369.5 bottom: 0} draw_bg.color: #ffb69eeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 369.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 4.0 margin: Inset{left: 228.0 right: 0 top: 376.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 380.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 215.5 right: 0 top: 362.5 bottom: 0} draw_bg.color: #ffe0d5ff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 215.5 right: 0 top: 336.5 bottom: 0} draw_bg.color: #e6b653eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 336.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 215.5 right: 0 top: 343.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 215.5 right: 0 top: 364.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 35.5 margin: Inset{left: 228.0 right: 0 top: 336.5 bottom: 0} draw_bg.color: #ffdf9deb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 336.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 21.5 margin: Inset{left: 228.0 right: 0 top: 343.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 228.0 right: 0 top: 364.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 215.5 right: 0 top: 329.5 bottom: 0} draw_bg.color: #ffebbeff }
    RoundedView{ width: 12.5 height: 50.0 margin: Inset{left: 320.5 right: 0 top: 383.5 bottom: 0} draw_bg.color: #e6b653eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 320.5 right: 0 top: 383.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 36.0 margin: Inset{left: 320.5 right: 0 top: 390.5 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 320.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 50.0 margin: Inset{left: 333.0 right: 0 top: 383.5 bottom: 0} draw_bg.color: #ffdf9deb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 333.0 right: 0 top: 383.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 36.0 margin: Inset{left: 333.0 right: 0 top: 390.5 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 333.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 320.5 right: 0 top: 376.5 bottom: 0} draw_bg.color: #ffebbeff }
    RoundedView{ width: 12.5 height: 20.5 margin: Inset{left: 250.5 right: 0 top: 413.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 250.5 right: 0 top: 413.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 6.5 margin: Inset{left: 250.5 right: 0 top: 420.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 250.5 right: 0 top: 426.0 bottom: 0} draw_bg.color: #1f9a8aff }
    RoundedView{ width: 12.5 height: 20.5 margin: Inset{left: 263.0 right: 0 top: 413.0 bottom: 0} draw_bg.color: #ebf0f7eb draw_bg.border_radius: 2.5 }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 263.0 right: 0 top: 413.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 6.5 margin: Inset{left: 263.0 right: 0 top: 420.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 12.5 height: 7.5 margin: Inset{left: 263.0 right: 0 top: 426.0 bottom: 0} draw_bg.color: #30d9c7ff }
    RoundedView{ width: 25.0 height: 14.0 margin: Inset{left: 250.5 right: 0 top: 406.0 bottom: 0} draw_bg.color: #f8fafeff }
    View{ width: 165.6 height: 15.0 margin: Inset{left: 40.0 right: 0 top: 147.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "July 2018 - Feb 2019" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 107.0 height: 28.0 margin: Inset{left: 40.0 right: 0 top: 125.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "Transactions" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 9.3 } } }
    RoundedShadowView{ width: 345.0 height: 145.0 margin: Inset{left: 15.0 right: 0 top: 545.0 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    View{ width: 55.0 height: 15.0 margin: Inset{left: 57.0 right: 0 top: 657.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Soccer" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 100.5 height: 17.0 margin: Inset{left: 34.5 right: 0 top: 643.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Hattie Bishop" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 70.0 height: 28.0 margin: Inset{left: 42.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "83%" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 9.9 } } }
    View{ width: 54.5 height: 15.0 margin: Inset{left: 287.0 right: 0 top: 657.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Hiking" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 94.5 height: 17.0 margin: Inset{left: 267.5 right: 0 top: 642.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Bessie Dunn" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 70.0 height: 28.0 margin: Inset{left: 272.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "23%" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 9.9 } } }
    View{ width: 68.5 height: 15.0 margin: Inset{left: 165.5 right: 0 top: 657.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Volleyball" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 103.0 height: 17.0 margin: Inset{left: 148.0 right: 0 top: 642.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Gregory Greer" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 70.0 height: 28.0 margin: Inset{left: 157.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "66%" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 9.9 } } }
    RoundedView{ width: 345.0 height: 50.0 margin: Inset{left: 15.0 right: 0 top: 717.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 55.2 height: 24.0 margin: Inset{left: 51.8 right: 0 top: 730.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 253.0 height: 16.0 margin: Inset{left: 120.8 right: 0 top: 737.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "generate report" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 375.0 height: 90.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #121217ff }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 331.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 20.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 114.0 height: 18.9 margin: Inset{left: 59.0 right: 0 top: 36.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Transaction history" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 49.0 height: 20.9 margin: Inset{left: 58.5 right: 0 top: 54.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "subtitle" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 329.0 right: 0 top: 46.5 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 311.5 right: 0 top: 54.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 8.2 height: 4.0 margin: Inset{left: 314.9 right: 0 top: 59.5 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.8 }
    RoundedView{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 37.5 height: 37.5 margin: Inset{left: 337.4 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 37.5 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 220.6 height: 30.0 margin: Inset{left: 77.2 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 6.0 }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.2 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    RoundedView{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 2.0 }
    RoundedView{ width: 14.0 height: 4.3 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.9 }
    RoundedView{ width: 9.1 height: 3.3 margin: Inset{left: 321.4 right: 0 top: 15.9 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.7 }
    RoundedView{ width: 4.2 height: 3.0 margin: Inset{left: 323.9 right: 0 top: 19.4 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.6 }
    RoundedView{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 1.9 }
    RoundedView{ width: 2.6 height: 3.5 margin: Inset{left: 299.0 right: 0 top: 18.8 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 5.2 margin: Inset{left: 303.1 right: 0 top: 17.1 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 7.2 margin: Inset{left: 307.2 right: 0 top: 15.1 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 9.2 margin: Inset{left: 311.4 right: 0 top: 13.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 0.5 }
    View{ width: 67.0 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #121217ff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
}
