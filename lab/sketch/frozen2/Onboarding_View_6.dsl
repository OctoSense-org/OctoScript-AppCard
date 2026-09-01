// FROZEN compile of ⟶ [Onboarding] View #6 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2680 }
    RoundedView{ width: 320.0 height: 365.0 margin: Inset{left: 25.0 right: 0 top: 392.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 75.0 height: 75.0 margin: Inset{left: 147.5 right: 0 top: 452.0 bottom: 0} draw_bg.color: #45e994ff draw_bg.color_2: #23bcbaff draw_bg.gradient_angle: 30.0 draw_bg.border_radius: 7.5 }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 162.5 right: 0 top: 467.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 29.0 height: 21.0 margin: Inset{left: 170.5 right: 0 top: 479.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/2bd77ccda8b0a4e1.png") }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 301.0 right: 0 top: 412.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 308.5 right: 0 top: 419.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e78b0d8db25b08ae.png") }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 308.5 right: 0 top: 419.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9ff34e085a97ce9a.png") }
    RoundedView{ width: 320.0 height: 60.0 margin: Inset{left: 25.0 right: 0 top: 697.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 320.0 height: 1.2 margin: Inset{left: 25.0 right: 0 top: 697.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    RoundedView{ width: 51.2 height: 28.8 margin: Inset{left: 159.4 right: 0 top: 712.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 206.5 height: 18.0 margin: Inset{left: 91.2 right: 0 top: 721.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Continue ➝" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 290.0 height: 75.5 margin: Inset{left: 45.0 right: 0 top: 582.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 205.7 height: 16.0 margin: Inset{left: 91.8 right: 0 top: 557.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Connected to cloud" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 320.0 height: 365.0 margin: Inset{left: 360.0 right: 0 top: 392.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 75.0 height: 75.0 margin: Inset{left: 482.5 right: 0 top: 472.0 bottom: 0} draw_bg.color: #645affff draw_bg.color_2: #a573ffff draw_bg.gradient_angle: -134.3 draw_bg.border_radius: 37.5 }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 497.5 right: 0 top: 487.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 21.0 height: 3.2 margin: Inset{left: 509.5 right: 0 top: 516.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/76fb558b82734789.png") }
    Image{ width: 21.0 height: 26.0 margin: Inset{left: 509.5 right: 0 top: 496.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/53b0ea24ed815ddc.png") }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 636.0 right: 0 top: 457.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 643.5 right: 0 top: 464.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e78b0d8db25b08ae.png") }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 643.5 right: 0 top: 464.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9ff34e085a97ce9a.png") }
    View{ width: 290.0 height: 75.5 margin: Inset{left: 380.0 right: 0 top: 602.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 146.9 height: 16.0 margin: Inset{left: 453.5 right: 0 top: 577.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Rule of thirds" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/7c12dd4cca557c00.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e9e64c9a5ee483a3.png") }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffff66 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/cc739ac0f046b01c.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/97cd7612f21eac70.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
}
