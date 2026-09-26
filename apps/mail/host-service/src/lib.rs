//! The `mail` host service: mail for contained apps, credentials kept by the
//! host.
//!
//! A script app granted `mail` calls, through `host.request`:
//!
//! | method | args | answer |
//! |---|---|---|
//! | `mail.accounts` | – | `[{id, address}]` this app may use |
//! | `mail.add_account` | – | `{id, address}` once the person signs in on the host's sheet |
//! | `mail.remove_account` | `{account}` | `{}`; the account is deleted when no app uses it |
//! | `mail.folders` | `{account}` | `[{id, name, role}]`, the inbox first (`role`: inbox, sent, drafts, junk, trash, archive, all, flagged or "") |
//! | `mail.sync` | `{account, folder?}` | `{new, total}` after fetching new mail |
//! | `mail.list` | `{account, folder?, offset?, limit?}` | `{folder, total, messages: [{id, sender, address, subject, preview, time, unread}]}` |
//! | `mail.message` | `{account, folder?, message}` | `{id, sender, address, subject, body, html, attachments, date, time}` |
//! | `mail.mark_read` | `{account, folder?, message}` | `{}` |
//! | `mail.send` | `{account, to, subject, body}` | `{accepted}` |
//!
//! The app never sees a password or a socket. `mail.add_account` raises the
//! host's sign-in sheet, a separate isolate over the app; only calls from
//! that sheet (`mail.signin.submit`, `mail.signin.cancel`) can carry a
//! password, and the service tests the account before it keeps it. Each
//! account is granted to the apps that added it, and an app can reach only
//! those.
//!
//! `folder` defaults to the inbox. Accounts read over IMAP (folders, and the
//! read flag goes back to the server) or POP3 (the inbox only); both send
//! over SMTP. `html` is the message rebuilt from the few tags the app's
//! `Html` view draws, with nothing remote in it; `body` is its text.
//!
//! State lives under the host's own directory (`<host_dir>/mail`), outside
//! every app's jail: `accounts.json` (no passwords) and `box-<id>…json` (the
//! fetched mail). Passwords go to the platform's secret store ([`vault`]).
use octosense_appstore::services::{close_sheet_later, HostService, Replier, ServiceCall, ServiceHost};
use serde_json::{json, Value};
use std::collections::HashSet;
use std::path::{Path, PathBuf};
use std::sync::{Arc, Mutex};

pub mod vault;
mod html;
mod imap;

use vault::Vault;

#[path = "../../native/src/network.rs"]
#[allow(dead_code)]
mod network;

pub const INBOX: &str = "INBOX";

/// How mail moves: IMAP or POP3 and SMTP in the shell, or a fake in tests.
pub trait Transport: Send + Sync {
    /// Sign in and out again: the account works.
    fn test(&self, account: &Value) -> Result<(), String>;
    fn folders(&self, account: &Value) -> Result<Vec<Value>, String>;
    /// Mail in `folder` that `state` has not seen, newest first: `{messages,
    /// state, reset}`. `state` is what the last fetch returned (or `{}`);
    /// `reset` says the folder must be fetched afresh.
    fn fetch(&self, account: &Value, folder: &str, state: &Value) -> Result<Value, String>;
    /// Tell the server a message was read, where it keeps that.
    fn mark_seen(&self, account: &Value, folder: &str, message: &Value) -> Result<(), String>;
    fn send(&self, account: &Value, draft: &Value) -> Result<Value, String>;
}

fn is_imap(account: &Value) -> bool {
    text(account, "protocol") == "imap"
}

fn inbox_only() -> Vec<Value> {
    vec![json!({"id": INBOX, "name": "Inbox", "role": "inbox"})]
}

/// IMAP or POP3 for reading, SMTP for sending: the native Mail app's code
/// and the service's IMAP client.
pub struct Network;

impl Transport for Network {
    fn test(&self, account: &Value) -> Result<(), String> {
        if is_imap(account) {
            imap::Imap::connect(account)?.logout();
            Ok(())
        } else {
            network::test(account).map(|_| ())
        }
    }
    fn folders(&self, account: &Value) -> Result<Vec<Value>, String> {
        if !is_imap(account) {
            return Ok(inbox_only());
        }
        let mut imap = imap::Imap::connect(account)?;
        let folders = imap.folders();
        imap.logout();
        folders
    }
    fn fetch(&self, account: &Value, folder: &str, state: &Value) -> Result<Value, String> {
        if is_imap(account) {
            let mut imap = imap::Imap::connect(account)?;
            let fetched = imap.fetch(folder, state, 25);
            imap.logout();
            return fetched;
        }
        if folder != INBOX {
            return Err("This account reads the inbox only.".into());
        }
        let mut seen: Vec<Value> = state["seen"].as_array().cloned().unwrap_or_default();
        let known: HashSet<String> = seen.iter().filter_map(|v| v.as_str().map(str::to_string)).collect();
        let fetched = network::fetch(account, &known)?;
        let messages = fetched["messages"].as_array().cloned().unwrap_or_default();
        seen.extend(messages.iter().map(|m| m["uid"].clone()));
        seen.extend(fetched["skipped_uids"].as_array().cloned().unwrap_or_default());
        Ok(json!({"messages": messages, "state": {"seen": seen}, "reset": false}))
    }
    fn mark_seen(&self, account: &Value, folder: &str, message: &Value) -> Result<(), String> {
        let Some(uid) = message["imap_uid"].as_u64().filter(|_| is_imap(account)) else { return Ok(()) };
        let mut imap = imap::Imap::connect(account)?;
        let marked = imap.mark_seen(folder, uid);
        imap.logout();
        marked
    }
    fn send(&self, account: &Value, draft: &Value) -> Result<Value, String> {
        network::send(account, draft)
    }
}

