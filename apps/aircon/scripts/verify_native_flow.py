#!/usr/bin/env python3
"""Exercise actual service controls through Makepad Studio instrumentation.

Run only when no per-frame capture owns the host. Every click uses inspected
native bounds and must produce a service transition from the host action log.
--self-check exercises the bindings offline without Studio or a live request.
"""
from pathlib import Path
import argparse,copy,hashlib,json,math,sys,tempfile,time,uuid

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / "lab"))
from core.native_paths import repository


def source_path(relative):
    """Resolve paths recorded before apps were grouped in apps/."""
    if relative.startswith("pipeline/"):
        name, _, tail = relative[9:].partition("/")
        return repository(name) / tail if name in ("makepad", "splash", "splash-makepad") else ROOT.parents[1] / relative[9:]
    return ROOT / relative

sys.path.insert(0,str(ROOT/'runtime'));sys.path.insert(0,str(ROOT/'service'))
sys.path.insert(0,str(ROOT.parents[1] / 'lab/image-to-appcard'))
from service_session import Session,read,native_event
from controller import demo_states,reduce,view_model
from render_runtime import render_runtime
from studio import request,save_viewport_screenshot

def save(path,obj):Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def require(condition,message):
 if not condition:raise RuntimeError(message)

def enabled_flag(value):
 """Disabled controls can be false or numeric zero in WidgetSnapshot."""
 require(type(value) in (bool,int,float) and value in (0,1),'Missing/invalid native enabled state: '+repr(value))
 return bool(value)

def native_rect(node,layout):
 if all(key in node for key in ('x','y','width','height')):
  bounds=[node[key] for key in ('x','y','width','height')]
 else:
  bounds=node.get('rect') or node.get('bounds')
  if bounds is None:bounds=next(item['bounds'] for item in layout['elements'] if item['id']==node['id'])
  if isinstance(bounds,dict):bounds=[bounds[key] for key in (('x','y','w','h') if 'w' in bounds else ('x','y','width','height'))]
 require(len(bounds)==4 and all(type(n) in (int,float) and math.isfinite(n) for n in bounds),'Invalid native rectangle')
 require(bounds[2]>0 and bounds[3]>0,'Native control has no area')
 return bounds

def provenance(build):
 path=ROOT/'runtime/infrastructure.json';infrastructure=read(path)
 require(infrastructure['binaries']['beauty-host']['build_id']==build,'Build id differs from runtime/infrastructure.json')
 files=['scripts/verify_native_flow.py','service/controller.py','service/fixture.json','service/contract.json',
        'runtime/service_session.py','runtime/render_runtime.py','pipeline/lab/image-to-appcard/studio.py',
        'pipeline/splash-makepad/apps/kit-host/src/beauty.rs','pipeline/splash-makepad/apps/kit-host/src/beauty_semantics.rs',
        'pipeline/splash-makepad/apps/kit-host/src/l0.rs']
 for frame in range(1,13):
  folder=ROOT/'cards'/f'aircon-{frame:02d}'
  files.extend(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and 'rounds' not in p.relative_to(folder).parts and p.suffix in ('.json','.card','.l0'))
 binaries={}
 for name,entry in infrastructure['binaries'].items():
  actual=sha(source_path(entry['path']));require(actual==entry['sha256'],'Binary differs from infrastructure: '+name)
  binaries[name]={'path':entry['path'],'sha256':actual}
 return {'build_id':build,'infrastructure_path':str(path.relative_to(ROOT)),'infrastructure_sha256':sha(path),
         'source_sha256':{p:sha(source_path(p)) for p in sorted(set(files))},'native_binaries':binaries}

