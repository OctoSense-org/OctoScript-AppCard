#!/usr/bin/env python3
"""Loopback bridge from native L0 bindings to the real Splash news workflow."""
import argparse
from concurrent.futures import Future
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import threading
import time
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
BINARY = ROOT / "target/release/octos-one-splash-research-experiment"
CACHE = {}
LOCK = threading.Lock()
GPU = threading.Semaphore(1)


def project(result, query, language):
    data = result["output"]["data"]
    summaries = {x["id"]: x["summary"] for x in (data.get("digest") or {}).get("items", [])}
    items = [{"id":a["id"], "title":a["title"], "summary":summaries.get(a["id"], "Summary unavailable"),
              "publisher":"BBC" if a["source"]["publisher"] == "bbc" else "The Guardian",
              "url":a["source"]["url"], "published_at":a["source"]["published_at"][:16].replace("T", " ")+" UTC"}
             for a in data["articles"]]
    feed_failure = any(not f["ok"] for f in data["discovery"]["feeds"])
    status = result["output"]["status"] if items else ("failed" if feed_failure else "empty")
    seconds = result["elapsed_ms"] / 1000
    if status == "empty":
        message = "No usable articles in the past 72 hours. Try another search."
    elif status == "failed":
        message = "News search is unavailable. Try again shortly."
    else:
        message = f"{len(items)} articles · {seconds:.1f} s · past 72 hours"
        if status == "partial": message += " · some results unavailable"
    return {"query":query,"language":language,"status":status,"message":message,"count":len(items),"items":items}


def search(query, language, base_url, evidence):
    key = (query, language)
    with LOCK:
        cached = CACHE.get(key)
        if cached and (not cached[1].done() or time.monotonic()-cached[0] < 60):
            future, owner = cached[1], False
        else:
            if len(CACHE) >= 32:
                for old in list(CACHE):
                    if CACHE[old][1].done(): del CACHE[old]; break
                else: raise RuntimeError("Too many searches are already running")
            future, owner = Future(), True
            CACHE[key] = (time.monotonic(), future)
    if owner:
        try:
            # One GPU inference slot. Coalesce repeated bindings and bound queueing.
            if not GPU.acquire(timeout=5): raise RuntimeError("Another search is running; try again shortly")
            try:
                proc = subprocess.run([str(BINARY), "--live-news", language, query, base_url],
                                      capture_output=True, text=True, timeout=85, check=True)
            finally:
                GPU.release()
            result = json.loads(proc.stdout)
            if evidence:
                evidence.mkdir(parents=True, exist_ok=True)
                (evidence / f"search-{time.time_ns()}.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
            output = project(result, query, language)
            print(json.dumps({"query":query,"language":language,"status":output["status"],"elapsed_ms":result["elapsed_ms"]}),flush=True)
            future.set_result(output)
        except Exception as error:
            future.set_exception(error)
            with LOCK: CACHE.pop(key, None)
    return future.result(timeout=90)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8767)
    parser.add_argument("--base-url", default="http://127.0.0.1:30881/v1")
    parser.add_argument("--evidence-dir", type=Path)
    args = parser.parse_args()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlsplit(self.path)
            if path.path == "/health":
                body = {"status":"ok"}
            elif path.path == "/news":
                params = parse_qs(path.query)
                query = params.get("q", [""])[0].strip()
                language = params.get("language", ["en"])[0]
                try:
                    if not query or len(query) > 160 or language not in ("en", "zh-CN"):
                        raise ValueError("Enter a search of 1–160 characters")
                    body = search(query, language, args.base_url, args.evidence_dir)
                except Exception as error:
                    print(f"News request failed: {error}", flush=True)
                    body = {"status":"failed","message":"Search could not finish. Try again shortly.","count":0,"items":[]}
            else:
                self.send_error(404); return
            raw = json.dumps(body, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            try: self.wfile.write(raw)
            except (BrokenPipeError, ConnectionResetError): pass

        def log_message(self, *_): pass

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Live news bridge listening on 127.0.0.1:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
