//! A mail's HTML, rebuilt from the few tags the app's `Html` view draws.
//!
//! Mail HTML is laid out with nested tables, styles and remote images, and can
//! carry scripts and tracking pixels. None of that reaches the app: the
//! message is walked once and rebuilt from paragraphs, headings, lists,
//! quotes, preformatted text and inline emphasis. Layout tables become
//! paragraphs, and images, styles, scripts and forms are dropped, so opening a
//! message fetches nothing. The same walk gives the plain text used for
//! previews.
use scraper::node::Node;
use scraper::Html;

/// At most this much rebuilt HTML per message.
const LIMIT: usize = 400_000;

pub struct Rebuilt {
    /// HTML using only the tags the app draws.
    pub html: String,
    /// The same content as text, a blank line between blocks.
    pub text: String,
}

pub fn rebuild(source: &str) -> Rebuilt {
    let doc = Html::parse_document(source);
    let mut out = Out::default();
    walk(&mut out, doc.tree.root());
    out.flush();
    let text = out.text.trim().to_string();
    Rebuilt { html: out.html, text }
}

#[derive(Default)]
struct Out {
    html: String,
    text: String,
    /// The paragraph being built: its HTML, and whether it holds any text.
    para: String,
    para_text: String,
    /// Inline tags open around the current point, reopened in each new
    /// paragraph so emphasis crossing a block boundary is not lost.
    inline: Vec<(String, &'static str)>,
    /// Inside a list item or heading: blocks become line breaks.
    in_line: usize,
    in_pre: usize,
    full: bool,
}

impl Out {
    fn push_text(&mut self, raw: &str) {
        if self.full {
            return;
        }
        let text = if self.in_pre > 0 {
            raw.to_string()
        } else {
            let mut collapsed = String::new();
            let mut space = self.para_text.is_empty() || self.para_text.ends_with([' ', '\n']);
            for c in raw.chars() {
                if c.is_whitespace() || c == '\u{a0}' || c == '\u{200c}' || c == '\u{34f}' {
                    if !space {
                        collapsed.push(' ');
                        space = true;
                    }
                } else {
                    collapsed.push(c);
                    space = false;
                }
            }
            collapsed
        };
        if text.is_empty() {
            return;
        }
        self.para.push_str(&escape(&text));
        self.para_text.push_str(&text);
    }

    fn open_inline(&mut self, open: String, tag: &'static str) {
        self.para.push_str(&open);
        self.inline.push((open, tag));
    }

    fn close_inline(&mut self) {
        if let Some((_, tag)) = self.inline.pop() {
            self.para.push_str(&format!("</{tag}>"));
        }
    }

    fn line_break(&mut self) {
        while self.para_text.ends_with(' ') && self.para.ends_with(' ') {
            self.para_text.pop();
            self.para.pop();
        }
        if !self.para_text.is_empty() && !self.para_text.ends_with('\n') {
            self.para.push_str("<br>");
            self.para_text.push('\n');
        }
    }

    /// End the current paragraph; emit it if it holds text.
    fn flush(&mut self) {
        let text = self.para_text.trim().to_string();
        if !text.is_empty() && !self.full {
            let mut para = std::mem::take(&mut self.para);
            for (_, tag) in self.inline.iter().rev() {
                para.push_str(&format!("</{tag}>"));
            }
            self.emit(&format!("<p>{}</p>", para.trim()), &text);
        }
        self.para.clear();
        self.para_text.clear();
        for (open, _) in &self.inline {
            self.para.push_str(open);
        }
    }

    fn emit(&mut self, html: &str, text: &str) {
        if self.html.len() + html.len() > LIMIT {
            self.full = true;
            return;
        }
        self.html.push_str(html);
        if !self.text.is_empty() {
            self.text.push_str("\n\n");
        }
        self.text.push_str(text);
    }

