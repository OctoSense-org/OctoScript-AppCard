//! The standalone binary: the whole app is the `octos_app` library; this
//! target only names its entry point. On Android cargo-makepad builds the
//! library itself as the cdylib (`app_main!` emits the JNI entry points
//! there), so this file is desktop-only glue.

#[cfg(not(any(target_os = "android", target_env = "ohos")))]
fn main() {
    octos_app::entry::app_main();
}

#[cfg(any(target_os = "android", target_env = "ohos"))]
fn main() {}
