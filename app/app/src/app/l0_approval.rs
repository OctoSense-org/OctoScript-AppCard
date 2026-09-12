use splash_ui_l0::approval::ArtifactApproval;

pub fn require(source: &str, kit: &str) -> Result<ArtifactApproval, String> {
    let directory = match std::env::var_os("OCTOS_L0_APPROVAL_DIR") {
        Some(path) => std::path::PathBuf::from(path),
        None => super::login::config_dir().ok_or("card approval directory unavailable")?.join("l0-approvals"),
    };
    super::l0_approval_store::require(&directory, source, env!("SPLASH_RUNTIME_BUNDLE"), kit)
}

pub fn verify(approval: &ArtifactApproval, source: &str, kit: &str) -> Result<(), String> {
    approval.verify(source, env!("SPLASH_RUNTIME_BUNDLE"), kit)
}
