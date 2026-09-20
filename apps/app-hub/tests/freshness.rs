//! The device's offline rules (ADR 0003 §6): a stale catalog pauses installs
//! but never running apps, and an older catalog can never replace a newer
//! one, so a replayed catalog cannot undo a withdrawal.
use octosense_app_hub::*;
use std::path::Path;

#[test]
fn installs_pause_when_the_catalog_is_stale_but_a_fresh_one_is_fine() {
    let anchor = HubKey::generate();
    let working = HubKey::generate();
    let cert = anchor.certify(&working.public_hex()).unwrap();
    let mut catalog = Catalog::new(1, "2026-09-01", Vec::new());
    working.sign_catalog(&mut catalog, &cert).unwrap();
    let mut store = Store::new(
        &anchor.public_hex(),
        Path::new("/tmp/octosense-freshness-test"),
        octosense_app_policy::HostLimits::default(),
    );
    store.accept_catalog(&serde_json::to_string(&catalog).unwrap()).unwrap();
    assert!(store.installs_allowed("2026-09-10").is_ok(), "9 days old is within the window");
    let err = store.installs_allowed("2026-09-20").unwrap_err();
    assert!(err.contains("19 days old"), "{err}");

    let mut older = Catalog::new(0, "2026-08-01", Vec::new());
    working.sign_catalog(&mut older, &cert).unwrap();
    let err = store.accept_catalog(&serde_json::to_string(&older).unwrap()).unwrap_err();
    assert!(err.contains("older than the one held"), "{err}");
}

#[test]
fn a_catalog_signed_by_an_uncertified_working_key_is_refused() {
    let anchor = HubKey::generate();
    let rogue = HubKey::generate();
    let mut catalog = Catalog::new(1, "2026-09-01", Vec::new());
    // The rogue key certifies itself; the device trusts only the anchor.
    let self_cert = rogue.certify(&rogue.public_hex()).unwrap();
    rogue.sign_catalog(&mut catalog, &self_cert).unwrap();
    let mut store = Store::new(&anchor.public_hex(), Path::new("/tmp/octosense-rogue-test"), octosense_app_policy::HostLimits::default());
    let err = store.accept_catalog(&serde_json::to_string(&catalog).unwrap()).unwrap_err();
    assert!(err.contains("did not certify"), "{err}");
}
