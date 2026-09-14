use std::env;

fn main() {
    pin_splash_runtime();
    // `mobile` — Android and OpenHarmony share a phone-shaped shell: a native
    // composer overlay instead of a docked one, a soft keyboard, a sandboxed
    // per-app HOME, and no desktop window chrome. Gate that shared behaviour on
    // `mobile` rather than repeating
    // `any(target_os = "android", target_env = "ohos")` at every site.
    //
    // NOTE iOS is deliberately NOT included: it has its own shell and its own
    // backend, and folding it in here would silently change its behaviour at
    // every one of these sites. Add it only with per-site review.
    println!("cargo:rustc-check-cfg=cfg(mobile)");
    if env::var("CARGO_CFG_TARGET_OS").unwrap_or_default() == "android"
        || env::var("CARGO_CFG_TARGET_ENV").unwrap_or_default() == "ohos"
    {
        println!("cargo:rustc-cfg=mobile");
    }
}

// Pin source contents, resources and lockfiles, including local path patches.
// A Git revision alone misses the working-tree fixes that this app is running.
fn pin_splash_runtime() {
    use std::{fs, path::{Path, PathBuf}};
    fn collect(path: &Path, files: &mut Vec<PathBuf>) {
        if path.is_dir() {
            for entry in fs::read_dir(path).expect("read runtime bundle") {
                let entry = entry.expect("read runtime entry");
                if matches!(entry.file_name().to_str(), Some(".git" | "target" | "node_modules" | ".DS_Store")) { continue; }
                // Repositories do not depend on directory symlinks; avoid cycles.
                if entry.file_type().expect("runtime file type").is_symlink() && entry.path().is_dir() { continue; }
                collect(&entry.path(), files);
            }
        } else if path.is_file() { files.push(path.to_owned()); }
    }
    let root = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap()).join("../..").canonicalize().unwrap();
    let mut files = Vec::new();
    for path in ["aichat", "app/app/src", "app/app/resources", "Octoscript/crates/octoscript-ui-l0", "Octoscript-Makepad/crates/octoscript-node",
        "app/crates", "octos/crates/octos-core", "app/Cargo.toml", "app/Cargo.lock", "app/app/Cargo.toml", "app/app/build.rs", "app/.cargo"] {
        collect(&root.join(path), &mut files);
    }
    files.sort();
    let mut hash = blake3::Hasher::new();
    for path in files {
        println!("cargo:rerun-if-changed={}", path.display());
        let name = path.strip_prefix(&root).unwrap().to_string_lossy();
        let bytes = fs::read(&path).expect("read pinned runtime file");
        hash.update(&(name.len() as u64).to_le_bytes());
        hash.update(name.as_bytes());
        hash.update(&(bytes.len() as u64).to_le_bytes());
        hash.update(&bytes);
    }
    let mut config: Vec<_> = env::vars().filter(|(name, _)| name.starts_with("CARGO_FEATURE_") || matches!(name.as_str(), "TARGET" | "OPT_LEVEL" | "DEBUG" | "CARGO_ENCODED_RUSTFLAGS")).collect();
    config.sort();
    hash.update(format!("{config:?}").as_bytes());
    let rustc = std::process::Command::new(env::var("RUSTC").unwrap()).arg("-vV").output().expect("rustc version");
    assert!(rustc.status.success());
    hash.update(&rustc.stdout);
    println!("cargo:rustc-env=SPLASH_RUNTIME_BUNDLE={}", hash.finalize().to_hex());
}
