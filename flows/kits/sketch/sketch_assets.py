"""Isolated Sketch graphic exports with explicit, reproducible paint bounds."""
import copy
import hashlib
import json
import math
import pathlib
import subprocess
import uuid
import zipfile
from PIL import Image, ImageChops


def clipping_style(mask):
    # Outline masks use geometry alone. Alpha masks require their original
    # gradient/image alpha; clearing their fills clips every descendant away.
    if mask.get('clippingMaskMode',0)==1:
        return copy.deepcopy(mask.get('style',{}))
    return {'_class':'style','fills':[],'borders':[],'shadows':[],'innerShadows':[]}


def isolated_document(source, destination, page_member, page):
    """Keep only the export page and its resources, avoiding a full kit copy."""
    with zipfile.ZipFile(source) as src:
        document=json.loads(src.read('document.json'))
        document['pages']=[p for p in document['pages'] if p['_ref']+'.json'==page_member]
        if len(document['pages'])!=1:
            raise ValueError('isolated export page is not referenced by the source document')
        document['currentPageIndex']=0
        # Export nodes come from the detached document and contain no instances.
        document['foreignSymbols']=[]
        refs=set()
        def visit(value):
            if isinstance(value,dict):
                for key,child in value.items():
                    if key=='_ref' and isinstance(child,str) and child.startswith('images/'):
                        refs.add(child)
                    else:visit(child)
            elif isinstance(value,list):
                for child in value:visit(child)
        visit(page);visit(document)
        with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as dst:
            dst.writestr('document.json',json.dumps(document))
            dst.writestr(page_member,json.dumps(page))
            for name in src.namelist():
                if name in ('document.json',page_member) or name.startswith(('pages/','previews/')):
                    continue
                if name.startswith('images/') and name not in refs:
                    continue
                dst.writestr(name,src.read(name))


def backdrop_prefix(source, target_id):
    """Only layers painted through the unsupported graphic, in source order."""
    result=copy.deepcopy(source)
    if source.get('do_objectID')==target_id:return result,True
    if 'layers' in source:
        result['layers']=[]
        for child in source['layers']:
            prefix,found=backdrop_prefix(child,target_id)
            result['layers'].append(prefix)
            if found:return result,True
    return result,False


