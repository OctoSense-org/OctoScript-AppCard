"""The pipeline's only LLM surface, vendored so flows/core stands alone.

Two callers, one contract: `claude_text` runs a single prompt through the
claude CLI with Read as its only tool (the vision judge and the card author
both hand it file paths to look at); `strip_fence` peels a fenced block off
a reply. Extracted from flows/style-factory/batch_styles.py, which carries a
whole research bench this pipeline does not need.
"""
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent


def claude_text(prompt, timeout=900):
    try:
        r = subprocess.run(
            ["claude", "-p", prompt, "--model", "opus", "--allowedTools", "Read",
             "--output-format", "json"],
            capture_output=True, text=True, timeout=timeout, cwd=HERE)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"claude exceeded its {timeout}s timeout") from None
    if r.returncode:
        raise RuntimeError(f"claude failed ({r.returncode}): {r.stderr[-1000:]}")
    response = json.loads(r.stdout)
    if response.get("is_error") or not response.get("result"):
        raise RuntimeError(f"claude returned no successful result: {response}")
    return response["result"]


def strip_fence(text, lang=""):
    m = re.search(rf"```{lang}[^\n]*\n(.*?)```", text, re.S)
    return m.group(1) if m else text
