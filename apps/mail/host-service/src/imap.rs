//! IMAP for the mail service: folders, new mail by UID, and the read flag.
//!
//! Only what the service needs, over TLS or STARTTLS: `LOGIN`, `LIST`,
//! `EXAMINE`/`SELECT`, `UID SEARCH`, `UID FETCH` and `UID STORE`. Messages are
//! decoded by the same code as POP3's, so a message reads the same whichever
//! way it arrived.
use crate::network::{self, text, Wire};
use serde_json::{json, Value};

/// A message this large is listed but not downloaded.
const MAX_MESSAGE: usize = 2_000_000;

pub struct Imap {
    wire: Wire,
    tag: u32,
}

/// One untagged response: its text, with each literal it carried in order.
/// Where a literal sat, the text holds `{n}` as the server sent it.
pub struct Untagged {
    pub text: String,
    pub literals: Vec<Vec<u8>>,
}

fn rejected() -> String {
    "Mail server rejected the sign-in. Check the address and app password.".into()
}

impl Imap {
    pub fn connect(account: &Value) -> Result<Imap, String> {
        network::validate(account)?;
        let host = text(account, "host");
        let port = text(account, "port").parse().map_err(|_| "Port must be between 1 and 65535.")?;
        let mut wire = Wire::connect(host, port)?;
        if text(account, "security") == "tls" {
            wire = wire.tls(host)?;
        }
        let mut imap = Imap::greeted(wire)?;
        if text(account, "security") == "starttls" {
            imap.command("STARTTLS")?;
            imap.wire = imap.wire.tls(host)?;
        }
        imap.login(text(account, "username"), text(account, "password"))?;
        Ok(imap)
    }

    fn greeted(mut wire: Wire) -> Result<Imap, String> {
        let greeting = wire.line()?;
        if !greeting.starts_with(b"* OK") && !greeting.starts_with(b"* PREAUTH") {
            return Err("Invalid IMAP greeting.".into());
        }
        Ok(Imap { wire, tag: 0 })
    }

    fn login(&mut self, user: &str, pass: &str) -> Result<(), String> {
        self.run(&[Part::Atom("LOGIN"), Part::Str(user), Part::Str(pass)]).map_err(|e| if e.starts_with("Mail server said") { rejected() } else { e })?;
        Ok(())
    }

    pub fn command(&mut self, command: &str) -> Result<Vec<Untagged>, String> {
        self.run(&[Part::Atom(command)])
    }

    /// Send one command, strings quoted or sent as literals as they need,
    /// and read to its tagged completion.
    fn run(&mut self, parts: &[Part]) -> Result<Vec<Untagged>, String> {
        self.tag += 1;
        let tag = format!("a{}", self.tag);
        let mut line = tag.clone().into_bytes();
        for part in parts {
            line.push(b' ');
            match part {
                Part::Atom(atom) => line.extend_from_slice(atom.as_bytes()),
                Part::Str(value) if quotable(value) => line.extend_from_slice(quote(value).as_bytes()),
                Part::Str(value) => {
                    // A literal: announce its length, wait for the go-ahead.
                    line.extend_from_slice(format!("{{{}}}\r\n", value.len()).as_bytes());
                    self.wire.write(&line)?;
                    let go = self.wire.line()?;
                    if !go.starts_with(b"+") {
                        return Err("Mail server refused the request.".into());
                    }
                    line = value.as_bytes().to_vec();
                }
            }
        }
        line.extend_from_slice(b"\r\n");
        self.wire.write(&line)?;
        self.read_to(&tag)
    }

    fn read_to(&mut self, tag: &str) -> Result<Vec<Untagged>, String> {
        let mut out = Vec::new();
        let mut total = 0usize;
        loop {
            let first = self.wire.line()?;
            if first.starts_with(tag.as_bytes()) && first.get(tag.len()) == Some(&b' ') {
                let status = String::from_utf8_lossy(&first[tag.len() + 1..]).to_string();
                if status.starts_with("OK") {
                    return Ok(out);
                }
                return Err(format!("Mail server said: {}", status.trim()));
            }
            let mut response = Untagged { text: String::new(), literals: Vec::new() };
            let mut line = first;
            loop {
                let trimmed = trim_crlf(&line);
                response.text.push_str(&String::from_utf8_lossy(trimmed));
                match literal_len(trimmed) {
                    Some(n) => {
                        total += n;
                        if total > MAX_MESSAGE * 4 {
                            return Err("Mail server sent more than expected.".into());
                        }
                        response.literals.push(self.wire.read_exact(n)?);
                        line = self.wire.line()?;
                    }
                    None => break,
                }
            }
            out.push(response);
        }
    }

