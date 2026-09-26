"""Regressions for the inspection gap, using the captured native Weather pilot."""
import json,shutil,tempfile,unittest
from pathlib import Path
from catalogue import HERE
from compile import digest
from gate import evaluate
from observe import light_foreground

class InspectionGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.directory=Path(self.temp.name)/'weather-01';self.directory.mkdir()
        source=HERE/'weather-01';self.round=self.directory/'round'
        shutil.copytree(source/'rounds/004',self.round)
        for name in ['reference.png','observations.json']:shutil.copy2(source/name,self.directory/name)
    def tearDown(self):self.temp.cleanup()
    def change(self,name,fn):
        path=self.round/name;data=json.loads(path.read_text());fn(data);path.write_text(json.dumps(data))
        # Update the file receipt so the test isolates the semantic failure.
        proof_path=self.round/'provenance.json';proof=json.loads(proof_path.read_text())
        proof['files'][name]=digest(path.read_bytes());proof_path.write_text(json.dumps(proof))
    def test_host_only_never_passes(self):
        self.change('tree.json',lambda d:d.update(dump='W3 3\n0 -1 main_window Window 0 0 406 776\n1 0 body KeyboardView 0 0 406 776\n2 1 host Splash 0 0 406 776\n'))
        self.change('snapshot.json',lambda d:d.update(widgets=[w for w in d['widgets'] if not w['id'].startswith('beauty_')]))
        report=evaluate(self.directory,self.round)
        self.assertFalse(report['native_structure_pass']);self.assertTrue(any('host-only' in e for e in report['native_errors']))
    def test_current_nonce_is_required(self):
        self.change('layout.json',lambda d:d.update(nonce='a-previous-screen'))
        report=evaluate(self.directory,self.round)
        self.assertIn('stale native layout nonce',report['native_errors'])
    def test_each_native_widget_requires_its_query(self):
        self.change('queries.json',lambda d:d.pop('beauty_0_10_2'))
        report=evaluate(self.directory,self.round)
        self.assertTrue(any('primary_control' in e and 'WidgetQuery' in e for e in report['native_errors']))
    def test_disabled_control_cannot_pass_as_enabled(self):
        def disable(d):
            next(w for w in d['widgets'] if w['id']=='beauty_0_10_2')['enabled']=False
        self.change('snapshot.json',disable)
        report=evaluate(self.directory,self.round)
        self.assertTrue(any('primary_control' in e and 'enabled-state' in e for e in report['native_errors']))
    def test_modified_screenshot_receipt_fails(self):
        proof=self.round/'provenance.json';data=json.loads(proof.read_text());data['files']['native.png']='0'*64;proof.write_text(json.dumps(data))
        self.assertIn('stale evidence: native.png',evaluate(self.directory,self.round)['native_errors'])
    def test_visual_findings_feed_the_current_repair_round(self):
        finding={'area':'typography','status':'open','detail':'Word spaces collapse in the heading.'}
        review={'reference_sha256':digest((self.directory/'reference.png').read_bytes()),
                'native_sha256':digest((self.round/'native.png').read_bytes()),
                'reviewer':'test reviewer','verdict':'repair',
                'criteria':{'typography':False,'colors':True,'imagery':True,'effects':True},'findings':[finding]}
        (self.directory/'visual-review.json').write_text(json.dumps(review))
        self.assertFalse(evaluate(self.directory,self.round)['accepted'])
        repair=json.loads((self.round/'repair.json').read_text())
        self.assertEqual(repair['visual_findings'],[finding])
        self.assertEqual(repair['visual_verdict'],'repair')
        review['native_sha256']='0'*64
        (self.directory/'visual-review.json').write_text(json.dumps(review))
        evaluate(self.directory,self.round)
        stale=json.loads((self.round/'repair.json').read_text())
        self.assertFalse(stale['visual_review_current'])
        self.assertEqual(stale['visual_findings'],[])

class TextContrastTests(unittest.TestCase):
    def test_muted_text_on_dark_surface_is_light_foreground(self):
        text={'id':'label','color':0xffa0afa9};root={'id':'page','bg':0xff171c1c,'c':[text]}
        self.assertTrue(light_foreground(text,[root,text]))
    def test_button_uses_its_paint_surface_for_contrast(self):
        text={'id':'label','color':0xff171c1c};paint={'id':'paint','bg':0xffd2ef82};button={'id':'button','kit':'{}','c':[paint,text]}
        self.assertFalse(light_foreground(text,[button,paint,text]))

if __name__=='__main__':unittest.main()
