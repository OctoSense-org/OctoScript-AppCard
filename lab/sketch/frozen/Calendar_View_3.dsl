// FROZEN compile of ⟶ [Calendar] View #3 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffff }
    RoundedShadowView{ width: 375.0 height: 660.0 margin: Inset{left: 0.0 right: 0 top: 162.0 bottom: 0} draw_bg.shadow_color: #3b4a7433 draw_bg.shadow_radius: 18.0 draw_bg.shadow_offset: vec2(0.0, 3.0) draw_bg.color: #ffffffff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 305.0 height: 40.0 margin: Inset{left: 35.0 right: 0 top: 702.5 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 6.0 }
    RoundedView{ width: 48.8 height: 19.2 margin: Inset{left: 67.5 right: 0 top: 712.9 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 223.7 height: 14.0 margin: Inset{left: 128.6 right: 0 top: 718.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "add to calendar" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 287.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 116.0 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 294.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "9:00 - 11:00 AM" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 326.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 216.2 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 333.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Wendsday, November 2019" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 365.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 119.0 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 372.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Meeting Room" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 404.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 98.0 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 411.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Description" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 290.0 height: 51.0 margin: Inset{left: 59.0 right: 0 top: 428.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "Insanity is doing the same thing, over and over again, but expecting different results." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.1 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 484.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 114.5 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 491.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Prototype link" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 290.0 height: 27.5 margin: Inset{left: 59.0 right: 0 top: 508.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "https://ui8.net/products/atro-mobile-ui-kit" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.1 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 541.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 112.0 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 548.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Video sharing" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 290.0 height: 28.0 margin: Inset{left: 59.0 right: 0 top: 564.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "zoom.us/meeting-#21345" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.1 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 600.5 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 100.0 height: 16.0 margin: Inset{left: 59.0 right: 0 top: 607.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Preparation" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 290.0 height: 48.0 margin: Inset{left: 59.0 right: 0 top: 624.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "You will be notified 15 minute before the meeting" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.1 } } }
    RoundedView{ width: 375.0 height: 1.0 margin: Inset{left: 0.0 right: 0 top: 264.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 72.5 height: 17.0 margin: Inset{left: 20.0 right: 0 top: 187.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Invited" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 27.5 height: 30.0 margin: Inset{left: 47.6 right: 0 top: 207.0 bottom: 0} draw_bg.color: #ffffff5e draw_bg.border_radius: 5.5 }
    RoundedView{ width: 27.5 height: 30.0 margin: Inset{left: 20.0 right: 0 top: 207.0 bottom: 0} draw_bg.color: #ffffff5e draw_bg.border_radius: 5.5 }
    RoundedView{ width: 27.5 height: 30.0 margin: Inset{left: 75.2 right: 0 top: 207.0 bottom: 0} draw_bg.color: #ffffff5e draw_bg.border_radius: 5.5 }
    RoundedView{ width: 27.5 height: 30.0 margin: Inset{left: 102.8 right: 0 top: 207.0 bottom: 0} draw_bg.color: #ffffff5e draw_bg.border_radius: 5.5 }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 130.5 right: 0 top: 207.0 bottom: 0} draw_bg.color: #ffffff66 draw_bg.border_radius: 15.0 }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 130.5 right: 0 top: 207.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 10.3 height: 10.3 margin: Inset{left: 140.3 right: 0 top: 216.8 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 142.3 right: 0 top: 218.8 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 342.5 height: 73.5 margin: Inset{left: 20.0 right: 0 top: 86.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fill height: Fit text: "Mobile App nav patterns explorations" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 14.9 } } }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #121217eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #131315eb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #121217ff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 375.0 height: 90.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ffffffff }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 331.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 299.5 right: 0 top: 36.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 20.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff856 }
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
