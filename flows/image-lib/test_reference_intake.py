import importlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
import save_reference
import studio


class ReferenceIntakeTests(unittest.TestCase):
    def test_records_declared_provider_without_inventing_model_or_local_path(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);design=root/'example-01';design.mkdir()
            (design/'image-prompt.md').write_text('A specified UI with native control intent.')
            source=root/'generated.png';Image.new('RGB',(406,776),'white').save(source)
            with patch.object(save_reference,'HERE',root):
                save_reference.save('example-01',source,provider='external-generator')
                with self.assertRaises(FileExistsError):
                    save_reference.save('example-01',source,provider='another-generator')
            receipt=json.loads((design/'generation.json').read_text())
            self.assertEqual(receipt['provider'],'external-generator')
            self.assertEqual(receipt['model'],'not recorded')
            self.assertNotIn(td,json.dumps(receipt))
            self.assertEqual(source.read_bytes(),(design/'reference.png').read_bytes())

    def test_missing_prompt_does_not_leave_partial_reference(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);design=root/'example-01';design.mkdir()
            source=root/'generated.png';Image.new('RGB',(20,40),'white').save(source)
            with patch.object(save_reference,'HERE',root), self.assertRaises(FileNotFoundError):
                save_reference.save('example-01',source,provider='external-generator')
            self.assertFalse((design/'reference.png').exists())

    def test_bridge_uses_shared_environment_configuration(self):
        try:
            with patch.dict(os.environ,{'BEAUTY_BRIDGE':'http://127.0.0.1:18169'}):
                importlib.reload(studio)
                self.assertEqual(studio.BRIDGE,'http://127.0.0.1:18169')
        finally:
            importlib.reload(studio)


if __name__=='__main__':unittest.main()
