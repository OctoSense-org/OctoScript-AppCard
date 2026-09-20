//! The store as a standalone app: the same APPSTORE_MODULE the shell links,
//! hosted in one window by octosense-app-host.
//!
//! `OCTOSENSE_HUB` points at a hub mirror, `OCTOSENSE_HUB_ANCHOR` at the
//! anchor public key to trust, and `OCTOSENSE_APP_DATA` at where installed
//! apps keep their jails.
use makepad_widgets::*;

pub use makepad_widgets;

app_main!(App, font_set: International);

script_mod! {
    use mod.prelude.widgets.*
    use mod.widgets.*

    startup() do #(App::script_component(vm)) {
        ui: Root {
            main_window := Window {
                window.title: "Apps"
                window.inner_size: vec2(412, 892)
                pass +: { clear_color: #f2f2f6 }
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

impl AppMain for App {
    fn script_mod(vm: &mut ScriptVm) -> ScriptValue {
        makepad_widgets::script_mod(vm);
        octosense_app_host::script_mod(vm);
        self::script_mod(vm)
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        if !self.opened {
            self.opened = true;
            octosense_app_host::open_in(&self.ui.widget(cx, ids!(host)), &octosense_appstore::APPSTORE_MODULE, "{}");
        }
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}
