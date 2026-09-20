//! What a store shows about an app, as the publisher wrote it.
//!
//! The manifest says what an app may DO and is the security-relevant file.
//! The listing says what an app IS: description, category, screenshots,
//! who publishes it, where it runs. It is reviewed like everything else in
//! the bundle, and the store shows it beside the permissions, never instead
//! of them. What the store says an app may do always comes from the resolved
//! manifest; the listing cannot claim otherwise.
use crate::manifest::AppManifest;
use serde::{Deserialize, Serialize};

pub const LISTING_FILE: &str = "listing.json";
pub const LISTING_SCHEMA: u32 = 1;

pub const MAX_SUBTITLE: usize = 80;
pub const MAX_DESCRIPTION: usize = 4000;
pub const MAX_KEYWORDS: usize = 10;
pub const MAX_SCREENSHOTS: usize = 8;

/// The categories a store sorts by. Closed, so search and shelves agree.
pub const CATEGORIES: &[&str] = &[
    "productivity", "utilities", "photo-video", "news", "weather", "travel", "finance", "health", "education",
    "entertainment", "games", "social", "shopping", "lifestyle", "developer",
];

/// Where a card app can run: every shell that links the card host. A
/// publisher lists what they tested; the store shows it as-is.
pub const PLATFORMS: &[&str] = &["android", "ios", "macos", "windows", "linux", "openharmony", "web"];

/// Age ratings a listing may declare, coarse on purpose.
pub const AGE_RATINGS: &[&str] = &["all", "12+", "16+", "18+"];

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
#[serde(deny_unknown_fields)]
pub struct Listing {
    pub schema: u32,
    /// One line under the name.
    #[serde(default)]
    pub subtitle: String,
    /// What the app does, for a person deciding whether to install it.
    pub description: String,
    pub category: String,
    #[serde(default)]
    pub keywords: Vec<String>,
    /// Bundle-relative paths to PNG screenshots, in display order.
    #[serde(default)]
    pub screenshots: Vec<String>,
    /// Bundle-relative path to a square PNG or SVG icon.
    #[serde(default)]
    pub icon: Option<String>,
    pub platforms: Vec<String>,
    pub publisher: Publisher,
    /// What changed in this version, shown as "what's new".
    #[serde(default)]
    pub release_notes: String,
    pub age_rating: String,
    /// An SPDX licence identifier, when the source is open.
    #[serde(default)]
    pub license: Option<String>,
}

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
#[serde(deny_unknown_fields)]
pub struct Publisher {
    /// The person or organisation as a person reads it.
    pub name: String,
    /// Where a person gets help: a URL or an email address.
    pub support: String,
    /// Required, as it is on every store: where the app's privacy terms live.
    pub privacy_policy_url: String,
}

impl Listing {
    pub fn parse(json: &str) -> Result<Self, String> {
        let listing: Listing = serde_json::from_str(json).map_err(|e| format!("listing is not valid: {e}"))?;
        if listing.schema != LISTING_SCHEMA {
            return Err(format!("listing schema {} is not {}", listing.schema, LISTING_SCHEMA));
        }
        listing.check()?;
        Ok(listing)
    }

    /// The rules a listing must meet, in words a publisher can act on.
    pub fn check(&self) -> Result<(), String> {
        if self.description.trim().is_empty() {
            return Err("listing description is empty".into());
        }
        if self.description.chars().count() > MAX_DESCRIPTION {
            return Err(format!("listing description is over {MAX_DESCRIPTION} characters"));
        }
        if self.subtitle.chars().count() > MAX_SUBTITLE {
            return Err(format!("listing subtitle is over {MAX_SUBTITLE} characters"));
        }
        if !CATEGORIES.contains(&self.category.as_str()) {
            return Err(format!("listing category {:?} is not one of {:?}", self.category, CATEGORIES));
        }
        if self.keywords.len() > MAX_KEYWORDS {
            return Err(format!("listing has more than {MAX_KEYWORDS} keywords"));
        }
        if self.screenshots.len() > MAX_SCREENSHOTS {
            return Err(format!("listing has more than {MAX_SCREENSHOTS} screenshots"));
        }
        if self.platforms.is_empty() {
            return Err("listing names no platforms".into());
        }
        for platform in &self.platforms {
            if !PLATFORMS.contains(&platform.as_str()) {
                return Err(format!("listing platform {platform:?} is not one of {:?}", PLATFORMS));
            }
        }
        if !AGE_RATINGS.contains(&self.age_rating.as_str()) {
            return Err(format!("listing age rating {:?} is not one of {:?}", self.age_rating, AGE_RATINGS));
        }
        if self.publisher.name.trim().is_empty() {
            return Err("listing publisher name is empty".into());
        }
        if self.publisher.support.trim().is_empty() {
            return Err("listing publisher support (a URL or an email) is empty".into());
        }
        if !self.publisher.privacy_policy_url.starts_with("https://") {
            return Err("listing privacy policy must be an https URL".into());
        }
        for path in self.screenshots.iter().chain(self.icon.iter()) {
            if path.starts_with('/') || path.contains("..") || path.contains("://") {
                return Err(format!("listing asset {path:?} must be a plain bundle-relative path"));
            }
            let lower = path.to_ascii_lowercase();
            if !(lower.ends_with(".png") || lower.ends_with(".svg")) {
                return Err(format!("listing asset {path:?} must be a PNG or SVG"));
            }
        }
        Ok(())
    }
}

