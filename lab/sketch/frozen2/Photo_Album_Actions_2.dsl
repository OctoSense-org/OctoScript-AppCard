// FROZEN compile of ⟶ [Photo] Album Actions#2 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 34.5 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2680 }
    RoundedView{ width: 355.0 height: 490.0 margin: Inset{left: 10.0 right: 0 top: 202.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    RoundedView{ width: 90.0 height: 135.0 margin: Inset{left: 20.0 right: 0 top: 212.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 9.0 }
    RoundedView{ width: 21.6 height: 32.4 margin: Inset{left: 79.4 right: 0 top: 301.1 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 21.6 height: 32.4 margin: Inset{left: 79.4 right: 0 top: 301.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e346736a7ae012bf.png") }
    RoundedView{ width: 118.5 height: 135.0 margin: Inset{left: 115.0 right: 0 top: 212.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 11.8 }
    RoundedView{ width: 28.4 height: 32.4 margin: Inset{left: 193.2 right: 0 top: 301.1 bottom: 0} draw_bg.color: #1c8ff800 }
    RoundedView{ width: 116.5 height: 135.0 margin: Inset{left: 238.5 right: 0 top: 212.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 11.7 }
    RoundedView{ width: 27.9 height: 32.4 margin: Inset{left: 315.4 right: 0 top: 301.1 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 27.9 height: 32.4 margin: Inset{left: 315.4 right: 0 top: 301.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/70b717898f8eafff.png") }
    RoundedView{ width: 213.5 height: 135.0 margin: Inset{left: 20.0 right: 0 top: 352.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 13.5 }
    RoundedView{ width: 51.2 height: 32.4 margin: Inset{left: 160.9 right: 0 top: 441.1 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 51.2 height: 32.4 margin: Inset{left: 160.9 right: 0 top: 441.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/5c888d2d85817447.png") }
    RoundedView{ width: 116.5 height: 135.0 margin: Inset{left: 238.5 right: 0 top: 352.0 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 11.7 }
    RoundedView{ width: 27.9 height: 32.4 margin: Inset{left: 315.4 right: 0 top: 441.1 bottom: 0} draw_bg.color: #1c8ff800 }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 492.0 bottom: 0} draw_bg.color: #4c5fefff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 512.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "View albums" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 542.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 542.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 562.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Move to library" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 592.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 592.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 612.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Share with..." draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 642.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 642.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 662.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Take photo" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 707.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 10.0 }
    RoundedView{ width: 355.0 height: 50.0 margin: Inset{left: 10.0 right: 0 top: 707.0 bottom: 0} draw_bg.color: #4c5fefff }
    RoundedView{ width: 355.0 height: 1.0 margin: Inset{left: 10.0 right: 0 top: 707.0 bottom: 0} draw_bg.color: #f4f6f9ff }
    View{ width: 229.1 height: 16.0 margin: Inset{left: 83.3 right: 0 top: 727.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Close" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
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
