// FROZEN compile of ⟶ [Filter] Flyout — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94e draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 253.0 height: 390.0 margin: Inset{left: 102.0 right: 0 top: 80.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 12.5 }
    RoundedView{ width: 203.0 height: 35.0 margin: Inset{left: 127.0 right: 0 top: 410.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 10.5 }
    View{ width: 142.9 height: 23.4 margin: Inset{left: 162.6 right: 0 top: 419.8 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "Show results" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 126.7 height: 17.0 margin: Inset{left: 127.0 right: 0 top: 212.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Size" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 126.7 height: 17.0 margin: Inset{left: 228.5 right: 0 top: 212.5 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "3mb - 50mb" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 202.4 height: 2.5 margin: Inset{left: 127.3 right: 0 top: 242.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 108.3 height: 20.0 margin: Inset{left: 176.4 right: 0 top: 233.5 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedShadowView{ width: 39.4 height: 20.0 margin: Inset{left: 245.3 right: 0 top: 233.5 bottom: 0} draw_bg.shadow_color: #3b4a7467 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #5882f2eb draw_bg.border_radius: 4.0 }
    RoundedShadowView{ width: 39.4 height: 20.0 margin: Inset{left: 176.4 right: 0 top: 233.5 bottom: 0} draw_bg.shadow_color: #3b4a7467 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #5882f2eb draw_bg.border_radius: 4.0 }
    RoundedShadowView{ width: 31.5 height: 2.5 margin: Inset{left: 214.8 right: 0 top: 242.5 bottom: 0} draw_bg.shadow_color: #3b4a7467 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #5882f2ff }
    View{ width: 126.7 height: 17.0 margin: Inset{left: 127.0 right: 0 top: 141.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Licence" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 75.0 height: 30.0 margin: Inset{left: 127.0 right: 0 top: 162.5 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 19.8 height: 15.0 margin: Inset{left: 171.8 right: 0 top: 170.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 56.2 height: 16.0 margin: Inset{left: 137.6 right: 0 top: 172.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Creative" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 75.0 height: 30.0 margin: Inset{left: 209.0 right: 0 top: 162.5 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 19.8 height: 15.0 margin: Inset{left: 253.8 right: 0 top: 170.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 56.2 height: 16.0 margin: Inset{left: 219.6 right: 0 top: 172.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Editorial" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 300.0 right: 0 top: 162.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 311.8 right: 0 top: 174.3 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.3 right: 0 top: 276.5 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 131.8 right: 0 top: 278.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.3 right: 0 top: 276.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.6 }
    View{ width: 182.7 height: 17.0 margin: Inset{left: 166.3 right: 0 top: 279.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Best match" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.0 right: 0 top: 320.5 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.0 right: 0 top: 320.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 134.5 right: 0 top: 326.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 188.1 height: 17.0 margin: Inset{left: 166.0 right: 0 top: 323.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Newest" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.3 right: 0 top: 364.5 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 130.3 right: 0 top: 364.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 134.8 right: 0 top: 370.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 127.1 height: 17.0 margin: Inset{left: 166.3 right: 0 top: 367.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Staff picks" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 253.0 height: 1.0 margin: Inset{left: 102.0 right: 0 top: 119.5 bottom: 0} draw_bg.color: #ffffffff }
    View{ width: 49.6 height: 17.0 margin: Inset{left: 118.8 right: 0 top: 95.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "filter content by:" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 37.5 height: 37.5 margin: Inset{left: 337.4 right: 0 top: 0.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 37.5 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.5 }
    RoundedView{ width: 220.6 height: 30.0 margin: Inset{left: 77.2 right: 0 top: 0.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 6.0 }
    View{ width: 67.0 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.2 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #131315ff draw_bg.border_radius: 1.4 }
    RoundedView{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 2.0 }
    RoundedView{ width: 14.0 height: 4.3 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.9 }
    RoundedView{ width: 9.1 height: 3.3 margin: Inset{left: 321.4 right: 0 top: 15.9 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.7 }
    RoundedView{ width: 4.2 height: 3.0 margin: Inset{left: 323.9 right: 0 top: 19.4 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.6 }
    RoundedView{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 1.9 }
    RoundedView{ width: 2.6 height: 3.5 margin: Inset{left: 299.0 right: 0 top: 18.8 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 5.2 margin: Inset{left: 303.1 right: 0 top: 17.1 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 7.2 margin: Inset{left: 307.2 right: 0 top: 15.1 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 2.6 height: 9.2 margin: Inset{left: 311.4 right: 0 top: 13.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 0.5 }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #121217ff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
}
