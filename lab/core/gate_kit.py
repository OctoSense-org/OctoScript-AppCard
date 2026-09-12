#!/usr/bin/env python3
"""Validate reusable L0 definitions and their source-linked native consumers."""
import argparse
import hashlib
import json
import subprocess

from core import kitconf
from core.promote_l0 import PACKS, definition, parse_design, walk


def evaluate(kit):
    out=kit['splash_makepad_dir'];out.mkdir(parents=True,exist_ok=True)
    if kit.get('input_format')!='l0-kit':
        return {'required':False,'pass':None,'screens':[]}
    audit=out/'kit-tree-audit.json'
    audit.unlink(missing_ok=True)
    command=['cargo','run','--release','-q','-p','splash-makepad','--example','kit_audit','--',
             str(kit['cards_dir']),str(kitconf.HERE/kit['source_designs_dir']),str(PACKS.parent),str(audit)]
    result=subprocess.run(command,cwd=kitconf.HERE.parents[1]/'splash-makepad',capture_output=True,text=True)
    (out/'kit-tree-audit.log').write_text(result.stdout+result.stderr)
    audits={r['screen']:r for r in json.loads(audit.read_text()).get('screens',[])} if audit.exists() else {}
    rows=[]
    for name in kit['screens']:
        errors=[]
        try:
            card=kit['cards_dir']/f'{name}.card';data=card.with_suffix('.data.json');mapping=card.with_suffix('.l0map.json')
            info=json.loads(mapping.read_text());pack_path=PACKS/info['theme']/'kit.json'
            pack=json.loads(pack_path.read_text());source=card.read_text()
            if not audits.get(name,{}).get('pass'):errors.append(audits.get(name,{}).get('error','missing native tree audit'))
            for component in info['components']:
                if definition(component,pack['components'][component]) not in source:
                    errors.append('component contract differs from shared library: '+component)
            for component in info['compounds']:
                if pack['compounds'][component]['definition'] not in source:
                    errors.append('compound differs from shared library: '+component)
            old=kitconf.HERE/kit['source_designs_dir']/f'{name}.splash'
            source_nodes={n['id']:n for n in walk(parse_design(old.read_text()))}
            added=info.get('added_controls',{})
            if set(source_nodes)|set(added)!=set(info['elements']):errors.append('incomplete L0/Sketch mapping')
            for ident,control in added.items():
                if control['owner'] not in source_nodes or control['kind'] not in ('radio','button') or ident!=control['owner']+'_kit_'+control['kind']:
                    errors.append('unregistered added control: '+ident)
            if any(not row.get('source_id') for row in info['elements'].values()):errors.append('kit instance missing Sketch owner')
            portable=out/f'{name}.portable.json'
            runtime_nodes=json.loads(portable.read_text())['elements']
            runtime={n.get('original_id') for n in runtime_nodes}
            if runtime!=set(source_nodes)|set(added):errors.append('native inspection does not cover all kit instances')
            snapshot=out/f'{name}.snapshot.json'
            widgets={n['id']:n for n in json.loads(snapshot.read_text())['widgets']}
            runtime_by_source={n.get('original_id'):n for n in runtime_nodes}
            differences=[]
            semantic=out/f'{name}.semantic-interactions.json'
            if info.get('semantic_widgets'):
                if not semantic.exists() or json.loads(semantic.read_text()).get('pass') is not True:
                    errors.append('missing or failed semantic widget interaction evidence')
            for ident,config in info.get('semantic_widgets',{}).items():
                generated=runtime_by_source.get(ident,{})
                actual=widgets.get(generated.get('id'),{})
                ok=actual.get('widget_type')==config['widget'] and generated.get('kit')==json.dumps(config,sort_keys=True,separators=(',',':'))
                differences.append({'source_widget':ident,'widget_id':generated.get('id'),'expected_type':config['widget'],
                    'actual_type':actual.get('widget_type'),'pass':ok})
                if not ok:errors.append('semantic widget is missing or generic: '+ident)
            reused=[n for n in info['components'] if len(pack['components'][n]['screens'])>1]
            if not reused:errors.append('no component shared with another screen')
            paths=[card,data,mapping,pack_path,old,portable,snapshot]
            if info.get('semantic_widgets') and semantic.exists():paths.append(semantic)
            row={'screen':name,'pass':not errors,'errors':errors,'instances':len(source_nodes),
                 'shared_components':len(reused),'compound_definitions':len(info['compounds']),
                 'semantic_widgets':differences,'added_native_controls':len(added),
                 'evidence_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
        except (OSError,ValueError,KeyError,TypeError) as error:
            row={'screen':name,'pass':False,'errors':[str(error)]}
        (out/f'{name}.kit.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
    report={'required':True,'pass':bool(rows) and result.returncode==0 and all(r['pass'] for r in rows),
            'scope':'registered_tokens_and_reusable_l0_components','screens':rows,
            'layout_scope':'source-artboard placements; responsive behavior requires separate validation'}
    (out/'kit-gate.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--kit',required=True)
    report=evaluate(kitconf.load(parser.parse_args().kit))
    print(f"L0 kit gate: {sum(r['pass'] for r in report['screens'])}/{len(report['screens'])}")
    if report['pass'] is False:raise SystemExit(1)
