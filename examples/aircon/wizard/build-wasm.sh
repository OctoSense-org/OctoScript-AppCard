#!/usr/bin/env bash
set -euo pipefail
WIZARD_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APPCARD_ROOT="$(cd "$WIZARD_ROOT/../.." && pwd)"
OCTOSENSE_WORKSPACE="$(PYTHONPATH="$APPCARD_ROOT/lab" python3 -c 'from core.native_paths import WORKSPACE; print(WORKSPACE)')"
export OCTOSENSE_WORKSPACE
WIZARD_HOST="$WIZARD_ROOT/wizard/wasm-host"
mkdir -p "$WIZARD_HOST/resources/service"
for weight in Regular Medium Bold; do
  cp "$WIZARD_ROOT/fonts/NotoSansSC-$weight.ttf" "$WIZARD_HOST/resources/service/"
done
cd "$WIZARD_HOST"
"$OCTOSENSE_WORKSPACE/makepad/target/release/cargo-makepad" wasm --no-threads build -p octosense-wizard --release
"$APPCARD_ROOT/flows/image-lib/.venv/bin/python" - "$WIZARD_ROOT" <<'PY'
from pathlib import Path
import hashlib,json,re,shutil,sys,tempfile,subprocess
from fontTools.ttLib import TTFont
root=Path(sys.argv[1]);host=root/'wizard/wasm-host'
sys.path.insert(0,str(root.parents[1]/'flows'))
from core.native_paths import repository,WORKSPACE
build=host/'target/makepad-wasm-app/release/octosense-wizard'
published=root/'wizard/wasm-dist'
dist=Path(tempfile.mkdtemp(prefix='.wasm-dist-',dir=root/'wizard'))
shutil.copytree(build,dist,dirs_exist_ok=True)
wasm_name=re.search(r"'\./(octosense-wizard[^']*\.wasm)'",(build/'index.html').read_text()).group(1)
shutil.copy2(build/wasm_name,dist/'octosense-wizard.wasm')
for path in dist.glob('octosense-wizard.*.wasm'):path.unlink()
# Only these native fallback faces are requested by this fixed card kit.
# The complete Noto Sans SC face is embedded and installed by App::Startup.
fallback_fonts={'IBMPlexSans-Text.ttf','NotoSans-Regular.ttf','jetbrains_mono_variable.ttf','NotoColorEmoji.ttf'}
for path in list(dist.rglob('*')):
    if path.is_file() and path.suffix.lower() in {'.ttf','.otf','.woff','.woff2'}:
        if path.parent!=dist/'makepad_widgets/resources' or path.name not in fallback_fonts:path.unlink()
for path in sorted(dist.rglob('*'),reverse=True):
    if path.is_dir() and not any(path.iterdir()):path.rmdir()
web=dist/'makepad_platform/web.js'
web_source=web.read_text();web_before=hashlib.sha256(web_source.encode()).hexdigest()
focus_patches=[
    ("embedded-blur-does-not-recapture-focus",
     "ta.addEventListener('blur',e=>{\nthis.focus_keyboard_input();\n})",
     "ta.addEventListener('blur',e=>{\nif(window.self===window.top)this.focus_keyboard_input();\n})"),
    ("initial-focus-prevents-parent-scroll","ta.focus();","ta.focus({preventScroll:true});"),
    ("keyboard-focus-prevents-parent-scroll","this.text_area.focus();","this.text_area.focus({preventScroll:true});")]
for name,before,after in focus_patches:
    if web_source.count(before)!=1:raise RuntimeError('Makepad web focus patch requires review: '+name)
    web_source=web_source.replace(before,after)
web.write_text(web_source)
for name in ('index.html','bridge.mjs'):
    shutil.copy2(host/name,dist/name)
for card in list((root/'cards').glob('aircon-*'))+list((root/'service-cards').glob('*/*')):
    if not (card/'contract.json').is_file():continue
    name=json.loads((card/'contract.json').read_text())['id']
    if (card/'assets').is_dir():shutil.copytree(card/'assets',dist/'card-assets'/name/'assets',dirs_exist_ok=True)
