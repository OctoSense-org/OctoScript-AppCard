//! End-to-end tests over the plugin protocol: spawn the binary exactly as
//! octos does (`main <tool>` + JSON on stdin) against fixture data.

use std::io::Write;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};

use serde_json::{json, Value};

struct Rig {
    _dir: tempfile::TempDir,
    config: PathBuf,
}

fn fixtures() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("tests").join("fixtures")
}

fn rig() -> Rig {
    let dir = tempfile::tempdir().unwrap();
    let mail_dir = dir.path().join("mail");
    std::fs::create_dir_all(&mail_dir).unwrap();
    std::fs::copy(fixtures().join("mailbox-fixture.json"), mail_dir.join("mailbox-fixture.json")).unwrap();
    // The calendar fixture gets one extra event dated relative to today so
    // tests that depend on "recent" windows never rot.
    let mut state: Value =
        serde_json::from_slice(&std::fs::read(fixtures().join("calendar-state.json")).unwrap()).unwrap();
    let soon = (chrono::Utc::now() + chrono::Days::new(1)).format("%Y-%m-%d").to_string();
    state["state"]["events"]["sam-soon"] = json!({
        "id": "sam-soon", "calendar": "family", "created_by": "alex-phone", "updated_by": "alex-phone",
        "start": format!("{soon}T18:00:00+08:00"), "end": format!("{soon}T19:00:00+08:00"), "all_day": false,
        "title": {"en": "Walk with Sam", "cn": ""}, "location": {"en": "", "cn": ""}, "notes": "", "deleted": false
    });
    let state_path = dir.path().join("calendar-state.json");
    std::fs::write(&state_path, state.to_string()).unwrap();
    let config = dir.path().join("config.json");
    std::fs::write(
        &config,
        json!({
            "state_dir": dir.path().join("state"),
            "locale": "en",
            "mail": {"dirs": [mail_dir], "index_bodies": false},
            "calendar": {"state_file": state_path}
        })
        .to_string(),
    )
    .unwrap();
    Rig { _dir: dir, config }
}

fn call(rig: &Rig, tool: &str, input: Value) -> (bool, String) {
    let mut child = Command::new(env!("CARGO_BIN_EXE_main"))
        .arg(tool)
        .env("PERSONAL_DATA_CONFIG", &rig.config)
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .unwrap();
    child.stdin.take().unwrap().write_all(input.to_string().as_bytes()).unwrap();
    let out = child.wait_with_output().unwrap();
    let envelope: Value = serde_json::from_slice(&out.stdout)
        .unwrap_or_else(|e| panic!("stdout is not JSON ({e}): {}", String::from_utf8_lossy(&out.stdout)));
    (
        envelope["success"].as_bool().unwrap(),
        envelope["output"].as_str().unwrap().to_string(),
    )
}

#[test]
fn should_rank_subject_hits_and_hide_trash_when_searching_mail() {
    let rig = rig();
    let (ok, out) = call(&rig, "mail_search", json!({"query": "hike"}));
    assert!(ok, "{out}");
    assert!(out.contains("Weekend hike: West Hill trail"), "{out}");
    assert!(out.contains("id=fixture/m1"), "{out}");
    assert!(out.contains("flag:green"), "{out}");
    // The trashed dentist reminder is not in the inbox…
    let (_, out) = call(&rig, "mail_search", json!({"query": "appointment"}));
    assert!(!out.contains("id=fixture/m3"), "{out}");
    // …but folder=all finds it and labels it.
    let (_, out) = call(&rig, "mail_search", json!({"query": "appointment", "folder": "all"}));
    assert!(out.contains("id=fixture/m3") && out.contains("(trash)"), "{out}");
}

#[test]
fn should_list_latest_first_when_query_is_empty() {
    let rig = rig();
    let (ok, out) = call(&rig, "mail_search", json!({"limit": 2}));
    assert!(ok);
    let first = out.find("id=fixture/m1").unwrap();
    let second = out.find("id=fixture/m4").unwrap();
    assert!(first < second, "newest message first:\n{out}");
    assert!(!out.contains("id=fixture/m2"), "archived message is not in the inbox listing");
}

#[test]
fn should_filter_by_sender_and_date_when_searching_mail() {
    let rig = rig();
    let (_, out) = call(&rig, "mail_search", json!({"from": "sam", "since": "2026-09-15", "folder": "all"}));
    assert!(out.contains("id=fixture/m1") && !out.contains("id=fixture/m4"), "{out}");
    let (ok, out) = call(&rig, "mail_search", json!({"since": "not a date"}));
    assert!(!ok && out.contains("since"), "{out}");
}

#[test]
fn should_render_html_body_when_reading_mail() {
    let rig = rig();
    let (ok, out) = call(&rig, "mail_read", json!({"id": "m2"}));
    assert!(ok, "{out}");
    assert!(out.contains("Log in to view your statement."), "{out}");
    assert!(!out.contains("<b>") && !out.contains("x()"), "{out}");
    assert!(out.starts_with("Personal data"), "banner marks the content as untrusted:\n{out}");
    let (ok, out) = call(&rig, "mail_read", json!({"id": "nope"}));
    assert!(!ok && out.contains("No message"), "{out}");
}

#[test]
fn should_search_all_dates_when_calendar_query_has_words() {
    let rig = rig();
    let (ok, out) = call(&rig, "calendar_query", json!({"query": "dentist"}));
    assert!(ok, "{out}");
    assert!(out.contains("id=dentist") && out.contains("Sunrise Dental"), "{out}");
    assert!(!out.contains("id=gone"), "deleted events stay hidden:\n{out}");
    let (_, out) = call(&rig, "calendar_query", json!({"query": "dentist", "include_deleted": true}));
    assert!(out.contains("id=gone") && out.contains("deleted"), "{out}");
    let (_, out) = call(&rig, "calendar_query", json!({"query": "牙医"}));
    assert!(out.contains("id=dentist"), "CJK falls back to substring match:\n{out}");
}

