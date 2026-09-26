"""Inject composition failures that visually convincing screenshots can hide."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import copy
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

from core import acceptance
from core import gate_composition
from core import repair_feedback
from core import gallery


def fixture():
    photo = {'cls': 'bitmap', 'object_id': 'photo', 'name': 'hero',
             'x': 0, 'y': 0, 'w': 375, 'h': 812, 'image': 'images/photo.png',
             'native_widget_id': 'photo', 'native_paint_id': 'photo_paint',
             'graphic_asset': 'photo.png',
             'rendering': {'backend': 'bitmap', 'reason': 'source photograph/bitmap'}}
    label = {'cls': 'text', 'object_id': 'label', 'name': 'title',
             'x': 20, 'y': 20, 'w': 100, 'h': 30, 'native_widget_id': 'label',
             'text': {'string': 'Welcome'}}
    button = {'cls': 'group', 'object_id': 'button', 'name': 'continue',
              'x': 20, 'y': 100, 'w': 100, 'h': 40, 'native_widget_id': 'button',
              'control_widget_id': 'button_hit', 'control': {'kind': 'button'}}
    spec = {'cls': 'artboard', 'object_id': 'screen', 'w': 375, 'h': 812,
            'native_widgets_first': True, 'children': [photo, label, button]}
    portable = {'elements': [
        {'id': 'p', 'original_id': 'photo_paint', 'kind': 'Image', 'image': 'http://localhost/photo.png'},
        {'id': 't', 'original_id': 'label', 'kind': 'Text'},
        {'id': 'b', 'original_id': 'button_hit', 'kind': 'Button'}]}
    return spec, portable


class CompositionTests(unittest.TestCase):
    def test_full_bleed_source_photo_with_native_text_and_control_is_valid(self):
        result = gate_composition.compare(*fixture())
        self.assertTrue(result['pass'], result)
        self.assertEqual(result['asset_counts'], {'source_bitmap': 1})

    def test_unowned_paint_and_backend_lies_fail(self):
        for mutation in ('unowned', 'wrong_backend', 'wrong_asset', 'missing_reason', 'false_photo'):
            with self.subTest(mutation=mutation):
                spec, portable = fixture()
                photo = spec['children'][0]
                if mutation == 'unowned': portable['elements'][0]['original_id'] = 'screenshot'
                elif mutation == 'wrong_backend': photo['rendering']['backend'] = 'native_surface'
                elif mutation == 'wrong_asset': portable['elements'][0]['image'] = 'whole-screen.png'
                elif mutation == 'missing_reason': photo['rendering']['reason'] = ' '
                else: del photo['image']
                self.assertFalse(gate_composition.compare(spec, portable)['pass'])

    def test_native_svg_still_cannot_flatten_source_text(self):
        spec, portable = fixture()
        photo = spec['children'][0]
        photo['rendering'] = {'backend': 'native_svg', 'reason': 'vector geometry'}
        portable['elements'][0]['kind'] = 'Svg'
        photo['children'] = [copy.deepcopy(spec['children'][1])]
        result = gate_composition.compare(spec, portable)
        self.assertFalse(result['pass'])
        self.assertTrue(any('contains source text' in d['issue'] for d in result['element_differences']))

    def test_artboard_screenshot_and_backdrop_text_are_rejected(self):
        for defect in ('artboard', 'backdrop'):
            spec, portable = fixture()
            if defect == 'artboard': spec['children'][0]['cls'] = 'artboard'
            else: spec['children'][0]['backdrop_context'] = {'text_in_paint_region': ['label']}
            self.assertFalse(gate_composition.compare(spec, portable)['pass'])

    def test_text_and_controls_cannot_be_replaced_by_empty_containers(self):
        for index in (1, 2):
            spec, portable = fixture()
            portable['elements'][index]['kind'] = 'Stack'
            self.assertFalse(gate_composition.compare(spec, portable)['pass'])

    def test_rich_text_requires_descendant_labels(self):
        spec, portable = fixture()
        portable['elements'][1]['kind'] = 'Stack'
        portable['elements'].append({'id': 'run', 'original_id': 'label_run0', 'kind': 'Text', 'parent': 't'})
        self.assertTrue(gate_composition.compare(spec, portable)['pass'])

    def test_missing_source_and_disabled_policy_fail_without_losing_reports(self):
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);out=root/'captures';specs=root/'specs'
            out.mkdir();specs.mkdir()
            kit = {'name': 'fixture', 'screens': ['A'], 'input_format': 'design',
                   'splash_makepad_dir': out, 'specs_dir': specs}
            self.assertFalse(gate_composition.evaluate(kit)['pass'])
            spec, portable = fixture()
            (specs/'A.json').write_text(json.dumps(spec))
            (out/'A.portable.json').write_text(json.dumps(portable))
            self.assertFalse(gate_composition.evaluate(kit)['pass'])
            kit['native_widgets_first'] = True
            self.assertFalse(gate_composition.evaluate(kit)['pass'])
            from core.semantic_policy import source_tree_hash,POLICY
            review={'policy_version':POLICY['version'],'reference_sha256':spec.get('reference_sha256'),
                'elements':[],'source_review':{'verdict':'complete','reviewer':'test','basis':'reviewed fixture source',
                    'method':'source_image_and_hierarchy','source_tree_sha256':source_tree_hash(spec)}}
            (root/'semantics').mkdir();(root/'semantics/A.json').write_text(json.dumps(review))
            self.assertTrue(gate_composition.evaluate(kit)['pass'])
            (specs/'A.json').write_text('{broken')
            self.assertFalse(gate_composition.evaluate(kit)['pass'])
            self.assertTrue((out/'A.composition.json').exists())

    def test_visual_and_structural_pass_cannot_hide_composition_failure(self):
        with tempfile.TemporaryDirectory() as td:
            out = pathlib.Path(td)
            kit = {'name': 'fixture', 'screens': ['A'], 'input_format': 'design',
                   'native_widgets_first': True, 'design_scale': 1,
                   'splash_makepad_dir': out, 'specs_dir': out, 'targets_dir': out}
            spec, portable = fixture()
            portable['elements'][2]['kind'] = 'Stack'
            (out/'A.json').write_text(json.dumps(spec))
            (out/'A.portable.json').write_text(json.dumps(portable))
            (out/'A.structure.json').write_text('{"pass": true}')
            with patch.object(repair_feedback.gate_visual, 'evaluate', return_value=[{'screen': 'A', 'pass': True}]):
                result = json.loads(repair_feedback.collect(kit).read_text())
            self.assertTrue(result['screens'][0]['needs_repair'])
            self.assertTrue(result['screens'][0]['composition']['element_differences'])
            self.assertFalse(result['acceptance']['pass'])

    def test_fixed_artboard_pass_never_certifies_responsive_components(self):
        with tempfile.TemporaryDirectory() as td:
            result = acceptance.write({'name': 'fixture', 'splash_makepad_dir': pathlib.Path(td)},
                                      [{'needs_repair': False}], {})
            self.assertTrue(result['pass'])
            self.assertEqual(result['scope'], 'fixed_artboard_parity')
            self.assertFalse(result['application_complete'])
            self.assertEqual({r['status'] for r in result['next_composition_round']}, {'not_established'})

    def test_standalone_gallery_refreshes_acceptance_and_exposes_policy_failure(self):
        with tempfile.TemporaryDirectory() as td:
            out = pathlib.Path(td)
            kit = {'name': 'fixture', 'screens': ['A'], 'input_format': 'design',
                   'native_widgets_first': True, 'design_scale': 1,
                   'splash_makepad_dir': out, 'specs_dir': out, 'targets_dir': out,
                   'verdicts': {'splash_makepad': str(out/'verdicts.jsonl')}}
            spec, portable = fixture()
            portable['elements'][2]['kind'] = 'Stack'
            (out/'A.json').write_text(json.dumps(spec))
            (out/'A.portable.json').write_text(json.dumps(portable))
            (out/'A.structure.json').write_text('{"pass": true}')
            with patch.object(gallery.kitconf, 'load', return_value=kit), \
                 patch('sys.argv', ['gallery.py', '--kit', 'fixture']), \
                 patch.object(gallery.gate_visual, 'evaluate', return_value=[{'screen': 'A', 'pass': True}]):
                gallery.main()
            html = (out/'gallery.html').read_text()
            self.assertIn('Fixed artboard parity: FAILED', html)
            self.assertIn('Native widget policy: FAIL', html)
            self.assertIn('data-repair="true"', html)
            self.assertFalse(json.loads((out/'acceptance.json').read_text())['pass'])


if __name__ == '__main__':
    unittest.main()
