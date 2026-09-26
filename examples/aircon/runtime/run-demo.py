#!/usr/bin/env python3
"""Open the native service demo through its isolated Makepad Studio RunItem."""
from pathlib import Path
import argparse, fcntl, json, os, socket, subprocess, sys, time

ROOT = Path(__file__).resolve().parents[1]
os.environ['BEAUTY_BRIDGE'] = 'http://127.0.0.1:8182'
sys.path.insert(0, str(ROOT.parents[1] / 'lab/image-to-appcard'))
sys.path.insert(0, str(ROOT / 'runtime'))
sys.path.insert(0, str(ROOT / 'service'))
from studio import launch, request
from service_session import Session
from controller import demo_states

def listening(port):
    try:
        with socket.create_connection(('127.0.0.1', port), timeout=.3): return True
    except OSError: return False

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frame', type=int, choices=range(1, 13), default=6)
    parser.add_argument('--reuse-build', action='store_true', help='Reuse the current isolated demo RunItem')
    args = parser.parse_args()
    directory = ROOT / 'runtime/demo-session'
    directory.mkdir(parents=True, exist_ok=True)
    lock = (directory / 'watcher.lock').open('w')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit('这个演示会话已在运行')
    children, logs = [], []
    build = None
    try:
        for port, script in [(8012, 'start-studio.sh'), (8182, 'start-bridge.sh'), (8170, 'start-artwork.sh')]:
            if listening(port): continue
            log = (directory / (script + '.log')).open('a')
            logs.append(log)
            child = subprocess.Popen(['bash', str(ROOT / 'runtime' / script)], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
            children.append(child)
            deadline = time.monotonic() + 30
            while not listening(port):
                if child.poll() is not None or time.monotonic() > deadline:
                    raise RuntimeError(f'{script} did not start; see {log.name}')
                time.sleep(.2)
        if args.reuse_build:
            builds = request('ListBuilds', [], 'Builds')['builds']
            matches = [b for b in builds if b.get('package') == 'octos-ux-image-studio']
            if matches: build = matches[-1]['build_id']
        if build is None: build = launch()
        session = Session(directory, build_id=build)
        session.start(demo_states()[0][args.frame])
        request('RunViewResize', {'build_id': build, 'window_id': 0,
                                 'width': 406, 'height': 776, 'dpi': 2.0})
        print(json.dumps({'native_demo': 'Makepad Studio :8012', 'build_id': build,
                          'frame': args.frame, 'session': str(directory),
                          'note': '本地服务演示；Ctrl+C 结束。付款仅生成模拟回执'}, ensure_ascii=False), flush=True)
        session.watch()
    except KeyboardInterrupt:
        pass
    finally:
        if build is not None:
            try: request('ClearBuild', {'build_id': build})
            except (OSError, RuntimeError): pass
        for child in reversed(children):
            child.terminate()
            try: child.wait(timeout=5)
            except subprocess.TimeoutExpired: child.kill()
        for log in logs: log.close()
        lock.close()

if __name__ == '__main__': main()
