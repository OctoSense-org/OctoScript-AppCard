// FROZEN compile of ⟶ [Account] Success Overlay — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2699 }
    RoundedView{ width: 355.0 height: 500.0 margin: Inset{left: 10.0 right: 0 top: 257.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 41.5 right: 0 top: 682.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 25.0 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 164.3 right: 0 top: 695.0 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 102.0 right: 0 top: 702.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Close" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    Image{ width: 123.2 height: 65.0 margin: Inset{left: 122.2 right: 0 top: 413.2 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/429b948bad3af69c.png") }
    Image{ width: 32.6 height: 37.5 margin: Inset{left: 176.9 right: 0 top: 443.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e53096dcc0d6fc6b.png") }
    Image{ width: 50.0 height: 80.0 margin: Inset{left: 162.6 right: 0 top: 384.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/b6d2da08d03e700e.png") }
    Image{ width: 27.6 height: 43.0 margin: Inset{left: 181.9 right: 0 top: 436.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/d299020d27f8fab9.png") }
    Image{ width: 26.1 height: 14.9 margin: Inset{left: 183.9 right: 0 top: 476.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/8fe8119f7a8359e2.png") }
    Image{ width: 31.5 height: 35.9 margin: Inset{left: 141.0 right: 0 top: 397.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/cad1404d1f366ab9.png") }
    Image{ width: 12.0 height: 8.8 margin: Inset{left: 150.9 right: 0 top: 410.2 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/4c3e9d473879aa2c.png") }
    View{ width: 310.0 height: 75.5 margin: Inset{left: 37.5 right: 0 top: 579.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "You will shortly receive an email with a link to a web page where you will be able to set up a new password for your account." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 282.5 height: 55.0 margin: Inset{left: 89.5 right: 0 top: 520.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Your password has been reset" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 12.4 } } }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e9e64c9a5ee483a3.png") }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffff66 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/cc739ac0f046b01c.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/97cd7612f21eac70.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/7c12dd4cca557c00.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
}
