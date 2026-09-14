#!/usr/bin/env python3
"""Extract source-backed component styles for adaptive native app compositions."""
import hashlib
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NATIVE = ROOT / 'Octoscript-Makepad/components/l0/native'
THEMES = ('atro','atro_light','camo','camo_light','taskplan_light')


def export(theme):
    raw=(NATIVE/theme/'kit.json').read_bytes()
    kit=json.loads(raw)
    def resolve(v):
        if isinstance(v,dict):
            if '$token' in v:return kit['tokens'][v['$token']]['value']
            return {k:resolve(x) for k,x in v.items()}
        if isinstance(v,list):return [resolve(x) for x in v]
        return v
    def style(pattern):
        return resolve(kit['components'][pattern[0]]['style'])
    def at(pattern,path):
        for index in path:pattern=pattern[1][index]
        return pattern
    def styles(pattern):
        yield style(pattern)
        for child in pattern[1]:yield from styles(child)
    result={}
    for role,entry in kit['semantic_roles'].items():
        if role.endswith('BottomNavigation'):continue
        key=entry['composition']
        if role=='AtroButton':
            # Use a text button rather than the default icon-only semantic role.
            candidates=[(name,c) for name,c in kit['compounds'].items() if c.get('semantic')
                        and name.startswith('AtroButton') and 'label: text' in c['definition'].splitlines()[0]]
            key=max(candidates,key=lambda pair:pair[1]['uses'])[0]
        if role=='CamoButton':
            # The most frequent source button is a dim, borderless action.
            # App add/search actions use the source's filled primary button.
            candidates=[]
            for name,c in kit['compounds'].items():
                if not c.get('semantic') or not name.startswith('CamoButton') or 'label: text' not in c['definition'].splitlines()[0]:continue
                ss=list(styles(c['pattern']))
                if any(s.get('bg',0)>>24==255 and max((s['bg']>>shift)&255 for shift in (0,8,16))-min((s['bg']>>shift)&255 for shift in (0,8,16))>80 for s in ss):
                    candidates.append((name,c))
            if candidates:key=max(candidates,key=lambda pair:pair[1]['uses'])[0]
        compound=kit['compounds'][key]
        pattern=compound['pattern'];root=style(pattern);contract=json.loads(root['kit'])
        parts={name:dict(component=at(pattern,path)[0],style=style(at(pattern,path)))
               for name,path in contract['bindings'].items()}
        surfaces=[]
        def collect(p):
            s=style(p)
            if s.get('bg',0)>>24 and s.get('variant') in ('surface','ellipse'):
                surfaces.append(dict(component=p[0],style=s))
            for child in p[1]:collect(child)
        collect(pattern)
        simple={'KitButton':'button','KitFormField':'field','KitTabBar':'tabs',
                'CamoTrackRow':'row','TaskplanProjectCard':'card'}[contract['widget']]
        selection={k:v for k,v in contract.items() if k in ('active_color','inactive_color','active_surface','inactive_surface')}
        if simple=='tabs' and 'active_surface' not in selection:
            filled=next((i for i in contract.get('items',[]) if i.get('surface_color',0)>>24==255),None)
            unfilled=next((i for i in contract.get('items',[]) if i.get('surface_color')==0),None)
            if filled and unfilled:
                selection.update(active_color=filled['ink'],active_surface=filled['surface_color'],
                                 inactive_color=unfilled['ink'],inactive_surface=unfilled['surface_color'])
        result[simple]=dict(widget=contract['widget'],source_role=role,source_composition=key,
                            source_component=pattern[0],source_screens=compound['screens'],
                            source_kit_sha256=hashlib.sha256(raw).hexdigest(),parts=parts,surfaces=surfaces,
                            selection=selection)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if bundled app recipes are stale')
    args=parser.parse_args()
    data={theme:export(theme) for theme in THEMES}
    out=NATIVE/'app-recipes.json'
    encoded=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
    if args.check:
        if not out.exists() or out.read_text()!=encoded:
            raise SystemExit('App recipes are stale; run lab/sketch-to-appcard/export_app_recipes.py')
    else:
        out.write_text(encoded)
    print(out, out.stat().st_size)
    for theme,recipes in data.items():
        print(theme,{name:(r['source_composition'],list(r['parts'])) for name,r in recipes.items()})
