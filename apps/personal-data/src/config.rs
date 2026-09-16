//! Skill configuration.
//!
//! The kernel launches skill binaries with a filtered environment and the
//! session workspace as the working directory, so nothing here depends on env
//! vars or the cwd: the config file sits next to the binary
//! (`<skill dir>/config.json`) and so does the index (`<skill dir>/state/`).
//! `PERSONAL_DATA_CONFIG` overrides the config path for tests and manual runs.

use std::path::{Path, PathBuf};

use serde::Deserialize;

#[derive(Debug, Clone, Deserialize)]
#[serde(default)]
pub struct Config {
    /// Directory holding the SQLite index. Default `<skill dir>/state`.
    pub state_dir: Option<PathBuf>,
    /// Display locale for bilingual calendar fields (`en` or `cn`).
    pub locale: String,
    pub mail: MailConfig,
    pub calendar: CalendarConfig,
}

#[derive(Debug, Clone, Deserialize)]
#[serde(default)]
pub struct MailConfig {
    /// Directories that hold the Mail module's `mailbox-*.json` files.
    pub dirs: Vec<PathBuf>,
    /// Index message bodies (opt-in). Default indexes subject, sender, date
    /// and the app's preview line only; `mail_read` always reads the body live.
    pub index_bodies: bool,
}

#[derive(Debug, Clone, Deserialize)]
#[serde(default)]
pub struct CalendarConfig {
    /// Calendar sync server, e.g. `http://127.0.0.1:8190`.
    pub server: Option<String>,
    pub token: Option<String>,
    /// File containing the bearer token (preferred over `token`).
    pub token_file: Option<PathBuf>,
    /// Offline alternative: a `/v1/state` document on disk.
    pub state_file: Option<PathBuf>,
    /// Seconds to wait for the server before using the cached index.
    pub timeout_secs: u64,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            state_dir: None,
            locale: "en".into(),
            mail: MailConfig::default(),
            calendar: CalendarConfig::default(),
        }
    }
}

impl Default for MailConfig {
    fn default() -> Self {
        Self {
            dirs: default_mail_dirs(),
            index_bodies: false,
        }
    }
}

impl Default for CalendarConfig {
    fn default() -> Self {
        Self {
            server: None,
            token: None,
            token_file: None,
            state_file: None,
            timeout_secs: 2,
        }
    }
}

/// Where the Mail module keeps its private storage when no data dir is
/// provided by the platform (macOS desktop): `$TMPDIR/octosense-native-mail/mail`.
fn default_mail_dirs() -> Vec<PathBuf> {
    vec![std::env::temp_dir().join("octosense-native-mail").join("mail")]
}

pub struct Loaded {
    pub config: Config,
    pub skill_dir: PathBuf,
}

impl Loaded {
    pub fn load() -> Result<Self, String> {
        let path = match std::env::var_os("PERSONAL_DATA_CONFIG") {
            Some(p) => PathBuf::from(p),
            None => skill_dir()?.join("config.json"),
        };
        let skill_dir = path
            .parent()
            .map(Path::to_path_buf)
            .unwrap_or_else(|| PathBuf::from("."));
        let config = match std::fs::read_to_string(&path) {
            Ok(text) => serde_json::from_str(&text)
                .map_err(|e| format!("invalid config {}: {e}", path.display()))?,
            Err(_) => Config::default(),
        };
        Ok(Self { config, skill_dir })
    }

    pub fn state_dir(&self) -> PathBuf {
        self.config
            .state_dir
            .clone()
            .unwrap_or_else(|| self.skill_dir.join("state"))
    }

    pub fn calendar_token(&self) -> Option<String> {
        if let Some(file) = &self.config.calendar.token_file {
            let path = if file.is_absolute() {
                file.clone()
            } else {
                self.skill_dir.join(file)
            };
            if let Ok(t) = std::fs::read_to_string(path) {
                let t = t.trim().to_string();
                if !t.is_empty() {
                    return Some(t);
                }
            }
        }
        self.config.calendar.token.clone()
    }
}

fn skill_dir() -> Result<PathBuf, String> {
    let exe = std::env::current_exe().map_err(|e| format!("cannot locate skill binary: {e}"))?;
    Ok(exe
        .parent()
        .map(Path::to_path_buf)
        .unwrap_or_else(|| PathBuf::from(".")))
}
