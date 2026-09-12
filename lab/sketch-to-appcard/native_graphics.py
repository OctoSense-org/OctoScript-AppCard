"""Prefer native surfaces and SVG geometry; record why a bitmap is necessary."""
import copy
import re
import xml.etree.ElementTree as ET


def rgba(color, opacity=1):
    return (round(color.get('a',1)*opacity*255)<<24) | int(color['hex'][1:],16)


def shadow_backdrop_reason(raw):
    """Overlay shadows change hue/coverage with the underlying scene."""
    for kind in ('shadows','innerShadows'):
        for shadow in raw.get('style',{}).get(kind,[]):
            blend=shadow.get('contextSettings',{}).get('blendMode',0)
            if shadow.get('isEnabled') and blend == 7:
                return f'native SVG shadows cannot sample the backdrop for source shadow blend mode {blend}'
    return None


def surface(node, raw):
    """Simple surfaces are widget properties, not exported pictures."""
    if node['cls'] not in ('rectangle','oval') or node.get('image') or node.get('backdrop_fallback') or node.get('native_vector_overlay'):
        return None
    style = raw.get('style',{})
    if node['cls']=='rectangle' and raw.get('points'):
        # Edited Sketch rectangles can be diamonds or arbitrary paths. Their
        # class name alone is not evidence for a native rectangular surface.
        points=[tuple(float(v) for v in p.get('point','{0,0}').strip('{}').split(',')) for p in raw['points']]
        corners={(0,0),(1,0),(1,1),(0,1)}
        if len(points)!=4 or {tuple(round(v,5) for v in p) for p in points}!=corners:
            return None
    if node.get('rot') or node.get('export_graphic_masks',node.get('graphic_masks')) or node.get('shadow'):
        return None
    if any(x.get('isEnabled') for x in style.get('innerShadows',[])):
        return None
    fills = [x for x in style.get('fills',[]) if x.get('isEnabled')]
    borders = [x for x in style.get('borders',[]) if x.get('isEnabled')]
    if any(b.get('contextSettings',{}).get('blendMode',0) for b in borders):return None
    blurs=[x for x in style.get('blurs',[]) if x.get('isEnabled')]
    blend=fills[0].get('contextSettings',{}).get('blendMode',0) if fills else 0
    if blurs and len(blurs)==1 and blurs[0].get('type')==3 and len(fills)==1 and node.get('fill') and not borders and blend in (0,7):
        return dict(t='stack',variant='glass_overlay' if blend==7 else 'glass_surface',
                    bg=rgba(node['fill']),radius=node.get('radius',min(node['w'],node['h'])/2 if node['cls']=='oval' else 0),
                    blur=blurs[0]['radius'])
    if blurs or blend or style.get('contextSettings',{}).get('blendMode',0):
        return None
    if len(fills)>1 or len(borders)>1 or node.get('gradient'):
        return None
    if borders and (borders[0].get('fillType',0) != 0 or
                    borders[0].get('position',0) != 1 or
                    style.get('borderOptions',{}).get('dashPattern')):
        return None
    radii = {p.get('cornerRadius',0) for p in raw.get('points',[])}
    if len(radii)>1:
        return None
    opacity = node.get('opacity',1)*node.get('ancestor_opacity',1)
    result = dict(t='stack',variant='ellipse' if node['cls']=='oval' else 'surface',
                  bg=rgba(node['fill'],opacity) if node.get('fill') else 0,
                  radius=node.get('radius',0))
    if borders:
        stroke=node['stroke']
        result.update(border=stroke['w'],bordercolor=rgba(stroke['c'],opacity),
                      # Sketch: 0 centered, 1 inside, 2 outside.
                      value=borders[0].get('position',0))
    return result


def active_masks(node, raw_nodes):
    """Omit only outline masks proven not to intersect the element's paint."""
    active=[]; inactive=[]
    padding=node.get('stroke',{}).get('w',0)
    x,y,w,h=(node[k] for k in ('x','y','w','h'))
    x-=padding;y-=padding;w+=2*padding;h+=2*padding
    for mask in node.get('graphic_masks',[]):
        raw=raw_nodes[mask['object_id']]
        radius=max([raw.get('fixedRadius',0),*[p.get('cornerRadius',0) for p in raw.get('points',[])]])
        mx,my,mw,mh=(mask[k] for k in ('x','y','w','h'))
        contains=(x>=mx and y>=my and x+w<=mx+mw and y+h<=my+mh and
                  ((x>=mx+radius and x+w<=mx+mw-radius) or
                   (y>=my+radius and y+h<=my+mh-radius)))
        safe=(raw['_class']=='rectangle' and not raw.get('rotation') and not mask.get('rot') and
              raw.get('clippingMaskMode',0)==0 and not node.get('rot') and
              not node.get('shadow') and contains)
        (inactive if safe else active).append(mask)
    node['export_graphic_masks']=active
    node['nonintersecting_graphic_masks']=inactive


