//! Host-owned durable approvals. Existing approvals are never silently repinned.

use splash_ui_l0::approval::ArtifactApproval;
use std::{fs, io::{ErrorKind, Write}, path::Path};

/// Explicit host deployment action. The renderer never invokes this path.
/// Old receipts remain available for rollback/audit; normal `require` must
/// admit each card again against the current source, policy and runtime.
pub fn archive_for_reapproval(directory: &Path, migration: &str) -> Result<(), String> {
    if migration.is_empty() || !migration.bytes().all(|b| b.is_ascii_digit()) {
        return Err("invalid card reapproval migration ID".into());
    }
    let backup = directory.with_file_name(format!("l0-approvals-before-studio-{migration}"));
    if backup.try_exists().map_err(|e| e.to_string())? {
        return Err("card reapproval migration already exists".into());
    }
    if directory.try_exists().map_err(|e| e.to_string())? {
        fs::rename(directory, backup).map_err(|e| format!("archive old card receipts: {e}"))?;
    }
    Ok(())
}

pub fn require(directory: &Path, source: &str, runtime: &str, kit: &str) -> Result<ArtifactApproval, String> {
    let candidate = ArtifactApproval::admit(source, runtime, kit)?;
    fs::create_dir_all(directory).map_err(|e| format!("create card approval directory: {e}"))?;
    // Serialize publication across app instances. HarmonyOS app storage rejects
    // hard links; an atomic rename under this lock preserves complete records
    // and ensures a competing runtime verifies the winner instead of repinning.
    let publication_lock = fs::OpenOptions::new().read(true).write(true).create(true)
        .truncate(false).open(directory.join(".publication-lock"))
        .map_err(|e| format!("open card approval lock: {e}"))?;
    publication_lock.lock().map_err(|e| format!("lock card approval: {e}"))?;
    let path = directory.join(format!("{}.json", ArtifactApproval::source_key(source)));
    let read = || -> Result<ArtifactApproval, String> {
        let raw = fs::read(&path).map_err(|e| format!("read card approval: {e}"))?;
        let json = serde_json::from_slice(&raw).map_err(|e| format!("parse card approval: {e}"))?;
        let approval = ArtifactApproval::from_json(&json)?;
        approval.verify(source, runtime, kit)?;
        Ok(approval)
    };
    match fs::metadata(&path) {
        Ok(_) => return read(),
        Err(e) if e.kind() == ErrorKind::NotFound => {},
        Err(e) => return Err(format!("inspect card approval: {e}")),
    }
    // Stage and sync the entire record before publishing it. The lock remains
    // held until after this function returns, including verification above.
    static NEXT: std::sync::atomic::AtomicU64 = std::sync::atomic::AtomicU64::new(0);
    let serial = NEXT.fetch_add(1, std::sync::atomic::Ordering::Relaxed);
    let temporary = directory.join(format!(".approval-{}-{serial}", std::process::id()));
    let result = (|| {
        let mut file = fs::OpenOptions::new().write(true).create_new(true).open(&temporary)
            .map_err(|e| format!("stage card approval: {e}"))?;
        file.write_all(candidate.to_json().to_string().as_bytes()).and_then(|_| file.sync_all())
            .map_err(|e| format!("save card approval: {e}"))?;
        fs::rename(&temporary, &path).map_err(|e| format!("publish card approval: {e}"))?;
        Ok(candidate)
    })();
    let _ = fs::remove_file(temporary);
    result
}

#[cfg(test)]
mod tests {
use super::*;
#[test]
fn generation_render_explicit_reapproval_preserves_old_runtime_receipts() {
    let root = std::env::temp_dir().join(format!("splash-reapproval-{}", std::process::id()));
    fs::create_dir(&root).unwrap();
    let directory = root.join("l0-approvals");
    let source = "view root Surface { Rule() }";
    let old = require(&directory, source, "runtime-a", "kit").unwrap();
    assert!(require(&directory, source, "runtime-b", "kit").is_err());
    assert!(archive_for_reapproval(&directory, "../escape").is_err());
    archive_for_reapproval(&directory, "1").unwrap();
    let new = require(&directory, source, "runtime-b", "kit").unwrap();
    assert_ne!(old, new);
    let backup = root.join("l0-approvals-before-studio-1");
    assert_eq!(require(&backup, source, "runtime-a", "kit").unwrap(), old);
    assert!(archive_for_reapproval(&directory, "1").is_err());
    assert_eq!(require(&directory, source, "runtime-b", "kit").unwrap(), new);
    fs::remove_dir_all(root).unwrap();
}
#[test]
fn concurrent_approval_writers_keep_one_runtime_pin() {
    let directory = std::env::temp_dir().join(format!("splash-approvals-concurrent-{}", std::process::id()));
    std::fs::create_dir(&directory).unwrap();
    let barrier = std::sync::Arc::new(std::sync::Barrier::new(8));
    let source = "view root Surface { Rule() }";
    let results = std::thread::scope(|scope| {
        let jobs: Vec<_> = (0..8).map(|i| {
            let barrier = barrier.clone();
            let directory = &directory;
            scope.spawn(move || {
                let runtime = if i % 2 == 0 { "runtime-a" } else { "runtime-b" };
                barrier.wait();
                (runtime, require(directory, source, runtime, "kit").is_ok())
            })
        }).collect();
        jobs.into_iter().map(|job| job.join().unwrap()).collect::<Vec<_>>()
    });
    let winner = results.iter().find(|(_, success)| *success).unwrap().0;
    assert!(results.iter().all(|(runtime, success)| *success == (*runtime == winner)));
    assert!(require(&directory, source, winner, "kit").is_ok());
    std::fs::remove_dir_all(directory).unwrap();
}
#[test]
fn durable_approvals_survive_restart_and_fail_closed_on_change_or_corruption() {
    let directory = std::env::temp_dir().join(format!("splash-approvals-{}", std::process::id()));
    std::fs::create_dir(&directory).unwrap();
    let source = "view root Surface { Rule() }";
    let a = require(&directory, source, "runtime-a", "kit-a").unwrap();
    assert_eq!(require(&directory, source, "runtime-a", "kit-a").unwrap(), a);
    assert!(require(&directory, source, "runtime-b", "kit-a").is_err());
    let path = directory.join(format!("{}.json", ArtifactApproval::source_key(source)));
    std::fs::write(&path, "broken").unwrap();
    assert!(require(&directory, source, "runtime-a", "kit-a").is_err());
    assert_eq!(std::fs::read_to_string(path).unwrap(), "broken");
    std::fs::remove_dir_all(directory).unwrap();
}

}
