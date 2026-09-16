//! The hosting API: the whole app as a widget another Makepad app mounts
//! inside its own tree — no `Window{}`, no `app_main!`.
//!
//! A host (OctoSense's in-process module, say) does three things:
//!
//! 1. [`register_script_mods`] in the VM (or isolate) the app will live in,
//!    after the widgets' own `script_mod`. This registers every prototype the
//!    app's DSL names, the kits, and [`BODY_WIDGET`] — the app's root body
//!    without the standalone `Window{}` around it — plus `OctosAppShell`.
//! 2. [`AppShell::create`] mints the shell: one [`App`] built from the same
//!    DSL the standalone binary uses, with `ui: OctosAppBody{}` in place of
//!    `ui: Root{Window{..}}`. The shell is a `WidgetRef` the host draws and
//!    dispatches like any other; it delivers `Event::Startup` to the app on
//!    first contact (the host's own startup is long gone), so the agent,
//!    the kernel transport, sessions and the composer come up exactly as in
//!    the APK.
//! 3. [`AppShell::ask`] to submit text as if typed into the composer, and
//!    [`AppShell::shutdown`] before the host frees the isolate.
//!
//! The pieces that stay host-owned: the OS window, keyboard/IME insets (the
//! standalone body sits in the window's `KeyboardView`), and everything
//! `Window`-shaped the app asks of `ids!(main_window)` — those lookups come
//! back empty here and the app treats them as no-ops.

use crate::App;
use makepad_widgets::*;

/// The DSL name of the app's root body without the window: `OctosAppBody`.
pub const BODY_WIDGET: &str = "OctosAppBody";

/// Register every script_mod the app owns in `vm`, in the order the
/// standalone `AppMain::script_mod` does — minus `makepad_widgets::script_mod`
/// (the host has run it) and minus the standalone `Window{}` root.
pub fn register_script_mods(vm: &mut ScriptVm) {
    crate::makepad_code_editor::script_mod(vm);
    crate::makepad_diagram_kit::script_mod(vm);
    crate::app::login::script_mod(vm);
    crate::app::approvals::script_mod(vm);
    crate::app::content_browser::script_mod(vm);
    crate::app::viewers::script_mod(vm);
    crate::app::octo_thinking::script_mod(vm);
    crate::app::coding::script_mod(vm);
    // The app's own DSL: every prototype, and `OctosAppBody`.
    crate::script_mod(vm);
    // The shell, and the app component itself as a nameable type.
    self::script_mod(vm);
}

script_mod! {
    use mod.prelude.widgets.*
    use mod.widgets.*

    // The app's state object as a component type, so a host can evaluate
    // `OctosApp{ ui: OctosAppBody{} }` the way `app_main!` evaluates
    // `startup() do #(App::script_component(vm)){ ui: Root{..} }`.
    mod.widgets.OctosApp = #(App::script_component(vm))

    mod.widgets.OctosAppShell = set_type_default() do #(AppShell::register_widget(vm)) {
    }
}

/// The whole app as one widget. Owns the [`App`] (state, agent, timers) and
/// forwards every event to `AppMain::handle_event`; draws the app's body.
#[derive(Script, ScriptHook, Widget)]
pub struct AppShell {
    #[uid]
    uid: WidgetUid,
    #[source]
    source: ScriptObjectRef,
    /// The app's `ui` (the `OctosAppBody` view): walk, area, redraw and the
    /// widget-tree children all come from it.
    #[wrap]
    #[rust]
    body: WidgetRef,
    #[rust]
    app: Option<App>,
    /// `Event::Startup` delivered to the app once, on first event or draw.
    #[rust]
    started: bool,
}

