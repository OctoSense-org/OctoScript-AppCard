#!/usr/bin/env python3
"""Export authoritative Sketch references and source-linked Splash design trees.

Sketch resolves symbol overrides/resizing before extraction. Only graphic layers
become image assets; text remains native text and groups remain native Views.
The original archive is never modified. All premium design artifacts stay in work/.
"""
import argparse
import collections
import copy
import hashlib
import fcntl
import functools
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image

import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))
from core.native_paths import repository
from core import kitconf
from sketch2spec import Extractor
from sketch_assets import export_graphics
import native_graphics
import sketch_fonts
import semantic_lowering
from core.source_identity import retained_widget_ids


def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def import_current(receipt,key):
    try:
        row=json.loads(receipt.read_text())
        return (row.get('inputs')==key and bool(row.get('outputs'))
                and all(digest(path)==expected for path,expected in row['outputs'].items()))
    except (OSError,ValueError,KeyError,TypeError):return False


def widget_id(source_id):
    return 'sketch_' + hashlib.sha256(source_id.encode()).hexdigest()[:24]


def taskplan_tab_variant(node):
    """Distinguish a component catalogue from its individual tab variants."""
    name=node.get('name','');variant=node.get('symbol_name','')
    if name=='Tab Field' and not variant and any(
            re.fullmatch(r'State=(Default|Hover|Disable), Type=(Filled|Outline)',c.get('name',''))
            for c in node.get('children',[])):
        return None
    if (node.get('cls')=='group' and re.fullmatch(
            r'State=(Default|Hover|Disable), Type=(Filled|Outline)',name)
            and any(c.get('text') for c in node.get('children',[]))):
        return name
    if name!='Tab Field':return None
    if not any('State='+state in variant for state in ('Default','Hover','Disable')):
        raise ValueError('unsupported Sketch tab variant: '+repr(variant))
    return variant


def raster_to_avoid_seams(n):
    """Should this compound graphic rasterize to PNG instead of native SVG?

    The native SVG rasterizer fills each `<path>` independently, so a wordmark
    built from one glyph-path per letter (nine for "Taskplan") shows hairline
    cracks down the vertical stems where adjacent fills meet — a ghost smudge
    the visual review scored 7/10 and marked rework. The exported 2x PNG has no
    such seam, and the Image emit path already samples premultiplied to avoid
    dark fringes. So a pure fill compound of enough subpaths, with no gradient,
    blur or overlay to reproduce, keeps the raster. Icons of one or two paths
    still take the SVG, which scales and recolours.
    """
    subpaths = [c for c in n.get('children', []) if c.get('cls') == 'shapePath']
    return (len(subpaths) >= 4
            and not n.get('gradient')
            and not n.get('native_vector_blur')
            and not n.get('native_vector_overlay'))


def empty_graphic_children(source):
    """Keep boolean operands inspectable when their compound paints no pixels."""
    children=[]
    for i,child in enumerate(source.get('children',[])):
        if child.get('text') or child.get('image') or child.get('control'):
            raise ValueError('empty graphic cannot suppress text, images or controls')
        child.pop('graphic_part_of',None)
        child['native_widget_id']=widget_id(source['native_widget_id']+'/'+str(i)+'/'+child['object_id'])
        child['empty_graphic_owner']=source['native_widget_id']
        children.append(dict(t='stack',id=child['native_widget_id'],
            **{k:child[k] for k in ('x','y','w','h')},c=empty_graphic_children(child)))
    return children


def artboard_names(artboards, overrides=None):
    """Name collisions must never overwrite another source artboard's evidence."""
    base = {a['object_id']: re.sub(r'[^\w\-]+', '_', a['name']).strip('_')[:60]
            for a in artboards}
    counts = collections.Counter(base.values())
    result = {key: name if counts[name] == 1 else name + '_' + key[:8].lower()
              for key, name in base.items()}
    for key, name in (overrides or {}).items():
        if key not in result or not re.fullmatch(r'[\w-]+', name):
            raise ValueError('invalid source artboard name override: '+str(key))
        result[key] = name
    if len(set(result.values())) != len(result):
        raise ValueError('artboard name overrides collide')
    return result


def splash(value):
    if isinstance(value, dict):
        return '{' + ' '.join(f'{k}: {splash(v)}' for k, v in value.items()) + '}'
    if isinstance(value, list):
        return '[' + ', '.join(splash(v) for v in value) + ']'
    return json.dumps(value, ensure_ascii=False)


def text_spans(path, unrotated_size=None, source_text=None, source_frame=None):
    """Read Sketch's resolved line breaks and rich-text spans, in layer space."""
    spans = []
    source_origin = [0,0]
    def visit(e, x=0, y=0, style=None, opacity=1):
        style = (style or {}) | e.attrib
        opacity *= float(e.get('opacity',1))
        transform = e.get('transform', '')
        if transform and source_frame is None:
            match = re.fullmatch(r'translate\(([-\d.eE]+)[, ]+([-\d.eE]+)\)', transform)
            if not match:
                rotated=re.fullmatch(r'translate\(([-\d.eE]+), ([-\d.eE]+)\) rotate\(([-\d.eE]+)\) translate\(([-\d.eE]+), ([-\d.eE]+)\)',transform)
                if not rotated or unrotated_size is None or any(abs(float(rotated[i])+float(rotated[i+3]))>.001 for i in (1,2)):
                    raise ValueError('unsupported rich text transform: ' + transform)
                source_origin[:]=[x+float(rotated[1])-unrotated_size[0]/2,
                                  y+float(rotated[2])-unrotated_size[1]/2]
            else:
                x += float(match[1]); y += float(match[2])
        if e.tag.endswith('}tspan') and e.text:
            spans.append(dict(text=e.text, x=x+float(e.get('x',0)), y=y+float(e.get('y',0)),
                              font=style['font-family'].split(',')[0], size=float(style['font-size']),
                              color=style.get('fill','#111927'),
                              opacity=opacity*float(style.get('fill-opacity',1)),
                              tracking=float(style.get('letter-spacing',0))))
        for child in e: visit(child,x,y,style,opacity)
    visit(ET.parse(path).getroot())
    if source_frame is not None:
        # Sketch emits tspan coordinates in the text layer's parent space.
        # Its export crop and ancestor rotations are presentation transforms;
        # neither changes the baseline inside the unrotated source frame.
        source_origin[:]=[source_frame['x'],source_frame['y']]
    for span in spans:
        span['x']-=source_origin[0];span['y']-=source_origin[1]
    if source_text is not None:
        # SVG omits paragraph-break characters because spans already carry y.
        # Retain a semantic separator at those boundaries without drawing an
        # additional line or changing the following span's measured position.
        compact=lambda s:re.sub(r'\s','',s)
        if compact(''.join(s['text'] for s in spans))!=compact(source_text):
            raise ValueError('Sketch text measurement changed source content: '+str(path))
        cursor=0
        for i,span in enumerate(spans):
            chars=compact(span['text'])
            for j,char in enumerate(chars):
                start=cursor
                while cursor<len(source_text) and source_text[cursor].isspace():cursor+=1
                if j==0 and i and cursor>start and not spans[i-1]['text'][-1:].isspace():
                    spans[i-1]['text']+=' '
                if cursor>=len(source_text) or source_text[cursor]!=char:
                    raise ValueError('Sketch text span cannot be aligned to source')
                cursor+=1
    return spans


def apply_group_rotations(root):
    """Carry Sketch group rotation into each native element's frame and angle.

    Views retain the source hierarchy, while each leaf owns its transformed
    placement. Graphics export that same accumulated rotation; text uses the
    native rotated text renderer rather than a rasterized group.
    """
    def visit(n, transforms=(), orientation=(1,0,0,1)):
        x,y,w,h=(n[k] for k in ('x','y','w','h'))
        cx,cy=x+w/2,y+h/2
        own=n.get('rot',0)
        fx,fy=n.get('flip_x',False),n.get('flip_y',False)
        next_transforms=transforms+((cx,cy,own,fx,fy),) if own or fx or fy else transforms
        for px,py,degrees,flip_x,flip_y in reversed(transforms):
            rad=math.radians(-degrees)
            dx,dy=cx-px,cy-py
            rx,ry=dx*math.cos(rad)-dy*math.sin(rad),dx*math.sin(rad)+dy*math.cos(rad)
            # Sketch reflects the rotated result in the parent's axes.
            cx,cy=px+rx*(-1 if flip_x else 1),py+ry*(-1 if flip_y else 1)
        rad=math.radians(-own);co,si=math.cos(rad),math.sin(rad)
        sx,sy=(-1 if fx else 1),(-1 if fy else 1)
        a,b,c,d=orientation
        matrix=(a*sx*co+c*sy*si,b*sx*co+d*sy*si,
                -a*sx*si+c*sy*co,-b*sx*si+d*sy*co)
        a,b,c,d=matrix
        reflected=a*d-b*c<0
        angle=-math.degrees(math.atan2(b,-a if reflected else a))
        if transforms:
            n['source_untransformed_frame']=[x,y,w,h]
            n['x'],n['y']=cx-w/2,cy-h/2
            n['ancestor_rotation']=angle-own
            n['ancestor_transform']=True
        if own or transforms or fx or fy:
            n['rot']=round(angle,10)
            n['flip_x'],n['flip_y']=reflected,False
        for child in n.get('children',[]):visit(child,next_transforms,matrix)
    visit(root)


def font_properties(family, source_fonts=None):
    if not family:
        raise ValueError('source text has no resolved font; check fonts before Sketch detachment')
    weight = next((v for k,v in [('SemiBold',600),('Bold',700),('Medium',500),('Light',300)] if k in family),400)
    if family in (source_fonts or {}):
        record=source_fonts[family]
        return dict(weight=record.get('weight',weight), font_src=record['resource'])
    if family == 'AppleColorEmoji':
        return dict(weight=400, font_src='file:/System/Library/Fonts/Apple Color Emoji.ttc')
    if family.startswith('PlusJakartaSans'): font = 'PlusJakartaSans.ttf'
    elif family.startswith('Inter'): font = 'Inter.ttf'
    elif family.startswith('Poppins'): font = family + '.ttf'
    elif family.startswith('Montserrat'):
        return dict(weight=weight,font_src='self:resources/atro/'+family+'.ttf')
    else: raise ValueError(f'font not bundled: {family}')
    return dict(weight=weight, font_src='self:resources/taskplan/' + font)


def validate_text_fonts(text,source_fonts):
    """Validate every rich-text run, including faces Sketch might substitute."""
    names={text.get('run',{}).get('font')}
    for run in text.get('runs',[]):
        names.add(run.get('attributes',{}).get('MSAttributedStringFontAttribute',{}).get('attributes',{}).get('name'))
    for name in sorted(n for n in names if n):font_properties(name,source_fonts)


