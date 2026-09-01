// FROZEN compile of ⟶ [Onboarding] View #7 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #d8d8d8ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f2680 }
    RoundedView{ width: 355.0 height: 450.0 margin: Inset{left: 10.0 right: 0 top: 307.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 20.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 321.0 right: 0 top: 327.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 334.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e78b0d8db25b08ae.png") }
    Image{ width: 9.5 height: 9.5 margin: Inset{left: 328.5 right: 0 top: 334.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9ff34e085a97ce9a.png") }
    Image{ width: 110.7 height: 261.6 margin: Inset{left: 128.7 right: 0 top: 304.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/df15b17418c78fe6.png") }
    Image{ width: 145.8 height: 162.1 margin: Inset{left: 114.6 right: 0 top: 353.6 bottom: 0} fit: ImageFit.CropToFill src: http_resource("http://127.0.0.1:8787/07ba47471dcfb1cf35c1f1c38d42614b382d9987.png") }
    RoundedShadowView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 358.6 bottom: 0} draw_bg.shadow_color: #ffffff34 draw_bg.shadow_radius: 1.0 draw_bg.shadow_offset: vec2(0.0, 1.0) draw_bg.color: #030303ff draw_bg.border_radius: 22.2 draw_bg.border_size: 1.0 draw_bg.border_color: #00000092 }
    RoundedView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 358.6 bottom: 0} draw_bg.color: #140f26ff draw_bg.border_radius: 22.2 }
    Image{ width: 109.0 height: 7.8 margin: Inset{left: 129.4 right: 0 top: 358.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/ffa9717b3ad505f3.png") }
    Image{ width: 79.0 height: 84.0 margin: Inset{left: 147.8 right: 0 top: 395.2 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/5b5a795d5c0b61d2.png") }
    Image{ width: 104.0 height: 110.5 margin: Inset{left: 135.5 right: 0 top: 382.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/698345607ed856fc.png") }
    Image{ width: 57.0 height: 60.5 margin: Inset{left: 159.0 right: 0 top: 407.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/1e52d84ed500f486.png") }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 165.0 right: 0 top: 415.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 26.0 height: 23.0 margin: Inset{left: 174.5 right: 0 top: 426.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/bbb492ed425b5791.png") }
    RoundedView{ width: 243.0 height: 50.0 margin: Inset{left: 66.0 right: 0 top: 682.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 25.0 }
    RoundedView{ width: 38.9 height: 24.0 margin: Inset{left: 241.8 right: 0 top: 695.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 14.1 height: 17.5 margin: Inset{left: 254.6 right: 0 top: 698.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/84020b246c4cb1b7.png") }
    View{ width: 156.8 height: 16.0 margin: Inset{left: 94.3 right: 0 top: 702.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "pair watch" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 305.0 height: 75.5 margin: Inset{left: 40.0 right: 0 top: 568.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #6c7b8aff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 146.9 height: 16.0 margin: Inset{left: 121.0 right: 0 top: 543.5 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Rule of thirds" draw_text.color: #140f26ff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
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
