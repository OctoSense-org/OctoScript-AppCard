import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import json,tempfile,unittest
from pathlib import Path
from core.curve import sample


class CurveTests(unittest.TestCase):
    def execute(self,path,attributes=''):
        with tempfile.TemporaryDirectory() as td:
            source=Path(td)/'source.svg';output=Path(td)/'data.json'
            source.write_text(f'<svg viewBox="0 0 100 100"><path {attributes} d="{path}"/></svg>')
            receipt=sample(source,output,8)
            return receipt,json.loads(output.read_text())
    def test_numeric_endpoints_and_source_provenance(self):
        receipt,rows=self.execute('M0 100 C25 100 75 0 100 0')
        self.assertEqual(rows[0],{'x':0,'y':0});self.assertEqual(rows[-1],{'x':1,'y':1})
        self.assertEqual(len(rows),9);self.assertTrue(receipt['approximate'])
        self.assertEqual(receipt['origin'],'measured_sketch')
    def test_nonmonotonic_or_untransformed_assumption_fails(self):
        for path,attrs in [('M100 0 L0 100',''),('M0 0 L100 100','transform="scale(2)"')]:
            with self.assertRaises(ValueError):self.execute(path,attrs)
    def test_unsupported_or_invalid_commands_fail(self):
        for path in ['L0 0 L100 100','M0 0 Q50 50 100 100','M0 0 L100 100 Z']:
            with self.assertRaises(ValueError):self.execute(path)


if __name__=='__main__':unittest.main()
