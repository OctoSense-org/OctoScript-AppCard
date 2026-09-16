"""Repository-relative pipeline and isolated native dependency locations."""
from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = Path(os.environ.get('OCTOS_APPCARD_PIPELINE', ROOT.parents[1])).resolve()
IMAGE = PIPELINE / 'lab/image-to-appcard'
NATIVE_ROOT = Path(os.environ.get('OCTOS_MAIL_NATIVE_ROOT', ROOT / 'runtime/native')).resolve()
sys.path.insert(0, str(IMAGE))
sys.path.insert(0, str(ROOT / 'service'))
