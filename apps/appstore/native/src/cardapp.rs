//! An installed card app as an app of its own.
//!
//! The store installs; this runs. One module, `card`, opened with the id of
//! an installed app, becomes that app's window-manager client: its own tile,
//! its own entry in recents, its own close. It re-checks the app against the
//! last verified catalog before drawing anything, so a withdrawal reaches an
//! app that was installed long ago, with no store screen involved.
//!
//! Everything about containment is the same as the store's own runner was:
//! the policy resolved from the manifest is applied to the isolate, the
//! artwork is served from a loopback origin that serves only this bundle,
//! and that origin's port is the one loopback entry the isolate may reach.
use makepad_app_module::{
    makepad_ai_services::wire::{ServiceCall, ServiceManifest, ToolResult},
    AppModule, ExecOutcome, InstanceHandles, InstanceParts, OpenArgKind, OpenSchema, ServiceExecutor, ValidatedOpen,
};
use makepad_widgets::*;
use octosense_app_hub::Store;
use octosense_app_policy::HostLimits;
use std::path::PathBuf;

script_mod! {
    use mod.prelude.widgets.*

    mod.widgets.CardAppView = set_type_default() do #(CardAppView::register_widget(vm)) {
        width: Fill height: Fill flow: Down
        show_bg: true draw_bg.color: #fff
        notice := Label { width: Fill text: "" draw_text.color: #b00 draw_text.text_style.font_size: 12 margin: 16 }
        card := Splash { width: Fill height: Fill }
    }
}

#[derive(Script, ScriptHook, Widget)]
pub struct CardAppView {
    #[deref]
    view: View,
    #[rust]
    app_id: String,
    #[rust]
    started: bool,
    #[rust]
    asset_server: Option<octosense_app_policy::AssetServer>,
}

impl CardAppView {
    fn start(&mut self, cx: &mut Cx) {
        let root = crate::data_root(cx);
        let anchor = std::env::var("OCTOSENSE_HUB_ANCHOR").unwrap_or_else(|_| crate::DEFAULT_ANCHOR.to_string());
        let mut store = Store::new(&anchor, &root, HostLimits::default());
        // The catalog the store last verified. Without one, nothing runs:
        // an app the device cannot show was offered is not run on trust.
        let catalog = std::fs::read_to_string(root.join("catalog.json")).unwrap_or_default();
        if let Err(e) = store.accept_catalog(&catalog) {
            return self.refuse(cx, &format!("Cannot open {}: no verified catalog on this device ({e})", self.app_id));
        }
        let policy = match store.may_run(&self.app_id) {
            Ok(policy) => policy,
            Err(e) => return self.refuse(cx, &format!("Cannot open: {e}")),
        };
        let mut settings = policy.isolate_settings(&root);
        if let Err(e) = std::fs::create_dir_all(&settings.jail_root) {
            return self.refuse(cx, &format!("Cannot make the app's storage: {e}"));
        }
        let bundle = store.install_dir(&self.app_id);
        let server = match octosense_app_policy::AssetServer::start(&bundle) {
            Ok(server) => server,
            Err(e) => return self.refuse(cx, &format!("Cannot serve the app's artwork: {e}")),
        };
        settings.hosts.push(server.allowlist_entry());
        let origin = server.origin().to_string();
        self.asset_server = Some(server);
        let splash = self.view.splash(cx, ids!(card));
        let applied = octosense_app_policy::splash_adapter::apply(&splash, cx, &settings);
        log!(
            "card: {} running under {} capability(ies), {} host(s), {} bytes of storage, {} instructions, {} bytes of heap",
            self.app_id, applied.capabilities, applied.hosts, applied.storage_quota, applied.instruction_budget, applied.memory_bytes
        );
        match crate::card_source(&bundle, &origin) {
            Ok(source) => splash.set_text(cx, &source),
            Err(e) => self.refuse(cx, &format!("The app did not open: {e}")),
        }
    }

    fn refuse(&mut self, cx: &mut Cx, reason: &str) {
        error!("card: {reason}");
        self.view.label(cx, ids!(notice)).set_text(cx, reason);
        self.view.redraw(cx);
    }
}

impl Widget for CardAppView {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if !self.started {
            self.started = true;
            self.start(cx);
        }
        self.view.handle_event(cx, event, scope);
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.view.draw_walk(cx, scope, walk)
    }
}

pub struct CardModule;
pub static CARD_MODULE: CardModule = CardModule;

impl AppModule for CardModule {
    fn id(&self) -> &'static str {
        "card"
    }
    fn label(&self) -> &'static str {
        "Card app"
    }
    /// The module itself asks for nothing; each app it runs is bounded by
    /// its own manifest, resolved and enforced per isolate.
    fn capabilities(&self) -> &'static [&'static str] {
        &[]
    }
    fn open_schema(&self) -> OpenSchema {
        OpenSchema::new(1).arg("app", OpenArgKind::Text, true)
    }
    fn register(&self, vm: &mut ScriptVm) {
        octoscript_widgets::design::script_mod(vm);
        octoscript_widgets::kit::script_mod(vm);
        script_mod(vm);
        crate::register_card_vocabulary();
    }
    fn create(&self, vm: &mut ScriptVm, open: ValidatedOpen, _handles: InstanceHandles) -> InstanceParts {
        let value = script_eval!(vm, { use mod.widgets.* CardAppView {} });
        let root = WidgetRef::script_from_value(vm, value);
        if let Some(mut view) = root.borrow_mut::<CardAppView>() {
            view.app_id = open.text("app").unwrap_or_default().to_string();
        }
        InstanceParts { root, executor: Box::new(CardExecutor), shutdown: Box::new(|_vm| {}) }
    }
}

struct CardExecutor;

impl ServiceExecutor for CardExecutor {
    fn manifest(&self) -> ServiceManifest {
        ServiceManifest::new("card", "Card app", "An installed card app, running in its own contained isolate.")
    }
    fn execute(&mut self, _cx: &mut Cx, call: &ServiceCall) -> ExecOutcome {
        ExecOutcome::Done(ToolResult::unavailable(&call.call_id, "A card app offers no tools to the assistant yet"))
    }
    fn cancel(&mut self, _cx: &mut Cx, _call_id: &str) {}
    fn subscribe(&mut self, _cx: &mut Cx, _sub_id: &str, _topic: &str, _filter: Option<&str>) {}
    fn unsubscribe(&mut self, _cx: &mut Cx, _sub_id: &str) {}
}

#[allow(dead_code)]
fn _unused(_: PathBuf) {}
