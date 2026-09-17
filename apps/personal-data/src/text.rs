//! Small text helpers: HTML to text, truncation, CJK detection, FTS queries.

/// Reduce an HTML document to readable text (scripts/styles dropped, tags
/// removed, entities decoded, whitespace collapsed).
pub fn html_to_text(html: &str) -> String {
    let mut out = String::with_capacity(html.len() / 4);
    let mut rest = html;
    let mut skip_depth: Option<&str> = None;
    while let Some(start) = rest.find('<') {
        let before = &rest[..start];
        if skip_depth.is_none() {
            out.push_str(before);
        }
        rest = &rest[start..];
        let Some(end) = rest.find('>') else { break };
        let tag = &rest[1..end];
        let name: String = tag
            .trim_start_matches('/')
            .chars()
            .take_while(|c| c.is_ascii_alphanumeric())
            .collect::<String>()
            .to_ascii_lowercase();
        let closing = tag.starts_with('/');
        match (skip_depth, closing) {
            (None, false) if name == "script" || name == "style" || name == "head" => {
                skip_depth = Some(if name == "script" {
                    "script"
                } else if name == "style" {
                    "style"
                } else {
                    "head"
                });
            }
            (Some(open), true) if name == open => skip_depth = None,
            (None, _) => {
                if matches!(
                    name.as_str(),
                    "p" | "div" | "br" | "tr" | "li" | "h1" | "h2" | "h3" | "h4" | "td" | "table"
                ) {
                    out.push(' ');
                }
            }
            _ => {}
        }
        rest = &rest[end + 1..];
    }
    if skip_depth.is_none() {
        out.push_str(rest);
    }
    collapse(&decode_entities(&out))
}

fn decode_entities(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut rest = s;
    while let Some(i) = rest.find('&') {
        out.push_str(&rest[..i]);
        rest = &rest[i..];
        let mut window = rest.len().min(12);
        while !rest.is_char_boundary(window) {
            window -= 1;
        }
        let Some(end) = rest[..window].find(';') else {
            out.push('&');
            rest = &rest[1..];
            continue;
        };
        let entity = &rest[1..end];
        let decoded = match entity {
            "amp" => Some('&'),
            "lt" => Some('<'),
            "gt" => Some('>'),
            "quot" => Some('"'),
            "apos" | "#39" => Some('\''),
            "nbsp" => Some(' '),
            e if e.starts_with("#x") || e.starts_with("#X") => u32::from_str_radix(&e[2..], 16)
                .ok()
                .and_then(char::from_u32),
            e if e.starts_with('#') => e[1..].parse::<u32>().ok().and_then(char::from_u32),
            _ => None,
        };
        match decoded {
            Some(c) => {
                out.push(c);
                rest = &rest[end + 1..];
            }
            None => {
                out.push('&');
                rest = &rest[1..];
            }
        }
    }
    out.push_str(rest);
    out
}

pub fn collapse(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut space = true;
    for c in s.chars() {
        if c.is_whitespace() {
            if !space {
                out.push(' ');
                space = true;
            }
        } else {
            out.push(c);
            space = false;
        }
    }
    out.trim().to_string()
}

/// Truncate on a char boundary, appending an ellipsis when cut.
pub fn clip(s: &str, max: usize) -> String {
    if s.chars().count() <= max {
        return s.to_string();
    }
    let mut out: String = s.chars().take(max.saturating_sub(1)).collect();
    out.push('…');
    out
}

pub fn has_cjk(s: &str) -> bool {
    s.chars().any(|c| {
        matches!(c as u32, 0x3040..=0x30FF | 0x3400..=0x4DBF | 0x4E00..=0x9FFF | 0xAC00..=0xD7AF | 0xF900..=0xFAFF)
    })
}

/// Build a safe FTS5 MATCH expression: each term quoted, joined with AND,
/// prefix-matched so partial words still hit. Returns None for no terms.
pub fn fts_query(query: &str) -> Option<String> {
    let terms: Vec<String> = query
        .split(|c: char| !c.is_alphanumeric() && c != '@' && c != '.' && c != '-' && c != '_')
        .filter(|t| !t.is_empty())
        .map(|t| format!("\"{}\"*", t.replace('"', "\"\"")))
        .collect();
    if terms.is_empty() {
        None
    } else {
        Some(terms.join(" AND "))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn should_strip_markup_and_scripts_when_converting_html() {
        let html = "<html><head><style>p{}</style></head><body><p>Hi&nbsp;<b>Sam</b>,</p>\
                    <script>alert(1)</script><div>see you &amp; Alex at 10 &#x2014; ok</div></body></html>";
        assert_eq!(html_to_text(html), "Hi Sam, see you & Alex at 10 — ok");
    }

    #[test]
    fn should_not_split_multibyte_text_when_scanning_entities() {
        assert_eq!(html_to_text("<p>&amp;欢迎访问我们的网站</p>"), "&欢迎访问我们的网站");
        assert_eq!(html_to_text("&欢迎访问我们的网站再来一次"), "&欢迎访问我们的网站再来一次");
    }

    #[test]
    fn should_quote_terms_when_building_fts_query() {
        assert_eq!(fts_query("car rental \"8\""), Some("\"car\"* AND \"rental\"* AND \"8\"*".into()));
        assert_eq!(fts_query("  ,, "), None);
    }

    #[test]
    fn should_detect_cjk_text() {
        assert!(has_cjk("牙医"));
        assert!(!has_cjk("dentist"));
    }

    #[test]
    fn should_clip_on_char_boundary() {
        assert_eq!(clip("日出牙科诊所", 4), "日出牙…");
        assert_eq!(clip("short", 10), "short");
    }
}
