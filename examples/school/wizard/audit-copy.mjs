// Exact-font route audit adapted from shared auditor; this writes school evidence only.
import {readFile,writeFile} from 'node:fs/promises';
import metrics from '../../shared/font-metrics.mjs';
import {buildNativePayload} from '../../shared/render.mjs';
const root=new URL('../../',import.meta.url),issues=new Map();
for(const id of ['school']) {
 const service=await import(new URL(`${id}/wizard/service.mjs`,root));
 const bundle=JSON.parse(await readFile(new URL(`${id}/wizard/card-bundle/cards.bundle.json`,root)));
 const routes=JSON.parse(await readFile(new URL(`${id}/route_test.json`,root))).routes;
 for(const locale of ['cn','en'])for(const route of routes) {
  let session=service.createSession({locale});
  const inspect=()=>{
   const view=service.getView(session),payload=buildNativePayload(bundle,view,{id:view.renderId,assetBase:'http://127.0.0.1:4324/wasm/service-cards/card-assets/'});
   for(const node of payload.mapping.elements) {
    if(!node.text)continue;
    const placement=payload.data.$kit.placements[node.source_id],style=payload.kit.components[placement.component].style;
    const resolve=v=>v?.$token?payload.kit.tokens[v.$token].value:v;
    const font=String(resolve(style.font_src)),m=metrics[font.includes('Bold')?'Bold':font.includes('Medium')?'Medium':'Regular'];
    const width=Math.max(...node.text.split('\n').map(line=>[...line].reduce((n,c)=>n+(m.advance[c.codePointAt(0)]??m.default),0)))*resolve(style.size);
    if(width>placement.layout.w+2)issues.set(`${id}/${locale}/${view.frameId}/${node.source_id}/${node.text}`,{id,locale,frame:view.frameId,sourceId:node.source_id,text:node.text,width,available:placement.layout.w,size:resolve(style.size)});
   }
  };
  inspect();let index=0;
  for(const step of route.steps){if(step.disabled)continue;const view=service.getView(session),event=`audit-${route.name}-${index++}`;
   if(step.control)session=service.activateControl(session,step.control,event,view.renderId);
   else if(step.update)session=service.nextUpdate(session,event);
   else if(step.back)session=service.goBack(session);
   else if(step.restart)session=service.restart(session);
   inspect();
  }
 }
}
console.log(JSON.stringify([...issues.values()],null,2));
await writeFile(new URL('../copy-audit.json',import.meta.url),JSON.stringify([...issues.values()],null,2)+'\n');
