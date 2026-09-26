import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import json,tempfile,unittest
from pathlib import Path
from core.repair import apply,sha


class RepairTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for name,value in [('gate.json',{'pass':False}),('mapped.json',{'x':8}),('data.json',{'values':[1,2]})]:
            (self.root/name).write_text(json.dumps(value))
        self.plan={'schema_version':1,'findings':['layout shifted; data misbound'],
            'evidence':{'gate.json':sha((self.root/'gate.json').read_bytes())},
            'inputs':{n:sha((self.root/n).read_bytes()) for n in ('mapped.json','data.json')},
            'operations':[{'op':'set','category':cat,'file':name,'pointer':ptr,'before':before,'after':after,
                'element':'chart','reason':'measured source discrepancy'} for cat,name,ptr,before,after in
                [('layout','mapped.json','/x',8,12),('data','data.json','/values',[1,2],[2,4])]]}
        self.path=self.root/'repair.json';self.save()
    def save(self):self.path.write_text(json.dumps(self.plan))
    def tearDown(self):self.temp.cleanup()
    def test_preview_does_not_mutate(self):
        result=apply(self.root,self.path,True)
        self.assertEqual(result['status'],'prepared');self.assertEqual(json.loads((self.root/'mapped.json').read_text())['x'],8)
        self.assertFalse((self.root/'.repairs').exists())
    def test_repeated_apply_is_idempotent(self):
        apply(self.root,self.path);before=(self.root/'mapped.json').read_bytes()
        self.assertTrue(apply(self.root,self.path)['replayed']);self.assertEqual((self.root/'mapped.json').read_bytes(),before)
    def test_resume_after_interruption_between_files(self):
        def stop(index):raise InterruptedError('simulated process loss')
        with self.assertRaises(InterruptedError):apply(self.root,self.path,after_write=stop)
        self.assertEqual(json.loads((self.root/'mapped.json').read_text())['x'],12)
        self.assertEqual(json.loads((self.root/'data.json').read_text())['values'],[1,2])
        self.assertEqual(apply(self.root,self.path)['status'],'applied')
        self.assertEqual(json.loads((self.root/'data.json').read_text())['values'],[2,4])
    def test_stale_plan_does_not_write_any_file(self):
        (self.root/'data.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'stale'):apply(self.root,self.path)
        self.assertEqual(json.loads((self.root/'mapped.json').read_text())['x'],8)
    def test_recovery_preserves_concurrent_user_edits(self):
        def stop(index):raise InterruptedError()
        with self.assertRaises(InterruptedError):apply(self.root,self.path,after_write=stop)
        (self.root/'data.json').write_text('{"values":[99]}')
        with self.assertRaisesRegex(ValueError,'conflict'):apply(self.root,self.path)
        self.assertEqual(json.loads((self.root/'data.json').read_text())['values'],[99])
    def test_evidence_cannot_be_edited_by_repair(self):
        self.plan['inputs']['gate.json']=self.plan['evidence']['gate.json']
        self.plan['operations'][0]['file']='gate.json';self.save()
        with self.assertRaisesRegex(ValueError,'evidence'):apply(self.root,self.path)
    def test_recovery_checks_unmodified_dependencies(self):
        self.plan['operations']=self.plan['operations'][:1];self.save()
        def stop(index):raise InterruptedError()
        with self.assertRaises(InterruptedError):apply(self.root,self.path,after_write=stop)
        (self.root/'data.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'dependency changed'):apply(self.root,self.path)
    def test_path_escape_fails(self):
        self.plan['inputs']['../outside']=None;self.save()
        with self.assertRaisesRegex(ValueError,'escapes'):apply(self.root,self.path)


if __name__=='__main__':unittest.main()