/// The privacy summary a store shows, derived from the manifest rather than
/// written by the publisher: the app cannot understate what it does.
pub fn privacy_summary(manifest: &AppManifest) -> Vec<String> {
    let has = |c: &str| manifest.capabilities.iter().any(|x| x == c);
    let mut lines = Vec::new();
    if has("storage") {
        lines.push("Keeps its own data on this device, in a space only it can read.".to_string());
    } else {
        lines.push("Stores nothing.".to_string());
    }
    if has("net") && !manifest.network.hosts.is_empty() {
        lines.push(format!("Contacts only: {}.", manifest.network.hosts.join(", ")));
    } else {
        lines.push("Never contacts the network.".to_string());
    }
    if has("ledger.read") {
        lines.push("Reads your shared data.".to_string());
    }
    for (cap, text) in [("location", "Uses your location."), ("camera", "Uses the camera."), ("clipboard", "Uses the clipboard."), ("prompt", "May ask you questions.")] {
        if has(cap) {
            lines.push(text.to_string());
        }
    }
    match &manifest.agent {
        Some(agent) => lines.push(format!(
            "Runs an assistant limited to this app's own data{}.",
            if agent.tools.is_empty() { String::new() } else { format!(" with {}", agent.tools.join(", ")) }
        )),
        None => lines.push("Runs no assistant.".to_string()),
    }
    lines
}

#[cfg(test)]
mod tests {
    use super::*;

    fn good() -> String {
        r#"{"schema":1,"subtitle":"The photo-mode screen","description":"A camera viewfinder.","category":"photo-video",
            "keywords":["camera"],"screenshots":["screenshots/01.png"],"platforms":["android","macos"],
            "publisher":{"name":"ymote","support":"https://github.com/ymote/camera-card/issues","privacy_policy_url":"https://example.com/privacy"},
            "release_notes":"First release.","age_rating":"all","license":"Apache-2.0"}"#
            .to_string()
    }

    #[test]
    fn a_complete_listing_parses() {
        let listing = Listing::parse(&good()).unwrap();
        assert_eq!(listing.category, "photo-video");
        assert_eq!(listing.platforms.len(), 2);
    }

    #[test]
    fn the_closed_lists_are_enforced() {
        assert!(Listing::parse(&good().replace("photo-video", "toys")).unwrap_err().contains("category"));
        assert!(Listing::parse(&good().replace("\"android\"", "\"symbian\"")).unwrap_err().contains("platform"));
        assert!(Listing::parse(&good().replace("\"all\"", "\"any\"")).unwrap_err().contains("age rating"));
    }

    #[test]
    fn a_privacy_policy_must_be_https_and_assets_must_stay_in_the_bundle() {
        assert!(Listing::parse(&good().replace("https://example.com/privacy", "http://example.com/privacy")).unwrap_err().contains("https"));
        assert!(Listing::parse(&good().replace("screenshots/01.png", "../01.png")).unwrap_err().contains("bundle-relative"));
        assert!(Listing::parse(&good().replace("screenshots/01.png", "screenshots/01.gif")).unwrap_err().contains("PNG or SVG"));
    }

    #[test]
    fn unknown_fields_are_refused() {
        assert!(Listing::parse(&good().replace("\"license\"", "\"price\":0,\"license\"")).unwrap_err().contains("not valid"));
    }

    #[test]
    fn the_privacy_summary_comes_from_the_manifest_not_the_listing() {
        let m = AppManifest::parse(r#"{"schema":1,"id":"a","version":"1","name":"A","integrity":{"bundle_blake3":"00"},
            "capabilities":["storage","net","camera"],"network":{"hosts":["api.example"]}}"#).unwrap();
        let lines = privacy_summary(&m);
        assert!(lines.iter().any(|l| l.contains("api.example")));
        assert!(lines.iter().any(|l| l.contains("camera")));
        assert!(lines.iter().any(|l| l.contains("no assistant")));
        let quiet = AppManifest::parse(r#"{"schema":1,"id":"a","version":"1","name":"A","integrity":{"bundle_blake3":"00"}}"#).unwrap();
        let lines = privacy_summary(&quiet);
        assert!(lines.contains(&"Stores nothing.".to_string()));
        assert!(lines.contains(&"Never contacts the network.".to_string()));
    }
}
