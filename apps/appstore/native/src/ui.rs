//! The store's screens, as generated widget source, in the shape people know
//! from the App Store: a large title over a list of icon-and-pill rows, and
//! a product page with a big icon, an information strip, a screenshot rail,
//! the description, what's new, an information list, and the app's privacy.
//!
//! The screens are built from the catalog each time it changes, so they are
//! written as script and evaluated in the store's own vm. That is fine here
//! and only here: this is OUR code in the trusted tier. A card from the hub
//! never takes this path — it goes to an isolate, which is the whole point
//! of ADR 0002.
use octosense_app_hub::{Availability, Listing};

const BLUE: &str = "#007aff";
const GREY: &str = "#8e8e93";
const HAIRLINE: &str = "#e5e5ea";
const PILL: &str = "#eeeef2";

fn escape(text: &str) -> String {
    text.replace('\\', "\\\\").replace('"', "\\\"").replace('\n', " ")
}

/// Where a listing image is fetched from: the hub's copy of the bundle.
fn asset_url(asset_base: Option<&str>, listing: &Listing, path: &str) -> Option<String> {
    let base = asset_base?;
    Some(format!("{}{}/{}", base, listing.artifact.trim_end_matches('/'), path.trim_start_matches('/')))
}

/// An icon at `size`, by URL: an `Svg` for vectors, an `Image` for bitmaps,
/// and a soft placeholder square when the listing has none.
fn icon_source(asset_base: Option<&str>, listing: &Listing, size: u32, radius: u32) -> String {
    let url = listing.about.as_ref().and_then(|about| about.icon.as_deref()).and_then(|path| asset_url(asset_base, listing, path));
    match url {
        Some(url) if url.to_ascii_lowercase().ends_with(".svg") => format!(
            r#"Svg {{ width: {size} height: {size} animating: false draw_svg.svg: http_resource("{}") draw_svg.preserve_viewbox: true draw_svg.preserve_aspect: false }}"#,
            escape(&url)
        ),
        Some(url) => format!(
            r#"RoundedView {{ width: {size} height: {size} draw_bg.radius: {radius} draw_bg.color: {PILL} show_bg: true Image {{ width: {size} height: {size} src: http_resource("{}") fit: ImageFit.Stretch }} }}"#,
            escape(&url)
        ),
        None => format!(
            r#"RoundedView {{ width: {size} height: {size} draw_bg.radius: {radius} draw_bg.color: {PILL} show_bg: true align: Align{{x: 0.5, y: 0.5}} Label {{ text: "{}" draw_text.color: {GREY} draw_text.text_style.font_size: {} }} }}"#,
            escape(listing.name.chars().next().map(|c| c.to_uppercase().to_string()).unwrap_or_default().as_str()),
            size / 3
        ),
    }
}

/// The blue-on-grey pill: GET, OPEN, or a withdrawn note.
fn pill_source(id: &str, listing: &Listing) -> String {
    let (text, colour) = match &listing.availability {
        Availability::Installable => ("GET", BLUE),
        Availability::Installed { .. } => ("OPEN", BLUE),
        Availability::Withdrawn { .. } => ("WITHDRAWN", "#ff3b30"),
    };
    format!(
        r#"{id} := Button {{ text: "{text}" draw_text.color: {colour} draw_text.text_style.font_size: 12 draw_bg.color: {PILL} draw_bg.color_hover: #e0e0e6 draw_bg.color_down: #d6d6dc draw_bg.radius: 14 draw_bg.border_width: 0 padding: Inset{{left: 18., right: 18., top: 6., bottom: 6.}} }}"#
    )
}

