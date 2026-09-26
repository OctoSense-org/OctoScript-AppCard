import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
from core import review


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / 'reference.png'
        self.native = self.root / 'native.png'
        for path in (self.source, self.native):
            Image.new('RGB', (20, 40), 'white').save(path)
        self.packet = self.root / 'packet'
        self.origin = {'kind': 'image', 'design': 'example-01'}
        self.mock = patch.object(review, 'paths', return_value=(self.source, self.native))
        self.mock.start()
        review.prepare(self.origin, self.packet)

    def tearDown(self):
        self.mock.stop()
        self.temp.cleanup()

    def decision(self):
        value = review.read(self.packet / 'decision.template.json')
        value.update(reviewer='Unit test fixture', verdict='pass', design_match=9,
                     criteria={k: True for k in review.CRITERIA}, basis='Explicit fixture decision')
        target = self.root / 'decision.json'
        review.write(target, value)
        return target

    def test_preparation_does_not_approve_and_unreviewed_template_is_rejected(self):
        self.assertFalse((self.root / 'visual-review.json').exists())
        with self.assertRaisesRegex(ValueError, 'explicit reviewed verdict'):
            review.submit(self.packet, self.packet / 'decision.template.json')

    def test_changed_native_pixels_require_a_new_review(self):
        decision = self.decision()
        Image.new('RGB', (20, 40), 'black').save(self.native)
        with self.assertRaisesRegex(ValueError, 'pixels changed'):
            review.submit(self.packet, decision)

    def test_modified_packet_is_rejected(self):
        decision = self.decision()
        Image.new('RGB', (20, 40), 'black').save(self.packet / 'reference.png')
        with self.assertRaisesRegex(ValueError, 'packet changed'):
            review.submit(self.packet, decision)

    def test_image_receipt_preserves_previous_review_and_requires_all_criteria(self):
        previous = self.root / 'visual-review.json'
        previous.write_text('{"verdict":"repair"}')
        old_hash = review.sha(previous)
        decision = self.decision()
        value = review.read(decision)
        value['criteria']['imagery'] = False
        review.write(decision, value)
        with self.assertRaisesRegex(ValueError, 'all four'):
            review.submit(self.packet, decision)
        review.submit(self.packet, self.decision())
        self.assertEqual(review.read(previous)['native_sha256'], review.sha(self.native))
        self.assertEqual(review.read(self.root / 'visual-reviews' / (old_hash + '.json')), {'verdict': 'repair'})

    def test_sketch_receipt_uses_existing_gate_hash_without_calling_a_model(self):
        import sys
        sys.path.insert(0, str(review.SKETCH))
        from core import kitconf
        from core.judge_shots import PROMPT
        packet = review.read(self.packet / 'packet.json')
        packet['origin'] = {'kind': 'sketch', 'kit': 'example', 'screen': 'Home'}
        review.write(self.packet / 'packet.json', packet)
        target = self.root / 'verdicts.jsonl'
        with patch.object(kitconf, 'load', return_value={'verdicts': {'splash_makepad': str(target)}}):
            review.submit(self.packet, self.decision())
        receipt = json.loads(target.read_text())
        self.assertEqual(receipt['inputs'], hashlib.sha256(self.source.read_bytes() + self.native.read_bytes() + PROMPT.encode()).hexdigest())
        self.assertEqual((receipt['verdict'], receipt['design_match']), ('accept', 9))

    def test_source_packet_stays_unreviewed_and_rejects_changed_source_pixels(self):
        import sys
        sys.path.insert(0, str(review.SKETCH))
        from core import kitconf
        spec={'name':'Home','cls':'artboard','reference_sha256':review.sha(self.source),
              'children':[{'name':'Group 42','cls':'group','native_widget_id':'anonymous'}]}
        specs=self.root/'specs';specs.mkdir();review.write(specs/'Home.json',spec)
        shutil_source=self.root/'Home.png'
        shutil_source.write_bytes(self.source.read_bytes())
        kit={'screens':['Home'],'specs_dir':specs,'targets_dir':self.root}
        with patch.object(kitconf,'load',return_value=kit):
            template=review.prepare_source('example','Home',self.root/'source-review')
            manifest=review.read(template)
            self.assertEqual(manifest['source_review']['verdict'],'needs_review')
            self.assertEqual(manifest['source_review']['reviewer'],'')
            Image.new('RGB',(20,40),'black').save(shutil_source)
            with self.assertRaisesRegex(ValueError,'pixels changed since import'):
                review.prepare_source('example','Home',self.root/'changed-source')


if __name__ == '__main__':
    unittest.main()