def run(build):
 out=ROOT/'evidence/native-flow'/(time.strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:8]);out.mkdir(parents=True)
 states,_=demo_states();session=Session(out/'session',build_id=build)
 checks=[];inputs=[];proof=None
 def owned():require(session.owns_request(),'Another capture/session owns the native request; verification stopped')
 def reply(kind,body=None):
  result=request(kind,{'build_id':build,**(body or {})},kind)
  require(result.get('build_id')==build,'Stale Studio build in '+kind)
  return result
 def settled():
  owned()
  nonce=session.meta['request']['nonce'];deadline=time.monotonic()+30
  request('RunViewResize',{'build_id':build,'window_id':0,'width':406,'height':776,'dpi':2.0})
  while time.monotonic()<deadline:
   owned()
   try:
    layout=read(session.meta['request']['layout']);native=read(session.meta['request']['result'])
    if layout.get('nonce')==nonce and native.get('request',{}).get('nonce')==nonce:
     require(native['request'].get('build_id')==build,'Native manifest has stale build')
     require(native.get('ok') is True,'Native host rejected the live L0 request')
     return layout
   except (OSError,ValueError):pass
   time.sleep(.1)
  raise RuntimeError('Native layout did not settle for '+nonce)
 def snapshot():return reply('WidgetSnapshot')
 def actions(mounted):
  try:result=read(mounted['actions'])
  except FileNotFoundError:return []
  require(isinstance(result,list),'Native actions must be a list')
  return result
 def capture(name):
  layout=settled();folder=out/name;folder.mkdir()
  mounted=copy.deepcopy(session.meta['request'])
  snap=snapshot();save(folder/'snapshot.json',snap)
  shot=reply('Screenshot',{'kind_id':0})
  crop=save_viewport_screenshot(shot,folder/'native.png',width=406,height=776,dpi=2.0)
  require(crop['crop_xywh']==[0,0,812,1552] and crop['resampled'] is False,'Screenshot was not an exact native viewport crop')
  save(folder/'screenshot.json',shot)
  save(folder/'state.json',session.state);save(folder/'request.json',mounted)
  save(folder/'view.json',view_model(session.state));save(folder/'layout.json',layout)
  save(folder/'native.json',read(mounted['result']));save(folder/'actions.json',actions(mounted))
  save(folder/'mapping.json',read(session.meta['mapping']))
  save(folder/'service-actions.json',read(session.meta['service_actions']))
  owned();require(read(mounted['layout']).get('nonce')==mounted['nonce'],'Capture changed its request nonce')
  files={str(p.relative_to(out)):sha(p) for p in sorted(folder.iterdir()) if p.is_file()}
  checks.append({'name':name,'passed':True,'frame_id':session.meta['frame_id'],'request_nonce':mounted['nonce'],'build_id':build,'evidence':str(folder.relative_to(ROOT)),'artifact_sha256':files})
  return snap
 def click(source,double=False,expect_transition=True,expected_action=None):
  layout=settled();before=copy.deepcopy(session.state);mounted=copy.deepcopy(session.meta['request'])
  mapping=read(session.meta['mapping']);controls=read(session.meta['service_actions'])['controls']
  require(source in controls,'Missing source control binding: '+source)
  matches=[n for n in mapping['elements'] if n['source_id']==source+'_control']
  require(len(matches)==1,'Native control mapping must resolve uniquely')
  native=matches[0]['native_id'];query=reply('WidgetQuery',{'query':'id:'+native})
  require(query.get('query')=='id:'+native and len(query.get('rects',[]))==1,'Native query must resolve the exact id uniquely')
  matches=[n for n in snapshot()['widgets'] if n['id']==native]
  require(len(matches)==1,'Native snapshot must resolve the button uniquely')
  node=matches[0]
  require(node.get('widget_type')=='Button' and node.get('visible') is True,'Service control must be a visible native Button')
  require(enabled_flag(node.get('enabled'))==expect_transition,'Unexpected native enabled state: '+source)
  r=native_rect(node,layout);x,y=round(r[0]+r[2]/2),round(r[1]+r[3]/2)
  clipped=next((n.get('clipped_bounds',n['bounds']) for n in layout['elements'] if n['id']==native),r)
  require(0<=x<406 and 0<=y<776 and clipped[0]<=x<clipped[0]+clipped[2] and clipped[1]<=y<clipped[1]+clipped[3],'Click is outside the inspected visible viewport')
  expected=native_event(before,{'id':native,'action':{'kind':'activated'}},mapping,controls,'expected-only')
  if expected_action:require(expected['action']==expected_action,'Control resolved to wrong service action')
  baseline=actions(mounted);input_path=out/('input-'+str(len(inputs)+1).zfill(2)+'-'+source+'.json')
  evidence={'source_control':source,'native_id':native,'query':query,'snapshot':node,'bounds':r,'click':[x,y],'nonce':mounted['nonce'],'build_id':build,'click_count':2 if double else 1,'expected_event':expected,'before_state':before,'before_actions':baseline}
  save(input_path,evidence)
  for _ in range(2 if double else 1):
   owned();request('Click',{'build_id':build,'x':x,'y':y})
  # Collect before remounting: reducer rejection must not conceal a broken
  # disabled native control, and double-payment evidence must show two inputs.
  deadline=time.monotonic()+(8 if expect_transition else .8);observed=[];activated=[]
  while time.monotonic()<deadline:
   owned();observed=actions(mounted)[len(baseline):]
   activated=[a for a in observed if a.get('action',{}).get('kind')=='activated']
   if expect_transition and len(activated)>=(2 if double else 1):break
   if not expect_transition and activated:break
   time.sleep(.08)
  evidence.update(observed_actions=observed,activated_count=len(activated));save(input_path,evidence)
  if not expect_transition:
   require(not activated,'Disabled native button emitted an activation')
   session.poll_native();require(session.state==before,'Disabled button changed service state')
   after=next(n for n in snapshot()['widgets'] if n['id']==native)
   require(not enabled_flag(after.get('enabled')),'Disabled native button became enabled')
   evidence['after_snapshot']=after
  else:
   require(len(activated)==(2 if double else 1),'Expected native activation count was not observed: '+source)
   for a in activated:
    resolved=native_event(before,a,mapping,controls,'observed-only')
    require(resolved is not None and resolved['action']==expected['action'] and resolved['payload']==expected['payload'],'Click activated another service control')
   deadline=time.monotonic()+8
   while time.monotonic()<deadline and session.state['revision']==before['revision']:
    session.poll_native();time.sleep(.08)
   require(session.state['revision']==before['revision']+1,'Native input did not produce exactly one accepted service transition')
   require(any(key.startswith(mounted['nonce']+':') for key in session.state['processed_events']),'Service transition has no matching native event id')
   settled()
  evidence.update(passed=True,after_state=session.state,next_nonce=session.meta['request']['nonce']);save(input_path,evidence)
  inputs.append({'path':str(input_path.relative_to(ROOT)),'sha256':sha(input_path),'source':source,'action':expected['action'],'native_activations':len(activated),'passed':True})
 def provider(action):
  event={'id':'native-verify-'+uuid.uuid4().hex,'action':action,'actor':'provider'};before=copy.deepcopy(session.state)
  session.dispatch(event)
  settled()
  save(out/('provider-'+action+'.json'),{'event':event,'before':before,'after':session.state,'simulation':True})
 try:
  proof=provenance(build);save(out/'provenance.json',proof)
  session.start(states[1])
  capture('01-product-app')
  click('buy',expected_action='order.purchase_demo')
  require(session.meta['frame_id']==2 and session.state['order']['status']=='paid_demo','Native purchase did not create the demonstration order')
  capture('02-order-app')
  click('back',expected_action='navigation.desktop')
  require(session.meta['frame_id']==3 and session.state['ui']['surface']=='desktop','Native back did not show the desktop order card')
  capture('03-desktop-order-card')
  provider('logistics.out_for_delivery')
  require(session.meta['frame_id']==4 and session.state['delivery']['status']=='out_for_delivery','Provider update did not show the logistics card')
  capture('04-logistics-update')
  provider('logistics.delivered')
  require(session.meta['frame_id']==5 and session.state['installation']['status']=='available','Delivery did not enable the installation service')
  capture('05-installation-offer')
  click('choose_time',expected_action='installation.open_slots')
  require(session.meta['frame_id']==6,'Native choose-time action did not expand the picker')
  capture('06-slot-picker')
  click('conflict_slot',expect_transition=False,expected_action='installation.choose_slot')
  require(session.state['installation']['selected_slot_id'] is None,'Conflict slot was selected')
  capture('07-conflict-blocked')
  click('afternoon',expected_action='installation.choose_slot')
  require(session.meta['frame_id']==7 and session.state['installation']['selected_slot_id']=='afternoon','Afternoon slot selection failed')
  capture('08-selected-afternoon')
  click('confirm_booking',expected_action='installation.confirm')
  event_id=session.state['fixture']['calendar']['installation_event_id']
  require(session.meta['frame_id']==8 and session.state['installation']['status']=='booked' and event_id in session.state['calendar']['events'],'Booking and calendar were not committed together')
  booked=copy.deepcopy(session.state['installation']);calendar_event=copy.deepcopy(session.state['calendar']['events'][event_id])
  unrelated={key:value for key,value in session.state['calendar']['events'].items() if key!=event_id}
  capture('09-booking-and-calendar')
  click('acknowledge_calendar',expected_action='calendar.acknowledge')
  require(session.state['calendar']['acknowledged'] and session.state['installation']==booked,'Calendar acknowledgement changed the service reservation')
  require(sum(n['kind']=='calendar.upsert' for n in session.state['effects'])==1,'Acknowledgement duplicated the calendar event')
  snap=capture('10-calendar-acknowledged')
  require(any(n.get('text')=='已确认' for n in snap['widgets']),'Native acknowledgement label was not updated')
  click('acknowledge_calendar',expect_transition=False,expected_action='calendar.acknowledge')
  click('undo_calendar',expected_action='calendar.undo')
  require(session.meta['frame_id']==9 and session.state['installation']==booked and session.state['calendar']['events']==unrelated,'Calendar undo changed the booking or unrelated events')
  capture('11-calendar-only-undo')
  click('restore_calendar',expected_action='calendar.restore')
  require(session.state['calendar']['events'][event_id]==calendar_event and session.state['installation']==booked,'Calendar restore changed the reservation or event identity')
  require(sum(n['kind']=='installation.upsert' for n in session.state['effects'])==1,'Calendar restore rebooked the service')
  capture('12-calendar-restored')
  provider('installation.technician_departed');require(session.meta['frame_id']==10,'Technician update did not show the service card')
  capture('13-technician-arriving')
  provider('installation.completed')
  require(session.state['payment']['status']=='pending' and session.state['payment']['receipt'] is None,'Service completion must not authorize payment')
  capture('14-payment-pending');calendar_before_payment=copy.deepcopy(session.state['calendar'])
  click('withdraw_payment_request',expected_action='payment.cancel')
  require(session.state['payment']['status']=='cancelled' and session.state['payment']['receipt'] is None and session.state['installation']['status']=='completed' and session.state['calendar']==calendar_before_payment,'Pending cancellation changed service/calendar or created a receipt')
  snap=capture('15-payment-request-cancelled')
  require(any(n.get('text')=='重新打开' for n in snap['widgets']),'Cancelled payment native action label was not rebound')
  click('withdraw_payment_request',expect_transition=False,expected_action='payment.cancel')
  click('pay_materials',expected_action='payment.reopen')
  require(session.state['payment']['status']=='pending' and session.state['payment']['receipt'] is None,'Reopening a payment request captured money')
  capture('16-payment-request-reopened')
  click('pay_materials',double=True,expected_action='payment.pay')
  require(session.meta['frame_id']==12 and session.state['payment']['receipt']['amount_minor']==13000,'Expected simulated receipt is missing')
  require(sum(n['kind']=='payment.capture_demo' for n in session.state['effects'])==1,'Repeated native clicks created multiple payment captures')
  capture('17-payment-once')
  click('view_payment_receipt',expected_action='navigation.open_app')
  require(session.state['ui']['surface']=='app' and session.state['ui']['app']=='payment' and session.state['ui']['page']=='receipt','Receipt route did not open the internal payment view')
  snap=capture('18-native-receipt-route')
  require(any(n.get('text')=='付款凭证' for n in snap['widgets']),'Internal receipt route has no native heading')
  require(len(checks)==18 and {n['frame_id'] for n in checks}==set(range(1,13)),'Native evidence does not cover all 12 design frames and 18 flow states')
  require(sha(ROOT/proof['infrastructure_path'])==proof['infrastructure_sha256'],'Infrastructure changed during verification')
  for path,digest in proof['source_sha256'].items():require(sha(source_path(path))==digest,'Source changed during verification: '+path)
  report={'passed':True,'build_id':build,'checks':checks,'inputs':inputs,'provenance':proof,
          'mode':'Makepad Studio native Click, WidgetQuery, WidgetSnapshot, Screenshot; deterministic local services','simulation':True,
          'route_scope':'Internal native data preview; no external OS application launched',
          'double_payment_scope':'Two observed native activations from the same mount; one accepted service transition and one simulated receipt',
          'screenshot_policy':'Original Studio backing PNG plus exact 812x1552 viewport crop and hash receipt; no resampling'}
  save(out/'report.json',report);save(ROOT/'evidence/native-flow-latest.json',{'directory':str(out.relative_to(ROOT)),**report})
  print(json.dumps({'passed':True,'checks':len(checks),'inputs':len(inputs),'report':str(out/'report.json')}),flush=True)
 except Exception as e:
  save(out/'report.json',{'passed':False,'checks':checks,'inputs':inputs,'error':str(e),'build_id':build,'provenance':proof})
  raise

