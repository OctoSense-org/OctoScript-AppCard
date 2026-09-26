"""Failure handoff and composition evidence for the native beauty cycle."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[2]))  # flows/, for `core`
import json
import pathlib
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from core import composition
import run_kit


class BeautyLoopTests(unittest.TestCase):
    def test_render_failure_still_saves_failure_and_hands_off_to_repair(self):
        with tempfile.TemporaryDirectory() as td:
            kit = {'name':'fixture','splash_makepad_dir':pathlib.Path(td)}
            def result(*args, **kwargs):
                return SimpleNamespace(returncode=int(args[1] == 'capture_loop.py'))
            with patch.object(run_kit,'sh',side_effect=result) as calls, \
                 patch.object(run_kit,'stage_report') as report, self.assertRaises(SystemExit):
                run_kit.stage_splash_makepad(kit)
            report.assert_called_once_with(kit)
            scripts = [c.args[1] for c in calls.call_args_list]
            self.assertIn('gate_structure.py',scripts)
            self.assertNotIn('judge_shots.py',scripts)
            run = json.loads((pathlib.Path(td)/'pipeline-run.json').read_text())
            self.assertEqual(run['status'],'failed')
            self.assertEqual(run['errors'],['capture_loop.py exited 1'])

    def test_judge_failure_cannot_skip_visual_gate_or_repair(self):
        with tempfile.TemporaryDirectory() as td:
            kit = {'name':'fixture','splash_makepad_dir':pathlib.Path(td),'visual_review':'claude_cli'}
            with patch.object(run_kit,'sh',side_effect=lambda *a,**k:
                    SimpleNamespace(returncode=int(a[1]=='judge_shots.py'))) as calls, \
                 patch.object(run_kit,'stage_report') as report, self.assertRaises(SystemExit):
                run_kit.stage_splash_makepad(kit)
            self.assertIn('gate_visual.py',[c.args[1] for c in calls.call_args_list])
            report.assert_called_once()

    def test_native_capture_defaults_to_external_review_without_provider_calls(self):
        with tempfile.TemporaryDirectory() as td:
            kit={'name':'fixture','splash_makepad_dir':pathlib.Path(td)}
            with patch.object(run_kit,'sh',return_value=SimpleNamespace(returncode=0)) as calls, \
                 patch.object(run_kit,'stage_report'):
                run_kit.stage_splash_makepad(kit)
            scripts=[c.args[1] for c in calls.call_args_list]
            self.assertNotIn('judge_shots.py',scripts)
            self.assertIn('gate_visual.py',scripts)

    def test_native_doctor_requires_provider_cli_only_when_selected(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            binary = root / 'local-tool'
            binary.touch()
            kit = {'name': 'fixture', 'input_format': 'design',
                   'rails': ['splash-makepad'], 'sketch': str(binary), 'img_dir': str(root)}
            with patch.dict('os.environ', {'BEAUTY_BRIDGE': '', 'CARGO_MAKEPAD': str(binary),
                                          'SKETCHTOOL': str(binary)}), \
                 patch.object(run_kit, '_try_import', return_value=True), \
                 patch.object(run_kit.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='', stderr='')), \
                 patch('shutil.which', side_effect=lambda name: None if name == 'claude' else str(binary)) as which:
                for input_format in ('design', 'l0-kit'):
                    kit['input_format'] = input_format
                    run_kit.stage_doctor(kit)
                self.assertNotIn('claude', [call.args[0] for call in which.call_args_list])
                kit['visual_review'] = 'claude_cli'
                with self.assertRaisesRegex(SystemExit, 'preflight failed'):
                    run_kit.stage_doctor(kit)
                self.assertIn('claude', [call.args[0] for call in which.call_args_list])

    def test_composition_gate_failure_fails_pipeline_and_preserves_handoff(self):
        with tempfile.TemporaryDirectory() as td:
            kit = {'name':'fixture','splash_makepad_dir':pathlib.Path(td)}
            with patch.object(run_kit,'sh',side_effect=lambda *a,**k:
                    SimpleNamespace(returncode=int(a[1]=='gate_composition.py'))), \
                 patch.object(run_kit,'stage_report') as report, self.assertRaises(SystemExit):
                run_kit.stage_splash_makepad(kit)
            report.assert_called_once()
            run = json.loads((pathlib.Path(td)/'pipeline-run.json').read_text())
            self.assertEqual(run['status'], 'failed')
            self.assertEqual(run['scope'], 'fixed_artboard_parity')

    def test_saved_audit_runs_all_three_gates_without_capture_or_new_review(self):
        with tempfile.TemporaryDirectory() as td:
            kit = {'name':'fixture','splash_makepad_dir':pathlib.Path(td)}
            with patch.object(run_kit,'sh',return_value=SimpleNamespace(returncode=0)) as calls, \
                 patch.object(run_kit,'stage_report'):
                run_kit.stage_audit(kit)
            self.assertEqual([c.args[1] for c in calls.call_args_list],
                             ['gate_structure.py', 'gate_composition.py', 'gate_visual.py'])

    def test_manifest_counts_do_not_claim_complete_when_a_screen_is_missing(self):
        with tempfile.TemporaryDirectory() as td:
            out = pathlib.Path(td)
            kit = {'name':'fixture','input_format':'design','screens':['A','B'],
                   'splash_makepad_dir':out}
            (out/'A.portable.json').write_text(json.dumps({'elements':[
                {'kind':'Stack'},{'kind':'Image'},{'kind':'Text'},{'kind':'Input'}]}))
            report = composition.write(kit)
            self.assertFalse(report['complete'])
            self.assertIn('error',report['screens'][1])
            self.assertEqual(report['node_counts']['Image'],1)
            self.assertIn('absolute',report['layout'])
            self.assertIn('responsive layout',report['not_established'])


if __name__ == '__main__':
    unittest.main()