licenses=dist/'licenses';licenses.mkdir(exist_ok=True)
shutil.copy2(repository('makepad')/'LICENSE',licenses/'Makepad-MIT.txt')
shutil.copy2(repository('splash')/'LICENSE',licenses/'Splash-MIT.txt')
shutil.copy2(root/'fonts/OFL.txt',licenses/'NotoSansSC-OFL.txt')
font_notices=[]
for name in sorted(fallback_fonts):
    font=TTFont(repository('makepad')/'widgets/resources'/name)
    metadata={record.nameID:record.toUnicode() for record in font['name'].names if record.nameID in (0,13,14)}
    font_notices.append(name+'\n'+'\n'.join(metadata[key] for key in (0,13,14) if key in metadata))
(licenses/'Bundled-fonts.txt').write_text('\n\n'.join(font_notices)+'\n\n'+(root/'fonts/OFL.txt').read_text())
(dist/'THIRD_PARTY_NOTICES.md').write_text('''# Third-party notices

Makepad widgets, renderer, browser loader and WASM bridge are from the pinned Makepad checkout. The MIT license and copyright are in `licenses/Makepad-MIT.txt`.

Splash / splash-ui-l0 are from the pinned Splash checkout. The distributed MIT license is in `licenses/Splash-MIT.txt`. Splash-Makepad (splash-render, splash-node, splash-widgets and splash-makepad) declares “MIT OR Apache-2.0” in its README License section; this distribution selects MIT and includes the matching Makepad MIT text.

The complete Noto Sans SC Regular font is embedded in the WASM module. Its original copyright and SIL Open Font License 1.1 are in `licenses/NotoSansSC-OFL.txt`. The separate IBM Plex Sans, Noto Sans, JetBrains Mono and Noto Color Emoji fallback fonts retain their embedded copyright/license metadata, copied to `licenses/Bundled-fonts.txt`, together with the SIL OFL text.

No fonts have been converted to bitmap text. Card photographs and illustrations are the project's generated source assets. Exact packaged source hashes are in `build.json`.
''')
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
wasm_sha=sha(dist/'octosense-wizard.wasm')
for name,before,after in [
    ('index.html','src="./bridge.mjs"',f'src="./bridge.mjs?v={wasm_sha}"'),
    ('bridge.mjs',"'./octosense-wizard.wasm'",f"'./octosense-wizard.wasm?v={wasm_sha}'")]:
    path=dist/name;source=path.read_text()
    if source.count(before)!=1:raise RuntimeError('WASM cache version stamping requires review: '+name)
    path.write_text(source.replace(before,after))
receipt={'renderer':'Makepad/WASM','threads':False,'source':'Pinned working Makepad + Splash, in-memory L0/kit lowering',
         'font_backend':'SDF/SLUG; compile-time no-atomics branch does not start an MSDF worker',
         'generated_runtime_patches':{'makepad_platform/web.js':{'source_sha256':web_before,'packaged_sha256':sha(web),'operations':[name for name,_,_ in focus_patches]}},
         'revisions':{name:subprocess.check_output(['git','-C',str(repository(name)),'rev-parse','HEAD'],text=True).strip() for name in ('makepad','splash','splash-makepad')},
         'embedded_fonts':{'NotoSansSC-Regular.ttf':sha(root/'fonts/NotoSansSC-Regular.ttf')},
         'asset_policy':'Browser validates iframe same-origin card-assets; WASM renderer permits only loopback and explicit Octosense HTTPS card-assets bases; native renderer remains loopback-only',
         'wasm_sha256':wasm_sha,'cache_version':wasm_sha,
         'sources':{str(p.relative_to(root)):sha(p) for p in [host/'Cargo.toml',host/'Cargo.lock',host/'src/main.rs',host/'bridge.mjs',root/'wizard/build-wasm.sh']},
         'pipeline_sources':{str(p.relative_to(WORKSPACE)):sha(p) for p in [repository('makepad')/'draw/src/text/fonts.rs',repository('makepad')/'platform/src/os/web/web.js',repository('splash-makepad')/'crates/splash-makepad/src/design.rs']},
         'files':{str(p.relative_to(dist)):sha(p) for p in sorted(dist.rglob('*')) if p.is_file() and p.name!='build.json'}}
(dist/'build.json').write_text(json.dumps(receipt,indent=2)+'\n')
if published.exists():shutil.rmtree(published)
dist.rename(published)
print(json.dumps({'directory':str(published),'wasm_bytes':(published/'octosense-wizard.wasm').stat().st_size,'sha256':receipt['wasm_sha256']}))
PY
