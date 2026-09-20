//! A bundle as one file, for delivery over HTTP.
//!
//! A bundle is a directory, and the digest is defined over the directory
//! ([`octosense_app_policy::digest_dir`]). Serving a directory over HTTP means
//! a request per file; a pack is the same files in one JSON document, so a
//! device fetches once, unpacks into a staging directory, and hashes THAT —
//! the pack itself carries no authority, the unpacked bytes do.
//!
//! Base64 in JSON is not compact, but it needs no archive dependency, is
//! trivially inspectable, and bundles are small by rule (8 MB ceiling).
use base64::Engine;
use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;
use std::path::{Component, Path};

pub const PACK_SCHEMA: u32 = 1;

#[derive(Serialize, Deserialize)]
pub struct Pack {
    pub schema: u32,
    /// Relative path → base64 bytes, sorted so a pack is deterministic.
    pub files: BTreeMap<String, String>,
}

/// Pack every file under `root`, the manifest included, so the unpacked
/// directory is the bundle exactly.
pub fn pack_dir(root: &Path) -> Result<Pack, String> {
    let mut files = BTreeMap::new();
    collect(root, root, &mut files)?;
    Ok(Pack { schema: PACK_SCHEMA, files })
}

fn collect(root: &Path, dir: &Path, out: &mut BTreeMap<String, String>) -> Result<(), String> {
    for entry in std::fs::read_dir(dir).map_err(|e| format!("{}: {e}", dir.display()))? {
        let entry = entry.map_err(|e| e.to_string())?;
        let path = entry.path();
        let kind = entry.file_type().map_err(|e| e.to_string())?;
        if kind.is_symlink() {
            return Err(format!("{}: a bundle may not hold a symlink", path.display()));
        }
        if kind.is_dir() {
            collect(root, &path, out)?;
            continue;
        }
        let relative = path.strip_prefix(root).map_err(|e| e.to_string())?;
        let bytes = std::fs::read(&path).map_err(|e| format!("{}: {e}", path.display()))?;
        out.insert(
            relative.to_string_lossy().replace('\\', "/"),
            base64::engine::general_purpose::STANDARD.encode(bytes),
        );
    }
    Ok(())
}

/// Unpack into `into`, refusing any path that is not a plain relative path:
/// a pack from a hostile origin must not be able to write outside the
/// staging directory, whatever it claims its file names are.
pub fn unpack(pack: &Pack, into: &Path) -> Result<(), String> {
    if pack.schema != PACK_SCHEMA {
        return Err(format!("pack schema {} is not {}", pack.schema, PACK_SCHEMA));
    }
    std::fs::create_dir_all(into).map_err(|e| e.to_string())?;
    for (name, encoded) in &pack.files {
        let relative = Path::new(name);
        if relative.components().any(|c| !matches!(c, Component::Normal(_))) || name.is_empty() {
            return Err(format!("pack names a path it may not: {name:?}"));
        }
        let target = into.join(relative);
        if let Some(parent) = target.parent() {
            std::fs::create_dir_all(parent).map_err(|e| e.to_string())?;
        }
        let bytes = base64::engine::general_purpose::STANDARD
            .decode(encoded)
            .map_err(|e| format!("{name}: not base64: {e}"))?;
        std::fs::write(&target, bytes).map_err(|e| format!("{}: {e}", target.display()))?;
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn scratch(name: &str) -> std::path::PathBuf {
        let dir = std::env::temp_dir().join(format!("app-hub-pack-{name}-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&dir);
        std::fs::create_dir_all(dir.join("kit")).unwrap();
        std::fs::write(dir.join("manifest.json"), b"{}").unwrap();
        std::fs::write(dir.join("page.card"), b"card").unwrap();
        std::fs::write(dir.join("kit/kit.json"), b"{\"k\":1}").unwrap();
        dir
    }

    #[test]
    fn a_pack_round_trips_to_the_same_digest() {
        let dir = scratch("roundtrip");
        let before = octosense_app_policy::digest_dir(&dir).unwrap();
        let pack = pack_dir(&dir).unwrap();
        let out = dir.with_extension("unpacked");
        let _ = std::fs::remove_dir_all(&out);
        unpack(&pack, &out).unwrap();
        assert_eq!(before, octosense_app_policy::digest_dir(&out).unwrap());
        assert_eq!(std::fs::read(out.join("manifest.json")).unwrap(), b"{}");
    }

    #[test]
    fn a_pack_may_not_write_outside_its_staging_directory() {
        let mut pack = Pack { schema: PACK_SCHEMA, files: BTreeMap::new() };
        pack.files.insert("../escape.txt".into(), base64::engine::general_purpose::STANDARD.encode(b"x"));
        let out = std::env::temp_dir().join(format!("app-hub-pack-escape-{}", std::process::id()));
        let err = unpack(&pack, &out).unwrap_err();
        assert!(err.contains("may not"), "{err}");
        pack.files.clear();
        pack.files.insert("/abs.txt".into(), base64::engine::general_purpose::STANDARD.encode(b"x"));
        assert!(unpack(&pack, &out).is_err());
    }
}
