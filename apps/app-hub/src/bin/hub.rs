//! `hub` — the command the publisher and the hub both run.
//!
//! ```sh
//! hub keygen <path>                       # a signing key (anchor or working)
//! hub certify --anchor <key> --working <key>
//! hub stamp <bundle>                      # write the bundle digest into its manifest
//! hub sign-manifest <bundle> --key <key> --key-id <id>
//! hub check <bundle> [--catalog <file>] [--allow-unsigned] [--publisher-key id=hex]
//! hub publish <bundle> --catalog <file> --key <working> --anchor-cert <hex>
//!             --publisher <id> --repo <url> --commit <sha> [--out <dir>]
//! hub verify <catalog> --anchor <hex>
//! ```
//!
//! `check` is the gate: a developer runs it before submitting and sees the
//! same report the hub's job produces. `publish` runs the gate again, copies
//! the bundle into the artifact store and signs the catalog.
use octosense_app_hub::*;
use octosense_app_hub::scan::Route;
use octosense_app_policy::{AppManifest, HostLimits};
use std::path::{Path, PathBuf};

fn main() {
    if let Err(e) = run() {
        eprintln!("hub: {e}");
        std::process::exit(1);
    }
}

fn run() -> Result<(), String> {
    let argv: Vec<String> = std::env::args().collect();
    let command = argv.get(1).map(String::as_str).unwrap_or("help");
    let flag = |name: &str| argv.windows(2).find(|w| w[0] == format!("--{name}")).map(|w| w[1].clone());
    let has = |name: &str| argv.iter().any(|a| a == &format!("--{name}"));
    let positional = argv.get(2).cloned();

    match command {
        "keygen" => {
            let path = positional.ok_or("usage: hub keygen <path>")?;
            let key = HubKey::generate();
            std::fs::write(&path, hex::encode(key.to_bytes())).map_err(|e| e.to_string())?;
            println!("{}", key.public_hex());
            Ok(())
        }
        "pubkey" => {
            let key = load_key(&positional.ok_or("usage: hub pubkey <key file>")?)?;
            println!("{}", key.public_hex());
            Ok(())
        }
        "certify" => {
            let anchor = load_key(&flag("anchor").ok_or("--anchor <key file>")?)?;
            let working = load_key(&flag("working").ok_or("--working <key file>")?)?;
            println!("{}", anchor.certify(&working.public_hex())?);
            Ok(())
        }
        "stamp" => {
            let bundle = PathBuf::from(positional.ok_or("usage: hub stamp <bundle>")?);
            let digest = octosense_app_policy::digest_dir(&bundle)?;
            let path = bundle.join(octosense_app_policy::MANIFEST_FILE);
            let text = std::fs::read_to_string(&path).map_err(|e| e.to_string())?;
            let mut value: serde_json::Value = serde_json::from_str(&text).map_err(|e| e.to_string())?;
            value["integrity"]["bundle_blake3"] = serde_json::Value::String(digest.clone());
            write_json(&path, &value)?;
            println!("{digest}");
            Ok(())
        }
        "sign-manifest" => {
            let bundle = PathBuf::from(positional.ok_or("usage: hub sign-manifest <bundle> --key <f> --key-id <id>")?);
            let key = load_key(&flag("key").ok_or("--key <key file>")?)?;
            let key_id = flag("key-id").ok_or("--key-id <id>")?;
            let path = bundle.join(octosense_app_policy::MANIFEST_FILE);
            let mut manifest = AppManifest::parse(&std::fs::read_to_string(&path).map_err(|e| e.to_string())?)?;
            sign_manifest(&key, &mut manifest, &key_id)?;
            write_json(&path, &serde_json::to_value(&manifest).map_err(|e| e.to_string())?)?;
            println!("signed {} {} with {key_id}", manifest.id, manifest.version);
            Ok(())
        }
        "check" => {
            let bundle = PathBuf::from(positional.ok_or("usage: hub check <bundle>")?);
            let report = gate_for(&bundle, &argv, has("allow-unsigned"), flag("catalog"))?;
            print!("{}", report.render());
            if report.passed() {
                Ok(())
            } else {
                Err("the bundle was refused".into())
            }
        }
        "publish" => {
            let bundle = PathBuf::from(positional.ok_or("usage: hub publish <bundle> --catalog <file> …")?);
            let catalog_path = PathBuf::from(flag("catalog").ok_or("--catalog <file>")?);
            let report = gate_for(&bundle, &argv, has("allow-unsigned"), Some(catalog_path.to_string_lossy().into()))?;
            print!("{}", report.render());
            if !report.passed() {
                return Err("refusing to publish a bundle the gate refused".into());
            }
            let working = load_key(&flag("key").ok_or("--key <working key file>")?)?;
            let anchor_certificate = flag("anchor-cert").ok_or("--anchor-cert <hex>")?;
            let publisher = flag("publisher").ok_or("--publisher <id>")?;
            let repository = flag("repo").unwrap_or_default();
            let commit = flag("commit").unwrap_or_default();
            let out = PathBuf::from(flag("out").unwrap_or_else(|| ".".into()));

            let mut catalog = read_catalog(&catalog_path).unwrap_or_else(|_| Catalog::new(0, &today(), Vec::new()));
            // The publisher's public key travels in the signed catalog, so a
            // device can check their signature without asking the hub again.
            let publisher_key = argv
                .windows(2)
                .filter(|w| w[0] == "--publisher-key")
                .filter_map(|w| w[1].split_once('=').map(|(id, key)| (id.to_string(), key.to_string())))
                .find(|(id, _)| id == &publisher)
                .map(|(_, key)| key)
                .unwrap_or_default();
            let entry = entry_for(&bundle, &report, &publisher, &publisher_key, &repository, &commit, &today())?;
            // The artifact store keeps its own copy: review binds to bytes.
            let artifact = out.join(&entry.artifact);
            if let Some(parent) = artifact.parent() {
                std::fs::create_dir_all(parent).map_err(|e| e.to_string())?;
            }
            copy_tree(&bundle, &artifact)?;
            // The same bytes as one file, for devices that fetch over HTTP.
            let pack = pack_dir(&bundle)?;
            let pack_path = out.join(format!("{}.pack.json", entry.artifact));
            std::fs::write(&pack_path, serde_json::to_string(&pack).map_err(|e| e.to_string())?).map_err(|e| e.to_string())?;
            // Stage two, when a reviewer is configured: judgement on top of
            // the facts. A reject stops the publish; human-review stops it
            // too, until a person re-runs with --reviewed.
            if let Some(reviewer) = flag("reviewer") {
                let packet = packet(&bundle, &report)?;
                let verdict = scan(&packet, &reviewer);
                println!("  scan: {:?} — {}", verdict.route, verdict.reasons.join("; "));
                match verdict.route {
                    Route::Pass => {}
                    Route::Reject => return Err("the scan rejected this bundle".into()),
                    Route::HumanReview if has("reviewed") => println!("  scan: human review recorded by --reviewed"),
                    Route::HumanReview => return Err("the scan asks for human review; publish again with --reviewed once a person has looked".into()),
                }
            }
            catalog.entries.push(entry);
            catalog.sequence += 1;
            catalog.published = today();
            working.sign_catalog(&mut catalog, &anchor_certificate)?;
            write_json(&catalog_path, &serde_json::to_value(&catalog).map_err(|e| e.to_string())?)?;
            println!("published {} {} (catalog sequence {})", report.app_id, report.version, catalog.sequence);
            Ok(())
        }
        "withdraw" => {
            let app_id = positional.ok_or("usage: hub withdraw <app id> --version <v> --reason <text> --catalog <f> --key <f> --anchor-cert <hex>")?;
            let version = flag("version").ok_or("--version <v>")?;
            let reason = flag("reason").ok_or("--reason <text shown to the person>")?;
            let catalog_path = PathBuf::from(flag("catalog").ok_or("--catalog <file>")?);
            let working = load_key(&flag("key").ok_or("--key <working key file>")?)?;
            let anchor_certificate = flag("anchor-cert").ok_or("--anchor-cert <hex>")?;
            let mut catalog = read_catalog(&catalog_path)?;
            let entry = catalog
                .entries
                .iter_mut()
                .find(|e| e.app_id() == app_id && e.version() == version)
                .ok_or_else(|| format!("{app_id} {version} is not in the catalog"))?;
            entry.status = Status::Withdrawn(reason.clone());
            catalog.sequence += 1;
            catalog.published = today();
            working.sign_catalog(&mut catalog, &anchor_certificate)?;
            write_json(&catalog_path, &serde_json::to_value(&catalog).map_err(|e| e.to_string())?)?;
            println!("withdrew {app_id} {version}: {reason} (catalog sequence {})", catalog.sequence);
            Ok(())
        }
        "scan" => {
            let bundle = PathBuf::from(positional.ok_or("usage: hub scan <bundle> [--reviewer <cmd>] [--packet <out.json>]")?);
            let report = gate_for(&bundle, &argv, true, flag("catalog"))?;
            if !report.passed() {
                print!("{}", report.render());
                return Err("the gate refused this bundle; a scan is not offered".into());
            }
            let packet = packet(&bundle, &report)?;
            if let Some(path) = flag("packet") {
                write_json(Path::new(&path), &serde_json::to_value(&packet).map_err(|e| e.to_string())?)?;
                println!("wrote the review packet to {path}");
            }
            match flag("reviewer") {
                Some(reviewer) => {
                    let verdict = scan(&packet, &reviewer);
                    println!("{}", serde_json::to_string_pretty(&verdict).map_err(|e| e.to_string())?);
                    if verdict.route == Route::Reject {
                        return Err("rejected".into());
                    }
                    Ok(())
                }
                None => {
                    println!("no --reviewer given; the packet holds {} questions for one", packet.questions.len());
                    Ok(())
                }
            }
        }
        "verify" => {
            let catalog = read_catalog(Path::new(&positional.ok_or("usage: hub verify <catalog> --anchor <hex>")?))?;
            let anchor = flag("anchor").ok_or("--anchor <hex public key>")?;
            verify_catalog(&catalog, &anchor)?;
            println!("catalog sequence {} verified, {} entries", catalog.sequence, catalog.entries.len());
            Ok(())
        }
        _ => {
            println!("{}", include_str!("hub-usage.txt"));
            Ok(())
        }
    }
}

