//! Adaptive compositions of the ported semantic kits for existing L0 apps.
//! Recipes retain source component IDs; runtime bindings retain L0 data/events.
use serde_json::{json, Value};
use octoscript_node::{Attrs, NodeKind, UiNode};
use std::sync::OnceLock;

fn recipes() -> &'static Value {
    static RECIPES: OnceLock<Value> = OnceLock::new();
    RECIPES.get_or_init(|| serde_json::from_str(include_str!(
        "../../../../../octoscript-makepad/components/l0/native/app-recipes.json"
    )).expect("bundled native component recipes"))
}

fn node(kind: NodeKind, children: Vec<UiNode>) -> UiNode {
    UiNode { kind, attrs: Attrs { fillw: Some(1), fith: Some(1), ..Attrs::default() }, children }
}
fn event(n: &UiNode) -> Option<String> {
    let target = n.attrs.tapto.as_deref()?.strip_prefix("l0:")?;
    serde_json::from_str::<Value>(target).ok()?["e"].as_str().map(str::to_owned)
}
fn width_fill(n: &mut UiNode) {
    n.attrs.w = None;
    n.attrs.fitw = None;
    n.attrs.fillw = Some(1);
}
fn unwrap_tap(mut n: UiNode) -> UiNode {
    if n.kind == NodeKind::Column && n.attrs.tapto.is_some() && n.children.len() == 1
        && matches!(n.children[0].kind, NodeKind::Chip | NodeKind::Row | NodeKind::Card) {
        let mut child = n.children.remove(0);
        child.attrs.tapto = n.attrs.tapto;
        if n.attrs.fitw == Some(1) {
            child.attrs.fillw = None;
            child.attrs.fitw = Some(1);
        }
        return child;
    }
    n
}

fn text_id(n: &UiNode) -> Option<String> {
    if n.kind == NodeKind::Text { return n.attrs.id.clone(); }
    n.children.iter().find_map(text_id)
}