def source_linear_gradient(svg, source):
    """Reconstruct Sketch's point-space gradient in SVG gradient space.

    Sketch's SVG export can compress a non-square layer's gradient endpoints;
    its PNG and original gradient definition agree on point-space projection.
    Keep native SVG rendering standards-correct and normalize the source here.
    """
    gradient=source.get('gradient',{})
    if gradient.get('type')!=0 or source.get('w',0)<=0 or source.get('h',0)<=0:
        return svg,None
    root=ET.fromstring(svg)
    local=lambda e:e.tag.rsplit('}',1)[-1]
    colors=[s['c']['hex'].lower() for s in gradient['stops']]
    candidates=[e for e in root.iter() if local(e)=='linearGradient'
        and e.get('gradientUnits','objectBoundingBox')=='objectBoundingBox'
        and not e.get('gradientTransform')
        and [s.get('stop-color','').lower() for s in e if local(s)=='stop']==colors]
    if len(candidates)!=1:return svg,None
    g=candidates[0]
    uses=[e for e in root.iter() if e.get('fill')=='url(#'+g.get('id','')+')']
    if len(uses)!=1:return svg,None
    x,y=gradient['from'];end_x,end_y=gradient['to']
    dx,dy=end_x-x,end_y-y;w,h=source['w'],source['h']
    length2=(w*dx)**2+(h*dy)**2
    nx,ny=w*w*dx,h*h*dy;normal2=nx*nx+ny*ny
    if normal2<1e-12:return svg,None
    before={k:g.get(k) for k in ('x1','y1','x2','y2')}
    coords=dict(x1=x,y1=y,x2=x+nx*length2/normal2,y2=y+ny*length2/normal2)
    for k,v in coords.items():g.set(k,str(v))
    return ET.tostring(root,encoding='unicode'),dict(method='Sketch point-space linear gradient',
        exported_endpoints=before,native_endpoints=coords)


def overlay_graphic(raw):
    """A graphic-only Overlay blend can use native SVG backdrop sampling."""
    def graphics_only(n):
        return n.get('_class') not in ('text','bitmap','symbolInstance') and not any(
            f.get('isEnabled') and f.get('fillType')==4 for f in n.get('style',{}).get('fills',[])) and all(
            graphics_only(c) for c in n.get('layers',[]))
    if not graphics_only(raw):return False
    style=raw.get('style',{})
    if style.get('contextSettings',{}).get('blendMode')==7:return True
    paints=[p for key in ('fills','borders') for p in style.get(key,[]) if p.get('isEnabled')]
    return bool(paints) and all(p.get('contextSettings',{}).get('blendMode')==7 for p in paints)