    /// The folders a person can open, inbox first, then the special ones.
    pub fn folders(&mut self) -> Result<Vec<Value>, String> {
        let mut folders = Vec::new();
        for row in self.command("LIST \"\" \"*\"")? {
            let Some(rest) = row.text.strip_prefix("* LIST ") else { continue };
            let Some((flags, rest)) = rest.strip_prefix('(').and_then(|r| r.split_once(')')) else { continue };
            let flags = flags.to_ascii_lowercase();
            if flags.contains("\\noselect") || flags.contains("\\nonexistent") {
                continue;
            }
            let mut words = Words { text: rest.trim_start(), literals: row.literals.iter() };
            let delimiter = words.next().unwrap_or_default();
            let Some(name) = words.next() else { continue };
            let role = if name.eq_ignore_ascii_case("INBOX") {
                "inbox"
            } else {
                ["sent", "drafts", "junk", "trash", "archive", "all", "flagged"]
                    .into_iter()
                    .find(|role| flags.contains(&format!("\\{role}")))
                    .unwrap_or("")
            };
            let shown = match role {
                "inbox" => "Inbox".to_string(),
                _ => {
                    let leaf = if delimiter.is_empty() { name.as_str() } else { name.rsplit(delimiter.as_str()).next().unwrap_or(&name) };
                    decode_utf7(leaf)
                }
            };
            folders.push(json!({"id": name, "name": shown, "role": role}));
        }
        let order = |f: &Value| ["inbox", "flagged", "drafts", "sent", "archive", "all", "junk", "trash", ""].iter().position(|r| *r == text(f, "role")).unwrap_or(9);
        folders.sort_by(|a, b| order(a).cmp(&order(b)).then_with(|| text(a, "name").to_lowercase().cmp(&text(b, "name").to_lowercase())));
        Ok(folders)
    }

    /// Mail newer than `state.last_uid` in `folder`, newest first, at most
    /// `limit`; the whole folder again if the server renumbered it.
    pub fn fetch(&mut self, folder: &str, state: &Value, limit: usize) -> Result<Value, String> {
        let selected = self.run(&[Part::Atom("EXAMINE"), Part::Str(folder)])?;
        let validity = selected.iter().find_map(|r| bracket_number(&r.text, "UIDVALIDITY")).unwrap_or(0);
        let exists = selected.iter().find_map(|r| r.text.strip_suffix(" EXISTS").and_then(|t| t.strip_prefix("* ")).and_then(|n| n.parse::<u64>().ok())).unwrap_or(0);
        let reset = state["uidvalidity"].as_u64() != Some(validity);
        let last = if reset { 0 } else { state["last_uid"].as_u64().unwrap_or(0) };
        let mut uids: Vec<u64> = Vec::new();
        if exists > 0 {
            for row in self.command(&format!("UID SEARCH UID {}:*", last + 1))? {
                if let Some(list) = row.text.strip_prefix("* SEARCH") {
                    // `n:*` always matches the highest UID, even an old one.
                    uids.extend(list.split_whitespace().filter_map(|u| u.parse::<u64>().ok()).filter(|u| *u > last));
                }
            }
        }
        uids.sort_unstable();
        let newest = uids.last().copied().unwrap_or(last);
        let has_more = uids.len() > limit;
        let wanted: Vec<u64> = uids.into_iter().rev().take(limit).collect();
        let mut messages = Vec::new();
        if !wanted.is_empty() {
            let set = wanted.iter().map(u64::to_string).collect::<Vec<_>>().join(",");
            let mut meta = std::collections::HashMap::new();
            for row in self.command(&format!("UID FETCH {set} (UID FLAGS RFC822.SIZE)"))? {
                if let Some(uid) = item_number(&row.text, "UID") {
                    let size = item_number(&row.text, "RFC822.SIZE").unwrap_or(0) as usize;
                    let unread = !row.text.to_ascii_lowercase().contains("\\seen");
                    meta.insert(uid, (size, unread));
                }
            }
            for uid in &wanted {
                let Some((size, unread)) = meta.get(uid).copied() else { continue };
                let key = format!("{folder}\n{validity}/{uid}");
                let mut message = if size > MAX_MESSAGE {
                    let raw = self.body(*uid, "BODY.PEEK[HEADER]")?;
                    let mut message = network::decode(&raw, &key)?;
                    let note = format!("This message is {:.1} MB, too large to download here.", size as f64 / 1e6);
                    message["body"] = json!(note);
                    message["preview"] = json!(note);
                    message
                } else {
                    network::decode(&self.body(*uid, "BODY.PEEK[]")?, &key)?
                };
                message["imap_uid"] = json!(uid);
                message["unread"] = json!(unread);
                messages.push(message);
            }
        }
        Ok(json!({"messages": messages, "reset": reset, "state": {"uidvalidity": validity, "last_uid": newest}, "has_more": has_more}))
    }

