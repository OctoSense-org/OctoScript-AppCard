#!/usr/bin/env python3
"""Twenty live intents: real Splash workflow + generated and reusable L0 views."""
import argparse,asyncio,datetime,json,re,time,traceback
from pathlib import Path
import adapters,cards,model
ROOT=Path(__file__).resolve().parents[1]

def jobs_for(plan):
 jobs=[]
 def add(kind,params):jobs.append({'id':f'{kind}{len(jobs)+1}','kind':kind,'params':params})
 for city in plan['cities']:
  add('weather',{'city':city,'horizon':plan['horizon']})
  if plan['needs_air']:add('air',{'city':city})
  if plan['needs_places']:add('places',{'city':city})
 for ticker in plan['tickers']:add('quote',{'ticker':ticker})
 if plan['topic']:add('news',{'topic':plan['topic']})
 if not 1<=len(jobs)<=8:raise ValueError('Invalid source budget')
 return jobs

async def workflow(case,plan):
 request={'intent':case['intent'],'plan':plan,'jobs':jobs_for(plan),'output_schema':model.ANSWER_SCHEMA}
 process=await asyncio.create_subprocess_exec(str(ROOT/'target/release/composition-vm'),stdin=asyncio.subprocess.PIPE,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
 process.stdin.write((json.dumps(request,ensure_ascii=False)+'\n').encode());await process.stdin.drain()
 adapter=adapters.Adapters();tasks=set();trace=[];timings=[];limit=asyncio.Semaphore(4);write_lock=asyncio.Lock();start=time.perf_counter()
 async def dispatch(message):
  entry={'tool':message['tool'],'input':message['input'],'start_s':time.perf_counter()-start,'vm_start_ms':message['ms']};trace.append(entry)
  try:
   if message['tool']=='composition.fetch':
    async with limit:result=await asyncio.to_thread(adapter.run,message['input'])
   elif message['tool']=='composition.synthesize':
    result,t=await asyncio.to_thread(model.synthesize,message['input']);timings.append(t)
   else:raise ValueError('Unknown capability')
   reply={'reply':message['invoke'],'output':result};entry['status']=result.get('status','ready')
  except Exception as e:reply={'reply':message['invoke'],'error':str(e)};entry['error']=str(e)
  entry['end_s']=time.perf_counter()-start
  async with write_lock:
   process.stdin.write((json.dumps(reply,ensure_ascii=False)+'\n').encode());await process.stdin.drain()
 try:
  while True:
   line=await asyncio.wait_for(process.stdout.readline(),timeout=100)
   if not line:
    raise RuntimeError((await process.stderr.read()).decode() or 'Workflow exited without result')
   message=json.loads(line)
   if 'invoke'in message:
    task=asyncio.create_task(dispatch(message));tasks.add(task);task.add_done_callback(tasks.discard)
   elif 'done'in message:
    await asyncio.gather(*tasks);process.stdin.close();await process.wait()
    return {'result':message['done'],'elapsed_s':time.perf_counter()-start,'vm_elapsed_ms':message['elapsed_ms'],'trace':trace,'model_calls':timings,'request':request}
 finally:
  if process.returncode is None:process.terminate();await process.wait()
  for task in tasks:task.cancel()

def source_label(e):
 label={'weather':'Weather · Open-Meteo','air':'Air quality · Open-Meteo','places':'Places · OpenStreetMap','quote':'Prices · Yahoo Finance','news':'News · Bing'}[e['kind']]
 d=e.get('data',{});place=d.get('place',d.get('ticker',''))
 if isinstance(place,dict):place=place.get('name','')
 return label+(' · '+place if place else '')

def user_prose(text,ids):
 # Citation metadata is displayed separately. Strip only pure metadata parentheses.
 tokens=set(ids)|{'host_comparisons'}
 def without_metadata(match):
  words={w.strip() for w in match.group(1).split(',')}
  return '' if words and words<=tokens else match.group(0)
 text=re.sub(r'\(([^()]*)\)',without_metadata,text)
 return text.replace('do not describe as mild','plan shade and breaks').strip()

def dataset(case,plan,work):
 evidence=work['result']['evidence'];answer=work['result']['answer'];byid={e['id']:e for e in evidence};ready=[e for e in evidence if e['status']=='ready']
 data={key:'' for key in cards.FIELDS}
 data.update(title=plan['title'],subtitle={'today':'Today','next3days':'Next three days','this_week':'This week','weekend':'This weekend','next7days':'Next seven days'}[plan['horizon']] + (' · Some sources unavailable' if len(ready)!=len(evidence) else ''),summary=answer['summary'],status='partial' if len(ready)!=len(evidence) else 'ready',as_of='Retrieved '+datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),evidence_title='Sources and observations')
 data['coverage']=answer['limitations']
 data['as_of']='Retrieved '+max(datetime.datetime.fromisoformat(e['retrieved_at']) for e in evidence).strftime('%Y-%m-%d %H:%M UTC')
 if len(data['title'])>=55 and plan['language']=='en':data['title']=data['title'].rsplit(' ',1)[0]
 lines=[];metrics=[]
 for e in evidence:
  k=e['kind'];d=e['data'];tag=source_label(e)
  if e['status']!='ready':lines.append(f'[{tag}] Temporarily unavailable');continue
  if k=='weather':
   rows=d['days'];lines.append(f'[{tag}] {d["place"]["name"]} · {d["timezone"]}')
   for day in rows:lines.append(f'{day["date"]}: {day["low_c"]}–{day["high_c"]} °C; rain {day["rain_probability_pct"]}%; wind {day["wind_kmh"]} km/h; sunset {day["sunset"][11:]}')
   if rows:metrics.append((d['place']['name'],f'{min(r["low_c"] for r in rows)}–{max(r["high_c"] for r in rows)} °C\nRain {min(r["rain_probability_pct"] for r in rows)}–{max(r["rain_probability_pct"] for r in rows)}%'))
  elif k=='air':
   lines.append(f'[{tag}] {d["place"]} · current modeled US AQI {d["current"].get("us_aqi")} at {d["current"]["time"]}')
   lines.extend(f'{day}: forecast max US AQI {n}' for day,n in d['forecast_daily_max_us_aqi'].items())
  elif k=='places':
   lines.append(f'[{tag}] {d["place"]}: '+', '.join(p['name'] for p in d['items']));lines.append(d['coverage'])
  elif k=='quote':
   metrics.append((d['ticker'],f'{d["currency"]} {d["price"]:.2f}\n{d["change_pct"]:+.2f}% / 1 session'))
   lines.append(f'[{tag}] {d["ticker"]} · {d["company"]}\n{d["currency"]} {d["price"]} at {d["quote_at"]}\nPrevious daily close {d["previous_close"]}; change {d["change_pct"]:+.3f}%\n'+d['baseline'])
  elif k=='news':
   lines.append(f'[{tag}] {d["topic"]} · indexed excerpts only')
   for item in d['items']:lines.append(item['title']+' · '+item['publisher']+' · '+item['published_at'])
  lines.append('Source: '+e['url']+'\n')
 if len(metrics)<2:
  news=next((e for e in ready if e['kind']=='news'),None);air=next((e for e in ready if e['kind']=='air'),None)
  if air:metrics.append(('Modeled US AQI',str(air['data']['current'].get('us_aqi','Unavailable'))))
  elif news:metrics.append(('News coverage',str(len(news['data']['items']))+' indexed articles\nPast 72 hours'))
  else:metrics.append(('Coverage',str(len(ready))+' live sources'))
 for i,(label,value) in enumerate(metrics[:2],1):data[f'metric{i}_label']=label;data[f'metric{i}_value']=value
 data['evidence_body']='\n'.join(lines)
 for i,pick in enumerate(answer['picks'],1):
  data[f'pick{i}_title']=user_prose(pick['title'],byid);data[f'pick{i}_body']=user_prose(pick['body'],byid)
  labels=[]
  for source_id in dict.fromkeys(pick['source_ids']):
   e=byid[source_id];label={'weather':'Weather','air':'Air quality','places':'Places','quote':'Prices','news':'News'}[e['kind']]
   place=e['data'].get('place',e['data'].get('ticker',''))
   if isinstance(place,dict):place=place.get('name','')
   if place and (len(plan['cities'])>1 or e['kind']=='quote'):label+=' · '+place
   if label not in labels:labels.append(label)
  data[f'pick{i}_source']='Sources: '+' / '.join(labels)
  sources=[byid[s] for s in pick['source_ids'] if byid[s]['status']=='ready']
  link='';text=(pick['title']+' '+pick['body']).lower()
  for source in sources:
   if source['kind']=='places':
    match=next((p for p in source['data']['items'] if p['name'].lower() in text),None)
    if match:link=match['url'];break
  if not link:
   news=next((s for s in sources if s['kind']=='news'),None);quote=next((s for s in sources if s['kind']=='quote'),None)
   if news:link=news['data']['items'][0]['url']
   elif quote:link='https://finance.yahoo.com/quote/'+quote['data']['ticker']+'/'
   elif sources:link=sources[0]['url']
  data[f'url{i}']=link
 data['summary']=user_prose(data['summary'],byid)
 data['coverage']=user_prose(data['coverage'],byid)
 return {'id':case['id'],'data':data}