/// Offer the service to the Card runner, over the network, with passwords in
/// the platform's secret store.
pub fn register() {
    register_with(Arc::new(Network));
}

/// Offer the service over a demo mailbox: any address, the password `demo`,
/// a few sample messages in two folders, and sends that go nowhere. For
/// developing and showing the Mail app without a real account. The demo
/// password is no secret, so it stays in a file rather than the keychain.
pub fn register_demo() {
    register_with_vault(Arc::new(DemoTransport::default()), Arc::new(vault::FileVault));
}

#[derive(Default)]
pub struct DemoTransport {
    sent: Mutex<usize>,
}

const DEMO_WELCOME: &str = r#"<html><head><style>.x{color:red}</style></head><body><table><tr><td>
<h1>Welcome to <b>Mail</b></h1>
<p>Mail runs as a contained app. It reads and sends through OctoSense, and never sees your password.</p>
<ul><li>Accounts over <b>IMAP</b> show every folder.</li><li>Passwords live in the device's secret store.</li></ul>
<p>Read more at <a href="https://octosense.dev/mail">octosense.dev/mail</a>.<img src="https://tracker.example/p.gif"></p>
</td></tr></table></body></html>"#;

impl Transport for DemoTransport {
    fn test(&self, account: &Value) -> Result<(), String> {
        if text(account, "password") == "demo" { Ok(()) } else { Err("The demo mailbox's password is \"demo\".".into()) }
    }
    fn folders(&self, account: &Value) -> Result<Vec<Value>, String> {
        self.test(account)?;
        let mut folders = inbox_only();
        folders.push(json!({"id": "Sent", "name": "Sent", "role": "sent"}));
        Ok(folders)
    }
    fn fetch(&self, account: &Value, folder: &str, state: &Value) -> Result<Value, String> {
        self.test(account)?;
        let samples: &[(&str, &str, &str, &str, &str, &str)] = if folder == INBOX {
            &[
                ("demo-1", "Rose Chen", "rose@example.com", "Dinner on Saturday?", "We are thinking of trying the new place on Market Street around seven. Are you in?", ""),
                ("demo-2", "OctoSense", "hello@octosense.dev", "Welcome to Mail", "", DEMO_WELCOME),
                ("demo-3", "Noah Park", "noah@example.com", "Photos from the hike", "I put the good ones in the shared album. The view from the ridge came out great.", ""),
            ]
        } else {
            &[("demo-sent-1", "Me", "me@example.com", "Re: Photos from the hike", "They look great, thanks!", "")]
        };
        let mut seen: Vec<Value> = state["seen"].as_array().cloned().unwrap_or_default();
        let messages: Vec<Value> = samples
            .iter()
            .filter(|(uid, ..)| !seen.iter().any(|s| s == uid))
            .map(|(uid, sender, address, subject, body, html)| {
                json!({"id": &network::hash(uid)[..24], "uid": uid, "sender": sender, "address": address, "subject": subject,
                    "body": if body.is_empty() { "(No readable message body)" } else { body }, "preview": body, "html": html,
                    "time": "Sep 25", "date": "2026-09-25T09:00:00Z", "unread": folder == INBOX})
            })
            .collect();
        seen.extend(messages.iter().map(|m| m["uid"].clone()));
        Ok(json!({"messages": messages, "state": {"seen": seen}, "reset": false}))
    }
    fn mark_seen(&self, _account: &Value, _folder: &str, _message: &Value) -> Result<(), String> {
        Ok(())
    }
    fn send(&self, account: &Value, _draft: &Value) -> Result<Value, String> {
        self.test(account)?;
        *self.sent.lock().unwrap() += 1;
        Ok(json!({"accepted": true}))
    }
}

pub fn register_with(transport: Arc<dyn Transport>) {
    register_with_vault(transport, vault::platform());
}

pub fn register_with_vault(transport: Arc<dyn Transport>, vault: Arc<dyn Vault>) {
    octosense_appstore::services::register_host_service(Box::new(MailService { transport, vault, pending: Arc::default() }));
}

pub struct MailService {
    transport: Arc<dyn Transport>,
    vault: Arc<dyn Vault>,
    /// The app waiting on a sign-in, and where its answer goes. Shared with
    /// the worker that tests an account: it answers on success, and leaves
    /// the app waiting on a failure, so the person can fix the form.
    pending: Arc<Mutex<Option<(String, Replier)>>>,
}

const ACCOUNT_FIELDS: [&str; 10] = ["address", "username", "protocol", "host", "port", "security", "smtp_host", "smtp_port", "smtp_security", "id"];

fn text<'a>(v: &'a Value, key: &str) -> &'a str {
    v[key].as_str().unwrap_or("")
}

struct Store {
    dir: PathBuf,
    vault: Arc<dyn Vault>,
}