#[test]
fn should_respect_explicit_range_and_calendar_when_listing_events() {
    let rig = rig();
    let (_, out) = call(&rig, "calendar_query", json!({"from": "2026-09-24", "to": "2026-09-24"}));
    assert!(out.contains("id=dentist") && out.contains("id=dinner"), "{out}");
    assert!(!out.contains("id=holiday") && !out.contains("id=old"), "{out}");
    let (_, out) = call(&rig, "calendar_query", json!({"from": "2026-09-24", "days": 10, "calendar": "family"}));
    assert!(out.contains("id=dinner") && !out.contains("id=dentist"), "{out}");
    let (_, out) = call(&rig, "calendar_query", json!({"from": "2026-10-01", "to": "2026-10-01"}));
    assert!(out.contains("all day · National Day"), "{out}");
    let (_, out) = call(&rig, "calendar_query", json!({"query": "dentist"}));
    assert!(out.contains("10:30–11:15 (UTC+08:00)"), "times carry the event's own offset:\n{out}");
}

#[test]
fn should_match_names_on_word_boundaries_when_looking_up_contacts() {
    let rig = rig();
    let (ok, out) = call(&rig, "contacts_lookup", json!({"name": "sam"}));
    assert!(ok, "{out}");
    assert!(out.contains("Sam Lee <sam.lee@example.org> · 2 message(s)"), "{out}");
    assert!(!out.contains("transamerica"), "substring inside a word must not match:\n{out}");
    assert!(out.contains("id=sam-soon"), "calendar events mentioning the name:\n{out}");
    assert!(out.contains("shared with sam"), "{out}");
}

#[test]
fn should_refresh_index_when_mailbox_changes() {
    let rig = rig();
    let (_, out) = call(&rig, "mail_search", json!({"query": "brand new subject"}));
    assert!(out.contains("0 of 0"), "{out}");
    let path = rig._dir.path().join("mail").join("mailbox-fixture.json");
    let mut doc: Value = serde_json::from_slice(&std::fs::read(&path).unwrap()).unwrap();
    doc["messages"].as_array_mut().unwrap().push(json!({
        "id": "m5", "uid": "u5", "date": "2026-09-16T10:00:00+00:00", "sender": "New Person",
        "address": "new@example.net", "subject": "brand new subject", "preview": "hello", "body": "hello", "html": ""
    }));
    std::fs::write(&path, doc.to_string()).unwrap();
    let (_, out) = call(&rig, "mail_search", json!({"query": "brand new subject"}));
    assert!(out.contains("id=fixture/m5"), "{out}");
    let (_, out) = call(&rig, "personal_data_status", json!({}));
    assert!(out.contains("rows: 5 mail, 6 events, 3 calendars"), "{out}");
}

#[test]
fn should_keep_messages_apart_when_two_accounts_share_an_id() {
    let rig = rig();
    let other = json!({
        "account_id": "other", "address": "pat@example.net", "available": 1, "has_more": false,
        "host": "pop.example.net", "synced_at": "2026-09-16T08:00:00+00:00",
        "messages": [{
            "id": "m1", "uid": "u1", "date": "2026-09-15T12:00:00+00:00", "sender": "Pat Quinn",
            "address": "pat@example.net", "subject": "Weekend hike moved to Sunday", "preview": "Rain on Saturday.",
            "body": "Rain on Saturday, let's do Sunday.", "html": "", "unread": true, "flagged": false,
            "archived": false, "trashed": false, "attachments": 0, "attachment_items": [], "inline_images": {}, "source": "fixture"
        }]
    });
    std::fs::write(rig._dir.path().join("mail").join("mailbox-other.json"), other.to_string()).unwrap();
    let (_, out) = call(&rig, "mail_search", json!({"query": "hike"}));
    assert!(out.contains("id=fixture/m1") && out.contains("id=other/m1"), "both accounts' messages listed:\n{out}");
    let (ok, out) = call(&rig, "mail_read", json!({"id": "other/m1"}));
    assert!(ok && out.contains("moved to Sunday") && out.contains("pat@example.net"), "{out}");
    let (ok, out) = call(&rig, "mail_read", json!({"id": "fixture/m1"}));
    assert!(ok && out.contains("West Hill trail"), "{out}");
    // Removing the second mailbox drops its rows on the next call.
    std::fs::remove_file(rig._dir.path().join("mail").join("mailbox-other.json")).unwrap();
    let (_, out) = call(&rig, "mail_search", json!({"query": "hike"}));
    assert!(!out.contains("id=other/m1"), "stale account removed:\n{out}");
}

#[test]
fn should_rebuild_when_body_indexing_is_switched_on() {
    let rig = rig();
    let (_, out) = call(&rig, "mail_search", json!({"query": "alex"}));
    assert!(out.contains("0 of 0"), "bodies are not indexed by default:\n{out}");
    let cfg_path = rig.config.clone();
    let mut cfg: Value = serde_json::from_slice(&std::fs::read(&cfg_path).unwrap()).unwrap();
    cfg["mail"]["index_bodies"] = json!(true);
    std::fs::write(&cfg_path, cfg.to_string()).unwrap();
    let (_, out) = call(&rig, "mail_search", json!({"query": "alex"}));
    assert!(out.contains("id=fixture/m1"), "flipping index_bodies re-indexes without a mailbox change:\n{out}");
}

#[test]
fn should_report_unknown_tool_with_failure_envelope() {
    let rig = rig();
    let (ok, out) = call(&rig, "bogus", json!({}));
    assert!(!ok && out.contains("Unknown tool"), "{out}");
}
