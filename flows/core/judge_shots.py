#!/usr/bin/env python3
"""Strict design-match over one rail's captures, resumable per screen.

Usage: judge_shots.py --kit atro --rail desktop|android|ohos [--redo name]
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import collections
import fcntl
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import io
import json
import pathlib
import statistics
import sys
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
from core import llm as B  # noqa: E402
from core import kitconf  # noqa: E402

PROMPT = (
    "Read {t} (the DESIGN) and {x} (an IMPLEMENTATION screenshot). You are a "
    "strict design reviewer. Judge whether the implementation reproduces the "
    "design at equal pixel dimensions (reference: RGBA Lanczos, white window matte v2). "
    "Compare VISUAL DESIGN: typography, font sizing and weight, colors, "
    "button/control styling, imagery, gradients, shadows and effects. Geometry, "
    "hierarchy, alignment, spacing and clipping have a separate measured Studio "
    "structural gate and your score cannot override its failures. Content matching is NOT "
    "sufficient. Return ONLY JSON: "
    '{{"design_match": 1-10, "verdict": "accept"|"rework"|"reject", '
    '"worst": "<=12 words"}}')


def comparison_reference(target, capture, output):
    """Match review scale while preserving the original Sketch export."""
    with Image.open(capture) as im:size=im.size
    with Image.open(target) as im:
        # Sketch rounds a fractional export canvas up; Studio rounds its
        # logical dimensions to the nearest device pixel. Allow one pixel of
        # that quantization, but never normalize a genuinely stretched frame.
        width_error=abs(im.width*size[1]/im.height-size[0])
        height_error=abs(im.height*size[0]/im.width-size[1])
        if abs(im.width/im.height-size[0]/size[1])>.001 and min(width_error,height_error)>1.000001:
            raise ValueError('reference and capture aspect ratios differ')
        rgba=im.convert('RGBA')
        if im.size!=size:rgba=rgba.resize(size,Image.Resampling.LANCZOS)
        # Sketch may omit its artboard background from PNG export. The native
        # host and side-by-side gallery use a white window behind those pixels.
        Image.alpha_composite(Image.new('RGBA',size,'white'),rgba).save(output)
    return output


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    rail = sys.argv[sys.argv.index("--rail") + 1] if "--rail" in sys.argv else "desktop"
    res = HERE / kit["verdicts"][rail]
    res.parent.mkdir(exist_ok=True)
    # Concurrent invocations must read the latest rows after the previous
    # writer finishes, including a full run following a focused repair.
    with res.with_suffix('.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        judge(kit,rail,res)


def judge(kit,rail,res):
    shots = kit[f"{rail}_dir"]
    rows = [json.loads(l) for l in res.open()] if res.exists() else []
    if "--redo" in sys.argv:
        redo = sys.argv[sys.argv.index("--redo") + 1]
        rows = [r for r in rows if redo not in r["screen"]]
    previous = {r["screen"]: r for r in rows}
    only=[sys.argv[i+1] for i,arg in enumerate(sys.argv[:-1]) if arg=='--only']
    selected=[n for n in kit['screens'] if not only or any(p in n for p in only)]
    if not selected:raise SystemExit('no configured screens match --only')
    workers=int(sys.argv[sys.argv.index('--workers')+1]) if '--workers' in sys.argv else 3
    if not 1<=workers<=8:raise SystemExit('--workers must be between 1 and 8')
    def save():
        # Preserve completed reviews for other screens during a partial repair
        # or a later timeout. Their input hashes still govern acceptance.
        result=[previous[n] for n in kit['screens'] if n in previous]
        temporary=res.with_suffix('.pending.jsonl')
        temporary.write_text(''.join(json.dumps(r)+'\n' for r in result))
        temporary.replace(res)
    rows = []
    jobs=[]
    for name in selected:
        t = (kit["targets_dir"] / f"{name}.png").resolve()
        x = (shots / f"{name}.png").resolve()
        if not t.exists() or not x.exists():
            raise SystemExit(f"{name}: missing target or capture; cannot judge this rail")
        suffix = 'splash' if kit.get('input_format') == 'design' else 'card'
        if x.stat().st_mtime < (kit["cards_dir"] / f"{name}.{suffix}").stat().st_mtime:
            raise SystemExit(f"{name}: stale capture; rerender before judging")
        target_bytes,capture_bytes=t.read_bytes(),x.read_bytes()
        inputs = hashlib.sha256(target_bytes + capture_bytes + PROMPT.encode()).hexdigest()
        if previous.get(name, {}).get("inputs") == inputs:
            rows.append(previous[name])
            continue
        # Freeze both inputs for this verdict. A repair/capture can finish
        # while the visual reviewer is reading; its evidence must not change
        # underneath the content hash attached to the verdict.
        review_dir=shots/'.visual-inputs'/inputs
        review_dir.mkdir(parents=True,exist_ok=True)
        review_capture=review_dir/'native.png'
        review_capture.write_bytes(capture_bytes)
        review_target=comparison_reference(io.BytesIO(target_bytes),review_capture,review_dir/'reference.png')
        jobs.append((name,inputs,review_target,review_capture))
    def review(job):
        name,inputs,review_target,review_capture=job
        out = B.claude_text(PROMPT.format(t=review_target, x=review_capture))
        v = json.JSONDecoder().raw_decode(out[out.index("{"):])[0]
        if (type(v.get("design_match")) is not int or not 1 <= v["design_match"] <= 10
                or v.get("verdict") not in ("accept", "rework", "reject")):
            raise ValueError(f"{name}: invalid judge result {v!r}")
        return {"screen": name, "inputs": inputs,
            'comparison_reference':str(review_target),
            'comparison_capture':str(review_capture),
            'comparison_reference_sha256':hashlib.sha256(review_target.read_bytes()).hexdigest(),**v}
    # Freeze all pairs first. Only this thread writes verdicts; workers read
    # independent immutable files. Persist a batch's successes before stopping
    # on any error, so a timeout cannot lose other completed judgments.
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for offset in range(0,len(jobs),workers):
            errors=[]
            futures=[pool.submit(review,job) for job in jobs[offset:offset+workers]]
            for future in as_completed(futures):
                try:row=future.result()
                except Exception as error:
                    errors.append(error);continue
                rows.append(row);name=row['screen'];previous[name]=row
                save()
                print(f"{name:<28} {row['design_match']:>2}/10 {row['verdict']:<7} "
                    f"{str(row['worst'])[:46]}",flush=True)
            if errors:raise RuntimeError(f'visual review batch failed: {errors[0]}')
    save()
    if rows:
        print(f"\n{rail}: median "
              f"{statistics.median(r['design_match'] for r in rows)} · "
              f"{dict(collections.Counter(r['verdict'] for r in rows))}")


if __name__ == "__main__":
    main()
