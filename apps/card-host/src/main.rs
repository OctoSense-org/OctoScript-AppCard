//! Run one card bundle under its own policy.
//!
//! ```sh
//! card-host --bundle <dir> [--app-data <dir>] [--allow-unsigned] [--stamp]
//! ```
//!
//! The bundle is a directory holding `manifest.json`, `page.card`,
//! `page.data.json` and a `kit/` directory. `--stamp` rewrites the manifest's
//! digest to match the directory, which is what a build step does before
//! signing; without it a bundle whose bytes changed is refused.
//!
//! The order is the one ADR 0002 fixes: admit, resolve, apply, then evaluate.
//! Nothing here may widen what the manifest asked for, and the two settings
//! the runtime cannot enforce yet are printed rather than assumed.
use makepad_widgets::*;
use octosense_app_policy::{admit_and_resolve_dir, AppPolicy, HostLimits, RefuseAllSignatures};
use std::path::{Path, PathBuf};

app_main!(
    App,
    font_set: International,
    font_assets: [
        "octosense_card_host/resources/service/NotoSansSC-Regular.ttf",
        "octosense_card_host/resources/service/NotoSansSC-Bold.ttf",
    ]
);

script_mod! {
    use mod.prelude.widgets.*
    use mod.widgets.*

    startup() do #(App::script_component(vm)) {
        ui: Root {
            main_window := Window {
                window.title: "Card host"
                window.inner_size: vec2(412, 892)
                pass +: { clear_color: #fff }
                body +: {
                    padding: 0 margin: 0 spacing: 0
                    card := Splash { width: Fill height: Fill }
                }
            }
        }
    }
}

#[derive(Script, ScriptHook)]
pub struct App {
    #[live]
    ui: WidgetRef,
    #[rust]
    mounted: bool,
    #[rust]
    assets: Option<octosense_app_policy::AssetServer>,
}

struct Args {
    bundle: PathBuf,
    app_data: PathBuf,
    allow_unsigned: bool,
    stamp: bool,
}

fn args() -> Args {
    let argv: Vec<String> = std::env::args().collect();
    let value = |name: &str| argv.windows(2).find(|w| w[0] == name).map(|w| w[1].clone());
    Args {
        bundle: value("--bundle").map(PathBuf::from).unwrap_or_else(|| PathBuf::from(".")),
        app_data: value("--app-data")
            .map(PathBuf::from)
            .unwrap_or_else(|| std::env::temp_dir().join("octosense-card-apps")),
        allow_unsigned: argv.iter().any(|a| a == "--allow-unsigned"),
        stamp: argv.iter().any(|a| a == "--stamp"),
    }
}

/// Admit the bundle and resolve what it gets. Refusals are fatal: a card that
/// cannot be admitted must not be drawn, not even partially.
fn policy_for(args: &Args) -> Result<AppPolicy, String> {
    let manifest_path = args.bundle.join(octosense_app_policy::MANIFEST_FILE);
    let mut manifest_json = std::fs::read_to_string(&manifest_path)
        .map_err(|e| format!("{}: {e}", manifest_path.display()))?;
    let digest = octosense_app_policy::digest_dir(&args.bundle)?;

    if args.stamp {
        let mut value: serde_json::Value = serde_json::from_str(&manifest_json).map_err(|e| e.to_string())?;
        value["integrity"]["bundle_blake3"] = serde_json::Value::String(digest.clone());
        manifest_json = serde_json::to_string_pretty(&value).map_err(|e| e.to_string())?;
        std::fs::write(&manifest_path, format!("{manifest_json}\n")).map_err(|e| e.to_string())?;
        log!("card-host: stamped {} with digest {}", manifest_path.display(), digest);
    }

    let limits = HostLimits { require_signature: !args.allow_unsigned, ..HostLimits::default() };
    // The digest is computed from the directory, so the manifest's claim is
    // checked against what is actually there.
    admit_and_resolve_dir(&manifest_json, &digest, &limits, &RefuseAllSignatures)
}

