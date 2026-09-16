const {chromium}=require('/Users/ychen/home/Octosense-website/node_modules/playwright');
const fs=require('node:fs');const path=require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
 const errors=[];page.on('console',message=>{if(message.type()==='error')errors.push(message.text());});
 try{
  await page.route('http://127.0.0.1:8494/__focus-test',route=>route.fulfill({contentType:'text/html',body:`<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0;background:#f0f5f2}header{height:140px}iframe{width:390px;height:776px;border:0}button{display:block;margin:28px;width:320px;height:58px}footer{height:500px}</style><header>Focus test</header><iframe src="/" title="Native Makepad"></iframe><button id="next" onclick="window.clicks=(window.clicks||0)+1">Next service update</button><footer></footer>`}));
  await page.goto('http://127.0.0.1:8494/__focus-test');
  await page.waitForFunction(()=>document.querySelector('iframe').contentWindow.__octosense?.ready,null,{timeout:60000});
  const frame=page.frames().find(frame=>frame!==page.mainFrame());
  await frame.evaluate(()=>window.__octosense.webgl.focus_keyboard_input());
  await page.locator('#next').scrollIntoViewIfNeeded();
  const before=await page.evaluate(()=>window.scrollY);
  const bounds=await page.locator('#next').boundingBox();
  await page.touchscreen.tap(bounds.x+bounds.width/2,bounds.y+bounds.height/2);
  await page.waitForTimeout(200);
  const result=await page.evaluate(()=>({clicks:window.clicks||0,scrollY:window.scrollY,activeElement:document.activeElement.id}));
  const report={passed:result.clicks===1&&Math.abs(result.scrollY-before)<=1&&result.activeElement==='next'&&errors.length===0,beforeScrollY:before,...result,consoleErrors:errors};
  const out=path.join(__dirname,'smoke-evidence','mobile-focus-'+new Date().toISOString().replaceAll(':','-')+'.json');
  fs.writeFileSync(out,JSON.stringify(report,null,2));console.log(JSON.stringify({...report,evidence:out}));
  if(!report.passed)throw Error('Embedded native input stole parent focus or scroll');
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