@functools.cache
def emoji_metrics(size, text):
    # CoreText applies Apple's optical-size adjustment (e.g. a 16 pt emoji
    # has a 20 pt em). Reading only hhea/sbix misses this source behavior.
    from fontTools.ttLib import TTFont
    path='/System/Library/Fonts/Apple Color Emoji.ttc'
    with TTFont(path,fontNumber=0) as font:
        units=font['head'].unitsPerEm
        asc=font['hhea'].ascent/units;desc=font['hhea'].descent/units
    script='''import CoreText; import Foundation
let f=CTFontCreateWithName("AppleColorEmoji" as CFString,Double(CommandLine.arguments[1])!,nil)
let line=CTLineCreateWithAttributedString(NSAttributedString(string:CommandLine.arguments[2],attributes:[NSAttributedString.Key(kCTFontAttributeName as String):f]))
let run=(CTLineGetGlyphRuns(line) as! [CTRun])[0]
var glyph=CGGlyph(); CTRunGetGlyphs(run,CFRange(location:0,length:1),&glyph)
var bounds=CGRect.zero; CTFontGetBoundingRectsForGlyphs(f,.default,&glyph,&bounds,1)
print(CTFontGetAscent(f),-bounds.minY)'''
    ascent,shift=map(float,subprocess.check_output(['swift','-e',script,str(size),text],text=True).split())
    return dict(size=ascent/asc,ascender=asc,descender=desc,baseline_shift=shift)


def apply_emoji_metrics(node, baseline):
    metrics=emoji_metrics(node['size'],node['text']);node['size']=metrics['size']
    # Apple's bitmap glyphs have an optical baseline offset beyond sbix's
    # zero origin. Preserve CoreText's painted position in the native Label.
    baseline+=metrics['baseline_shift']
    node.update(font_asc=baseline/node['size']-metrics['ascender'],
                font_desc=(baseline-node['line_height'])/node['size']-metrics['descender'])


def scale_design(node, scale):
    if scale <= 0:
        raise ValueError('design_scale must be positive')
    for key in ('x','y','w','h','size','line_height','radius','border','tracking','blur','padleft'):
        if key in node: node[key] /= scale
    for child in node.get('c',[]): scale_design(child,scale)


def promote_glass_groups(node, root=True):
    """Keep coincident tooltip wrappers and their foreground widgets together."""
    for child in node.get('c',[]):promote_glass_groups(child,False)
    if root or node.get('t')!='stack' or node.get('variant'):
        return
    # Source button hit areas can include padding around a circular glass
    # background. Its digits/labels still belong above that background.
    if (any(c.get('t')=='button' for c in node.get('c',[])) and
        any(c.get('variant') in ('glass_surface','glass_overlay','glass_group') for c in node.get('c',[]))):
        node['variant']='glass_group'
        return
    for child in node.get('c',[]):
        if child.get('variant') in ('glass_group','glass_surface','glass_overlay') and all(
            # Sketch keyboard backgrounds extend by 1.1 source pixels beyond
            # their symbol frame. Allow one logical point at this 2x source
            # scale, keeping their keys in front of the backdrop surface.
            abs(node.get(k,0)-child.get(k,0))<=2 for k in ('x','y','w','h')):
            node['variant']='glass_group'
            return


def text_row_baselines(spans):
    """Font and emoji baseline offsets within one row are not extra lines."""
    if not spans:
        return []
    rows=[]
    threshold=min(s['size'] for s in spans)*.5
    for y in sorted({s['y'] for s in spans}):
        if not rows or y-rows[-1]>threshold:
            rows.append(y)
    return rows


def measured_line_height(spans, fallback):
    """Use uniform baseline spacing; mixed-font spans can share a text row."""
    rows=text_row_baselines(spans)
    gaps=[b-a for a,b in zip(rows,rows[1:])]
    return gaps[0] if gaps and max(gaps)-min(gaps)<.1 else fallback


def text_row_count(spans, line_height):
    """Include blank paragraph rows evidenced by gaps between SVG baselines."""
    rows=text_row_baselines(spans)
    if not rows or line_height<=0:return len(rows)
    return max(len(rows),1+math.ceil((rows[-1]-rows[0])/line_height-1e-6))


def route_fullscreen_glass(tree):
    """Keep the background photo in Scene and later content above its glass.

    Window Gauss draws its overlay after Scene. An artboard-sized background
    blur must therefore retain its preceding photograph in Scene, and route
    subsequent foreground siblings to the overlay in source paint order.
    """
    routed=[]
    def full(n):
        # SVG export canvases include shadow/AA padding. Its owning source
        # layer, rather than the padded paint child, defines full-screen glass.
        glass=(n.get('variant') in ('glass_surface','glass_overlay','glass_svg') or
            (n.get('variant')=='glass_group' and
             any(c.get('variant')=='glass_svg' for c in n.get('c',[]))))
        return glass and all(
            abs(n.get(k,0)-tree.get(k,0))<=2 for k in ('x','y','w','h'))
    def visit(n):
        if full(n):return True
        found=False
        children=[]
        for child in n.get('c',[]):
            if found:
                wrapper=dict(t='stack',variant='glass_group',id=child['id']+'_foreground',
                    **{k:child.get(k,0) for k in ('x','y','w','h')},c=[child])
                children.append(wrapper);routed.append(child['id'])
            else:
                found=visit(child)
                children.append(child)
        if 'c' in n:n['c']=children
        if found and n.get('variant')=='glass_group':n.pop('variant')
        return found
    visit(tree)
    return routed


def route_glass_foreground(tree):
    """Preserve paint order for later widgets overlapping deferred glass."""
    deferred=[];routed=[]
    def overlaps(a,b):
        return (a.get('x',0)<b.get('x',0)+b['w'] and a.get('y',0)<b.get('y',0)+b['h']
            and a.get('x',0)+a['w']>b.get('x',0) and a.get('y',0)+a['h']>b.get('y',0))
    def visit(n,overlay=False):
        if not overlay and any(overlaps(n,b) for b in deferred):
            wrapper=dict(t='stack',variant='glass_group',id=n['id']+'_foreground',
                **{k:n.get(k,0) for k in ('x','y','w','h')},c=[visit(n,True)])
            routed.append(n['id'])
            return wrapper
        overlay=overlay or n.get('variant')=='glass_group'
        glass=n.get('variant') in ('glass_surface','glass_overlay','glass_svg')
        # An exported shadow may extend beyond the glass it overlaps. Once
        # deferred, that shadow must also precede later labels in its own area.
        # Track painted leaves, not transparent container/hit-area rectangles.
        paints=(n.get('t') in ('text','image','svg','input','toggle','slider') or
                bool(n.get('bg',0)>>24) or bool(n.get('border',0)))
        if glass or (overlay and paints):deferred.append(n)
        if 'c' in n:n['c']=[visit(c,overlay) for c in n['c']]
        return n
    visit(tree)
    return routed


def fixed_text_overflows(raw, spans):
    # Current Sketch writes sizing modes; older documents used textBehaviour.
    fixed=raw.get('verticalSizing') in (0,3) or raw.get('textBehaviour')==2
    rows=sorted({s['y'] for s in spans})
    multiline=len(rows)>1 and rows[-1]-rows[0]>min(s.get('size',0) for s in spans)*.5
    return fixed and multiline and any(s['y']>raw['frame']['height']+2 for s in spans)


def rotated_bounds(x,y,w,h,degrees):
    angle=math.radians(degrees)
    rw=abs(w*math.cos(angle))+abs(h*math.sin(angle))
    rh=abs(w*math.sin(angle))+abs(h*math.cos(angle))
    return x+(w-rw)/2,y+(h-rh)/2,rw,rh


def compose_glass_materials(tree, vector_materials=None):
    """Resolve covering glass tints against the window's shared scene texture.

    Native Gauss samples the scene before overlays. A nested key must therefore
    carry the keyboard material as well as its own tint. Normal alpha blends
    compose exactly; sequential Gaussian radii combine in quadrature.
    """
    vector_materials=vector_materials or {}
    coverage={}
    painted=[]
    findings={}
    def visible_bounds(n):
        x,y=n.get('x',0),n.get('y',0)
        right,bottom=x+n['w'],y+n['h']
        if tree.get('w',0)>0 and tree.get('h',0)>0:
            x,y=max(x,tree.get('x',0)),max(y,tree.get('y',0))
            right=min(right,tree.get('x',0)+tree['w'])
            bottom=min(bottom,tree.get('y',0)+tree['h'])
        return x,y,right,bottom
    def contains(a,b):
        ax,ay,ar,ab=visible_bounds(a);bx,by,br,bb=visible_bounds(b)
        if not (ax<=bx and ay<=by and ar>=br and ab>=bb and bx<br and by<bb):return False
        material=vector_materials.get(a.get('id'))
        if material:
            # Compound glass has holes. Prove the entire candidate is covered
            # using the source export's alpha, never its bounding box alone.
            if a['id'] not in coverage:
                with Image.open(material['coverage']) as im:
                    coverage[a['id']]=im.convert('RGBA').getchannel('A')
            mask=coverage[a['id']]
            sx,sy=mask.width/a['w'],mask.height/a['h']
            box=(math.floor((bx-a.get('x',0))*sx),math.floor((by-a.get('y',0))*sy),
                 math.ceil((br-a.get('x',0))*sx),math.ceil((bb-a.get('y',0))*sy))
            if mask.crop(box).getextrema()[0] < max(1,(material['color']>>24)-1):return False
        return True
    def visit(n):
        variant=n.get('variant')
        material=vector_materials.get(n.get('id'))
        if material:n['bg']=material['color']
        color=n.get('bg',0);alpha=(color>>24)/255
        if variant in ('glass_surface','glass_overlay','glass_svg'):
            for previous in reversed(painted):
                if not contains(previous,n):continue
                if previous.get('variant') not in ('glass_surface','glass_svg'):break
                bg=previous['bg'];ba=(bg>>24)/255
                if variant in ('glass_overlay','glass_svg'):
                    n['color']=bg
                    n['blur']=math.hypot(n.get('blur',0),previous.get('blur',0))
                    findings[n['id']]={'covering_widget_id':previous['id'],
                        'source_tint':color,'backdrop_tint':bg,
                        'method':'native '+('Overlay blend' if variant=='glass_overlay' else 'SVG fill')+' after covering glass tint'}
                    if variant=='glass_overlay':break
                combined=alpha+ba*(1-alpha)
                channels=[round((((color>>shift)&255)*alpha+
                    ((bg>>shift)&255)*ba*(1-alpha))/combined) for shift in (16,8,0)] if combined else [0,0,0]
                n['bg']=(round(combined*255)<<24)|(channels[0]<<16)|(channels[1]<<8)|channels[2]
                if variant!='glass_svg':
                    n['blur']=math.hypot(n.get('blur',0),previous.get('blur',0))
                    findings[n['id']]={'covering_widget_id':previous['id'],
                        'source_tint':color,'composed_tint':n['bg'],
                        'method':'normal alpha composition over covering native glass'}
                break
            if variant!='glass_svg' or material:painted.append(n)
        elif alpha==1 and variant not in ('glass_overlay',):
            painted.append(n)
        for c in n.get('c',[]):visit(c)
    visit(tree)
    return findings


