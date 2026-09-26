import json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import studio


class CaptureLifecycleTests(unittest.TestCase):
    def test_launch_redirects_every_output_away_from_archived_round(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);old=root/'rounds/001';old.mkdir(parents=True)
            archive=old/'native.json';archive.write_text('immutable evidence')
            request={'card':'page.card','data':'page.data.json','result':str(archive),'layout':str(old/'layout.json'),
                     'actions':str(old/'actions.json'),'semantic_result':str(old/'semantic-state.json'),'semantic_probe':str(old/'probe.json')}
            (root/'current-request.json').write_text(json.dumps(request))
            def remote(kind,*args):
                return {'builds':[]} if kind=='ListBuilds' else {'build_id':[999]}
            with patch.object(studio,'HERE',root),patch.object(studio,'request',side_effect=remote):studio.launch()
            current=json.loads((root/'current-request.json').read_text())
            for key in ('result','layout','actions','semantic_result','semantic_probe'):
                self.assertTrue(Path(current[key]).is_relative_to(root/'qa-work/startup'))
            self.assertEqual(archive.read_text(),'immutable evidence')
    def test_interaction_cannot_rewrite_an_already_gated_round(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td);(p/'gate.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'immutable'):studio.click_controls(p,[1])

    def test_progress_probe_waits_for_requested_value_and_paint_on_restore(self):
        before={'before':.3,'after':.75,'value':.75,'painted_value':.75}
        samples=[
            {**before,'painted_value':.3},  # late paint from the preceding probe
            {'before':.75,'after':.3,'value':.3,'painted_value':.75},
            {'before':.75,'after':.3,'value':.3,'painted_value':.3},
        ]
        read=iter({'elements':{'progress':s}} for s in samples)
        with patch.object(studio.time,'sleep') as sleep:
            result=studio.await_semantic_change(lambda:next(read),'progress',before,.3,paint=True)
        self.assertEqual(result,samples[-1]);self.assertEqual(sleep.call_count,2)

    def test_unsettled_probe_fails_instead_of_publishing_stale_state(self):
        with patch.object(studio.time,'monotonic',side_effect=[0,6]):
            with self.assertRaisesRegex(RuntimeError,'did not settle for progress'):
                studio.await_semantic_change(lambda:{'elements':{}},'progress',{},.3,paint=True)


if __name__=='__main__':unittest.main()
