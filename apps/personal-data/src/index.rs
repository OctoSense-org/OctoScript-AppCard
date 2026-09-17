//! The app-side index: one SQLite file with FTS5 tables for mail headers and
//! calendar events, refreshed lazily when a source's fingerprint changes.
//! Bodies are not stored unless `mail.index_bodies` is set, so the index
//! stays a few percent of the apps' own data.

use std::path::Path;

use rusqlite::{params, Connection, OptionalExtension};

use crate::calendar::{Calendar, Event, State};
use crate::mail::{epoch, Mailbox};
use crate::text::{clip, fts_query, has_cjk};

pub struct Index {
    conn: Connection,
}

#[derive(Debug, Default, Clone)]
pub struct MailFilter {
    pub query: String,
    pub folder: String,
    pub from: String,
    pub since: Option<i64>,
    pub before: Option<i64>,
    pub unread_only: bool,
    pub flagged_only: bool,
    pub limit: usize,
}

#[derive(Debug, Clone)]
pub struct MailHit {
    pub id: String,
    pub date: String,
    pub sender: String,
    pub address: String,
    pub subject: String,
    pub preview: String,
    pub unread: bool,
    pub flagged: bool,
    pub flag: String,
    pub folder: String,
    pub attachments: i64,
}

#[derive(Debug, Default, Clone)]
pub struct EventFilter {
    pub query: String,
    pub calendar: String,
    /// Inclusive wall-clock day bounds, `YYYY-MM-DD`.
    pub from: Option<String>,
    pub to: Option<String>,
    pub include_deleted: bool,
    pub limit: usize,
}

#[derive(Debug, Clone)]
pub struct Source {
    pub name: String,
    pub fingerprint: String,
    pub refreshed: String,
    pub note: String,
}

#[derive(Debug, Clone)]
pub struct Contact {
    pub name: String,
    pub address: String,
    pub messages: i64,
    pub last: String,
    pub subjects: Vec<String>,
}

impl Index {
    pub fn open(dir: &Path) -> Result<Self, String> {
        std::fs::create_dir_all(dir).map_err(|e| format!("create {}: {e}", dir.display()))?;
        let path = dir.join("index.sqlite");
        let conn = Connection::open(&path).map_err(|e| format!("open {}: {e}", path.display()))?;
        conn.execute_batch(SCHEMA).map_err(|e| format!("schema: {e}"))?;
        Ok(Self { conn })
    }

    pub fn source(&self, name: &str) -> Option<Source> {
        self.conn
            .query_row(
                "SELECT name, fingerprint, refreshed, note FROM sources WHERE name = ?1",
                [name],
                |r| {
                    Ok(Source {
                        name: r.get(0)?,
                        fingerprint: r.get(1)?,
                        refreshed: r.get(2)?,
                        note: r.get(3)?,
                    })
                },
            )
            .optional()
            .ok()
            .flatten()
    }

    pub fn sources(&self) -> Vec<Source> {
        let mut stmt = match self.conn.prepare("SELECT name, fingerprint, refreshed, note FROM sources ORDER BY name") {
            Ok(s) => s,
            Err(_) => return Vec::new(),
        };
        stmt.query_map([], |r| {
            Ok(Source {
                name: r.get(0)?,
                fingerprint: r.get(1)?,
                refreshed: r.get(2)?,
                note: r.get(3)?,
            })
        })
        .map(|rows| rows.flatten().collect())
        .unwrap_or_default()
    }

    /// Drop an account that is no longer configured (its mailbox file
    /// vanished or its directory left `mail.dirs`).
    pub fn remove_mail_source(&mut self, account: &str) -> Result<(), String> {
        let tx = self.conn.transaction().map_err(|e| e.to_string())?;
        tx.execute("DELETE FROM mail WHERE account = ?1", [account]).map_err(|e| e.to_string())?;
        tx.execute("DELETE FROM mail_fts WHERE account = ?1", [account]).map_err(|e| e.to_string())?;
        tx.execute("DELETE FROM sources WHERE name = ?1", [format!("mail:{account}")]).map_err(|e| e.to_string())?;
        tx.commit().map_err(|e| e.to_string())
    }

    /// Drop every calendar row and the calendar source entry.
    pub fn clear_calendar(&mut self) -> Result<(), String> {
        let tx = self.conn.transaction().map_err(|e| e.to_string())?;
        for table in ["events", "events_fts", "calendars"] {
            tx.execute(&format!("DELETE FROM {table}"), []).map_err(|e| e.to_string())?;
        }
        tx.execute("DELETE FROM sources WHERE name = 'calendar'", []).map_err(|e| e.to_string())?;
        tx.commit().map_err(|e| e.to_string())
    }

