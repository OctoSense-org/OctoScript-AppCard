#!/usr/bin/env python3
"""Image branch of the beauty loop. Image generation remains an explicit tool step."""
import argparse,json,sys
from catalogue import HERE
from compile import compile_page
from observe import observe,map_observations
from measure_surfaces import measure
from studio import launch,capture,click_controls,write
from gate import evaluate
from gallery import publish
from repair_text import repair
from semantics import propose,audit
from fit_reference_fonts import fit as fit_fonts
sys.path.insert(0,str(HERE.parent))
from core.repair import apply as apply_repair

def main():
    p=argparse.ArgumentParser();p.add_argument('--design',action='append');p.add_argument('--all',action='store_true')
    p.add_argument('--stages');p.add_argument('--launch',action='store_true')
    p.add_argument('--repair-plan',help='hash-bound layout/font/asset/data/semantic repair plan')
    a=p.parse_args()
    ids=[r['id'] for r in json.loads((HERE/'catalogue.json').read_text())] if a.all else a.design or ['weather-01']
    stages=(a.stages or 'classify,observe,measure,map,compile,capture,gate,gallery').split(',');valid={'classify','semantic','observe','measure','map','font','compile','capture','gate','repair','gallery'}
    if set(stages)-valid:p.error('Unknown stage: '+','.join(set(stages)-valid))
    build=None
    failed=False
    for id in ids:
        d=HERE/id
        d.mkdir(parents=True,exist_ok=True)
        run={'id':id,'status':'running','scope':'fixed_artboard_parity','accepted':False,'stages':[],'errors':[]}
        write(d/'pipeline-run.json',run)
        for stage in stages:
            if stage=='gallery':continue
            stage_pass=True
            run['current_stage']=stage;write(d/'pipeline-run.json',run)
            try:
                if stage=='classify':propose(d)
                elif stage=='semantic':
                    r=audit(d);stage_pass=r['pass'];failed |= not stage_pass
                    print(json.dumps({'id':id,'semantic_pass':r['pass'],'findings':len(r['errors'])}),flush=True)
                elif stage=='observe':observe(d)
                elif stage=='measure':
                    if not (d/'annotations.json').exists():measure(d)
                elif stage=='map':
                    if a.stages is not None or not (d/'mapped.json').exists():map_observations(d)
                elif stage=='compile':compile_page(d)
                elif stage=='font':fit_fonts(d)
                elif stage=='repair':
                    if a.repair_plan:apply_repair(d,a.repair_plan)
                    else:repair(d)
                elif stage=='capture':
                    compile_page(d)  # Preflight must succeed before any Studio build.
                    if build is None:build=launch() if a.launch else json.loads((HERE/'studio-run.json').read_text())['build_id']
                    click_controls(capture(id,build),build)
                elif stage=='gate':
                    latest=json.loads((d/'latest.json').read_text());r=evaluate(d,d/'rounds'/latest['round'])
                    print(json.dumps({'id':id,'native_pass':r['native_structure_pass'],'image_structure_pass':r['image_structure_pass'],
                                      'semantic_mapping_pass':r['semantic_mapping_pass'],'accepted':r['accepted'],
                                      'visual_status':r['visual_review'].get('status')}),flush=True)
                    stage_pass=r['accepted'];run['accepted']=r['accepted'];failed |= not stage_pass
            except KeyboardInterrupt:
                run['status']='interrupted';run['accepted']=False
                run['errors'].append(stage+': interrupted');stage_pass=False
                failed=True
                raise
            except (OSError,ValueError,RuntimeError,KeyError) as error:
                print(json.dumps({'id':id,'stage':stage,'blocked':str(error)}),flush=True)
                failed=True
                stage_pass=False;run['errors'].append(stage+': '+str(error));run['accepted']=False
                break
            finally:
                run['stages'].append({'stage':stage,'pass':stage_pass})
                write(d/'pipeline-run.json',run)
        run['status']='failed' if run['errors'] or any(not s['pass'] for s in run['stages']) else 'passed' if run['accepted'] else 'completed_without_acceptance'
        write(d/'pipeline-run.json',run)
    if 'gallery' in stages:publish()
    raise SystemExit(1 if failed else 0)

if __name__=='__main__':main()
