//! One window, one module, no window manager.
//!
//! An `AppModule` never opens a window: it is created inside a splash
//! isolate by a host, which hands it the four things the contract names —
//! a scope, a storage namespace, a viewport and a reply channel — and then
//! draws the root it returns. The OctoSense shell does that in a tile,
//! with a launcher, a bus and a shade around it. This crate does the same
//! thing with nothing around it, so the identical app crate can ship three
//! ways: a desktop binary, a mobile binary, or a module linked into the
//! shell for the ROM.
//!
//! An app's standalone entry is then a window with [`AppHostView`] in it
//! plus one call to [`AppHostViewRef::open`]; see `apps/*/native/src/bin`.
//!
//! What this host deliberately does NOT provide, because there is no shell
//! around it: the assistant bus (the module's `ServiceExecutor` is held but
//! never called), tiles and focus arbitration, and the launcher catalog. A
//! module that only reaches those through the bus still runs; it simply has
//! no assistant in the window.
use makepad_app_module::{AppModule, InstanceHandles, InstanceParts, ModuleUpstream, ReplySink, ServiceExecutor, ValidatedOpen};
use makepad_widgets::widget_async::{enter_isolate, leave_isolate};
use makepad_widgets::*;
use std::sync::mpsc::Receiver;

pub use makepad_app_module;
pub use makepad_widgets;

