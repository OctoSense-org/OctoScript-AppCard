//! Serving an installed app its own artwork, and nothing else.
//!
//! The lowering rule is that a card's vectors must come from a loopback HTTP
//! origin: a path on disk is refused outright (`design.rs`,
//! "design vectors require a local SVG asset"). A bundle, meanwhile, must not
//! name an outside origin — the hub's gate refuses that, because the resource
//! loader is not gated by the isolate's network grant.
//!
//! Both rules hold at once only if the HOST serves the app's bytes. That is
//! this server: one per running app, bound to loopback on a port the kernel
//! picks, serving strictly the files inside that app's installed bundle. The
//! app never learns a URL it did not get from us, and a request that climbs
//! out of the bundle is refused before it touches the filesystem.
use std::io::{BufRead, BufReader, Read, Write};
use std::net::TcpListener;
use std::path::{Component, Path, PathBuf};
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;

pub struct AssetServer {
    origin: String,
    port: u16,
    stop: Arc<AtomicBool>,
}

impl AssetServer {
    /// Serve `root` on loopback. Returns a server whose `origin()` is the
    /// base URL a lowered card should use.
    pub fn start(root: &Path) -> Result<AssetServer, String> {
        let listener = TcpListener::bind("127.0.0.1:0").map_err(|e| format!("asset server: {e}"))?;
        let port = listener.local_addr().map_err(|e| e.to_string())?.port();
        listener.set_nonblocking(false).map_err(|e| e.to_string())?;
        let stop = Arc::new(AtomicBool::new(false));
        let root = root.to_path_buf();
        let flag = stop.clone();
        std::thread::spawn(move || {
            for stream in listener.incoming() {
                if flag.load(Ordering::Relaxed) {
                    break;
                }
                let Ok(mut stream) = stream else { continue };
                // Accepted sockets inherit non-blocking mode on macOS; a
                // blocking read is what the rest of this expects.
                let _ = stream.set_nonblocking(false);
                let _ = serve_one(&mut stream, &root);
            }
        });
        Ok(AssetServer { origin: format!("http://127.0.0.1:{port}/"), port, stop })
    }

    pub fn origin(&self) -> &str {
        &self.origin
    }

    /// The allowlist entry that admits exactly this server and no other
    /// loopback service: `127.0.0.1:<port>`.
    pub fn allowlist_entry(&self) -> String {
        format!("127.0.0.1:{}", self.port)
    }
}

impl Drop for AssetServer {
    fn drop(&mut self) {
        self.stop.store(true, Ordering::Relaxed);
        // Wake the accept loop so the thread can notice and end.
        let _ = std::net::TcpStream::connect(self.origin.trim_start_matches("http://").trim_end_matches('/'));
    }
}

fn serve_one(stream: &mut std::net::TcpStream, root: &Path) -> std::io::Result<()> {
    let mut reader = BufReader::new(stream.try_clone()?);
    let mut request = String::new();
    reader.read_line(&mut request)?;
    // Read the whole head: a partial read makes the next request look like a
    // new one and answers it with a 404.
    let mut line = String::new();
    loop {
        line.clear();
        if reader.read_line(&mut line)? == 0 || line.trim().is_empty() {
            break;
        }
    }
    let path = request.split_whitespace().nth(1).unwrap_or("/").to_string();
    match resolve(root, &path) {
        Some(file) => {
            let mut bytes = Vec::new();
            match std::fs::File::open(&file).and_then(|mut f| f.read_to_end(&mut bytes)) {
                Ok(_) => {
                    let mime = match file.extension().and_then(|e| e.to_str()).unwrap_or("") {
                        "svg" => "image/svg+xml",
                        "png" => "image/png",
                        "jpg" | "jpeg" => "image/jpeg",
                        "webp" => "image/webp",
                        "json" => "application/json",
                        _ => "application/octet-stream",
                    };
                    write!(
                        stream,
                        "HTTP/1.1 200 OK\r\nContent-Type: {mime}\r\nContent-Length: {}\r\nCache-Control: no-store\r\nConnection: close\r\n\r\n",
                        bytes.len()
                    )?;
                    stream.write_all(&bytes)?;
                }
                Err(_) => not_found(stream)?,
            }
        }
        None => not_found(stream)?,
    }
    stream.flush()
}

fn not_found(stream: &mut std::net::TcpStream) -> std::io::Result<()> {
    write!(stream, "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n")
}

/// Map a request path to a file inside `root`, or nothing. Anything that is
/// not a plain relative path under the bundle is refused: no parent
/// components, no absolute paths, no symlinks.
fn resolve(root: &Path, request_path: &str) -> Option<PathBuf> {
    let trimmed = request_path.split('?').next().unwrap_or("").trim_start_matches('/');
    if trimmed.is_empty() {
        return None;
    }
    let decoded = percent_decode(trimmed);
    let candidate = Path::new(&decoded);
    if candidate.components().any(|c| !matches!(c, Component::Normal(_))) {
        return None;
    }
    let file = root.join(candidate);
    let canonical_root = root.canonicalize().ok()?;
    let canonical_file = file.canonicalize().ok()?;
    if !canonical_file.starts_with(&canonical_root) || !canonical_file.is_file() {
        return None;
    }
    Some(canonical_file)
}

fn percent_decode(text: &str) -> String {
    let bytes = text.as_bytes();
    let mut out = Vec::with_capacity(bytes.len());
    let mut i = 0;
    while i < bytes.len() {
        if bytes[i] == b'%' && i + 2 < bytes.len() {
            if let Ok(value) = u8::from_str_radix(&text[i + 1..i + 3], 16) {
                out.push(value);
                i += 3;
                continue;
            }
        }
        out.push(bytes[i]);
        i += 1;
    }
    String::from_utf8_lossy(&out).into_owned()
}

/// Point a card's bundle-relative asset references at this server.
///
/// The gate refuses a bundle that names an origin, so what is in the data is
/// a relative path; the host is the only thing that turns it into a URL, and
/// it can only ever be this app's own origin.
pub fn rewrite_assets(data: &mut serde_json::Value, origin: &str) {
    match data {
        serde_json::Value::String(text) => {
            if !text.contains("://") && (text.ends_with(".svg") || text.ends_with(".png") || text.ends_with(".webp") || text.ends_with(".jpg")) {
                *text = format!("{origin}{}", text.trim_start_matches('/'));
            }
        }
        serde_json::Value::Array(items) => items.iter_mut().for_each(|item| rewrite_assets(item, origin)),
        serde_json::Value::Object(map) => map.values_mut().for_each(|value| rewrite_assets(value, origin)),
        _ => {}
    }
}
