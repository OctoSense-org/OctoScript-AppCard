import AppKit

// stdout is a private pipe to the controller, never an instrument or log file.
let app = NSApplication.shared
app.setActivationPolicy(.accessory)
let alert = NSAlert()
alert.messageText = "Mail Password"
alert.informativeText = "Enter your mail password or app password. Tap Save in Mail Server settings to apply it."
alert.addButton(withTitle: "Use Password")
alert.addButton(withTitle: "Cancel")
let field = NSSecureTextField(frame: NSRect(x: 0, y: 0, width: 320, height: 28))
field.placeholderString = "Password or app password"
alert.accessoryView = field
alert.window.initialFirstResponder = field
app.activate(ignoringOtherApps: true)
let response = alert.runModal()
if response == .alertFirstButtonReturn {
    let data = try JSONSerialization.data(withJSONObject: ["password": field.stringValue])
    FileHandle.standardOutput.write(data)
} else {
    exit(2)
}
