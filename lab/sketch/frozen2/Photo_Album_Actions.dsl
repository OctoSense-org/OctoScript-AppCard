// FROZEN compile of ⟶ [Photo] Album Actions — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 34.5 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2680 }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/dbbd9db129e5adec.png") }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffff66 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/f9e85dd1496baadf.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/47adc1dc07e11640.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    RoundedShadowView{ width: 355.0 height: 410.0 margin: Inset{left: 10.0 right: 0 top: 232.0 bottom: 0} draw_bg.shadow_color: #3b4a7486 draw_bg.shadow_radius: 21.5 draw_bg.shadow_offset: vec2(0.0, 5.5) draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    RoundedView{ width: 50.0 height: 25.5 margin: Inset{left: 162.5 right: 0 top: 201.5 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 19.9 height: 8.0 margin: Inset{left: 177.4 right: 0 top: 213.2 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/5eac26569d877ef5.png") }
    RoundedView{ width: 355.0 height: 100.0 margin: Inset{left: 10.0 right: 0 top: 657.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 707.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 707.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 727.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Delete" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 657.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 657.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 677.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Move to albums" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/d5c153885dd141a3.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
}
