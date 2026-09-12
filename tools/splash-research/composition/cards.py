import json,subprocess,time
from pathlib import Path
import model
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['title','subtitle','summary','coverage','status','as_of','metric1_label','metric1_value','metric2_label','metric2_value']+[f'{p}{i}{s}' for i in range(1,4) for p,s in [('pick','_title'),('pick','_body'),('pick','_source'),('url','')]]+['evidence_title','evidence_body']
def q(s):return json.dumps(s,ensure_ascii=False)
def header(case_id,theme):
 return f'''# ledger composition-{case_id}@1.0.0
theme {theme}
source facts sys.dataset(id: {q(case_id)}, fields: [{', '.join(FIELDS)}])
source page sys.link(fields: [url])
state tab {{ shape: enum[summary, evidence], initial: .summary }}
event summary {{ tab: set(.summary) }}
event evidence {{ tab: set(.evidence) }}
event open_source {{ page: set($value) }}
copy summary {{ class: vocabulary, en: "Plan" }}
copy evidence {{ class: vocabulary, en: "Evidence" }}
copy source {{ class: vocabulary, en: "Open source ↗" }}
'''
def template(case_id,plan):
 family=plan['family'];theme={'travel':'atro_light','outdoor':'camo_light','compare':'taskplan_light','briefing':'atro_light','market':'camo_light'}[family]
 s=header(case_id,theme)
 metric='''Row(gap: 12) {
 Col(width: .fill) { Card { Col(gap: 6) { TextCaption(text: facts.metric1_label) TextBody(text: facts.metric1_value, width: .fill) } } }
 Col(width: .fill) { Card { Col(gap: 6) { TextCaption(text: facts.metric2_label) TextBody(text: facts.metric2_value, width: .fill) } } }
}'''
 # Families vary hierarchy and grouping while sharing the data contract.
 s+='view root Surface(pad: .page) { Col(gap: 12) {\nTextTitle(text: facts.title, width: .fill)\nTextCaption(text: facts.subtitle, width: .fill)\n'
 s+='Row(gap: 10) { Chip(text: copy.summary, on_tap: summary) Chip(text: copy.evidence, on_tap: evidence) }\n'
 s+='when tab == .summary { Col(gap: 12) {\n'
 if family in ['market','compare','outdoor']:s+=metric+'\n'
 s+='Panel { Col(gap: 8) { TextBody(text: facts.summary, width: .fill) } }\n'
 if family in ['travel','briefing']:s+=metric+'\n'
 for i in range(1,4):
  wrapper='Panel' if family=='briefing' else 'Card'
  s+=f'''{wrapper} {{ Col(gap: 8) {{
 TextBody(text: facts.pick{i}_title, width: .fill)
 TextBody(text: facts.pick{i}_body, width: .fill)
 TextCaption(text: facts.pick{i}_source, width: .fill)
 when facts.url{i} != "" {{ Chip(text: copy.source, on_tap: open_source, value: facts.url{i}) }}
}} }}\n'''
 s+='TextCaption(text: facts.coverage, width: .fill)\n} }\n'
 s+='when tab == .evidence { Col(gap: 12) { TextTitle(text: facts.evidence_title, width: .fill) TextBody(text: facts.evidence_body, width: .fill) TextCaption(text: facts.as_of, width: .fill) TextBody(text: facts.coverage, width: .fill) } }\n} }\n'
 return s

def check(path):
 p=subprocess.run([str(ROOT/'target/release/l0-check'),str(path)],text=True,capture_output=True,timeout=10)
 return p.returncode==0,p.stdout+p.stderr

def generate(case,plan,folder):
 fixed=header(case['id'],{'travel':'atro_light','outdoor':'camo_light','compare':'taskplan_light','briefing':'atro_light','market':'camo_light'}[plan['family']])
 prompt='''Generate an L0 native app layout for the supplied intent. Output ONLY a view root declaration, no fences. The host prepends exactly the declarations supplied below; do not repeat them. All content is in facts fields; never put actual facts in literals. Choose hierarchy and grouping to fit this intent. Use only Surface(pad: .page), Col(gap: 12), Row(gap: 10), Card, Panel, Rule(), TextTitle(text: facts.title, width: .fill), TextBody, TextCaption, and Chip. Every text uses text: facts.FIELD, width: .fill. TextCaption and TextBody wrap; TextTitle can truncate, so only use it for the short app title. Keep long prose in Col, never squeeze into a narrow Row. Card and Panel take NO arguments. For two metrics use a Row containing two Col(width: .fill) wrappers, each containing a Card. All text fields are strings, so use no TextValue or charts. Use theme roles, no colors/sizes/fonts. Every facts reference must be in the declared fields. No loops or new states, events or vocabulary. Render title, subtitle; Plan and Evidence chips; a when tab == .summary branch with summary, two labeled metrics, three pick title/body/source groups with Open source chips, and coverage. A when tab == .evidence branch must display evidence_title, evidence_body, as_of and coverage. Exact chip syntax: Chip(text: copy.summary, on_tap: summary), Chip(text: copy.evidence, on_tap: evidence), Chip(text: copy.source, on_tap: open_source, value: facts.url1). There is NO copy argument on Chip. Use all three picks, all source URLs, and both tabs. Valid syntax: view root Surface(pad: .page) { Col(gap: 12) { TextTitle(text: facts.title, width: .fill) } }. No JavaScript, semicolons or Makepad raw View syntax. Favor readable mobile vertical layouts.'''
 attempts=[]
 for attempt in range(2):
  user={'intent':case['intent'],'plan':plan,'declarations':fixed,'valid_reference_view':'view root'+template(case['id'],plan).split('view root',1)[1]}
  if attempts:
   user['previous_error']=attempts[-1]['diagnostics'][:2000]
   user['previous_view']=body
  body,t=model.call(prompt,user,max_tokens=2300)
  if body.strip().startswith('```'):body=body.strip().split('\n',1)[1].rsplit('```',1)[0]
  source=fixed+'\n'+body.strip()+'\n';path=folder/f'generated-{attempt+1}.card';path.write_text(source)
  valid,why=check(path)
  required=['facts.summary','facts.metric1_value','facts.metric2_value','facts.evidence_body']+[f'facts.pick{i}_body' for i in range(1,4)]+[f'facts.url{i}' for i in range(1,4)]
  missing=[f for f in required if f not in body]
  if missing:valid=False;why+=' Missing required bindings '+repr(missing)
  attempts.append({'timing':t,'valid':valid,'diagnostics':why,'file':path.name})
  if valid:return source,attempts
 return None,attempts