    pub fn note_source(&self, name: &str, note: &str) {
        let _ = self.conn.execute(
            "INSERT INTO sources(name, fingerprint, refreshed, note) VALUES (?1, '', '', ?2)
             ON CONFLICT(name) DO UPDATE SET note = excluded.note",
            params![name, note],
        );
    }

    pub fn count(&self, table: &str) -> i64 {
        self.conn
            .query_row(&format!("SELECT COUNT(*) FROM {table}"), [], |r| r.get(0))
            .unwrap_or(0)
    }

    /// Replace one account's messages. `index_bodies` adds the body text to
    /// the FTS table (never to the row table).
    pub fn ingest_mailbox(&mut self, mailbox: &Mailbox, fingerprint: &str, index_bodies: bool) -> Result<(), String> {
        let tx = self.conn.transaction().map_err(|e| e.to_string())?;
        tx.execute("DELETE FROM mail WHERE account = ?1", [&mailbox.account]).map_err(|e| e.to_string())?;
        tx.execute("DELETE FROM mail_fts WHERE account = ?1", [&mailbox.account])
            .map_err(|e| e.to_string())?;
        {
            let mut row = tx
                .prepare(
                    "INSERT OR REPLACE INTO mail(key, id, account, uid, ts, date, sender, address, subject, preview,
                     unread, flagged, flag, archived, trashed, attachments)
                     VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12,?13,?14,?15,?16)",
                )
                .map_err(|e| e.to_string())?;
            let mut fts = tx
                .prepare("INSERT INTO mail_fts(key, account, sender, address, subject, preview, body) VALUES (?1,?2,?3,?4,?5,?6,?7)")
                .map_err(|e| e.to_string())?;
            for m in &mailbox.messages {
                let body = if index_bodies { clip(&m.text(), 20_000) } else { String::new() };
                let key = mail_key(&mailbox.account, &m.id);
                row.execute(params![
                    key,
                    m.id,
                    mailbox.account,
                    m.uid,
                    epoch(&m.date),
                    m.date,
                    m.sender,
                    m.address,
                    m.subject,
                    m.preview,
                    m.unread as i64,
                    m.flagged as i64,
                    m.flag,
                    m.archived as i64,
                    m.trashed as i64,
                    m.attachments
                ])
                .map_err(|e| e.to_string())?;
                fts.execute(params![key, mailbox.account, m.sender, m.address, m.subject, m.preview, body])
                    .map_err(|e| e.to_string())?;
            }
        }
        let note = format!("{} · {} messages · synced {}", mailbox.address, mailbox.messages.len(), mailbox.synced_at);
        tx.execute(
            "INSERT INTO sources(name, fingerprint, refreshed, note) VALUES (?1, ?2, ?3, ?4)
             ON CONFLICT(name) DO UPDATE SET fingerprint = excluded.fingerprint, refreshed = excluded.refreshed, note = excluded.note",
            params![format!("mail:{}", mailbox.account), fingerprint, now(), note],
        )
        .map_err(|e| e.to_string())?;
        tx.commit().map_err(|e| e.to_string())
    }

    pub fn ingest_calendar(&mut self, state: &State) -> Result<(), String> {
        let tx = self.conn.transaction().map_err(|e| e.to_string())?;
        for table in ["events", "events_fts", "calendars"] {
            tx.execute(&format!("DELETE FROM {table}"), []).map_err(|e| e.to_string())?;
        }
        {
            let mut row = tx
                .prepare(
                    "INSERT INTO events(id, calendar, start, end, start_ts, end_ts, first_day, last_day, all_day, title, title_alt,
                     location, location_alt, notes, deleted, invitation, created_by)
                     VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12,?13,?14,?15,?16,?17)",
                )
                .map_err(|e| e.to_string())?;
            let mut fts = tx
                .prepare("INSERT INTO events_fts(id, title, title_alt, location, location_alt, notes, calendar) VALUES (?1,?2,?3,?4,?5,?6,?7)")
                .map_err(|e| e.to_string())?;
            for e in &state.events {
                row.execute(params![
                    e.id, e.calendar, e.start, e.end, e.start_ts, e.end_ts, e.first_day, e.last_day, e.all_day as i64, e.title,
                    e.title_alt, e.location, e.location_alt, e.notes, e.deleted as i64, e.invitation, e.created_by
                ])
                .map_err(|x| x.to_string())?;
                fts.execute(params![e.id, e.title, e.title_alt, e.location, e.location_alt, e.notes, e.calendar])
                    .map_err(|x| x.to_string())?;
            }
            let mut cal = tx
                .prepare("INSERT INTO calendars(id, name, name_alt, color, visible, shared_with) VALUES (?1,?2,?3,?4,?5,?6)")
                .map_err(|e| e.to_string())?;
            for c in &state.calendars {
                cal.execute(params![c.id, c.name, c.name_alt, c.color, c.visible as i64, c.shared_with.join(",")])
                    .map_err(|e| e.to_string())?;
            }
        }
        let note = format!("{} events · {} calendars", state.events.len(), state.calendars.len());
        tx.execute(
            "INSERT INTO sources(name, fingerprint, refreshed, note) VALUES ('calendar', ?1, ?2, ?3)
             ON CONFLICT(name) DO UPDATE SET fingerprint = excluded.fingerprint, refreshed = excluded.refreshed, note = excluded.note",
            params![state.fingerprint, now(), note],
        )
        .map_err(|e| e.to_string())?;
        tx.commit().map_err(|e| e.to_string())
    }

    pub fn search_mail(&self, f: &MailFilter) -> Result<(Vec<MailHit>, i64), String> {
        let mut clauses = Vec::new();
        let mut args: Vec<rusqlite::types::Value> = Vec::new();
        match f.folder.as_str() {
            "" | "inbox" => clauses.push("m.archived = 0 AND m.trashed = 0".to_string()),
            "archive" => clauses.push("m.archived = 1 AND m.trashed = 0".to_string()),
            "trash" => clauses.push("m.trashed = 1".to_string()),
            _ => {}
        }
        if !f.from.trim().is_empty() {
            clauses.push(format!("(m.sender LIKE ?{0} OR m.address LIKE ?{0})", args.len() + 1));
            args.push(format!("%{}%", f.from.trim()).into());
        }
        if let Some(since) = f.since {
            clauses.push(format!("m.ts >= ?{}", args.len() + 1));
            args.push(since.into());
        }
        if let Some(before) = f.before {
            clauses.push(format!("m.ts < ?{}", args.len() + 1));
            args.push(before.into());
        }
        if f.unread_only {
            clauses.push("m.unread = 1".into());
        }
        if f.flagged_only {
            clauses.push("m.flagged = 1".into());
        }
        let limit = f.limit.clamp(1, 50) as i64;
        let fts = fts_query(&f.query);
        let use_fts = fts.is_some() && !has_cjk(&f.query);
        let (join, order) = if use_fts {
            clauses.push(format!("mail_fts MATCH ?{}", args.len() + 1));
            args.push(fts.clone().unwrap().into());
            (
                "mail_fts JOIN mail m ON m.key = mail_fts.key",
                "bm25(mail_fts, 0.0, 0.0, 2.0, 1.0, 5.0, 1.0, 0.5), m.ts DESC",
            )
        } else {
            if !f.query.trim().is_empty() {
                let like = format!("%{}%", f.query.trim());
                let n = args.len() + 1;
                // Substring fallback (CJK or empty FTS): headers plus any
                // opted-in body text kept in the FTS table.
                clauses.push(format!(
                    "(m.subject LIKE ?{n} OR m.sender LIKE ?{n} OR m.preview LIKE ?{n} OR m.address LIKE ?{n} \
                     OR EXISTS (SELECT 1 FROM mail_fts f WHERE f.key = m.key AND f.body LIKE ?{n}))"
                ));
                args.push(like.into());
            }
            ("mail m", "m.ts DESC")
        };
        let where_sql = if clauses.is_empty() { String::new() } else { format!("WHERE {}", clauses.join(" AND ")) };
        let total: i64 = self
            .conn
            .query_row(&format!("SELECT COUNT(*) FROM {join} {where_sql}"), rusqlite::params_from_iter(args.iter()), |r| r.get(0))
            .map_err(|e| format!("count: {e}"))?;
        let sql = format!(
            "SELECT m.key, m.date, m.sender, m.address, m.subject, m.preview, m.unread, m.flagged, m.flag,
             m.archived, m.trashed, m.attachments FROM {join} {where_sql} ORDER BY {order} LIMIT {limit}"
        );
        let mut stmt = self.conn.prepare(&sql).map_err(|e| format!("query: {e}"))?;
        let rows = stmt
            .query_map(rusqlite::params_from_iter(args.iter()), |r| {
                let archived: i64 = r.get(9)?;
                let trashed: i64 = r.get(10)?;
                Ok(MailHit {
                    id: r.get(0)?,
                    date: r.get(1)?,
                    sender: r.get(2)?,
                    address: r.get(3)?,
                    subject: r.get(4)?,
                    preview: r.get(5)?,
                    unread: r.get::<_, i64>(6)? != 0,
                    flagged: r.get::<_, i64>(7)? != 0,
                    flag: r.get(8)?,
                    folder: if trashed != 0 { "trash" } else if archived != 0 { "archive" } else { "inbox" }.into(),
                    attachments: r.get(11)?,
                })
            })
            .map_err(|e| format!("rows: {e}"))?
            .flatten()
            .collect();
        Ok((rows, total))
    }

    pub fn search_events(&self, f: &EventFilter) -> Result<(Vec<Event>, i64), String> {
        let mut clauses = Vec::new();
        let mut args: Vec<rusqlite::types::Value> = Vec::new();
        if !f.include_deleted {
            clauses.push("e.deleted = 0".to_string());
        }
        if !f.calendar.trim().is_empty() {
            clauses.push(format!("e.calendar = ?{}", args.len() + 1));
            args.push(f.calendar.trim().to_string().into());
        }
        if let Some(from) = &f.from {
            clauses.push(format!("e.last_day >= ?{}", args.len() + 1));
            args.push(from.clone().into());
        }
        if let Some(to) = &f.to {
            clauses.push(format!("e.first_day <= ?{}", args.len() + 1));
            args.push(to.clone().into());
        }
        let fts = fts_query(&f.query);
        let join = if fts.is_some() && !has_cjk(&f.query) {
            clauses.push(format!("events_fts MATCH ?{}", args.len() + 1));
            args.push(fts.unwrap().into());
            "events_fts JOIN events e ON e.id = events_fts.id"
        } else {
            if !f.query.trim().is_empty() {
                let n = args.len() + 1;
                clauses.push(format!(
                    "(e.title LIKE ?{n} OR e.title_alt LIKE ?{n} OR e.location LIKE ?{n} OR e.location_alt LIKE ?{n} OR e.notes LIKE ?{n})"
                ));
                args.push(format!("%{}%", f.query.trim()).into());
            }
            "events e"
        };
        let where_sql = if clauses.is_empty() { String::new() } else { format!("WHERE {}", clauses.join(" AND ")) };
        let total: i64 = self
            .conn
            .query_row(&format!("SELECT COUNT(*) FROM {join} {where_sql}"), rusqlite::params_from_iter(args.iter()), |r| r.get(0))
            .map_err(|e| format!("count: {e}"))?;
        let limit = f.limit.clamp(1, 100) as i64;
        let sql = format!(
            "SELECT e.id, e.calendar, e.start, e.end, e.start_ts, e.end_ts, e.first_day, e.last_day, e.all_day, e.title,
             e.title_alt, e.location, e.location_alt, e.notes, e.deleted, e.invitation, e.created_by FROM {join} {where_sql}
             ORDER BY e.first_day, e.all_day DESC, e.start_ts, e.id LIMIT {limit}"
        );
        let mut stmt = self.conn.prepare(&sql).map_err(|e| format!("query: {e}"))?;
        let rows = stmt
            .query_map(rusqlite::params_from_iter(args.iter()), |r| {
                Ok(Event {
                    id: r.get(0)?,
                    calendar: r.get(1)?,
                    start: r.get(2)?,
                    end: r.get(3)?,
                    start_ts: r.get(4)?,
                    end_ts: r.get(5)?,
                    first_day: r.get(6)?,
                    last_day: r.get(7)?,
                    all_day: r.get::<_, i64>(8)? != 0,
                    title: r.get(9)?,
                    title_alt: r.get(10)?,
                    location: r.get(11)?,
                    location_alt: r.get(12)?,
                    notes: r.get(13)?,
                    deleted: r.get::<_, i64>(14)? != 0,
                    invitation: r.get(15)?,
                    created_by: r.get(16)?,
                })
            })
            .map_err(|e| format!("rows: {e}"))?
            .flatten()
            .collect();
        Ok((rows, total))
    }

    pub fn calendars(&self) -> Vec<Calendar> {
        let Ok(mut stmt) = self.conn.prepare("SELECT id, name, name_alt, color, visible, shared_with FROM calendars ORDER BY id") else {
            return Vec::new();
        };
        stmt.query_map([], |r| {
            let shared: String = r.get(5)?;
            Ok(Calendar {
                id: r.get(0)?,
                name: r.get(1)?,
                name_alt: r.get(2)?,
                color: r.get(3)?,
                visible: r.get::<_, i64>(4)? != 0,
                shared_with: shared.split(',').filter(|s| !s.is_empty()).map(str::to_string).collect(),
            })
        })
        .map(|rows| rows.flatten().collect())
        .unwrap_or_default()
    }

    /// People seen in mail whose display name has a word starting with
    /// `name`, or whose address has a local-part token starting with it
    /// (so "sam" finds "Sam Lee" and "sam.lee@…" but not "transamerica").
    pub fn contacts(&self, name: &str, limit: usize) -> Result<Vec<Contact>, String> {
        let needle = name.trim().to_lowercase();
        let word = format!("% {needle}%");
        let local = format!("{needle}%");
        let mut stmt = self
            .conn
            .prepare(
                "SELECT address, MAX(sender), COUNT(*), MAX(date) FROM mail
                 WHERE trashed = 0 AND (
                   (' ' || lower(sender)) LIKE ?1
                   OR lower(address) LIKE ?2
                   OR lower(address) LIKE ?3
                   OR (' ' || replace(replace(replace(replace(lower(address), '.', ' '), '_', ' '), '-', ' '), '+', ' ')) LIKE ?1)
                 GROUP BY address ORDER BY COUNT(*) DESC, MAX(ts) DESC LIMIT ?4",
            )
            .map_err(|e| e.to_string())?;
        let mut contacts: Vec<Contact> = stmt
            .query_map(params![word, local, format!("%@{needle}%"), limit.clamp(1, 25) as i64], |r| {
                Ok(Contact {
                    address: r.get(0)?,
                    name: r.get(1)?,
                    messages: r.get(2)?,
                    last: r.get(3)?,
                    subjects: Vec::new(),
                })
            })
            .map_err(|e| e.to_string())?
            .flatten()
            .collect();
        let mut subj = self
            .conn
            .prepare("SELECT subject FROM mail WHERE address = ?1 AND trashed = 0 ORDER BY ts DESC LIMIT 3")
            .map_err(|e| e.to_string())?;
        for c in &mut contacts {
            c.subjects = subj
                .query_map([&c.address], |r| r.get::<_, String>(0))
                .map(|rows| rows.flatten().collect())
                .unwrap_or_default();
        }
        Ok(contacts)
    }
}

