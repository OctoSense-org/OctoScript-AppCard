//! The OctoSense app store (ADR 0003 §7).
//!
//! Three screens: a searchable list of what the hub offers, a detail screen
//! that says in plain words what an app will be allowed to do BEFORE it is
//! installed, and the app itself running in its own contained isolate.
//!
//! What the store is careful about:
//!
//! - it verifies the catalog against the anchor before showing anything;
//! - it hashes a staged bundle before it reaches a jail;
//! - it shows permissions derived from the resolved policy, never from the
//!   app's own description;
//! - it refuses to open an app whose version has been withdrawn, even when
//!   that app is already installed.
use makepad_app_module::{
    makepad_ai_services::wire::{ServiceCall, ServiceManifest, ToolResult},
    AppModule, ExecOutcome, InstanceHandles, InstanceParts, OpenArgKind, OpenSchema, ServiceExecutor, ValidatedOpen,
};
use makepad_widgets::*;
use octosense_app_hub::{Availability, Listing, Store};
use octosense_app_policy::HostLimits;
use std::path::PathBuf;

pub mod cardapp;
pub mod source;
pub mod ui;

pub use makepad_widgets;

use std::sync::{Mutex, OnceLock};

/// Where installed apps live. The shell sets it from the platform's data
/// directory at startup so the store, the card host and the shell's own
/// launcher catalog all read the same place; `OCTOSENSE_APP_DATA` overrides.
static DATA_ROOT: OnceLock<Mutex<Option<PathBuf>>> = OnceLock::new();

pub fn set_data_root(root: PathBuf) {
    *DATA_ROOT.get_or_init(|| Mutex::new(None)).lock().unwrap() = Some(root);
}

/// The apps root: `$OCTOSENSE_APP_DATA`, else what the host set, else the
/// platform data directory, else a temp directory (tests and previews).
pub fn data_root(cx: &Cx) -> PathBuf {
    if let Some(root) = std::env::var("OCTOSENSE_APP_DATA").ok().filter(|v| !v.is_empty()) {
        return PathBuf::from(root);
    }
    if let Some(root) = DATA_ROOT.get().and_then(|m| m.lock().unwrap().clone()) {
        return root;
    }
    cx.get_data_dir()
        .map(|dir| PathBuf::from(dir).join("apps"))
        .unwrap_or_else(|| std::env::temp_dir().join("octosense-apps"))
}

/// The apps root without a `Cx`, for a host building its launcher catalog.
/// None until the host has set it (or the environment names it).
pub fn data_root_if_set() -> Option<PathBuf> {
    std::env::var("OCTOSENSE_APP_DATA")
        .ok()
        .filter(|v| !v.is_empty())
        .map(PathBuf::from)
        .or_else(|| DATA_ROOT.get().and_then(|m| m.lock().unwrap().clone()))
}

/// An installed card app, as a launcher needs it.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct InstalledApp {
    pub id: String,
    pub name: String,
    pub version: String,
}

/// Every app installed under `root`, read from each bundle's own manifest.
pub fn installed_apps(root: &std::path::Path) -> Vec<InstalledApp> {
    let mut out = Vec::new();
    let Ok(entries) = std::fs::read_dir(root) else { return out };
    for entry in entries.flatten() {
        let manifest = entry.path().join("bundle").join(octosense_app_policy::MANIFEST_FILE);
        let Ok(json) = std::fs::read_to_string(&manifest) else { continue };
        if let Ok(m) = octosense_app_policy::AppManifest::parse(&json) {
            out.push(InstalledApp { id: m.id, name: m.name, version: m.version });
        }
    }
    out.sort_by(|a, b| a.name.cmp(&b.name));
    out
}

/// What the store asks its host to do. A host that links the store handles
/// these; the store never launches an app itself, because an app is a
/// client of the window manager, not a screen inside the store.
#[derive(Clone, Debug, Default)]
pub enum AppStoreAction {
    /// Open this installed app as an app of its own.
    Launch(String),
    /// An app was installed or removed: the launcher's catalog changed.
    CatalogChanged,
    #[default]
    None,
}
pub use octoscript_widgets;