def source_provenance(resolved, source, path):
    """Retain original instance identities and variant names after detachment."""
    resolved['source_path'] = '/'.join(path + [source['object_id']])
    if source.get('symbol_name'):
        resolved['symbol_name'] = source['symbol_name']
    left, right = collections.defaultdict(list), collections.defaultdict(list)
    for i,n in enumerate(source.get('children', [])): left[n['name']].append((i,n))
    for n in resolved.get('children', []): right[n['name']].append(n)
    for name, children in left.items():
        if len(children) == len(right[name]):
            for (i,old),new in zip(children,right[name]):
                source_provenance(new,old,path+[source['object_id'],str(i)])


def annotate_overlay_backdrops(root, raw_nodes):
    """Identify glass whose source backdrop is a later foreground photograph.

    Window Gauss has one scene texture, captured before deferred overlays. It
    cannot include a foreground photo above full-screen glass in that texture.
    Preserve that individual effect with a coverage-masked source graphic.
    """
    fullscreen=False;photos=[]
    def visit(n):
        nonlocal fullscreen
        raw=raw_nodes[n['object_id']]
        blurred=any(b.get('isEnabled') and b.get('type')==3 for b in raw.get('style',{}).get('blurs',[]))
        if fullscreen and (blurred or native_graphics.overlay_graphic(raw)):
            for photo in reversed(photos):
                if (photo['x']<=n['x'] and photo['y']<=n['y'] and
                    photo['x']+photo['w']>=n['x']+n['w'] and photo['y']+photo['h']>=n['y']+n['h']):
                    n['backdrop_fallback']='native window Gauss scene excludes the preceding foreground photograph'
                    n['foreground_backdrop_source_id']=photo['object_id']
                    break
        if blurred and all(abs(n.get(k,0)-root.get(k,0))<=2 for k in ('x','y','w','h')):
            fullscreen=True
        if fullscreen and n.get('image'):photos.append(n)
        for c in n.get('children',[]):visit(c)
    visit(root)


def annotate_group_blends(root, raw_nodes, ancestors=()):
    """An isolated child must retain the effect of its enclosing blend groups."""
    if ancestors:
        root['ancestor_blend_groups']=list(ancestors)
        if root.get('text') or root.get('control'):
            raise ValueError('blended text/control requires native compositing: '+root['object_id'])
        root.setdefault('backdrop_fallback','native SVG cannot sample ancestor group blend modes '+
                        ', '.join(str(a['mode']) for a in ancestors))
    raw=raw_nodes[root['object_id']]
    mode=raw.get('style',{}).get('contextSettings',{}).get('blendMode',0)
    if raw.get('_class')=='group' and mode:
        ancestors=ancestors+({'source_id':root['object_id'],'mode':mode},)
    for child in root.get('children',[]):annotate_group_blends(child,raw_nodes,ancestors)


def annotate_inputs(root, retained_ids=None):
    """Interpret explicit Sketch input variants while retaining source strings.

    A trailing vertical bar in a focused variant denotes its caret. It is
    rendered by TextInput's real cursor, and is never inserted into its value.
    """
    def descendants(n):
        for child in n.get('children', []):
            yield child
            yield from descendants(child)
    for group in [root, *descendants(root)]:
        camo_variant=group.get('symbol_name') or group.get('name','')
        if camo_variant.startswith(('Inputs/Text-Field/','Inputs/Code/')):
            nodes=list(descendants(group))
            title_ids={id(n) for title in nodes if title.get('name')=='Title'
                       for n in descendants(title)}
            fields=[n for n in nodes if n.get('text') and id(n) not in title_ids]
            if fields and all(n.get('control') for n in fields):
                continue
            code=camo_variant.startswith('Inputs/Code/')
            if code and not fields:
                group['control']=dict(kind='text_input',value='',placeholder='',focused=False,
                    enabled=True,password=False,state_source='Camo empty code cell; source underline retained',
                    symbol_name=camo_variant)
                group['native_empty_input']=True
                continue
            if len(fields)!=1:
                raise ValueError('Camo input must have one source value outside its floating title: '+camo_variant)
            field=fields[0];display=field['text']['string']
            placeholder=display if display.lower().startswith(('enter ','search ','your ','full name','password','email address','phone number')) else ''
            masked=bool(display.strip()) and not set(display)-{'•','●','*',' '}
            field['control']=dict(kind='text_input',value='' if placeholder else display,
                placeholder=placeholder,display_text=display,focused=False,enabled=True,password=masked,
                state_source='Camo source value and masking; floating title is styling, not keyboard focus',
                symbol_name=camo_variant)
            continue
        if group.get('name','').startswith('Textfield/'):
            fields = [n for n in descendants(group) if n.get('text') and
                      any(n.get('name','').endswith(s) for s in ('value','label')) and
                      not n.get('name','').endswith('field-label')]
            fields = [n for n in fields if not n.get('control')]
            if not fields:
                continue  # An enclosing source field already annotated its input.
            preferred = [n for n in fields if n['name'].endswith('value')]
            fields = preferred or fields
            if len(fields) != 1:
                raise ValueError('Atro input must have one identifiable source value: '+group['name'])
            field=fields[0]; display=field['text']['string']
            placeholder=display if display.lower().startswith(('find ','search','enter ','type ','write a ','your password','validate new password')) or display in ('MM / YY','CVV No') else ''
            variant=group.get('symbol_name',group['name'])
            masked=bool(display.strip()) and set(display.strip())=={'•'}
            password=masked or (bool(placeholder) and 'password' in placeholder.lower())
            field['control']=dict(kind='text_input',value='' if placeholder else display.strip() if masked else display,
                placeholder=placeholder,display_text=display,focused=':focus' in variant.lower(),enabled=True,password=password,
                leading_spaces=len(display)-len(display.lstrip()) if masked else 0,
                state_source='Atro source value, password mask and focus variant',symbol_name=variant)
            continue
        code = group.get('name') == 'Code Input'
        if group.get('name') not in ('Text Input', 'Text Input/chevron', 'Code Input', 'Search', 'Text Area'):
            continue
        variant = group.get('symbol_name', '').lower()
        if not variant and group['name']=='Search':
            continue  # A page/section title, not a source symbol control.
        if not variant:
            raise ValueError('input lacks original Sketch variant provenance')
        nodes = list(descendants(group))
        fields = [n for n in nodes if (code or n.get('name') == 'Text') and n.get('text')]
        if code and not fields:
            group['control'] = dict(kind='text_input',value='',placeholder='',focused=False,
                                    enabled=True,password=False,state_source='empty Sketch Code Input variant',
                                    symbol_name=group['symbol_name'])
            group['native_empty_input'] = True
            continue
        if len(fields) != 1:
            raise ValueError('input must have exactly one source text field')
        field = fields[0]
        original = field['text']['string']
        focused = 'focus' in variant or (group['name'] == 'Search' and original.endswith('|'))
        display = original[:-1] if focused and original.endswith('|') else original
        placeholder = display if ('default' in variant or
            (group['name'] == 'Search' and display.lower().startswith('search'))) else ''
        password = any('password' in n.get('text', {}).get('string', '').lower()
                       for n in nodes if n.get('name') == 'Label')
        # The kit also shows the eye-open state. Preserve its visible sample
        # value; the field label alone does not imply that masking is active.
        masked = password and not (not placeholder and display and set(display)-{'•'})
        field['control'] = dict(kind='text_input', value='' if placeholder else display,
                                placeholder=placeholder, display_text=display,
                                focused=focused, enabled=True, password=bool(masked),
                                password_field=password,
                                multiline=group['name'] == 'Text Area',
                                state_source='Sketch input variant and source text',
                                symbol_name=group['symbol_name'])

    # Camo draws password masks as sibling circles over a blank input. Bind
    # those explicit source shapes to the editable field and render its real
    # password glyphs, so editing changes the mask instead of leaving an image.
    all_nodes=[root,*descendants(root)]
    identities={}
    def index(n,path=()):
        identities[id(n)]=(retained_ids or {}).get(id(n),widget_id('/'.join((*path,n.get('object_id') or 'node'))))
        for i,c in enumerate(n.get('children',[])):
            index(c,(*path,n.get('object_id') or 'node',str(i)))
    index(root)
    for mask in all_nodes:
        if mask.get('name')!='Password / Hide':continue
        dots=sorted(mask.get('children',[]),key=lambda n:n['x'])
        if not dots or any(d.get('cls')!='oval' or abs(d['w']-d['h'])>.01 for d in dots):
            raise ValueError('password mask must contain only source circles')
        fields=[n for n in all_nodes if n.get('control',{}).get('kind')=='text_input'
                and not n.get('text',{}).get('string','').strip()
                and n['x']<=mask['x'] and n['y']<=mask['y']
                and n['x']+n['w']>=mask['x']+mask['w'] and n['y']+n['h']>=mask['y']+mask['h']]
        if len(fields)!=1:raise ValueError('password circles need one containing native input')
        field=fields[0];display='•'*len(dots)
        field['control'].update(value=display,display_text=display,password=True,
            graphic_mask_source_id=mask['object_id'],state_source='source password circles mapped to native TextInput masking')
        field['native_password_mask']={'dots':[{k:d[k] for k in ('x','y','w','h','fill')} for d in dots]}
        for n in [mask,*descendants(mask)]:n['control_part_of']=identities[id(field)]


