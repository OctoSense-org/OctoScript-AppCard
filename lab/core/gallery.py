#!/usr/bin/env python3
"""Build a local comparison gallery using each rail's actual captures."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import argparse
import html
import json
import os
import pathlib
from core import kitconf
from core import gate_visual
from core.repair_feedback import collect

HERE = pathlib.Path(__file__).resolve().parent


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--kit', required=True)
    p.add_argument('--rail', default='splash_makepad')
    args = p.parse_args()
    kit = kitconf.load(args.kit)
    out = kit[f'{args.rail}_dir']/'gallery.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    verdict_file = HERE/kit['verdicts'][args.rail]
    verdicts = ({r['screen']:r for r in map(json.loads, verdict_file.read_text().splitlines())}
                if verdict_file.exists() else {})
    if args.rail == 'splash_makepad':
        feedback = json.loads(collect(kit).read_text())
        visual = {r['screen']: r['visual'] for r in feedback['screens']}
        implementation = feedback['composition']
        compositions = {r['screen']: r['composition'] for r in feedback['screens']}
        policy = json.loads((out.parent/'composition-gate.json').read_text())
    else:
        visual = {r['screen']:r for r in gate_visual.evaluate(kit, args.rail)}
        implementation, compositions, policy = None, {}, None
    def esc(value): return html.escape(str(value), quote=True)
    title = f"{kit['name']} · pipeline validation"
    composition_html = ''
    if implementation:
        counts = ' · '.join(f'{k}: {v:,}' for k,v in implementation['node_counts'].items())
        composition_html = (f"<p><strong>Composition:</strong> {esc(implementation['composition_path'])}. "
            f"{esc(implementation['layout'])}. {esc(implementation['graphics'])}.</p>"
            f"<p>{esc(counts)}. Counts are generated node instances, including repeated graphics. "
            '<a href="composition.json">Composition report</a></p>'
            f'<p><strong>Fixed artboard parity: {esc(feedback["acceptance"]["status"].upper())}.</strong> '
            + ('Reusable L0 components have a separate <a href="kit-gate.json">kit gate</a>. Responsive layout and application workflows remain unverified. '
               if kit.get('input_format')=='l0-kit' else 'Responsive layout, reusable L0–L3 composition and application workflows remain unverified. ') +
            '<a href="acceptance.json">Acceptance and next composition round</a> · '
            '<a href="composition-gate.json">Native widget audit</a> · '
            '<a href="repair-feedback.json">Repair findings</a></p>')
        composition_html += (f'<p>Native widget policy: '
            f'{"PASS" if policy["pass"] is True else "FAIL" if policy["required"] else "NOT ASSESSED"}.</p>')
        if implementation.get('semantic_widget_counts'):
            semantic_counts=' · '.join(f'{k}: {v:,}' for k,v in implementation['semantic_widget_counts'].items())
            composition_html += f'<p><strong>Semantic components:</strong> {esc(semantic_counts)}. Native types and actions are checked by the kit gate.</p>'
    run_path = out.parent/'pipeline-run.json'
    if run_path.exists():
        run = json.loads(run_path.read_text())
        composition_html += (f"<p><strong>Latest pipeline run: {esc(run['status'])}</strong> "
            f"{esc('; '.join(run.get('errors',[])))} · "
            '<a href="pipeline-run.json">Stage results</a>. Per-screen evidence below may precede a failed run.</p>')
    sections = []
    for name in kit['screens']:
        verdict = visual[name].get('review',verdicts.get(name, {}))
        followup_html=''
        if visual[name].get('review_method'):
            original=visual[name]['original_review']
            followup_html=(f'<details><summary>Evidence-informed follow-up; initial score '
                f'{esc(original.get("design_match","?"))}/10</summary><p>{esc(verdict.get("reason",""))}</p>'
                f'<p>Initial finding: {esc(original.get("worst",""))}</p>'
                f'<a href="{esc(name)}.visual-followup.json">Follow-up verdict and measured evidence</a></details>')
        target = kit['targets_dir']/f'{name}.png'
        shot = kit[f'{args.rail}_dir']/f'{name}.png'
        structure_path=out.parent/f'{name}.structure.json'
        try:
            structure=json.loads(structure_path.read_text()) if structure_path.exists() else {}
        except (OSError, ValueError):
            structure={}
        structural_status=('PASS' if structure.get('pass') else 'FAIL') if visual[name].get('capture_current',True) else 'STALE'
        structural=(f"Structural gate: {structural_status} · "
                    f"{structure.get('inspected_nodes',0)} inspected nodes · "
                    f"{structure.get('failed_checks',0)} differences")
        visual_status = 'PASS' if visual[name]['pass'] else 'FAIL'
        reference = 'Original Sketch export' if kit.get('reference_renderer') == 'Sketch' else 'Design target (spec reconstruction)'
        component = compositions.get(name, {})
        component_status = 'PASS' if component.get('pass') is True else 'FAIL' if component.get('pass') is False else 'NOT ASSESSED'
        component_html = (f'<p>Native widget policy: {component_status} · '
            f'<a href="{esc(name)}.composition.json">Source mappings and composition findings</a></p>') if implementation else ''
        if kit.get('input_format')=='l0-kit':
            card=kit['cards_dir']/f'{name}.card'
            component_html += (f'<p><a href="{esc(os.path.relpath(card,out.parent))}">L0 card</a> · '
                f'<a href="{esc(os.path.relpath(card.with_suffix(".data.json"),out.parent))}">Placement data</a> · '
                f'<a href="{esc(os.path.relpath(card.with_suffix(".l0map.json"),out.parent))}">Sketch-to-component map</a> · '
                f'<a href="{esc(name)}.kit.json">Reusable component audit</a></p>')
            if (out.parent/f'{name}.semantic-interactions.json').exists():
                component_html += f'<p><a href="{esc(name)}.semantic-interactions.json">Component actions and state restoration</a></p>'
        needs_repair=(next(r['needs_repair'] for r in feedback['screens'] if r['screen']==name)
                      if implementation else structural_status!='PASS' or not visual[name]['pass'])
        sections.append(f'''<section id="{esc(name)}" data-repair="{str(needs_repair).lower()}"><h2>{esc(name.replace('_',' '))}</h2>
          <p>{esc(structural)} · <a href="{esc(structure_path.name)}">Per-element findings</a>
          · <a href="{esc(name)}.snapshot.json">Native state</a></p>
          {component_html}<p>Visual gate: {visual_status} · {esc(verdict.get('design_match','?'))}/10 · {esc(verdict.get('verdict','unjudged'))}
          — {esc(verdict.get('worst',''))}</p>{followup_html}<div class="pair">
          <figure><figcaption>{esc(reference)}</figcaption>
          <img loading="lazy" decoding="async" alt="Sketch design for {esc(name.replace('_',' '))}" src="{esc(os.path.relpath(target,out.parent))}"></figure>
          <figure><figcaption>Native {esc(args.rail)} capture</figcaption>
          <img loading="lazy" decoding="async" alt="Native Makepad capture of {esc(name.replace('_',' '))}" src="{esc(os.path.relpath(shot,out.parent))}"></figure></div></section>''')
    out.write_text('''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>''' + esc(title) + '''</title><style>
body{font:16px system-ui;background:#eef1f4;color:#172131;margin:0;padding:32px;max-width:1000px;margin:auto}
h1{font-size:30px}h2{font-size:21px}section{margin:40px 0}.pair{display:flex;gap:24px;align-items:start}
figure{margin:0;flex:1;min-width:0;max-width:393px}figcaption{margin-bottom:12px;color:#526477;font-size:13px}
img{width:100%;border-radius:10px;box-shadow:0 2px 12px #17213118}p{line-height:1.5}
nav{position:sticky;top:0;background:#eef1f4f5;padding:12px 0;z-index:1;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
input[type=search]{font:inherit;padding:8px 12px;border:1px solid #bbc4ce;border-radius:8px;min-width:240px}
section[hidden]{display:none}
</style><h1>''' + esc(title) + '''</h1>
<p>Configured Sketch artboards rendered through the release splash-makepad host.
Structural, native composition and visual gates must pass for source-mapped designs. Missing or stale screenshot reviews fail the visual gate.
Successful capture and text parity alone do not imply design acceptance.</p>''' + composition_html + '''
<nav><input id="search" type="search" aria-label="Find a screen" placeholder="Find a screen">
<label><input id="repairs" type="checkbox"> Needs repair or review</label><span id="count"></span></nav>
''' + ''.join(sections) + '''<script>
const sections=[...document.querySelectorAll('section')];
const search=document.querySelector('#search'),repairs=document.querySelector('#repairs');
function filter(){let shown=0;const query=search.value.trim().toLowerCase();
for(const section of sections){section.hidden=!(section.querySelector('h2').textContent.toLowerCase().includes(query)&&(!repairs.checked||section.dataset.repair==='true'));if(!section.hidden)shown++;}
document.querySelector('#count').textContent=shown+' / '+sections.length+' screens';}
search.addEventListener('input',filter);repairs.addEventListener('change',filter);filter();
</script>''')
    print(out)


if __name__ == '__main__':
    main()
