// FROZEN compile of ⟶ [Onboarding] View #4 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #6b999fff }
    RoundedView{ width: 9.2 height: 2.0 margin: Inset{left: 161.0 right: 0 top: 625.5 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 9.2 height: 2.0 margin: Inset{left: 190.2 right: 0 top: 625.5 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 9.2 height: 2.0 margin: Inset{left: 204.8 right: 0 top: 625.5 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 9.2 height: 2.0 margin: Inset{left: 175.6 right: 0 top: 625.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.0 }
    RoundedView{ width: 309.5 height: 50.0 margin: Inset{left: 34.0 right: 0 top: 650.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 49.5 height: 24.0 margin: Inset{left: 67.0 right: 0 top: 663.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.8 height: 10.9 margin: Inset{left: 86.9 right: 0 top: 666.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/f71046c38c027cbd.png") }
    Image{ width: 22.7 height: 7.0 margin: Inset{left: 80.4 right: 0 top: 673.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e032a7553facc737.png") }
    View{ width: 199.7 height: 16.0 margin: Inset{left: 128.9 right: 0 top: 670.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "enable microphone" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 236.5 height: 16.0 margin: Inset{left: 80.8 right: 0 top: 720.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Already have an account? Sign In" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 320.0 height: 53.0 margin: Inset{left: 32.5 right: 0 top: 557.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 146.9 height: 16.0 margin: Inset{left: 121.0 right: 0 top: 532.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Rule of thirds" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 375.0 height: 418.0 margin: Inset{left: 0.0 right: 0 top: 69.5 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #000000ff }
    RoundedShadowView{ width: 240.5 height: 520.0 margin: Inset{left: 67.0 right: 0 top: -43.0 bottom: 0} draw_bg.shadow_color: #4162a94e draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 270.0 height: 538.0 margin: Inset{left: 52.5 right: 0 top: -51.0 bottom: 0} draw_bg.color: #393e45ff draw_bg.color_2: #0a0d10ff draw_bg.border_radius: 54.0 }
    RoundedView{ width: 15.3 height: 497.0 margin: Inset{left: 72.5 right: 0 top: -34.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 29.4 margin: Inset{left: 72.5 right: 0 top: -34.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 29.4 margin: Inset{left: 72.5 right: 0 top: 433.6 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 8.0 height: 443.1 margin: Inset{left: 72.5 right: 0 top: -8.3 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 }
    RoundedView{ width: 15.3 height: 494.0 margin: Inset{left: 286.5 right: 0 top: -34.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 29.1 margin: Inset{left: 286.5 right: 0 top: -34.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 29.1 margin: Inset{left: 286.5 right: 0 top: 430.9 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 8.0 height: 440.4 margin: Inset{left: 286.5 right: 0 top: -8.5 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 }
    RoundedView{ width: 15.3 height: 235.0 margin: Inset{left: 178.8 right: 0 top: 359.1 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 34.5 margin: Inset{left: 178.8 right: 0 top: 359.1 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 34.5 margin: Inset{left: 178.8 right: 0 top: 559.6 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 8.0 height: 171.4 margin: Inset{left: 178.8 right: 0 top: 389.4 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 }
    RoundedView{ width: 15.3 height: 243.0 margin: Inset{left: 179.5 right: 0 top: -158.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 35.8 margin: Inset{left: 179.5 right: 0 top: -158.0 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 15.3 height: 35.8 margin: Inset{left: 179.5 right: 0 top: 49.2 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 draw_bg.border_radius: 3.1 }
    RoundedView{ width: 8.0 height: 177.3 margin: Inset{left: 179.5 right: 0 top: -126.8 bottom: 0} draw_bg.color: #ffffff00 draw_bg.color_2: #ffffff8c draw_bg.gradient_fill_horizontal: 1.0 }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/d5c153885dd141a3.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/dbbd9db129e5adec.png") }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffff66 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/f9e85dd1496baadf.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/47adc1dc07e11640.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
}
