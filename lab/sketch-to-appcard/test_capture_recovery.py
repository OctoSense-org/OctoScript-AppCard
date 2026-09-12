import tempfile,unittest,json
from pathlib import Path
import capture_loop


class CaptureRecoveryTests(unittest.TestCase):
    def execute(self,results):
        with tempfile.TemporaryDirectory() as td:
            kit={'name':'fixture','splash_makepad_dir':Path(td)};calls=[]
            def run(kit,log):
                code,text=results[len(calls)];calls.append(log);log.write_text(text);return code
            passed=capture_loop.run(kit,runner=run)
            return passed,len(calls),json.loads((Path(td)/'capture-recovery.json').read_text())
    def test_blank_readback_restarts_and_resumes(self):
        result,count,receipt=self.execute([(1,'empty native frame after three readbacks'),(0,'current capture')])
        self.assertTrue(result);self.assertEqual(count,2);self.assertEqual(receipt['status'],'passed')
    def test_semantic_failure_does_not_retry(self):
        result,count,_=self.execute([(1,'native data mapping is incorrect')])
        self.assertFalse(result);self.assertEqual(count,1)
    def test_repeated_black_frames_never_pass(self):
        result,count,receipt=self.execute([(1,'empty native frame after three readbacks')]*3)
        self.assertFalse(result);self.assertEqual(count,3);self.assertEqual(receipt['status'],'failed')
    def test_stale_l0_sources_fail_before_starting_studio(self):
        with tempfile.TemporaryDirectory() as td:
            def forbidden(*args):self.fail('Studio must not start with stale L0 sources')
            kit={'name':'fixture','splash_makepad_dir':Path(td)}
            self.assertFalse(capture_loop.run(kit,runner=forbidden,validate=lambda kit:False))
            receipt=json.loads((Path(td)/'capture-recovery.json').read_text())
            self.assertEqual(receipt['status'],'failed');self.assertEqual(receipt['attempts'],[])


if __name__=='__main__':unittest.main()
