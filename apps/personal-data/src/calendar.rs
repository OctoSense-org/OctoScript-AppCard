//! Reading the Calendar app's state (`GET /v1/state` on the sync server, or a
//! state document on disk for offline use and tests).

use std::time::Duration;

use serde_json::Value;

use crate::config::{CalendarConfig, Loaded};
use crate::mail::epoch;

#[derive(Debug, Clone, Default)]
pub struct Event {
    pub id: String,
    pub calendar: String,
    pub start: String,
    pub end: String,
    pub start_ts: i64,
    pub end_ts: i64,
    /// Wall-clock days in the event's own offset (`YYYY-MM-DD`), inclusive.
    /// Date filters use these so "what's on the 24th" means the calendar's
    /// 24th, not the machine's time zone.
    pub first_day: String,
    pub last_day: String,
    pub all_day: bool,
    pub title: String,
    pub title_alt: String,
    pub location: String,
    pub location_alt: String,
    pub notes: String,
    pub deleted: bool,
    pub invitation: String,
    pub created_by: String,
}

#[derive(Debug, Clone, Default)]
pub struct Calendar {
    pub id: String,
    pub name: String,
    pub name_alt: String,
    pub color: String,
    pub visible: bool,
    pub shared_with: Vec<String>,
}

pub struct State {
    pub fingerprint: String,
    pub events: Vec<Event>,
    pub calendars: Vec<Calendar>,
}

pub enum Fetch {
    Fresh(State),
    /// The source exists in the config but could not be reached.
    Unavailable(String),
    NotConfigured,
}

pub fn fetch(loaded: &Loaded, locale: &str) -> Fetch {
    let cfg: &CalendarConfig = &loaded.config.calendar;
    if let Some(file) = &cfg.state_file {
        let path = if file.is_absolute() { file.clone() } else { loaded.skill_dir.join(file) };
        return match std::fs::read(&path) {
            Ok(raw) => match serde_json::from_slice::<Value>(&raw) {
                Ok(doc) => Fetch::Fresh(parse(&doc, crate::mail::fingerprint(&path).unwrap_or_default(), locale)),
                Err(e) => Fetch::Unavailable(format!("{}: {e}", path.display())),
            },
            Err(e) => Fetch::Unavailable(format!("{}: {e}", path.display())),
        };
    }
    let Some(server) = &cfg.server else { return Fetch::NotConfigured };
    let url = format!("{}/v1/state", server.trim_end_matches('/'));
    let token = loaded.calendar_token();
    match crate::http::get(&url, token.as_deref(), Duration::from_secs(cfg.timeout_secs.max(1))) {
        Ok((200, body)) => match serde_json::from_slice::<Value>(&body) {
            Ok(doc) => {
                let seq = doc.get("seq").and_then(Value::as_i64).unwrap_or(0);
                Fetch::Fresh(parse(&doc, format!("seq:{seq}"), locale))
            }
            Err(e) => Fetch::Unavailable(format!("{url}: bad JSON: {e}")),
        },
        Ok((status, _)) => Fetch::Unavailable(format!("{url}: HTTP {status}")),
        Err(e) => Fetch::Unavailable(e),
    }
}

fn parse(doc: &Value, fingerprint: String, locale: &str) -> State {
    let state = doc.get("state").unwrap_or(doc);
    let alt = if locale == "cn" { "en" } else { "cn" };
    let mut events: Vec<Event> = state
        .get("events")
        .and_then(Value::as_object)
        .map(|m| m.values().map(|e| event(e, locale, alt)).collect())
        .unwrap_or_default();
    events.sort_by(|a, b| a.start_ts.cmp(&b.start_ts).then(a.id.cmp(&b.id)));
    let mut calendars: Vec<Calendar> = state
        .get("calendars")
        .and_then(Value::as_object)
        .map(|m| {
            m.iter()
                .map(|(id, c)| Calendar {
                    id: id.clone(),
                    name: localized(c.get("name"), locale),
                    name_alt: localized(c.get("name"), alt),
                    color: str_of(c, "color"),
                    visible: c.get("visible").and_then(Value::as_bool).unwrap_or(true),
                    shared_with: c
                        .get("shared_with")
                        .and_then(Value::as_array)
                        .map(|a| a.iter().filter_map(Value::as_str).map(str::to_string).collect())
                        .unwrap_or_default(),
                })
                .collect()
        })
        .unwrap_or_default();
    calendars.sort_by(|a, b| a.id.cmp(&b.id));
    State { fingerprint, events, calendars }
}