struct Composer<'a> {
    theme: &'a str,
    app: &'a str,
    layout: &'a str,
    recipes: &'a Value,
    serial: usize,
    has_story_cards: bool,
}
impl Composer<'_> {
    fn id(&mut self) -> String {
        let id = format!("kit_{}", self.serial);
        self.serial += 1;
        id
    }
    fn style_text(&self, n: &mut UiNode, recipe: &Value, role: &str) {
        let style = &recipe["parts"][role]["style"];
        if let Some(size) = style["size"].as_f64() { n.attrs.size = Some((size * 0.75) as f32); }
        if let Some(weight) = style["weight"].as_i64() { n.attrs.weight = Some(weight as i32); }
        if let Some(color) = style["color"].as_u64() { n.attrs.color = Some(color as u32); }
        n.attrs.family = Some(format!("kit:{}:body", self.theme));
    }
    fn contract(&self, recipe: &Value, bindings: Value) -> Value {
        json!({"widget": recipe["widget"], "bindings": bindings,
            "recipe_theme": self.theme, "page_layout": self.layout, "source_role": recipe["source_role"],
            "source_composition": recipe["source_composition"],
            "source_component": recipe["source_component"],
            "source_kit_sha256": recipe["source_kit_sha256"],
            "adaptation": "Flow layout with live app slots; source artboard geometry is not retained."})
    }
    fn interactive(&mut self, mut body: UiNode, recipe: &Value, title: Option<String>) -> UiNode {
        let target = body.attrs.tapto.take();
        let id = self.id();
        let control = format!("{id}_control");
        let label = title.or_else(|| text_id(&body));
        let binding = if recipe["widget"] == "KitButton" { "label" } else { "title" };
        let mut bindings = json!({"control":control});
        if let Some(label) = label { bindings[binding] = label.into(); }
        let contract = self.contract(recipe, bindings);
        let attrs = Attrs { id: Some(id), kit: Some(contract.to_string()),
            fillw: body.attrs.fillw, fitw: body.attrs.fitw, w: body.attrs.w,
            fith: Some(1), ..Attrs::default() };
        body.attrs.margin = None;
        let button = UiNode { kind: NodeKind::Button, attrs: Attrs {
            id: Some(control), fillw: Some(1), fillh: Some(1), tapto: target,
            enabled: Some(1), ..Attrs::default()
        }, children: vec![] };
        UiNode { kind: NodeKind::Stack, attrs, children: vec![body, button] }
    }
    fn field(&mut self, mut input: UiNode) -> UiNode {
        let recipe = self.recipes["field"].clone();
        let id = self.id();
        let input_id = format!("{id}_input");
        input.attrs.id = Some(input_id.clone());
        self.style_text(&mut input, &recipe, "input");
        input.attrs.size = Some(input.attrs.size.unwrap_or(12.0).max(12.0));
        width_fill(&mut input);
        input.attrs.h = Some(44.0);
        input.attrs.pad = None;
        input.attrs.padx = Some(14.0);
        input.attrs.pady = Some(10.0);
        input.attrs.margin = Some(0.0);
        if let Some(surface) = recipe["surfaces"].as_array().and_then(|s| s.first()) {
            input.attrs.bg = surface["style"]["bg"].as_u64().map(|c| c as u32);
            input.attrs.radius = surface["style"]["radius"].as_f64().map(|c| c as f32);
        }
        let mut children = vec![];
        let mut bindings = json!({"input":input_id});
        if recipe["parts"]["label"].is_object() && input.attrs.placeholder.as_deref().is_some_and(|s| !s.is_empty()) {
            let mut label = node(NodeKind::Text, vec![]);
            label.attrs.id = Some(format!("{id}_label"));
            label.attrs.text = Some(input.attrs.placeholder.clone().unwrap_or_default());
            self.style_text(&mut label, &recipe, "label");
            bindings["label"] = label.attrs.id.clone().unwrap().into();
            children.push(label);
        }
        children.push(input);
        let mut root = node(NodeKind::Column, children);
        root.attrs.id = Some(id);
        root.attrs.spacing = Some(6.0);
        root.attrs.kit = Some(self.contract(&recipe, bindings).to_string());
        root
    }
    fn chip(&mut self, mut n: UiNode) -> UiNode {
        let recipe = self.recipes["button"].clone();
        n.attrs.h = Some(44.0);
        n.attrs.pady = Some(10.0);
        n.attrs.padx = Some(14.0);
        if let Some(label) = n.children.iter_mut().find(|n| n.kind == NodeKind::Text) {
            let state_ink = label.attrs.color;
            self.style_text(label, &recipe, "label");
            // A source text-only button recipe has no selected surface/ink
            // pair. Keep the native theme's selected ink with its background.
            if n.attrs.selected == Some(1) && recipe["surfaces"].as_array().is_none_or(|s| s.is_empty()) {
                label.attrs.color = state_ink;
            }
            label.attrs.size = Some(label.attrs.size.unwrap_or(11.0).max(11.0));
        }
        if let Some(surface) = recipe["surfaces"].as_array().and_then(|s| s.first()) {
            n.attrs.bg = surface["style"]["bg"].as_u64().map(|c| c as u32);
            n.attrs.radius = surface["style"]["radius"].as_f64().map(|c| c as f32);
        }
        self.interactive(n, &recipe, None)
    }
    fn stock_row(&mut self, mut n: UiNode) -> UiNode {
        let recipe = self.recipes["row"].clone();
        // Camo's title/subtitle lane + trailing action lane becomes a quote lane.
        // Identity and company name get the flexible width; prices stack at right.
        let mut identity = n.children.remove(0);
        width_fill(&mut identity);
        identity.attrs.spacing = Some(4.0);
        if let Some(title) = identity.children.get_mut(0) { self.style_text(title, &recipe, "title"); }
        if let Some(subtitle) = identity.children.get_mut(1) { self.style_text(subtitle, &recipe, "artist"); width_fill(subtitle); }
        let title = text_id(&identity);
        let mut quote = node(NodeKind::Column, std::mem::take(&mut n.children));
        quote.attrs.fillw = None;
        quote.attrs.w = Some(112.0);
        quote.attrs.spacing = Some(3.0);
        for (i, child) in quote.children.iter_mut().enumerate() {
            width_fill(child);
            child.attrs.alignx = Some(1.0);
            child.attrs.size = Some(if i == 0 { 12.5 } else { 11.0 });
        }
        n.children = vec![identity, quote];
        n.attrs.spacing = Some(14.0);
        n.attrs.pady = Some(8.0);
        n.attrs.aligny = Some(0.5);
        if self.layout == "tiles" {
            n.kind = NodeKind::Card;
            n.attrs.pad = Some(14.0);
            n.attrs.pady = None;
            n.attrs.radius = Some(12.0);
            n.attrs.bg = Some(0xff1e1e28);
            let quote = &mut n.children[1];
            width_fill(quote);
            for child in &mut quote.children { child.attrs.alignx = Some(0.0); }
        }
        self.interactive(n, &recipe, title)
    }
    fn story_card(&mut self, mut n: UiNode) -> UiNode {
        self.has_story_cards = true;
        let recipe = self.recipes["card"].clone();
        let (mut title, meta, badge) = if n.kind == NodeKind::Card && n.children.len() == 3 {
            let badge = n.children.remove(0);
            let title = n.children.remove(0);
            (title, n.children.remove(0), badge)
        } else {
            let badge = n.children.remove(0);
            let mut content = n.children.remove(0);
            let title = content.children.remove(0);
            (title, content.children.remove(0), badge)
        };
        self.style_text(&mut title, &recipe, "title");
        width_fill(&mut title);
        title.attrs.variant = None;
        let title_id = title.attrs.id.clone();
        let mut tag = node(NodeKind::Chip, vec![badge]);
        tag.attrs.fillw = None;
        tag.attrs.fitw = Some(1);
        tag.attrs.padx = Some(8.0);
        tag.attrs.pady = Some(4.0);
        if let Some(surface) = recipe["surfaces"].as_array().and_then(|s| s.last()) {
            tag.attrs.bg = surface["style"]["bg"].as_u64().map(|c| c as u32);
            tag.attrs.radius = surface["style"]["radius"].as_f64().map(|c| c as f32);
        }
        self.style_text(&mut tag.children[0], &recipe, "status");
        tag.children[0].attrs.w = None;
        tag.children[0].attrs.fillw = None;
        tag.children[0].attrs.fitw = Some(1);
        n.kind = NodeKind::Card;
        n.attrs.bg = Some(0xffffffff);
        n.attrs.bg2 = None;
        n.attrs.radius = Some(16.0);
        n.attrs.pad = Some(16.0);
        n.attrs.padx = None;
        n.attrs.pady = None;
        n.attrs.spacing = Some(12.0);
        n.attrs.marginbottom = Some(12.0);
        n.children = vec![tag, title, meta];
        if self.layout == "compact" {
            let tag = n.children.remove(0);
            let mut content = node(NodeKind::Column, std::mem::take(&mut n.children));
            content.attrs.spacing = Some(6.0);
            n.kind = NodeKind::Row;
            n.attrs.pad = Some(10.0);
            n.attrs.spacing = Some(10.0);
            n.attrs.marginbottom = Some(0.0);
            n.attrs.radius = Some(8.0);
            n.children = vec![tag, content];
        }
        self.interactive(n, &recipe, title_id)
    }
    fn tabs(&mut self, mut n: UiNode) -> UiNode {
        let recipe = self.recipes["tabs"].clone();
        let id = self.id();
        let colors: Vec<_> = n.children.iter().map(|c| c.attrs.bg).collect();
        let selected = colors.iter().enumerate().find(|(_, c)| colors.iter().filter(|v| *v == *c).count() == 1).map(|(i,_)| i).unwrap_or(0);
        let mut items = vec![];
        for (i, child) in n.children.iter_mut().enumerate() {
            let target = child.attrs.tapto.take();
            width_fill(child);
            child.attrs.id = Some(format!("{id}_surface_{i}"));
            child.attrs.h = Some(44.0);
            if let Some(radius) = recipe["surfaces"].as_array().and_then(|s| s.first()).and_then(|s| s["style"]["radius"].as_f64()) {
                child.attrs.radius = Some(radius as f32);
            }
            child.attrs.padx = Some(4.0);
            child.attrs.pady = Some(10.0);
            let surface = child.attrs.id.clone().unwrap();
            let text = child.children.iter_mut().find(|n| n.kind == NodeKind::Text).expect("range chip label");
            text.attrs.id = Some(format!("{id}_label_{i}"));
            text.attrs.alignx = Some(0.5);
            width_fill(text);
            self.style_text(text, &recipe, if i == selected { "label" } else { "subtitle" });
            text.attrs.size = Some(text.attrs.size.unwrap_or(11.0).max(11.0));
            let paint = text.attrs.id.clone().unwrap();
            let control = format!("{id}_control_{i}");
            let button = UiNode { kind: NodeKind::Button, attrs: Attrs { id: Some(control.clone()),
                fillw: Some(1), fillh: Some(1), tapto: target, enabled: Some(1), ..Attrs::default() }, children: vec![] };
            let body = child.clone();
            *child = node(NodeKind::Stack, vec![body, button]);
            child.attrs.id = Some(format!("{id}_item_{i}"));
            items.push(json!({"root":child.attrs.id,"control":control,"paint":[paint],"surfaces":[surface],"source_enabled":true}));
        }
        n.attrs.id = Some(id);
        n.attrs.spacing = Some(4.0);
        let mut contract = self.contract(&recipe, json!({}));
        for (key,value) in recipe["selection"].as_object().unwrap() { contract[key] = value.clone(); }
        contract["items"] = items.into();
        contract["source_selected_index"] = (-1).into();
        contract["selected_index"] = selected.into();
        n.attrs.kit = Some(contract.to_string());
        n
    }
    fn visit(&mut self, n: UiNode) -> UiNode {
        let mut n = unwrap_tap(n);
        n.children = n.children.into_iter().map(unwrap_tap).collect();
        if n.kind == NodeKind::Row && n.children.len() >= 2 && n.children.iter().all(|c| event(c).as_deref() == Some("set_range") && c.kind == NodeKind::Chip) {
            return self.tabs(n);
        }
        if n.kind == NodeKind::Input { return self.field(n); }
        if n.kind == NodeKind::Chip && n.attrs.tapto.is_some() { return self.chip(n); }
        if self.app == "stock" && self.recipes["row"].is_object() && event(&n).as_deref() == Some("open_quote")
            && n.children.len() == 3 && n.children[0].kind == NodeKind::Column && n.children[0].children.len() == 2 {
            return self.stock_row(n);
        }
        if self.app == "news" && self.recipes["card"].is_object() && event(&n).as_deref() == Some("open_story")
            && ((n.kind == NodeKind::Card && n.children.len() == 3) || (n.kind == NodeKind::Row && n.children.len() == 2 && n.children[1].children.len() == 2)) {
            return self.story_card(n);
        }
        n.children = n.children.into_iter().map(|c| self.visit(c)).collect();
        if self.layout == "magazine" && n.kind == NodeKind::Row
            && n.children.iter().any(|c| c.attrs.kit.as_deref().is_some_and(|s| s.contains("TaskplanProjectCard"))) {
            // Grid rows inherit centered cross-axis alignment from L0 Row.
            // Unequal headline lengths should align cards at their top edge.
            n.attrs.aligny = Some(0.0);
        }
        if self.app == "weather" && event(&n).as_deref() == Some("toggle") && n.kind == NodeKind::Row {
            n.attrs.h = Some(40.0);
            n.attrs.aligny = Some(0.5);
            return self.interactive(n, &self.recipes["button"].clone(), None);
        }
        n
    }
}