def self_check():
 """Validate the verifier and the full control sequence without native claims."""
 require(not enabled_flag(False) and not enabled_flag(0) and not enabled_flag(0.0),'Numeric disabled classification failed')
 require(enabled_flag(True) and enabled_flag(1),'Enabled classification failed')
 for value in (None,'false','0',[],2):
  try:enabled_flag(value)
  except RuntimeError:pass
  else:raise RuntimeError('Invalid native enabled state was accepted')
 require(native_rect({'id':'button','x':1,'y':2,'width':30,'height':40},{})==[1,2,30,40],'Native snapshot geometry was not used')
 state=demo_states()[0][1]
 plan=[('buy','order.purchase_demo',True),('back','navigation.desktop',True),
       (None,'logistics.out_for_delivery',True),(None,'logistics.delivered',True),
       ('choose_time','installation.open_slots',True),('conflict_slot','installation.choose_slot',False),
       ('afternoon','installation.choose_slot',True),('confirm_booking','installation.confirm',True),
       ('acknowledge_calendar','calendar.acknowledge',True),('acknowledge_calendar','calendar.acknowledge',False),
       ('undo_calendar','calendar.undo',True),('restore_calendar','calendar.restore',True),
       (None,'installation.technician_departed',True),(None,'installation.completed',True),
       ('withdraw_payment_request','payment.cancel',True),('withdraw_payment_request','payment.cancel',False),
       ('pay_materials','payment.reopen',True),('pay_materials','payment.pay',True),
       ('view_payment_receipt','navigation.open_app',True)]
 frames={1}
 with tempfile.TemporaryDirectory(prefix='octosense-verifier-selfcheck-') as temporary:
  for index,(source,action,enabled) in enumerate(plan):
   if source:
    rendered=render_runtime(state,view_model(state),Path(temporary)/str(index))
    mapping=read(rendered['mapping']);controls=read(rendered['service_actions'])['controls']
    node=next(n for n in mapping['elements'] if n['source_id']==source+'_control')
    require(enabled_flag(node['enabled'])==enabled,'Rendered enabled state differs at '+source)
    event=native_event(state,{'id':node['native_id'],'action':{'kind':'activated'}},mapping,controls,'selfcheck-'+str(index))
    require(event['action']==action,'Wrong source-to-service binding: '+source)
    if not enabled:continue
   else:event={'id':'selfcheck-'+str(index),'action':action,'actor':'provider'}
   state=reduce(state,event);frames.add(view_model(state)['frame_id'])
 require(frames==set(range(1,13)),'Offline flow does not cover all twelve design frames')
 require(state['ui']['page']=='receipt' and state['payment']['receipt']['amount_minor']==13000,'Offline flow did not reach the receipt route')
 require(sum(n['kind']=='payment.capture_demo' for n in state['effects'])==1,'Offline flow duplicated payment')
 print(json.dumps({'passed':True,'mode':'offline verifier self-check','control_and_provider_steps':len(plan),
                   'design_frames':sorted(frames),'studio_called':False,'live_request_changed':False}),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--build-id',type=json.loads);p.add_argument('--self-check',action='store_true');args=p.parse_args()
 if args.self_check:self_check()
 elif args.build_id is None:p.error('--build-id is required for native verification')
 else:run([args.build_id] if type(args.build_id) is int else args.build_id)