    fn body(&mut self, uid: u64, item: &str) -> Result<Vec<u8>, String> {
        self.command(&format!("UID FETCH {uid} ({item})"))?
            .into_iter()
            .find_map(|row| row.literals.into_iter().next())
            .ok_or_else(|| "The mail server did not send the message.".to_string())
    }

    pub fn mark_seen(&mut self, folder: &str, uid: u64) -> Result<(), String> {
        self.run(&[Part::Atom("SELECT"), Part::Str(folder)])?;
        self.command(&format!("UID STORE {uid} +FLAGS.SILENT (\\Seen)"))?;
        Ok(())
    }

    pub fn logout(mut self) {
        let _ = self.command("LOGOUT");
    }
}

enum Part<'a> {
    Atom(&'a str),
    Str(&'a str),
}

fn quotable(value: &str) -> bool {
    value.is_ascii() && !value.contains(['\r', '\n', '\0']) && value.len() < 1000
}

fn quote(value: &str) -> String {
    format!("\"{}\"", value.replace('\\', "\\\\").replace('"', "\\\""))
}

fn trim_crlf(line: &[u8]) -> &[u8] {
    let line = line.strip_suffix(b"\n").unwrap_or(line);
    line.strip_suffix(b"\r").unwrap_or(line)
}

/// `{123}` at the end of a line: a literal of that many bytes follows.
fn literal_len(line: &[u8]) -> Option<usize> {
    let line = line.strip_suffix(b"}")?;
    let open = line.iter().rposition(|b| *b == b'{')?;
    std::str::from_utf8(&line[open + 1..]).ok()?.trim_end_matches('+').parse().ok()
}

/// `[NAME 123]` in a response: the number.
fn bracket_number(text: &str, name: &str) -> Option<u64> {
    let at = text.find(&format!("[{name} "))? + name.len() + 2;
    text[at..].split(']').next()?.trim().parse().ok()
}

/// `NAME 123` inside a FETCH response: the number.
fn item_number(text: &str, name: &str) -> Option<u64> {
    let mut words = text.split(|c: char| c.is_whitespace() || c == '(' || c == ')');
    while let Some(word) = words.next() {
        if word.eq_ignore_ascii_case(name) {
            return words.next()?.parse().ok();
        }
    }
    None
}

/// The words of a LIST response after its flags: quoted strings, `NIL`,
/// atoms and literals.
struct Words<'a, I: Iterator<Item = &'a Vec<u8>>> {
    text: &'a str,
    literals: I,
}

impl<'a, I: Iterator<Item = &'a Vec<u8>>> Iterator for Words<'a, I> {
    type Item = String;
    fn next(&mut self) -> Option<String> {
        let text = self.text.trim_start();
        if text.is_empty() {
            return None;
        }
        if let Some(rest) = text.strip_prefix('"') {
            let mut out = String::new();
            let mut chars = rest.char_indices();
            while let Some((i, c)) = chars.next() {
                match c {
                    '\\' => out.extend(chars.next().map(|(_, c)| c)),
                    '"' => {
                        self.text = &rest[i + 1..];
                        return Some(out);
                    }
                    c => out.push(c),
                }
            }
            self.text = "";
            return Some(out);
        }
        if text.starts_with('{') {
            self.text = text.split_once('}').map(|(_, r)| r).unwrap_or("");
            return self.literals.next().map(|l| String::from_utf8_lossy(l).to_string());
        }
        let end = text.find(' ').unwrap_or(text.len());
        self.text = &text[end..];
        let word = &text[..end];
        Some(if word.eq_ignore_ascii_case("NIL") { String::new() } else { word.to_string() })
    }
}