impl AppShell {
    /// Build the shell in `vm`: an `OctosAppShell{}` around one `App` whose
    /// `ui` is `OctosAppBody{}`. Requires [`register_script_mods`] first.
    pub fn create(vm: &mut ScriptVm) -> WidgetRef {
        let shell_value = script_eval!(vm, {
            use mod.widgets.*
            OctosAppShell {}
        });
        let shell = WidgetRef::script_from_value(vm, shell_value);
        let app_value = script_eval!(vm, {
            use mod.prelude.widgets.*
            use mod.widgets.*
            OctosApp {
                ui: OctosAppBody {}
            }
        });
        let mut app = App::script_from_value(vm, app_value);
        <App as AppMain>::after_new_from_script(vm, &mut app);
        if let Some(mut inner) = shell.borrow_mut::<AppShell>() {
            inner.body = app.ui();
            inner.app = Some(app);
        } else {
            log::error!("host: OctosAppShell did not resolve to an AppShell; is register_script_mods missing?");
        }
        shell
    }

    /// Submit `text` as if typed into the composer and sent.
    pub fn ask(&mut self, cx: &mut Cx, text: &str) -> bool {
        self.ensure_started(cx);
        match self.app.as_mut() {
            Some(app) => {
                app.ask(cx, text);
                true
            }
            None => false,
        }
    }

    /// Stop the app's backend (agent, tokio runtime, kernel child). The
    /// widgets stay valid until the host drops the shell.
    pub fn shutdown(&mut self) {
        if let Some(app) = self.app.as_mut() {
            app.shutdown_runtime();
        }
    }

    /// Whether an app is seated in this shell.
    pub fn has_app(&self) -> bool {
        self.app.is_some()
    }

    fn ensure_started(&mut self, cx: &mut Cx) {
        if self.started {
            return;
        }
        self.started = true;
        if let Some(app) = self.app.as_mut() {
            <App as AppMain>::handle_event(app, cx, &Event::Startup);
        }
    }
}

impl Widget for AppShell {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, _scope: &mut Scope) {
        self.ensure_started(cx);
        // The shell delivers the app's ONE `Startup` itself (above). A host
        // that mounts the shell while its own startup is still being
        // dispatched — OctoSense's `--test-action launch-appcard` runs inside
        // the WM's `handle_startup`, and the same `Event::Startup` then walks
        // the tree into this widget — must not start the app twice: a second
        // `handle_startup` rebuilds the agent, and the first kernel child
        // (`kill_on_drop`) dies under the sessions just created on it, so
        // every submit after that is "transport task gone".
        if matches!(event, Event::Startup) {
            return;
        }
        if let Some(app) = self.app.as_mut() {
            <App as AppMain>::handle_event(app, cx, event);
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.ensure_started(cx);
        if self.body.is_empty() {
            return DrawStep::done();
        }
        self.body.draw_walk_all(cx, scope, walk);
        DrawStep::done()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// The hosted path end to end, the way a module host does it: the app's
    /// script_mods in a fresh isolate (network off, `mod.res` gone), then
    /// one shell — with no script errors and an app seated in it.
    #[test]
    fn the_shell_builds_in_an_isolate_without_script_errors() {
        let mut cx = Cx::new(Box::new(|_, _| {}));
        cx.with_vm(makepad_widgets::script_mod);
        let vm_id = cx.alloc_splash_vm_with_network(false);
        let root = cx.with_script_vm_id_trusted(vm_id, |vm| {
            register_script_mods(vm);
            let errors = vm.take_errors();
            assert!(errors.is_empty(), "register_script_mods left script errors: {errors:?}");
            let root = AppShell::create(vm);
            let errors = vm.take_errors();
            assert!(errors.is_empty(), "AppShell::create left script errors: {errors:?}");
            root
        });
        assert!(!root.is_empty(), "the shell is a real widget");
        assert!(
            root.borrow::<AppShell>().map(|s| s.has_app()).unwrap_or(false),
            "the shell seats an App"
        );
        assert!(!root.borrow::<AppShell>().unwrap().body.is_empty(), "the app's body is mounted");
        drop(root);
        cx.free_splash_vm(vm_id);
    }
}
