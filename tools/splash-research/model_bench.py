#!/usr/bin/env python3
"""Real model comparison: bounded parallel tool loop vs one template binding.

Uses identical fixture inputs/results and a real Splash executable. No shell
or model-generated commands are executed. Default endpoint is the local tunnel.
"""
import argparse
import asyncio
import json
from pathlib import Path
import statistics
import subprocess
import tempfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
CASES = json.loads((ROOT / "fixtures.json").read_text())
BINARY = ROOT / "target/release/octos-one-splash-research-experiment"


def schema(value):
    if isinstance(value, dict):
        return {"type": "object", "required": list(value), "additionalProperties": False,
                "properties": {k: schema(v) for k, v in value.items()}}
    if isinstance(value, list):
        return {"type": "array", "maxItems": 3, "items": schema(value[0]) if value else {}}
    if isinstance(value, str):
        return {"type": "string"}
    return {"type": "number"}


def model_call(base, model, messages, tools=None, output_schema=None):
    body = {"model": model, "messages": messages, "temperature": 0, "max_tokens": 2048,
            "chat_template_kwargs": {"enable_thinking": False}}
    if tools:
        body.update(tools=tools, parallel_tool_calls=True, tool_choice="auto")
    if output_schema is not None:
        body["response_format"] = {"type":"json_schema", "json_schema":{
            "name":"research_output", "strict":True, "schema":output_schema}}
    raw = json.dumps(body).encode()
    started = time.perf_counter()
    request = urllib.request.Request(base + "/chat/completions", raw, {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=90) as response:
        result = json.load(response)
    choice = result["choices"][0]
    if choice["finish_reason"] not in ("stop", "tool_calls"):
        raise ValueError("incomplete model output: " + choice["finish_reason"])
    return choice["message"], {"elapsed_s": time.perf_counter() - started,
                              "usage": result.get("usage"), "request_bytes": len(raw),
                              "finish_reason": choice["finish_reason"]}


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


def user_request(case):
    intents = {
        "weather": "Show current temperature in Celsius and air quality (US AQI) at these coordinates.",
        "stock": "Show this instrument's quote, previous-session-close return in percent, and headlines. This is not a return since a news event.",
        "news": "Search this topic and show the first three full article records in discovery order, with sources.",
    }
    return intents[case["name"]] + " Resolved request parameters: " + json.dumps(case["input"])


def template_run(case, base, model):
    catalog = [{"template": c["name"], "input_schema": schema(c["input"])} for c in CASES]
    messages = [{"role": "system", "content":
        "Select one registered research template and copy the resolved request parameters into its input. "
        "Return only JSON {\"template\":name,\"input\":object}. No data retrieval or prose. Catalog: " + json.dumps(catalog)},
        {"role": "user", "content": user_request(case)}]
    started = time.perf_counter()
    # One common contract for every case: the response grammar must not reveal
    # which template is expected. The host validates the selected pair afterward.
    binding_schema = {"type":"object", "additionalProperties":False,
        "required":["template","input"], "properties":{
            "template":{"type":"string","enum":[c["name"] for c in CASES]},
            "input":{"anyOf":[schema(c["input"]) for c in CASES]}}}
    message, timing = model_call(base, model, messages, output_schema=binding_schema)
    binding = parse_json(message["content"])
    if binding != {"template": case["name"], "input": case["input"]}:
        raise ValueError("invalid template binding: " + repr(binding))
    with tempfile.TemporaryDirectory(prefix="splash-research-") as tmp:
        path = Path(tmp) / "input.json"
        path.write_text(json.dumps(binding["input"]))
        result = subprocess.run([str(BINARY), "--once", binding["template"], str(path)],
                                check=True, capture_output=True, text=True, timeout=15)
    execution = json.loads(result.stdout)
    return {"mode": "splash_template", "case": case["name"], "elapsed_s": time.perf_counter() - started,
            "model_calls": [timing], "binding": binding, "execution": execution, "output": execution["output"]}


def tool_loop(case, base, model, expected):
    unique = {t["method"]: t for t in case["tools"]}
    tools = [{"type": "function", "function": {"name": name,
        "description": "Read-only " + name + ". Returns JSON with this schema: " + json.dumps(schema(t["output"])),
        "parameters": schema(t["input"])}} for name, t in unique.items()]
    messages = [{"role": "system", "content":
        "Fill the research dataset using the available tools. Call independent tools together in parallel. "
        "Every tool invocation has a one-call budget, except article which can read each discovered ID once. "
        "Fetch all required sources. Wait for search before fetching its article IDs. Use all complete evidence and preserve source fields. "
        "Return only a JSON DATA INSTANCE matching this schema. Never repeat the schema itself: " + json.dumps(schema(expected)) +
        ". schema_id is '" + case["name"] + ".v1'; status is 'ready' when all tools succeed, otherwise 'partial'. "
        "For stock return_pct=(quote.price/baseline.price-1)*100. For news discovery=search.source and missing=0 if all articles succeeded."},
        {"role": "user", "content": user_request(case)}]
    timings, batches, used = [], [], set()
    started = time.perf_counter()
    for _ in range(6):
        # Enforce exhausted capability budgets in the next offered catalog too.
        # This gives the baseline the same bounded host policy as Splash.
        remaining = {t["method"] for i, t in enumerate(case["tools"]) if i not in used}
        available = [t for t in tools if t["function"]["name"] in remaining]
        message, timing = model_call(base, model, messages, available,
                                    output_schema=None if available else schema(expected))
        timings.append(timing)
        calls = message.get("tool_calls", [])
        if not calls:
            if len(used) != len(case["tools"]):
                raise ValueError("tool loop omitted required evidence")
            return {"mode": "tool_loop", "case": case["name"], "elapsed_s": time.perf_counter()-started,
                    "model_calls": timings, "batch_sizes": batches, "output": parse_json(message["content"])}
        messages.append(message)
        pending = []
        for call in calls:
            name = call["function"]["name"]
            args = json.loads(call["function"]["arguments"])
            matches = [i for i, t in enumerate(case["tools"]) if t["method"] == name and t["input"] == args]
            if len(matches) != 1 or matches[0] in used:
                raise ValueError("unauthorized, duplicate, or invalid fixture tool call: " + json.dumps({"name":name,"arguments":args}))
            if name == "article" and 0 not in used:
                raise ValueError("article fetch before discovery")
            pending.append((call["id"], matches[0]))
        for _, index in pending:
            if index in used:
                raise ValueError("duplicate tool call in batch")
            used.add(index)
        batches.append(len(pending))

        async def dispatch():
            semaphore = asyncio.Semaphore(3)
            async def one(call_id, index):
                async with semaphore:
                    fixture = case["tools"][index]
                    await asyncio.sleep(fixture["delay_ms"] / 1000)
                    return {"role": "tool", "tool_call_id": call_id, "content": json.dumps(fixture["output"])}
            return await asyncio.gather(*(one(*item) for item in pending))
        messages.extend(asyncio.run(dispatch()))
    raise ValueError("model loop exceeded six turns")


def equal(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a-b) < 1e-7
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(equal(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(equal(x, y) for x, y in zip(a, b))
    return a == b


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:30881/v1")
    parser.add_argument("--model", default="qwen3.8-27b")
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fixture-results", type=Path, required=True)
    args = parser.parse_args()
    references = {r["case"]: r["output"] for r in json.loads(args.fixture_results.read_text())["runs"]}
    report = {"model": args.model, "mode": "real_model_fixture_tools", "runs": []}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for case in CASES:
        for round_ in range(args.repeats):
            for mode in (["splash_template", "tool_loop"] if round_ % 2 == 0 else ["tool_loop", "splash_template"]):
                try:
                    run = (template_run(case, args.base_url, args.model) if mode == "splash_template"
                           else tool_loop(case, args.base_url, args.model, references[case["name"]]))
                    run["valid"] = equal(run["output"], references[case["name"]])
                except Exception as error:
                    run = {"case": case["name"], "mode": mode, "valid": False, "error": str(error)}
                run["round"] = round_
                report["runs"].append(run)
                print(case["name"], mode, "valid="+str(run["valid"]), round(run.get("elapsed_s", 0),3), run.get("error", ""), flush=True)
                args.output.write_text(json.dumps(report, indent=2)+"\n")
    report["summary"] = []
    for case in CASES:
        for mode in ["splash_template", "tool_loop"]:
            rows = [r for r in report["runs"] if r["case"] == case["name"] and r["mode"] == mode]
            valid = [r for r in rows if r["valid"]]
            report["summary"].append({"case":case["name"],"mode":mode,"valid":len(valid),"total":len(rows),
                "median_s":statistics.median(r["elapsed_s"] for r in valid) if valid else None,
                "model_call_counts":[len(r["model_calls"]) for r in valid]})
    args.output.write_text(json.dumps(report, indent=2)+"\n")


if __name__ == "__main__":
    main()
