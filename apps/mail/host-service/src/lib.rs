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
//! | `mail.sync` | `{account}` | `{new, total}` after fetching new mail |
//! | `mail.list` | `{account, offset?, limit?}` | `{total, messages: [{id, sender, address, subject, preview, time, unread}]}` |
//! | `mail.message` | `{account, message}` | `{id, sender, address, subject, body, date, time}` |
//! | `mail.mark_read` | `{account, message}` | `{}` |
//! | `mail.send` | `{account, to, subject, body}` | `{accepted}` |
//!
//! The app never sees a password or a socket. `mail.add_account` raises the
//! host's sign-in sheet, a separate isolate over the app; only calls from
//! that sheet (`mail.signin.submit`, `mail.signin.cancel`) can carry a
//! password, and the service tests the account before it keeps it. Each
//! account is granted to the apps that added it, and an app can reach only
//! those.
//!
//! State lives under the host's own directory (`<host_dir>/mail`), outside
//! every app's jail: `accounts.json` (no passwords), `secrets/<id>` (the
//! password, owner-only), and `box-<id>.json` (the fetched mail).
use octosense_appstore::services::{close_sheet_later, HostService, Replier, ServiceCall, ServiceHost};
use serde_json::{json, Value};
use std::collections::HashSet;
use std::path::{Path, PathBuf};
use std::sync::{Arc, Mutex};

#[path = "../../native/src/network.rs"]
#[allow(dead_code)]
mod network;

/// How mail moves: POP3 and SMTP in the shell, or a fake in tests.
pub trait Transport: Send + Sync {
    fn test(&self, account: &Value) -> Result<Value, String>;
    fn fetch(&self, account: &Value, seen: &HashSet<String>) -> Result<Value, String>;
    fn send(&self, account: &Value, draft: &Value) -> Result<Value, String>;
}

/// POP3 over TLS for reading, SMTP for sending: the native Mail app's code.
pub struct Pop3Smtp;

impl Transport for Pop3Smtp {
    fn test(&self, account: &Value) -> Result<Value, String> {
        network::test(account)
    }
    fn fetch(&self, account: &Value, seen: &HashSet<String>) -> Result<Value, String> {
        network::fetch(account, seen)
    }
    fn send(&self, account: &Value, draft: &Value) -> Result<Value, String> {
        network::send(account, draft)
    }
}

/// Offer the service to the Card runner, over POP3 and SMTP.
pub fn register() {
    register_with(Arc::new(Pop3Smtp));
}

/// Offer the service over a demo mailbox: any address, the password `demo`,
/// a few sample messages, and sends that go nowhere. For developing and
/// showing the Mail app without a real account.
pub fn register_demo() {
    register_with(Arc::new(DemoTransport::default()));
}

#[derive(Default)]
pub struct DemoTransport {
    sent: Mutex<usize>,
}

impl Transport for DemoTransport {
    fn test(&self, account: &Value) -> Result<Value, String> {
        if text(account, "password") == "demo" { Ok(json!({})) } else { Err("The demo mailbox's password is \"demo\".".into()) }
    }
    fn fetch(&self, account: &Value, seen: &HashSet<String>) -> Result<Value, String> {
        self.test(account)?;
        let samples = [
            ("demo-1", "Rose Chen", "rose@example.com", "Dinner on Saturday?", "We are thinking of trying the new place on Market Street around seven. Are you in?"),
            ("demo-2", "OctoSense", "hello@octosense.dev", "Welcome to Mail", "Mail runs as a contained app: it reads and sends through the host, and never sees your password."),
            ("demo-3", "Noah Park", "noah@example.com", "Photos from the hike", "I put the good ones in the shared album. The view from the ridge came out great."),
        ];
        let messages: Vec<Value> = samples
            .iter()
            .filter(|(uid, ..)| !seen.contains(*uid))
            .map(|(uid, sender, address, subject, body)| {
                json!({"id": &network::hash(uid)[..24], "uid": uid, "sender": sender, "address": address, "subject": subject,
                    "body": body, "preview": body, "time": "Sep 25", "date": "2026-09-25T09:00:00Z", "unread": true})
            })
            .collect();
        Ok(json!({"messages": messages, "skipped_uids": []}))
    }
    fn send(&self, account: &Value, _draft: &Value) -> Result<Value, String> {
        self.test(account)?;
        *self.sent.lock().unwrap() += 1;
        Ok(json!({"accepted": true}))
    }
}

