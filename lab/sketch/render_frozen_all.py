import pathlib, sys, os, socket, subprocess, time
sys.path.insert(0, str(pathlib.Path('../gates').resolve()))
os.environ['GATE_WINDOW'] = '375x902'
import shoot; shoot.SIZE = '375x902'
IMG = pathlib.Path('/private/tmp/claude-501/-Users-yuechen-home-Splash/df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images')
s = socket.socket()
if s.connect_ex(('127.0.0.1', 8787)) != 0:
    subprocess.Popen(['python3','-m','http.server','8787'], cwd=IMG,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
s.close()
t0 = time.time()
todo = [d for d in sorted(pathlib.Path('frozen').glob('*.dsl'))
        if not d.with_suffix('.png').exists()]
for i, d in enumerate(todo, 1):
    ok = shoot.shoot(d, d.with_suffix('.png'), None, data=None, crop_bottom=90)
    el = time.time() - t0
    print(f"[{i}/{len(todo)}] {d.stem[:32]:<32} {'ok' if ok else 'FAIL'} "
          f"[{el/60:.0f}m ~{el/i*(len(todo)-i)/60:.0f}m left]", flush=True)
