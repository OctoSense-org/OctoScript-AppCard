// FROZEN compile of ⟶ [Filter] Flyout#2 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94e draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f268d draw_bg.border_radius: 75.0 }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f26ab }
    RoundedView{ width: 40.0 height: 40.0 margin: Inset{left: 323.0 right: 0 top: 40.5 bottom: 0} draw_bg.color: #140f26ab draw_bg.border_radius: 20.0 }
    RoundedView{ width: 250.0 height: 314.9 margin: Inset{left: 117.5 right: 0 top: 143.1 bottom: 0} draw_bg.color: #140f2693 draw_bg.border_radius: 16.6 }
    RoundedView{ width: 35.9 height: 86.6 margin: Inset{left: 306.6 right: 0 top: 88.0 bottom: 0} draw_bg.color: #140f2687 draw_bg.border_radius: 7.2 }
    RoundedView{ width: 250.0 height: 370.0 margin: Inset{left: 117.5 right: 0 top: 88.0 bottom: 0} draw_bg.color: #140f2675 draw_bg.border_radius: 50.0 }
    RoundedView{ width: 250.0 height: 314.9 margin: Inset{left: 117.5 right: 0 top: 143.1 bottom: 0} draw_bg.color: #140f2693 draw_bg.border_radius: 16.6 }
    RoundedView{ width: 35.9 height: 86.6 margin: Inset{left: 306.6 right: 0 top: 88.0 bottom: 0} draw_bg.color: #140f2687 draw_bg.border_radius: 7.2 }
    RoundedView{ width: 40.0 height: 188.9 margin: Inset{left: 130.0 right: 0 top: 206.1 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 142.5 right: 0 top: 256.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Price" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 242.5 right: 0 top: 256.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "$230 - $520" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 200.0 height: 2.5 margin: Inset{left: 142.5 right: 0 top: 285.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 48.6 height: 25.0 margin: Inset{left: 186.2 right: 0 top: 274.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 48.6 height: 25.0 margin: Inset{left: 254.2 right: 0 top: 274.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 107.0 height: 20.0 margin: Inset{left: 191.0 right: 0 top: 277.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 19.4 height: 2.5 margin: Inset{left: 234.8 right: 0 top: 285.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 38.9 height: 20.0 margin: Inset{left: 259.1 right: 0 top: 277.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 29.2 height: 15.0 margin: Inset{left: 263.9 right: 0 top: 279.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 38.9 height: 20.0 margin: Inset{left: 191.0 right: 0 top: 277.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 29.2 height: 15.0 margin: Inset{left: 195.8 right: 0 top: 279.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 142.5 right: 0 top: 317.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Type" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 86.5 height: 30.0 margin: Inset{left: 142.5 right: 0 top: 338.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 22.8 height: 15.0 margin: Inset{left: 194.1 right: 0 top: 345.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 61.2 height: 16.0 margin: Inset{left: 154.7 right: 0 top: 348.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Illustration" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 65.0 height: 30.0 margin: Inset{left: 237.0 right: 0 top: 338.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 17.1 height: 15.0 margin: Inset{left: 275.8 right: 0 top: 345.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 52.0 height: 16.0 margin: Inset{left: 246.1 right: 0 top: 348.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Image" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 312.5 right: 0 top: 338.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 324.3 right: 0 top: 349.8 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 142.5 right: 0 top: 388.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Height (cm)" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 242.5 right: 0 top: 388.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "182CM" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 200.0 height: 2.5 margin: Inset{left: 142.5 right: 0 top: 417.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 105.9 height: 25.0 margin: Inset{left: 227.2 right: 0 top: 406.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 180.0 height: 20.0 margin: Inset{left: 142.5 right: 0 top: 409.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 84.7 height: 2.5 margin: Inset{left: 142.5 right: 0 top: 417.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 84.7 height: 20.0 margin: Inset{left: 237.8 right: 0 top: 409.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 63.5 height: 15.0 margin: Inset{left: 248.4 right: 0 top: 411.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 16.0 height: 24.0 margin: Inset{left: 338.1 right: 0 top: 116.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 49.4 height: 17.0 margin: Inset{left: 134.2 right: 0 top: 122.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "refine search" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 181.5 right: 0 top: 174.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Staff picks" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 145.5 right: 0 top: 171.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 145.5 right: 0 top: 171.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 150.0 right: 0 top: 176.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 181.5 right: 0 top: 218.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "New items" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 145.5 right: 0 top: 215.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 145.5 right: 0 top: 215.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 150.0 right: 0 top: 220.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
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
}
