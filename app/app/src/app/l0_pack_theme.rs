//! Source kit typography for the existing, flowing L0 app layouts.
//! Color/shape deltas remain the mode-aware `_palette_<theme>.splash` exports.
use serde_json::Value;
use std::collections::BTreeMap;
use std::sync::OnceLock;

fn packs() -> &'static BTreeMap<&'static str, Value> {
    static PACKS: OnceLock<BTreeMap<&'static str, Value>> = OnceLock::new();
    PACKS.get_or_init(|| {
        [
            ("atro", include_str!(concat!(env!("OCTOSENSE_WORKSPACE"), "/octoscript-makepad/components/l0/native/atro/tokens.json"))),
            ("atro_light", include_str!(concat!(env!("OCTOSENSE_WORKSPACE"), "/octoscript-makepad/components/l0/native/atro_light/tokens.json"))),
            ("camo", include_str!(concat!(env!("OCTOSENSE_WORKSPACE"), "/octoscript-makepad/components/l0/native/camo/tokens.json"))),
            ("camo_light", include_str!(concat!(env!("OCTOSENSE_WORKSPACE"), "/octoscript-makepad/components/l0/native/camo_light/tokens.json"))),
            ("taskplan_light", include_str!(concat!(env!("OCTOSENSE_WORKSPACE"), "/octoscript-makepad/components/l0/native/taskplan_light/tokens.json"))),
        ].into_iter().map(|(name, json)| (name, serde_json::from_str(json).expect("bundled theme tokens"))).collect()
    })
}

/// Insert before the explicit theme axes and size derivation, so those axes win.
pub fn defaults(theme: &str) -> String {
    let Some(tokens) = packs().get(theme) else { return String::new() };
    let body = tokens["typography.body.size"]["value"].as_f64().expect("body size");
    // Use the same 0.75 source-size calibration as the native kit pipeline.
    // The app's scale derives body = base + step and keeps its existing roles.
    format!("// Native kit typography: {theme}\nlet font_base = {}\nlet font_step = 1\nlet l0_family = \"kit:{theme}:body\"\nlet l0_display_family = \"kit:{theme}:title\"\n", body * 0.75 - 1.0)
}

/// Resolve registered kit fonts in the widget crate, which is registered in every
/// isolated Splash VM. The host application crate is not registered in those VMs.
pub fn font_resource(family: &str, weight: i32) -> Option<String> {
    let (theme, role) = family.strip_prefix("kit:")?.split_once(':')?;
    if !matches!(role, "body" | "title") { return None }
    let tokens = packs().get(theme)?;
    let key = format!("typography.{role}.font_src");
    let source = tokens[&key]["value"].as_str()?.strip_prefix("self:resources/")?;
    let source = if source.ends_with("Montserrat-Regular.ttf") || source.ends_with("DMSans-Regular.ttf") {
        let suffix = if weight >= 600 {
            if source.contains("Montserrat") { "SemiBold" } else { "Bold" }
        } else if weight >= 500 { "Medium" } else { "Regular" };
        source.replace("Regular.ttf", &format!("{suffix}.ttf"))
    } else { source.to_owned() };
    Some(format!("makepad_widgets:resources/theme-kits/{source}"))
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn registered_fonts_are_bundled_and_keep_their_source_family() {
        for theme in packs().keys() {
            assert!(!defaults(theme).is_empty());
            for role in ["body", "title"] {
                for weight in [400, 500, 600, 700] {
                    let path = font_resource(&format!("kit:{theme}:{role}"), weight).unwrap();
                    assert!(std::path::Path::new(env!("OCTOSENSE_WORKSPACE")).join("makepad/widgets").join(path.strip_prefix("makepad_widgets:").unwrap()).is_file(), "{path}");
                }
            }
        }
        assert!(font_resource("kit:camo:body", 600).unwrap().ends_with("DMSans-Bold.ttf"));
        assert!(font_resource("kit:taskplan_light:body", 400).unwrap().ends_with("PlusJakartaSans.ttf"));
        assert!(font_resource("kit:taskplan_light:title", 700).unwrap().ends_with("Inter.ttf"));
        assert!(defaults("dark").is_empty());
        assert!(font_resource("kit:missing:body", 400).is_none());
    }
}
