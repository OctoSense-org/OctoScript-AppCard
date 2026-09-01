// FROZEN compile of ⟶ [Navigation] View #8 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 381.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2675 draw_bg.border_radius: 75.0 }
    RoundedView{ width: 375.0 height: 360.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f26a5 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 145.0 height: 33.0 margin: Inset{left: 115.0 right: 0 top: 348.5 bottom: 0} draw_bg.color: #140f2698 draw_bg.border_radius: 6.6 }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 180.0 right: 0 top: 356.5 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 300.0 height: 40.0 margin: Inset{left: 37.5 right: 0 top: 291.0 bottom: 0} draw_bg.color: #ffffff80 draw_bg.border_radius: 20.0 }
    RoundedView{ width: 22.1 height: 24.0 margin: Inset{left: 306.1 right: 0 top: 299.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 114.0 height: 17.0 margin: Inset{left: 56.0 right: 0 top: 305.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Find something..." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 162.2 right: 0 top: 192.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 177.6 right: 0 top: 210.1 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 181.1 right: 0 top: 213.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 74.0 height: 15.0 margin: Inset{left: 162.5 right: 0 top: 257.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Gallery" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 53.2 right: 0 top: 192.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 68.5 right: 0 top: 210.1 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 72.1 right: 0 top: 213.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 66.0 height: 15.0 margin: Inset{left: 57.5 right: 0 top: 257.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "alerts" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 271.2 right: 0 top: 192.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 286.6 right: 0 top: 210.1 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 290.1 right: 0 top: 213.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 77.5 height: 15.0 margin: Inset{left: 269.8 right: 0 top: 257.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Settings" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 53.2 right: 0 top: 90.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 68.5 right: 0 top: 108.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 72.1 right: 0 top: 111.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 83.5 height: 15.0 margin: Inset{left: 48.8 right: 0 top: 155.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Messages" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 162.2 right: 0 top: 90.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 177.6 right: 0 top: 108.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 181.1 right: 0 top: 111.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 82.0 height: 15.0 margin: Inset{left: 158.5 right: 0 top: 155.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Trending" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 49.9 height: 54.2 margin: Inset{left: 271.2 right: 0 top: 90.4 bottom: 0} draw_bg.color: #f4f6f9eb draw_bg.border_radius: 10.0 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 286.6 right: 0 top: 108.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 290.1 right: 0 top: 111.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 96.0 height: 15.0 margin: Inset{left: 260.5 right: 0 top: 155.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Bookmarks" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 375.0 height: 90.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #121217ff }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 331.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 20.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 15.0 height: 13.5 margin: Inset{left: 345.0 right: 0 top: 44.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 3.5 }
    View{ width: 35.5 height: 15.0 margin: Inset{left: 347.1 right: 0 top: 46.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "21" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
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