/// Lower the card to isolate source: realize it, then lower it with the kit
/// that ships in the bundle. Nothing is read from outside the bundle.
fn card_source(bundle: &Path, asset_origin: &str) -> Result<String, String> {
    let card = std::fs::read_to_string(bundle.join("page.card")).map_err(|e| format!("page.card: {e}"))?;
    let data_text = std::fs::read_to_string(bundle.join("page.data.json")).unwrap_or_else(|_| "{}".into());
    let mut data: serde_json::Value = serde_json::from_str(&data_text).map_err(|e| format!("page.data.json: {e}"))?;
    octosense_app_policy::rewrite_assets(&mut data, asset_origin);
    let prepared = octoscript_makepad::l0::prepare(&card, &data, &bundle.join("kit"))?;
    let ui = octoscript_makepad::design::to_makepad_ui(&prepared.tree)?;
    // The isolate's prelude opens a `View{`; the body continues it, exactly as
    // a splash app's body does.
    Ok(format!("width:Fill height:Fill flow:Overlay {ui}"))
}

/// Give every card isolate the kit vocabulary it needs to draw.
///
/// An isolate starts with the standard widgets only, so a lowered L0 card,
/// which names `DesignSurface`, `KitButton` and friends, does not evaluate
/// without this. Note the shape of the hook: it is PROCESS-WIDE, so every
/// isolate gets the same vocabulary. ADR 0002 phase 1 wants this per app,
/// from the manifest; until the runtime can do that, a host must choose one
/// vocabulary for all its cards and keep it to drawing.
fn register_card_vocabulary() {
    use makepad_widgets::widget_async::register_splash_isolate_mod;
    fn design(vm: &mut ScriptVm) {
        octoscript_widgets::design::script_mod(vm);
    }
    fn kit(vm: &mut ScriptVm) {
        octoscript_widgets::kit::script_mod(vm);
    }
    register_splash_isolate_mod(design);
    register_splash_isolate_mod(kit);
}

impl App {
    fn mount(&mut self, cx: &mut Cx) {
        let args = args();
        let policy = match policy_for(&args) {
            Ok(policy) => policy,
            Err(e) => {
                error!("card-host: refused: {e}");
                return;
            }
        };
        log!(
            "card-host: {} {} admitted — capabilities {:?}, hosts {:?}, storage {} bytes, agent {}",
            policy.app_id,
            policy.version,
            policy.capabilities,
            policy.hosts,
            policy.storage_bytes,
            policy.agent.as_ref().map(|a| a.profile.as_kernel_mode()).unwrap_or("none"),
        );

        let mut settings = policy.isolate_settings(&args.app_data);
        if let Err(e) = std::fs::create_dir_all(&settings.jail_root) {
            error!("card-host: cannot make the app's jail at {}: {e}", settings.jail_root.display());
            return;
        }
        // The app's artwork is served from a loopback origin of our own,
        // serving only its bundle, and that origin — this port, no other — is
        // the one loopback entry the isolate may reach.
        let server = match octosense_app_policy::AssetServer::start(&args.bundle) {
            Ok(server) => server,
            Err(e) => {
                error!("card-host: cannot serve the app's artwork: {e}");
                return;
            }
        };
        settings.hosts.push(server.allowlist_entry());
        let origin = server.origin().to_string();
        self.assets = Some(server);
        let splash = self.ui.splash(cx, ids!(card));
        let applied = octosense_app_policy::splash_adapter::apply(&splash, cx, &settings);
        log!(
            "card-host: isolate jailed at {} with {} bytes, {} capability(ies), {} host(s), {} instructions, {} bytes of heap, prompts {} — all enforced",
            settings.jail_root.display(),
            applied.storage_quota,
            applied.capabilities,
            applied.hosts,
            applied.instruction_budget,
            applied.memory_bytes,
            settings.host_prompts,
        );

        // The session profile this app's agent would run under. Printed here
        // so the two containers can be compared at a glance; asking the kernel
        // for it is the next phase.
        if let Some(session) = policy.session_profile(&args.app_data) {
            match serde_json::to_string(&session) {
                Ok(json) => log!("card-host: agent session profile {json}"),
                Err(e) => error!("card-host: cannot render the session profile: {e}"),
            }
        }

        match card_source(&args.bundle, &origin) {
            Ok(source) => splash.set_text(cx, &source),
            Err(e) => error!("card-host: the card did not lower: {e}"),
        }
    }
}

impl AppMain for App {
    fn script_mod(vm: &mut ScriptVm) -> ScriptValue {
        makepad_widgets::script_mod(vm);
        octoscript_widgets::design::script_mod(vm);
        octoscript_widgets::kit::script_mod(vm);
        self::script_mod(vm)
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        if !self.mounted {
            self.mounted = true;
            register_card_vocabulary();
            self.mount(cx);
        }
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}
