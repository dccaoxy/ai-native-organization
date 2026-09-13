from pathlib import Path
from contextlib import closing
import sqlite3
import tempfile
import unittest

from organization.portal_backup import backup,restore,verify


class PortalBackupTests(unittest.TestCase):
    def test_online_backup_verify_and_restore_without_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'portal.sqlite3';copy=root/'backup.sqlite3';restored=root/'restored.sqlite3'
            with closing(sqlite3.connect(source)) as db:
                db.execute('CREATE TABLE evidence (id INTEGER PRIMARY KEY, value TEXT)')
                db.execute("INSERT INTO evidence(value) VALUES ('synthetic')")
                db.execute('PRAGMA journal_mode=WAL')
                db.commit()
                receipt=backup(source,copy)
            self.assertEqual(receipt['integrity_check'],'ok');self.assertGreater(receipt['size'],0)
            self.assertEqual(verify(copy)['integrity_check'],'ok')
            with self.assertRaises(FileExistsError):backup(source,copy)
            restore(copy,restored)
            with closing(sqlite3.connect(restored)) as db:self.assertEqual(db.execute('SELECT value FROM evidence').fetchone()[0],'synthetic')
            with self.assertRaises(FileExistsError):restore(copy,restored)

    def test_missing_or_invalid_database_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            with self.assertRaises(FileNotFoundError):verify(root/'missing.sqlite3')
            invalid=root/'invalid.sqlite3';invalid.write_text('not sqlite',encoding='utf-8')
            with self.assertRaises(sqlite3.DatabaseError):verify(invalid)
