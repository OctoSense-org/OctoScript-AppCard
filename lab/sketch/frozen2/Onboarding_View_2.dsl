// FROZEN compile of ⟶ [Onboarding] View #2 — spec2dsl.py.
// A poster, not an app: no roles, no data, no theme.
View{ flow: Overlay width: 375 height: 812 draw_bg.color: #ffffffff
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #2087f2ff draw_bg.color_2: #001c51ff draw_bg.border_size: 2.5 draw_bg.border_color: #ff0000ff }
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #17212dff }
    RoundedView{ width: 375.0 height: 667.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #140f264d draw_bg.color_2: #140f26ff }
    RoundedView{ width: 375.0 height: 812.0 margin: Inset{left: 0.0 right: 0 top: 0.0 bottom: 0} draw_bg.color: #6c7580ff draw_bg.color_2: #262b34ff draw_bg.gradient_angle: 45.0 }
    Image{ width: 329.5 height: 332.0 margin: Inset{left: 20.0 right: 0 top: 153.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/45eb7dcbe82fc77e.png") }
    Image{ width: 294.5 height: 288.5 margin: Inset{left: 37.0 right: 0 top: 175.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/f35963528db1e909.png") }
    Image{ width: 243.5 height: 248.5 margin: Inset{left: 62.5 right: 0 top: 195.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/a61871e67898e2c0.png") }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 151.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 191.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 211.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffff99 draw_bg.border_radius: 1.0 }
    RoundedView{ width: 12.5 height: 2.0 margin: Inset{left: 171.5 right: 0 top: 500.0 bottom: 0} draw_bg.color: #ffffffff draw_bg.border_radius: 1.0 }
    RoundedView{ width: 55.0 height: 55.0 margin: Inset{left: 160.0 right: 0 top: 646.0 bottom: 0} draw_bg.color: #f4f6f9ff draw_bg.border_radius: 27.5 }
    RoundedView{ width: 18.9 height: 18.9 margin: Inset{left: 178.1 right: 0 top: 664.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 3.7 height: 7.5 margin: Inset{left: 188.9 right: 0 top: 670.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/19820cbdc9dab85e.png") }
    RoundedView{ width: 11.8 height: 11.8 margin: Inset{left: 181.6 right: 0 top: 667.6 bottom: 0} draw_bg.color: #50a1ff00 }
    View{ width: 236.5 height: 16.0 margin: Inset{left: 80.8 right: 0 top: 721.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Already have an account? Sign In" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 7.8 } } }
    View{ width: 320.0 height: 53.0 margin: Inset{left: 32.5 right: 0 top: 581.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fill height: Fit text: "The rule of thirds states that an image is most pleasing when its subjects or regions are ..." draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Regular.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.4 line_spacing: 2.0 } } }
    View{ width: 146.9 height: 16.0 margin: Inset{left: 121.0 right: 0 top: 556.0 bottom: 0} flow: Down align: Align{x: 0.5} Label{ width: Fit height: Fit text: "Rule of thirds" draw_text.color: #ffffffff draw_text.text_style: TextStyle{ font_family: FontFamily{ latin := FontMember{ res: crate_resource("makepad_widgets:resources/Montserrat-Medium.ttf") asc: 0.0 desc: 0.0 } } font_size: 8.1 } } }
    Image{ width: 110.7 height: 261.6 margin: Inset{left: 128.7 right: 0 top: 189.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/df15b17418c78fe6.png") }
    Image{ width: 145.8 height: 162.1 margin: Inset{left: 114.6 right: 0 top: 238.6 bottom: 0} fit: ImageFit.CropToFill src: http_resource("http://127.0.0.1:8787/07ba47471dcfb1cf35c1f1c38d42614b382d9987.png") }
    RoundedShadowView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 243.7 bottom: 0} draw_bg.shadow_color: #ffffff34 draw_bg.shadow_radius: 1.0 draw_bg.shadow_offset: vec2(0.0, 1.0) draw_bg.color: #030303ff draw_bg.border_radius: 22.2 draw_bg.border_size: 1.0 draw_bg.border_color: #00000092 }
    RoundedView{ width: 129.0 height: 152.5 margin: Inset{left: 119.4 right: 0 top: 243.7 bottom: 0} draw_bg.color: #140f26ff draw_bg.border_radius: 22.2 }
    Image{ width: 109.0 height: 7.8 margin: Inset{left: 129.4 right: 0 top: 243.7 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/ffa9717b3ad505f3.png") }
    Image{ width: 88.0 height: 86.0 margin: Inset{left: 140.2 right: 0 top: 276.2 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9a2cdee5995e958f.png") }
    Image{ width: 109.0 height: 110.0 margin: Inset{left: 130.0 right: 0 top: 264.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/c34ae6993ab68460.png") }
    Image{ width: 57.0 height: 60.5 margin: Inset{left: 156.0 right: 0 top: 289.0 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/addeacaec8f4237d.png") }
    RoundedView{ width: 45.0 height: 45.0 margin: Inset{left: 162.0 right: 0 top: 297.0 bottom: 0} draw_bg.color: #1c8ff800 }
    Image{ width: 15.1 height: 18.1 margin: Inset{left: 187.9 right: 0 top: 301.8 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/e1ffb172a6e25c47.png") }
    Image{ width: 16.1 height: 10.2 margin: Inset{left: 168.4 right: 0 top: 301.5 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/861abf6c911c858d.png") }
    Image{ width: 20.6 height: 12.1 margin: Inset{left: 179.1 right: 0 top: 304.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/87791d725f7fa230.png") }
    Image{ width: 6.4 height: 15.7 margin: Inset{left: 169.6 right: 0 top: 307.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/2b9fef0dd51d9206.png") }
    Image{ width: 5.7 height: 7.8 margin: Inset{left: 190.9 right: 0 top: 309.4 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/19e59407980831e8.png") }
    Image{ width: 15.3 height: 14.9 margin: Inset{left: 172.7 right: 0 top: 307.6 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/c711ee7c79a3f921.png") }
    Image{ width: 16.2 height: 11.8 margin: Inset{left: 175.7 right: 0 top: 310.7 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/c2bb290d11b570e5.png") }
    Image{ width: 8.1 height: 5.1 margin: Inset{left: 182.7 right: 0 top: 313.7 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/fc5c81a263faeccc.png") }
    Image{ width: 5.8 height: 4.2 margin: Inset{left: 181.8 right: 0 top: 316.9 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/9926f55756925fda.png") }
    Image{ width: 2.6 height: 16.3 margin: Inset{left: 179.8 right: 0 top: 321.1 bottom: 0} fit: ImageFit.Stretch src: http_resource("http://127.0.0.1:8787/_icons/bab063de1ea68a33.png") }
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
