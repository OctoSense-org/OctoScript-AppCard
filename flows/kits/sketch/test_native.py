"""Regression checks for native Sketch import and Studio interaction failures."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[2]))  # flows/, for `core`
import io
import json
import pathlib
import queue
import tempfile
import unittest
import zipfile
from types import SimpleNamespace
from unittest.mock import patch

from core import render_splash_makepad as native
import sketch_native
from sketch_native import artboard_names


class NativePipelineTests(unittest.TestCase):
    def test_sketch_row_count_preserves_blank_paragraph_lines(self):
        spans=[dict(y=y,size=20) for y in (19,47,103,131)]
        self.assertEqual(sketch_native.text_row_count(spans,28),5)
        spans.insert(1,dict(y=22,size=20))
        self.assertEqual(sketch_native.text_row_count(spans,28),5)
        self.assertEqual(sketch_native.text_row_count([],28),0)

    def test_cached_fingerprint_detects_same_size_edit_and_file_replacement(self):
        with tempfile.TemporaryDirectory() as td:
            source=pathlib.Path(td)/'asset'
            source.write_bytes(b'first')
            initial=native.fingerprint([source])
            self.assertEqual(native.fingerprint([source]),initial)
            source.write_bytes(b'other')
            changed=native.fingerprint([source])
            self.assertNotEqual(changed,initial)
            replacement=source.with_suffix('.replacement')
            replacement.write_bytes(b'final')
            replacement.replace(source)
            self.assertNotEqual(native.fingerprint([source]),changed)

    def test_atro_input_masks_preserve_spacing_and_focus_provenance(self):
        def control(text,variant):
            field={'name':'value','text':{'string':text}}
            sketch_native.annotate_inputs({'name':'Textfield/Input','symbol_name':variant,'children':[field]})
            return field['control']
        masked=control('      •••••','Forms/Textfield/List-Input')
        self.assertEqual(masked['value'],'•••••')
        self.assertTrue(masked['password'])
        self.assertEqual(masked['leading_spaces'],6)
        self.assertTrue(control('maria@email.com','Forms/Textfield/Input:Focus')['focused'])
        placeholder=control('Your password','Forms/Textfield/Input-Dark')
        self.assertEqual(placeholder['value'],'')
        self.assertTrue(placeholder['password'])

    def test_many_subpath_fill_compound_rasters_to_avoid_svg_seams(self):
        # A 9-glyph wordmark rasters (native SVG tessellation cracks the stems,
        # scored 7/10 rework); a 1-2 path icon keeps its SVG; gradient/blur/
        # overlay compounds keep SVG because the raster cannot reproduce them.
        many=lambda k: {'cls':'shapeGroup','children':[{'cls':'shapePath'} for _ in range(k)]}
        self.assertTrue(sketch_native.raster_to_avoid_seams(many(9)))
        self.assertFalse(sketch_native.raster_to_avoid_seams(many(2)))
        self.assertFalse(sketch_native.raster_to_avoid_seams({**many(6),'gradient':{'x':1}}))
        self.assertFalse(sketch_native.raster_to_avoid_seams({**many(6),'native_vector_blur':2}))
        self.assertFalse(sketch_native.raster_to_avoid_seams({**many(6),'native_vector_overlay':True}))

    def test_graphic_mask_chain_respects_groups_and_breaks(self):
        def node(id, **extra):return dict(object_id=id,x=0,y=0,w=20,h=20,**extra)
        root=node('root',children=[node('mask',mask=True),node('group',children=[node('image')]),
                                  node('break'),node('last')])
        raw={k:{} for k in ('root','mask','group','image','last')}
        raw['break']={'shouldBreakMaskChain':True}
        sketch_native.annotate_graphic_masks(root,raw)
        self.assertEqual(root['children'][1]['children'][0]['graphic_masks'][0]['object_id'],'mask')
        self.assertEqual(root['children'][2]['graphic_masks'],[])
        self.assertEqual(root['children'][3]['graphic_masks'],[])

    def test_input_variants_preserve_source_and_require_native_state(self):
        def field(variant, text, label='Email', name='Text Input'):
            leaf = {'name':'Text','text':{'string':text}}
            group = {'name':name,'symbol_name':variant,'children':[
                {'name':'Label','text':{'string':label}},leaf]}
            sketch_native.annotate_inputs(group)
            self.assertEqual(leaf['text']['string'],text)
            return leaf['control']
        empty = field('input=Default','Enter email')
        self.assertEqual((empty['value'],empty['placeholder'],empty['focused']),('', 'Enter email',False))
        focused = field('input=Focused','example@gmai|')
        self.assertEqual((focused['value'],focused['display_text'],focused['focused']),('example@gmai','example@gmai',True))
        self.assertTrue(field('input=filled','••••','Password')['password'])
        shown=field('Type=Filled','Examplepass1232','Password')
        self.assertTrue(shown['password_field'])
        self.assertFalse(shown['password'])
        search = field('Search','Sell |',name='Search')
        self.assertEqual((search['value'],search['focused']),('Sell ',True))
        self.assertEqual(field('Search','Search member',name='Search')['value'],'')
        self.assertTrue(field('Type=Filled','long description',name='Text Area')['multiline'])
        with self.assertRaisesRegex(ValueError,'provenance'):
            sketch_native.annotate_inputs({'name':'Text Input'})

    def test_blank_gpu_frame_fails_but_flat_source_is_valid(self):
        from PIL import Image, ImageDraw
        with tempfile.TemporaryDirectory() as td:
            target,capture = pathlib.Path(td)/'target.png',pathlib.Path(td)/'capture.png'
            image = Image.new('RGBA',(100,100),'white')
            ImageDraw.Draw(image).rectangle((10,10,80,80),fill='blue')
            image.save(target)
            Image.new('RGBA',(100,100),(0,0,0,0)).save(capture)
            self.assertFalse(native.frame_has_content(target,capture))
            Image.new('RGBA',(100,100),'white').save(capture)
            self.assertFalse(native.frame_has_content(target,capture))
            image.save(capture)
            self.assertTrue(native.frame_has_content(target,capture))
            Image.new('RGBA',(100,100),'white').save(target)
            Image.new('RGBA',(100,100),'white').save(capture)
            self.assertTrue(native.frame_has_content(target,capture))

    def test_source_cache_requires_archive_tool_and_detached_hashes(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)/'work'
            root.mkdir()
            archive = pathlib.Path(td)/'purchase.zip'
            def pack(content):
                document = io.BytesIO()
                with zipfile.ZipFile(document,'w') as z:
                    z.writestr('document.json',content)
                with zipfile.ZipFile(archive,'w') as z:
                    z.writestr('kit.sketch',document.getvalue())
            pack('first source')
            with patch.object(sketch_native.subprocess,'check_output',return_value='Sketch test'), \
                 patch.object(sketch_native.subprocess,'run') as detach:
                sketch_native.source_documents(root,archive,'sketchtool')
                self.assertEqual(detach.call_count,1)
                (root/'resolved/document.json').write_text('tampered extraction')
                sketch_native.source_documents(root,archive,'sketchtool')
                self.assertEqual(detach.call_count,1)
                self.assertEqual((root/'resolved/document.json').read_text(),'first source')
                (root/'resolved.sketch').write_bytes(b'corrupt detached document')
                sketch_native.source_documents(root,archive,'sketchtool')
                self.assertEqual(detach.call_count,2)
                pack('changed source')
                sketch_native.source_documents(root,archive,'sketchtool')
                self.assertEqual(detach.call_count,3)
                self.assertEqual((root/'resolved/document.json').read_text(),'changed source')
                sketch_native.source_documents(root,archive,'sketchtool',font_inputs={'DMSans-Regular':'v1'})
                self.assertEqual(detach.call_count,4)
                sketch_native.source_documents(root,archive,'sketchtool',font_inputs={'DMSans-Regular':'v1'})
                self.assertEqual(detach.call_count,4)
                sketch_native.source_documents(root,archive,'sketchtool',font_inputs={'DMSans-Regular':'v2'})
                self.assertEqual(detach.call_count,5)

    def test_same_named_artboards_keep_distinct_stable_artifacts(self):
        boards = [{'object_id':'aaaaaaaa-1','name':'Edit Profile'},
                  {'object_id':'bbbbbbbb-2','name':'Edit Profile'},
                  {'object_id':'cccccccc-3','name':'Login'}]
        names = artboard_names(boards)
        self.assertEqual(len(set(names.values())), 3)
        self.assertEqual(names, artboard_names(reversed(boards)))
        self.assertEqual(names['cccccccc-3'], 'Login')

    def test_bridge_parse_errors_are_reported_instead_of_discarded(self):
        bridge = native.Bridge.__new__(native.Bridge)
        bridge.log = io.StringIO()
        bridge.q = queue.Queue()
        bridge.p = SimpleNamespace(stdout=io.StringIO(
            'studio remote: invalid request json: expected signed integer\n'))
        bridge._read()
        with self.assertRaisesRegex(RuntimeError, 'expected signed integer'):
            bridge.wait('WidgetSnapshot', timeout=1)

    def test_runtime_shader_error_cannot_be_followed_by_successful_capture(self):
        bridge = native.Bridge.__new__(native.Bridge)
        bridge.q = queue.Queue()
        bridge.q.put({'QueryLogResults':{'entries':[[1,{'level':{'Log':[]},
            'message':'[E] shader type error'}]]}})
        bridge.q.put({'Screenshot':{'path':'incorrect.png'}})
        with self.assertRaisesRegex(RuntimeError,'shader type error'):
            bridge.wait('Screenshot',timeout=1)

    def test_embedded_frame_recovers_from_studio_initial_tab_resize(self):
        from unittest.mock import Mock, patch
        bridge=Mock()
        bridge.wait.side_effect=[{'width':796,'height':1200},{'width':750,'height':1624}]
        with patch.object(native.time,'sleep'):
            native.ensure_embedded_frame(bridge,[28],375,812)
        self.assertIn((('RunViewResize',{'build_id':[28],'window_id':0,
            'width':375,'height':812,'dpi':2.0}),),bridge.send.call_args_list)

    def test_screenshot_cleanup_preserves_evidence_and_failed_copy_source(self):
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td)
            hub=root/'makepad_studio_hub'
            hub.mkdir()
            source=hub/'build-29-kind-0-req-1.png'
            source.write_bytes(b'captured image')
            with patch.object(native.tempfile,'gettempdir',return_value=td):
                with self.assertRaises(FileNotFoundError):
                    native.save_screenshot({'path':str(source)},root/'missing'/'output.png')
                self.assertTrue(source.exists())
                output=root/'output.png'
                native.save_screenshot({'path':str(source)},output)
                self.assertEqual(output.read_bytes(),b'captured image')
                self.assertFalse(source.exists())
                native.release_screenshot({'path':str(output)})
                self.assertTrue(output.exists())

    def test_embedded_frame_rejects_persistently_wrong_dimensions(self):
        from unittest.mock import Mock, patch
        bridge=Mock()
        bridge.wait.return_value={'width':796,'height':1200}
        with patch.object(native.time,'sleep'),self.assertRaisesRegex(RuntimeError,'did not settle'):
            native.ensure_embedded_frame(bridge,[28],375,812)

    def test_graphic_only_splashscreen_is_not_rejected_as_empty(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            result = {'ok':True,'nodes':2,'texts':[],
                      'elements':[{'id':'root'},{'id':'logo'}]}
            with patch.object(native,'selected_inputs',return_value=(root/'a',root/'b',root/'c')), \
                 patch.object(native.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=json.dumps(result))):
                self.assertEqual(native.validate({'splash_makepad_dir':root},'splash'),result)

    def test_toggle_uses_integer_local_coordinates_and_verifies_restore(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root/'screen.layout.json').write_text(json.dumps({'elements':[
                {'id':'toggle','bounds':[325,642,44,24]}]}))
            (root/'shot.png').write_bytes(b'example PNG fixture')
            states = iter([False,True])
            sent = []
            def send(kind,value):
                if kind=='Click':
                    self.assertIs(type(value['x']),int)
                    self.assertIs(type(value['y']),int)
                    sent.append((value['x'],value['y']))
            def wait(kind):
                if kind=='WidgetSnapshot':
                    return {'widgets':[{'id':'toggle','checked':next(states)}]}
                return {'path':str(root/'shot.png')}
            with patch.object(native.time,'sleep'):
                files = native.check_toggles(SimpleNamespace(send=send,wait=wait),[1],'screen',
                    {'elements':[{'kind':'Toggle','id':'toggle','original_id':'sketch_x','on':1}]},
                    {'widgets':[{'id':'toggle','x':405,'y':722,'width':44,'height':24}]},root)
            self.assertEqual(sent,[(347,654),(347,654)])
            self.assertEqual(len(files),3)
            self.assertEqual([s['widget']['checked'] for s in json.loads(files[0].read_text())['checks'][0]['states']], [False,True])


if __name__ == '__main__':
    unittest.main()
