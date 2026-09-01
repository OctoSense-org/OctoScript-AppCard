// FROZEN compile of ⟶ [Filter] Sidebar — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94e draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2699 }
    RoundedShadowView{ width: 273.0 height: 812.0 margin: Inset{left: 102.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffeb draw_bg.border_radius: 54.6 }
    RoundedShadowView{ width: 250.0 height: 812.0 margin: Inset{left: 125.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 23.6 height: 199.0 margin: Inset{left: 102.0 right: 0 top: 528.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 4.7 }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 116.0 right: 0 top: 611.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 127.8 right: 0 top: 622.8 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 200.0 height: 35.0 margin: Inset{left: 150.0 right: 0 top: 702.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 10.5 }
    View{ width: 141.0 height: 23.4 margin: Inset{left: 185.0 right: 0 top: 711.8 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "Show results" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 49.4 height: 17.0 margin: Inset{left: 141.7 right: 0 top: 74.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "refine search" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 189.0 right: 0 top: 126.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Staff picks" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 153.0 right: 0 top: 123.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 153.0 right: 0 top: 123.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 157.5 right: 0 top: 128.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 189.0 right: 0 top: 170.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "New items" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 153.0 right: 0 top: 167.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 153.0 right: 0 top: 167.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 157.5 right: 0 top: 172.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 150.0 right: 0 top: 208.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Rating" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 60.0 height: 30.0 margin: Inset{left: 150.0 right: 0 top: 229.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 15.8 height: 15.0 margin: Inset{left: 185.8 right: 0 top: 236.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 49.8 height: 16.0 margin: Inset{left: 158.4 right: 0 top: 239.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "5 star" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 61.0 height: 30.0 margin: Inset{left: 218.0 right: 0 top: 229.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 16.1 height: 15.0 margin: Inset{left: 254.4 right: 0 top: 236.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 50.2 height: 16.0 margin: Inset{left: 226.6 right: 0 top: 239.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "4 star" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 150.0 right: 0 top: 340.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Type" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 86.5 height: 30.0 margin: Inset{left: 150.0 right: 0 top: 362.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 22.8 height: 15.0 margin: Inset{left: 201.6 right: 0 top: 369.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 61.2 height: 16.0 margin: Inset{left: 162.2 right: 0 top: 372.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Illustration" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 65.0 height: 30.0 margin: Inset{left: 244.5 right: 0 top: 362.0 bottom: 0} draw_bg.color: #140f2680 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 17.1 height: 15.0 margin: Inset{left: 283.2 right: 0 top: 369.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 52.0 height: 16.0 margin: Inset{left: 253.6 right: 0 top: 372.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Image" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.2 } } }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 320.0 right: 0 top: 362.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 331.8 right: 0 top: 373.8 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 150.0 right: 0 top: 279.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Price" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 250.0 right: 0 top: 279.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "$230 - $520" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 200.0 height: 2.5 margin: Inset{left: 150.0 right: 0 top: 308.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 48.6 height: 25.0 margin: Inset{left: 193.7 right: 0 top: 297.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 48.6 height: 25.0 margin: Inset{left: 261.8 right: 0 top: 297.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 107.0 height: 20.0 margin: Inset{left: 198.5 right: 0 top: 300.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 19.4 height: 2.5 margin: Inset{left: 242.2 right: 0 top: 308.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 38.9 height: 20.0 margin: Inset{left: 266.6 right: 0 top: 300.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 29.2 height: 15.0 margin: Inset{left: 271.4 right: 0 top: 302.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 38.9 height: 20.0 margin: Inset{left: 198.5 right: 0 top: 300.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 29.2 height: 15.0 margin: Inset{left: 203.3 right: 0 top: 302.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 150.0 right: 0 top: 412.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Width (px)" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 250.0 right: 0 top: 412.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "3840 PX" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 200.0 height: 2.5 margin: Inset{left: 150.0 right: 0 top: 441.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 105.9 height: 25.0 margin: Inset{left: 234.7 right: 0 top: 430.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 180.0 height: 20.0 margin: Inset{left: 150.0 right: 0 top: 433.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 84.7 height: 2.5 margin: Inset{left: 150.0 right: 0 top: 441.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 84.7 height: 20.0 margin: Inset{left: 245.3 right: 0 top: 433.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 63.5 height: 15.0 margin: Inset{left: 255.9 right: 0 top: 435.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 150.0 right: 0 top: 473.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Height (px)" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    View{ width: 125.0 height: 17.0 margin: Inset{left: 250.0 right: 0 top: 473.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "2160 PX" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 200.0 height: 2.5 margin: Inset{left: 150.0 right: 0 top: 502.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 62.0 height: 25.0 margin: Inset{left: 199.7 right: 0 top: 491.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 12.5 }
    RoundedView{ width: 105.5 height: 20.0 margin: Inset{left: 150.0 right: 0 top: 494.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 49.6 height: 2.5 margin: Inset{left: 150.0 right: 0 top: 502.5 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 1.2 }
    RoundedView{ width: 49.6 height: 20.0 margin: Inset{left: 205.8 right: 0 top: 494.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 4.0 }
    RoundedView{ width: 37.2 height: 15.0 margin: Inset{left: 212.1 right: 0 top: 496.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #121217ff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
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
}
