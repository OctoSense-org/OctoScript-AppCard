//! Source-backed page compositions. Only named views change; the app keeps its
//! sources, state and event declarations. The result is a standalone L0 card.
use std::collections::BTreeMap;

pub const LAYOUTS: &[(&str, &str)] = &[
    ("weather", "dashboard"), ("weather", "forecast"),
    ("stock", "tiles"), ("stock", "chart"),
    ("news", "magazine"), ("news", "compact"),
];

fn recipe(app: &str, layout: &str) -> Option<(&'static str, &'static str)> {
    macro_rules! page { ($path:literal) => { include_str!(concat!(
        "../../../../splash-makepad/components/l0/pages/", $path, ".l0")) }; }
    Some(match (app, layout) {
        ("weather", "dashboard") => ("", page!("weather/dashboard")),
        ("weather", "forecast") => ("", page!("weather/forecast")),
        ("stock", "tiles") => (page!("stock/shared"), page!("stock/tiles")),
        ("stock", "chart") => (page!("stock/shared"), page!("stock/chart")),
        ("news", "magazine") => (page!("news/shared"), page!("news/magazine")),
        ("news", "compact") => (page!("news/shared"), page!("news/compact")),
        _ => return None,
    })
}

/// Fixed prompt reference: the same native page fragments used by kit review.
/// The model may compose these views while retaining the app's data and events.
pub fn prompt_reference(app: &str) -> String {
    let mut out = String::new();
    for &(domain, layout) in LAYOUTS {
        if domain != app { continue; }
        if let Some((shared, page)) = recipe(domain, layout) {
            out.push_str(&format!("\n[OPTIONAL NATIVE PAGE COMPOSITION: {domain}/{layout}]\n\
These are replacement views for this app's exemplar; retain its sources, state, \
copy and events. Choose or adapt the composition to supplied context. Emit the \
complete standalone card; a layout comment alone changes nothing.\n{shared}\n{page}\n"));
        }
    }
    out
}

// The bundled cards and authored fragments use unindented top-level
// declarations. Nested component views are indented and remain untouched.
fn declarations(source: &str) -> Vec<(&str, &str)> {
    let mut starts = vec![];
    let mut offset = 0;
    for line in source.split_inclusive('\n') {
        if ["view ", "component ", "source ", "state ", "event ", "copy ", "theme "]
            .iter().any(|prefix| line.starts_with(prefix)) {
            starts.push(offset);
        }
        offset += line.len();
    }
    if starts.first().copied() != Some(0) { starts.insert(0, 0); }
    starts.push(source.len());
    starts.windows(2).filter_map(|range| {
        let body = &source[range[0]..range[1]];
        if body.is_empty() { return None; }
        let name = body.strip_prefix("view ").and_then(|s| s.split_whitespace().next()).unwrap_or("");
        Some((name, body))
    }).collect()
}

pub fn apply(app: &str, layout: &str, source: &str) -> Result<String, String> {
    if layout.is_empty() { return Ok(source.to_owned()); }
    let (shared, page) = recipe(app, layout)
        .ok_or_else(|| format!("unknown page layout {app}/{layout}"))?;
    let mut replacements: BTreeMap<_, _> = declarations(shared).into_iter()
        .chain(declarations(page)).filter(|(name, _)| !name.is_empty()).collect();
    let mut result = format!("# page_layout: {layout}\n");
    for (name, body) in declarations(source) {
        result.push_str(replacements.remove(name).unwrap_or(body));
        if !result.ends_with('\n') { result.push('\n'); }
    }
    for body in replacements.into_values() { result.push_str(body); result.push('\n'); }
    Ok(result)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn page_recipes_live_chart_ticker_stays_text_in_kit_lowering() {
        let source = "source movers sys.movers(count: 1, fields: [ticker])\n\
            state range { shape: enum[d1, m1], initial: .d1 }\n\
            view root Surface { StockPlot(symbol: movers.0.ticker, range: range) }\n";
        let report = splash_ui_l0::realize(source, &serde_json::json!({
            "movers": [{"ticker": "BLTE"}], "range": "d1"
        }), splash_ui_l0::RealizeLimits::default());
        let lowered = splash_ui_l0::kit::lower(report.complete_root().unwrap());
        assert!(lowered.contains("l0_stockplot(sys.movers(0, \"symbol\", \"\"), \"d1\")"), "{lowered}");
        assert!(!lowered.contains("sys.num("), "a ticker must never be coerced to a number");
    }

    #[test]
    fn page_recipes_are_closed_cards_and_preserve_application_logic() {
        for &(app, layout) in LAYOUTS {
            let original = crate::L0_APPS.iter().find(|(name, _, _)| *name == app).unwrap().2;
            let source = apply(app, layout, original).unwrap();
            let report = splash_ui_l0::check_ui_l0_named(app, &source);
            assert!(report.diagnostics.is_empty(), "{app}/{layout}: {:#?}", report.diagnostics);
            for (_, declaration) in declarations(original).into_iter().filter(|(name, body)| name.is_empty() && !body.starts_with('#')) {
                assert!(source.contains(declaration), "{app}/{layout} changed app logic: {declaration}");
            }
            assert_eq!(splash_ui_l0::state_initials(original), splash_ui_l0::state_initials(&source));
        }
        assert!(apply("weather", "tiles", "").is_err());
        assert_eq!(apply("weather", "", "original").unwrap(), "original");
    }
}
