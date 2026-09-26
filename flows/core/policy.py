"""One semantic policy and data/artwork validation implementation for both branches."""
import hashlib,json,math
import xml.etree.ElementTree as ET
from pathlib import Path

POLICY_PATH=Path(__file__).resolve().parents[1]/'image-to-appcard/mapping-rules.json'
POLICY=json.loads(POLICY_PATH.read_text())

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())

def numeric(value):
    return type(value) in (int, float) and math.isfinite(value)


def local_asset(directory, relative):
    if not isinstance(relative, str) or not relative:
        return None
    if Path(relative).is_absolute():
        return None
    root = Path(directory).resolve()
    path = (root / relative).resolve()
    return path if path.is_relative_to(root) and path.is_file() else None


def runtime_data_issues(directory,entry,runtime):
    """Inspect numerical values as well as the hash the binding reports."""
    data=entry.get('data',{});errors=data_issues(directory,entry)
    if runtime.get('data_sha256')!=data.get('sha256'):
        errors.append('inspected chart data does not match the declared series')
    path=local_asset(directory,data.get('path'))
    if errors or not path:return errors
    rows=read(path);x=[r[data['x_key']] for r in rows]
    if entry['role']=='chart.bar' or (entry['role']=='waveform' and entry.get('plot',{}).get('mode')=='intervals'):
        expected=[{k:r[k] for k in ('x','low','high','width')} for r in rows]
        if runtime.get('intervals')!=expected:
            errors.append('native bar intervals differ from numeric asset')
    elif entry['role']=='chart.scatter':
        if runtime.get('points')!=[{k:r[k] for k in ('x','y','radius')} for r in rows]:
            errors.append('native bubble coordinates or radii differ from numeric asset')
    elif entry['role']=='chart.donut':
        if runtime.get('values')!=[r[data['y_keys'][0]] for r in rows]:
            errors.append('native slice values differ from numeric asset')
    else:
        expected=[]
        for key in data['y_keys']:
            if entry.get('plot',{}).get('mode')=='waveform':
                expected.extend({'x':[r[data['x_key']],r[data['x_key']]],'y':[-r[key],r[key]]} for r in rows)
            else:expected.append({'x':x,'y':[r[key] for r in rows]})
        if runtime.get('series',[])[:len(expected)]!=expected:
            errors.append('actual native series differ from numeric asset')
    return errors


def data_issues(directory, entry):
    data = entry.get('data', {})
    path = local_asset(directory, data.get('path'))
    errors = []
    if data.get('origin') not in ('fixture', 'measured_image', 'measured_sketch', 'live_snapshot'):
        errors.append('declare data origin: fixture, measured_image, measured_sketch or live_snapshot')
    if not path or data.get('sha256') != sha(path):
        errors.append('missing or stale numeric data asset')
        return errors
    try:
        points = read(path)
    except (ValueError, OSError):
        return errors + ['numeric data asset must be valid JSON']
    keys = [data.get('x_key')] + data.get('y_keys', [])
    if len(keys) < 2 or not all(isinstance(k, str) and k for k in keys):
        errors.append('declare x_key and y_keys for the numeric series')
    elif not isinstance(points, list) or len(points) < 2 or any(
        not isinstance(p, dict) or any(not numeric(p.get(k)) for k in keys) for p in points
    ):
        errors.append('series must contain at least two finite numeric samples')
    if not all(data.get('units', {}).get(k) for k in ('x', 'y')):
        errors.append('declare axis units, including normalized or category-index units')
    for axis in ('x', 'y'):
        domain = data.get('domain', {}).get(axis)
        if not isinstance(domain, list) or len(domain) != 2 or not all(map(numeric, domain)) or domain[0] >= domain[1]:
            errors.append('declare a finite increasing ' + axis + ' domain')
    if data.get('origin') in ('measured_image','measured_sketch') and data.get('approximate') is not True:
        origin='image' if data['origin']=='measured_image' else 'Sketch'
        errors.append(origin+'-recovered values must be labeled approximate')
    return errors


def asset_issues(directory, entry, manifest, reference_dir=None):
    asset = entry.get('asset', {})
    path = local_asset(directory, asset.get('path'))
    errors = []
    method = asset.get('method')
    if method not in ('reference_svg', 'source_crop', 'original_asset', 'kit_asset', 'generated_asset'):
        errors.append('missing artwork strategy/provenance; generic SVG replacement is unverified')
    if not path or asset.get('sha256') != sha(path):
        errors.append('missing or stale artwork asset')
    if path and method == 'reference_svg' and path.suffix.lower() != '.svg':
        errors.append('reference_svg strategy requires an SVG file')
    if path and path.suffix.lower() == '.svg':
        try:
            elements = ET.fromstring(path.read_text()).iter()
            if any(e.tag.split('}')[-1] in ('image', 'text', 'foreignObject') for e in elements):
                errors.append('SVG artwork may not embed raster UI or UI text')
        except ET.ParseError:
            errors.append('invalid SVG artwork')
    if method in ('reference_svg', 'source_crop'):
        if asset.get('reference_sha256') != manifest['reference_sha256']:
            errors.append('artwork provenance points to a different reference')
    if entry.get('role')=='icon' and method=='source_crop' and not asset.get('fallback_reason'):
        errors.append('raster icon requires a recorded vector-renderer limitation')
    if method == 'source_crop':
        from PIL import Image
        if path and path.suffix.lower() not in ('.png', '.webp'):
            return errors + ['source crops require lossless PNG or WebP assets']
        bounds = asset.get('crop_pixels')
        reference_path = (reference_dir or directory) / 'reference.png'
        with Image.open(reference_path) as reference:
            width, height = reference.size
        valid = isinstance(bounds, list) and len(bounds) == 4 and all(type(v) is int for v in bounds)
        if valid:
            x, y, w, h = bounds
            valid = x >= 0 and y >= 0 and w > 0 and h > 0 and x+w <= width and y+h <= height
        if not valid:
            errors.append('invalid crop_pixels: use [x,y,width,height] in original pixels')
        else:
            if w == width and h == height:
                errors.append('a full-screen screenshot cannot be an illustration asset')
            if path:
                with Image.open(reference_path) as reference:
                    expected = reference.convert('RGBA').crop((x, y, x+w, y+h))
                with Image.open(path) as original:
                    actual = original.convert('RGBA')
                if expected.size != actual.size or expected.tobytes() != actual.tobytes():
                    errors.append('crop pixels do not match the original artwork region')
        if asset.get('contains_ui') is not False:
            errors.append('crop must be reviewed as artwork only, without UI text or controls')
    if method in ('kit_asset', 'original_asset', 'generated_asset') and not asset.get('source'):
        errors.append('record asset source or generation receipt')
    if asset.get('fit') not in ('contain', 'cover', 'stretch') or not isinstance(asset.get('clip'), bool):
        errors.append('declare asset fit and clipping')
    return errors
