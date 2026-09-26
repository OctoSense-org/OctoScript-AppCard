#!/usr/bin/env python3
"""Render every compiled scene of a flow project headless and compare it with
its page image: per-band pixel differences, a side-by-side, an ink-presence
probe for every text widget, and a JSON summary.

    compare_screens.py --project examples/calendar --pages eval-inputs/pages \
        --out examples/calendar/evidence/screenshots [--host <beauty-host>] [scene ids...]

Evidence about pixels, not an approval. Read the side-by-sides with
`view_image`; the numbers only tell you where to look.

Why it is shaped this way (from the calendar evaluation):
- one fresh host process per scene, with a fresh request nonce: the host's
  live reload is not trustworthy, and a stale grab was twice reported as a
  real defect;
- per-band means, not one whole-page mean: a wrong background in one band
  hid behind a whole-page number for a while;
- an ink probe at each text widget's rect: `/snap` reports a widget with the
  right text and rect even when nothing paints (alignx out of range, a box
  of zero height), so a structural pass is not a rendered pass.
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.parse
import uuid
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw

DEFAULT_HOST = Path.home() / 'home/octosense-org/octoscript-makepad/target/release/beauty-host'
ARTBOARD = (406, 776)
SCALE = 2

# 2x bands over the 812x1552 frame. Coarse on purpose: they localise a
# difference to a region a person can look at.
BANDS = {
    'status_bar': (0, 0, 812, 54),
    'nav': (0, 100, 812, 180),
    'body_top': (0, 180, 812, 700),
    'list': (0, 700, 812, 1400),
    'tab_bar': (0, 1380, 812, 1552),
}


def port_from(log):
    for line in log.read_text(errors='ignore').splitlines():
        if 'listening on 127.0.0.1:' in line:
            return line.split('listening on 127.0.0.1:')[1].split()[0]
    return None


def curl(url, timeout=90):
    raw = subprocess.check_output(['curl', '-s', '--max-time', str(timeout), url])
    return json.loads(raw or b'{}')


class Host:
    def __init__(self, binary, workdir):
        self.binary = Path(binary)
        self.workdir = Path(workdir)
        self.proc = None
        self.port = None
        self.log = self.workdir / 'host.log'
        self.request = self.workdir / 'request.json'

    def start(self, directory, nonce, timeout=40):
        self.stop()
        self.request.write_text(json.dumps({
            'card': str(directory / 'page.card'),
            'data': str(directory / 'page.data.json'),
            'format': 'l0-kit',
            'kit_dir': str(directory / 'kit'),
            'width': ARTBOARD[0], 'height': ARTBOARD[1],
            'result': str(self.workdir / 'native.json'),
            'layout': str(self.workdir / 'layout.json'),
            'actions': str(self.workdir / 'actions.json'),
            'nonce': nonce,
        }))
        self.log.unlink(missing_ok=True)
        env = {**os.environ, 'MAKEPAD_HIDE_WINDOWS': '1', 'BEAUTY_REQUEST': str(self.request)}
        self.proc = subprocess.Popen([str(self.binary), '--remote'], env=env,
                                     stdout=self.log.open('w'), stderr=subprocess.STDOUT)
        deadline = time.time() + timeout
        while time.time() < deadline:
            if self.log.exists():
                self.port = port_from(self.log)
                if self.port:
                    time.sleep(6)  # let the scene mount and its icons resolve
                    return
            if self.proc.poll() is not None:
                raise SystemExit('host exited early; see ' + str(self.log))
            time.sleep(0.5)
        raise SystemExit('host did not report a port within %ss' % timeout)

    def stop(self):
        if self.port:
            subprocess.run(['curl', '-s', '--max-time', '5', f'localhost:{self.port}/quit'], capture_output=True)
            time.sleep(1)
        if self.proc and self.proc.poll() is None:
            self.proc.kill()
        self.proc, self.port = None, None

    def grab(self):
        return curl(f'localhost:{self.port}/g')

    def snap(self, query):
        return curl(f'localhost:{self.port}/snap?' + urllib.parse.urlencode({'q': query, 'all': 1}))

    def host_log_problems(self):
        text = self.log.read_text(errors='ignore')
        return [l.strip() for l in text.splitlines()
                if 'BEAUTY_ERROR' in l or 'HTTP load failed' in l or 'HTTP request error' in l
                or 'font miss' in l]


def mean_diff(a, b):
    diff = ImageChops.difference(a.convert('RGB'), b.convert('RGB'))
    hist = diff.histogram()
    n = sum(hist[i] for i in range(256))
    per = [sum(i * hist[ch * 256 + i] for i in range(256)) for ch in range(3)]
    return sum(per) / (3 * n) if n else 0.0


def region_diff(a, b, box):
    return mean_diff(a.crop(box), b.crop(box))


def ink_present(native, rect, background):
    """Does the widget's rect contain pixels that are not the page background?

    `rect` is in artboard points; the frame is 2x.
    """
    x, y, w, h = [v * SCALE for v in rect]
    if w <= 0 or h <= 0:
        return False, 0.0
    crop = native.convert('RGB').crop((int(x), int(y), int(x + w), int(y + h)))
    if crop.size[0] == 0 or crop.size[1] == 0:
        return False, 0.0
    bg = Image.new('RGB', crop.size, background)
    diff = ImageChops.difference(crop, bg).convert('L')
    hist = diff.histogram()
    total = sum(hist)
    ink = sum(hist[24:])  # pixels at least 24/255 away from the background
    share = ink / total if total else 0.0
    return share > 0.01, round(share, 4)


def _dominant_ink(crop):
    """Mean colour of the pixels that are not the crop's own background
    (its median colour), and the share of such pixels. Local, so a grey
    desktop card and a white phone page are treated alike."""
    a = np.asarray(crop.convert('RGB')).astype(int)
    if a.size == 0:
        return None, 0.0
    bg = np.median(a.reshape(-1, 3), axis=0)
    dist = np.abs(a - bg).max(axis=2)
    mask = dist > 40
    share = float(mask.mean())
    if mask.sum() == 0:
        return None, 0.0
    return tuple(int(v) for v in a[mask].mean(axis=0)), share


def text_colour_probe(native, page, rect):
    """Per text widget: does the ink have the page's colour and weight?

    Round 2 of the calendar evaluation: a date header drawn red and bold
    where the page has grey regular passed every band number and every
    presence probe. Colour distance and ink coverage per element catch it.
    """
    x, y, w, h = [v * SCALE for v in rect]
    box = (int(x), int(y), int(x + w), int(y + h))
    n_ink, n_share = _dominant_ink(native.crop(box))
    p_ink, p_share = _dominant_ink(page.crop(box))
    if n_ink is None or p_ink is None:
        return None
    distance = max(abs(a - b) for a, b in zip(n_ink, p_ink))
    weight = n_share / p_share if p_share else 0.0
    problem = None
    if distance > 60:
        problem = f'colour {rgb(n_ink)} vs page {rgb(p_ink)}'
    elif weight > 1.45 or weight < 0.65:
        problem = f'ink coverage {n_share:.3f} vs page {p_share:.3f} (weight or size)'
    return problem


def rgb(c):
    return '#%02X%02X%02X' % tuple(c)


def diff_regions(native, page, threshold=40, block=8, min_blocks=1, limit=16):
    """Where the frames differ, as regions: the mask of pixels more than
    `threshold` apart is tiled into `block` px cells, cells with over a
    quarter of their pixels different are grouped by adjacency, and each
    group is reported with its bounding box in artboard points and the two
    frames' mean colours inside it. A missing event dot or badge is a
    small region a band mean never shows.
    """
    a = np.asarray(native.convert('RGB')).astype(int)
    b = np.asarray(page.convert('RGB')).astype(int)
    if a.shape != b.shape:
        return []
    mask = np.abs(a - b).max(axis=2) > threshold
    H, W = mask.shape
    gh, gw = H // block, W // block
    cells = mask[:gh * block, :gw * block].reshape(gh, block, gw, block).mean(axis=(1, 3)) > 0.25
    seen = np.zeros_like(cells, dtype=bool)
    regions = []
    for gy in range(gh):
        for gx in range(gw):
            if not cells[gy, gx] or seen[gy, gx]:
                continue
            stack = [(gy, gx)]
            seen[gy, gx] = True
            members = []
            while stack:
                cy, cx = stack.pop()
                members.append((cy, cx))
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1), (cy - 1, cx - 1), (cy - 1, cx + 1), (cy + 1, cx - 1), (cy + 1, cx + 1)):
                    if 0 <= ny < gh and 0 <= nx < gw and cells[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        stack.append((ny, nx))
            if len(members) < min_blocks:
                continue
            ys = [m[0] for m in members]
            xs = [m[1] for m in members]
            y0, y1 = min(ys) * block, (max(ys) + 1) * block
            x0, x1 = min(xs) * block, (max(xs) + 1) * block
            n_mean = a[y0:y1, x0:x1].reshape(-1, 3).mean(axis=0)
            p_mean = b[y0:y1, x0:x1].reshape(-1, 3).mean(axis=0)
            regions.append({
                'rect_pt': [round(x0 / SCALE, 1), round(y0 / SCALE, 1), round((x1 - x0) / SCALE, 1), round((y1 - y0) / SCALE, 1)],
                'cells': len(members),
                'colour_distance': int(np.abs(n_mean - p_mean).max()),
                'native': rgb(n_mean.astype(int)),
                'page': rgb(p_mean.astype(int)),
            })
    # Biggest first, then the most different in colour: a missing red dot is
    # one cell with a large colour distance and belongs above glyph fuzz.
    regions.sort(key=lambda r: (-min(r['cells'], 8), -r['colour_distance']))
    return regions[:limit]


def app_frame(grab, crop, page_size):
    """A running-app grab cropped to the artboard and scaled to the page.
    The shell draws its own status bar above the app and a home indicator
    below it; `crop` is x,y,w,h in grab pixels of the artboard area."""
    x, y, w, h = crop
    return grab.convert('RGB').crop((x, y, x + w, y + h)).resize(page_size, Image.LANCZOS)


def side_by_side(native, page, out, label):
    w, h = page.size
    canvas = Image.new('RGB', (w * 2 + 12, h + 28), (24, 24, 26))
    canvas.paste(page.convert('RGB'), (0, 28))
    canvas.paste(native.convert('RGB').resize(page.size), (w + 12, 28))
    draw = ImageDraw.Draw(canvas)
    draw.text((6, 8), 'page (reference)', fill=(240, 240, 240))
    draw.text((w + 18, 8), f'native: {label}', fill=(240, 240, 240))
    canvas.save(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('scenes', nargs='*', help='scene ids from the manifest; default all')
    parser.add_argument('--project', required=True, type=Path)
    parser.add_argument('--manifest', type=Path, help='default <project>/image-to-appcard-flow.json')
    parser.add_argument('--pages', required=True, type=Path, help='directory of page-NN.png references')
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--host', type=Path, default=DEFAULT_HOST)
    parser.add_argument('--background', default='#FFFFFF', help='page background for the ink probe')
    parser.add_argument('--app-grab', type=Path, help='compare ONE running-app grab (from the shell) with the scene instead of rendering it')
    parser.add_argument('--app-crop', default=None, help='x,y,w,h of the artboard inside the app grab (default: below an 88 px shell status bar, full width, page aspect)')
    parser.add_argument('--port', help='instrument port of the running app, for --forbid-text')
    parser.add_argument('--forbid-text', action='append', default=[],
                        help='text that must NOT be a widget in the running app (e.g. the page mock status bar clock 09:41); needs --port')
    args = parser.parse_args()

    project = args.project.resolve()
    manifest = json.loads((args.manifest or project / 'image-to-appcard-flow.json').read_text())
    scenes = [s for s in manifest['scenes'] if not args.scenes or s['id'] in args.scenes]
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    work = out / '.host'
    work.mkdir(exist_ok=True)
    host = Host(args.host, work)
    bg = tuple(int(args.background.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

    summary = []
    if args.app_grab:
        # The running app, one screen at a time: no host to launch, the
        # grab is the evidence. Forbidden texts are looked up on the app's
        # own instrument when a port is given.
        if len(scenes) != 1:
            raise SystemExit('--app-grab compares one scene: name it')
        scene = scenes[0]
        page = Image.open(args.pages / f'page-{int(scene["id"]):02d}.png')
        grab = Image.open(args.app_grab)
        if args.app_crop:
            crop = [int(v) for v in args.app_crop.split(',')]
        else:
            w = grab.size[0]
            crop = [0, 88, w, int(w * page.size[1] / page.size[0])]
        native = app_frame(grab, crop, page.size)
        record = {'scene': scene['id'], 'design_id': scene['design_id'], 'app_grab': str(args.app_grab), 'app_crop': crop}
        record['mean_diff'] = round(mean_diff(native, page), 2)
        record['bands'] = {name: round(region_diff(native, page, box), 2) for name, box in BANDS.items()}
        record['diff_regions'] = diff_regions(native, page)
        forbidden = []
        if args.port:
            for text in args.forbid_text:
                hits = [w for w in curl(f'localhost:{args.port}/snap?' + urllib.parse.urlencode({'q': text, 'all': 1})).get('s', [])
                        if (w.get('t') or '').strip() == text]
                if hits:
                    forbidden.append({'text': text, 'widgets': len(hits), 'rect': hits[0].get('r')})
        record['forbidden_text_widgets'] = forbidden
        pair = out / f'{scene["design_id"]}-app-compare.png'
        side_by_side(native, page, pair, scene['design_id'] + ' (app)')
        record['compare'] = str(pair)
        (out / 'app-comparison.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({k: v for k, v in record.items() if k != 'compare'}, ensure_ascii=False))
        print(f'\nside-by-side: {pair}; the diff regions above are where to look.')
        return

    for scene in scenes:
        directory = (project / scene['directory']).resolve()
        page_no = f'{int(scene["id"]):02d}'
        page_path = args.pages / f'page-{page_no}.png'
        record = {'scene': scene['id'], 'design_id': scene['design_id']}
        try:
            host.start(directory, uuid.uuid4().hex)
            got = host.grab()
            # Every text widget the host placed: does it actually paint?
            widgets = host.snap('Label').get('s', []) + host.snap('Text').get('s', [])
            problems = host.host_log_problems()
        finally:
            host.stop()
        png = got.get('png')
        if not png or not Path(png).is_file():
            record['error'] = 'no screenshot'
            summary.append(record)
            print(json.dumps(record), flush=True)
            continue
        native = Image.open(png)
        page = Image.open(page_path)
        record['size'] = list(native.size)
        record['mean_diff'] = round(mean_diff(native.resize(page.size), page), 2)
        record['bands'] = {name: round(region_diff(native.resize(page.size), page, box), 2) for name, box in BANDS.items()}
        blank = []
        wrong_ink = []
        seen = set()
        fitted = native.resize(page.size)
        for w in widgets:
            wid, rect, text = w.get('i'), w.get('r'), (w.get('t') or '').strip()
            # A zero-size rect is the host's own hidden label, not a scene widget.
            if not rect or not text or wid in seen or rect[2] <= 0 or rect[3] <= 0:
                continue
            seen.add(wid)
            present, share = ink_present(native, rect, bg)
            if not present:
                blank.append({'id': wid, 'text': text[:40], 'rect': rect, 'ink': share})
                continue
            problem = text_colour_probe(fitted, page, rect)
            if problem:
                wrong_ink.append({'id': wid, 'text': text[:40], 'rect': rect, 'problem': problem})
        record['text_widgets'] = len(seen)
        record['blank_text_widgets'] = blank
        record['wrong_ink_text_widgets'] = wrong_ink
        record['diff_regions'] = diff_regions(fitted, page)
        record['host_problems'] = problems
        shot = out / f'{scene["design_id"]}-native.png'
        native.save(shot)
        pair = out / f'{scene["design_id"]}-compare.png'
        side_by_side(native, page, pair, scene['design_id'])
        record['native'] = str(shot)
        record['compare'] = str(pair)
        summary.append(record)
        print(json.dumps({k: v for k, v in record.items() if k not in ('native', 'compare')}, ensure_ascii=False), flush=True)

    (out / 'comparison.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    ok = [r for r in summary if 'mean_diff' in r]
    print('\nscene  mean   worst band          blank   wrong ink   regions   host problems')
    for r in ok:
        worst = max(r['bands'].items(), key=lambda kv: kv[1])
        print(f"{r['scene']:>5}  {r['mean_diff']:5.1f}  {worst[0]:<10} {worst[1]:6.1f}   "
              f"{len(r['blank_text_widgets']):>3}/{r['text_widgets']:<3}   {len(r['wrong_ink_text_widgets']):>5}      "
              f"{len(r['diff_regions']):>4}      {len(r['host_problems'])}")
    for r in ok:
        for w in r['wrong_ink_text_widgets']:
            print(f"  scene {r['scene']}: text {w['id']} {w['text']!r}: {w['problem']}")
        for g in r['diff_regions'][:4]:
            print(f"  scene {r['scene']}: region at {g['rect_pt']} pt — native {g['native']} vs page {g['page']}")
    print(f'\nside-by-sides in {out}; look at each with view_image before deciding anything.')


if __name__ == '__main__':
    main()
