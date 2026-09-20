//! Where the catalog and its artifacts come from.
//!
//! Two sources, one interface. A directory is a mirrored hub, which is what
//! tests and an offline device use. An HTTP origin is the ordinary case.
//! Neither is trusted: whatever comes back is verified against the anchor
//! before it is read, and a bundle is unpacked and hashed before it is
//! installed, so a hostile origin can withhold but not forge.
use octosense_app_hub::Remote;
use std::path::{Path, PathBuf};

#[derive(Clone, Debug)]
pub enum Origin {
    /// A mirrored hub: `<dir>/catalog.json` and `<dir>/artifacts/…`.
    Directory(PathBuf),
    /// `<base>/catalog.json` and `<base>/artifacts/….pack.json` over HTTP.
    Http(String),
}

impl Origin {
    /// `OCTOSENSE_HUB` when set (a path, or a URL when it starts with http),
    /// else the built-in hub.
    pub fn from_env() -> Option<Origin> {
        let value = std::env::var("OCTOSENSE_HUB")
            .ok()
            .filter(|v| !v.is_empty())
            .unwrap_or_else(|| crate::DEFAULT_HUB.to_string());
        Some(Origin::parse(&value))
    }

    /// A URL when it starts with http, else a mirror directory.
    pub fn parse(value: &str) -> Origin {
        if value.starts_with("http") { Origin::Http(value.to_string()) } else { Origin::Directory(PathBuf::from(value)) }
    }

    pub fn describe(&self) -> String {
        match self {
            Origin::Directory(path) => path.display().to_string(),
            Origin::Http(base) => base.clone(),
        }
    }

    /// The catalog's bytes. Verification happens in the caller: this only
    /// fetches.
    pub fn catalog(&self) -> Result<String, String> {
        match self {
            Origin::Directory(dir) => std::fs::read_to_string(dir.join("catalog.json")).map_err(|e| format!("catalog: {e}")),
            Origin::Http(base) => Remote::new(base).catalog(),
        }
    }

    /// Stage an artifact for install: put the bundle somewhere the store can
    /// hash it before it goes anywhere near an app jail.
    pub fn stage(&self, artifact: &str, into: &Path) -> Result<PathBuf, String> {
        let staged = into.join("staged");
        if staged.exists() {
            std::fs::remove_dir_all(&staged).map_err(|e| e.to_string())?;
        }
        match self {
            Origin::Directory(dir) => {
                let from = dir.join(artifact);
                if !from.is_dir() {
                    return Err(format!("{} is not in this hub mirror", from.display()));
                }
                copy_tree(&from, &staged)?;
            }
            Origin::Http(base) => {
                let pack = Remote::new(base).pack(artifact)?;
                octosense_app_hub::unpack(&pack, &staged)?;
            }
        }
        Ok(staged)
    }
}

fn copy_tree(from: &Path, to: &Path) -> Result<(), String> {
    std::fs::create_dir_all(to).map_err(|e| e.to_string())?;
    for entry in std::fs::read_dir(from).map_err(|e| format!("{}: {e}", from.display()))? {
        let entry = entry.map_err(|e| e.to_string())?;
        let kind = entry.file_type().map_err(|e| e.to_string())?;
        if kind.is_symlink() {
            return Err("a bundle may not hold a symlink".into());
        }
        let target = to.join(entry.file_name());
        if kind.is_dir() {
            copy_tree(&entry.path(), &target)?;
        } else {
            std::fs::copy(entry.path(), &target).map_err(|e| e.to_string())?;
        }
    }
    Ok(())
}