/// Account-qualified row key: Mail's message ids hash only the UID, so two
/// accounts can share one; the key is what the tools hand back as `id`.
pub fn mail_key(account: &str, id: &str) -> String {
    format!("{account}/{id}")
}

pub fn now() -> String {
    chrono::Local::now().to_rfc3339_opts(chrono::SecondsFormat::Secs, true)
}

const SCHEMA: &str = "
PRAGMA journal_mode = WAL;
CREATE TABLE IF NOT EXISTS sources(name TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, refreshed TEXT NOT NULL, note TEXT NOT NULL DEFAULT '');
CREATE TABLE IF NOT EXISTS mail(
  key TEXT PRIMARY KEY, id TEXT NOT NULL, account TEXT NOT NULL, uid TEXT NOT NULL, ts INTEGER NOT NULL, date TEXT NOT NULL,
  sender TEXT NOT NULL, address TEXT NOT NULL, subject TEXT NOT NULL, preview TEXT NOT NULL,
  unread INTEGER NOT NULL, flagged INTEGER NOT NULL, flag TEXT NOT NULL, archived INTEGER NOT NULL,
  trashed INTEGER NOT NULL, attachments INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS mail_ts ON mail(ts DESC);
CREATE INDEX IF NOT EXISTS mail_address ON mail(address);
CREATE VIRTUAL TABLE IF NOT EXISTS mail_fts USING fts5(
  key UNINDEXED, account UNINDEXED, sender, address, subject, preview, body, tokenize='unicode61 remove_diacritics 2');
CREATE TABLE IF NOT EXISTS events(
  id TEXT PRIMARY KEY, calendar TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL,
  start_ts INTEGER NOT NULL, end_ts INTEGER NOT NULL, first_day TEXT NOT NULL, last_day TEXT NOT NULL, all_day INTEGER NOT NULL,
  title TEXT NOT NULL, title_alt TEXT NOT NULL, location TEXT NOT NULL, location_alt TEXT NOT NULL,
  notes TEXT NOT NULL, deleted INTEGER NOT NULL, invitation TEXT NOT NULL, created_by TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS events_days ON events(first_day, last_day);
CREATE VIRTUAL TABLE IF NOT EXISTS events_fts USING fts5(
  id UNINDEXED, title, title_alt, location, location_alt, notes, calendar, tokenize='unicode61 remove_diacritics 2');
CREATE TABLE IF NOT EXISTS calendars(
  id TEXT PRIMARY KEY, name TEXT NOT NULL, name_alt TEXT NOT NULL, color TEXT NOT NULL,
  visible INTEGER NOT NULL, shared_with TEXT NOT NULL);
";