fn event(e: &Value, locale: &str, alt: &str) -> Event {
    let start = str_of(e, "start");
    let end = str_of(e, "end");
    let all_day = e.get("all_day").and_then(Value::as_bool).unwrap_or(false);
    let (first_day, last_day) = days(&start, &end, all_day);
    Event {
        id: str_of(e, "id"),
        calendar: str_of(e, "calendar"),
        start_ts: epoch(&start),
        end_ts: epoch(&end),
        start,
        end,
        first_day,
        last_day,
        all_day,
        title: localized(e.get("title"), locale),
        title_alt: localized(e.get("title"), alt),
        location: localized(e.get("location"), locale),
        location_alt: localized(e.get("location"), alt),
        notes: str_of(e, "notes"),
        deleted: e.get("deleted").and_then(Value::as_bool).unwrap_or(false),
        invitation: e
            .get("invitation")
            .map(|v| match v {
                Value::String(s) => s.clone(),
                Value::Null => String::new(),
                other => other.to_string(),
            })
            .unwrap_or_default(),
        created_by: str_of(e, "created_by"),
    }
}

/// Inclusive wall-clock day span. All-day ends are exclusive in the app's
/// model (`end` = the morning after), as is a timed event ending exactly at
/// midnight, so those pull the last day back by one.
pub fn days(start: &str, end: &str, all_day: bool) -> (String, String) {
    let first = start.chars().take(10).collect::<String>();
    let end_day = end.chars().take(10).collect::<String>();
    let ends_at_midnight = all_day || end.get(11..16).map(|t| t == "00:00").unwrap_or(true);
    let last = match (
        chrono::NaiveDate::parse_from_str(&first, "%Y-%m-%d"),
        chrono::NaiveDate::parse_from_str(&end_day, "%Y-%m-%d"),
    ) {
        (Ok(a), Ok(b)) if ends_at_midnight && b > a => (b - chrono::Days::new(1)).format("%Y-%m-%d").to_string(),
        (Ok(a), Ok(b)) if b < a => a.format("%Y-%m-%d").to_string(),
        (Ok(_), Ok(_)) => end_day,
        _ => first.clone(),
    };
    (first, last)
}

/// Bilingual fields are `{"en": …, "cn": …}`; plain strings pass through.
fn localized(v: Option<&Value>, locale: &str) -> String {
    match v {
        Some(Value::String(s)) => s.clone(),
        Some(Value::Object(m)) => m
            .get(locale)
            .and_then(Value::as_str)
            .filter(|s| !s.trim().is_empty())
            .or_else(|| m.values().filter_map(Value::as_str).find(|s| !s.trim().is_empty()))
            .unwrap_or("")
            .to_string(),
        _ => String::new(),
    }
}

fn str_of(v: &Value, key: &str) -> String {
    v.get(key).and_then(Value::as_str).unwrap_or("").to_string()
}

#[cfg(test)]
mod tests {
    use super::days;

    #[test]
    fn should_span_wall_clock_days_in_the_events_own_offset() {
        assert_eq!(days("2026-09-24T10:30:00+08:00", "2026-09-24T11:15:00+08:00", false), ("2026-09-24".into(), "2026-09-24".into()));
        assert_eq!(days("2026-10-01", "2026-10-02", true), ("2026-10-01".into(), "2026-10-01".into()));
        assert_eq!(days("2026-10-01", "2026-10-04", true), ("2026-10-01".into(), "2026-10-03".into()));
        assert_eq!(days("2026-09-24T22:00:00+08:00", "2026-09-25T00:00:00+08:00", false), ("2026-09-24".into(), "2026-09-24".into()));
        assert_eq!(days("2026-09-24T22:00:00+08:00", "2026-09-25T01:00:00+08:00", false), ("2026-09-24".into(), "2026-09-25".into()));
    }
}
