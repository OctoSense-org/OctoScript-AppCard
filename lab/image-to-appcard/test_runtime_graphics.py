"""Regression evidence for bugs found by the Studio visual repair rounds."""
import json,shutil,tempfile,unittest
from pathlib import Path
from catalogue import HERE
from semantics import evaluate as semantic_gate,sha
from gate import evaluate as image_gate

class RuntimeGraphicEvidenceTests(unittest.TestCase):
    def fixture(self,id,round):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup)
        directory=Path(temp.name)/id;directory.mkdir();capture=directory/'round'
        source=HERE/id;shutil.copytree(source/'rounds'/round,capture)
        shutil.copy2(source/'reference.png',directory/'reference.png')
        shutil.copy2(capture/'semantic-map.json',directory/'semantic-map.json')
        return directory,capture

    def test_state_change_cannot_pass_an_unpainted_progress_fill(self):
        directory,capture=self.fixture('news-09','003')
        report=image_gate(directory,capture)
        self.assertTrue(any('painted fill differs from native value' in e for e in report['image_errors']))

    def test_repaired_progress_has_baseline_and_changed_pixel_evidence(self):
        directory,capture=self.fixture('news-09','004')
        report=image_gate(directory,capture)
        self.assertFalse(any('fill' in e for e in report['image_errors']),report['image_errors'])

    def test_a_data_hash_cannot_hide_different_actual_native_samples(self):
        directory,capture=self.fixture('stock-04','004')
        path=capture/'semantic-state.json';state=json.loads(path.read_text())
        state['elements']['price_chart']['series'][0]['y'][0]+=.1
        path.write_text(json.dumps(state))
        proof_path=capture/'provenance.json';proof=json.loads(proof_path.read_text())
        proof['files']['semantic-state.json']=sha(path);proof_path.write_text(json.dumps(proof))
        report=semantic_gate(directory,capture)
        self.assertTrue(any('actual native series differ' in e for e in report['errors']))

    def test_range_selection_must_update_the_native_label_color(self):
        directory,capture=self.fixture('stock-04','006')
        self.assertTrue(semantic_gate(directory,capture)['pass'])
        path=capture/'semantic-state.json';state=json.loads(path.read_text())
        # The unselected label retains the active color, as in the repaired bug.
        state['elements']['range_control_1']['label_color']=state['elements']['range_control_0']['label_color']
        path.write_text(json.dumps(state))
        proof_path=capture/'provenance.json';proof=json.loads(proof_path.read_text())
        proof['files']['semantic-state.json']=sha(path);proof_path.write_text(json.dumps(proof))
        report=semantic_gate(directory,capture)
        self.assertTrue(any('label color does not follow' in e for e in report['errors']))

if __name__=='__main__':unittest.main()