pub fn register_with(transport: Arc<dyn Transport>) {
    octosense_appstore::services::register_host_service(Box::new(MailService { transport, pending: Arc::default() }));
}

pub struct MailService {
    transport: Arc<dyn Transport>,
    /// The app waiting on a sign-in, and where its answer goes. Shared with
    /// the worker that tests an account: it answers on success, and leaves
    /// the app waiting on a failure, so the person can fix the form.
    pending: Arc<Mutex<Option<(String, Replier)>>>,
}

const ACCOUNT_FIELDS: [&str; 9] = ["address", "username", "host", "port", "security", "smtp_host", "smtp_port", "smtp_security", "id"];

fn text<'a>(v: &'a Value, key: &str) -> &'a str {
    v[key].as_str().unwrap_or("")
}

struct Store {
    dir: PathBuf,
}

impl Store {
    fn at(host_dir: &Path) -> Self {
        Store { dir: host_dir.join("mail") }
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
        let account = self
            .accounts()
            .into_iter()
            .find(|a| text(a, "id") == id)
            .ok_or("There is no such account.")?;
        let granted = account["apps"].as_array().is_some_and(|apps| apps.iter().any(|a| a == app_id));
        if !granted {
            return Err("This app may not use that account.".into());
        }
        let mut full = account.clone();
        full["password"] = json!(self.secret(id)?);
        Ok(full)
    }

    fn secret(&self, id: &str) -> Result<String, String> {
        std::fs::read_to_string(self.dir.join("secrets").join(id)).map_err(|_| "The account's password is missing; sign in again.".to_string())
    }

