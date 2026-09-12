#!/usr/bin/env python3
"""Run the actual Splash news-digest template with real model summaries."""
import argparse
import datetime
import json
from pathlib import Path
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parent
BINARY = ROOT / "target/release/octos-one-splash-research-experiment"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:30881/v1")
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--live", action="store_true", help="Discover and retrieve real publisher articles on every run")
    parser.add_argument("--topic", choices=["technology", "world", "business"], default="technology")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.repeats < 1:
        parser.error("--repeats must be positive")
    report = {"mode":"live_rss_articles_rtx_splash" if args.live else "real_rtx_summaries_fixture_retrieval",
              "measured_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(), "runs":[]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for round_ in range(args.repeats):
        for language in (["en", "zh-CN"] if round_ % 2 == 0 else ["zh-CN", "en"]):
            command = ([str(BINARY), "--live-news", language, args.topic, args.base_url] if args.live
                       else [str(BINARY), "--news-digest", language, args.base_url])
            try:
                started = time.perf_counter()
                execution = subprocess.run(command, capture_output=True, text=True, timeout=95, check=True)
                row = json.loads(execution.stdout)
                row.update(language=language, round=round_, process_elapsed_ms=(time.perf_counter()-started)*1000)
                data = row["output"]["data"]
                expected = {a["id"] for a in data["articles"]} if args.live else {"a", "b", "c"}
                row["structurally_valid"] = (row["output"]["status"] == "ready" and row["llm_calls"] == 1
                    and len(row["model_calls"]) == 1 and len(expected) == 3
                    and data["digest"]["language"] == language and data["missing"] == 0
                    and {i["id"] for i in data["digest"]["items"]} == expected)
                if args.live:
                    row["structurally_valid"] &= (data["discovery"]["kind"] == "live-rss"
                        and all(a["source"]["kind"] == "live-article" for a in data["articles"]))
            except (subprocess.SubprocessError, ValueError, KeyError, TypeError) as error:
                row = {"language":language, "round":round_, "structurally_valid":False, "error":str(error)}
                if isinstance(error, subprocess.CalledProcessError):
                    row["stderr"] = error.stderr
            report["runs"].append(row)
            args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
            print(language, row["structurally_valid"], round(row.get("elapsed_ms", 0)), "ms", flush=True)
    report["summary"] = []
    for language in ["en", "zh-CN"]:
        rows = [r for r in report["runs"] if r["language"] == language and r["structurally_valid"]]
        report["summary"].append({"language":language, "valid":len(rows), "total":args.repeats,
            "median_pipeline_ms":statistics.median(r["elapsed_ms"] for r in rows) if rows else None,
            "median_process_ms":statistics.median(r["process_elapsed_ms"] for r in rows) if rows else None,
            "median_model_ms":statistics.median(r["model_calls"][0]["elapsed_ms"] for r in rows) if rows else None})
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    if not all(row["structurally_valid"] for row in report["runs"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