def style_password_mask(source,node,fonts):
    """Match the source circle ink using the bundled font's actual bullet bounds."""
    from fontTools.ttLib import TTFont
    from fontTools.pens.boundsPen import BoundsPen
    dots=source['native_password_mask']['dots'];first=dots[0]
    record=fonts[source['text']['run']['font']]
    path=record.get('installed') or record.get('source_file')
    with TTFont(path) as font:
        glyph=font.getBestCmap()[ord('•')];pen=BoundsPen(font.getGlyphSet())
        font.getGlyphSet()[glyph].draw(pen)
        left,bottom,right,top=pen.bounds;units=font['head'].unitsPerEm
        ratio=first['w']/(right-left)
        size=ratio*units;advance=font['hmtx'][glyph][0]*ratio
    if abs((top-bottom)*ratio-first['h'])>.2:
        raise ValueError('native font bullet does not match source password circle')
    step=dots[1]['x']-first['x'] if len(dots)>1 else advance
    if any(abs(d['x']-first['x']-i*step)>.01 or abs(d['y']-first['y'])>.01
           or abs(d['w']-first['w'])>.01 for i,d in enumerate(dots)):
        raise ValueError('password circle spacing or size is not uniform')
    baseline=first['y']-source['y']+top*ratio
    metrics=record['metrics']
    node.update(size=size,tracking=step-advance,padleft=first['x']-source['x']-left*ratio,
        font_asc=baseline/size-metrics['ascender'],
        font_desc=(baseline-node['line_height'])/size-metrics['descender'],
        color=native_graphics.rgba(first['fill']))
    source['text'].update(native_baseline=baseline,source_rows=1)
    source['native_password_mask'].update(font_bullet_bounds=[left,bottom,right,top],
        size=size,baseline=baseline,advance=step)


def source_documents(root, archive, sketchtool, member=None, font_inputs=None):
    """Reuse detached source only with a matching source/tool/content receipt."""
    source, detached = root/'source.sketch', root/'resolved.sketch'
    receipt_path = root/'source-cache.json'
    # The tool version is part of the cache key, but querying it forces
    # sketchtool to exist even when nothing needs re-detaching. Reuse the
    # recorded version when a receipt is present, and only shell out to the
    # tool if the cache actually misses — a re-lowering on a host without
    # Sketch installed then works from the already-resolved document.
    prior=json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
    version=(prior.get('sketchtool') if prior else None) or (
        subprocess.check_output([sketchtool, '--version'], text=True).strip()
        if sketchtool else None)
    with zipfile.ZipFile(archive) as z:
        members = [n for n in z.namelist() if n.endswith('.sketch') and not n.startswith('__MACOSX/')]
        if member is not None:
            if member not in members:
                raise ValueError('configured Sketch member is absent from the archive: ' + member)
            members = [member]
        if len(members) != 1:
            raise ValueError('set sketch_member when the archive contains multiple Sketch documents')
        document = z.read(members[0])
    expected = {'archive_sha256':digest(archive), 'member':members[0],
                'source_sha256':hashlib.sha256(document).hexdigest(), 'sketchtool':version}
    if font_inputs:
        expected['source_fonts'] = font_inputs
    receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
    current = (all(receipt.get(k)==v for k,v in expected.items())
               and source.exists() and digest(source)==expected['source_sha256']
               and detached.exists() and digest(detached)==receipt.get('resolved_sha256'))
    if not current:
        source.write_bytes(document)
        temporary = root/'resolved.pending.sketch'
        temporary.write_bytes(document)
        subprocess.run([sketchtool, 'detach', str(temporary)], check=True)
        temporary.replace(detached)
        receipt_path.write_text(json.dumps(expected | {'resolved_sha256':digest(detached)},indent=2)+'\n')
    # Always unpack from verified documents, replacing only these importer-owned
    # directories. A changed JSON file in an old extraction cannot become input.
    for document, directory in ((source,root/'original'),(detached,root/'resolved')):
        if directory.exists(): shutil.rmtree(directory)
        with zipfile.ZipFile(document) as z:
            z.extractall(directory)
    return source, detached, version


def apply_group_shadows(node, raw_nodes):
    """An opaque full-frame background carries its enclosing group's shadow.

    The background already contains the group's visible silhouette. Exporting
    its shadow separately preserves native text and controls inside the group.
    Groups without that background keep their effect in the source for review.
    """
    if node.get('shadow') and node.get('children') and node['cls'] != 'shapeGroup':
        def paint_candidates(n):
            for c in n.get('children',[]):
                if not all(abs(c[k]-node[k])<=.25 for k in ('x','y','w','h')):continue
                yield c
                if (c['cls']=='group' and not c.get('fill') and not c.get('rot')
                        and c.get('opacity',1)==1):yield from paint_candidates(c)
        backgrounds = [c for c in paint_candidates(node)
                       if c.get('fill',{}).get('a',0) > .99
                       and c['cls'] in ('rectangle','oval','shapePath','shapeGroup')
                       and all(abs(c[k]-node[k]) <= .25 for k in ('x','y','w','h'))]
        if backgrounds:
            bg = backgrounds[0]
            parent = raw_nodes[node['object_id']]
            child = raw_nodes[bg['object_id']]
            shadows = [s for s in parent.get('style',{}).get('shadows',[]) if s.get('isEnabled')]
            child.setdefault('style',{}).setdefault('shadows',[]).extend(shadows)
            bg.setdefault('inherited_group_effects',[]).append({'source_object_id':node['object_id'],
                                                              'shadow':node['shadow']})
            extent = lambda s: s.get('blur',0)*3 + abs(s.get('dx',0)) + abs(s.get('dy',0))
            bg['shadow'] = max([bg.get('shadow') or {},node['shadow']],key=extent)
    for child in node.get('children',[]): apply_group_shadows(child,raw_nodes)


def annotate_graphic_masks(root, raw_nodes):
    """Retain Sketch's preceding-sibling mask chain for isolated leaf exports."""
    def visit(node, inherited, opacity=1):
        node['graphic_masks'] = inherited
        node['ancestor_opacity'] = opacity
        local = []
        for child in node.get('children', []):
            raw = raw_nodes[child['object_id']]
            if raw.get('shouldBreakMaskChain'):
                local = []
            visit(child, inherited + local, opacity*node.get('opacity',1))
            if child.get('mask'):
                local = [{**{k:child[k] for k in ('object_id','x','y','w','h')},
                          **{k:child[k] for k in ('rot','flip_x','flip_y') if k in child}}]
    visit(root, [])


def annotate_text_tints(root, raw_nodes, inherited=None):
    """A group's opaque foreground fill recolors its children's silhouettes."""
    if root.get('text') and inherited:
        root['text']['group_tint'] = inherited
    raw = raw_nodes[root['object_id']]
    fills = [f for f in raw.get('style',{}).get('fills',[]) if f.get('isEnabled')]
    foreground = [f for f in fills if f.get('layeringType') == 1]
    tint = inherited
    if raw.get('_class') == 'group' and foreground:
        fill = foreground[-1]
        if (fill.get('fillType') == 0 and fill.get('color',{}).get('alpha',1) == 1
            and fill.get('contextSettings',{}).get('blendMode',0) == 0
            and fill.get('contextSettings',{}).get('opacity',1) == 1):
            from sketch2spec import hexa
            # An outer opaque group fill is applied after the inner group's.
            tint = inherited or {'source_id':root['object_id'],'color':hexa(fill['color'])}
    for child in root.get('children',[]):
        annotate_text_tints(child, raw_nodes, tint)


def native_text_color(node, span):
    tint = node['text'].get('group_tint',{}).get('color')
    return native_graphics.rgba({'hex':tint['hex'] if tint else span['color'],
                                'a':span['opacity']})


def text_baseline(node, spans):
    baseline = min((s['y'] for s in spans), default=0)
    text = node['text']
    paragraph = text.get('runs',[{}])[0].get('attributes',{}).get('paragraphStyle',{})
    size = text['run']['size']
    # Sketch's PNG centers the extra leading of an explicit line height.
    # Its SVG export writes the natural baseline and omits that offset.
    # Montserrat's embedded hhea metrics are asc=.968, desc=-.251, gap=0.
    explicit = paragraph.get('minimumLineHeight',0)
    metrics = text.get('font_metrics') or (dict(ascender=.968,descender=-.251,line_gap=0)
              if text['run']['font'].startswith('Montserrat') else None)
    natural = round(size*(metrics['ascender']-metrics['descender']+metrics['line_gap'])) if metrics else 0
    if (metrics and explicit > 0
        and explicit == paragraph.get('maximumLineHeight')):
        leading = (explicit-natural)/2
        # Some SVG exports already compress a short fixed line box. Detect
        # the lowered baseline against the font ascent before applying the
        # same negative leading again (Camo's 60 pt chart numerals).
        if leading<0 and baseline<size*metrics['ascender']-1:
            leading=0
        text['svg_baseline'] = baseline
        text['paragraph_leading_offset'] = leading
        baseline += leading
    if metrics and text.get('vertical_alignment'):
        rows = text_row_baselines(spans)
        height = (rows[-1]-rows[0] if rows else 0) + (explicit or natural)
        offset = max(0,node['h']-height)*text['vertical_alignment']/2
        text['vertical_alignment_offset'] = offset
        baseline += offset
    return baseline


