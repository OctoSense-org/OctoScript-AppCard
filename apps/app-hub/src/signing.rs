//! Who signed what, and what a device checks.
//!
//! Three keys, deliberately unrelated (ADR 0003 §4): the ROM's update key,
//! the platform package key, and the hub anchor. Only the anchor appears
//! here. The anchor is offline and rarely used; it certifies the hub's
//! working key, which signs every catalog. A device trusts the anchor and
//! follows the certificate, so rotating the working key needs no release.
use crate::index::Catalog;
use ed25519_dalek::{Signature, Signer, SigningKey, Verifier, VerifyingKey};
use octosense_app_policy::{AppManifest, SignatureVerifier};

/// A signing key, for the hub's own jobs and for tests. Devices never hold one.
pub struct HubKey(SigningKey);

impl HubKey {
    pub fn generate() -> Self {
        // ed25519-dalek 3 wants its own rand_core version; take 32 bytes
        // from the OS and build the key from them, which is the same thing
        // `generate` does and avoids pinning two rand_core lines together.
        let mut seed = [0u8; 32];
        rand_core::TryRngCore::try_fill_bytes(&mut rand_core::OsRng, &mut seed).expect("the OS has no randomness");
        HubKey(SigningKey::from_bytes(&seed))
    }

    /// Load from 32 raw bytes, as stored by the release job.
    pub fn from_bytes(bytes: &[u8; 32]) -> Self {
        HubKey(SigningKey::from_bytes(bytes))
    }

    pub fn to_bytes(&self) -> [u8; 32] {
        self.0.to_bytes()
    }

    pub fn public_hex(&self) -> String {
        hex::encode(self.0.verifying_key().to_bytes())
    }

    pub fn sign_hex(&self, message: &[u8]) -> String {
        hex::encode(self.0.sign(message).to_bytes())
    }

    /// The anchor certifying a working key: a signature over its public bytes.
    pub fn certify(&self, working_public_hex: &str) -> Result<String, String> {
        let bytes = hex::decode(working_public_hex).map_err(|e| format!("working key is not hex: {e}"))?;
        Ok(self.sign_hex(&bytes))
    }

    /// Sign a catalog in place with this working key, recording the anchor's
    /// certificate so a device can follow the chain.
    pub fn sign_catalog(&self, catalog: &mut Catalog, anchor_certificate: &str) -> Result<(), String> {
        let bytes = catalog.signing_bytes()?;
        catalog.signature = Some(self.sign_hex(&bytes));
        catalog.key = Some(crate::index::WorkingKey {
            public: self.public_hex(),
            anchor_certificate: anchor_certificate.to_string(),
        });
        Ok(())
    }
}

fn verifying_key(hex_key: &str) -> Result<VerifyingKey, String> {
    let raw = hex::decode(hex_key).map_err(|e| format!("key is not hex: {e}"))?;
    let bytes: [u8; 32] = raw.as_slice().try_into().map_err(|_| "key is not 32 bytes".to_string())?;
    VerifyingKey::from_bytes(&bytes).map_err(|e| format!("key is not a valid ed25519 key: {e}"))
}

fn signature(hex_sig: &str) -> Result<Signature, String> {
    let raw = hex::decode(hex_sig).map_err(|e| format!("signature is not hex: {e}"))?;
    let bytes: [u8; 64] = raw.as_slice().try_into().map_err(|_| "signature is not 64 bytes".to_string())?;
    Ok(Signature::from_bytes(&bytes))
}

/// Verify a catalog against the anchor a device was shipped with.
///
/// Both links are checked: the anchor certified this working key, and that
/// working key signed these bytes. A catalog with no signature is refused —
/// there is no "unsigned but fine" case, because the catalog is also how
/// revocation travels.
pub fn verify_catalog(catalog: &Catalog, anchor_public_hex: &str) -> Result<(), String> {
    let key = catalog.key.as_ref().ok_or("catalog names no signing key")?;
    let signature_hex = catalog.signature.as_ref().ok_or("catalog is not signed")?;

    let anchor = verifying_key(anchor_public_hex)?;
    let working_raw = hex::decode(&key.public).map_err(|e| format!("working key is not hex: {e}"))?;
    anchor
        .verify(&working_raw, &signature(&key.anchor_certificate)?)
        .map_err(|_| "the anchor did not certify this working key".to_string())?;

    let working = verifying_key(&key.public)?;
    let bytes = catalog.signing_bytes()?;
    working
        .verify(&bytes, &signature(signature_hex)?)
        .map_err(|_| "the catalog's signature does not match its contents".to_string())?;
    Ok(())
}

/// Verifies a publisher's signature over a manifest. Registered publishers
/// are looked up by the key identity the manifest names, so an app cannot
/// introduce a key the hub has not recorded.
pub struct PublisherKeys {
    keys: Vec<(String, String)>,
}

impl PublisherKeys {
    pub fn new() -> Self {
        PublisherKeys { keys: Vec::new() }
    }

    pub fn with(mut self, key_id: &str, public_hex: &str) -> Self {
        self.keys.push((key_id.to_string(), public_hex.to_string()));
        self
    }
}

impl Default for PublisherKeys {
    fn default() -> Self {
        Self::new()
    }
}

impl SignatureVerifier for PublisherKeys {
    fn verify(&self, key_id: &str, signature_hex: &str, signed_bytes: &[u8]) -> Result<(), String> {
        let (_, public) = self
            .keys
            .iter()
            .find(|(id, _)| id == key_id)
            .ok_or_else(|| format!("publisher key {key_id:?} is not registered with this hub"))?;
        verifying_key(public)?
            .verify(signed_bytes, &signature(signature_hex)?)
            .map_err(|_| format!("the signature from key {key_id:?} does not match the manifest"))
    }
}

/// Sign a manifest as a publisher would, for tests and for the signing tool.
pub fn sign_manifest(key: &HubKey, manifest: &mut AppManifest, key_id: &str) -> Result<(), String> {
    manifest.integrity.signature = None;
    let bytes = manifest.signing_bytes()?;
    manifest.integrity.signature = Some(octosense_app_policy::manifest::Signature {
        key_id: key_id.to_string(),
        value: key.sign_hex(&bytes),
    });
    Ok(())
}