impl Store {
    fn at(host_dir: &Path, vault: Arc<dyn Vault>) -> Self {
        Store { dir: host_dir.join("mail"), vault }
    }

    fn accounts(&self) -> Vec<Value> {
        std::fs::read(self.dir.join("accounts.json"))
            .ok()
            .and_then(|b| serde_json::from_slice::<Vec<Value>>(&b).ok())
            .unwrap_or_default()
    }

    fn save_accounts(&self, accounts: &[Value]) -> Result<(), String> {
        write_atomic(&self.dir.join("accounts.json"), &serde_json::to_vec_pretty(accounts).unwrap())
    }

    /// An account this app was granted, with its password, ready for the
    /// transport; or why not.
    fn account_for(&self, app_id: &str, id: &str) -> Result<Value, String> {
        let account = self.granted(app_id, id)?;
        let mut full = account.clone();
        full["password"] = json!(self.vault.get(&self.dir, id)?);
        Ok(full)
    }

    /// The account, without its password, if this app was granted it.
    fn granted(&self, app_id: &str, id: &str) -> Result<Value, String> {
        let account = self
            .accounts()
            .into_iter()
            .find(|a| text(a, "id") == id)
            .ok_or("There is no such account.")?;
        let granted = account["apps"].as_array().is_some_and(|apps| apps.iter().any(|a| a == app_id));
        if !granted {
            return Err("This app may not use that account.".into());
        }
        Ok(account)
    }

    /// The inbox keeps the name older builds gave it.
    fn mailbox_path(&self, id: &str, folder: &str) -> PathBuf {
        if folder == INBOX {
            self.dir.join(format!("box-{id}.json"))
        } else {
            self.dir.join(format!("box-{id}-{}.json", &network::hash(folder)[..12]))
        }
    }

    fn mailbox(&self, id: &str, folder: &str) -> Value {
        let mut mailbox = std::fs::read(self.mailbox_path(id, folder))
            .ok()
            .and_then(|b| serde_json::from_slice::<Value>(&b).ok())
            .unwrap_or_else(|| json!({"messages": []}));
        if mailbox.get("state").is_none() {
            // Older builds kept POP3's seen list at the top.
            mailbox["state"] = json!({"seen": mailbox.get("seen").cloned().unwrap_or(json!([]))});
        }
        mailbox
    }

    fn save_mailbox(&self, id: &str, folder: &str, mailbox: &Value) -> Result<(), String> {
        write_atomic(&self.mailbox_path(id, folder), &serde_json::to_vec(mailbox).unwrap())
    }

    fn folders(&self, id: &str) -> Option<Value> {
        std::fs::read(self.dir.join(format!("folders-{id}.json"))).ok().and_then(|b| serde_json::from_slice(&b).ok())
    }

    fn forget(&self, id: &str) {
        self.vault.remove(&self.dir, id);
        if let Ok(entries) = std::fs::read_dir(&self.dir) {
            for entry in entries.flatten() {
                let name = entry.file_name().to_string_lossy().to_string();
                if name == format!("box-{id}.json") || name.starts_with(&format!("box-{id}-")) || name == format!("folders-{id}.json") {
                    let _ = std::fs::remove_file(entry.path());
                }
            }
        }
    }
}

fn write_atomic(path: &Path, bytes: &[u8]) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|e| format!("Cannot store mail: {e}"))?;
    }
    let temp = path.with_extension("tmp");
    std::fs::write(&temp, bytes).map_err(|e| format!("Cannot store mail: {e}"))?;
    std::fs::rename(&temp, path).map_err(|e| format!("Cannot store mail: {e}"))
}

/// A fetched message as it is kept: its HTML rebuilt from safe tags, its
/// text from that when the mail had no text part, and no attachment bytes
/// or inline images (nothing the app is shown needs them).
fn normalize(mut message: Value) -> Value {
    let source = text(&message, "html").to_string();
    if !source.trim().is_empty() {
        let rebuilt = html::rebuild(&source);
        let body = text(&message, "body").to_string();
        // The decoder falls back to every text node, style sheets included,
        // when a mail has no text part; the rebuilt text reads better.
        let fallback = scraper::Html::parse_fragment(&source).root_element().text().collect::<Vec<_>>().join(" ");
        if (body == fallback || body == "(No readable message body)" || body.trim().is_empty()) && !rebuilt.text.is_empty() {
            message["preview"] = json!(rebuilt.text.split_whitespace().collect::<Vec<_>>().join(" ").chars().take(180).collect::<String>());
            message["body"] = json!(rebuilt.text);
        }
        message["html"] = json!(rebuilt.html);
    }
    if let Some(items) = message.get("attachment_items").and_then(Value::as_array).cloned() {
        let listed: Vec<Value> = items.iter().map(|a| json!({"filename": a["filename"], "mime": a["mime"], "size": a["size"]})).collect();
        message["attachment_items"] = json!(listed);
    }
    if let Some(object) = message.as_object_mut() {
        object.remove("inline_images");
    }
    message
}

/// What an app sees of a message in a list.
fn header(message: &Value) -> Value {
    json!({
        "id": message["id"], "sender": message["sender"], "address": message["address"],
        "subject": message["subject"], "preview": message["preview"], "time": message["time"],
        "unread": message["unread"].as_bool().unwrap_or(true),
    })
}