    fn save_secret(&self, id: &str, password: &str) -> Result<(), String> {
        let path = self.dir.join("secrets").join(id);
        write_atomic(&path, password.as_bytes())?;
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            let _ = std::fs::set_permissions(&path, std::fs::Permissions::from_mode(0o600));
        }
        Ok(())
    }

    fn mailbox(&self, id: &str) -> Value {
        std::fs::read(self.dir.join(format!("box-{id}.json")))
            .ok()
            .and_then(|b| serde_json::from_slice(&b).ok())
            .unwrap_or_else(|| json!({"messages": [], "seen": []}))
    }

    fn save_mailbox(&self, id: &str, mailbox: &Value) -> Result<(), String> {
        write_atomic(&self.dir.join(format!("box-{id}.json")), &serde_json::to_vec(mailbox).unwrap())
    }

    fn forget(&self, id: &str) {
        let _ = std::fs::remove_file(self.dir.join("secrets").join(id));
        let _ = std::fs::remove_file(self.dir.join(format!("box-{id}.json")));
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

impl HostService for MailService {
    fn family(&self) -> &'static str {
        "mail"
    }

    fn call(&mut self, call: ServiceCall, reply: Replier, host: &mut dyn ServiceHost) {
        let store = Store::at(&call.host_dir);
        let account_arg = text(&call.args, "account").to_string();
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
                std::thread::spawn(move || {
                    if let Err(e) = transport.test(&account) {
                        return reply.send(Err(e));
                    }
                    let id = network::identity(&account);
                    let mut accounts = store.accounts();
                    match accounts.iter_mut().find(|a| text(a, "id") == id) {
                        Some(existing) => {
                            let apps = existing["apps"].as_array_mut().unwrap();
                            if !apps.iter().any(|a| a == app_id.as_str()) {
                                apps.push(json!(app_id));
                            }
                        }
                        None => {
                            let mut kept = json!({"apps": [app_id], "id": id});
                            for key in ACCOUNT_FIELDS.iter().filter(|k| **k != "id") {
                                kept[*key] = account[*key].clone();
                            }
                            accounts.push(kept);
                        }
                    }
                    let saved = store.save_secret(&id, text(&account, "password")).and_then(|_| store.save_accounts(&accounts));
                    if let Err(e) = saved {
                        return reply.send(Err(e));
                    }
                    close_sheet_later();
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
            "sync" => {
                let account = match store.account_for(&call.app_id, &account_arg) {
                    Ok(account) => account,
                    Err(e) => return reply.send(Err(e)),
                };
                let transport = self.transport.clone();
                std::thread::spawn(move || {
                    let mut mailbox = store.mailbox(&account_arg);
                    let seen: HashSet<String> = mailbox["seen"]
                        .as_array()
                        .map(|a| a.iter().filter_map(|v| v.as_str().map(str::to_string)).collect())
                        .unwrap_or_default();
                    let result = transport.fetch(&account, &seen).and_then(|fetched| {
                        let new: Vec<Value> = fetched["messages"].as_array().cloned().unwrap_or_default();
                        let mut messages: Vec<Value> = mailbox["messages"].as_array().cloned().unwrap_or_default();
                        let mut seen: Vec<Value> = mailbox["seen"].as_array().cloned().unwrap_or_default();
                        for message in new.iter().rev() {
                            seen.push(message["uid"].clone());
                            messages.insert(0, message.clone());
                        }
                        for uid in fetched["skipped_uids"].as_array().cloned().unwrap_or_default() {
                            seen.push(uid);
                        }
                        let total = messages.len();
                        mailbox["messages"] = json!(messages);
                        mailbox["seen"] = json!(seen);
                        store.save_mailbox(&account_arg, &mailbox)?;
                        Ok(json!({"new": new.len(), "total": total}))
                    });
                    reply.send(result);
                });
            }
            "list" => {
                if let Err(e) = store.account_for(&call.app_id, &account_arg) {
                    return reply.send(Err(e));
                }
                let mailbox = store.mailbox(&account_arg);
                let messages = mailbox["messages"].as_array().cloned().unwrap_or_default();
                let offset = call.args["offset"].as_f64().unwrap_or(0.0).max(0.0) as usize;
                let limit = call.args["limit"].as_f64().unwrap_or(50.0).clamp(1.0, 200.0) as usize;
                let page: Vec<Value> = messages.iter().skip(offset).take(limit).map(header).collect();
                reply.send(Ok(json!({"total": messages.len(), "messages": page})));
            }
            "message" | "mark_read" => {
                if let Err(e) = store.account_for(&call.app_id, &account_arg) {
                    return reply.send(Err(e));
                }
                let wanted = text(&call.args, "message").to_string();
                let mut mailbox = store.mailbox(&account_arg);
                let Some(message) = mailbox["messages"]
                    .as_array_mut()
                    .and_then(|m| m.iter_mut().find(|m| text(m, "id") == wanted))
                else {
                    return reply.send(Err("There is no such message.".into()));
                };
                message["unread"] = json!(false);
                let answer = if call.method() == "message" {
                    json!({
                        "id": message["id"], "sender": message["sender"], "address": message["address"],
                        "subject": message["subject"], "body": message["body"], "date": message["date"], "time": message["time"],
                    })
                } else {
                    json!({})
                };
                let _ = store.save_mailbox(&account_arg, &mailbox);
                reply.send(Ok(answer));
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
                std::thread::spawn(move || reply.send(transport.send(&account, &draft)));
            }
            other => reply.send(Err(format!("mail has no method {other:?}"))),
        }
    }
}

/// The host's sign-in sheet: a Splash program run in its own isolate, over
/// the app. What is typed here reaches the service, never the app.
fn signin_sheet() -> String {
    r##"fn submit(){
    ui.status.set_text("Checking the account…")
    host.request("mail.signin.submit", {
        address: ui.address.text() username: ui.username.text() password: ui.password.text()
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
SolidView{width: Fill height: Fill flow: Down align: Align{x: 0.5 y: 0.5} draw_bg.color: #x000000aa new_batch: true padding: 16
    RoundedView{width: Fill height: Fit flow: Down spacing: 8 padding: 18 new_batch: true show_bg: true draw_bg.color: #xffffff draw_bg.border_radius: 18.0
        Label{text: "OctoSense · Add a mail account" draw_text.color: #x1c1c1e draw_text.text_style: theme.font_bold{font_size: 17}}
        Label{width: Fill text: "Your password stays with OctoSense. The app that asked only gets your mail." draw_text.color: #x3a3a3c draw_text.text_style.font_size: 12}
        Caption{text: "Email address"}
        address := Field{empty_text: "you@example.com"}
        Caption{text: "Login (if not the address)"}
        username := Field{empty_text: "optional"}
        Caption{text: "Password or app password"}
        password := Field{empty_text: "password" is_password: true}
        View{width: Fill height: Fit flow: Right spacing: 8
            View{width: Fill height: Fit flow: Down spacing: 4 Caption{text: "Incoming (POP3, TLS)"} pop_host := Field{text: "pop.gmail.com"}}
            View{width: 80 height: Fit flow: Down spacing: 4 Caption{text: "Port"} pop_port := Field{text: "995"}}
        }
        View{width: Fill height: Fit flow: Right spacing: 8
            View{width: Fill height: Fit flow: Down spacing: 4 Caption{text: "Outgoing (SMTP, TLS)"} smtp_host := Field{text: "smtp.gmail.com"}}
            View{width: 80 height: Fit flow: Down spacing: 4 Caption{text: "Port"} smtp_port := Field{text: "465"}}
        }
        status := Label{width: Fill text: "" draw_text.color: #xff3b30 draw_text.text_style.font_size: 12}
        View{width: Fill height: Fit flow: Right spacing: 8 align: Align{y: 0.5}
            ButtonFlat{text: "Cancel" height: 40 on_click: || cancel()
                draw_bg +: {color: #x00000000 color_hover: #x0000000a color_down: #x00000014 border_size: 0.0}
                draw_text +: {color: #x007aff color_hover: #x007aff color_down: #x007aff text_style +: {font_size: 15}}}
            View{width: Fill height: 1}
            ButtonFlat{text: "Sign in" height: 40 padding: Inset{left: 20 right: 20} on_click: || submit()
                draw_bg +: {border_radius: 20.0 color: #x007aff color_hover: #x0a84ff color_down: #x0062cc border_size: 0.0}
                draw_text +: {color: #xffffff color_hover: #xffffff color_down: #xffffff text_style +: {font_size: 15}}}
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
    }
    impl Transport for Fake {
        fn test(&self, account: &Value) -> Result<Value, String> {
            if text(account, "password") == self.password { Ok(json!({})) } else { Err("Wrong password.".into()) }
        }
        fn fetch(&self, account: &Value, seen: &HashSet<String>) -> Result<Value, String> {
            self.test(account)?;
            Ok(json!({"messages": self.inbox.iter().filter(|m| !seen.contains(text(m, "uid"))).cloned().collect::<Vec<_>>(), "skipped_uids": []}))
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
        let fake = Arc::new(Fake { password: "s3cret".into(), inbox: vec![message("u1", "First"), message("u2", "Second")], sent: Mutex::default() });
        register_with(fake.clone());
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

        ask(&dir, "os.mail", "mail.send", json!({"account": id, "to": "alex@example.com", "subject": "Hi", "body": "Hello"}), false, &mut host).unwrap();
        assert_eq!(fake.sent.lock().unwrap()[0]["to"], "alex@example.com");

        ask(&dir, "os.mail", "mail.remove_account", json!({"account": id}), false, &mut host).unwrap();
        assert!(!dir.join("mail/secrets").join(&id).exists(), "the last app out takes the password with it");
    }
}