def vector_asset(path, native_overlay=False):
    """Normalize Sketch's local <use> references for native Makepad SVG.

    Unsupported SVG features cannot silently disappear in the native parser.
    This returns a fallback reason rather than claiming their SVG was rendered.
    """
    root=ET.parse(path).getroot()
    local=lambda e:e.tag.rsplit('}',1)[-1]
    for e in root.iter():
        blend=re.search(r'(?:^|;)\s*mix-blend-mode\s*:\s*([^;]+)',e.get('style',''))
        if blend and blend[1].strip()!='normal':
            if native_overlay and blend[1].strip()=='overlay':
                e.set('style',re.sub(r'(?:^|;)\s*mix-blend-mode\s*:[^;]+','',e.get('style','')))
            else:return None,'native SVG lacks backdrop blend mode: '+blend[1].strip()
        if local(e) in ('linearGradient','radialGradient') and e.get('gradientUnits')=='userSpaceOnUse':
            if any('%' in e.get(k,'') for k in ('x1','y1','x2','y2','cx','cy','r','fx','fy')):
                return None,'native SVG lacks viewport-relative user-space gradient percentages'
    references={m for e in root.iter() for v in e.attrib.values() for m in re.findall(r'url\(#([^)]*)\)',v)}
    for parent in root.iter():
        for child in list(parent):
            if local(child)=='mask' and child.get('id') not in references:
                parent.remove(child)
    # Sketch's common outer-shadow filter is representable by Makepad's native
    # DropShadow effect. Keep the exact blur, offset, color and alpha.
    for f in root.iter():
        if local(f)!='filter':continue
        children=list(f);tags=[local(e) for e in children]
        if tags==['feOffset','feGaussianBlur','feColorMatrix']:
            offset,blur,color=children
            values=[float(v) for v in color.get('values','').split()]
            if len(values)!=20 or any(values[i] for i in (0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,19)):
                continue
            effect=ET.Element('feDropShadow',{'dx':offset.get('dx','0'),'dy':offset.get('dy','0'),
                'stdDeviation':blur.get('stdDeviation','0'),
                'flood-color':'#'+''.join(f'{round(values[i]*255):02x}' for i in (4,9,14)),
                'flood-opacity':str(values[18])})
            for child in children:f.remove(child)
            f.append(effect)
    ids={e.get('id'):e for e in root.iter() if e.get('id')}
    def expand(parent, seen=()):
        for index,child in enumerate(list(parent)):
            if local(child)=='use':
                href=child.get('{http://www.w3.org/1999/xlink}href',child.get('href',''))
                if not href.startswith('#') or href[1:] not in ids or href in seen:
                    raise ValueError('unresolved SVG reference')
                group=ET.Element('g', {k:v for k,v in child.attrib.items()
                    if k not in ('href','{http://www.w3.org/1999/xlink}href','x','y')})
                if child.get('x') or child.get('y'):
                    group.set('transform',f"translate({child.get('x','0')} {child.get('y','0')}) "
                              + group.get('transform',''))
                group.append(copy.deepcopy(ids[href[1:]]))
                parent.remove(child);parent.insert(index,group)
                expand(group,seen+(href,))
            else:
                expand(child,seen)
    try:
        expand(root)
    except ValueError as error:
        return None,str(error)
    # Native SVG renders shape filters, but has no offscreen group filtering.
    # A group with one painted shape can transfer its filter without changing
    # the effect. Multiple shapes require an explicit bitmap fallback.
    geometry={'path','rect','ellipse','circle','line','polyline','polygon'}
    for group in root.iter():
        if local(group)=='g' and group.get('filter'):
            shapes=[e for e in group.iter() if local(e) in geometry]
            if len(shapes)!=1 or shapes[0].get('filter'):
                return None,'native SVG lacks filtering of a group containing multiple shapes'
            shapes[0].set('filter',group.attrib.pop('filter'))
    if any(local(e) in ('path','polygon','polyline') and e.get('filter') for e in root.iter()):
        return None,'native SVG cannot match Gaussian shadows on arbitrary compound paths'
    allowed={'svg','g','defs','path','rect','ellipse','circle','line','polyline','polygon',
             'linearGradient','radialGradient','stop','title','desc','filter','feDropShadow'}
    unsupported=sorted({local(e) for e in root.iter()}-allowed)
    if unsupported:
        return None,'native SVG does not support: '+', '.join(unsupported)
    if not any(local(e) in ('path','rect','ellipse','circle','line','polyline','polygon') for e in root.iter()):
        return '',None  # An unpainted source group: retain a native View only.
    if any(e.get(k) for e in root.iter() for k in ('clip-path','mask')):
        return None,'native SVG does not implement this clipping/mask'
    # Unused shape definitions need not be drawn; every use is now expanded.
    for parent in root.iter():
        if local(parent)=='defs':
            for child in list(parent):
                if local(child) not in ('linearGradient','radialGradient','filter'):
                    parent.remove(child)
    for parent in list(root.iter()):
        for child in list(parent):
            if local(child)=='path' and not child.get('d','').strip():
                parent.remove(child)
    if not any(local(e) in geometry for e in root.iter()):
        return '',None
    def has_paint(element, inherited=None):
        # Mask outlines can survive export as geometry with fill/stroke both
        # disabled. They have layout, but no native SVG draw area to inspect.
        paint=dict(inherited or {'fill':'black','stroke':'none','stroke-width':'1'})
        paint.update({k:v for k,v in element.attrib.items()
                      if k in ('fill','stroke','stroke-width')})
        for declaration in element.get('style','').split(';'):
            key,sep,value=declaration.partition(':')
            if sep and key.strip() in paint:paint[key.strip()]=value.strip()
        if local(element) in geometry and (paint['fill']!='none' or
                (paint['stroke']!='none' and paint['stroke-width'] not in ('0','0px'))):
            return True
        return any(has_paint(child,paint) for child in element
                   if local(child) not in ('defs','filter'))
    if not has_paint(root):
        return '',None
    for element in root.iter():
        element.tag=local(element)
    return ET.tostring(root,encoding='unicode'),None