/// The account a sign-in form describes, or why it cannot be one.
fn account_from_form(form: &Value) -> Result<Value, String> {
    let mut account = network::defaults();
    let imap = text(form, "protocol") != "pop3";
    account["protocol"] = json!(if imap { "imap" } else { "pop3" });
    if imap {
        account["host"] = json!("imap.gmail.com");
        account["port"] = json!("993");
    }
    for key in ["address", "username", "password", "host", "port", "security", "smtp_host", "smtp_port", "smtp_security"] {
        if let Some(value) = form[key].as_str().filter(|v| !v.trim().is_empty()) {
            // A password is taken as typed: spaces can be part of it.
            account[key] = json!(if key == "password" { value } else { value.trim() });
        } else if let Some(value) = form[key].as_f64() {
            account[key] = json!(value.to_string());
        }
    }
    if text(&account, "username").is_empty() {
        account["username"] = account["address"].clone();
    }
    network::validate(&account)?;
    Ok(account)
}

/// A worker thread for slow work, so the UI thread never waits on a server.
fn work(f: impl FnOnce() + Send + 'static) {
    std::thread::spawn(f);
}

impl HostService for MailService {
    fn family(&self) -> &'static str {
        "mail"
    }

    fn call(&mut self, call: ServiceCall, reply: Replier, host: &mut dyn ServiceHost) {
        let store = Store::at(&call.host_dir, self.vault.clone());
        let account_arg = text(&call.args, "account").to_string();
        let folder = Some(text(&call.args, "folder")).filter(|f| !f.is_empty()).unwrap_or(INBOX).to_string();
        match call.method() {
            "accounts" => {
                let mine: Vec<Value> = store
                    .accounts()
                    .into_iter()
                    .filter(|a| a["apps"].as_array().is_some_and(|apps| apps.iter().any(|x| x == call.app_id.as_str())))
                    .map(|a| json!({"id": a["id"], "address": a["address"]}))
                    .collect();
                reply.send(Ok(json!(mine)));
            }
            "add_account" => {
                if let Some((_, earlier)) = self.pending.lock().unwrap().take() {
                    earlier.send(Err("Another sign-in replaced this one.".into()));
                }
                *self.pending.lock().unwrap() = Some((call.app_id.clone(), reply));
                host.open_sheet(signin_sheet());
            }
            "signin.cancel" if call.from_sheet => {
                host.close_sheet();
                if let Some((_, pending)) = self.pending.lock().unwrap().take() {
                    pending.send(Err("Sign-in cancelled.".into()));
                }
                reply.send(Ok(json!({})));
            }
            "signin.submit" if call.from_sheet => {
                let Some(app_id) = self.pending.lock().unwrap().as_ref().map(|(app, _)| app.clone()) else {
                    host.close_sheet();
                    reply.send(Err("No app is waiting for this sign-in.".into()));
                    return;
                };
                let account = match account_from_form(&call.args) {
                    Ok(account) => account,
                    Err(e) => return reply.send(Err(e)),
                };
                let (transport, pending) = (self.transport.clone(), self.pending.clone());
                work(move || {
                    if let Err(e) = transport.test(&account) {
                        return reply.send(Err(e));
                    }
                    let id = network::identity(&account);
                    let mut accounts = store.accounts();
                    let mut kept = json!({"apps": [app_id], "id": id});
                    for key in ACCOUNT_FIELDS.iter().filter(|k| **k != "id") {
                        kept[*key] = account[*key].clone();
                    }
                    match accounts.iter_mut().find(|a| text(a, "id") == id) {
                        Some(existing) => {
                            // Signing in again updates the settings and
                            // grants the account to this app too.
                            let mut apps = existing["apps"].as_array().cloned().unwrap_or_default();
                            if !apps.iter().any(|a| a == app_id.as_str()) {
                                apps.push(json!(app_id));
                            }
                            kept["apps"] = json!(apps);
                            *existing = kept;
                        }
                        None => accounts.push(kept),
                    }
                    let saved = store.vault.put(&store.dir, &id, text(&account, "password")).and_then(|_| store.save_accounts(&accounts));
                    if let Err(e) = saved {
                        return reply.send(Err(e));
                    }
                    close_sheet_later(&app_id);
                    if let Some((_, waiting)) = pending.lock().unwrap().take() {
                        waiting.send(Ok(json!({"id": id, "address": account["address"]})));
                    }
                    reply.send(Ok(json!({})));
                });
            }
            "signin.submit" | "signin.cancel" => reply.send(Err("Only the sign-in sheet may do that.".into())),
            "remove_account" => {
                let mut accounts = store.accounts();
                if let Some(account) = accounts.iter_mut().find(|a| text(a, "id") == account_arg) {
                    if let Some(apps) = account["apps"].as_array_mut() {
                        apps.retain(|a| a != call.app_id.as_str());
                    }
                }
                let orphaned: Vec<String> = accounts
                    .iter()
                    .filter(|a| a["apps"].as_array().is_none_or(|apps| apps.is_empty()))
                    .map(|a| text(a, "id").to_string())
                    .collect();
                accounts.retain(|a| !orphaned.iter().any(|id| id == text(a, "id")));
                for id in &orphaned {
                    store.forget(id);
                }
                reply.send(store.save_accounts(&accounts).map(|_| json!({})));
            }
            "folders" => {
                let account = match store.account_for(&call.app_id, &account_arg) {
                    Ok(account) => account,
                    Err(e) => return reply.send(Err(e)),
                };
                let transport = self.transport.clone();
                work(move || {
                    let answer = match transport.folders(&account) {
                        Ok(folders) => {
                            let folders = json!(folders);
                            let _ = write_atomic(&store.dir.join(format!("folders-{account_arg}.json")), folders.to_string().as_bytes());
                            Ok(folders)
                        }
                        // Offline: the folders the last listing found.
                        Err(e) => store.folders(&account_arg).ok_or(e),
                    };
                    reply.send(answer);
                });
            }
            "sync" => {
                let account = match store.account_for(&call.app_id, &account_arg) {
                    Ok(account) => account,
                    Err(e) => return reply.send(Err(e)),
                };
                let transport = self.transport.clone();
                work(move || {
                    let mut mailbox = store.mailbox(&account_arg, &folder);
                    let result = transport.fetch(&account, &folder, &mailbox["state"]).and_then(|fetched| {
                        let new: Vec<Value> = fetched["messages"].as_array().cloned().unwrap_or_default();
                        let mut messages: Vec<Value> =
                            if fetched["reset"] == true { Vec::new() } else { mailbox["messages"].as_array().cloned().unwrap_or_default() };
                        for message in new.iter().rev() {
                            messages.insert(0, normalize(message.clone()));
                        }
                        let total = messages.len();
                        mailbox["messages"] = json!(messages);
                        mailbox["state"] = fetched["state"].clone();
                        if let Some(object) = mailbox.as_object_mut() {
                            object.remove("seen");
                        }
                        store.save_mailbox(&account_arg, &folder, &mailbox)?;
                        Ok(json!({"new": new.len(), "total": total}))
                    });
                    reply.send(result);
                });
            }
            "list" => {
                if let Err(e) = store.granted(&call.app_id, &account_arg) {
                    return reply.send(Err(e));
                }
                let mailbox = store.mailbox(&account_arg, &folder);
                let messages = mailbox["messages"].as_array().cloned().unwrap_or_default();
                let offset = call.args["offset"].as_f64().unwrap_or(0.0).max(0.0) as usize;
                let limit = call.args["limit"].as_f64().unwrap_or(50.0).clamp(1.0, 200.0) as usize;
                let page: Vec<Value> = messages.iter().skip(offset).take(limit).map(header).collect();
                reply.send(Ok(json!({"folder": folder, "total": messages.len(), "messages": page})));
            }
            "message" | "mark_read" => {
                if let Err(e) = store.granted(&call.app_id, &account_arg) {
                    return reply.send(Err(e));
                }
                let wanted = text(&call.args, "message").to_string();
                let mut mailbox = store.mailbox(&account_arg, &folder);
                let Some(message) = mailbox["messages"]
                    .as_array_mut()
                    .and_then(|m| m.iter_mut().find(|m| text(m, "id") == wanted))
                else {
                    return reply.send(Err("There is no such message.".into()));
                };
                let was_unread = message["unread"].as_bool().unwrap_or(true);
                message["unread"] = json!(false);
                let answer = if call.method() == "message" {
                    let attachments: Vec<Value> = message["attachment_items"]
                        .as_array()
                        .map(|items| items.iter().map(|a| json!({"filename": a["filename"], "size": a["size"]})).collect())
                        .unwrap_or_default();
                    json!({
                        "id": message["id"], "sender": message["sender"], "address": message["address"],
                        "subject": message["subject"], "body": message["body"], "html": text(message, "html"),
                        "attachments": attachments, "date": message["date"], "time": message["time"],
                    })
                } else {
                    json!({})
                };
                let seen = message.clone();
                let _ = store.save_mailbox(&account_arg, &folder, &mailbox);
                reply.send(Ok(answer));
                // The server hears too, where it keeps a read flag; failing
                // that is not worth an error: the next sync is unaffected.
                if was_unread {
                    if let Ok(account) = store.account_for(&call.app_id, &account_arg) {
                        let transport = self.transport.clone();
                        work(move || {
                            let _ = transport.mark_seen(&account, &folder, &seen);
                        });
                    }
                }
            }
            "send" => {
                let account = match store.account_for(&call.app_id, &account_arg) {
                    Ok(account) => account,
                    Err(e) => return reply.send(Err(e)),
                };
                let now = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_nanos()).unwrap_or(0);
                let domain = text(&account, "address").split('@').nth(1).unwrap_or("octosense.local").to_string();
                let draft = json!({
                    "to": text(&call.args, "to"), "subject": text(&call.args, "subject"), "body": text(&call.args, "body"),
                    "message_id": format!("<{now:x}@{domain}>"),
                });
                let transport = self.transport.clone();
                work(move || reply.send(transport.send(&account, &draft)));
            }
            other => reply.send(Err(format!("mail has no method {other:?}"))),
        }
    }
}

