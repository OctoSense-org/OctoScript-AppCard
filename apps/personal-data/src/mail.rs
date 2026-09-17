//! Reading the Mail module's private `mailbox-*.json` files.
//!
//! The mailbox file is the record of truth; the index only keeps headers and
//! the preview line unless bodies are opted in. Credentials live in the
//! sibling `account.json`, which this skill never opens.

use std::path::{Path, PathBuf};

use serde_json::Value;

use crate::text::{clip, collapse, html_to_text};

#[derive(Debug, Clone)]
pub struct Mailbox {
    pub account: String,
    pub address: String,
    pub synced_at: String,
    pub messages: Vec<Message>,
}

#[derive(Debug, Clone, Default)]
pub struct Message {
    pub id: String,
    pub uid: String,
    pub date: String,
    pub sender: String,
    pub address: String,
    pub subject: String,
    pub preview: String,
    pub unread: bool,
    pub flagged: bool,
    pub flag: String,
    pub archived: bool,
    pub trashed: bool,
    pub attachments: i64,
    body: String,
    html: String,
}

impl Message {
    /// Readable body: the plain part when present, else the HTML reduced to text.
    pub fn text(&self) -> String {
        let plain = collapse(&self.body);
        if plain.chars().count() >= 40 || self.html.trim().is_empty() {
            plain
        } else {
            html_to_text(&self.html)
        }
    }

    pub fn folder(&self) -> &'static str {
        if self.trashed {
            "trash"
        } else if self.archived {
            "archive"
        } else {
            "inbox"
        }
    }
}

/// Every `mailbox-*.json` under the configured directories.
pub fn mailbox_files(dirs: &[PathBuf]) -> Vec<PathBuf> {
    let mut files = Vec::new();
    for dir in dirs {
        let Ok(entries) = std::fs::read_dir(dir) else { continue };
        for entry in entries.flatten() {
            let path = entry.path();
            let name = entry.file_name().to_string_lossy().to_string();
            if name.starts_with("mailbox-") && name.ends_with(".json") {
                files.push(path);
            }
        }
    }
    files.sort();
    files
}

/// Cheap change detector: modification time + size.
pub fn fingerprint(path: &Path) -> Option<String> {
    let meta = std::fs::metadata(path).ok()?;
    let modified = meta
        .modified()
        .ok()?
        .duration_since(std::time::UNIX_EPOCH)
        .ok()?;
    Some(format!("{}:{}", modified.as_nanos(), meta.len()))
}

pub fn load(path: &Path) -> Result<Mailbox, String> {
    let raw = std::fs::read(path).map_err(|e| format!("read {}: {e}", path.display()))?;
    let value: Value = serde_json::from_slice(&raw).map_err(|e| format!("parse {}: {e}", path.display()))?;
    let account = value
        .get("account_id")
        .and_then(Value::as_str)
        .map(str::to_string)
        .unwrap_or_else(|| {
            path.file_stem()
                .map(|s| s.to_string_lossy().trim_start_matches("mailbox-").to_string())
                .unwrap_or_default()
        });
    let messages = value
        .get("messages")
        .and_then(Value::as_array)
        .map(|list| list.iter().map(message).collect())
        .unwrap_or_default();
    Ok(Mailbox {
        account,
        address: string(&value, "address"),
        synced_at: string(&value, "synced_at"),
        messages,
    })
}

fn message(v: &Value) -> Message {
    Message {
        id: string(v, "id"),
        uid: string(v, "uid"),
        date: string(v, "date"),
        sender: string(v, "sender"),
        address: string(v, "address"),
        subject: string(v, "subject"),
        preview: clip(&collapse(&string(v, "preview")), 200),
        unread: flag(v, "unread"),
        flagged: flag(v, "flagged"),
        flag: string(v, "flag"),
        archived: flag(v, "archived"),
        trashed: flag(v, "trashed"),
        attachments: v.get("attachments").and_then(Value::as_i64).unwrap_or(0),
        body: string(v, "body"),
        html: string(v, "html"),
    }
}

fn string(v: &Value, key: &str) -> String {
    v.get(key).and_then(Value::as_str).unwrap_or("").to_string()
}

fn flag(v: &Value, key: &str) -> bool {
    v.get(key).and_then(Value::as_bool).unwrap_or(false)
}

/// Epoch seconds for an RFC 3339 date, or for a plain `YYYY-MM-DD`.
pub fn epoch(date: &str) -> i64 {
    if let Ok(dt) = chrono::DateTime::parse_from_rfc3339(date) {
        return dt.timestamp();
    }
    if let Ok(d) = chrono::NaiveDate::parse_from_str(date, "%Y-%m-%d") {
        return d.and_hms_opt(0, 0, 0).map(|t| t.and_utc().timestamp()).unwrap_or(0);
    }
    0
}
