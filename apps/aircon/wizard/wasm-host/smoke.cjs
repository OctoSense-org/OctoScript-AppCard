const { chromium } = require('~/home/Octosense-website/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../..');
const testOrigin = process.env.OCTOSENSE_TEST_ORIGIN;
const appURL = testOrigin ? `${testOrigin}/wasm/service-cards/` : 'http://127.0.0.1:8494/';
const assetBase = `${appURL}card-assets/`;
const out = path.join(__dirname, 'smoke-evidence', new Date().toISOString().replaceAll(':', '-'));
fs.mkdirSync(out, { recursive: true });
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const save = (name, value) => fs.writeFileSync(path.join(out, name), JSON.stringify(value, null, 2));
(async () => {
 const browser = await chromium.launch({ headless: true, ...(process.env.OCTOSENSE_CHROMIUM_EXECUTABLE ? {executablePath:process.env.OCTOSENSE_CHROMIUM_EXECUTABLE} : {}) });
 const page = await browser.newPage({ viewport: { width: 406, height: 776 }, deviceScaleFactor: 2 });
 const logs = [];
 if(process.env.OCTOSENSE_DEBUG)page.on('request',r=>console.log('REQUEST',r.url()));
 page.on('console', msg => { logs.push({type:msg.type(),text:msg.text()}); if(msg.type()==='error'||process.env.OCTOSENSE_DEBUG) console.log(msg.type(),msg.text()); });
 page.on('pageerror', error => { logs.push({ type:'pageerror', text:String(error) }); console.log(String(error)); });
 try {
  if (testOrigin) {
   const dist = path.join(root, 'wizard/wasm-dist');
   const types = { '.html':'text/html', '.js':'text/javascript', '.mjs':'text/javascript', '.wasm':'application/wasm', '.json':'application/json', '.ttf':'font/ttf', '.png':'image/png', '.jpg':'image/jpeg', '.svg':'image/svg+xml' };
   await page.route(`${testOrigin}/**`, async route => {
    const url = new URL(route.request().url());
    if (!url.pathname.startsWith('/wasm/service-cards/')) return route.fulfill({status:404,body:'Outside test package'});
    const relative = decodeURIComponent(url.pathname.slice('/wasm/service-cards/'.length)) || 'index.html';
    const file = path.resolve(dist, relative);
    if (!file.startsWith(dist + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) return route.fulfill({status:404,body:'Missing test asset'});
    await route.fulfill({status:200,path:file,contentType:types[path.extname(file)] || 'application/octet-stream'});
   });
  }
  console.log('Opening',appURL);
  await page.goto(appURL);
  console.log('Document loaded');
  await page.waitForFunction(() => window.__octosense?.ready, null, { timeout: 120000 });
  console.log('Native ready');
  const source = path.join(root, 'cards/aircon-07');
  const map = read(path.join(source, 'mapping.json'));
  const payload = { id:'smoke-07', generation:1, width:406, height:776,
   card:fs.readFileSync(path.join(source,'page.card'),'utf8'), data:read(path.join(source,'page.data.json')),
   kit:read(path.join(source,'kit/native/light/kit.json')), mapping:map, updates:[] };
  const request = JSON.parse(JSON.stringify(payload).replaceAll('http://127.0.0.1:8170/ux-images/', assetBase));
  await page.evaluate(value => window.__octosense.mount(value), request);
  console.log('Scene 7 submitted');
  await page.waitForFunction(() => window.__octosense.snapshot?.generation === 1, null, { timeout: 60000 });
  const snap = await page.evaluate(() => window.__octosense.snapshot);save('snapshot.json',snap);
  await page.locator('canvas').screenshot({ path:path.join(out,'native-wasm.png') });
  const control = sourceId => snap.widgets.find(w => w.sourceId === sourceId);
  const click = async sourceId => {const w=control(sourceId); if(!w)throw Error('Missing '+sourceId);const[x,y,width,height]=w.bounds;await page.mouse.click(x+width/2,y+height/2);await page.waitForTimeout(300);};
  await click('conflict_slot_control');
  let events = await page.evaluate(() => window.__octosense.events);
  if(events.some(e=>e.type==='octosense:action'))throw Error('Disabled control activated');
  await click('confirm_booking_control');
  events = await page.evaluate(() => window.__octosense.events);
  if(!events.some(e=>e.type==='octosense:action'&&e.sourceId==='confirm_booking'&&e.generation===1))throw Error('Native confirmation did not activate');
  const photoSource=path.join(root,'cards/aircon-01');
  const photo={id:'smoke-01',generation:2,width:406,height:776,
   card:fs.readFileSync(path.join(photoSource,'page.card'),'utf8'),data:read(path.join(photoSource,'page.data.json')),
   kit:read(path.join(photoSource,'kit/native/light/kit.json')),mapping:read(path.join(photoSource,'mapping.json')),updates:[]};
  await page.evaluate(value=>window.__octosense.mount(value),JSON.parse(JSON.stringify(photo).replaceAll('http://127.0.0.1:8170/ux-images/',assetBase)));
  await page.waitForFunction(()=>window.__octosense.snapshot?.generation===2,null,{timeout:30000});
  save('photo-snapshot.json',await page.evaluate(()=>window.__octosense.snapshot));
  await page.locator('canvas').screenshot({path:path.join(out,'photo-native-wasm.png')});
  await page.evaluate(value=>window.__octosense.mount(value),{...request,id:'smoke-enabled',generation:3,updates:[{id:'conflict_slot_control',enabled:true},{id:'text_123',text:'周日 9月20日'}]});
  await page.waitForFunction(()=>window.__octosense.snapshot?.generation===3,null,{timeout:30000});
  const enabledSnap=await page.evaluate(()=>window.__octosense.snapshot);
  const enabled=enabledSnap.widgets.find(w=>w.sourceId==='conflict_slot_control');
  if(!enabled.enabled)throw Error('Native enabled override did not apply');
  if(enabledSnap.widgets.find(w=>w.sourceId==='text_123').text!=='周日 9月20日')throw Error('Native text override did not apply');
  await page.mouse.click(enabled.bounds[0]+enabled.bounds[2]/2,enabled.bounds[1]+enabled.bounds[3]/2);
  await page.waitForTimeout(300);
  events=await page.evaluate(()=>window.__octosense.events);
  if(!events.some(e=>e.type==='octosense:action'&&e.sourceId==='conflict_slot'&&e.generation===3))throw Error('Enabled override did not activate');
  save('updated-snapshot.json',enabledSnap);
  const rejectedAssets = [];
  for (const src of [
   'https://foreign.example/wasm/service-cards/card-assets/aircon-07/assets/icon.svg',
   'https://octosense-org.github.io/wasm/service-cards/card-assets/aircon-07/assets/icon.svg',
   `${new URL(appURL).origin}/outside/aircon-07/assets/icon.svg`,
   `${assetBase}../outside/assets/icon.svg`,
   `${assetBase}%2e%2e/outside/assets/icon.svg`,
  ]) {
   const result = await page.evaluate(({request,src}) => {
    let changed=false;
    const replace = value => {
     if (!value || typeof value !== 'object') return;
     for (const [key,child] of Object.entries(value)) {
      if (!changed && key==='src' && typeof child==='string') {value[key]=src;changed=true;}
      else replace(child);
     }
    };
    replace(request.data);replace(request.kit);
    if (!changed) throw Error('No artwork src found for rejection fixture');
    try {window.__octosense.mount({...request,id:'invalid-asset',generation:4});return {rejected:false};}
    catch(error) {return {rejected:true,error:String(error)};}
   }, {request,src});
   if (!result.rejected || !result.error.includes('same-origin card-assets')) throw Error('Unsafe artwork accepted: '+src);
   rejectedAssets.push({src,...result});
  }
  if (await page.evaluate(()=>window.__octosense.snapshot.generation)!==3) throw Error('Rejected artwork changed native scene');
  if (logs.some(entry=>entry.type==='error'||entry.type==='pageerror')) throw Error('Browser emitted runtime errors');
  save('events.json',events);save('report.json',{passed:true,url:appURL,renderer:'Makepad/WASM',widgets:snap.widgets.length,disabledBlocked:true,confirmationActivated:true,photoRendered:true,enabledOverrideActivated:true,rejectedAssets,build:read(path.join(root,'wizard/wasm-dist/build.json')).wasm_sha256});
  console.log(JSON.stringify({passed:true,evidence:out}));
 } catch(error) {
  save('error.json',{error:String(error)});save('events.json',await page.evaluate(()=>window.__octosense?.events).catch(()=>[]));
  await page.locator('canvas').screenshot({path:path.join(out,'failed-canvas.png')}).catch(()=>{});
  throw error;
 } finally {save('console.json',logs);await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