/// IMAP's modified UTF-7 folder names (`&AOk-t&AOk-` is `été`).
pub fn decode_utf7(name: &str) -> String {
    use base64::Engine;
    let mut out = String::new();
    let mut rest = name;
    while let Some(start) = rest.find('&') {
        out.push_str(&rest[..start]);
        let after = &rest[start + 1..];
        let Some(end) = after.find('-') else {
            out.push_str(&rest[start..]);
            return out;
        };
        let chunk = &after[..end];
        if chunk.is_empty() {
            out.push('&');
        } else {
            let b64 = chunk.replace(',', "/");
            match base64::engine::general_purpose::STANDARD_NO_PAD.decode(b64.trim_end_matches('=')) {
                Ok(bytes) => {
                    let units: Vec<u16> = bytes.chunks_exact(2).map(|p| u16::from_be_bytes([p[0], p[1]])).collect();
                    out.push_str(&String::from_utf16_lossy(&units));
                }
                Err(_) => out.push_str(&rest[start..start + end + 2]),
            }
        }
        rest = &after[end + 1..];
    }
    out.push_str(rest);
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn folder_names_and_responses_parse() {
        assert_eq!(decode_utf7("Entw&APw-rfe"), "Entwürfe");
        assert_eq!(decode_utf7("&ZeVnLIqe-"), "日本語");
        assert_eq!(decode_utf7("A&-B"), "A&B");
        assert_eq!(literal_len(b"* 1 FETCH (UID 7 BODY[] {42}"), Some(42));
        assert_eq!(literal_len(b"* 1 FETCH (UID 7)"), None);
        assert_eq!(bracket_number("* OK [UIDVALIDITY 3857529045] UIDs valid", "UIDVALIDITY"), Some(3857529045));
        assert_eq!(item_number("* 3 FETCH (UID 812 FLAGS (\\Seen) RFC822.SIZE 4410)", "RFC822.SIZE"), Some(4410));
        assert_eq!(item_number("* 3 FETCH (UID 812 FLAGS (\\Seen) RFC822.SIZE 4410)", "UID"), Some(812));
        let literals = [b"Odd \"name\"".to_vec()];
        let mut words = Words { text: "\"/\" {10}", literals: literals.iter() };
        assert_eq!(words.next().as_deref(), Some("/"));
        assert_eq!(words.next().as_deref(), Some("Odd \"name\""));
        let mut words = Words { text: "\"/\" \"[Gmail]/Sent \\\"Mail\\\"\"", literals: [].iter() };
        words.next();
        assert_eq!(words.next().as_deref(), Some("[Gmail]/Sent \"Mail\""));
        assert_eq!(quote("a\"b\\c"), "\"a\\\"b\\\\c\"");
    }

    /// A scripted server on localhost, spoken to without TLS: sign-in with a
    /// literal password, folders, a fetch with an oversized message, a
    /// second fetch that finds nothing new, and the read flag.
    #[test]
    fn a_session_against_a_scripted_server() {
        use std::io::{BufRead, BufReader, Read, Write};
        let listener = std::net::TcpListener::bind("127.0.0.1:0").unwrap();
        let port = listener.local_addr().unwrap().port();
        let raw = "From: Ana <ana@example.com>\r\nSubject: Hi\r\nDate: Thu, 24 Sep 2026 10:00:00 +0000\r\n\r\nHello from IMAP\r\n";
        let server = std::thread::spawn(move || {
            let (stream, _) = listener.accept().unwrap();
            let mut out = stream.try_clone().unwrap();
            let mut input = BufReader::new(stream);
            let mut heard = Vec::new();
            out.write_all(b"* OK ready\r\n").unwrap();
            loop {
                let mut line = String::new();
                if input.read_line(&mut line).unwrap() == 0 {
                    break;
                }
                let mut line = line.trim_end().to_string();
                if let Some(n) = literal_len(line.as_bytes()) {
                    out.write_all(b"+ go\r\n").unwrap();
                    let mut literal = vec![0; n];
                    input.read_exact(&mut literal).unwrap();
                    let mut rest = String::new();
                    input.read_line(&mut rest).unwrap();
                    line = format!("{line}<{}>{}", String::from_utf8(literal).unwrap(), rest.trim_end());
                }
                let (tag, command) = line.split_once(' ').unwrap();
                heard.push(command.to_string());
                let reply = match command {
                    c if c.starts_with("LOGIN") => String::new(),
                    "LIST \"\" \"*\"" => concat!(
                        "* LIST (\\HasChildren \\Noselect) \"/\" \"[Gmail]\"\r\n",
                        "* LIST (\\HasNoChildren \\Sent) \"/\" \"[Gmail]/Sent Mail\"\r\n",
                        "* LIST (\\HasNoChildren) \"/\" \"Entw&APw-rfe\"\r\n",
                        "* LIST (\\HasNoChildren) \"/\" {5}\r\nOdd\"x\r\n",
                        "* LIST (\\HasNoChildren) \"/\" \"INBOX\"\r\n"
                    )
                    .to_string(),
                    "EXAMINE \"INBOX\"" => "* 3 EXISTS\r\n* OK [UIDVALIDITY 42] UIDs valid\r\n".to_string(),
                    "UID SEARCH UID 1:*" => "* SEARCH 5 7 9\r\n".to_string(),
                    "UID SEARCH UID 10:*" => "* SEARCH 9\r\n".to_string(),
                    "UID FETCH 9,7,5 (UID FLAGS RFC822.SIZE)" => concat!(
                        "* 1 FETCH (UID 5 FLAGS (\\Seen) RFC822.SIZE 100)\r\n",
                        "* 2 FETCH (UID 7 FLAGS () RFC822.SIZE 3000000)\r\n",
                        "* 3 FETCH (UID 9 FLAGS (\\Recent) RFC822.SIZE 90)\r\n"
                    )
                    .to_string(),
                    "UID FETCH 9 (BODY.PEEK[])" | "UID FETCH 5 (BODY.PEEK[])" => format!("* 3 FETCH (UID 9 BODY[] {{{}}}\r\n{raw})\r\n", raw.len()),
                    "UID FETCH 7 (BODY.PEEK[HEADER])" => {
                        let head = "From: big@example.com\r\nSubject: Huge\r\n\r\n";
                        format!("* 2 FETCH (UID 7 BODY[HEADER] {{{}}}\r\n{head})\r\n", head.len())
                    }
                    "SELECT \"INBOX\"" | "UID STORE 9 +FLAGS.SILENT (\\Seen)" => String::new(),
                    "LOGOUT" => "* BYE\r\n".to_string(),
                    other => {
                        out.write_all(format!("{tag} BAD unexpected {other}\r\n").as_bytes()).unwrap();
                        continue;
                    }
                };
                out.write_all(format!("{reply}{tag} OK done\r\n").as_bytes()).unwrap();
                if command == "LOGOUT" {
                    break;
                }
            }
            heard
        });

        let mut imap = Imap::greeted(Wire::connect("127.0.0.1", port).unwrap()).unwrap();
        imap.login("me@example.com", "pässword").unwrap();
        let folders = imap.folders().unwrap();
        let names: Vec<(&str, &str, &str)> = folders.iter().map(|f| (text(f, "id"), text(f, "name"), text(f, "role"))).collect();
        assert_eq!(names, [("INBOX", "Inbox", "inbox"), ("[Gmail]/Sent Mail", "Sent Mail", "sent"), ("Entw&APw-rfe", "Entwürfe", ""), ("Odd\"x", "Odd\"x", "")]);

        let fetched = imap.fetch("INBOX", &json!({}), 25).unwrap();
        let messages = fetched["messages"].as_array().unwrap();
        assert_eq!(messages.len(), 3);
        assert_eq!(messages[0]["subject"], "Hi");
        assert_eq!(messages[0]["body"].as_str().unwrap().trim(), "Hello from IMAP");
        assert_eq!(messages[0]["unread"], true);
        assert_eq!(messages[0]["imap_uid"], 9);
        assert_eq!(messages[1]["subject"], "Huge");
        assert!(messages[1]["body"].as_str().unwrap().contains("too large"));
        assert_eq!(messages[2]["unread"], false, "\\Seen on the server is read here");
        assert_eq!(fetched["state"], json!({"uidvalidity": 42, "last_uid": 9}));
        assert_eq!(fetched["reset"], true, "a first fetch starts the folder afresh");

        let again = imap.fetch("INBOX", &fetched["state"], 25).unwrap();
        assert_eq!(again["messages"], json!([]), "the highest UID a search always returns is not new");
        assert_eq!(again["reset"], false);

        imap.mark_seen("INBOX", 9).unwrap();
        imap.logout();
        let heard = server.join().unwrap();
        assert_eq!(heard[0], "LOGIN \"me@example.com\" {9}<pässword>", "a non-ASCII password goes as a literal");
    }

    /// Reaches Gmail: `cargo test -- --ignored gmail`.
    #[test]
    #[ignore]
    fn gmail_refuses_a_wrong_password_with_a_readable_error() {
        let mut account = network::defaults();
        for (k, v) in [("address", "nobody.octosense.test@gmail.com"), ("username", "nobody.octosense.test@gmail.com"), ("password", "not-a-password"), ("host", "imap.gmail.com"), ("port", "993")] {
            account[k] = json!(v);
        }
        let error = Imap::connect(&account).err().unwrap();
        assert_eq!(error, rejected());
    }
}
