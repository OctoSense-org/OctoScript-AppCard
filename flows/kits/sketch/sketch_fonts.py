"""Use Atro's embedded font files and retain their source hashes."""
import argparse
import fcntl
import hashlib
import json
import pathlib
import re
import shutil
import io
import zipfile
import subprocess

from fontTools.ttLib import TTFont
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[2]))  # flows/, for `core`
from core.native_paths import repository
from core import kitconf


STYLES={300:'Light',400:'Regular',500:'Medium',600:'SemiBold',700:'Bold'}
RESOURCE=repository('splash-makepad')/'apps/kit-host/resources/atro'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bundle(unpacked):
    fonts={}
    for path in sorted((unpacked/'fonts').glob('*')):
        with TTFont(path) as font:
            name=font['name'].getDebugName(6)
            if name not in {'Montserrat-'+s for s in STYLES.values()}:continue
            target=RESOURCE/(name+'.ttf')
            RESOURCE.mkdir(parents=True,exist_ok=True)
            if not target.exists() or sha(path)!=sha(target):shutil.copyfile(path,target)
            fonts[name]={'source':str(path.relative_to(unpacked)), 'sha256':sha(path),
                'version':font['name'].getDebugName(5),'resource':'self:resources/atro/'+target.name}
    if fonts:
        missing={'Montserrat-'+s for s in STYLES.values()}-fonts.keys()
        if missing:raise ValueError('missing embedded Montserrat styles: '+str(sorted(missing)))
        (unpacked.parent/'native-fonts.json').write_text(json.dumps(fonts,indent=2)+'\n')
    return fonts


def bundle_archive(kit):
    """Bundle exact fonts supplied next to the Sketch file, with source receipts.

    Sketch's CLI also needs these installed to export an authentic reference.
    Use a kit-specific user font directory; never replace another kit's files.
    """
    prefix = kit.get('font_archive_prefix')
    if not prefix:
        return {}
    namespace = kit['font_namespace']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', namespace):
        raise ValueError('invalid font namespace')
    resource = RESOURCE.parent/namespace
    installed = pathlib.Path.home()/'Library/Fonts'/('Beauty-'+namespace)
    fonts = {}
    with zipfile.ZipFile(kit['source_archive']) as archive:
        for member in archive.namelist():
            if not member.startswith(prefix) or not member.lower().endswith(('.ttf','.otf')):
                continue
            raw = archive.read(member)
            with TTFont(io.BytesIO(raw)) as font:
                name = font['name'].getDebugName(6)
                if not name or not re.fullmatch(r'[A-Za-z0-9_-]+', name):
                    raise ValueError('unsupported font PostScript name: '+str(name))
                filename = name + pathlib.Path(member).suffix.lower()
                units = font['head'].unitsPerEm
                record = {'source_archive': kit['source_archive'], 'member': member,
                    'sha256': hashlib.sha256(raw).hexdigest(), 'version': font['name'].getDebugName(5),
                    'weight': font['OS/2'].usWeightClass,
                    'metrics': {key: getattr(font['hhea'], field)/units for key, field in
                                (('ascender','ascent'),('descender','descent'),('line_gap','lineGap'))},
                    'resource': f'self:resources/{namespace}/{filename}',
                    'installed': str(installed/filename)}
            if name in fonts and fonts[name]['sha256'] != record['sha256']:
                raise ValueError('conflicting archive font: '+name)
            for directory in (resource, installed):
                directory.mkdir(parents=True, exist_ok=True)
                target = directory/filename
                if not target.exists() or sha(target) != record['sha256']:
                    target.write_bytes(raw)
            fonts[name] = record
    if not fonts:
        raise ValueError('no fonts found at configured archive prefix')
    (kit['specs_dir'].parent/'native-fonts.json').write_text(json.dumps(fonts, indent=2)+'\n')
    return fonts


def installed_fonts(kit):
    """Reference locally installed platform fonts without embedding their files."""
    fonts={}
    for expected, filename in kit.get('font_files',{}).items():
        path=pathlib.Path(filename).expanduser().resolve(strict=True)
        with TTFont(path, fontNumber=0) as font:
            name=font['name'].getDebugName(6)
            if name!=expected:raise ValueError(f'font file is {name}, expected {expected}')
            units=font['head'].unitsPerEm
            fonts[name]={'source_file':str(path),'sha256':sha(path),
                'version':font['name'].getDebugName(5),'weight':font['OS/2'].usWeightClass,
                'metrics':{key:getattr(font['hhea'],field)/units for key,field in
                           (('ascender','ascent'),('descender','descent'),('line_gap','lineGap'))},
                'resource':'file:'+str(path)}
    for alias,name in kit.get('font_aliases',{}).items():
        if name not in fonts:raise ValueError('font alias target must have a verified font_files entry: '+name)
        fonts[alias]=dict(fonts[name],resolved_name=name)
    return fonts


def verify_fonts(fonts):
    paths={name:record.get('installed',record.get('source_file')) for name,record in fonts.items()}
    paths={name:path for name,path in paths.items() if path}
    if not paths:return {}
    script=kitconf.HERE/'sketch_font_preflight.swift'
    args=[item for name,path in sorted(paths.items()) for item in
          (name+'='+fonts[name]['resolved_name'] if fonts[name].get('resolved_name') else name,path)]
    resolved=json.loads(subprocess.check_output(['swift',str(script),*args],text=True))
    return {'registered_fonts':resolved,'preflight_sha256':sha(script)}


def refresh_design(text):
    if 'self:resources/atro/Montserrat.ttf' in text and ' padleft: ' in text:
        raise ValueError('regenerate this design from Sketch: embedded font advances change input padding')
    pattern=r'weight: (300|400|500|600|700) font_src: "self:resources/atro/Montserrat.ttf"'
    updated=re.sub(pattern,lambda m:'weight: '+m[1]+' font_src: "self:resources/atro/Montserrat-'+STYLES[int(m[1])]+'.ttf"',text)
    if 'self:resources/atro/Montserrat.ttf' in updated:
        raise ValueError('unrecognized Montserrat binding; regenerate this design from Sketch')
    return updated


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kit',required=True)
    args=parser.parse_args();kit=kitconf.load(args.kit);root=kit['specs_dir'].parent
    with (root/'.native-import.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        fonts=bundle(root/'resolved')
        if not fonts:raise ValueError('no embedded Atro fonts')
        prepared=[]
        for name in kit['screens']:
            path=kit['cards_dir']/(name+'.splash')
            text=path.read_text();updated=refresh_design(text)
            prepared.append((name,path,text,updated))
        changes=[]
        for name,path,text,updated in prepared:
            before=sha(path)
            if updated!=text:path.write_text(updated)
            changes.append({'screen':name,'before':before,'after':sha(path)})
        (root/'font-repair.json').write_text(json.dumps({'fonts':fonts,'designs':changes},indent=2)+'\n')
        print(f'{len(changes)} designs use the verified embedded Montserrat fonts')


if __name__=='__main__':main()
