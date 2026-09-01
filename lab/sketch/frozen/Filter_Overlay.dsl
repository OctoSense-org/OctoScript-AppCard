// FROZEN compile of ⟶ [Filter] Overlay — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #2f2f3eff }
    RoundedShadowView{ width: 330.0 height: 714.5 margin: Inset{left: 22.5 right: 0 top: 57.5 bottom: 0} draw_bg.shadow_color: #4162a94e draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff draw_bg.border_radius: 16.5 }
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2699 }
    RoundedShadowView{ width: 375.0 height: 423.0 margin: Inset{left: 0.0 right: 0 top: 388.5 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffeb draw_bg.border_radius: 75.0 }
    RoundedShadowView{ width: 375.0 height: 399.6 margin: Inset{left: 0.0 right: 0 top: 411.9 bottom: 0} draw_bg.shadow_color: #3b4a7424 draw_bg.shadow_radius: 14.5 draw_bg.shadow_offset: vec2(0.0, 1.5) draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 23.6 height: 199.0 margin: Inset{left: 175.5 right: 0 top: 300.9 bottom: 0} draw_bg.color: #ffffffeb draw_bg.border_radius: 4.7 }
    RoundedView{ width: 25.0 height: 5.0 margin: Inset{left: 175.0 right: 0 top: 403.5 bottom: 0} draw_bg.color: #dfe5eeff draw_bg.border_radius: 2.5 }
    RoundedView{ width: 345.0 height: 50.0 margin: Inset{left: 15.0 right: 0 top: 711.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    View{ width: 253.0 height: 16.0 margin: Inset{left: 86.3 right: 0 top: 731.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "view results (171)" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 62.0 height: 17.0 margin: Inset{left: 25.0 right: 0 top: 436.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "filter content by" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 310.0 height: 1.0 margin: Inset{left: 65.0 right: 0 top: 507.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 473.0 bottom: 0} draw_bg.color: #1c8ff856 }
    View{ width: 85.5 height: 17.0 margin: Inset{left: 64.0 right: 0 top: 478.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Everything" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 476.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 335.5 right: 0 top: 477.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 476.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 310.0 height: 1.0 margin: Inset{left: 65.0 right: 0 top: 553.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 519.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 522.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 522.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 338.5 right: 0 top: 527.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 63.5 height: 17.0 margin: Inset{left: 64.0 right: 0 top: 524.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Photos" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 310.0 height: 1.0 margin: Inset{left: 65.0 right: 0 top: 599.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 565.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 568.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 568.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 338.5 right: 0 top: 573.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 62.0 height: 17.0 margin: Inset{left: 64.0 right: 0 top: 570.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Videos" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 310.0 height: 1.0 margin: Inset{left: 65.0 right: 0 top: 645.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 611.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 614.0 bottom: 0} draw_bg.color: #dfe5eeeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 335.5 right: 0 top: 615.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.0 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 614.0 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 3.6 }
    View{ width: 74.0 height: 17.0 margin: Inset{left: 64.0 right: 0 top: 616.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Contacts" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 20.0 right: 0 top: 657.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 660.0 bottom: 0} draw_bg.color: #4c5fefeb draw_bg.border_radius: 3.6 }
    RoundedView{ width: 18.0 height: 18.0 margin: Inset{left: 334.0 right: 0 top: 660.0 bottom: 0} draw_bg.color: #000000ff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 9.5 height: 7.0 margin: Inset{left: 338.5 right: 0 top: 665.5 bottom: 0} draw_bg.color: #000000eb draw_bg.border_radius: 1.4 }
    View{ width: 90.0 height: 17.0 margin: Inset{left: 64.0 right: 0 top: 663.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Documents" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
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
