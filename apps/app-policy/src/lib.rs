//! ADR 0002 phase 1: one declaration, two containers.
//!
//! An app that arrives after the build ships a bundle and a manifest. This
//! crate is the only thing that turns that manifest into what the app gets:
//! the settings for its splash isolate, and the profile for its octos agent
//! session. Both come from the same resolved [`AppPolicy`], so the app and
//! its agent can never have different reach.
//!
//! The order is always: [`AppManifest::parse`] → [`verify::admit`] →
//! [`policy::resolve`] → [`AppPolicy::isolate_settings`] and
//! [`AppPolicy::session_profile`]. Skipping a step is the bug this crate
//! exists to make hard.
//!
//! ```
//! use octosense_app_policy::{admit_and_resolve, HostLimits, RefuseAllSignatures};
//! let bundle = b"the card bundle bytes";
//! let manifest = format!(
//!     r#"{{"schema":1,"id":"weather","version":"1.0.0","name":"Weather",
//!         "integrity":{{"bundle_blake3":"{}"}},
//!         "capabilities":["storage","net"],
//!         "network":{{"hosts":["api.weather.example"]}}}}"#,
//!     octosense_app_policy::bundle_digest(bundle)
//! );
//! let limits = HostLimits { require_signature: false, ..HostLimits::default() };
//! let policy = admit_and_resolve(&manifest, bundle, &limits, &RefuseAllSignatures).unwrap();
//! assert!(policy.allows_host("api.weather.example"));
//! assert!(!policy.allows_host("example.com"));
//! assert!(policy.agent.is_none(), "an app gets no agent unless it asks");
//! ```
pub mod assets;
pub mod bundle;
pub mod containers;
pub mod listing;
#[cfg(feature = "splash")]
pub mod splash_adapter;
pub mod manifest;
pub mod policy;
pub mod verify;

pub use assets::{rewrite_assets, AssetServer};
pub use bundle::{digest_dir, MANIFEST_FILE};
pub use containers::{IsolateSettings, Provenance, SessionProfile};
pub use listing::{privacy_summary, Listing, Publisher, LISTING_FILE};
pub use manifest::{AgentSpec, AppManifest, ProfileMode, KNOWN_CAPABILITIES, SCHEMA};
pub use policy::{AgentPolicy, AppPolicy, HostLimits};
pub use verify::{admit, admit_digest, bundle_digest, RefuseAllSignatures, SignatureVerifier};

/// The whole admission path for a bundle that is a directory: parse, check
/// the digest the caller computed over that directory, resolve.
pub fn admit_and_resolve_dir(
    manifest_json: &str,
    bundle_digest_hex: &str,
    limits: &HostLimits,
    verifier: &dyn SignatureVerifier,
) -> Result<AppPolicy, String> {
    let manifest = AppManifest::parse(manifest_json)?;
    verify::admit_digest(&manifest, bundle_digest_hex, verifier)?;
    policy::resolve(&manifest, limits)
}

/// The whole admission path in one call: parse, admit, resolve. A host that
/// uses this cannot forget the digest check.
pub fn admit_and_resolve(
    manifest_json: &str,
    bundle: &[u8],
    limits: &HostLimits,
    verifier: &dyn SignatureVerifier,
) -> Result<AppPolicy, String> {
    let manifest = AppManifest::parse(manifest_json)?;
    verify::admit(&manifest, bundle, verifier)?;
    policy::resolve(&manifest, limits)
}
