// FROZEN compile of ⟶ [Photo] Crop — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #ff0002ff }
    Image{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/02866067d23f8354.png") }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 20.0 right: 0 top: 83.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 345.0 right: 0 top: 83.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 20.0 right: 0 top: 493.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 5.0 }
    RoundedView{ width: 10.0 height: 10.0 margin: Inset{left: 345.0 right: 0 top: 493.5 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 5.0 }
    Image{ width: 260.5 height: 13.5 margin: Inset{left: 58.0 right: 0 top: 565.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/04bb9d897c44d2df.png") }
    RoundedView{ width: 1.5 height: 25.0 margin: Inset{left: 187.0 right: 0 top: 559.5 bottom: 0} draw_bg.color: #ffdf9dff draw_bg.border_radius: 0.8 }
    RoundedView{ width: 79.0 height: 20.0 margin: Inset{left: 187.5 right: 0 top: 527.5 bottom: 0} draw_bg.color: #140f2693 draw_bg.border_radius: 5.0 }
    RoundedView{ width: 14.1 height: 10.0 margin: Inset{left: 187.5 right: 0 top: 542.5 bottom: 0} draw_bg.color: #140f2693 }
    Image{ width: 79.0 height: 25.0 margin: Inset{left: 187.5 right: 0 top: 527.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/b416515aaa88a7d3.png") }
    View{ width: 73.4 height: 17.0 margin: Inset{left: 193.7 right: 0 top: 532.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "rotate -10°" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 70.0 height: 70.0 margin: Inset{left: 152.5 right: 0 top: 667.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 35.0 }
    RoundedView{ width: 24.0 height: 24.0 margin: Inset{left: 175.5 right: 0 top: 690.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 5.0 height: 9.5 margin: Inset{left: 185.0 right: 0 top: 697.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/1a78307009573cd6.png") }
    RoundedView{ width: 15.0 height: 15.0 margin: Inset{left: 180.0 right: 0 top: 694.5 bottom: 0} draw_bg.color: #50a1ff00 }
    RoundedView{ width: 95.0 height: 35.0 margin: Inset{left: 37.0 right: 0 top: 602.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 17.5 }
    RoundedView{ width: 14.2 height: 21.0 margin: Inset{left: 44.6 right: 0 top: 609.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 7.7 height: 11.3 margin: Inset{left: 48.8 right: 0 top: 611.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/4d20c9354ee60c58.png") }
    Image{ width: 7.7 height: 11.3 margin: Inset{left: 46.5 right: 0 top: 615.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/69092f8f46bdd49a.png") }
    View{ width: 68.4 height: 21.4 margin: Inset{left: 62.6 right: 0 top: 611.8 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Crop" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 95.0 height: 35.0 margin: Inset{left: 140.0 right: 0 top: 602.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 17.5 }
    RoundedView{ width: 14.2 height: 21.0 margin: Inset{left: 147.6 right: 0 top: 609.0 bottom: 0} draw_bg.color: #1c8ff800 }
    View{ width: 68.4 height: 21.4 margin: Inset{left: 165.7 right: 0 top: 611.8 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Adjust" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 95.0 height: 35.0 margin: Inset{left: 243.0 right: 0 top: 602.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 17.5 }
    RoundedView{ width: 14.2 height: 21.0 margin: Inset{left: 250.6 right: 0 top: 609.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 7.7 height: 10.8 margin: Inset{left: 254.8 right: 0 top: 613.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/b3dc7eb23fa30783.png") }
    Image{ width: 6.3 height: 8.8 margin: Inset{left: 253.4 right: 0 top: 617.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/1c03ac9f29304bcc.png") }
    View{ width: 68.4 height: 21.4 margin: Inset{left: 268.6 right: 0 top: 611.8 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Filter" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 375.0 height: 90.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #121217ff }
    RoundedView{ width: 24.0 height: 30.9 margin: Inset{left: 20.0 right: 0 top: 36.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 4.7 height: 6.0 margin: Inset{left: 29.9 right: 0 top: 48.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9697cd323027aa7d.png") }
    Image{ width: 4.7 height: 6.0 margin: Inset{left: 29.9 right: 0 top: 48.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/c50c962fe6723ed7.png") }
    View{ width: 83.1 height: 18.9 margin: Inset{left: 279.5 right: 0 top: 45.0 bottom: 0} flow: Down align: Align{x: 1.0} Label{ width: Fit height: Fit text: "Save photo" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
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