async def one(case,out,templates_only=False):
 folder=out/case['id'];folder.mkdir(parents=True,exist_ok=True);started=time.perf_counter()
 plan,t=await asyncio.to_thread(model.plan,case['intent'])
 if case.get('family') and plan['family']!=case['family']:raise ValueError('Intent classified into wrong family: '+repr(plan))
 template_started=time.perf_counter();templated=cards.template(case['id'],plan);template_s=time.perf_counter()-template_started
 (folder/'template.card').write_text(templated)
 good,why=cards.check(folder/'template.card')
 if not good:raise ValueError('Template invalid: '+why)
 generation=None if templates_only else asyncio.create_task(asyncio.to_thread(cards.generate,case,plan,folder))
 work=await workflow(case,plan)
 source,attempts=(templated,[]) if templates_only else await generation
 data=dataset(case,plan,work);(folder/'dataset.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 (folder/'data.json').write_text(json.dumps({'facts':data['data']},ensure_ascii=False,indent=2))
 # Preserve failures; a fallback is explicit in both metrics and the gallery.
 (folder/'app.card').write_text(source or templated)
 result={'mode':'template' if templates_only else 'generated','case':case,'plan':plan,'plan_call':t,'ui_generation':attempts,'ui_fallback':source is None,'template_instantiation_s':template_s,'workflow':work,'generation_and_research_s':time.perf_counter()-started,'dataset_status':data['data']['status'],'ui':None}
 (folder/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
 return result
async def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);parser.add_argument('--ids',default='');parser.add_argument('--intent');parser.add_argument('--resume',action='store_true');parser.add_argument('--templates-only',action='store_true');args=parser.parse_args()
 args.out.mkdir(parents=True,exist_ok=True);cases=json.loads((Path(__file__).parent/'cases.json').read_text());selected=set(args.ids.split(',')) if args.ids else None
 if args.intent:cases=[{'id':'custom','intent':args.intent}]
 for case in cases:
  if selected and case['id'] not in selected:continue
  if args.resume and (args.out/case['id']/'result.json').exists():continue
  print(json.dumps({'start':case['id'],'intent':case['intent']}),flush=True)
  try:
   r=await one(case,args.out,args.templates_only);print(json.dumps({'done':case['id'],'seconds':round(r['generation_and_research_s'],2),'status':r['dataset_status'],'ui_fallback':r['ui_fallback'],'model_ui_s':round(sum(a['timing']['elapsed_s'] for a in r['ui_generation']),2)}),flush=True)
  except Exception as e:
   (args.out/case['id']).mkdir(exist_ok=True);(args.out/case['id']/'failure.json').write_text(json.dumps({'error':str(e),'traceback':traceback.format_exc()}));print(json.dumps({'failed':case['id'],'error':str(e)}),flush=True)
if __name__=='__main__':asyncio.run(main())
