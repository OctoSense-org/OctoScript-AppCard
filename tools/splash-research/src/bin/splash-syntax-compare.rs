//! Effect-free comparison of canonical workflow syntax and the inherited parser.
//! The compatibility column is not a full Makepad UI runtime test.
use serde_json::json;
use splash_core::{check_syntax, check_vm_compatibility, Runtime};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cases = [
        ("basic arithmetic", "let x = 20\nx + 22", true),
        ("semicolon statements", "let x = 20; x + 22", true),
        ("comma-separated record", "let r = {left: 20, right: 22}\nr.left + r.right", true),
        ("newline-separated record", "let r = {\nleft: 20\nright: 22\n}\nr.left + r.right", true),
        ("space-separated record", "let r = {left: 20 right: 22}\nr.left + r.right", false),
        ("comma-separated array", "let a = [20, 22]\na[0] + a[1]", true),
        ("space-separated array", "let a = [20 22]\na[0] + a[1]", false),
        ("closure", "let add = |a, b| a + b\nadd(20, 22)", true),
        ("canonical recovery", "try {\n    (1).missing()\n} catch {\n    42\n}", true),
        ("legacy recovery", "try { (1).missing() } { 42 }", false),
        ("range operator", "let total = 0\nfor n in 0..3 {\n    total += n\n}\ntotal", false),
        ("bounded range helper", "use mod.std.array\nlet total = 0\nfor n in array.range(0, 3) {\n    total += n\n}\ntotal", true),
        ("native array method", "let a = []\na.push(42)\na[0]", true),
        ("bounded array helper", "use mod.std.array\nlet a = []\narray.push(a, 42)\na[0]", true),
        ("Makepad UI", "let count = 0\nView{width: Fill height: Fit\nlabel := Label{text: \"0\"}\nButton{text: \"+\" on_click: || {count += 1; ui.label.set_text(count + \"\")}}\n}", false),
        ("deferred tool syntax", "use mod.tool\nlet pending = tool.start(\"text.echo\", \"hello\")\npending.await()", false),
        ("L0 card", "theme taskplan_light\nview root Surface(pad: .page) { TextTitle(text: \"Hello\") }", false),
    ];
    let mut results = Vec::new();
    for (name, source, evaluate) in cases {
        let canonical = check_syntax(source)?;
        let inherited = check_vm_compatibility(source)?;
        let execution = if canonical.valid && evaluate {
            let mut runtime = Runtime::new((), ())?;
            let result = runtime.eval(source)?;
            Some(json!({
                "completed": result.completed(),
                "value": format!("{:?}", result.value),
                "diagnostics": result.diagnostics,
            }))
        } else {
            None
        };
        results.push(json!({
            "case": name, "source": source,
            "canonical": canonical.valid,
            "canonical_diagnostics": format!("{:?}", canonical.diagnostics),
            "inherited_parser": inherited.valid,
            "inherited_diagnostics": format!("{:?}", inherited.diagnostics),
            "canonical_execution": execution,
        }));
    }
    println!("{}", serde_json::to_string_pretty(&results)?);
    Ok(())
}