script_mod! {
    use mod.prelude.widgets_internal.*
    use mod.widgets.*

    mod.widgets.AppHostViewBase = #(AppHostView::register_widget(vm))

    mod.widgets.AppHostView = set_type_default() do mod.widgets.AppHostViewBase {
        width: Fill
        height: Fill
        draw_bg +: { color: #fff }
    }
}

/// The instance this window hosts.
struct Instance {
    module: &'static dyn AppModule,
    vm_id: SplashVmId,
    root: WidgetRef,
    /// Held so the module's tools stay alive for its own internal use; a
    /// standalone window has no assistant to call them.
    _executor: Box<dyn ServiceExecutor>,
    shutdown: Option<Box<dyn FnOnce(&mut ScriptVm)>>,
    upstream: Receiver<ModuleUpstream>,
}

/// The window's body: it creates the instance on the first draw (when the
/// viewport is known) and then draws the module's root inside its isolate.
#[derive(Script, ScriptHook, Widget)]
pub struct AppHostView {
    #[uid]
    uid: WidgetUid,
    #[source]
    source: ScriptObjectRef,
    #[walk]
    walk: Walk,
    #[layout]
    layout: Layout,
    #[redraw]
    #[live]
    draw_bg: DrawColor,
    #[rust]
    instance: Option<Instance>,
    /// Set by [`AppHostViewRef::open`]; consumed by the first draw.
    #[rust]
    pending: Option<Pending>,
    #[rust]
    area: Area,
}

struct Pending {
    module: &'static dyn AppModule,
    open_json: String,
}

impl AppHostView {
    /// Create the instance for `size`: allocate its isolate, jail its
    /// storage under the module id, let it register its widget families,
    /// and keep the root it mints in that heap.
    fn create(&mut self, cx: &mut Cx, pending: Pending, size: DVec2) {
        let module = pending.module;
        let schema = module.open_schema();
        let open: ValidatedOpen = match schema.validate(&pending.open_json, &[]) {
            Ok(open) => open,
            Err(e) => {
                error!("app-host: {} cannot open with {}: {}", module.id(), pending.open_json, e);
                match schema.empty_open() {
                    Ok(open) => open,
                    Err(e) => {
                        error!("app-host: {} cannot open without arguments: {}", module.id(), e);
                        return;
                    }
                }
            }
        };
        // The same jail the shell gives an app's FIRST instance
        // (`calendar.1`), so an app ejected from the shell opens the data it
        // wrote inside it, and vice versa.
        let storage = cx.storage(&format!("{}.1", module.id()));
        let (replies, upstream) = ReplySink::pair();
        let handles = InstanceHandles {
            scope: makepad_app_module::InstanceScope::new(1, 1),
            storage,
            viewport: makepad_app_module::Viewport { size },
            replies,
        };
        // The isolate's own network stays off, as it is in the shell: a
        // module that needs the network declares `net` and does it from
        // Rust (the calendar's sync thread, mail's loopback controller).
        let vm_id = cx.alloc_splash_vm_with_network(false);
        let parts: InstanceParts = cx.with_script_vm_id_trusted(vm_id, |vm| {
            module.register(vm);
            module.create(vm, open, handles)
        });
        cx.widget_tree_insert_child(self.uid, live_id!(root), parts.root.clone());
        log!("app-host: {} open in isolate {:?} at {:.0}x{:.0}", module.id(), vm_id, size.x, size.y);
        self.instance = Some(Instance {
            module,
            vm_id,
            root: parts.root,
            _executor: parts.executor,
            shutdown: Some(parts.shutdown),
            upstream,
        });
    }

    /// Host `module` in this view. `open_json` is the module's open
    /// arguments as JSON (`"{}"` for none); the instance is created on the
    /// next draw, when its viewport is known.
    pub fn open(&mut self, module: &'static dyn AppModule, open_json: &str) {
        self.pending = Some(Pending { module, open_json: open_json.to_string() });
    }

    /// Run the module's shutdown inside its isolate and drop the instance.
    /// The root goes first: nothing may draw a widget whose heap is freed.
    pub fn close(&mut self, cx: &mut Cx) {
        let Some(mut instance) = self.instance.take() else { return };
        // Dropping the instance drops the root ref with it; the ground keeps
        // drawing, as the shell's tile does through its close animation.
        self.draw_bg.redraw(cx);
        let vm_id = instance.vm_id;
        if let Some(shutdown) = instance.shutdown.take() {
            cx.with_script_vm_id_trusted(vm_id, |vm| shutdown(vm));
        }
        log!("app-host: {} closed", instance.module.id());
    }

    /// Whatever the instance sent upstream while nobody was listening: in
    /// the shell these are tool results and publications for the bus, here
    /// they are drained so the channel never fills.
    fn drain_upstream(&mut self) {
        if let Some(instance) = &self.instance {
            while instance.upstream.try_recv().is_ok() {}
        }
    }
}

impl Widget for AppHostView {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.drain_upstream();
        let Some(instance) = &self.instance else { return };
        let (root, vm_id) = (instance.root.clone(), instance.vm_id);
        let entry = enter_isolate(cx, vm_id);
        root.handle_event(cx, event, scope);
        leave_isolate(cx, entry);
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        cx.begin_turtle(walk, self.layout);
        let rect = cx.turtle().rect();
        if let Some(pending) = self.pending.take() {
            // The module is created with the size it will actually draw at,
            // which a window only knows once the turtle has a rect.
            self.create(cx.cx, pending, rect.size);
        }
        if let Some(instance) = &self.instance {
            // The instance's own theme decides the ground under a root that
            // paints only its own chrome.
            if let Some(color) = cx
                .with_script_vm_id_trusted(instance.vm_id, |vm| script_eval!(vm, { mod.theme.color_bg_app }))
                .as_color()
            {
                self.draw_bg.color = Vec4f::from_u32(color);
            }
        }
        self.draw_bg.draw_abs(cx, rect);
        if let Some(instance) = &self.instance {
            let (root, vm_id) = (instance.root.clone(), instance.vm_id);
            let entry = enter_isolate(cx, vm_id);
            root.draw_walk_all(cx, scope, Walk::fill());
            leave_isolate(cx, entry);
        }
        cx.end_turtle_with_area(&mut self.area);
        DrawStep::done()
    }
}

/// Host `module` in the `AppHostView` that `widget` refers to: what an
/// app's standalone entry calls once, on its first event.
pub fn open_in(widget: &WidgetRef, module: &'static dyn AppModule, open_json: &str) {
    match widget.borrow_mut::<AppHostView>() {
        Some(mut view) => view.open(module, open_json),
        None => error!("app-host: the window body is not an AppHostView"),
    }
}