def export_graphics(sketchtool, source, original, raw_nodes, nodes, out, work, native_first=False,
                    backdrop_source=None,spec=None):
    def is_artboard(n):
        return n.get('_class') == 'artboard' or (n.get('_class') == 'group' and n.get('groupBehavior') == 1)
    page_file, page = next((p, json.loads(p.read_text()))
        for p in (original/'pages').glob('*.json')
        if any(is_artboard(n) for n in json.loads(p.read_text()).get('layers', [])))
    template = next(n for n in page['layers'] if is_artboard(n))
    page = copy.deepcopy(page)
    page['layers'] = []
    exports = []
    coverage = {}
    text_checks = {}
    def has_rotation(n):
        return bool(n.get('rotation')) or any(has_rotation(c) for c in n.get('layers', []))
    for n in nodes:
        raw = copy.deepcopy(raw_nodes[n['object_id']])
        # This isolated leaf's mask role is recreated for later source siblings
        # by their mask chains. Here it must remain clipped by its own ancestors,
        # rather than starting a new chain and escaping their clipping.
        raw['hasClippingMask']=False
        if 'rot' in n:
            raw['rotation']=n['rot']
        if 'flip_x' in n:
            raw['isFlippedHorizontal']=n['flip_x']
            raw['isFlippedVertical']=n.get('flip_y',False)
        if native_first and n.get('ancestor_opacity',1)!=1:
            context=raw.setdefault('style',{}).setdefault('contextSettings',{'_class':'graphicsContextSettings'})
            context['opacity']=context.get('opacity',1)*n['ancestor_opacity']
        w,h = n['w'],n['h']
        # A fixed transparent canvas avoids Sketch's implicit trimming of
        # rotated subpaths, outside strokes and asymmetric shadows.
        shadow = n.get('shadow') or {}
        pad = math.ceil((max(w,h)/2 if has_rotation(raw) else 0) + 8 + shadow.get('blur',0)*3
                        + abs(shadow.get('dx',0)) + abs(shadow.get('dy',0))
                        + n.get('stroke',{}).get('w',0)*2)
        if n.get('backdrop_fallback'):
            angle=math.radians(raw.get('rotation',0))
            rotated_padding=max(0,(abs(w*math.cos(angle))+abs(h*math.sin(angle))-w)/2,
                                  (abs(w*math.sin(angle))+abs(h*math.cos(angle))-h)/2)
            pad=math.ceil(rotated_padding+1+shadow.get('blur',0)*3+abs(shadow.get('dx',0))+
                          abs(shadow.get('dy',0))+n.get('stroke',{}).get('w',0)/2)
        aw,ah = math.ceil(w+2*pad), math.ceil(h+2*pad)
        artboard_id = str(uuid.uuid5(uuid.NAMESPACE_URL, 'taskplan-graphic:'+n['object_id'])).upper()
        board = copy.deepcopy(template)
        board.update(do_objectID=artboard_id,name=n['object_id'],layers=[raw],
                     hasBackgroundColor=False,includeBackgroundColorInExport=False)
        board['frame'].update(x=0,y=0,width=aw,height=ah)
        raw['frame'].update(x=pad,y=pad)
        # Exporting a leaf alone loses masks owned by preceding siblings. Wrap
        # that leaf in the same mask chain, in artboard-local coordinates. Mask
        # paint stays in its own source-linked graphic; these copies only clip.
        for index, mask in enumerate(reversed(n.get('export_graphic_masks',n.get('graphic_masks', [])))):
            clip = copy.deepcopy(raw_nodes[mask['object_id']])
            def identify(layer, path=''):
                layer['do_objectID'] = str(uuid.uuid5(uuid.NAMESPACE_URL,
                    f"taskplan-mask:{n['object_id']}:{index}:{path}")).upper()
                for i,child in enumerate(layer.get('layers', [])): identify(child,path+'/'+str(i))
            identify(clip)
            clip['frame'].update(x=mask['x']-n['x']+pad,y=mask['y']-n['y']+pad)
            if 'rot' in mask:clip['rotation']=mask['rot']
            if 'flip_x' in mask:
                clip['isFlippedHorizontal']=mask['flip_x']
                clip['isFlippedVertical']=mask.get('flip_y',False)
            clip['style'] = clipping_style(clip)
            clip['hasClippingMask'] = True
            clip['shouldBreakMaskChain'] = False
            raw['shouldBreakMaskChain'] = False
            raw = {'_class':'group','do_objectID':str(uuid.uuid5(uuid.NAMESPACE_URL,f"native-mask-group:{n['object_id']}:{index}")).upper(),
                   'name':'Source mask context','rotation':0,'isVisible':True,
                   'frame':{'_class':'rect','x':0,'y':0,'width':aw,'height':ah},
                   'layers':[clip,raw]}
        board['layers'] = [raw]
        if n.get('backdrop_fallback'):
            mask_id=str(uuid.uuid5(uuid.NAMESPACE_URL,'native-coverage:'+n['object_id'])).upper()
            mask_board=copy.deepcopy(board)
            mask_board.update(do_objectID=mask_id,name=mask_id)
            def normal_blend(layer):
                style=layer.get('style',{})
                if 'contextSettings' in style:style['contextSettings']['blendMode']=0
                for kind in ('fills','borders','shadows','innerShadows'):
                    for paint in style.get(kind,[]):
                        if 'contextSettings' in paint:paint['contextSettings']['blendMode']=0
                for child in layer.get('layers',[]):normal_blend(child)
            normal_blend(mask_board)
            page['layers'].append(mask_board)
            coverage[n['object_id']]=mask_id
            board,found=backdrop_prefix(backdrop_source,n['object_id'])
            if not found:raise ValueError('backdrop target missing from source')
            prefix_ids=set()
            def collect(layer):
                prefix_ids.add(layer['do_objectID'])
                for child in layer.get('layers',[]):collect(child)
            collect(board)
            left,top=n['x']-pad,n['y']-pad
            checks=[]
            def check(node):
                if node['object_id'] in prefix_ids and node.get('text',{}).get('string','').strip():
                    cx,cy=node['x']+node['w']/2,node['y']+node['h']/2
                    radius=math.hypot(node['w'],node['h'])/2 if node.get('rot') else 0
                    x,y,w,h=(cx-radius,cy-radius,radius*2,radius*2) if radius else (node[k] for k in ('x','y','w','h'))
                    if x<left+aw and y<top+ah and x+w>left and y+h>top:
                        checks.append((node['object_id'],[max(0,math.floor((x-left)*2)),max(0,math.floor((y-top)*2)),
                            min(aw*2,math.ceil((x+w-left)*2)),min(ah*2,math.ceil((y+h-top)*2))]))
                for child in node.get('children',[]):check(child)
            check(spec)
            text_checks[n['object_id']]=checks
            board.update(do_objectID=artboard_id,name=n['object_id'])
            board['frame'].update(x=0,y=0,width=aw,height=ah)
            for child in board.get('layers',[]):
                child['frame']['x']-=left;child['frame']['y']-=top
            n['backdrop_context']={'source_ids':sorted(prefix_ids),'text_in_paint_region':[],
                                   'reason':n['backdrop_fallback']}
        page['layers'].append(board)
        exports.append((n,artboard_id,pad,aw,ah))
    asset_doc = work/'graphics.sketch'
    member = str(page_file.relative_to(original))
    # Cache unmodified CLI exports independently of the native SVG normalizer.
    # A repair to widget composition need not re-export unchanged photography.
    cache=work/'graphic-export-cache';cache.mkdir(exist_ok=True)
    source_receipt=json.loads((work/'source-cache.json').read_text())
    provenance={k:source_receipt[k] for k in ('resolved_sha256','sketchtool')}
    signature=hashlib.sha256(json.dumps([page,provenance,native_first],sort_keys=True).encode()+pathlib.Path(__file__).read_bytes()).hexdigest()
    cache_dir=cache/signature
    files=[(n['object_id']+'@2x.'+ext,aid+'@2x.'+ext) for n,aid,_,_,_ in exports for ext in (('png','svg') if native_first else ('png',))]
    files += [(sid+'@2x.coverage.png',aid+'@2x.png') for sid,aid in coverage.items()]
    required=[name for name,_ in files]
    receipt=cache_dir/'receipt.json'
    cached=json.loads(receipt.read_text()) if receipt.exists() else {}
    valid=all((cache_dir/name).is_file() and hashlib.sha256((cache_dir/name).read_bytes()).hexdigest()==cached.get(name) for name in required)
    if valid:
        for name,raw_name in files:(out/raw_name).write_bytes((cache_dir/name).read_bytes())
    else:
        isolated_document(source,asset_doc,member,page)
        subprocess.run([sketchtool,'export','artboards',str(asset_doc),
                        '--items='+','.join([i for _,i,_,_,_ in exports]+list(coverage.values())),
                        '--formats=png,svg' if native_first else '--formats=png','--scales=2',
                        '--use-id-for-name=YES','--overwriting=YES','--output='+str(out)],check=True)
        cache_dir.mkdir(exist_ok=True)
        cached={}
        for name,raw_name in files:
            data=(out/raw_name).read_bytes()
            (cache_dir/name).write_bytes(data);cached[name]=hashlib.sha256(data).hexdigest()
        receipt.write_text(json.dumps(cached,sort_keys=True)+'\n')
    for n,aid,pad,aw,ah in exports:
        path = out/(aid+'@2x.png')
        target = out/(n['object_id']+'@2x.png')
        path.replace(target)
        if n['object_id'] in coverage:
            mask_path=out/(coverage[n['object_id']]+'@2x.png')
            with Image.open(mask_path) as im:mask=im.convert('RGBA').getchannel('A')
            forbidden=[sid for sid,box in text_checks[n['object_id']] if mask.crop(box).getextrema()[1]>0]
            if forbidden:raise ValueError('unsupported backdrop effect intersects native text; requires native composition: '+n['object_id']+': '+','.join(forbidden))
            # Preserve the exact composited pixels only on this graphic's paint
            # coverage. A ring's hole and padding stay transparent, leaving all
            # underlying native labels and widgets independently drawn.
            with Image.open(target) as im:result=im.convert('RGBA')
            result.putalpha(ImageChops.multiply(result.getchannel('A'),mask.point(lambda a:255 if a else 0)))
            result.save(target)
            n['backdrop_context']['coverage_sha256']=hashlib.sha256(mask.tobytes()).hexdigest()
        if native_first:
            (out/(aid+'@2x.svg')).replace(out/(n['object_id']+'@2x.svg'))
        n['paint_bounds'] = [n['x']-pad,n['y']-pad,aw,ah]
        n['graphic_canvas'] = {'artboard_id':aid,'padding':pad,'width':aw,'height':ah}
