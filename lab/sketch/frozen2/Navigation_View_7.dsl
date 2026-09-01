// FROZEN compile of ⟶ [Navigation] View #7 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: -65.5 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    Image{ width: 812.0 height: 88.5 margin: Inset{left: -75.5 right: 0 top: 361.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/ed371c3e8f724bb8.png") }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 315.5 right: 0 top: 370.5 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 15.0 }
    RoundedView{ width: 6.5 height: 6.5 margin: Inset{left: 327.3 right: 0 top: 382.3 bottom: 0} draw_bg.color: #1c8ff800 }
    RoundedView{ width: 27.0 height: 27.0 margin: Inset{left: -47.5 right: 0 top: 405.5 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 19.7 height: 19.7 margin: Inset{left: -44.1 right: 0 top: 409.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/425c526858072868.png") }
    RoundedView{ width: 30.0 height: 30.0 margin: Inset{left: 630.0 right: 0 top: 402.5 bottom: 0} draw_bg.color: #212b36ff draw_bg.border_radius: 15.0 }
    View{ width: 50.8 height: 16.0 margin: Inset{left: 170.0 right: 0 top: 412.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Places" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 65.0 height: 16.0 margin: Inset{left: 251.5 right: 0 top: 412.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Settings" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 68.8 height: 16.0 margin: Inset{left: 344.5 right: 0 top: 412.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Messages" draw_text.color: #5882f2ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 48.4 height: 16.0 margin: Inset{left: 447.0 right: 0 top: 412.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Search" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9529b95a64a3d054.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #131315ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #13131566 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #131315ff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9555b9ae4e9df132.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/efd8e387ca373f22.png") }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/21f19e633b0d4992.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #121217ff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
}
