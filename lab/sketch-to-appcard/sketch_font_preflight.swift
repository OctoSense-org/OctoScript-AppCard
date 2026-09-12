import CoreText
import Foundation

// Sketch resolves fonts by PostScript name. Merely copying a font file does not
// prove fontd has registered it yet, or that another version will not win.
let args = Array(CommandLine.arguments.dropFirst())
guard args.count % 2 == 0 else { fatalError("expected font-name/file pairs") }
var resolved: [String: String] = [:]
for index in stride(from: 0, to: args.count, by: 2) {
    let names = args[index].split(separator: "=", maxSplits: 1).map(String.init)
    let name = names[0]
    let expectedName = names.count == 2 ? names[1] : name
    let expected = URL(fileURLWithPath: args[index + 1]).resolvingSymlinksInPath()
    var error: Unmanaged<CFError>?
    _ = CTFontManagerRegisterFontsForURL(expected as CFURL, .user, &error)
    if let error { _ = error.takeRetainedValue() } // Already registered is normal.
    for _ in 0..<50 {
        // Apple's private UI aliases deliberately fall back when resolved by
        // PostScript name. Ask CoreText for the system UI face and still verify
        // its actual PostScript name and exact file against the declaration.
        let font = (name == ".AppleSystemUIFont" || name == ".SFNS-Regular")
            ? CTFontCreateUIFontForLanguage(.system, 16, nil)!
            : CTFontCreateWithName(name as CFString, 16, nil)
        if CTFontCopyPostScriptName(font) as String == expectedName,
           let url = CTFontCopyAttribute(font, kCTFontURLAttribute) as? URL,
           url.resolvingSymlinksInPath() == expected {
            resolved[name] = expected.path
            break
        }
        Thread.sleep(forTimeInterval: 0.1)
    }
    guard resolved[name] != nil else {
        fputs("Sketch font preflight failed: \(name) does not resolve to \(expected.path)\n", stderr)
        exit(1)
    }
}
let data = try JSONSerialization.data(withJSONObject: resolved, options: [.sortedKeys])
print(String(decoding: data, as: UTF8.self))
