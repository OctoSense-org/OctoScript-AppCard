"""Generate the isolated browser host's Cargo manifest from dependency paths."""
from pathlib import Path
import json


PACKAGE = "octosense-wizard"


def cargo_manifest(dependencies: dict[str, Path]) -> str:
    # JSON quoted strings are valid TOML basic strings, including Windows paths.
    crates = {
        "makepad-widgets": dependencies["makepad"] / "widgets",
        "octoscript-widgets": dependencies["octoscript-makepad"] / "crates/octoscript-widgets",
        "octoscript-render": dependencies["octoscript-makepad"] / "crates/octoscript-render",
        "octoscript-makepad": dependencies["octoscript-makepad"] / "crates/octoscript-makepad",
        "octoscript-ui-l0": dependencies["octoscript"] / "crates/octoscript-ui-l0",
    }
    paths = "\n".join(f"{name} = {{ path = {json.dumps(str(path.resolve()))} }}" for name, path in crates.items())
    return f'''[package]
name = "{PACKAGE}"
version = "0.1.0"
edition = "2021"

[workspace]

[dependencies]
serde_json = {{ version = "1", features = ["float_roundtrip"] }}
{paths}

[profile.release]
opt-level = 3
lto = false
codegen-units = 1

[[bin]]
name = "{PACKAGE}"
path = "src/main.rs"
'''
