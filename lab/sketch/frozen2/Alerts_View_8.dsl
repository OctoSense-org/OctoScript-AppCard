// FROZEN compile of ⟶ [Alerts] View #8 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2699 }
    RoundedView{ width: 355.0 height: 500.0 margin: Inset{left: 10.0 right: 0 top: 257.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    Image{ width: 122.9 height: 59.2 margin: Inset{left: 124.0 right: 0 top: 383.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/3ad43917797b16cc.png") }
    Image{ width: 10.4 height: 18.2 margin: Inset{left: 181.0 right: 0 top: 385.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/81b400a147bfb12c.png") }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 179.0 right: 0 top: 444.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 7.5 draw_bg.border_size: 1.5 draw_bg.border_color: #a3bfc6ff }
    Image{ width: 57.3 height: 54.5 margin: Inset{left: 158.0 right: 0 top: 394.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/6baf902715c206af.png") }
    Image{ width: 62.5 height: 7.8 margin: Inset{left: 155.5 right: 0 top: 444.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/2910a17b4b08e998.png") }
    Image{ width: 31.5 height: 35.9 margin: Inset{left: 193.5 right: 0 top: 378.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/4183404db897bad0.png") }
    Image{ width: 15.5 height: 3.5 margin: Inset{left: 201.5 right: 0 top: 392.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/50b9783a4ff05d0b.png") }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 277.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 284.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e78b0d8db25b08ae.png") }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 284.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9ff34e085a97ce9a.png") }
    View{ width: 115.5 height: 21.0 margin: Inset{left: 132.8 right: 0 top: 712.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Remind me later" draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 39.0 right: 0 top: 651.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 25.0 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 161.8 right: 0 top: 664.0 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 99.5 right: 0 top: 671.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Enable notifications" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 310.0 height: 78.0 margin: Inset{left: 37.5 right: 0 top: 567.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "Your device is not connect to internet, please make sure your connection is working." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 239.5 height: 58.0 margin: Inset{left: 73.5 right: 0 top: 502.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "Don’t miss out the important stuff" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-SemiBold.ttf") asc: 0.0 desc: 0.0 } } font_size: 12.4 line_spacing: 2.0 } } }
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
