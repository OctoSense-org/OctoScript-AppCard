//! Desktop entry point; the app itself is in `lib.rs` so mobile packagers
//! have a cdylib to load.
fn main() {
    octosense_calendar_app::app_main()
}
