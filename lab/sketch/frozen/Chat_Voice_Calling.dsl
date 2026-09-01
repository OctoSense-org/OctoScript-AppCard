// FROZEN compile of ⟶ [Chat] Voice Calling — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2691 }
    RoundedView{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 337.4 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 37.5 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 7.4 }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ffff }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 38.5 right: 0 top: 422.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 66.0 right: 0 top: 437.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 53.5 right: 0 top: 491.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Add to call" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 138.5 right: 0 top: 422.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 166.0 right: 0 top: 437.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 153.5 right: 0 top: 491.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Speaker" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 238.5 right: 0 top: 422.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 266.0 right: 0 top: 437.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 253.5 right: 0 top: 491.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Keypad" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 38.5 right: 0 top: 522.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 66.0 right: 0 top: 537.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 53.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Chat" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 138.5 right: 0 top: 522.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 166.0 right: 0 top: 537.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 153.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Video call" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 100.0 height: 100.0 margin: Inset{left: 238.5 right: 0 top: 522.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 266.0 right: 0 top: 537.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 94.0 height: 19.0 margin: Inset{left: 253.5 right: 0 top: 591.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Mute" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 75.0 height: 75.0 margin: Inset{left: 150.0 right: 0 top: 176.0 bottom: 0} draw_bg.color: #d8d8d8ff draw_bg.border_size: 0.5 draw_bg.border_color: #979797ff }
    RoundedView{ width: 75.0 height: 75.0 margin: Inset{left: 150.0 right: 0 top: 176.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 37.5 }
    View{ width: 211.9 height: 21.0 margin: Inset{left: 103.0 right: 0 top: 303.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "isabelle.barker@email.com" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 222.5 height: 31.0 margin: Inset{left: 98.8 right: 0 top: 273.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Isabelle Barker" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 14.9 } } }
    View{ width: 49.5 height: 19.5 margin: Inset{left: 174.8 right: 0 top: 333.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "2:35" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 300.0 height: 50.0 margin: Inset{left: 37.5 right: 0 top: 687.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 25.0 }
    RoundedView{ width: 48.0 height: 24.0 margin: Inset{left: 69.5 right: 0 top: 700.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 220.0 height: 16.0 margin: Inset{left: 129.5 right: 0 top: 707.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "End Call" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
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
