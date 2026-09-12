#!/usr/bin/env python3
"""Sequential native Studio review. Reuses the user's persistent bridge."""
import argparse,json,shutil,sys,time,urllib.request
from pathlib import Path

def studio(request,response=None,timeout=15):
 raw=json.dumps({'request':request,'response':response,'timeout':timeout}).encode()
 req=urllib.request.Request('http://127.0.0.1:8170',raw,{'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=timeout+3) as r:j=json.load(r)
 if 'error' in j:raise RuntimeError(j)
 return j

def visible(w):return w.get('visible') and w.get('width',0)>0 and w.get('height',0)>0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--ids',default='');ap.add_argument('--template',action='store_true');ap.add_argument('--wait',action='store_true');ap.add_argument('--build',action='store_true');args=ap.parse_args()
 ids=args.ids.split(',') if args.ids else [f'{i:02}' for i in range(1,21)]
 config_path=Path('/tmp/octos-macos-composition-request.json');config=json.loads(config_path.read_text());config['skip_build']=not args.build
 builds=studio({'ListBuilds':[]},'Builds')['builds'];old=next((b['build_id'] for b in builds if b['package']=='octos-macos-composition'),None)
 for case_id in ids:
  folder=args.out/case_id;p=folder/'result.json';deadline=time.monotonic()+360
  while not p.exists():
   if not args.wait or time.monotonic()>deadline:break
   time.sleep(1)
  if not p.exists():print(json.dumps({'skip':case_id,'reason':'No completed generation'}),flush=True);continue
  result=json.loads(p.read_text());data=json.loads((folder/'dataset.json').read_text())['data'];prefix='template-' if args.template else ''
  config.update(l0_card=str((folder/('template.card' if args.template else 'app.card')).resolve()),l0_data=str((folder/'data.json').resolve()),dataset_file=str((folder/'dataset.json').resolve()))
  config_path.write_text(json.dumps(config,indent=2))
  if old:studio({'ClearBuild':{'build_id':old}})
  start=time.perf_counter();run=studio({'RunItem':{'mount':'octos','name':'octos-macos-composition'}},'BuildStarted');build=run['build_id'];old=build
  j=None;error=None
  for _ in range(60):
   time.sleep(.2)
   try:j=studio({'WidgetSnapshot':{'build_id':build}},'WidgetSnapshot',timeout=2)
   except Exception:continue
   labels=[w.get('text','') for w in j['widgets'] if visible(w) and w['widget_type']=='Label']
   if data['title'] in labels and data['pick1_body'] in labels:break
  else:error='Expected title and first recommendation did not render'
  mount_s=time.perf_counter()-start
  ui={'build_id':build,'launch_to_visible_s':mount_s,'error':error,'evidence_tab':False,'plan_tab':False}
  if j:
   (folder/(prefix+'widgets.json')).write_text(json.dumps(j,ensure_ascii=False))
   try:
    shot=studio({'Screenshot':{'build_id':build}},'Screenshot');shutil.copyfile(shot['path'],folder/(prefix+'screen.png'))
    def click_text(text):
     current=studio({'WidgetSnapshot':{'build_id':build}},'WidgetSnapshot');o=next(w for w in current['widgets'] if w['widget_type']=='Window');w=next(w for w in current['widgets'] if visible(w) and w.get('text')==text)
     studio({'Click':{'build_id':build,'x':round(w['x']+w['width']/2-o['x']),'y':round(w['y']+w['height']/2-o['y'])}})
    click_text('Evidence')
    for _ in range(20):
     time.sleep(.15);e=studio({'WidgetSnapshot':{'build_id':build}},'WidgetSnapshot')
     if any(visible(w) and w.get('text')==data['evidence_body'] for w in e['widgets']):ui['evidence_tab']=True;break
    (folder/(prefix+'evidence-widgets.json')).write_text(json.dumps(e,ensure_ascii=False))
    shot=studio({'Screenshot':{'build_id':build}},'Screenshot');shutil.copyfile(shot['path'],folder/(prefix+'evidence.png'))
    click_text('Plan')
    for _ in range(20):
     time.sleep(.15);e=studio({'WidgetSnapshot':{'build_id':build}},'WidgetSnapshot')
     if any(visible(w) and w.get('text')==data['pick1_body'] for w in e['widgets']):ui['plan_tab']=True;break
   except Exception as e:ui['interaction_error']=str(e)
  result['template_ui' if args.template else 'ui']=ui;p.write_text(json.dumps(result,ensure_ascii=False,indent=2))
  print(json.dumps({'reviewed':case_id,**ui}),flush=True)
if __name__=='__main__':main()
