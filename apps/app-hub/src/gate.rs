//! Stage one of admission: the checks a model never makes (ADR 0003 §5).
//!
//! Everything here is a fact about the bundle, decided by code, reported the
//! same way whether it runs on a developer's machine before submitting or in
//! the hub's job after. A finding is either a refusal or a warning; an agent
//! scan runs afterwards on what passes, and never overrides a refusal.
use crate::index::{Catalog, Entry};
use octosense_app_policy::{digest_dir, policy, AppManifest, AppPolicy, HostLimits, Listing, SignatureVerifier, LISTING_FILE};
use std::path::Path;

/// Everything a bundle may hold besides its manifest, by extension. A bundle
/// is cards, data and artwork; anything else is a refusal, so a publisher
/// cannot smuggle a payload the checks do not understand.
const ALLOWED_EXTENSIONS: &[&str] = &["card", "json", "l0", "octoscript", "svg", "png", "jpg", "jpeg", "webp", "ttf", "otf", "txt", "md"];

/// Ceiling for a whole bundle. Cards are text and artwork; a bundle bigger
/// than this is either shipping something it should not, or should be split.
pub const MAX_BUNDLE_BYTES: u64 = 8 * 1024 * 1024;

#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Severity {
    /// The bundle is not admitted.
    Refusal,
    /// Admitted, but the publisher and a reviewer should see it.
    Warning,
}

#[derive(Clone, Debug)]
pub struct Finding {
    pub severity: Severity,
    pub check: &'static str,
    pub detail: String,
}

impl Finding {
    fn refuse(check: &'static str, detail: impl Into<String>) -> Self {
        Finding { severity: Severity::Refusal, check, detail: detail.into() }
    }
    fn warn(check: &'static str, detail: impl Into<String>) -> Self {
        Finding { severity: Severity::Warning, check, detail: detail.into() }
    }
}

#[derive(Debug)]
pub struct GateReport {
    pub app_id: String,
    pub version: String,
    pub digest: String,
    pub findings: Vec<Finding>,
    /// What the app would actually get, when the gate passed.
    pub policy: Option<AppPolicy>,
}

impl GateReport {
    pub fn passed(&self) -> bool {
        !self.findings.iter().any(|f| f.severity == Severity::Refusal)
    }

    /// One line per finding, for a pull-request comment or a terminal.
    pub fn render(&self) -> String {
        let mut out = format!("{} {} — {}\n", self.app_id, self.version, if self.passed() { "PASSED" } else { "REFUSED" });
        for finding in &self.findings {
            let mark = match finding.severity {
                Severity::Refusal => "refused",
                Severity::Warning => "warning",
            };
            out.push_str(&format!("  [{mark}] {}: {}\n", finding.check, finding.detail));
        }
        if let Some(policy) = &self.policy {
            out.push_str(&format!(
                "  grants: capabilities {:?}, hosts {:?}, storage {} bytes, agent {}\n",
                policy.capabilities,
                policy.hosts,
                policy.storage_bytes,
                policy.agent.as_ref().map(|a| a.profile.as_kernel_mode()).unwrap_or("none")
            ));
        }
        out
    }
}

