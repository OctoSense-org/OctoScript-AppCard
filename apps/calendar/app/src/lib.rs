//! Calendar as a standalone app (the entry crate).
//!
//! The entry lives in a LIBRARY, not a binary: `app_main!` emits `fn main`
//! only off-mobile, and the Android and OpenHarmony packagers load a cdylib.
//! `src/main.rs` is the desktop entry and does nothing but call into here.
//!
//! Calendar as a standalone app: one window, the Calendar module inside
//! it, no window manager. The module is the same `CALENDAR_MODULE` the
//! OctoSense shell links in, so this binary and the shell run identical
//! code; only the host around it differs (`octosense-app-host`).
//!
//! The service settings come from the environment, as they do under the
//! shell: CALENDAR_SERVER, CALENDAR_TOKEN, CALENDAR_DEVICE, CALENDAR_LOCALE.
use makepad_widgets::*;
use octosense_app_host::makepad_app_module::makepad_ai_services; // keep the pinned graph single-rooted

pub use makepad_widgets;

app_main!(
    App,
    font_set: International,
    font_assets: [
        "octosense_calendar/resources/service/NotoSansSC-Regular.ttf",
        "octosense_calendar/resources/service/NotoSansSC-Bold.ttf",
    ]
);

script_mod! {
    use mod.prelude.widgets.*
    use mod.widgets.*

    startup() do #(App::script_component(vm)) {
        ui: Root {
            main_window := Window {
                window.title: "Calendar"
                window.inner_size: vec2(412, 892)
                pass +: { clear_color: #fff }
                body +: {
                    padding: 0 margin: 0 spacing: 0
                    host := AppHostView {}
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
    opened: bool,
}

/// The open arguments the module's schema accepts, from the environment.
fn open_json() -> String {
    let mut fields = Vec::new();
    for (arg, var) in [("server", "CALENDAR_SERVER"), ("token", "CALENDAR_TOKEN"), ("device", "CALENDAR_DEVICE"), ("locale", "CALENDAR_LOCALE")] {
        if let Ok(value) = std::env::var(var) {
            if !value.is_empty() {
                fields.push(format!("{:?}:{:?}", arg, value));
            }
        }
    }
    format!("{{{}}}", fields.join(","))
}

impl AppMain for App {
    fn script_mod(vm: &mut ScriptVm) -> ScriptValue {
        makepad_widgets::script_mod(vm);
        octosense_app_host::script_mod(vm);
        self::script_mod(vm)
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        if !self.opened {
            self.opened = true;
            octosense_app_host::open_in(&self.ui.widget(cx, ids!(host)), &octosense_calendar::CALENDAR_MODULE, &open_json());
        }
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}

#[allow(unused)]
fn _keep(_: &makepad_ai_services::wire::ServiceManifest) {}
