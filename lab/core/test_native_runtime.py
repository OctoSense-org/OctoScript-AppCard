"""Guard the shared runtime boundary and preserve in-progress source work."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from core import native_runtime


class RuntimeLockTests(unittest.TestCase):
    def test_rejects_another_runtime_repository(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(native_runtime, 'APPCARDS', Path(temp).resolve()):
            (Path(temp)/'native-runtime.lock.json').write_text(json.dumps({
                'schema_version': 1, 'url': 'https://example.com/other.git', 'revision': 'a'*40}))
            with self.assertRaisesRegex(ValueError, 'Octoscript-Makepad'):
                native_runtime.runtime_lock()

    def test_requires_an_immutable_revision(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(native_runtime, 'APPCARDS', Path(temp).resolve()):
            (Path(temp)/'native-runtime.lock.json').write_text(json.dumps({
                'schema_version': 1, 'url': native_runtime.RUNTIME_URL, 'revision': 'main'}))
            with self.assertRaisesRegex(ValueError, 'full Git commit'):
                native_runtime.runtime_lock()

    def test_dirty_runtime_is_not_changed_or_fetched(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            runtime = root/'octoscript-makepad'
            runtime.mkdir()
            subprocess.run(['git', 'init', '--quiet', str(runtime)], check=True)
            work = runtime/'in-progress.txt'
            work.write_text('Preserve this work.\n')
            locked = {'schema_version': 1, 'url': native_runtime.RUNTIME_URL, 'revision': 'a'*40}
            with patch.object(native_runtime, 'runtime_lock', return_value=locked):
                with self.assertRaisesRegex(RuntimeError, 'Preserving local runtime edits'):
                    native_runtime.prepare(root, update=True, cache=root)
            self.assertEqual(work.read_text(), 'Preserve this work.\n')
            self.assertFalse((runtime/'.git/FETCH_HEAD').exists())

    def test_runtime_sources_cannot_be_nested_under_appcards(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(native_runtime, 'APPCARDS', Path(temp).resolve()):
            with self.assertRaisesRegex(RuntimeError, 'outside AppCards'):
                native_runtime.prepare(Path(temp)/'makepad')


if __name__ == '__main__':
    unittest.main()
