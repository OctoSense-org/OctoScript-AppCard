// FROZEN compile of ⟶ [Alerts] View #9 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2699 }
    RoundedView{ width: 355.0 height: 500.0 margin: Inset{left: 10.0 right: 0 top: 257.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    Image{ width: 150.3 height: 85.2 margin: Inset{left: 92.7 right: 0 top: 366.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/612be3c9f139c6f4.png") }
    Image{ width: 9.7 height: 33.0 margin: Inset{left: 182.7 right: 0 top: 433.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/af5d938d987a58d1.png") }
    Image{ width: 68.5 height: 44.0 margin: Inset{left: 158.4 right: 0 top: 393.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/2cdee6168ee7e599.png") }
    Image{ width: 33.0 height: 44.0 margin: Inset{left: 141.8 right: 0 top: 393.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/935ee485904aac55.png") }
    Image{ width: 42.7 height: 5.0 margin: Inset{left: 132.5 right: 0 top: 432.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/8c2de59c9dde1936.png") }
    Image{ width: 25.4 height: 37.0 margin: Inset{left: 204.1 right: 0 top: 374.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/6b12a1c712d13120.png") }
    Image{ width: 23.7 height: 14.8 margin: Inset{left: 151.5 right: 0 top: 411.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/7b0b75c32bed65f0.png") }
    Image{ width: 23.7 height: 14.8 margin: Inset{left: 151.5 right: 0 top: 406.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/7134b4bef19bb88d.png") }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 277.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 284.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9df0afcdb0e82232.png") }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 284.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/942271a300050bdc.png") }
    View{ width: 115.5 height: 21.0 margin: Inset{left: 132.8 right: 0 top: 712.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Remind me later" draw_text.color: #6e7982ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 39.0 right: 0 top: 651.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 25.0 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 161.8 right: 0 top: 664.0 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 99.5 right: 0 top: 671.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Try again..." draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 310.0 height: 78.0 margin: Inset{left: 37.5 right: 0 top: 567.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "Unfortunately at the moment our servers are not responding. Will be back soon" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 239.5 height: 58.0 margin: Inset{left: 73.5 right: 0 top: 502.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The email server is not responding" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 12.4 line_spacing: 2.0 } } }
    Image{ width: 375.0 height: 37.5 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/dbbd9db129e5adec.png") }
    RoundedView{ width: 1.1 height: 3.4 margin: Inset{left: 356.4 right: 0 top: 15.8 bottom: 0} draw_bg.color: #ffffff66 }
    RoundedView{ width: 14.4 height: 6.1 margin: Inset{left: 339.6 right: 0 top: 14.4 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.4 }
    Image{ width: 14.0 height: 9.9 margin: Inset{left: 319.0 right: 0 top: 12.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/f9e85dd1496baadf.png") }
    Image{ width: 15.0 height: 9.2 margin: Inset{left: 299.0 right: 0 top: 13.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/47adc1dc07e11640.png") }
    View{ width: 55.9 height: 16.0 margin: Inset{left: 25.0 right: 0 top: 14.5 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Atro UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.4 } } }
    Image{ width: 375.0 height: 37.0 margin: Inset{left: 0.0 right: 0 top: 775.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/d5c153885dd141a3.png") }
    RoundedView{ width: 100.0 height: 4.0 margin: Inset{left: 137.5 right: 0 top: 798.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 2.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 30.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 773.0 bottom: 0} draw_bg.color: #50a1ff00 }
}
