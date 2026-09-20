//! What exactly gets hashed.
//!
//! A bundle is a directory, so "the bundle bytes" needs a definition both the
//! signer and the host compute the same way, on any filesystem, in any order.
//! This is that definition: every file under the root except the manifest
//! itself, sorted by its path, each contributing its path, its length and its
//! bytes. Directory order, timestamps, permissions and the manifest's own
//! contents do not affect it.
//!
//! The manifest is excluded because it carries the digest; a symlink is
//! refused rather than followed, because what it points at is not in the
//! bundle and would not be signed.
use std::path::{Path, PathBuf};

/// The file inside a bundle that carries its manifest.
pub const MANIFEST_FILE: &str = "manifest.json";

/// Hex blake3 over the bundle's files, in the canonical order.
pub fn digest_dir(root: &Path) -> Result<String, String> {
    let mut files = Vec::new();
    collect(root, root, &mut files)?;
    files.sort();
    let mut hasher = blake3::Hasher::new();
    for relative in &files {
        let bytes = std::fs::read(root.join(relative)).map_err(|e| format!("{}: {e}", relative.display()))?;
        // Path, then length, then content: without the length a file ending
        // where the next path begins could be shuffled without changing the
        // digest.
        hasher.update(relative.to_string_lossy().as_bytes());
        hasher.update(&[0]);
        hasher.update(&(bytes.len() as u64).to_le_bytes());
        hasher.update(&bytes);
    }
    Ok(hasher.finalize().to_hex().to_string())
}

fn collect(root: &Path, dir: &Path, out: &mut Vec<PathBuf>) -> Result<(), String> {
    let entries = std::fs::read_dir(dir).map_err(|e| format!("{}: {e}", dir.display()))?;
    for entry in entries {
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
        let relative = path.strip_prefix(root).map_err(|e| e.to_string())?.to_path_buf();
        if relative == Path::new(MANIFEST_FILE) {
            continue;
        }
        out.push(relative);
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    fn scratch(name: &str) -> PathBuf {
        let dir = std::env::temp_dir().join(format!("app-policy-bundle-{name}-{}", std::process::id()));
        let _ = fs::remove_dir_all(&dir);
        fs::create_dir_all(dir.join("kit")).unwrap();
        fs::write(dir.join("page.card"), b"card source").unwrap();
        fs::write(dir.join("kit/kit.json"), b"{}").unwrap();
        dir
    }

    #[test]
    fn the_manifest_itself_is_not_part_of_the_digest() {
        let dir = scratch("manifest-excluded");
        let before = digest_dir(&dir).unwrap();
        fs::write(dir.join(MANIFEST_FILE), b"{\"schema\":1}").unwrap();
        assert_eq!(before, digest_dir(&dir).unwrap());
    }

    #[test]
    fn changing_any_content_changes_the_digest() {
        let dir = scratch("content");
        let before = digest_dir(&dir).unwrap();
        fs::write(dir.join("kit/kit.json"), b"{ }").unwrap();
        assert_ne!(before, digest_dir(&dir).unwrap());
    }

    #[test]
    fn moving_content_between_files_changes_the_digest() {
        let dir = scratch("shuffle");
        fs::write(dir.join("a.txt"), b"onetwo").unwrap();
        fs::write(dir.join("b.txt"), b"").unwrap();
        let before = digest_dir(&dir).unwrap();
        fs::write(dir.join("a.txt"), b"one").unwrap();
        fs::write(dir.join("b.txt"), b"two").unwrap();
        assert_ne!(before, digest_dir(&dir).unwrap());
    }

    #[test]
    fn a_symlink_is_refused_rather_than_followed() {
        let dir = scratch("symlink");
        #[cfg(unix)]
        std::os::unix::fs::symlink("/etc/hosts", dir.join("link")).unwrap();
        #[cfg(unix)]
        assert!(digest_dir(&dir).unwrap_err().contains("symlink"));
    }
}
