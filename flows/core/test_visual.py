import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import hashlib
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch
from core.gate_visual import review_result
from core.judge_shots import PROMPT,comparison_reference


class VisualGateTests(unittest.TestCase):
    def test_review_writer_lock_is_exclusive_and_released_after_failure(self):
        import fcntl
        from core import judge_shots as module
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'reviews.jsonl'
            kit={'verdicts':{'desktop':str(path)}}
            with path.with_suffix('.lock').open('a') as contender:
                def review(*args):
                    with self.assertRaises(BlockingIOError):
                        fcntl.flock(contender,fcntl.LOCK_EX|fcntl.LOCK_NB)
                    raise RuntimeError('review failed')
                with patch.object(module.kitconf,'load',return_value=kit), \
                     patch.object(module.sys,'argv',['judge']),patch.object(module,'judge',side_effect=review):
                    with self.assertRaisesRegex(RuntimeError,'review failed'):module.main()
                fcntl.flock(contender,fcntl.LOCK_EX|fcntl.LOCK_NB)

    def test_failed_review_batch_preserves_other_completed_verdicts(self):
        from core import judge_shots as judge
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);verdict=root/'reviews.jsonl'
            for name in ('first','second'):
                (root/(name+'.splash')).write_text('{}')
                Image.new('RGB',(10,20),'white').save(root/(name+'.png'))
            kit=dict(screens=['first','second'],targets_dir=root,cards_dir=root,splash_makepad_dir=root,
                input_format='design',verdicts={'splash_makepad':str(verdict)})
            with patch.object(judge.kitconf,'load',return_value=kit), \
                 patch.object(judge.sys,'argv',['judge','--rail','splash_makepad','--workers','2']), \
                 patch.object(judge.B,'claude_text',side_effect=[RuntimeError('judge unavailable'),
                     '{"design_match":9,"verdict":"accept","worst":"minor AA"}']):
                with self.assertRaisesRegex(RuntimeError,'review batch failed'):judge.main()
            rows=list(map(json.loads,verdict.read_text().splitlines()))
            self.assertEqual(len(rows),1)
            self.assertEqual(rows[0]['design_match'],9)

    def test_followup_cannot_reuse_changed_evidence_or_a_different_original_review(self):
        from core import visual_evidence as evidence
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);image=root/'region.png';image.write_bytes(b'original crop')
            proof=root/'measurements.json'
            proof.write_text(json.dumps({'inputs':'pair','regions':[{'bounds':[0,0,10,10]}],
                'files':{str(image):evidence.digest(image.read_bytes())}}))
            original={'inputs':'pair','design_match':8,'verdict':'accept','worst':'color mismatch'}
            review={'inputs':'pair','original_review_sha256':evidence.row_digest(original),
                'prompt_sha256':evidence.digest(evidence.PROMPT.encode()),'evidence':str(proof),
                'evidence_sha256':evidence.digest(proof.read_bytes())}
            self.assertEqual(evidence.validate_followup(review,original,'pair'),[])
            self.assertTrue(evidence.validate_followup(review,original,'new pixels'))
            self.assertTrue(evidence.validate_followup(review,original|{'worst':'missing text'},'pair'))
            image.write_bytes(b'changed crop')
            self.assertIn('changed evidence image',evidence.validate_followup(review,original,'pair'))

    def test_pixel_evidence_measures_equal_swatches_without_altering_sources(self):
        from core import visual_evidence as evidence
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);targets=root/'targets';targets.mkdir();out=root/'captures';out.mkdir()
            Image.new('RGB',(20,40),(76,95,239)).save(targets/'screen.png')
            Image.new('RGB',(10,20),(76,95,239)).save(out/'screen.png')
            source=(targets/'screen.png').read_bytes()
            kit=dict(targets_dir=targets,splash_makepad_dir=out)
            _,_,_,proof=evidence.build_evidence(kit,'screen',[{'bounds':[0,0,10,20],'name':'swatch'}],'Check the color finding')
            data=json.loads(proof.read_text());region=data['regions'][0]
            self.assertEqual(region['mean_absolute_rgb_error'],0)
            self.assertEqual(region['reference_dominant_rgb'],[76,95,239])
            self.assertEqual(region['native_dominant_rgb'],[76,95,239])
            self.assertEqual((targets/'screen.png').read_bytes(),source)

    def test_partial_review_preserves_other_screens_and_frozen_native_bytes(self):
        from core import judge_shots as judge
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td)
            Image.new('RGB',(10,20),'white').save(root/'screen.png')
            (root/'screen.splash').write_text('{}')
            # The fixture capture must follow its source, as in the native run.
            Image.new('RGB',(10,20),'white').save(root/'screen.png')
            verdict=root/'reviews.jsonl'
            other={'screen':'other','inputs':'old-evidence','design_match':9,'verdict':'accept'}
            verdict.write_text(json.dumps(other)+'\n')
            kit=dict(screens=['screen','other'],targets_dir=root,cards_dir=root,splash_makepad_dir=root,
                     input_format='design',verdicts={'splash_makepad':str(verdict)})
            original=(root/'screen.png').read_bytes()
            with patch.object(judge.kitconf,'load',return_value=kit), \
                 patch.object(judge.sys,'argv',['judge','--rail','splash_makepad','--only','screen']), \
                 patch.object(judge.B,'claude_text',return_value='{"design_match":9,"verdict":"accept","worst":"minor AA"}'):
                judge.main()
            rows=list(map(json.loads,verdict.read_text().splitlines()))
            self.assertEqual(rows[1],other)
            self.assertEqual(pathlib.Path(rows[0]['comparison_capture']).read_bytes(),original)

    def test_reference_uses_native_scale_and_window_matte_without_changing_source(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            target,capture,output=[pathlib.Path(td)/n for n in ('target.png','capture.png','comparison.png')]
            Image.new('RGBA',(200,400),(255,0,0,128)).save(target)
            Image.new('RGBA',(100,200),'white').save(capture)
            source=target.read_bytes()
            self.assertEqual(comparison_reference(target,capture,output),output)
            with Image.open(output) as im:
                self.assertEqual(im.size,(100,200))
                self.assertEqual(im.getpixel((50,100)),(255,127,127,255))
            self.assertEqual(target.read_bytes(),source)

    def test_fractional_export_rounding_is_allowed_but_stretching_is_not(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            target,capture,output=[pathlib.Path(td)/n for n in ('target.png','capture.png','comparison.png')]
            Image.new('RGB',(982,882),'white').save(target)
            Image.new('RGB',(981,882),'white').save(capture)
            comparison_reference(target,capture,output)
            Image.new('RGB',(960,882),'white').save(capture)
            with self.assertRaisesRegex(ValueError,'aspect'):
                comparison_reference(target,capture,output)

    def row(self, **kwargs):
        return dict(inputs=hashlib.sha256(b'design'+b'capture'+PROMPT.encode()).hexdigest(),
                    verdict='accept',design_match=9) | kwargs

    def test_current_accepted_review_at_threshold_passes(self):
        self.assertTrue(review_result(b'design',b'capture',self.row(),9)['pass'])

    def test_changed_pixels_or_missing_review_fail(self):
        self.assertFalse(review_result(b'changed',b'capture',self.row(),9)['pass'])
        self.assertFalse(review_result(b'design',b'changed',self.row(),9)['pass'])
        self.assertFalse(review_result(b'design',b'capture',{},9)['pass'])

    def test_high_score_cannot_override_rework_or_low_accepted_score(self):
        self.assertFalse(review_result(b'design',b'capture',self.row(verdict='rework',design_match=10),9)['pass'])
        self.assertFalse(review_result(b'design',b'capture',self.row(design_match=8),9)['pass'])


if __name__=='__main__':unittest.main()