/// Run the deterministic gate over a bundle directory.
///
/// `previous` is the catalog the hub already published, used for the identity
/// rules: a version may not be republished, and once a publisher key is on
/// record every later version must carry it.
pub fn check_bundle(
    bundle: &Path,
    limits: &HostLimits,
    verifier: &dyn SignatureVerifier,
    previous: Option<&Catalog>,
) -> Result<GateReport, String> {
    let manifest_path = bundle.join(octosense_app_policy::MANIFEST_FILE);
    let manifest_json = std::fs::read_to_string(&manifest_path).map_err(|e| format!("{}: {e}", manifest_path.display()))?;
    let manifest = AppManifest::parse(&manifest_json)?;
    let digest = digest_dir(bundle)?;
    let mut findings = Vec::new();

    // ---- integrity ------------------------------------------------------
    if digest.to_ascii_lowercase() != manifest.integrity.bundle_blake3.to_ascii_lowercase() {
        findings.push(Finding::refuse(
            "digest",
            format!("the bundle hashes to {digest}, the manifest claims {}", manifest.integrity.bundle_blake3),
        ));
    }
    match &manifest.integrity.signature {
        Some(signature) => {
            if let Err(e) = verifier.verify(&signature.key_id, &signature.value, &manifest.signing_bytes()?) {
                findings.push(Finding::refuse("publisher-signature", e));
            }
        }
        None if limits.require_signature => {
            findings.push(Finding::refuse("publisher-signature", "this hub requires a signed manifest"))
        }
        None => findings.push(Finding::warn("publisher-signature", "unsigned: accountability rests on the hub alone")),
    }

    // ---- contents -------------------------------------------------------
    let mut total = 0u64;
    for file in list_files(bundle)? {
        let path = bundle.join(&file);
        let size = std::fs::metadata(&path).map_err(|e| e.to_string())?.len();
        total += size;
        let extension = file.extension().and_then(|e| e.to_str()).unwrap_or("").to_ascii_lowercase();
        if !ALLOWED_EXTENSIONS.contains(&extension.as_str()) {
            findings.push(Finding::refuse(
                "contents",
                format!("{} has extension {extension:?}, which a bundle may not hold", file.display()),
            ));
        }
    }
    if total > MAX_BUNDLE_BYTES {
        findings.push(Finding::refuse("size", format!("the bundle is {total} bytes, over the {MAX_BUNDLE_BYTES} ceiling")));
    }

    // ---- assets are local ----------------------------------------------
    // ADR 0002's prototype found a card with no network grant fetching nine
    // images over HTTP, because the resource loader is not the network module
    // the grant gates. Until that is closed in the runtime, the gate is what
    // keeps a bundle from reaching outside itself.
    for reference in external_references(bundle)? {
        findings.push(Finding::refuse(
            "assets",
            format!("{reference} points outside the bundle; ship the asset with the app"),
        ));
    }

    // ---- the listing ----------------------------------------------------
    // A store shows nothing it has not reviewed: the listing ships in the
    // bundle, under the same digest, and its assets must be there too.
    match std::fs::read_to_string(bundle.join(LISTING_FILE)) {
        Err(_) => findings.push(Finding::refuse("listing", format!("no {LISTING_FILE}: a store needs a description, a category, screenshots, a publisher and the platforms it runs on"))),
        Ok(text) => match Listing::parse(&text) {
            Err(e) => findings.push(Finding::refuse("listing", e)),
            Ok(listing) => {
                // A screenshot is the one listing claim a reviewer can check
                // against the rendered card, and the icon is what the
                // launcher shows once installed: both are required, as on
                // every store people know.
                if listing.screenshots.is_empty() {
                    findings.push(Finding::refuse("listing", "no screenshots: at least one PNG in the bundle, named in the listing, is required"));
                }
                if listing.icon.is_none() {
                    findings.push(Finding::refuse("listing", "no icon: a square PNG or SVG in the bundle, named in the listing, is required"));
                }
                for asset in listing.screenshots.iter().chain(listing.icon.iter()) {
                    if !bundle.join(asset).is_file() {
                        findings.push(Finding::refuse("listing", format!("{asset} is named by the listing but is not in the bundle")));
                    }
                }
            }
        },
    }

    // ---- what it would get ----------------------------------------------
    let policy = match policy::resolve(&manifest, limits) {
        Ok(policy) => Some(policy),
        Err(e) => {
            findings.push(Finding::refuse("policy", e));
            None
        }
    };

    // ---- identity against what is already published ----------------------
    if let Some(catalog) = previous {
        for entry in &catalog.entries {
            if entry.app_id() == manifest.id && entry.version() == manifest.version {
                findings.push(Finding::refuse(
                    "version",
                    format!("version {} of {} is already published; publish a new version", manifest.version, manifest.id),
                ));
            }
        }
        if let Some(previous_entry) = catalog.entries.iter().filter(|e| e.app_id() == manifest.id).next_back() {
            let declared = manifest.integrity.signature.as_ref().map(|s| s.key_id.as_str());
            match declared {
                Some(key_id) if key_id == previous_entry.publisher => {}
                Some(key_id) => findings.push(Finding::refuse(
                    "continuity",
                    format!(
                        "{} was published by {:?}; this version is signed by {:?}. Re-keying is a reviewed change.",
                        manifest.id, previous_entry.publisher, key_id
                    ),
                )),
                None => findings.push(Finding::refuse(
                    "continuity",
                    format!("{} is already published by {:?}; an update must carry that key", manifest.id, previous_entry.publisher),
                )),
            }
        }
    }

    Ok(GateReport { app_id: manifest.id, version: manifest.version, digest, findings, policy })
}

