import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('maintain', Path(__file__).resolve().parents[1] / 'maintain.py')
maintain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(maintain)


class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.lab = Path(self.temp.name)
        self.work = self.lab / 'core/work/example/native'
        self.cache = self.work / 'graphic-export-cache'
        self.cache.mkdir(parents=True)
        (self.cache / 'export.png').write_bytes(b'cached export')
        for name in ('source.sketch', 'resolved.sketch', 'source-cache.json'):
            (self.work / name).write_bytes(b'retained source')
        self.asset = self.work / 'assets/final.png'
        self.asset.parent.mkdir()
        self.asset.write_bytes(b'accepted asset')
        self.capture = self.work / 'l0-captures/Screen.png'
        self.capture.parent.mkdir()
        self.capture.write_bytes(b'accepted capture')
        self.mock = patch.object(maintain, 'tracked_files', return_value=set())
        self.tracked = self.mock.start()

    def tearDown(self):
        self.mock.stop()
        self.temp.cleanup()

    def test_preview_and_default_preserve_exports_and_evidence(self):
        maintain.clean(self.lab, exports=True)
        self.assertTrue(self.cache.exists())
        maintain.clean(self.lab, apply=True)
        self.assertTrue(self.cache.exists())
        maintain.clean(self.lab, exports=True, apply=True)
        self.assertFalse(self.cache.exists())
        self.assertEqual(self.asset.read_bytes(), b'accepted asset')
        self.assertEqual(self.capture.read_bytes(), b'accepted capture')
        self.assertTrue((self.work / 'source.sketch').exists())

    def test_tracked_candidate_prevents_all_deletions(self):
        extra = self.lab / '.DS_Store'
        extra.touch()
        self.tracked.return_value = {self.cache / 'export.png'}
        with self.assertRaisesRegex(ValueError, 'tracked'):
            maintain.clean(self.lab, exports=True, apply=True)
        self.assertTrue(extra.exists())
        self.assertTrue(self.cache.exists())

    def test_missing_source_prevents_cache_deletion(self):
        (self.work / 'source.sketch').unlink()
        with self.assertRaisesRegex(ValueError, 'retained source'):
            maintain.clean(self.lab, exports=True, apply=True)
        self.assertTrue(self.cache.exists())

    def test_linked_cache_cannot_delete_external_files(self):
        (self.cache / 'linked.png').symlink_to(self.asset)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            maintain.clean(self.lab, exports=True, apply=True)
        self.assertTrue(self.cache.exists())
        self.assertEqual(self.asset.read_bytes(), b'accepted asset')

    def test_environments_and_linked_directories_are_skipped(self):
        env = self.lab / '.venv/__pycache__'
        env.mkdir(parents=True)
        (env / 'installed.pyc').touch()
        (self.lab / 'linked').symlink_to(self.work, target_is_directory=True)
        maintain.clean(self.lab, apply=True)
        self.assertTrue((env / 'installed.pyc').exists())
        self.assertTrue(self.asset.exists())


if __name__ == '__main__':
    unittest.main()
