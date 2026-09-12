use std::{env, fs};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let path = env::args().nth(1).ok_or("card path required")?;
    let source = fs::read_to_string(path)?;
    let report = splash_ui_l0::check_ui_l0_named("composition", &source);
    println!("{}", serde_json::json!({"valid":report.valid,"diagnostics":format!("{:?}",report.diagnostics)}));
    if !report.valid { std::process::exit(1); }
    Ok(())
}
