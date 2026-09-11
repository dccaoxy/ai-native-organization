import tempfile,unittest
from pathlib import Path
from tests import test_core as core
from organization.workspace import prepare
from organization.store import Store

class WorkspaceTests(unittest.TestCase):
    def test_consistent_seed_and_restart_preserve_source_and_key(self):
        f=core.CoreTests();f.setUp()
        try:
            f.task();original=f.org.store.events()
            with tempfile.TemporaryDirectory() as tmp:
                db,key=prepare(tmp,f.org.store.path)
                self.assertEqual(Store(db).events(),original)
                self.assertEqual(f.org.store.events(),original)
                secret=key.read_text();self.assertGreaterEqual(len(secret),43)
                prepare(tmp);self.assertEqual(key.read_text(),secret)
                with self.assertRaises(ValueError):prepare(tmp,f.org.store.path)
                self.assertEqual(Store(db).events(),original)
        finally:f.tearDown()

    def test_bad_source_does_not_create_or_overwrite_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'unified'
            with self.assertRaises(ValueError):prepare(dest,Path(tmp)/'missing.db')
            self.assertFalse((dest/'workspace.sqlite3').exists())
