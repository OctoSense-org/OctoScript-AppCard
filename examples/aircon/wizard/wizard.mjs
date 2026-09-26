import {createSession, getView, activateControl, nextUpdate, goBack, restart, errorMessage} from './service.mjs';
import {buildNativePayload} from './render.mjs';

const root = document.querySelector('[data-service-wizard]');
if (root) initialize(root);

function initialize(root) {
  const q = name => root.querySelector(`[data-${name}]`);
  const iframe=q('native-frame'), phone=q('phone'), locale=root.dataset.locale, en=locale==='en';
  const frameURL=iframe.src;
  let session=createSession({locale}), bundle, nativeReady=false, busy=true, generation=0, snapshot=null, renderTimer, loadTimer;
  let currentId=null, awaiting=null, events=[], focusControl=null;
  const loading=q('loading'), retry=q('retry');
  const strings = en ? {
    loading:'Preparing your space…', updating:'Updating your card…',
    failed:'Your cards could not load. Please try again.',
    complete:'You’re all set. Explore the receipt, or start again.',
    click:label=>`Choose “${label}” on the card`,
    update:'Continue below to see the next service update',
    choice:'Explore the actions on your card',
  } : {
    loading:'正在准备你的空间…', updating:'正在更新卡片…',
    failed:'卡片未能加载，请重试。',
    complete:'一切就绪，可以查看回执，或重新体验',
    click:label=>`点击卡片中的「${label}」`,
    update:'准备好后，点击下方按钮查看服务进展',
    choice:'选择卡片中的操作，继续体验',
  };
  function post(message) { iframe.contentWindow?.postMessage(message,location.origin); }
  function setBusy(value) {
    busy=value; root.dataset.busy=String(value);phone.dataset.busy=String(value);
    q('update').disabled=value;q('back').disabled=value||!getView(session).canGoBack;
    for(const button of q('accessible-controls').querySelectorAll('button'))button.disabled=value||button.dataset.enabled!=='true';
  }
  function fail(error) {
    clearTimeout(renderTimer);clearTimeout(loadTimer);setBusy(true);awaiting=null;
    q('loading-text').textContent=strings.failed;loading.hidden=false;retry.hidden=false;
    console.error('[OctoSense wizard]',error);
    root.dataset.status='error';
  }
  function renderGuide() {
    const view=getView(session),s=view.state;
    const phase=['pending','cancelled','paid'].includes(s.payment.status)?3:['available','booked','en_route','completed','cancelled'].includes(s.installation.status)?2:s.ui.surface==='desktop'||s.delivery.status!=='not_dispatched'?1:0;
    root.querySelectorAll('[data-phase]').forEach(item=>{
      const n=Number(item.dataset.phase);item.classList.toggle('is-complete',n<phase);
      if(n===phase)item.setAttribute('aria-current','step');else item.removeAttribute('aria-current');
    });
    q('step-title').textContent=view.guidance.title;
    q('step-description').textContent=view.guidance.description;
    const inApp=s.ui.surface==='app';
    q('surface').textContent=inApp?(en?'IN THE APP':'应用内'):(en?'ON YOUR DESKTOP':'桌面 App Card');
    q('stage-label').textContent=inApp?(en?'YOUR APP':'你的应用'):(en?'YOUR DESKTOP':'你的桌面');
    const primary=view.guidance.primary;
    q('instruction').textContent=view.completed?strings.complete:primary?.kind==='native'?strings.click(primary.label):view.nextUpdate?strings.update:strings.choice;
    q('update').hidden=!view.nextUpdate;q('provider-note').hidden=!view.nextUpdate;
    q('update-label').textContent=view.nextUpdate?.label||'';
    q('back').disabled=busy||!view.canGoBack;
    q('accessible-controls').replaceChildren(...view.nativeControls.map(control=>{
      const button=document.createElement('button');button.type='button';button.textContent=control.label;
      button.dataset.control=control.sourceId;button.dataset.enabled=String(control.enabled);button.disabled=busy||!control.enabled;
      button.addEventListener('click',()=>advance('native',control.sourceId));return button;
    }));
    root.dataset.frame=String(view.frameId);root.dataset.complete=String(view.completed);
  }
  function mount() {
    if(!bundle||!nativeReady)return;
    clearTimeout(renderTimer);clearTimeout(loadTimer);
    const view=getView(session);generation++;currentId=view.renderId;awaiting={id:currentId,generation};snapshot=null;
    setBusy(true);renderGuide();root.dataset.status='rendering';retry.hidden=true;
    // Keep the previous scene visible during a native redraw; it cannot receive input.
    if(!root.dataset.hasRendered){loading.hidden=false;q('loading-text').textContent=strings.loading;}
    try {
      const payload=buildNativePayload(bundle,view,{assetBase:new URL('card-assets/',import.meta.url).href,id:currentId});
      post({type:'octosense:render',...payload,generation});
      renderTimer=setTimeout(()=>fail(new Error('Native scene readiness timed out')),90000);
    } catch(error) { fail(error); }
  }
  function advance(kind,sourceId) {
    if(busy&&kind!=='restart')return;
    if(q('accessible-controls').contains(document.activeElement))focusControl=sourceId;
    q('error').hidden=true;
    try {
      const eventId=`${currentId}:${generation}:${kind}:${sourceId||''}`;
      if(kind==='native')session=activateControl(session,sourceId,eventId,currentId);
      else if(kind==='update')session=nextUpdate(session,eventId);
      else if(kind==='back')session=goBack(session);
      else if(kind==='restart')session=restart(session);
      mount();
    } catch(error) {
      q('error').textContent=errorMessage(error,locale);q('error').hidden=false;
    }
  }
  window.addEventListener('message',event=>{
    if(event.origin!==location.origin||event.source!==iframe.contentWindow||!event.data||typeof event.data!=='object')return;
    const message=event.data;
    if(!String(message.type).startsWith('octosense:'))return;
    events.push(message);if(events.length>80)events.shift();
    if(message.type==='octosense:ready') {
      if(nativeReady)return;nativeReady=true;mount();return;
    }
    if(message.type==='octosense:error') {
      if(message.id!==undefined&&(message.id!==currentId||message.generation!==generation))return;
      fail(new Error(message.error||'Native runtime error'));return;
    }
    if(message.id!==currentId||message.generation!==generation)return;
    if(message.type==='octosense:rendered'&&awaiting) {
      clearTimeout(renderTimer);awaiting=null;snapshot=message;setBusy(false);renderGuide();loading.hidden=true;
      root.dataset.hasRendered='true';root.dataset.status='ready';
      if(focusControl){
        const buttons=[...q('accessible-controls').querySelectorAll('button:not(:disabled)')];
        (buttons.find(button=>button.dataset.control===focusControl)||buttons[0])?.focus({preventScroll:true});
        focusControl=null;
      }
    } else if(message.type==='octosense:snapshot')snapshot=message;
    else if(message.type==='octosense:action'&&!busy)advance('native',message.sourceId||message.control);
  });
  q('update').addEventListener('click',()=>advance('update'));
  q('back').addEventListener('click',()=>advance('back'));
  q('restart').addEventListener('click',()=>advance('restart'));
  async function fetchBundle() {
    const bundleURL=new URL('cards.bundle.json',import.meta.url);bundleURL.search=new URL(import.meta.url).search;
    const response=await fetch(bundleURL);
    if(!response.ok)throw new Error(`Card bundle: ${response.status}`);
    bundle=await response.json();mount();
  }
  retry.addEventListener('click',()=>{
    nativeReady=false;setBusy(true);retry.hidden=true;q('loading-text').textContent=strings.loading;
    iframe.src=frameURL;
    loadTimer=setTimeout(()=>fail(new Error('Native startup timed out')),90000);
    if(!bundle)fetchBundle().catch(fail);
  });
  iframe.addEventListener('load',()=>post({type:'octosense:ping'}));
  const observer=new ResizeObserver(()=>{const width=phone.parentElement.getBoundingClientRect().width;phone.style.transform=`scale(${Math.min(1,width/406)})`;});
  observer.observe(phone.parentElement);
  // Read-only evidence for browser verification; interaction still uses actual widgets.
  Object.defineProperty(window,'__octosenseWizard',{value:{
    get view(){return getView(session);},get nativeSnapshot(){return snapshot;},
    get busy(){return busy;},get generation(){return generation;},get events(){return [...events];},
  },configurable:true});
  renderGuide();setBusy(true);
  loadTimer=setTimeout(()=>fail(new Error('Native startup timed out')),90000);
  fetchBundle().catch(fail);post({type:'octosense:ping'});
}
