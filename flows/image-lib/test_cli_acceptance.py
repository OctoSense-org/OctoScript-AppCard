"""Process success must mean acceptance whenever a gate was requested."""
import json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import run


class AcceptanceCliTests(unittest.TestCase):
    def execute(self,accepted,status):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);d=root/'new-design';d.mkdir()
            (d/'latest.json').write_text(json.dumps({'round':'001'}))
            report={'native_structure_pass':True,'image_structure_pass':True,
                    'semantic_mapping_pass':True,'accepted':accepted,'visual_review':{'status':status}}
            with patch.object(run,'HERE',root),patch.object(run,'evaluate',return_value=report), \
                 patch('sys.argv',['run.py','--design','new-design','--stages','gate']), \
                 self.assertRaises(SystemExit) as exit:
                run.main()
            return exit.exception.code

    def test_missing_review_fails(self):self.assertEqual(self.execute(False,'human review required'),1)
    def test_stale_review_fails(self):self.assertEqual(self.execute(False,'stale or incomplete visual review'),1)
    def test_rejected_review_fails(self):self.assertEqual(self.execute(False,'repair'),1)
    def test_current_acceptance_succeeds(self):self.assertEqual(self.execute(True,'pass'),0)


if __name__=='__main__':unittest.main()