pub fn compose(source: &str, root: UiNode) -> UiNode {
    // Generated cards may declare their app via `model` without an exemplar's
    // ledger identity. Use the language header parser for both valid forms.
    let header = octoscript_ui_l0::parse_header(source);
    let app = header.as_ref().filter(|h| h.contradictions.is_empty()).and_then(|h| {
        h.model.as_deref().or(h.ledger.as_deref())
    }).filter(|app| matches!(*app, "weather" | "stock" | "news"));
    let theme = octoscript_ui_l0::card_theme(source);
    let (Some(app), Some(theme)) = (app, theme.as_deref()) else { return root };
    let Some(recipes) = recipes().get(theme) else { return root };
    let mut root = root;
    fn assign(n: &mut UiNode, live: &mut usize, literal: &mut usize) {
        if n.kind == NodeKind::Text {
            if n.attrs.action.is_some() { n.attrs.id = Some(format!("l0v{live}")); *live += 1; }
            else { n.attrs.id = Some(format!("kit_text_{literal}")); *literal += 1; }
        }
        for child in &mut n.children { assign(child, live, literal); }
    }
    assign(&mut root, &mut 0, &mut 0);
    let layout = source.lines().find_map(|l| l.strip_prefix("# page_layout: ")).unwrap_or("");
    let mut composer = Composer { theme, app, layout, recipes, serial: 0, has_story_cards: false };
    let mut root = composer.visit(root);
    if app == "weather" && root.kind == NodeKind::Stack {
        // Let the foreground measure the overlay. Backgrounds remain Fill and
        // follow that measured size instead of imposing the old 1500px canvas.
        root.attrs.id = Some("kit_content_page".into());
        root.attrs.h = None;
        root.attrs.fillh = None;
        root.attrs.fith = Some(1);
        for child in &mut root.children {
            if child.kind == NodeKind::Column && !child.children.is_empty() {
                child.attrs.h = None;
                child.attrs.fillh = None;
                child.attrs.fith = Some(1);
            }
        }
    }
    if composer.has_story_cards || !layout.is_empty() {
        // The card feed may be taller than the legacy 1500px canvas. Its native
        // intrinsic height must reach PortalList so the last item can scroll in.
        root.attrs.h = None;
        root.attrs.fillh = None;
        root.attrs.fith = Some(1);
    }
    root
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn kit_classes_construct_in_the_app_splash_prelude() {
        use makepad_widgets::*;
        let mut cx = Cx::new(Box::new(|_, _| {}));
        let vm_id = cx.alloc_splash_vm();
        let root = cx.with_script_vm_id(vm_id, |vm| {
            let value = script_eval!(vm, {
                use mod.prelude.widgets.*
                View {
                    button := KitButton { label := Label { text: "Action" } control := Button {} }
                    field := KitFormField { input := TextInput { text: "City" } }
                    tabs := KitTabBar { control := KitSelectionControl {} }
                    navigation := KitBottomNavigation { control := Button {} }
                    card := TaskplanProjectCard { title := Label { text: "Headline" } control := Button {} }
                    row := CamoTrackRow { title := Label { text: "Ticker" } control := Button {} }
                }
            });
            assert!(!value.is_err() && !value.is_nil());
            View::script_from_value(vm, value)
        });
        assert_eq!(root.children.len(), 6);
        assert!(root.children[0].1.borrow::<kit::KitButton>().is_some());
        assert!(root.children[1].1.borrow::<kit::KitFormField>().is_some());
        assert!(root.children[2].1.borrow::<kit::KitTabBar>().is_some());
        assert!(root.children[3].1.borrow::<kit::KitBottomNavigation>().is_some());
        assert!(root.children[4].1.borrow::<kit::TaskplanProjectCard>().is_some());
        assert!(root.children[5].1.borrow::<kit::CamoTrackRow>().is_some());
        assert_eq!(root.child_by_path(&[LiveId::from_str("title")]).text(), "Headline");
    }
    fn tapped(event: &str, mut content: UiNode) -> UiNode {
        content.attrs.tapto = None;
        let mut wrapper = node(NodeKind::Column, vec![content]);
        wrapper.attrs.tapto = Some(format!("l0:{}", json!({"e":event,"k":"root","v":"BLTE"})));
        wrapper
    }
    fn text(value: &str, live: Option<&str>) -> UiNode {
        let mut n = node(NodeKind::Text, vec![]);
        n.attrs.text = Some(value.into());
        n.attrs.action = live.map(str::to_owned);
        n
    }
    fn walk<'a>(n: &'a UiNode, nodes: &mut Vec<&'a UiNode>) {
        nodes.push(n);
        for child in &n.children { walk(child, nodes); }
    }
    #[test]
    fn generation_render_selected_button_keeps_state_ink_and_event() {
        let mut label = text("Latest", None);
        label.attrs.color = Some(0xff111827);
        let mut chip = node(NodeKind::Chip, vec![label]);
        chip.attrs.selected = Some(1);
        chip.attrs.bg = Some(0xff428eba);
        let after = compose("# ledger news@1\ntheme taskplan_light\n", tapped("pick_tab", chip));
        assert_eq!(after.children[0].children[0].attrs.color, Some(0xff111827));
        assert_eq!(after.children[0].attrs.bg, Some(0xff428eba));
        assert!(after.children[1].attrs.tapto.as_ref().unwrap().contains("pick_tab"));
    }

    #[test]
    fn generation_render_model_header_activates_native_kit() {
        for app in ["weather", "stock", "news"] {
            let chip = || tapped("pick", node(NodeKind::Chip, vec![text("Open", None)]));
            for header in [format!("# model: {app}"), format!("# ledger {app}@1"),
                           format!("# ledger personal-card@1\n# model: {app}")] {
                let after = compose(&format!("{header}\n  theme taskplan_light\n"), chip());
                let contract: Value = serde_json::from_str(after.attrs.kit.as_ref()
                    .expect("valid app identity must activate native kit components")).unwrap();
                assert_eq!(contract["widget"], "KitButton");
                assert_eq!(contract["recipe_theme"], "taskplan_light");
                assert_eq!(event(&after.children[1]).as_deref(), Some("pick"));
            }
            let unknown = compose("# model: unrelated\ntheme taskplan_light\n", chip());
            assert!(unknown.attrs.kit.is_none());
            let conflicting = compose(&format!("# model: {app}\n# model: unrelated\ntheme taskplan_light\n"), chip());
            assert!(conflicting.attrs.kit.is_none());
        }
    }

    #[test]
    fn kit_composition_preserves_live_values_events_and_native_bindings() {
        let identity = node(NodeKind::Column, vec![text("BLTE", Some("sys.quote(\"ticker\")")), text("A long company name", Some("sys.quote(\"name\")"))]);
        let row = node(NodeKind::Row, vec![identity, text("193.61", Some("sys.quote(\"last\")")), text("13.16%", Some("sys.quote(\"pct\")"))]);
        let before = tapped("open_quote", row);
        let target = before.attrs.tapto.clone().unwrap();
        let after = compose("# ledger stock@1\ntheme camo\n", before);
        let mut nodes = vec![];
        walk(&after, &mut nodes);
        let contract: Value = serde_json::from_str(after.attrs.kit.as_ref().unwrap()).unwrap();
        assert_eq!(contract["widget"], "CamoTrackRow");
        assert_eq!(contract["source_composition"], "CamoTrackRow96c04695");
        assert!(nodes.iter().any(|n| n.kind == NodeKind::Button && n.attrs.tapto.as_deref() == Some(&target)));
        let bindings: Vec<_> = nodes.iter().filter(|n| n.kind == NodeKind::Text).map(|n| (n.attrs.id.as_deref().unwrap(),n.attrs.action.as_deref().unwrap())).collect();
        assert_eq!(bindings.len(), 4);
        assert_eq!(bindings[0], ("l0v0", "sys.quote(\"ticker\")"));
        assert_eq!(bindings[3], ("l0v3", "sys.quote(\"pct\")"));
        let content = &after.children[0];
        assert_eq!(content.children[0].attrs.fillw, Some(1));
        assert_eq!(content.children[1].children.len(), 2);
        let dsl = super::super::l0_widgets::to_dsl(&after);
        assert!(dsl.contains(" := CamoTrackRow{"));
        assert!(dsl.contains("ui.l0v0.set_text("));
        assert!(dsl.contains("on_click: || agent.notify("));
        for id in contract["bindings"].as_object().unwrap().values() {
            assert!(nodes.iter().any(|n| n.attrs.id.as_deref() == id.as_str()));
        }
    }
    #[test]
    fn kit_tabs_preserve_selected_range_and_each_event_payload() {
        let children = ["d1","w1","m1","m6","y1"].into_iter().enumerate().map(|(i,value)| {
            let mut chip = node(NodeKind::Chip, vec![text(value,None)]);
            chip.attrs.bg = Some(if i == 2 {0xff112233} else {0xff000000});
            let mut wrapper = tapped("set_range",chip);
            wrapper.attrs.tapto = Some(format!("l0:{}",json!({"e":"set_range","k":"root","v":value})));
            wrapper
        }).collect();
        let after = compose("# ledger stock@1\ntheme camo\n",node(NodeKind::Row,children));
        let config: Value = serde_json::from_str(after.attrs.kit.as_ref().unwrap()).unwrap();
        assert_eq!(config["widget"],"KitTabBar");
        assert_eq!(config["selected_index"],2);
        assert_eq!(config["items"].as_array().unwrap().len(),5);
        let mut all = vec![]; walk(&after,&mut all);
        let targets: Vec<_> = all.iter().filter_map(|n| n.attrs.tapto.as_deref()).collect();
        assert_eq!(targets.len(),5);
        assert!(targets.iter().any(|t| t.contains("y1")));
    }
    #[test]
    fn kit_fields_keep_native_search_change_and_commit_channels() {
        let mut input = node(NodeKind::Input,vec![]);
        input.attrs.tapto = Some("l0:{\"e\":\"preview\",\"k\":\"root\",\"v\":\"$$\"}".into());
        input.attrs.changeto = Some("l0:{\"e\":\"typing\",\"k\":\"root\",\"v\":\"$$\"}".into());
        input.attrs.text = Some("Cupertino".into());
        input.attrs.placeholder = Some("City".into());
        let after = compose("# ledger weather@1\ntheme atro_light\n",input.clone());
        let mut all = vec![]; walk(&after,&mut all);
        let actual = all.iter().find(|n| n.kind == NodeKind::Input).unwrap();
        assert_eq!(actual.attrs.tapto,input.attrs.tapto);
        assert_eq!(actual.attrs.changeto,input.attrs.changeto);
        assert_eq!(actual.attrs.text,input.attrs.text);
        let dsl = super::super::l0_widgets::to_dsl(&after);
        assert!(dsl.contains(" := KitFormField{"));
        assert!(dsl.contains(" := TextInput{"));
        assert!(dsl.contains("on_change: |t| agent.notify("));
        assert!(dsl.contains("on_return: |t| agent.notify("));
    }
    #[test]
    fn page_recipes_change_compound_flow_without_losing_controls() {
        let row = node(NodeKind::Row, vec![
            node(NodeKind::Column, vec![text("BLTE", Some("ticker")), text("Company", Some("name"))]),
            text("193.61", Some("last")), text("13.16%", Some("pct")),
        ]);
        let tiled = compose("# page_layout: tiles\n# ledger stock@1\ntheme camo\n", tapped("open_quote", row));
        let body = &tiled.children[0];
        assert_eq!(body.kind, NodeKind::Card);
        assert_eq!(body.children[1].attrs.w, None, "quote lane must fit half a phone");
        assert_eq!(body.children[1].attrs.fillw, Some(1));
        let mut nodes = vec![]; walk(&tiled, &mut nodes);
        assert_eq!(nodes.iter().filter(|n| n.attrs.action.is_some()).count(), 4);
        assert!(nodes.iter().any(|n| n.kind == NodeKind::Button && event(n).as_deref() == Some("open_quote")));

        let story = node(NodeKind::Row, vec![text("1", None), node(NodeKind::Column, vec![
            text("Headline", Some("title")), node(NodeKind::Row, vec![text("42", Some("points")), text("Author", Some("author"))]),
        ])]);
        let compact = compose("# page_layout: compact\n# ledger news@1\ntheme taskplan_light\n", tapped("open_story", story));
        let body = &compact.children[0];
        assert_eq!(body.kind, NodeKind::Row);
        assert_eq!(body.children[1].kind, NodeKind::Column);
        assert_eq!(body.children[1].children[0].attrs.action.as_deref(), Some("title"));
        assert_eq!(event(&compact.children[1]).as_deref(), Some("open_story"));
    }
    #[test]
    fn kit_news_cards_keep_all_data_and_grow_the_scrolling_canvas() {
        let story = node(NodeKind::Column, vec![text("A long headline", Some("sys.news(1, \"title\")")),
            node(NodeKind::Row, vec![text("42 pts", None), text("Author", None)])]);
        let mut root = node(NodeKind::Column, vec![tapped("open_story",
            node(NodeKind::Row, vec![text("1", None), story]))]);
        root.attrs.h = Some(1500.0);
        root.attrs.fillh = Some(1);
        let after = compose("# ledger news@1\ntheme taskplan_light\n", root);
        assert_eq!((after.attrs.h, after.attrs.fillh, after.attrs.fith), (None, None, Some(1)));
        let mut all = vec![]; walk(&after, &mut all);
        assert_eq!(all.iter().filter(|n| n.kind == NodeKind::Text).count(), 4);
        let contract: Value = serde_json::from_str(after.children[0].attrs.kit.as_ref().unwrap()).unwrap();
        assert_eq!(contract["widget"], "TaskplanProjectCard");
        assert_eq!(contract["bindings"]["title"], "l0v0");
        let dsl = super::super::l0_widgets::to_dsl(&after);
        assert!(dsl.contains("ui.l0v0.set_text("));
        assert!(!dsl.contains("height: 1500"));
    }
}
