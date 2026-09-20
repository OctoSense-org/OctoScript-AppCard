//! Admitting a bundle: the hash always, the signature when the host asks.
//!
//! The digest is over the bundle bytes as shipped, so a card that changed
//! after signing is refused before anything of it is parsed. Signatures are
//! behind a trait because this tree has no signing key format yet: the ROM
//! signs packages and the kernel signs skills, and app bundles should reuse
//! one of those rather than invent a third. Until then a host that sets
//! `require_signature` and installs no verifier admits nothing, which is the
//! safe direction to be wrong in.
use crate::manifest::AppManifest;

/// Verifies a detached signature over the canonical manifest bytes.
pub trait SignatureVerifier {
    /// `key_id` names the key as the host knows it. Return an error with a
    /// reason; returning `Ok(())` admits the bundle.
    fn verify(&self, key_id: &str, signature_hex: &str, signed_bytes: &[u8]) -> Result<(), String>;
}

/// The default: refuses every signature. A host without a real verifier can
/// still run unsigned bundles by turning `require_signature` off, which is a
/// deliberate, visible choice rather than an accidental one.
pub struct RefuseAllSignatures;

impl SignatureVerifier for RefuseAllSignatures {
    fn verify(&self, key_id: &str, _signature_hex: &str, _signed_bytes: &[u8]) -> Result<(), String> {
        Err(format!("no signature verifier is installed, so the signature from key {key_id:?} cannot be checked"))
    }
}

/// Hex blake3 of the bundle bytes, as the manifest records it.
pub fn bundle_digest(bundle: &[u8]) -> String {
    blake3::hash(bundle).to_hex().to_string()
}

/// Check a manifest against the bundle it describes, and its signature if it
/// carries one. Hash first: a bundle whose bytes do not match is refused
/// whatever its signature claims.
pub fn admit(manifest: &AppManifest, bundle: &[u8], verifier: &dyn SignatureVerifier) -> Result<(), String> {
    admit_digest(manifest, &bundle_digest(bundle), verifier)
}

/// The same check for a bundle that is a directory, whose digest the caller
/// already computed with [`crate::bundle::digest_dir`]. Separate from
/// [`admit`] so a caller cannot pass a digest where bytes are expected and
/// silently hash the digest instead of the bundle.
pub fn admit_digest(manifest: &AppManifest, digest: &str, verifier: &dyn SignatureVerifier) -> Result<(), String> {
    let actual = digest.to_ascii_lowercase();
    let declared = manifest.integrity.bundle_blake3.to_ascii_lowercase();
    if actual != declared {
        return Err(format!(
            "bundle digest {actual} does not match the manifest's {declared}: app {} version {}",
            manifest.id, manifest.version
        ));
    }
    if let Some(signature) = &manifest.integrity.signature {
        let signed = manifest.signing_bytes()?;
        verifier.verify(&signature.key_id, &signature.value, &signed)?;
    }
    Ok(())
}