/// The hub anchor this build trusts (ADR 0003 §4). Shipped in the binary;
/// the hub's working key is certified by it, so rotating that key needs no
/// release. `OCTOSENSE_HUB_ANCHOR` overrides it for development only.
pub const DEFAULT_ANCHOR: &str = "6000284a069ba7cada2925094074e8e0baae07e25d1b7fc31f396c993f363e11";

/// The hub this build reads by default: the OctoSense organisation's hub,
/// served from its repository. `OCTOSENSE_HUB` overrides it (a mirror
/// directory or another base URL).
pub const DEFAULT_HUB: &str = "https://raw.githubusercontent.com/OctoSense-org/octosense-app-hub/main/";

script_mod! {
    use mod.prelude.widgets.*

    mod.widgets.AppStoreView = set_type_default() do #(AppStoreView::register_widget(vm)) {
        width: Fill height: Fill flow: Down
        show_bg: true draw_bg.color: #fff
        scroll_bars: mod.widgets.ScrollBars { show_scroll_x: false, show_scroll_y: true }
        header := View {
            width: Fill height: Fit flow: Down padding: Inset{left: 16., right: 16., top: 14., bottom: 6.} spacing: 10
            Label { text: "Apps" draw_text.color: #000 draw_text.text_style.font_size: 30 }
            search := TextInput {
                width: Fill height: Fit
                empty_text: "Games, Apps, Publishers"
                draw_bg.color: #eeeef2 draw_bg.radius: 10 draw_bg.border_width: 0
                draw_text.color: #000
            }
            origin_label := Label { text: "" draw_text.color: #8e8e93 draw_text.text_style.font_size: 10 }
        }
        // One container per screen state: the store swaps what is IN it
        // rather than toggling visibility, so there is never a hidden screen
        // drawing behind a visible one.
        screen := Splash { width: Fill height: Fit }
        // The running app. Empty body means no app, and it takes no space.
        card := Splash { width: Fill height: Fill }
    }
}

#[derive(Clone, Debug, PartialEq)]
enum Screen {
    List,
    Detail(usize),
    Running(String),
}

#[derive(Script, ScriptHook, Widget)]
pub struct AppStoreView {
    #[deref]
    view: View,
    #[rust]
    started: bool,
    #[rust]
    query: String,
    #[rust]
    listings: Vec<Listing>,
    #[rust(Screen::List)]
    screen: Screen,
    #[rust]
    store: Option<Store>,
    #[rust]
    origin: Option<source::Origin>,
    #[rust]
    app_data_root: PathBuf,
    #[rust]
    status: String,
    /// Serves the running app its own artwork, and dies with it.
    #[rust]
    asset_server: Option<octosense_app_policy::AssetServer>,
    #[rust]
    layout_logged: bool,
}

impl AppStoreView {
    /// Load the catalog and verify it. Everything the store shows comes from
    /// a catalog that passed this; a failure leaves the list empty and says
    /// why, rather than showing unverified apps.
    fn start(&mut self, cx: &mut Cx) {
        // Installed apps live under the platform's data directory (the
        // app's files dir on Android), one jail per app; the environment
        // overrides it for development.
        self.app_data_root = data_root(cx);
        let anchor = std::env::var("OCTOSENSE_HUB_ANCHOR").unwrap_or_else(|_| DEFAULT_ANCHOR.to_string());
        let mut store = Store::new(&anchor, &self.app_data_root, HostLimits::default());

        // A hub override on disk (`<data dir>/hub.txt`, a path or a base URL)
        // wins over the built-in hub: how a device with no route to the
        // public hub reads a mirror, and how a test phone reads one over USB.
        let override_path = cx.get_data_dir().map(|dir| PathBuf::from(dir).join("hub.txt"));
        let override_value = override_path
            .as_ref()
            .and_then(|path| std::fs::read_to_string(path).ok())
            .map(|text| text.trim().to_string())
            .filter(|text| !text.is_empty());
        self.origin = match override_value {
            Some(value) => Some(source::Origin::parse(&value)),
            None => source::Origin::from_env(),
        };
        match &self.origin {
            None => self.status = "No hub configured. Set OCTOSENSE_HUB to a hub mirror.".into(),
            Some(origin) => match origin.catalog().and_then(|json| store.accept_catalog(&json)) {
                Ok(()) => {
                    // The verified catalog is kept beside the apps, so an app
                    // opened later (without the store) can still check that
                    // its version is offered and not withdrawn.
                    if let Ok(json) = origin.catalog() {
                        let _ = std::fs::create_dir_all(&self.app_data_root);
                        let _ = std::fs::write(self.app_data_root.join("catalog.json"), json);
                    }
                    let count = store.catalog().map(|c| c.entries.len()).unwrap_or(0);
                    let today = octosense_app_hub::today();
                    self.status = match store.installs_allowed(&today) {
                        Ok(()) => format!(
                            "{count} app(s) from {} · catalog {} day(s) old",
                            origin.describe(),
                            store.catalog_age_days(&today).unwrap_or(0)
                        ),
                        Err(reason) => format!("{count} app(s) · {reason}"),
                    };
                }
                Err(e) => {
                    // The status line truncates on a phone; the log holds
                    // the whole reason.
                    error!("appstore: catalog from {} refused: {e}", origin.describe());
                    self.status = format!("This catalog was refused: {e}");
                }
            },
        }
        self.store = Some(store);
        self.refresh(cx);
    }

    /// Re-read the listings for the current query and rebuild the screen.
    fn refresh(&mut self, cx: &mut Cx) {
        self.listings = self.store.as_ref().map(|s| s.search(&self.query)).unwrap_or_default();
        self.view.label(cx, ids!(origin_label)).set_text(cx, &self.status);
        let screen = self.screen.clone();
        let asset_base = self.asset_base();
        let body = match &screen {
            Screen::List => ui::list_source(&self.listings, &self.query, asset_base.as_deref()),
            Screen::Detail(index) => match self.listings.get(*index) {
                Some(listing) => ui::detail_source(listing, &self.status, asset_base.as_deref()),
                None => {
                    self.screen = Screen::List;
                    return self.refresh(cx);
                }
            },
            Screen::Running(app_id) => ui::running_source(app_id, &self.status),
        };
        self.mount(cx, ids!(screen), &body);
        self.layout_logged = false;
        if !matches!(screen, Screen::Running(_)) {
            // No app running: the card container holds nothing and its
            // isolate has nothing to draw.
            self.view.splash(cx, ids!(card)).set_text(cx, "");
        }
        self.view.redraw(cx);
    }

    /// Where listing images come from: the hub over HTTP. A mirror directory
    /// has no origin the widgets can load from, so its listings show no
    /// pictures.
    fn asset_base(&self) -> Option<String> {
        match &self.origin {
            Some(source::Origin::Http(base)) => Some(format!("{}/", base.trim_end_matches('/'))),
            _ => None,
        }
    }

    /// Evaluate generated source into `target`. Trusted-tier UI only: see the
    /// note at the top of `ui.rs`.
    fn mount(&mut self, cx: &mut Cx, target: &[LiveId], body: &str) {
        let code = format!("use mod.prelude.widgets.*\nreturn View{{{body}}}");
        let script_mod = ScriptMod {
            cargo_manifest_path: env!("CARGO_MANIFEST_DIR").into(),
            module_path: module_path!().into(),
            file: file!().into(),
            line: 1,
            column: 0,
            code,
            values: Vec::new(),
        };
        let built = cx.with_vm(|vm| vm.eval_checked(script_mod, 2_000_000).map(|value| View::script_from_value(vm, value)));
        let Some(built) = built else {
            error!("appstore: the store's own screen did not evaluate");
            return;
        };
        let host = self.view.widget(cx, target);
        let Some(mut host_splash) = host.borrow_mut::<makepad_widgets::splash::Splash>() else {
            error!("appstore: {target:?} is not a screen container");
            return;
        };
        host_splash.view = built;
        let uid = host_splash.widget_uid();
        let mut children = Vec::new();
        host_splash.children(&mut |id, child| children.push((id, child)));
        drop(host_splash);
        for (id, child) in children {
            cx.widget_tree_insert_child_deep(uid, id, child);
        }
        cx.widget_tree_mark_dirty(uid);
    }

    /// Install the app at `index`, then show it as installed. Every check the
    /// client makes is reported rather than swallowed: a refusal is the most
    /// useful thing the store can say.
    fn install(&mut self, cx: &mut Cx, index: usize) {
        let Some(listing) = self.listings.get(index).cloned() else { return };
        let (Some(store), Some(origin)) = (self.store.as_ref(), self.origin.as_ref()) else { return };
        let Some(entry) = store.entry(&listing.app_id) else { return };
        let artifact = entry.artifact.clone();
        let staging = self.app_data_root.join(&listing.app_id);
        if let Err(e) = std::fs::create_dir_all(&staging) {
            self.status = format!("Cannot prepare {}: {e}", listing.app_id);
            return self.refresh(cx);
        }
        self.status = match origin
            .stage(&artifact, &staging)
            .and_then(|staged| {
                // The publisher's key comes from the signed catalog, so the
                // store checks their signature itself rather than trusting
                // that the hub did.
                let keys = store.publisher_keys();
                store
                    .install_staged(&listing.app_id, &staged, &keys, &octosense_app_hub::today())
                    .map(|policy| (staged, policy))
            })
        {
            Ok((staged, policy)) => {
                let _ = std::fs::remove_dir_all(&staged);
                format!("Installed {} {} — {} capability(ies)", listing.name, listing.version, policy.capabilities.len())
            }
            Err(e) => format!("Not installed: {e}"),
        };
        self.refresh(cx);
    }

    /// Open an installed app: check it may still run, apply its policy to the
    /// isolate, then hand the card's source to that isolate.
    fn open(&mut self, cx: &mut Cx, app_id: &str) {
        let Some(store) = self.store.as_ref() else { return };
        let policy = match store.may_run(app_id) {
            Ok(policy) => policy,
            Err(e) => {
                self.status = format!("Cannot open: {e}");
                return self.refresh(cx);
            }
        };
        let mut settings = policy.isolate_settings(&self.app_data_root);
        if let Err(e) = std::fs::create_dir_all(&settings.jail_root) {
            self.status = format!("Cannot make the app's jail: {e}");
            return self.refresh(cx);
        }
        let bundle = store.install_dir(app_id);
        // One asset origin per running app, serving only that app's bundle.
        // It is the ONE loopback entry the isolate may reach: exactly this
        // port, so a sibling app's origin or a stray dev server is refused.
        let origin = match octosense_app_policy::AssetServer::start(&bundle) {
            Ok(server) => {
                let origin = server.origin().to_string();
                settings.hosts.push(server.allowlist_entry());
                self.asset_server = Some(server);
                origin
            }
            Err(e) => {
                self.status = format!("Cannot serve the app's artwork: {e}");
                return self.refresh(cx);
            }
        };
        let splash = self.view.splash(cx, ids!(card));
        let applied = octosense_app_policy::splash_adapter::apply(&splash, cx, &settings);
        match card_source(&bundle, &origin) {
            Ok(code) => {
                splash.set_text(cx, &code);
                self.screen = Screen::Running(app_id.to_string());
                self.status = format!(
                    "{} running · storage {} bytes · {} instructions · {} MB heap · {} host(s)",
                    app_id,
                    applied.storage_quota,
                    applied.instruction_budget,
                    applied.memory_bytes / (1024 * 1024),
                    applied.hosts
                );
            }
            Err(e) => self.status = format!("The app did not open: {e}"),
        }
        self.refresh(cx);
    }
}

/// The cards this process runs draw with the kit, so every isolate gets
/// that vocabulary. Process-wide by the runtime's design (see ADR 0002's
/// open question on per-app vocabulary); registered once, whichever host
/// links the store or the card module.
pub(crate) fn register_card_vocabulary() {
    use std::sync::Once;
    static ONCE: Once = Once::new();
    ONCE.call_once(|| {
        fn design(vm: &mut ScriptVm) {
            octoscript_widgets::design::script_mod(vm);
        }
        fn kit(vm: &mut ScriptVm) {
            octoscript_widgets::kit::script_mod(vm);
        }
        makepad_widgets::widget_async::register_splash_isolate_mod(design);
        makepad_widgets::widget_async::register_splash_isolate_mod(kit);
    });
}

/// Lower a card bundle to isolate source. Nothing outside the bundle is read.
pub(crate) fn card_source(bundle: &std::path::Path, asset_origin: &str) -> Result<String, String> {
    let card = std::fs::read_to_string(bundle.join("page.card")).map_err(|e| format!("page.card: {e}"))?;
    let data_text = std::fs::read_to_string(bundle.join("page.data.json")).unwrap_or_else(|_| "{}".into());
    let mut data: serde_json::Value = serde_json::from_str(&data_text).map_err(|e| format!("page.data.json: {e}"))?;
    octosense_app_policy::rewrite_assets(&mut data, asset_origin);
    let prepared = octoscript_makepad::l0::prepare(&card, &data, &bundle.join("kit"))?;
    let ui = octoscript_makepad::design::to_makepad_ui(&prepared.tree)?;
    Ok(format!("width:Fill height:Fill flow:Overlay {ui}"))
}

impl Widget for AppStoreView {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if !self.started {
            self.started = true;
            self.start(cx);
        }
        self.view.handle_event(cx, event, scope);
        let Event::Actions(actions) = event else { return };

        if let Some(query) = self.view.text_input(cx, ids!(search)).changed(actions) {
            self.query = query;
            if matches!(self.screen, Screen::List) {
                self.refresh(cx);
            }
        }
        match self.screen.clone() {
            Screen::List => {
                for index in 0..self.listings.len() {
                    if self.view.button(cx, &[LiveId::from_str(&format!("open_{index}"))]).clicked(actions) {
                        self.screen = Screen::Detail(index);
                        self.status.clear();
                        self.refresh(cx);
                        break;
                    }
                }
            }
            Screen::Detail(index) => {
                if self.view.button(cx, ids!(back_button)).clicked(actions) {
                    self.screen = Screen::List;
                    self.status.clear();
                    self.refresh(cx);
                } else if self.view.button(cx, ids!(action_button)).clicked(actions) {
                    match self.listings.get(index).map(|l| (l.app_id.clone(), l.availability.clone())) {
                        Some((app_id, Availability::Installed { .. })) => {
                            // The host opens it as an app of its own. With no
                            // host listening (the standalone store), fall back
                            // to running it in place.
                            if std::env::var("OCTOSENSE_STORE_INLINE").is_ok() {
                                self.open(cx, &app_id);
                            } else {
                                cx.widget_action(self.view.widget_uid(), AppStoreAction::Launch(app_id));
                            }
                        }
                        Some((_, Availability::Installable)) => {
                            self.install(cx, index);
                            cx.widget_action(self.view.widget_uid(), AppStoreAction::CatalogChanged);
                        }
                        _ => {}
                    }
                } else if self.view.button(cx, ids!(remove_button)).clicked(actions) {
                    if let (Some(store), Some(listing)) = (self.store.as_ref(), self.listings.get(index)) {
                        self.status = match store.remove(&listing.app_id) {
                            Ok(()) => format!("Removed {} and its data", listing.name),
                            Err(e) => format!("Not removed: {e}"),
                        };
                        self.refresh(cx);
                        cx.widget_action(self.view.widget_uid(), AppStoreAction::CatalogChanged);
                    }
                }
            }
            Screen::Running(_) => {
                if self.view.button(cx, ids!(close_button)).clicked(actions) {
                    // The app's asset origin goes when the app does.
                    self.asset_server = None;
                    self.screen = Screen::List;
                    self.refresh(cx);
                }
            }
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        let step = self.view.draw_walk(cx, scope, walk);
        // Layout evidence for a host with no instrument (a phone): where the
        // detail screen's controls landed, once per screen change.
        if matches!(self.screen, Screen::Detail(_)) && !self.layout_logged {
            let names = ["back_button", "action_button", "remove_button", "status_label"];
            let mut report = Vec::new();
            for name in names {
                let widget = self.view.widget(cx, &[LiveId::from_str(name)]);
                let rect = if widget.is_empty() { None } else { Some(widget.area().rect(cx)) };
                report.push(format!("{name}={:?}", rect.map(|r| (r.pos.x as i32, r.pos.y as i32, r.size.x as i32, r.size.y as i32))));
            }
            let screen = self.view.widget(cx, ids!(screen)).area().rect(cx);
            log!("appstore layout: screen container {:?}; {}", (screen.pos.y as i32, screen.size.y as i32), report.join(" "));
            self.layout_logged = true;
        }
        step
    }
}

pub struct AppStoreModule;
pub static APPSTORE_MODULE: AppStoreModule = AppStoreModule;

impl AppModule for AppStoreModule {
    fn id(&self) -> &'static str {
        "appstore"
    }
    fn label(&self) -> &'static str {
        "Apps"
    }
    /// Storage for what it installs; nothing else. The store holds the anchor
    /// and writes jails because it is trusted-tier code, not because a
    /// capability grants it.
    fn capabilities(&self) -> &'static [&'static str] {
        &["storage"]
    }
    fn open_schema(&self) -> OpenSchema {
        OpenSchema::new(1).arg("app", OpenArgKind::Text, false)
    }
    fn register(&self, vm: &mut ScriptVm) {
        octoscript_widgets::design::script_mod(vm);
        octoscript_widgets::kit::script_mod(vm);
        script_mod(vm);
        register_card_vocabulary();
    }
    fn create(&self, vm: &mut ScriptVm, open: ValidatedOpen, handles: InstanceHandles) -> InstanceParts {
        let value = script_eval!(vm, { use mod.widgets.* AppStoreView {} });
        let root = WidgetRef::script_from_value(vm, value);
        if let Some(mut store) = root.borrow_mut::<AppStoreView>() {
            // Opening straight onto an app, so a launcher entry can point at
            // one; the store still verifies before it runs anything.
            if let Some(app) = open.text("app") {
                store.screen = Screen::Running(app.to_owned());
            }
            let _ = handles.viewport;
        }
        InstanceParts {
            root,
            executor: Box::new(AppStoreExecutor),
            shutdown: Box::new(|_vm| {}),
        }
    }
}

struct AppStoreExecutor;

impl ServiceExecutor for AppStoreExecutor {
    fn manifest(&self) -> ServiceManifest {
        ServiceManifest::new("appstore", "Apps", "Browse, install and open apps published to the OctoSense app hub.")
    }
    fn execute(&mut self, _cx: &mut Cx, call: &ServiceCall) -> ExecOutcome {
        // Installing is a decision a person makes in front of the screen,
        // not a tool an agent calls.
        ExecOutcome::Done(ToolResult::unavailable(&call.call_id, "Use the Apps interface"))
    }
    fn cancel(&mut self, _cx: &mut Cx, _call_id: &str) {}
    fn subscribe(&mut self, _cx: &mut Cx, _sub_id: &str, _topic: &str, _filter: Option<&str>) {}
    fn unsubscribe(&mut self, _cx: &mut Cx, _sub_id: &str) {}
}