fn gate_for(bundle: &Path, argv: &[String], allow_unsigned: bool, catalog: Option<String>) -> Result<GateReport, String> {
    let mut keys = PublisherKeys::new();
    for pair in argv.windows(2).filter(|w| w[0] == "--publisher-key").map(|w| w[1].clone()) {
        let (id, public) = pair.split_once('=').ok_or("--publisher-key expects id=hexkey")?;
        keys = keys.with(id, public);
    }
    let limits = HostLimits { require_signature: !allow_unsigned, ..HostLimits::default() };
    let previous = match catalog {
        Some(path) if Path::new(&path).exists() => Some(read_catalog(Path::new(&path))?),
        _ => None,
    };
    check_bundle(bundle, &limits, &keys, previous.as_ref())
}

fn load_key(path: &str) -> Result<HubKey, String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{path}: {e}"))?;
    let raw = hex::decode(text.trim()).map_err(|e| format!("{path}: not hex: {e}"))?;
    let bytes: [u8; 32] = raw.as_slice().try_into().map_err(|_| format!("{path}: not a 32-byte key"))?;
    Ok(HubKey::from_bytes(&bytes))
}

fn read_catalog(path: &Path) -> Result<Catalog, String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{}: {e}", path.display()))?;
    serde_json::from_str(&text).map_err(|e| format!("{}: {e}", path.display()))
}

fn write_json(path: &Path, value: &serde_json::Value) -> Result<(), String> {
    let text = serde_json::to_string_pretty(value).map_err(|e| e.to_string())?;
    std::fs::write(path, format!("{text}\n")).map_err(|e| format!("{}: {e}", path.display()))
}

fn copy_tree(from: &Path, to: &Path) -> Result<(), String> {
    std::fs::create_dir_all(to).map_err(|e| e.to_string())?;
    for entry in std::fs::read_dir(from).map_err(|e| e.to_string())? {
        let entry = entry.map_err(|e| e.to_string())?;
        let target = to.join(entry.file_name());
        if entry.file_type().map_err(|e| e.to_string())?.is_dir() {
            copy_tree(&entry.path(), &target)?;
        } else {
            std::fs::copy(entry.path(), &target).map_err(|e| e.to_string())?;
        }
    }
    Ok(())
}
