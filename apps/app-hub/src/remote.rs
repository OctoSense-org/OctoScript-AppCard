//! Fetching a hub over HTTP, and the date the device compares against.
//!
//! The origin is not trusted: what comes back is verified against the anchor
//! before it is read, and a pack is unpacked and hashed before it reaches a
//! jail. So this module does the plain work of GET and nothing clever: no
//! caching headers to reason about, no partial trust.
use crate::pack::Pack;

/// A hub reachable as `<base>/catalog.json` and `<base>/<artifact>.pack.json`.
pub struct Remote {
    base: String,
}

impl Remote {
    pub fn new(base: &str) -> Self {
        Remote { base: base.trim_end_matches('/').to_string() }
    }

    fn get(&self, path: &str) -> Result<String, String> {
        let url = format!("{}/{}", self.base, path.trim_start_matches('/'));
        let agent = ureq::Agent::config_builder()
            .timeout_global(Some(std::time::Duration::from_secs(30)))
            .build()
            .new_agent();
        let mut response = agent.get(&url).call().map_err(|e| format!("{url}: {e}"))?;
        response
            .body_mut()
            .with_config()
            .limit(64 * 1024 * 1024)
            .read_to_string()
            .map_err(|e| format!("{url}: {e}"))
    }

    /// The catalog's text, unverified.
    pub fn catalog(&self) -> Result<String, String> {
        self.get("catalog.json")
    }

    /// An artifact's pack, unverified.
    pub fn pack(&self, artifact: &str) -> Result<Pack, String> {
        let text = self.get(&format!("{artifact}.pack.json"))?;
        serde_json::from_str(&text).map_err(|e| format!("{artifact}: not a pack: {e}"))
    }
}

/// Today's date as `YYYY-MM-DD`, from the system clock. What the freshness
/// window and the admission record are measured against.
pub fn today() -> String {
    let secs = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_secs())
        .unwrap_or(0);
    let days = (secs / 86_400) as i64;
    // Civil-from-days (Howard Hinnant's algorithm), proleptic Gregorian.
    let z = days + 719_468;
    let era = z.div_euclid(146_097);
    let doe = z - era * 146_097;
    let yoe = (doe - doe / 1460 + doe / 36_524 - doe / 146_096) / 365;
    let y = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let d = doy - (153 * mp + 2) / 5 + 1;
    let m = if mp < 10 { mp + 3 } else { mp - 9 };
    let y = if m <= 2 { y + 1 } else { y };
    format!("{y:04}-{m:02}-{d:02}")
}

#[cfg(test)]
mod tests {
    #[test]
    fn today_is_a_plausible_iso_date() {
        let t = super::today();
        assert_eq!(t.len(), 10);
        assert!(t.starts_with("20"));
        assert_eq!(crate::client::days_between(&t, &t), Some(0));
    }

    #[test]
    fn days_between_counts_civil_days() {
        assert_eq!(crate::client::days_between("2026-09-01", "2026-09-20"), Some(19));
        assert_eq!(crate::client::days_between("2026-02-27", "2026-03-02"), Some(3));
        assert_eq!(crate::client::days_between("2026-09-20", "2026-09-01"), Some(0), "the future is not stale");
        assert_eq!(crate::client::days_between("garbage", "2026-09-20"), None);
    }
}