/// The list: a row per app with its icon, name, subtitle and pill.
pub fn list_source(listings: &[Listing], query: &str, asset_base: Option<&str>) -> String {
    let mut rows = String::new();
    for (i, listing) in listings.iter().enumerate() {
        let subtitle = listing
            .about
            .as_ref()
            .map(|a| if a.subtitle.is_empty() { a.category.clone() } else { a.subtitle.clone() })
            .unwrap_or_else(|| listing.permissions.join(" · "));
        let category = listing.about.as_ref().map(|a| a.category.replace('-', " & ")).unwrap_or_default();
        rows.push_str(&format!(
            r#"
            View {{
                width: Fill height: Fit flow: Right spacing: 14 padding: Inset{{left: 0., right: 0., top: 10., bottom: 10.}} align: Align{{x: 0., y: 0.5}}
                {icon}
                View {{
                    width: Fill height: Fit flow: Down spacing: 3
                    Label {{ width: Fill text: "{name}" draw_text.color: #000 draw_text.text_style.font_size: 15 }}
                    Label {{ width: Fill text: "{subtitle}" draw_text.color: {GREY} draw_text.text_style.font_size: 12 }}
                    Label {{ width: Fill text: "{category}" draw_text.color: {GREY} draw_text.text_style.font_size: 10 }}
                }}
                {pill}
            }}
            View {{ width: Fill height: 1 show_bg: true draw_bg.color: {HAIRLINE} margin: Inset{{left: 78., right: 0., top: 0., bottom: 0.}} }}
            "#,
            icon = icon_source(asset_base, listing, 64, 14),
            name = escape(&listing.name),
            subtitle = escape(&subtitle),
            category = escape(&category),
            pill = pill_source(&format!("open_{i}"), listing),
        ));
    }
    if listings.is_empty() {
        let message = if query.trim().is_empty() {
            "No apps in this catalog yet.".to_string()
        } else {
            format!("No results for {:?}.", query.trim())
        };
        rows.push_str(&format!(r#"Label {{ text: "{}" draw_text.color: {GREY} margin: 24 }}"#, escape(&message)));
    }
    format!("width: Fill height: Fit flow: Down padding: Inset{{left: 16., right: 16., top: 0., bottom: 16.}} {rows}")
}

fn label(text: &str, colour: &str, size: u32, wrap: bool, margin: &str) -> String {
    format!(
        r#"Label {{ width: Fill text: "{}" draw_text.color: {colour} draw_text.text_style.font_size: {size} {} margin: {margin} }}"#,
        escape(text),
        if wrap { "draw_text.wrap: Words" } else { "" }
    )
}

fn heading(text: &str) -> String {
    format!(
        r#"Label {{ width: Fill text: "{}" draw_text.color: #000 draw_text.text_style.font_size: 17 margin: Inset{{left: 0., right: 0., top: 18., bottom: 6.}} }}"#,
        escape(text)
    )
}

fn info_row(key: &str, value: &str) -> String {
    format!(
        r#"View {{ width: Fill height: Fit flow: Right spacing: 10 padding: Inset{{left: 0., right: 0., top: 8., bottom: 8.}}
            Label {{ width: 120 text: "{}" draw_text.color: {GREY} draw_text.text_style.font_size: 12 }}
            Label {{ width: Fill text: "{}" draw_text.color: #000 draw_text.text_style.font_size: 12 draw_text.wrap: Words }}
        }}
        View {{ width: Fill height: 1 show_bg: true draw_bg.color: {HAIRLINE} }}"#,
        escape(key),
        escape(value)
    )
}

/// One cell of the strip under the header: a small grey caption, a value.
fn strip_cell(caption: &str, value: &str) -> String {
    format!(
        r#"View {{ width: Fit height: Fit flow: Down spacing: 2 align: Align{{x: 0.5, y: 0.}} padding: Inset{{left: 14., right: 14., top: 0., bottom: 0.}}
            Label {{ text: "{}" draw_text.color: {GREY} draw_text.text_style.font_size: 9 }}
            Label {{ text: "{}" draw_text.color: #48484a draw_text.text_style.font_size: 14 }}
        }}
        View {{ width: 1 height: 34 show_bg: true draw_bg.color: {HAIRLINE} }}"#,
        escape(caption),
        escape(value)
    )
}

/// The product page.
pub fn detail_source(listing: &Listing, status: &str, asset_base: Option<&str>) -> String {
    let about = listing.about.as_ref();
    let subtitle = about.map(|a| a.subtitle.clone()).filter(|s| !s.is_empty()).unwrap_or_else(|| listing.publisher.clone());

    // The strip: age, category, developer, version.
    let mut strip = String::new();
    strip.push_str(&strip_cell("AGE", about.map(|a| a.age_rating.as_str()).unwrap_or("—")));
    strip.push_str(&strip_cell("CATEGORY", &about.map(|a| a.category.replace('-', " & ")).unwrap_or_else(|| "—".into())));
    strip.push_str(&strip_cell("DEVELOPER", about.map(|a| a.publisher.name.as_str()).unwrap_or(listing.publisher.as_str())));
    strip.push_str(&strip_cell("VERSION", &listing.version));

    // The screenshot rail, when the listing has any.
    let mut shots = String::new();
    if let Some(about) = about {
        for path in &about.screenshots {
            if let Some(url) = asset_url(asset_base, listing, path) {
                shots.push_str(&format!(
                    r#"RoundedView {{ width: 180 height: 344 draw_bg.radius: 12 draw_bg.color: {PILL} show_bg: true clip_x: true clip_y: true
                        Image {{ width: 180 height: 344 src: http_resource("{}") fit: ImageFit.Stretch }} }}"#,
                    escape(&url)
                ));
            }
        }
    }
    let rail = if shots.is_empty() {
        String::new()
    } else {
        format!(
            r#"{}
            View {{ width: Fill height: Fit flow: Right spacing: 10 scroll_bars: mod.widgets.ScrollBars {{ show_scroll_x: true, show_scroll_y: false }} {shots} }}"#,
            heading("Preview")
        )
    };

    let description = about.map(|a| a.description.as_str()).unwrap_or("");
    let whats_new = about.map(|a| a.release_notes.as_str()).unwrap_or("");

    let mut information = String::new();
    if let Some(about) = about {
        information.push_str(&info_row("Provider", &about.publisher.name));
        information.push_str(&info_row("Category", &about.category.replace('-', " & ")));
        information.push_str(&info_row("Compatibility", &about.platforms.join(", ")));
        information.push_str(&info_row("Age Rating", &about.age_rating));
        information.push_str(&info_row("Support", &about.publisher.support));
        information.push_str(&info_row("Privacy Policy", &about.publisher.privacy_policy_url));
        if let Some(license) = &about.license {
            information.push_str(&info_row("Licence", license));
        }
    }
    information.push_str(&info_row("Publisher key", &listing.publisher));

    let bullets = |lines: &[String]| {
        lines
            .iter()
            .map(|line| label(&format!("•  {line}"), "#3a3a3c", 12, true, "Inset{left: 0., right: 0., top: 2., bottom: 2.}"))
            .collect::<Vec<_>>()
            .join("\n")
    };

    let note = match &listing.availability {
        Availability::Withdrawn { reason } => label(&format!("This app was withdrawn: {reason}"), "#ff3b30", 12, true, "8"),
        _ => String::new(),
    };
    let remove = match &listing.availability {
        Availability::Installed { .. } => format!(
            r#"remove_button := Button {{ text: "Remove" draw_text.color: #ff3b30 draw_text.text_style.font_size: 12 draw_bg.color: {PILL} draw_bg.radius: 14 draw_bg.border_width: 0 padding: Inset{{left: 14., right: 14., top: 6., bottom: 6.}} }}"#
        ),
        _ => String::new(),
    };

    format!(
        r#"width: Fill height: Fit flow: Down padding: Inset{{left: 16., right: 16., top: 0., bottom: 24.}}
        View {{
            width: Fill height: Fit flow: Right align: Align{{x: 0., y: 0.5}} margin: Inset{{left: 0., right: 0., top: 0., bottom: 10.}}
            back_button := Button {{ text: "‹ Apps" draw_text.color: {BLUE} draw_text.text_style.font_size: 14 draw_bg.color: #00000000 draw_bg.border_width: 0 padding: 0 }}
        }}
        View {{
            width: Fill height: Fit flow: Right spacing: 16 align: Align{{x: 0., y: 0.}}
            {big_icon}
            View {{
                width: Fill height: Fit flow: Down spacing: 4
                Label {{ width: Fill text: "{name}" draw_text.color: #000 draw_text.text_style.font_size: 22 }}
                Label {{ width: Fill text: "{subtitle}" draw_text.color: {GREY} draw_text.text_style.font_size: 13 draw_text.wrap: Words }}
                View {{ width: Fill height: 8 }}
                View {{ width: Fill height: Fit flow: Right spacing: 10 align: Align{{x: 0., y: 0.5}}
                    {pill}
                    {remove}
                }}
            }}
        }}
        {note}
        View {{ width: Fill height: 1 show_bg: true draw_bg.color: {HAIRLINE} margin: Inset{{left: 0., right: 0., top: 16., bottom: 0.}} }}
        View {{ width: Fill height: Fit flow: Right align: Align{{x: 0., y: 0.5}} padding: Inset{{left: 0., right: 0., top: 10., bottom: 10.}} scroll_bars: mod.widgets.ScrollBars {{ show_scroll_x: true, show_scroll_y: false }} {strip} }}
        View {{ width: Fill height: 1 show_bg: true draw_bg.color: {HAIRLINE} }}
        {rail}
        {desc_heading}
        {description}
        {new_heading}
        {whats_new}
        {info_heading}
        {information}
        {privacy_heading}
        {privacy_intro}
        {privacy}
        {allowed_heading}
        {permissions}
        status_label := Label {{ width: Fill text: "{status}" draw_text.color: {GREY} draw_text.text_style.font_size: 11 draw_text.wrap: Words margin: Inset{{left: 0., right: 0., top: 14., bottom: 0.}} }}
        "#,
        big_icon = icon_source(asset_base, listing, 110, 24),
        name = escape(&listing.name),
        subtitle = escape(&subtitle),
        pill = pill_source("action_button", listing),
        remove = remove,
        note = note,
        strip = strip,
        rail = rail,
        desc_heading = if description.is_empty() { String::new() } else { heading("Description") },
        description = if description.is_empty() { String::new() } else { label(description, "#1c1c1e", 13, true, "0") },
        new_heading = if whats_new.is_empty() { String::new() } else { heading("What's New") },
        whats_new = if whats_new.is_empty() { String::new() } else { label(&format!("Version {} · {}", listing.version, whats_new), "#1c1c1e", 13, true, "0") },
        info_heading = heading("Information"),
        information = information,
        privacy_heading = heading("App Privacy"),
        privacy_intro = label("Derived from what the app declared, not from what it says about itself.", GREY, 11, true, "Inset{left: 0., right: 0., top: 0., bottom: 6.}"),
        privacy = bullets(&listing.privacy),
        allowed_heading = heading("This app will be allowed to"),
        permissions = bullets(&listing.permissions),
        status = escape(status),
    )
}

/// The bar above a running app: a way back, and what the app is running under.
pub fn running_source(app_id: &str, status: &str) -> String {
    format!(
        r#"width: Fill height: Fit flow: Right padding: 10 spacing: 10 align: Align{{x: 0., y: 0.5}}
        close_button := Button {{ text: "‹ Close" draw_text.color: {BLUE} }}
        Label {{ width: Fill text: "{status}" draw_text.color: {GREY} draw_text.text_style.font_size: 11 }}
        "#,
        status = escape(if status.is_empty() { app_id } else { status }),
    )
}