/// Every file in the bundle except the manifest, relative to its root.
fn list_files(root: &Path) -> Result<Vec<std::path::PathBuf>, String> {
    fn walk(root: &Path, dir: &Path, out: &mut Vec<std::path::PathBuf>) -> Result<(), String> {
        for entry in std::fs::read_dir(dir).map_err(|e| format!("{}: {e}", dir.display()))? {
            let entry = entry.map_err(|e| e.to_string())?;
            let path = entry.path();
            let kind = entry.file_type().map_err(|e| e.to_string())?;
            if kind.is_symlink() {
                return Err(format!("{}: a bundle may not hold a symlink", path.display()));
            }
            if kind.is_dir() {
                walk(root, &path, out)?;
            } else {
                let relative = path.strip_prefix(root).map_err(|e| e.to_string())?.to_path_buf();
                if relative != Path::new(octosense_app_policy::MANIFEST_FILE) {
                    out.push(relative);
                }
            }
        }
        Ok(())
    }
    let mut out = Vec::new();
    walk(root, root, &mut out)?;
    out.sort();
    Ok(out)
}

/// Anything in the bundle's text that reaches outside it: an absolute URL, or
/// a path that climbs out. Cards name their artwork in text, so this is a
/// textual check by necessity; it is a gate, not the runtime's enforcement.
fn external_references(root: &Path) -> Result<Vec<String>, String> {
    let mut found = Vec::new();
    for file in list_files(root)? {
        // The two metadata files carry URLs on purpose (a support page, a
        // privacy policy); nothing loads them. Their own asset paths are
        // checked by the listing rules.
        if file == Path::new(LISTING_FILE) || file == Path::new(octosense_app_policy::MANIFEST_FILE) {
            continue;
        }
        let extension = file.extension().and_then(|e| e.to_str()).unwrap_or("").to_ascii_lowercase();
        if !matches!(extension.as_str(), "card" | "json" | "l0" | "octoscript" | "txt" | "md") {
            continue;
        }
        let text = match std::fs::read_to_string(root.join(&file)) {
            Ok(text) => text,
            Err(_) => continue, // not valid text: the extension check already covers it
        };
        for needle in ["http://", "https://", "file://", "../"] {
            if let Some(at) = text.find(needle) {
                let snippet: String = text[at..].chars().take(60).collect();
                found.push(format!("{} contains {}", file.display(), snippet.replace('\n', " ")));
                break;
            }
        }
    }
    Ok(found)
}

/// Build the index entry for a bundle the gate passed.
#[allow(clippy::too_many_arguments)]
pub fn entry_for(
    bundle: &Path,
    report: &GateReport,
    publisher: &str,
    publisher_key: &str,
    repository: &str,
    commit: &str,
    admitted: &str,
) -> Result<Entry, String> {
    let manifest_json = std::fs::read_to_string(bundle.join(octosense_app_policy::MANIFEST_FILE)).map_err(|e| e.to_string())?;
    let manifest = AppManifest::parse(&manifest_json)?;
    let listing = std::fs::read_to_string(bundle.join(LISTING_FILE)).ok().and_then(|t| Listing::parse(&t).ok());
    Ok(Entry {
        artifact: format!("artifacts/{}-{}.bundle", report.app_id, report.version),
        manifest,
        listing,
        publisher: publisher.to_string(),
        publisher_key: publisher_key.to_string(),
        source: crate::index::Source { repository: repository.to_string(), commit: commit.to_string() },
        status: crate::index::Status::Offered,
        admitted: admitted.to_string(),
    })
}
