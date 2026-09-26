"""Regression cases for semantic substitutions and artwork provenance."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image
from semantics import evaluate, propose, sha, write, asset_issues, data_issues, local_asset
from compile import compile_page


class MappingRulesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        Image.new('RGB', (80, 60), '#406050').save(self.directory / 'reference.png')

    def tearDown(self):
        self.temp.cleanup()

    def fixture(self, node, graphic=None):
        contract = {'schema_version': 1, 'id': 'fixture', 'tree': node,
                    'graphics': {node['id']: {'kind': graphic}} if graphic else {}}
        write(self.directory / 'contract.json', contract)
        return propose(self.directory)

    def test_text_can_pass_without_being_rasterized(self):
        self.fixture({'t': 'text', 'id': 'headline', 'text': 'Weather'})
        self.assertTrue(evaluate(self.directory)['pass'])

    def test_native_input_requires_a_declared_value_binding(self):
        manifest = self.fixture({'t': 'input', 'id': 'search', 'text': ''})
        self.assertFalse(evaluate(self.directory)['pass'])
        manifest['elements'][0]['behavior'] = {'event': 'changed', 'target': 'search', 'property': 'text'}
        write(self.directory / 'semantic-map.json', manifest)
        self.assertTrue(evaluate(self.directory)['pass'])

    def test_form_field_keeps_its_native_input_role(self):
        manifest = self.fixture({'t': 'stack', 'id': 'field',
            'kit': json.dumps({'widget': 'KitFormField', 'bindings': {'input': [0]}}),
            'c': [{'t': 'input', 'id': 'value', 'text': ''}]})
        for entry in manifest['elements']:
            self.assertEqual(entry['role'], 'input')
            entry['behavior'] = {'event': 'changed', 'target': 'value', 'property': 'text'}
        write(self.directory / 'semantic-map.json', manifest)
        self.assertTrue(evaluate(self.directory)['pass'])

    def test_svg_trend_is_rejected_even_though_it_is_a_native_widget_kind(self):
        self.fixture({'t': 'svg', 'id': 'trend'}, 'line')
        report = evaluate(self.directory)
        self.assertFalse(report['pass'])
        self.assertIn('LinePlot', report['elements'][0]['expected_widgets'])
        self.assertTrue(any('wrong renderer kind' in e for e in report['errors']))

    def test_declared_chart_cannot_be_reclassified_as_artwork_to_bypass_rules(self):
        manifest = self.fixture({'t': 'svg', 'id': 'trend'}, 'line')
        manifest['elements'][0]['role'] = 'illustration'
        write(self.directory / 'semantic-map.json', manifest)
        self.assertTrue(any('contradicts' in e for e in evaluate(self.directory)['errors']))

    def test_range_text_requires_a_real_stateful_control(self):
        self.fixture({'t': 'text', 'id': 'period_0', 'text': '1D'})
        report = evaluate(self.directory)
        self.assertFalse(report['pass'])
        self.assertEqual(report['elements'][0]['role'], 'range_option')
        self.assertTrue(any('binding' in e for e in report['errors']))

    def test_classification_does_not_overwrite_reviewed_decisions(self):
        manifest = self.fixture({'t': 'text', 'id': 'title', 'text': 'News'})
        manifest['elements'][0]['basis'] = 'Reviewed against source image'
        write(self.directory / 'semantic-map.json', manifest)
        self.assertEqual(propose(self.directory), manifest)

    def test_missing_source_node_mapping_fails(self):
        manifest = self.fixture({'t': 'text', 'id': 'title', 'text': 'News'})
        manifest['elements'] = []
        write(self.directory / 'semantic-map.json', manifest)
        self.assertIn('title: unclassified source element', evaluate(self.directory)['errors'])

    def test_new_reference_invalidates_mapping(self):
        self.fixture({'t': 'text', 'id': 'title', 'text': 'News'})
        Image.new('RGB', (80, 60), '#ffffff').save(self.directory / 'reference.png')
        self.assertFalse(evaluate(self.directory)['pass'])

    def test_unimplemented_chart_adapter_cannot_compile_by_changing_a_type_name(self):
        self.fixture({'t': 'line_plot', 'id': 'trend'}, 'line')
        self.assertTrue(any('adapter is not implemented' in e for e in evaluate(self.directory)['errors']))

    def test_preflight_preserves_existing_generated_card_on_failure(self):
        self.fixture({'t': 'svg', 'id': 'trend'}, 'line')
        output = self.directory / 'page.card'
        output.write_text('previous reviewed card')
        with self.assertRaisesRegex(ValueError, 'Semantic mapping blocked'):
            compile_page(self.directory)
        self.assertEqual(output.read_text(), 'previous reviewed card')

    def crop_fixture(self, full=False):
        size = (80, 60) if full else (20, 15)
        Image.new('RGB', size, '#406050').save(self.directory / 'banner.png')
        asset = {'method': 'source_crop', 'path': 'banner.png', 'sha256': sha(self.directory / 'banner.png'),
                 'reference_sha256': sha(self.directory / 'reference.png'), 'crop_pixels': [0, 0, *size],
                 'contains_ui': False, 'fit': 'contain', 'clip': True}
        return {'role': 'illustration', 'asset': asset}, {'reference_sha256': asset['reference_sha256']}

    def test_exact_illustration_region_is_an_allowed_image_asset(self):
        entry, manifest = self.crop_fixture()
        self.assertEqual(asset_issues(self.directory, entry, manifest), [])

    def test_verified_crop_compiles_as_a_bound_image_asset(self):
        manifest = self.fixture({'t': 'image', 'id': 'banner', 'w': 20, 'h': 15})
        entry, _ = self.crop_fixture()
        manifest['elements'][0].update(role='illustration', confidence=1, decision='reviewed',
                                       basis='Artwork-only region inspected in source', asset=entry['asset'])
        write(self.directory / 'semantic-map.json', manifest)
        with patch('compile.GALLERY', self.directory / 'gallery'):
            compile_page(self.directory)
        data = json.loads((self.directory / 'page.data.json').read_text())
        url = data['$kit']['placements']['banner']['layout']['src']
        self.assertTrue(url.endswith('-' + entry['asset']['sha256'][:12] + '.png'))
        mapping = json.loads((self.directory / 'mapping.json').read_text())['elements'][0]
        self.assertEqual((mapping['kind'], mapping['semantic_role']), ('image', 'illustration'))

    def test_repainted_crop_fails_even_with_a_fresh_asset_hash(self):
        entry, manifest = self.crop_fixture()
        Image.new('RGB', (20, 15), '#ffffff').save(self.directory / 'banner.png')
        entry['asset']['sha256'] = sha(self.directory / 'banner.png')
        self.assertTrue(any('crop pixels do not match' in e for e in asset_issues(self.directory, entry, manifest)))

    def test_contain_cannot_silently_use_stretch_at_a_different_aspect_ratio(self):
        manifest = self.fixture({'t': 'image', 'id': 'banner', 'w': 100, 'h': 100})
        entry, _ = self.crop_fixture()
        manifest['elements'][0].update(role='illustration', confidence=1, decision='reviewed',
                                       basis='Reviewed illustration crop', asset=entry['asset'])
        write(self.directory / 'semantic-map.json', manifest)
        self.assertTrue(any('native fitting adapter' in e for e in evaluate(self.directory)['errors']))

    def test_full_screen_crop_cannot_masquerade_as_illustration(self):
        entry, manifest = self.crop_fixture(full=True)
        self.assertTrue(any('full-screen' in e for e in asset_issues(self.directory, entry, manifest)))

    def test_crop_with_ui_is_rejected(self):
        entry, manifest = self.crop_fixture()
        entry['asset']['contains_ui'] = True
        self.assertTrue(any('artwork only' in e for e in asset_issues(self.directory, entry, manifest)))

    def test_svg_cannot_hide_ui_text(self):
        asset = self.directory / 'art.svg'
        asset.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text>Buy now</text></svg>')
        reference = sha(self.directory / 'reference.png')
        entry = {'asset': {'method': 'reference_svg', 'path': 'art.svg', 'sha256': sha(asset),
                           'reference_sha256': reference, 'fit': 'contain', 'clip': True}}
        self.assertTrue(any('UI text' in e for e in asset_issues(self.directory, entry, {'reference_sha256': reference})))

    def test_asset_paths_cannot_escape_capture(self):
        self.assertIsNone(local_asset(self.directory, '/etc/hosts'))
        self.assertIsNone(local_asset(self.directory, '../reference.png'))

    def test_image_recovered_series_cannot_claim_exact_values(self):
        path = self.directory / 'series.json'
        write(path, [{'t': 0, 'p': 10}, {'t': 1, 'p': 11}])
        data = {'origin': 'measured_image', 'path': 'series.json', 'sha256': sha(path),
                'x_key': 't', 'y_keys': ['p'], 'units': {'x': 'normalized', 'y': 'normalized'},
                'domain': {'x': [0, 1], 'y': [0, 20]}}
        self.assertIn('image-recovered values must be labeled approximate', data_issues(self.directory, {'data': data}))
        data['approximate'] = True
        self.assertEqual(data_issues(self.directory, {'data': data}), [])


if __name__ == '__main__':
    unittest.main()


class ValueDomainTests(unittest.TestCase):
    def test_flags_values_that_parse_but_cannot_render(self):
        from semantics import value_domain_issues
        bad = {'t': 'text', 'id': 'l', 'text': 'x', 'x': 0, 'y': 0, 'w': 60, 'h': 30, 'size': 44, 'alignx': 2, 'color': 'red'}
        issues = value_domain_issues(bad)
        self.assertTrue(any('alignx' in i for i in issues), issues)
        self.assertTrue(any('line box' in i for i in issues), issues)
        self.assertTrue(any('color' in i for i in issues), issues)

    def test_accepts_a_well_formed_text_node(self):
        from semantics import value_domain_issues
        good = {'t': 'text', 'id': 'l', 'text': 'x', 'x': 0, 'y': 0, 'w': 60, 'h': 22, 'size': 15,
                'alignx': 0.5, 'color': 4278190080, 'bg': '#FFFFFFFF'}
        self.assertEqual(value_domain_issues(good), [])
        # An authored line_height is the box the text needs, not 1.45 x size.
        measured = {'t': 'text', 'id': 'm', 'text': '09:41', 'w': 60, 'h': 20, 'size': 15, 'line_height': 19.5}
        self.assertEqual(value_domain_issues(measured), [])