    /// A block boundary: a new paragraph, or a line break inside an item.
    fn block(&mut self) {
        if self.in_line > 0 {
            self.line_break();
        } else {
            self.flush();
        }
    }
}

fn escape(text: &str) -> String {
    text.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;")
}

fn walk(out: &mut Out, node: ego_tree::NodeRef<'_, Node>) {
    for child in node.children() {
        if out.full {
            return;
        }
        match child.value() {
            Node::Text(text) => out.push_text(text),
            Node::Element(element) => element_node(out, child, element),
            _ => {}
        }
    }
}

fn element_node(out: &mut Out, node: ego_tree::NodeRef<'_, Node>, element: &scraper::node::Element) {
    let name = element.name();
    let inline: Option<&'static str> = match name {
        "b" | "strong" => Some("b"),
        "i" | "em" | "cite" => Some("i"),
        "u" | "ins" => Some("u"),
        "s" | "strike" | "del" => Some("s"),
        "code" | "tt" | "kbd" | "samp" => Some("code"),
        "sub" => Some("sub"),
        "sup" => Some("sup"),
        _ => None,
    };
    if let Some(tag) = inline {
        out.open_inline(format!("<{tag}>"), tag);
        walk(out, node);
        out.close_inline();
        return;
    }
    match name {
        "head" | "style" | "script" | "title" | "meta" | "link" | "noscript" | "template" | "svg" | "iframe" | "object" | "embed"
        | "video" | "audio" | "canvas" | "img" | "picture" | "input" | "button" | "select" | "textarea" | "map" => {}
        "br" => {
            if out.in_pre > 0 {
                out.push_text("\n");
            } else {
                out.line_break();
            }
        }
        "a" => {
            let href = element.attr("href").unwrap_or("").trim();
            let safe = ["https://", "http://", "mailto:"].iter().any(|s| href.to_ascii_lowercase().starts_with(s));
            if safe && !href.contains('"') {
                out.open_inline(format!("<a href=\"{}\">", escape(href)), "a");
                walk(out, node);
                out.close_inline();
            } else {
                walk(out, node);
            }
        }
        "h1" | "h2" | "h3" | "h4" | "h5" | "h6" => {
            out.flush();
            let level = &name[1..];
            // Mail headings are sized for a web page: one step smaller.
            let level = (level.parse::<u8>().unwrap_or(3) + 1).min(6);
            let mut sub = Out { in_line: 1, ..Default::default() };
            walk(&mut sub, node);
            sub_block(out, sub, &format!("<h{level}>"), &format!("</h{level}>"));
        }
        "ul" | "ol" => {
            out.flush();
            let mut items = String::new();
            let mut text = Vec::new();
            let mut n = 0;
            for item in node.children() {
                let mut sub = Out { in_line: 1, ..Default::default() };
                match item.value() {
                    Node::Element(e) if e.name() == "li" => walk(&mut sub, item),
                    Node::Element(_) => {
                        sub_node(&mut sub, item);
                    }
                    _ => continue,
                }
                let body = inner(&sub);
                if sub.para_text.trim().is_empty() {
                    continue;
                }
                items.push_str(&format!("<li>{body}</li>"));
                n += 1;
                let marker = if name == "ol" { format!("{n}. ") } else { "• ".into() };
                text.push(format!("{marker}{}", sub.para_text.trim()));
            }
            if !items.is_empty() {
                out.emit(&format!("<{name}>{items}</{name}>"), &text.join("\n"));
            }
        }
        "blockquote" => {
            out.flush();
            let mut sub = Out { in_line: 1, ..Default::default() };
            walk(&mut sub, node);
            sub_block(out, sub, "<blockquote>", "</blockquote>");
        }
        "pre" => {
            out.flush();
            let mut sub = Out { in_pre: 1, ..Default::default() };
            walk(&mut sub, node);
            let body = sub.para.trim_end().to_string();
            if !sub.para_text.trim().is_empty() {
                out.emit(&format!("<pre>{body}</pre>"), sub.para_text.trim_end());
            }
        }
        "hr" => {
            out.flush();
            out.emit("<hr>", "");
        }
        // Everything else is a block (div, p, td, tr, table, section…) or
        // an inline wrapper (span, font) whose content is kept.
        "span" | "font" | "small" | "big" | "abbr" | "label" | "mark" | "q" | "time" => walk(out, node),
        _ => {
            out.block();
            walk(out, node);
            out.block();
        }
    }
}

fn sub_node(out: &mut Out, node: ego_tree::NodeRef<'_, Node>) {
    if let Node::Element(e) = node.value() {
        element_node(out, node, e);
    }
}

/// A line-level block's HTML, without the break its last block left.
fn inner(sub: &Out) -> String {
    let mut html = sub.para.trim();
    while let Some(rest) = html.strip_suffix("<br>") {
        html = rest.trim_end();
    }
    html.to_string()
}

fn sub_block(out: &mut Out, sub: Out, open: &str, close: &str) {
    let text = sub.para_text.trim().to_string();
    if !text.is_empty() {
        out.emit(&format!("{open}{}{close}", inner(&sub)), &text);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn mail_html_is_rebuilt_from_safe_tags() {
        let source = r#"<html><head><style>p{color:red}</style><title>x</title></head><body>
            <table><tr><td><h1>Your <b>order</b></h1></td></tr>
            <tr><td>Hello&nbsp;there,<br>thanks for <a href="https://shop.example/o/1">your order</a>.<img src="https://track.example/p.gif"></td></tr></table>
            <script>alert(1)</script><a href="javascript:alert(1)">bad</a>
            <ul><li>One <div>item</div></li><li>Two</li></ul><p onclick="x()">A &lt;tag&gt;</p></body></html>"#;
        let rebuilt = rebuild(source);
        let html = &rebuilt.html;
        assert!(html.contains("<h2>Your <b>order</b></h2>"), "{html}");
        assert!(html.contains(r#"<a href="https://shop.example/o/1">your order</a>"#), "{html}");
        assert!(html.contains("Hello there,<br>thanks"), "{html}");
        assert!(html.contains("<ul><li>One<br>item</li><li>Two</li></ul>"), "{html}");
        assert!(html.contains("<p>A &lt;tag&gt;</p>"), "{html}");
        for gone in ["style", "color:red", "script", "alert", "img", "track.example", "onclick", "javascript"] {
            assert!(!html.contains(gone), "{gone} survived: {html}");
        }
        assert!(rebuilt.text.starts_with("Your order\n\nHello there,\nthanks for your order."), "{}", rebuilt.text);
        assert!(rebuilt.text.contains("• One\nitem\n• Two"), "{}", rebuilt.text);
    }
}
