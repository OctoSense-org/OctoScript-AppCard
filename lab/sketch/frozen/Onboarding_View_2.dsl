// FROZEN compile of ⟶ [Onboarding] View #2 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #2087f2ff draw_bg.color_2: #001c51ff draw_bg.border_size: 2.5 draw_bg.border_color: #ff0000ff }
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f264d draw_bg.color_2: #140f26ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #6c7580ff draw_bg.color_2: #262b34ff }
    RoundedView{ width: 329.5 height: 332.0 margin: Inset{left: 20.0 right: 0 top: 153.5 bottom: 0} draw_bg.color: #00000000 draw_bg.color_2: #ffffffff draw_bg.border_radius: 65.9 }
    RoundedView{ width: 294.5 height: 288.5 margin: Inset{left: 37.0 right: 0 top: 175.0 bottom: 0} draw_bg.color: #00000000 draw_bg.color_2: #ffffffff draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 57.7 }
    RoundedView{ width: 243.5 height: 248.5 margin: Inset{left: 62.5 right: 0 top: 195.0 bottom: 0} draw_bg.color: #00000000 draw_bg.color_2: #ffffffff draw_bg.border_radius: 48.7 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 151.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 191.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 211.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 171.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.0 }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 160.0 right: 0 top: 646.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 178.1 right: 0 top: 664.0 bottom: 0} draw_bg.color: #1c8ff856 }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 181.6 right: 0 top: 667.6 bottom: 0} draw_bg.color: #50a1ffff }
    View{ width: 268.8 height: 16.0 margin: Inset{left: 80.8 right: 0 top: 721.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Already have an account? Sign In" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 320.0 height: 53.0 margin: Inset{left: 32.5 right: 0 top: 581.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 } } }
    View{ width: 166.9 height: 16.0 margin: Inset{left: 121.0 right: 0 top: 556.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Rule of thirds" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 110.7 height: 261.6 margin: Inset{left: 128.7 right: 0 top: 189.0 bottom: 0} draw_bg.color: #ecf0f5ff draw_bg.color_2: #ccd6e6ff draw_bg.border_radius: 22.1 }
    Image{ width: 145.8 height: 162.1 margin: Inset{left: 114.6 right: 0 top: 238.6 bottom: 0} fit: ImageFit.CropToFill src: http_resource("http://127.0.0.1:8787/07ba47471dcfb1cf35c1f1c38d42614b382d9987.png") }
    RoundedShadowView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 243.7 bottom: 0} draw_bg.shadow_color: #ffffff34 draw_bg.shadow_radius: 1.0 draw_bg.shadow_offset: vec2(0.0, 1.0) draw_bg.color: #030303ff draw_bg.border_radius: 22.2 draw_bg.border_size: 1.0 draw_bg.border_color: #00000092 }
    RoundedView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 243.7 bottom: 0} draw_bg.color: #140f26ff draw_bg.border_radius: 22.2 }
    RoundedView{ width: 109.0 height: 7.8 margin: Inset{left: 129.4 right: 0 top: 243.7 bottom: 0} draw_bg.color: #ffffffcd draw_bg.color_2: #ffffff35 draw_bg.border_radius: 1.6 }
    RoundedView{ width: 109.0 height: 10.5 margin: Inset{left: 129.4 right: 0 top: 240.9 bottom: 0} draw_bg.color: #ffffffcd draw_bg.color_2: #ffffff35 draw_bg.border_radius: 5.2 }
    RoundedView{ width: 129.0 height: 152.5 margin: Inset{left: 119.2 right: 0 top: 243.7 bottom: 0} draw_bg.color: #ffffffcd draw_bg.color_2: #ffffff35 draw_bg.border_radius: 22.2 }
    RoundedView{ width: 88.0 height: 86.0 margin: Inset{left: 140.2 right: 0 top: 276.2 bottom: 0} draw_bg.color: #bb92ecff draw_bg.color_2: #55c3b2ff draw_bg.border_radius: 17.2 }
    RoundedView{ width: 109.0 height: 110.0 margin: Inset{left: 130.0 right: 0 top: 264.5 bottom: 0} draw_bg.color: #bb92ecff draw_bg.color_2: #55c3b2ff draw_bg.border_radius: 21.8 }
    RoundedView{ width: 57.0 height: 60.5 margin: Inset{left: 156.0 right: 0 top: 289.0 bottom: 0} draw_bg.color: #bb92ecff draw_bg.color_2: #55c3b2ff draw_bg.border_radius: 11.4 }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 162.0 right: 0 top: 297.0 bottom: 0} draw_bg.color: #1c8ff856 }
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