/// The host's sign-in sheet: a Splash program run in its own isolate, over
/// the app. What is typed here reaches the service, never the app.
fn signin_sheet() -> String {
    r##"let protocol = "imap"
fn choose(p){
    protocol = p
    ui.imap_on.set_visible(p == "imap")
    ui.imap_off.set_visible(p != "imap")
    ui.pop_on.set_visible(p == "pop3")
    ui.pop_off.set_visible(p != "pop3")
    // Swap Gmail's servers for each other; anything typed stays.
    let h = ui.pop_host.text()
    if p == "imap" {
        ui.incoming.set_text("Incoming (IMAP, TLS)")
        if h == "pop.gmail.com" || h == "" { ui.pop_host.set_text("imap.gmail.com") ui.pop_port.set_text("993") }
    } else {
        ui.incoming.set_text("Incoming (POP3, TLS)")
        if h == "imap.gmail.com" || h == "" { ui.pop_host.set_text("pop.gmail.com") ui.pop_port.set_text("995") }
    }
}
fn submit(){
    ui.status.set_text("Checking the account…")
    host.request("mail.signin.submit", {
        address: ui.address.text() username: ui.username.text() password: ui.password.text() protocol: protocol
        host: ui.pop_host.text() port: ui.pop_port.text() security: "tls"
        smtp_host: ui.smtp_host.text() smtp_port: ui.smtp_port.text() smtp_security: "tls"
    }, fn(r){ if r.is_ok { ui.status.set_text("Signed in") } else { ui.status.set_text(r.error) } })
}
fn cancel(){ host.request("mail.signin.cancel", {}, fn(r){}) }
let Field = TextInput{width: Fill height: 40
    draw_bg +: {color: #xf2f2f7 color_hover: #xf2f2f7 color_focus: #xf2f2f7 color_empty: #xf2f2f7
        border_color: #x00000000 border_color_hover: #x00000000 border_color_focus: #x007aff border_color_empty: #x00000000 border_radius: 10.0}
    draw_text +: {color: #x1c1c1e color_hover: #x1c1c1e color_focus: #x1c1c1e color_empty: #x8e8e93 color_empty_hover: #x8e8e93}
}
let Caption = Label{text: "" draw_text.color: #x8e8e93 draw_text.text_style.font_size: 11}
let Choice = ButtonFlat{height: 32 width: Fill
    draw_bg +: {border_radius: 8.0 color: #x00000000 color_hover: #x0000000a color_down: #x00000014 border_size: 0.0}
    draw_text +: {color: #x3a3a3c color_hover: #x3a3a3c color_down: #x3a3a3c text_style +: {font_size: 13}}}
let Chosen = ButtonFlat{height: 32 width: Fill
    draw_bg +: {border_radius: 8.0 color: #xffffff color_hover: #xffffff color_down: #xffffff border_size: 0.0}
    draw_text +: {color: #x1c1c1e color_hover: #x1c1c1e color_down: #x1c1c1e text_style +: {font_size: 13}}}
SolidView{width: Fill height: Fill flow: Down draw_bg.color: #x000000aa new_batch: true
    // Scrolls: on a small or dense screen, or with the keyboard up, the
    // form is taller than the window. The actions sit at the top so they
    // are never scrolled out of reach.
    ScrollYView{width: Fill height: Fill flow: Down padding: Inset{left: 12 right: 12 top: 24 bottom: 24}
    RoundedView{width: Fill height: Fit flow: Down spacing: 8 padding: 16 new_batch: true show_bg: true draw_bg.color: #xffffff draw_bg.border_radius: 18.0
        View{width: Fill height: Fit flow: Right spacing: 8 align: Align{y: 0.5}
            ButtonFlat{text: "Cancel" height: 40 on_click: || cancel()
                draw_bg +: {color: #x00000000 color_hover: #x0000000a color_down: #x00000014 border_size: 0.0}
                draw_text +: {color: #x007aff color_hover: #x007aff color_down: #x007aff text_style +: {font_size: 15}}}
            View{width: Fill height: 1}
            ButtonFlat{text: "Sign in" height: 40 padding: Inset{left: 20 right: 20} on_click: || submit()
                draw_bg +: {border_radius: 20.0 color: #x007aff color_hover: #x0a84ff color_down: #x0062cc border_size: 0.0}
                draw_text +: {color: #xffffff color_hover: #xffffff color_down: #xffffff text_style +: {font_size: 15}}}
        }
        Label{width: Fill text: "OctoSense · Add a mail account" draw_text.color: #x1c1c1e draw_text.text_style: theme.font_bold{font_size: 17}}
        Label{width: Fill text: "Your password stays with OctoSense. The app that asked only gets your mail." draw_text.color: #x3a3a3c draw_text.text_style.font_size: 12}
        status := Label{width: Fill text: "" draw_text.color: #xff3b30 draw_text.text_style.font_size: 12}
        Caption{text: "Email address"}
        address := Field{empty_text: "you@example.com"}
        Caption{text: "Login (if not the address)"}
        username := Field{empty_text: "optional"}
        Caption{text: "Password or app password"}
        password := Field{empty_text: "password" is_password: true}
        RoundedView{width: Fill height: Fit flow: Right padding: 2 show_bg: true draw_bg.color: #xe5e5ea draw_bg.border_radius: 10.0
            imap_on := Chosen{text: "IMAP: all folders"}
            imap_off := Choice{visible: false text: "IMAP: all folders" on_click: || choose("imap")}
            pop_on := Chosen{visible: false text: "POP3: inbox only"}
            pop_off := Choice{text: "POP3: inbox only" on_click: || choose("pop3")}
        }
        View{width: Fill height: Fit flow: Right spacing: 8
            View{width: Fill height: Fit flow: Down spacing: 4 incoming := Caption{text: "Incoming (IMAP, TLS)"} pop_host := Field{text: "imap.gmail.com"}}
            View{width: 80 height: Fit flow: Down spacing: 4 Caption{text: "Port"} pop_port := Field{text: "993"}}
        }
        View{width: Fill height: Fit flow: Right spacing: 8
            View{width: Fill height: Fit flow: Down spacing: 4 Caption{text: "Outgoing (SMTP, TLS)"} smtp_host := Field{text: "smtp.gmail.com"}}
            View{width: 80 height: Fit flow: Down spacing: 4 Caption{text: "Port"} smtp_port := Field{text: "465"}}
        }
    }
    }
}
"##
    .to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::sync::Mutex;

    /// A mailbox in memory: `test` checks the password, `fetch` hands out
    /// what the seen set does not hold, `send` records the draft.
    struct Fake {
        password: String,
        inbox: Vec<Value>,
        sent: Mutex<Vec<Value>>,
        marked: Mutex<Vec<String>>,
    }
    impl Transport for Fake {
        fn test(&self, account: &Value) -> Result<(), String> {
            if text(account, "password") == self.password { Ok(()) } else { Err("Wrong password.".into()) }
        }
        fn folders(&self, account: &Value) -> Result<Vec<Value>, String> {
            self.test(account)?;
            Ok(vec![json!({"id": INBOX, "name": "Inbox", "role": "inbox"}), json!({"id": "Archive", "name": "Archive", "role": "archive"})])
        }
        fn fetch(&self, account: &Value, folder: &str, state: &Value) -> Result<Value, String> {
            self.test(account)?;
            let last = state["last"].as_u64().unwrap_or(0) as usize;
            let inbox: Vec<Value> = if folder == INBOX { self.inbox.clone() } else { vec![message("a1", "Archived")] };
            let new: Vec<Value> = inbox.iter().skip(last).cloned().collect();
            Ok(json!({"messages": new, "state": {"last": inbox.len()}, "reset": false}))
        }
        fn mark_seen(&self, _account: &Value, folder: &str, message: &Value) -> Result<(), String> {
            self.marked.lock().unwrap().push(format!("{folder}/{}", text(message, "uid")));
            Ok(())
        }
        fn send(&self, account: &Value, draft: &Value) -> Result<Value, String> {
            self.test(account)?;
            self.sent.lock().unwrap().push(draft.clone());
            Ok(json!({"accepted": true}))
        }
    }

    #[derive(Default)]
    struct Host {
        sheet: Option<Option<String>>,
    }
    impl ServiceHost for Host {
        fn open_sheet(&mut self, body: String) {
            self.sheet = Some(Some(body));
        }
        fn close_sheet(&mut self) {
            self.sheet = Some(None);
        }
    }

    fn message(uid: &str, subject: &str) -> Value {
        json!({"id": &network::hash(uid)[..24], "uid": uid, "sender": "Alex", "address": "alex@example.com", "subject": subject,
            "preview": "hello", "body": "hello there", "time": "Sep 25", "date": "2026-09-25T00:00:00Z", "unread": true})
    }

    static NEXT: std::sync::atomic::AtomicUsize = std::sync::atomic::AtomicUsize::new(9_100);

    /// Send one request through the real dispatch path; each gets an
    /// isolate of its own, so answers cannot cross.
    fn send(dir: &Path, app: &str, service: &str, args: Value, from_sheet: bool, host: &mut Host) -> usize {
        let heap = NEXT.fetch_add(1, std::sync::atomic::Ordering::Relaxed);
        let call = ServiceCall { app_id: app.into(), service: service.into(), args, from_sheet, host_dir: dir.into() };
        octosense_appstore::services::dispatch(call, heap, 1, host);
        heap
    }

    fn wait(heap: usize) -> Result<Value, String> {
        for _ in 0..500 {
            if let Some((_, _, result)) = octosense_appstore::services::take_replies_for(&[heap]).pop() {
                return result.map(|s| serde_json::from_str(&s).unwrap());
            }
            std::thread::sleep(std::time::Duration::from_millis(5));
        }
        panic!("no answer on {heap}");
    }

    fn ask(dir: &Path, app: &str, service: &str, args: Value, from_sheet: bool, host: &mut Host) -> Result<Value, String> {
        let heap = send(dir, app, service, args, from_sheet, host);
        wait(heap)
    }

    #[test]
    fn an_app_signs_in_on_the_hosts_sheet_and_reads_and_sends_without_the_password() {
        let dir = std::env::temp_dir().join(format!("mail-service-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&dir);
        let mut html_mail = message("u2", "Second");
        html_mail["body"] = json!("(No readable message body)");
        html_mail["html"] = json!("<style>p{}</style><div><h1>Big news</h1><p>Read <a href='https://x.example'>this</a>.</p><img src='https://t.example/p'></div>");
        let fake = Arc::new(Fake { password: "s3cret".into(), inbox: vec![message("u1", "First"), html_mail], sent: Mutex::default(), marked: Mutex::default() });
        register_with_vault(fake.clone(), Arc::new(vault::FileVault));
        let mut host = Host::default();

        // The app cannot hand the service a password itself.
        assert!(ask(&dir, "os.mail", "mail.signin.submit", json!({"address": "me@example.com", "password": "s3cret"}), false, &mut host)
            .unwrap_err()
            .contains("Only the sign-in sheet"));

        // add_account raises the sheet and waits; a wrong password keeps it waiting.
        let add = send(&dir, "os.mail", "mail.add_account", Value::Null, false, &mut host);
        assert!(matches!(host.sheet, Some(Some(_))), "the host's sheet is up");
        let form = json!({"address": "me@example.com", "password": "wrong", "host": "pop.example.com", "port": "995", "security": "tls",
            "smtp_host": "smtp.example.com", "smtp_port": "465", "smtp_security": "tls"});
        assert!(ask(&dir, "os.mail", "mail.signin.submit", form.clone(), true, &mut host).unwrap_err().contains("Wrong password"));
        assert!(octosense_appstore::services::take_replies_for(&[add]).is_empty(), "the app is still waiting");
        let mut good = form;
        good["password"] = json!("s3cret");
        ask(&dir, "os.mail", "mail.signin.submit", good, true, &mut host).unwrap();
        let added = wait(add).unwrap();
        let id = text(&added, "id").to_string();
        assert_eq!(added["address"], "me@example.com");
        assert!(!std::fs::read_to_string(dir.join("mail/accounts.json")).unwrap().contains("s3cret"), "no password in the account list");

        // Another app cannot reach the account.
        assert!(ask(&dir, "os.other", "mail.list", json!({"account": id}), false, &mut host).unwrap_err().contains("may not use"));
        assert_eq!(ask(&dir, "os.other", "mail.accounts", Value::Null, false, &mut host).unwrap(), json!([]));
        assert_eq!(ask(&dir, "os.mail", "mail.accounts", Value::Null, false, &mut host).unwrap()[0]["id"], id.as_str());

        let synced = ask(&dir, "os.mail", "mail.sync", json!({"account": id}), false, &mut host).unwrap();
        assert_eq!(synced["new"], 2);
        let again = ask(&dir, "os.mail", "mail.sync", json!({"account": id}), false, &mut host).unwrap();
        assert_eq!(again["new"], 0, "seen mail is not fetched twice");
        let list = ask(&dir, "os.mail", "mail.list", json!({"account": id}), false, &mut host).unwrap();
        assert_eq!(list["total"], 2);
        assert!(list["messages"][0].get("body").is_none(), "a list carries headers, not bodies");
        let first = text(&list["messages"][0], "id").to_string();
        let read = ask(&dir, "os.mail", "mail.message", json!({"account": id, "message": first}), false, &mut host).unwrap();
        assert_eq!(read["body"], "hello there");
        let list = ask(&dir, "os.mail", "mail.list", json!({"account": id}), false, &mut host).unwrap();
        assert_eq!(list["messages"][0]["unread"], false);

        let html_id = text(&list["messages"][1], "id").to_string();
        assert_eq!(list["messages"][1]["preview"], "Big news Read this.", "a preview is the mail's text, not its style sheet");
        let read = ask(&dir, "os.mail", "mail.message", json!({"account": id, "message": html_id}), false, &mut host).unwrap();
        assert_eq!(read["html"], "<h2>Big news</h2><p>Read <a href=\"https://x.example\">this</a>.</p>");
        assert_eq!(read["body"], "Big news\n\nRead this.");
        for _ in 0..200 {
            if fake.marked.lock().unwrap().len() == 2 {
                break;
            }
            std::thread::sleep(std::time::Duration::from_millis(5));
        }
        let mut marked = fake.marked.lock().unwrap().clone();
        marked.sort();
        assert_eq!(marked, ["INBOX/u1", "INBOX/u2"], "the server hears a message was read, once");
        ask(&dir, "os.mail", "mail.message", json!({"account": id, "message": html_id}), false, &mut host).unwrap();
        assert_eq!(fake.marked.lock().unwrap().len(), 2);

        // Folders: listed, then each synced and listed on its own.
        let folders = ask(&dir, "os.mail", "mail.folders", json!({"account": id}), false, &mut host).unwrap();
        assert_eq!(folders[1]["id"], "Archive");
        assert_eq!(ask(&dir, "os.mail", "mail.sync", json!({"account": id, "folder": "Archive"}), false, &mut host).unwrap()["new"], 1);
        let archive = ask(&dir, "os.mail", "mail.list", json!({"account": id, "folder": "Archive"}), false, &mut host).unwrap();
        assert_eq!(archive["messages"][0]["subject"], "Archived");
        assert_eq!(ask(&dir, "os.mail", "mail.list", json!({"account": id}), false, &mut host).unwrap()["total"], 2, "folders keep their own mail");

        ask(&dir, "os.mail", "mail.send", json!({"account": id, "to": "alex@example.com", "subject": "Hi", "body": "Hello"}), false, &mut host).unwrap();
        assert_eq!(fake.sent.lock().unwrap()[0]["to"], "alex@example.com");

        ask(&dir, "os.mail", "mail.remove_account", json!({"account": id}), false, &mut host).unwrap();
        assert!(!dir.join("mail/secrets").join(&id).exists(), "the last app out takes the password with it");
        assert!(std::fs::read_dir(dir.join("mail")).unwrap().flatten().all(|e| !e.file_name().to_string_lossy().starts_with("box-")), "and its mail");
    }
}