def camo_binary_control(source, node):
    """Use native selection widgets for Camo's explicit source control symbols."""
    variant=source.get('symbol_name') or source.get('name','')
    if variant.startswith('Inputs/Selector/Checkbox/'):
        kind, selected='checkbox', variant.endswith('/Checked')
    elif variant.startswith('Inputs/Selector/Radio-Button/'):
        kind, selected='radio', variant.endswith('/Checked')
    elif variant.startswith('Inputs/Switch-Toggle/'):
        kind, selected='toggle', variant.endswith('/On')
    else:
        return False
    def descendants(n):
        yield n
        for child in n.get('children',[]):yield from descendants(child)
    parts=list(descendants(source))
    if any(n.get('text') or n.get('image') for n in parts):
        raise ValueError('Camo selection decoration cannot flatten text or photos')
    base=next((n for n in parts if n.get('fill') and
               abs(n.get('w',0)-source['w'])<.1 and abs(n.get('h',0)-source['h'])<.1),None)
    stroke=next((n['stroke'] for n in parts if n.get('stroke')),None)
    color=native_graphics.rgba(base['fill']) if base else 0
    mark=next((n['fill'] for n in parts if n is not base and n.get('fill')),dict(hex='#ffffff',a=1))
    node.update(t=kind,variant='camo',on=int(selected),enabled=1,
        color=color if selected else 0xff0077ff,bg=0x1a000000 if selected else color,
        bordercolor=native_graphics.rgba(mark),
        radius=base.get('radius',0) if base else (9 if kind=='radio' else 3))
    if stroke and not selected:
        node['bg']=native_graphics.rgba(stroke['c'])
    source['control']=dict(kind=kind,checked=selected,enabled=True,
        state_source='Camo named selector/switch variant',symbol_name=variant)
    for child in parts[1:]:child['control_part_of']=node['id']
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--kit', required=True)
    p.add_argument('--sketchtool', default=os.environ.get('SKETCHTOOL', shutil.which('sketchtool')))
    p.add_argument('--only',action='append',help='screen-name substring; repeat to repair a selected set')
    p.add_argument('--screen',action='append',help='exact screen name; repeat for a repair set')
    p.add_argument('--repair-feedback',type=pathlib.Path,
                   help='prior measured and visual findings to preserve as input to this repair round')
    p.add_argument('--all', action='store_true', help='import every artboard on the configured page')
    args = p.parse_args()
    kit = kitconf.load(args.kit)
    # sketchtool is required only to DETACH a source document. When the source
    # cache is already resolved (a re-lowering after an importer change, on a
    # host without Sketch), it is not needed — source_documents reuses the
    # recorded tool version and never shells out. Defer the hard error to the
    # point where a detach is actually attempted.
    if not args.sketchtool and not (kit['specs_dir'].parent/'source-cache.json').exists():
        p.error('set SKETCHTOOL to Sketch.app/Contents/MacOS/sketchtool')
    feedback = ({r['screen']:r for r in json.loads(args.repair_feedback.read_text())['screens']}
                if args.repair_feedback else {})
    root = kit['specs_dir'].parent
    root.mkdir(parents=True, exist_ok=True)
    import_lock=(root/'.native-import.lock').open('a')
    try:fcntl.flock(import_lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise RuntimeError('another native import owns '+str(root))
    # Install archive fonts before Sketch resolves symbols: otherwise detachment
    # can permanently substitute unnamed system fonts into the cached document.
    source_fonts=sketch_fonts.bundle_archive(kit)
    source_fonts.update(sketch_fonts.installed_fonts(kit))
    font_inputs=({'sha256':{name:record['sha256'] for name,record in source_fonts.items()},
                  **sketch_fonts.verify_fonts(source_fonts)} if source_fonts else {})
    source, detached, version = source_documents(root,kit['source_archive'],args.sketchtool,kit.get('sketch_member'),font_inputs)
    source_hash, resolved_hash = digest(source), digest(detached)
    unpacked = root / 'resolved'
    source_fonts.update(sketch_fonts.bundle(unpacked))
    if source_fonts:
        (root/'native-fonts.json').write_text(json.dumps(source_fonts,indent=2)+'\n')
    ex = Extractor(unpacked)
    raw_original = root / 'original'
    originals = {a['object_id']: a for a in Extractor(raw_original).artboards(kit.get('pages', ''))}
    names = artboard_names(originals.values(), kit.get('screen_names'))
    for directory in (kit['specs_dir'], kit['targets_dir'], kit['cards_dir'], pathlib.Path(kit['img_dir'])):
        directory.mkdir(parents=True, exist_ok=True)
    selected = []
    for page in ex.pages.values():
        if kit.get('pages', '') not in page['name']:
            continue
        for layer in page.get('layers', []):
            if layer['do_objectID'] not in originals:
                continue
            name = names[layer['do_objectID']]
            if (not args.all and name not in kit['screens']) or (args.only and not any(part in name for part in args.only)):
                continue
            if args.screen and name not in args.screen:continue
            selected.append((name, layer))
    if not selected:
        raise ValueError('no source artboards selected')
    if not args.all and not args.only and not args.screen and set(kit['screens']) != {n for n, _ in selected}:
        raise ValueError('configured screens do not match distinct source artboards')
    # Export before detachment: the reference is always the original document.
    reference_receipt=root/'reference-exports.json'
    receipts=json.loads(reference_receipt.read_text()) if reference_receipt.exists() else {}
    reference_key={'source_sha256':source_hash,'sketchtool':version,'scale':2}
    if font_inputs:reference_key['source_fonts']=font_inputs
    missing=[]
    for _,a in selected:
        sid=a['do_objectID'];previous=receipts.get(sid,{})
        if (previous.get('source')!=reference_key or any(
            not (kit['targets_dir']/f'{sid}@2x.{ext}').is_file() or
            digest(kit['targets_dir']/f'{sid}@2x.{ext}')!=previous.get(ext) for ext in ('png','svg'))):missing.append(sid)
    if missing:
        subprocess.run([args.sketchtool, 'export', 'artboards', str(source),
                        '--items=' + ','.join(missing),
                        '--formats=png,svg', '--scales=2', '--use-id-for-name=YES',
                        '--overwriting=YES', '--output=' + str(kit['targets_dir'])], check=True)
        for sid in missing:
            receipts[sid]={'source':reference_key,**{ext:digest(kit['targets_dir']/f'{sid}@2x.{ext}') for ext in ('png','svg')}}
        reference_receipt.write_text(json.dumps(receipts,sort_keys=True)+'\n')
    import_receipts=root/'import-receipts';import_receipts.mkdir(exist_ok=True)
    _adapter=pathlib.Path(__file__).resolve().parent
    importer_inputs={f:digest(_adapter/f) for f in
        ('sketch_native.py','sketch2spec.py','sketch_assets.py','native_graphics.py','sketch_fonts.py','semantic_lowering.py')}
    importer_inputs['source_identity.py']=digest(kitconf.HERE/'source_identity.py')
    importer_inputs.update({str(p):digest(p) for p in (root/'semantics').rglob('*') if p.is_file()})
    import_key=hashlib.sha256(json.dumps({'code':importer_inputs,'kit':kit,'source':source_hash,
        'resolved':resolved_hash,'fonts':font_inputs},sort_keys=True,default=str).encode()).hexdigest()
    for name, raw in selected:
        receipt=import_receipts/(name+'.json')
        if name not in feedback and import_current(receipt,import_key):
            print(f'{name}: current native import (source, code and output hashes match)',flush=True)
            continue
        frame = raw['frame']
        spec = ex.node(raw, -frame['x'], -frame['y'], 1, 1, {}, [])
        source_provenance(spec, originals[raw['do_objectID']], [])
        apply_group_rotations(spec)
        identity_baseline=root/'semantic-source'/f'{name}.json'
        retained_ids=(retained_widget_ids(spec,json.loads(identity_baseline.read_text()))
                      if identity_baseline.exists() else {})
        annotate_inputs(spec, retained_ids)
        spec.update(cls='artboard', page=kit.get('pages', ''), reference_renderer='Sketch',
                    native_widgets_first=kit.get('native_widgets_first',False),
                    source_sha256=source_hash, resolved_sha256=resolved_hash, sketchtool=version)
        raw_nodes = {}
        def index(n):
            # Imported compound shapes can share an ID with their subpaths.
            # Keep the first, enclosing shape; a later subpath must not replace
            # the full graphic used by the source-linked asset export.
            raw_nodes.setdefault(n['do_objectID'], n)
            for c in n.get('layers', []): index(c)
        index(raw)
        backdrop_source=copy.deepcopy(raw)
        apply_group_shadows(spec, raw_nodes)
        annotate_graphic_masks(spec, raw_nodes)
        annotate_text_tints(spec, raw_nodes)
        annotate_overlay_backdrops(spec,raw_nodes)
        annotate_group_blends(spec,raw_nodes)
        graphics = []
        graphic_nodes = []
        rich_nodes = []
        multiline_nodes = []
        styled_nodes = []
        clipped_text_nodes = []
        native_first = kit.get('native_widgets_first',False)
        def visit(n, path):
            if n.get('text'):validate_text_fonts(n['text'],source_fonts)
            sid = '/'.join(path + [n.get('object_id') or 'node'])
            n['native_widget_id'] = retained_ids.get(id(n),widget_id(sid))
            if n.get('control_part_of'):
                return None
            x,y,w,h = [n[k] for k in ('x','y','w','h')]
            stroke = n.get('stroke',{}).get('w',0)
            # A rule's stroke has area even when its source frame has a zero axis.
            if stroke > 0:
                if w == 0: x -= stroke/2; w = stroke
                if h == 0: y -= stroke/2; h = stroke
            mx,my,mr,mb=x,y,x+w,y+h
            for mask in n.get('graphic_masks',[]):
                if mask.get('rot') or raw_nodes[mask['object_id']].get('rotation'):continue
                mx,my=max(mx,mask['x']),max(my,mask['y'])
                mr,mb=min(mr,mask['x']+mask['w']),min(mb,mask['y']+mask['h'])
            if n.get('graphic_masks') and (mr<=mx or mb<=my):
                n['fully_clipped']=True
                return None
            if n.get('text') and (mx,my,mr,mb)!=(x,y,x+w,y+h):
                n['source_clip_bounds']=[mx,my,mr-mx,mb-my]
            vx,vy,vw,vh=rotated_bounds(x,y,w,h,n.get('rot',0))
            if w <= 0 or h <= 0 or vx >= spec['w'] or vy >= spec['h'] or vx+vw <= 0 or vy+vh <= 0:
                return None
            node = dict(t='stack', id=n['native_widget_id'], x=x, y=y, w=w, h=h)
            if native_first and camo_binary_control(n,node):
                return node
            if native_first and native_graphics.shadow_backdrop_reason(raw_nodes[n['object_id']]):
                n['backdrop_fallback']=native_graphics.shadow_backdrop_reason(raw_nodes[n['object_id']])
            if native_first and native_graphics.overlay_graphic(raw_nodes[n['object_id']]):
                n['native_vector_overlay']=True
            if n.get('mask') and raw_nodes[n['object_id']].get('clippingMaskMode',0)==1:
                if n.get('children'):
                    raise ValueError('compound alpha-mask layout requires explicit descendant mapping')
                n['mask_mode']='alpha'
                n['rendering']={'backend':'native_surface',
                    'reason':'alpha mask coverage is applied to descendant graphics; mask has no independent paint'}
                return node
            if n['name']=='slider':
                tracks=[c for c in n.get('children',[]) if c['name']=='Component/Slider/Track']
                ranges=[c for c in n.get('children',[]) if c['name'].startswith('Component/Slider/Range')]
                if len(tracks)!=1 or len(ranges)!=1:
                    raise ValueError('unrecognized native slider source: '+n['object_id'])
                track,r=tracks[0],ranges[0]
                ranged='Selector' in r['name']
                high=(r['x']+r['w']-r['h']/2-track['x'])/track['w']
                low=(r['x']+r['h']/2-track['x'])/track['w'] if ranged else high
                bg=next(c for c in r['children'] if c['name'].endswith('background'))
                node.update(t='rangeslider' if ranged else 'slider',value=low,
                    color=native_graphics.rgba(bg['fill']),border=0 if r['name'].endswith('filled') else 5,enabled=1)
                if ranged:node['value2']=high
                n['control']=dict(kind='range_slider' if ranged else 'slider',enabled=True,
                    value=[low,high] if ranged else low,state_source='resolved source handle centers / track width')
                def slider_part(c):
                    if c.get('text') or c.get('image'):
                        raise ValueError('slider decoration cannot flatten text or photos')
                    c['control_part_of']=node['id']
                    for child in c.get('children',[]):slider_part(child)
                for c in n.get('children',[]):slider_part(c)
                return node
            if n['cls']=='artboard' and n.get('fill'):
                node['bg']=native_graphics.rgba(n['fill'])
            if (n['name'] in ('Button','Logo Buttons') or n['name'].startswith(('Button/','Buttons/'))
                or n.get('symbol_name','').startswith(('Buttons/','Inputs/Dropdown','Navigation/Tabs/Items/','Navigation/Appbar/Item'))) and n.get('symbol_name'):
                enabled = 'Disable' not in n['symbol_name']
                n['control'] = {'kind':'button','enabled':enabled,'symbol_name':n['symbol_name'],
                                'state_source':'Sketch symbol variant'}
                node.update(variant='button',enabled=int(enabled))
                if native_first:
                    # The container preserves source children; a real Button
                    # supplies focus, enabled state and activation behavior.
                    node.pop('variant')
                    node.pop('enabled')
                    n['control_widget_id']=node['id']+'_button'
            if n['name']=='Component/Toggle/Pill':
                def descendants(c):
                    yield c
                    for d in c.get('children',[]):yield from descendants(d)
                parts=list(descendants(n))
                checked=any(c['name']=='check' for c in parts)
                background=next(c for c in n['children'] if c['name'].endswith('background'))
                color=background['fill'].copy()
                raw_bg=raw_nodes[background['object_id']]
                fill=next(f for f in raw_bg['style']['fills'] if f.get('isEnabled'))
                mode=fill.get('contextSettings',{}).get('blendMode',0)
                if mode:
                    if mode!=7 or not spec.get('fill'):raise ValueError('pill background needs a native blend mapping')
                    backdrop=spec['fill']
                    for layer in spec.get('children',[]):
                        if layer is n:break
                        if (layer.get('cls')=='rectangle' and layer.get('fill') and not layer.get('gradient') and
                            not layer.get('rot') and layer.get('visible',True) and
                            layer['x']<=0 and layer['y']<=0 and layer['w']>=spec['w'] and layer['h']>=spec['h'] and
                            layer['fill'].get('a',1)*layer.get('opacity',1)>=.999):
                            backdrop=layer['fill']
                            n['pill_backdrop_source_id']=layer['object_id']
                    base=backdrop['hex'];tint=color['hex'];alpha=color.get('a',1)
                    rgb=[]
                    for channel in (1,3,5):
                        b=int(base[channel:channel+2],16)/255;t=int(tint[channel:channel+2],16)/255
                        blend=2*b*t if b<.5 else 1-2*(1-b)*(1-t)
                        rgb.append(round((b*(1-alpha)+blend*alpha)*255))
                    color={'hex':'#'+''.join(f'{v:02x}' for v in rgb),'a':1}
                mark=next((c['stroke']['c'] for c in parts if c.get('stroke')),{'hex':'#ffffff','a':1})
                n['control']=dict(kind='checkbox',checked=checked,enabled=True,
                    state_source='Atro pill checkmark presence')
                n['control_widget_id']=node['id']+'_checkbox'
                node['variant']='pill'
                n['pill_style']=dict(bg=native_graphics.rgba(color),mark=native_graphics.rgba(mark))
                def pill_part(c):
                    if c.get('text') or c.get('image'):
                        raise ValueError('pill decoration cannot cover source text or photos')
                    c['control_part_of']=node['id']
                    for child in c.get('children',[]):pill_part(child)
                for c in n.get('children',[]):
                    if not c.get('text'):pill_part(c)
            if n['name'] == 'Radio Button':
                if n.get('symbol_name') != 'Type=Active':
                    raise ValueError('unsupported Sketch radio variant')
                n['control'] = dict(kind='radio',checked=True,enabled=True,
                                    state_source='Sketch active radio variant',symbol_name=n['symbol_name'])
                node.update(variant='radio',on=1)
                if native_first:
                    node.pop('variant');node.pop('on')
                    n['control_widget_id']=node['id']+'_radio'
            variant=taskplan_tab_variant(n)
            if variant is not None:
                # Taskplan uses Default for the filled active tab and Hover /
                # Disable for the other tabs, consistently across the source.
                selected, enabled = 'State=Default' in variant, 'State=Disable' not in variant
                n['control'] = dict(kind='tab',selected=str(selected).lower(),enabled=enabled,
                                    state_source='Taskplan filled tab source variants',symbol_name=variant)
                node.update(variant='button',selected=int(selected),enabled=int(enabled))
                if native_first:
                    # Makepad's Tab is a drawing component, not a Widget. A
                    # native RadioButton owns single-selection behavior while
                    # the source labels/surfaces remain separate children.
                    n['control'].update(kind='radio',checked=selected,semantic_role='tab',
                        adapter='native RadioButton selection; source tab paint and label retained')
                    n['control'].pop('selected')
                    n['control_widget_id']=node['id']+'_radio'
            if n['name'].startswith(('Component/Toggle/Switch-','Component/Checkbox/')):
                checkbox=n['name'].startswith('Component/Checkbox/')
                checked=('Checked' in n['name'] or 'Silent' in n['name']) if checkbox else n['name'].endswith('-ON')
                enabled='Disabled' not in n['name']
                node.update(t='checkbox' if checkbox else 'toggle',on=int(checked),enabled=int(enabled),
                            variant='atro_silent' if n['name'].endswith('/Silent') else 'atro')
                n['control']=dict(kind='checkbox' if checkbox else 'toggle',checked=checked,enabled=enabled,
                                  state_source='Atro named source control variant')
                if checkbox:
                    def decorations(c):
                        yield c
                        for d in c.get('children',[]):yield from decorations(d)
                    candidates=[c for c in decorations(n) if c.get('opacity',1)>.01 and c.get('visible',True)]
                    fill=next((c['fill'] for c in candidates if c.get('fill',{}).get('a',0)>.01),None)
                    stroke=next((c['stroke']['c'] for c in candidates if c.get('stroke')),None)
                    if fill or stroke:node['color']=native_graphics.rgba(fill or stroke)
                    def radii(c):
                        return [c.get('radius',0)]+[r for d in c.get('children',[]) for r in radii(d)]
                    node['radius']=max(radii(n))
                    compound=next((c for c in candidates if c['cls']=='shapeGroup' and c.get('rings')),None)
                    if compound:
                        if 1 in compound.get('ring_ops',[]):node['bordercolor']=0
                        if not node['radius']:
                            # An outlined compound path has no rectangle radius
                            # property; use its outer top-edge tangent instead.
                            points=[p for ring in compound['rings'] for p in ring]
                            top=min(p[1] for p in points)
                            tangents=[p[0] for p in points if abs(p[1]-top)<.00001]
                            if tangents:
                                node['radius']=max(0,min(tangents))*compound['w']
                                n['control']['radius_source']='source outline top-edge tangent'
                def control_part(c):
                    if c.get('text') or c.get('image'):
                        raise ValueError('native binary control cannot flatten text or photos')
                    c['control_part_of']=node['id']
                    for child in c.get('children',[]):control_part(child)
                for c in n.get('children',[]):control_part(c)
            elif n['name'].lower() in ('toogle','toggle') and n.get('symbol_name'):
                knobs = [c for c in n.get('children',[]) if c['cls']=='oval']
                if len(knobs) != 1:
                    raise ValueError('unrecognized toggle knob structure')
                knob = knobs[0]
                checked = knob['x'] + knob['w']/2 > x+w/2
                n['control'] = {'kind':'toggle','checked':checked,
                                'state_source':'resolved Sketch knob position', 'symbol_name':n['symbol_name']}
                node.update(t='toggle',on=int(checked))
                track=next(c for c in n['children'] if c['cls']=='rectangle')
                track_color=native_graphics.rgba(track['fill'])
                node.update(color=track_color if checked else 0xff1e8eba,
                            bg=0xffd2d6db if checked else track_color,
                            bordercolor=native_graphics.rgba(knob['fill']))
                def control_part(c):
                    if c.get('text') or c.get('image'):
                        raise ValueError('a toggle cannot flatten text or images')
                    c['control_part_of'] = node['id']
                    for child in c.get('children',[]): control_part(child)
                for c in n.get('children',[]): control_part(c)
            elif n.get('text'):
                run = n['text']['run']
                raw_text = raw_nodes[n['object_id']]
                attributes = raw_text.get('attributedString', {}).get('attributes', [])
                at = attributes[0]['attributes'] if attributes else {}
                transform=at.get('MSAttributedStringTextTransformAttribute',0)
                if transform in (1,2):
                    n['text']['source_string']=n['text']['string']
                    n['text']['string']=(n['text']['string'].upper() if transform==1 else n['text']['string'].lower())
                paragraph = at.get('paragraphStyle', {})
                n['text']['line_height'] = paragraph.get('maximumLineHeight') or run['size'] * 1.3
                n['text']['runs'] = attributes
                n['text']['source_rows'] = 1
                family = run['font']
                if not family and not n['text']['string'].strip():
                    family='DMSans-Regular' if 'DMSans-Regular' in source_fonts else 'Inter'
                    n['text']['font_resolution']='unnamed whitespace-only source run; no glyph substitution'
                    run['font']=family
                if family in source_fonts and source_fonts[family].get('metrics'):
                    n['text']['font_metrics']=source_fonts[family]['metrics']
                color = run['c']
                node.update(t='text', text=n['text']['string'], size=run['size'], **font_properties(family,source_fonts),
                            line_height=n['text']['line_height'],
                            alignx={0:0, 1:1, 2:.5}.get(run['align'],0),
                            color=(round(color.get('a',1)*255)<<24) | int(color['hex'][1:],16))
                if n.get('rot'):node['rotation']=-n['rot']
                if n.get('source_clip_bounds'):clipped_text_nodes.append((n,node))
                if native_first: styled_nodes.append((n,node))
                if n.get('control', {}).get('kind') == 'text_input':
                    control = n['control']
                    node.update(t='input', text=control['value'], placeholder=control['placeholder'],
                                focused=int(control['focused']), password=int(control['password']), enabled=1)
                    if control.get('multiline'):
                        node['variant'] = 'multiline'
                if len(attributes) > 1:
                    if node['t'] == 'input':
                        raise ValueError('rich text input requires explicit native span support')
                    rich_nodes.append((n,node))
                elif h > n['text']['line_height'] * 1.5:
                    multiline_nodes.append(n)
            elif not n.get('children') or n['cls'] == 'shapeGroup' or n.get('native_vector_overlay'):
                if native_first: native_graphics.active_masks(n,raw_nodes)
                primitive = native_graphics.surface(n,raw_nodes[n['object_id']]) if native_first else None
                if primitive:
                    node.update(primitive)
                    n['rendering'] = {'backend':'native_surface','reason':
                        'native GaussRoundedView backdrop blur and fill blending' if 'glass' in primitive.get('variant','') else
                        'native shape/fill/border properties'}
                    return node
                if native_first:
                    style=raw_nodes[n['object_id']].get('style',{})
                    blends=[style.get('contextSettings',{}).get('blendMode',0)]+[f.get('contextSettings',{}).get('blendMode',0) for f in style.get('fills',[]) if f.get('isEnabled')]
                    if any(blends) and not n.get('native_vector_overlay') and not n.get('backdrop_fallback'):n['backdrop_fallback']='native SVG lacks the source backdrop blend mode '+str(next(b for b in blends if b))
                    elif not n.get('backdrop_fallback') and any(b.get('isEnabled') and b.get('type')==3 for b in style.get('blurs',[])):
                        blurs=[b for b in style['blurs'] if b.get('isEnabled')]
                        if n['cls'] in ('shapeGroup','shapePath') and len(blurs)==1 and not n.get('export_graphic_masks'):
                            n['native_vector_blur']=blurs[0]['radius']
                        else:n['backdrop_fallback']='native GaussRoundedView cannot reproduce this gradient/masked backdrop blur as an isolated surface'
                # Sketch exports each graphic at its own layer bounds. No text
                # or screen image is embedded in the native implementation.
                graphics.append(n['object_id'])
                asset = n['object_id'] + '@2x.png'
                if n['cls'] == 'shapeGroup' or n.get('native_vector_overlay'):
                    # A Boolean shape is one graphic, including its cutouts.
                    # Preserve subpath provenance without inventing individual
                    # widgets for the paths that comprise a logo/icon.
                    n['graphic_asset'] = asset
                    def covered(child):
                        if child.get('text') or child.get('image'):
                            raise ValueError('a compound graphic cannot flatten text or images')
                        child['graphic_part_of'] = n['native_widget_id']
                        for c in child.get('children', []): covered(c)
                    for c in n.get('children', []): covered(c)
                node.update(t='image', src=f"http://127.0.0.1:{kit['img_port']}/{asset}")
                n['graphic_asset'] = asset
                graphic_nodes.append((n, node, asset))
            else:
                children = [visit(c, path + [n.get('object_id') or 'node', str(i)])
                            for i,c in enumerate(n.get('children', []))]
                node['c'] = [c for c in children if c]
                if n.get('control_widget_id','').endswith('_button'):
                    node['c'].append(dict(t='button',id=n['control_widget_id'],x=x,y=y,w=w,h=h,
                        text='',enabled=int(n['control']['enabled'])))
                if n.get('control_widget_id','').endswith('_radio'):
                    node['c'].append(dict(t='radio',variant='camo',id=n['control_widget_id'],
                        x=x,y=y,w=w,h=h,on=int(n['control']['checked']),
                        enabled=int(n['control']['enabled']),color=0,bg=0,bordercolor=0))
                if n.get('control_widget_id','').endswith('_checkbox'):
                    node['c'].insert(0,dict(t='checkbox',variant='atro_pill',id=n['control_widget_id'],
                        x=x,y=y,w=w,h=h,on=int(n['control']['checked']),enabled=1,
                        bg=n['pill_style']['bg'],color=n['pill_style']['mark']))
                if n.get('native_empty_input'):
                    helper = node['id'] + '_input'
                    n['control_widget_id'] = helper
                    camo=n['control'].get('symbol_name','').startswith('Inputs/Code/')
                    input_node=dict(t='input',id=helper,x=x,y=y,w=w,h=h,
                        text='',placeholder='',focused=0,password=0,enabled=1,
                        size=24 if camo else 16,line_height=34 if camo else 26,alignx=.5,color=0xff111927,
                        **font_properties('DMSans-Bold' if camo else 'PlusJakartaSans-SemiBold',source_fonts))
                    if camo:
                        background=int(spec.get('fill',{}).get('hex','#ffffff')[1:],16)
                        dark=sum((background>>s)&255 for s in (16,8,0))<384
                        metrics=source_fonts['DMSans-Bold']['metrics']
                        baseline=24+(34-round(24*(metrics['ascender']-metrics['descender'])))/2
                        input_node.update(color=0xffffffff if dark else 0xff000000,
                            font_asc=baseline/24-metrics['ascender'],
                            font_desc=(baseline-34)/24-metrics['descender'])
                        n['control']['empty_style_source']='source code font metrics and artboard foreground contrast'
                    node['c'].append(input_node)
            return node
        tree = visit(spec, [])
        measured_text = list({n['object_id']:n for n in ([n for n,_ in rich_nodes] + multiline_nodes +
                                                        [n for n,_ in styled_nodes])}.values())
        # The per-glyph text SVGs are export-only inputs to measurement; when
        # every one is already on disk from a prior extraction, re-lowering
        # after an importer change does not need sketchtool to remake them. Skip
        # the export when the cache is complete, and only require the tool when
        # something is genuinely missing.
        text_svgs = {n['object_id']: pathlib.Path(kit['img_dir'])/(n['object_id']+'.svg')
                     for n in measured_text}
        if measured_text and not all(p.is_file() for p in text_svgs.values()):
            if not args.sketchtool:
                missing = [i for i, p in text_svgs.items() if not p.is_file()]
                raise SystemExit('set SKETCHTOOL — measured-text SVGs missing from '
                                 f'cache: {missing[:3]}')
            subprocess.run([args.sketchtool, 'export', 'layers', str(detached),
                            '--items=' + ','.join(n['object_id'] for n in measured_text),
                            '--formats=svg', '--use-id-for-name=YES', '--overwriting=YES',
                            '--output=' + str(kit['img_dir'])], check=True)
        for n in measured_text:
            spans = text_spans(pathlib.Path(kit['img_dir']) / (n['object_id'] + '.svg'),(n['w'],n['h']),n['text']['string'],raw_nodes[n['object_id']]['frame'] if native_first else None)
            if re.sub(r'\s+', ' ', ''.join(s['text'] for s in spans)).strip() != re.sub(r'\s+', ' ', n['text']['string']).strip():
                raise ValueError('Sketch text measurement changed source content')
            n['text']['source_rows'] = text_row_count(spans,
                measured_line_height(spans,n['text']['line_height']))
        for n,node in styled_nodes:
            spans=text_spans(pathlib.Path(kit['img_dir'])/(n['object_id']+'.svg'),(n['w'],n['h']),n['text']['string'],raw_nodes[n['object_id']]['frame'] if native_first else None)
            if node['t']=='text' and node['text'].rstrip('\r\n'):
                # Sketch's exported ink excludes trailing paragraph breaks.
                # Keep those bytes in the source spec, without adding empty
                # native layout rows beyond the measured visible text.
                displayed=node['text'].rstrip('\r\n')
                if displayed!=node['text']:
                    node['text']=displayed
                    n['text']['rendered_string']=displayed
                    n['text']['trailing_breaks']='retained in source; absent from measured Sketch ink'
            if node['t']=='text' and n['text']['source_rows']==1:
                node['variant']='single_line'
            if node['t']=='input' and n['text']['source_rows']>1:
                node['variant']='multiline'
                n['control']['multiline']=True
                n['control']['multiline_source']='measured Sketch text rows'
            if node['t']!='input' and fixed_text_overflows(raw_nodes[n['object_id']],spans):
                if not n.get('source_clip_bounds'):
                    n['source_clip_bounds']=[n[k] for k in ('x','y','w','h')]
                    clipped_text_nodes.append((n,node))
                n['text']['clipping_reason']='fixed-height Sketch text box'
            if len(n['text']['runs'])==1:
                node['line_height']=measured_line_height(spans,node['line_height'])
                n['text']['line_height']=node['line_height']
            if not n['text']['string'].strip() and n['h']>0:
                # Empty keyboard labels have no exported ink or line metrics.
                # Keep their fallback line box inside the measured source frame
                # rather than inventing overflow from the generic 1.3 multiplier.
                node['line_height']=min(node['line_height'],n['h'])
                n['text']['line_height']=node['line_height']
            if '/atro/Montserrat' in node['font_src'] or n['text'].get('font_metrics'):
                baseline=text_baseline(n,spans)
                metrics=n['text'].get('font_metrics',dict(ascender=.968,descender=-.251))
                node.update(font_asc=baseline/node['size']-metrics['ascender'],
                            font_desc=(baseline-node['line_height'])/node['size']-metrics['descender'])
            if n['text']['run']['font']=='AppleColorEmoji':
                apply_emoji_metrics(node,text_baseline(n,spans))
            if spans:
                node.update(tracking=spans[0]['tracking'],
                            color=native_text_color(n,spans[0]))
            spaces=n.get('control',{}).get('leading_spaces',0)
            if spaces:
                from fontTools.ttLib import TTFont
                resource=repository('splash-makepad')/'apps/kit-host/resources'/node['font_src'].split('resources/',1)[1]
                with TTFont(resource) as font:
                    advance=font['hmtx'].metrics[font.getBestCmap()[32]][0]/font['head'].unitsPerEm
                node['padleft']=spaces*(advance*node['size']+node.get('tracking',0))
            n['text']['native_baseline']=text_baseline(n,spans)
            if n.get('native_password_mask'):style_password_mask(n,node,source_fonts)
        for n, node in rich_nodes:
            spans = text_spans(pathlib.Path(kit['img_dir']) / (n['object_id'] + '.svg'),(n['w'],n['h']),n['text']['string'],raw_nodes[n['object_id']]['frame'] if native_first else None)
            if re.sub(r'\s+', ' ', ''.join(s['text'] for s in spans)).strip() != re.sub(r'\s+', ' ', node['text']).strip():
                raise ValueError('Sketch rich text export changed content: ' + n['object_id'])
            if not spans:
                raise ValueError('empty Sketch rich text export')
            first_y = min(s['y'] for s in spans)
            children = []
            for i,s in enumerate(spans):
                child=dict(t='text',variant='single_line',id=node['id']+f'_run_{i}',text=s['text'],
                    x=node['x']+s['x'], y=node['y']+s['y']-first_y,
                    w=max(1,node['w']-s['x']),h=node['line_height'],
                    size=s['size'],line_height=node['line_height'],alignx=0,
                    color=native_text_color(n,s),
                    tracking=s['tracking'],**font_properties(s['font'],source_fonts))
                if native_first and (s['font'].startswith('Montserrat') or source_fonts.get(s['font'],{}).get('metrics')):
                    baseline=text_baseline(n,spans)
                    metrics=source_fonts.get(s['font'],{}).get('metrics',dict(ascender=.968,descender=-.251))
                    child.update(font_asc=baseline/s['size']-metrics['ascender'],
                                 font_desc=(baseline-node['line_height'])/s['size']-metrics['descender'])
                if s['font']=='AppleColorEmoji':
                    apply_emoji_metrics(child,text_baseline(n,spans))
                children.append(child)
            node.update(t='stack',variant='text_runs',c=children)
            n['text']['native_spans'] = spans
        for n,node in clipped_text_nodes:
            content=copy.deepcopy(node);content['id']=node['id']+'_content'
            n['native_text_id']=content['id']
            cx,cy,cw,ch=n['source_clip_bounds']
            clip=dict(t='stack',variant='clip',id=node['id']+'_clip',x=cx,y=cy,w=cw,h=ch,c=[content])
            node.clear();node.update(t='stack',variant='text_runs',id=n['native_widget_id'],
                x=n['x'],y=n['y'],w=n['w'],h=n['h'],text=n['text']['string'],c=[clip])
        for n,node in styled_nodes:
            if not n.get('shadow'):continue
            if node['t']!='text' or n.get('rot') or n.get('source_clip_bounds'):
                raise ValueError('native text shadow needs explicit rotated/clipped support: '+n['object_id'])
            shadow=n['shadow'];pad=math.ceil(shadow['blur']*1.5)
            foreground=copy.deepcopy(node);foreground['id']=node['id']+'_text'
            shade=copy.deepcopy(foreground);shade['id']=node['id']+'_shadow_text'
            shade['x']+=shadow.get('dx',0);shade['y']+=shadow.get('dy',0)
            cached=dict(t='stack',variant='text_shadow',id=node['id']+'_shadow',
                x=shade['x']-pad,y=shade['y']-pad,w=shade['w']+pad*2,h=shade['h']+pad*2,
                blur=shadow['blur'],color=native_graphics.rgba(shadow['c']),c=[shade])
            n['native_text_id']=foreground['id']
            n['text']['native_shadow']={'method':'native Label in CachedView with Gaussian alpha shader',
                'source_shadow':shadow,'widget_id':cached['id']}
            node.clear();node.update(t='stack',variant='text_shadow_label',id=n['native_widget_id'],
                x=n['x'],y=n['y'],w=n['w'],h=n['h'],text=n['text']['string'],c=[cached,foreground])
        if graphics:
            export_graphics(args.sketchtool,detached,unpacked,raw_nodes,
                            [n for n,_,_ in graphic_nodes],pathlib.Path(kit['img_dir']),root,native_first=native_first,
                            backdrop_source=backdrop_source,spec=spec)
        # Overlay is native only when every SVG paint in that graphic is
        # supported. Pattern/conic paints still need source backdrop context;
        # an isolated PNG silently changes their blend into ordinary alpha.
        unsupported_overlays=[]
        for n,_,_ in graphic_nodes:
            if native_first and n.get('native_vector_overlay') and not n.get('backdrop_fallback'):
                path=pathlib.Path(kit['img_dir'])/(n['object_id']+'@2x.svg')
                svg,reason=native_graphics.vector_asset(path,native_overlay=True)
                if svg is None:
                    n['backdrop_fallback']='native Overlay cannot compose this SVG paint: '+reason
                    unsupported_overlays.append(n)
        if unsupported_overlays:
            export_graphics(args.sketchtool,detached,unpacked,raw_nodes,unsupported_overlays,
                pathlib.Path(kit['img_dir']),root,native_first=True,backdrop_source=backdrop_source,spec=spec)
        for g in graphics:
            if not (pathlib.Path(kit['img_dir']) / (g + '@2x.png')).is_file():
                raise ValueError('Sketch did not export graphic ' + g)
        vector_materials={}
        for n, node, asset in graphic_nodes:
            # The layer frame and painted extent differ for rotated paths,
            # outside strokes and shadows. Retain both as inspected widgets.
            iw, ih = Image.open(pathlib.Path(kit['img_dir']) / asset).size
            iw, ih = iw / 2, ih / 2
            px,py,pw,ph = n['paint_bounds']
            if (iw,ih) != (pw,ph):
                raise ValueError('Sketch changed the explicit graphic canvas: ' + asset)
            n['native_paint_id'] = node['id'] + '_paint'
            paint = dict(t='image', id=n['native_paint_id'], x=px,y=py,w=iw,h=ih,src=node['src'])
            if native_first:
                svg_path = pathlib.Path(kit['img_dir'])/(n['object_id']+'@2x.svg')
                svg,reason = native_graphics.vector_asset(svg_path,native_overlay=n.get('native_vector_overlay',False))
                if n.get('backdrop_fallback'):svg,reason=None,n['backdrop_fallback']
                with Image.open(pathlib.Path(kit['img_dir'])/asset) as source_paint:
                    empty_paint=source_paint.convert('RGBA').getchannel('A').getextrema()[1]==0
                if empty_paint:
                    svg=''
                    n['empty_paint_evidence']={'source_png':asset,
                        'sha256':digest(pathlib.Path(kit['img_dir'])/asset),'maximum_alpha':0,'scale':2}
                if svg == '':
                    node.update(t='stack',c=empty_graphic_children(n))
                    node.pop('src',None)
                    n.pop('graphic_asset',None);n.pop('native_paint_id',None)
                    n['rendering']={'backend':'native_surface','reason':
                        'source graphic has zero alpha at reference scale; native layout container only'
                        if empty_paint else 'unpainted source group'}
                    continue
                # A many-subpath fill compound tessellates with visible SEAMS.
                # See raster_to_avoid_seams for the reasoning; kept as a named
                # function so a test can assert the decision without a full
                # Sketch re-import.
                if svg is not None and not n.get('image') and raster_to_avoid_seams(n):
                    subpaths=[c for c in n.get('children',[]) if c.get('cls')=='shapePath']
                    # Keep the exported PNG the paint already points at; do not
                    # write the SVG or reassign src. design.rs emits its Image
                    # branch (premultiplied sampling), which has no seams.
                    n['rendering']={'backend':'bitmap',
                        'reason':f'{len(subpaths)}-subpath fill compound rasterized to avoid '
                                 'native SVG tessellation seams between adjacent glyph fills'}
                    paint.update(image_width=iw*2,image_height=ih*2)
                elif svg is not None and not n.get('image'):
                    svg,gradient_fix=native_graphics.source_linear_gradient(svg,n)
                    svg_path.write_text(svg)
                    asset = svg_path.name
                    n['graphic_asset'] = asset
                    node['src'] = f"http://127.0.0.1:{kit['img_port']}/{asset}"
                    paint.update(t='svg',src=node['src'])
                    n['rendering'] = {'backend':'native_svg','reason':'native tessellated vector geometry'}
                    if gradient_fix:n['rendering']['gradient_normalization']=gradient_fix
                    if n.get('native_vector_blur') or n.get('native_vector_overlay'):
                        paint.update(variant='glass_svg',blur=n.get('native_vector_blur',0),value=int(n.get('native_vector_overlay',False)))
                        if n.get('fill',{}).get('hex') and not n.get('gradient') and not n.get('native_vector_overlay'):
                            vector_materials[paint['id']]={'color':native_graphics.rgba(n['fill']),
                                'coverage':pathlib.Path(kit['img_dir'])/(n['object_id']+'@2x.png')}
                        node['variant']='glass_group'
                        n['rendering']['reason']='native SVG geometry with Gauss backdrop texture'+(' and Overlay blending' if n.get('native_vector_overlay') else '')
                else:
                    n['rendering'] = {'backend':'bitmap','reason':'source photograph/bitmap' if n.get('image') else reason}
            # Actual exported pixel dimensions survive logical coordinate scaling.
            if paint['t']=='image': paint.update(image_width=iw*2,image_height=ih*2)
            node.update(t='stack', c=[paint])
            if paint.get('variant')=='glass_svg':node['variant']='glass_group'
        promote_glass_groups(tree)
        routed=route_fullscreen_glass(tree)
        if routed:spec['fullscreen_glass_foreground']=routed
        foreground=route_glass_foreground(tree)
        if foreground:spec['glass_foreground_routes']=foreground
        glass_materials=compose_glass_materials(tree,vector_materials)
        def record_materials(n):
            if n.get('native_widget_id') in glass_materials:
                n['rendering']['backdrop_material']=glass_materials[n['native_widget_id']]
            elif n.get('native_paint_id') in glass_materials:
                n['rendering']['backdrop_material']=glass_materials[n['native_paint_id']]
            for c in n.get('children',[]):record_materials(c)
        record_materials(spec)
        scale_design(tree,kit['design_scale'])
        for ext in ('png', 'svg'):
            shutil.copyfile(kit['targets_dir']/f"{raw['do_objectID']}@2x.{ext}", kit['targets_dir']/f'{name}.{ext}')
        spec['reference_sha256'] = digest(kit['targets_dir']/f'{name}.png')
        semantic_path=root/'semantics'/f'{name}.json'
        try:
            bindings=(semantic_lowering.lower(spec,tree,json.loads(semantic_path.read_text()),semantic_path.parent)
                      if semantic_path.exists() else [])
        except ValueError as error:
            failure=root/'semantic-failures'/f'{name}.json';failure.parent.mkdir(exist_ok=True)
            failure.write_text(json.dumps({'error':str(error),'source':spec,'generated':tree},indent=2)+'\n')
            raise
        (kit['specs_dir']/f'{name}.json').write_text(json.dumps(spec))
        (kit['cards_dir']/f'{name}.splash').write_text(splash(tree) + '\n')
        (kit['cards_dir']/f'{name}.data.json').write_text(json.dumps({'$kit':{'bindings':bindings}})+'\n')
        outputs=[kit['specs_dir']/f'{name}.json',kit['cards_dir']/f'{name}.splash',
                 kit['cards_dir']/f'{name}.data.json',kit['targets_dir']/f'{name}.png',
                 kit['targets_dir']/f'{name}.svg']
        def assets(n):
            if n.get('graphic_asset'):outputs.append(pathlib.Path(kit['img_dir'])/n['graphic_asset'])
            if n.get('empty_paint_evidence'):
                outputs.append(pathlib.Path(kit['img_dir'])/n['empty_paint_evidence']['source_png'])
            for child in n.get('children',[]):assets(child)
        assets(spec)
        receipt.write_text(json.dumps({'inputs':import_key,'outputs':{str(p):digest(p) for p in outputs}},indent=2)+'\n')
        if name in feedback:
            (kit['cards_dir']/f'{name}.repair-input.json').write_text(json.dumps({
                'prior_findings':feedback[name], 'importer_sha256':digest(__file__),
                'asset_exporter_sha256':digest(pathlib.Path(__file__).with_name('sketch_assets.py')),
                'status':'regenerated; fresh structural and screenshot reviews required'},indent=2)+'\n')
        print(f'{name}: native Sketch reference, {len(graphics)} graphic layers; text retained as widgets', flush=True)


if __name__ == '__main__': main()
