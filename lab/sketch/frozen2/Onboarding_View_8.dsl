// FROZEN compile of ⟶ [Onboarding] View #8 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    Image{ width: 147.0 height: 47.5 margin: Inset{left: 114.0 right: 0 top: 358.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e56930c20dd42527.png") }
    RoundedView{ width: 20.0 height: 17.6 margin: Inset{left: 272.5 right: 0 top: 360.0 bottom: 0} draw_bg.color: #140f2693 draw_bg.border_radius: 2.2 }
    RoundedView{ width: 3.5 height: 8.8 margin: Inset{left: 272.5 right: 0 top: 373.2 bottom: 0} draw_bg.color: #140f2693 }
    Image{ width: 20.0 height: 22.0 margin: Inset{left: 272.5 right: 0 top: 360.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/3a24618db34b5d26.png") }
    View{ width: 18.6 height: 15.7 margin: Inset{left: 274.1 right: 0 top: 363.9 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "UI" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    View{ width: 236.5 height: 16.0 margin: Inset{left: 80.8 right: 0 top: 757.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Already have an account? Sign In" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 41.5 right: 0 top: 677.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 102.0 right: 0 top: 697.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Sign Up" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    View{ width: 19.2 height: 17.0 margin: Inset{left: 178.8 right: 0 top: 651.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "OR" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 5.6 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 41.5 right: 0 top: 586.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 72.7 right: 0 top: 599.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 29.5 height: 12.3 margin: Inset{left: 81.5 right: 0 top: 605.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/712f361167b87621.png") }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 131.2 right: 0 top: 606.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Login with Twitter" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 41.5 right: 0 top: 521.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 72.7 right: 0 top: 534.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 14.8 height: 16.2 margin: Inset{left: 88.3 right: 0 top: 538.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/a4ee12e2b483a899.png") }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 131.2 right: 0 top: 541.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Login with Facebook" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    RoundedView{ width: 292.5 height: 50.0 margin: Inset{left: 41.5 right: 0 top: 456.0 bottom: 0} draw_bg.color: #4c5fefff draw_bg.border_radius: 7.5 }
    RoundedView{ width: 46.8 height: 24.0 margin: Inset{left: 72.7 right: 0 top: 469.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 25.4 height: 15.8 margin: Inset{left: 83.4 right: 0 top: 472.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/4e0757cde33b390f.png") }
    View{ width: 188.8 height: 16.0 margin: Inset{left: 131.2 right: 0 top: 476.0 bottom: 0} flow: Down align: Align{x: 0.0} Label{ width: Fit height: Fit text: "Login with Apple" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
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
