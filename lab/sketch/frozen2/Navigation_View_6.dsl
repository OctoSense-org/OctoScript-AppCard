// FROZEN compile of ⟶ [Navigation] View #6 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedShadowView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.shadow_color: #4162a94f draw_bg.shadow_radius: 35.0 draw_bg.shadow_offset: vec2(-1.5, 0.0) draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f26cc }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 300.0 right: 0 top: 602.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 318.1 right: 0 top: 620.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 3.2 height: 3.2 margin: Inset{left: 329.8 right: 0 top: 631.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/0837d7f25ad89cce.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 321.6 right: 0 top: 623.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 60.5 height: 17.0 margin: Inset{left: 225.0 right: 0 top: 624.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "search" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 300.0 right: 0 top: 392.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 318.1 right: 0 top: 410.1 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 5.2 height: 5.2 margin: Inset{left: 325.1 right: 0 top: 417.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/aa94c0305de7f6bc.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 321.6 right: 0 top: 413.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 57.8 height: 17.0 margin: Inset{left: 227.5 right: 0 top: 413.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "places" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 300.0 right: 0 top: 462.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 318.1 right: 0 top: 480.1 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 13.8 height: 13.8 margin: Inset{left: 320.4 right: 0 top: 482.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/1dd9937872548d7e.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 321.6 right: 0 top: 483.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 72.1 height: 17.0 margin: Inset{left: 214.5 right: 0 top: 484.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "Settings" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 300.0 right: 0 top: 532.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 318.1 right: 0 top: 550.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 11.0 height: 11.0 margin: Inset{left: 322.0 right: 0 top: 554.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/24680e88efd4740e.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 321.6 right: 0 top: 553.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 79.8 height: 17.0 margin: Inset{left: 207.5 right: 0 top: 554.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "Messages" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 6.8 } } }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 300.0 right: 0 top: 682.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 318.1 right: 0 top: 700.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 7.5 height: 7.5 margin: Inset{left: 323.9 right: 0 top: 706.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/beb2981412bf402c.png") }
    Image{ width: 7.5 height: 7.5 margin: Inset{left: 323.9 right: 0 top: 706.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e12496a50ca18fad.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 321.6 right: 0 top: 703.6 bottom: 0} draw_bg.color: #50a1ff00 }
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
