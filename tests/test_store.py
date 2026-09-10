from pathlib import Path
import tempfile
import unittest
from organization.store import Store


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / 'state.sqlite3'
        self.store = Store(self.path)

    def tearDown(self): self.tmp.cleanup()

    def send(self, key='one'):
        return self.store.transact('H1','example',{},key,lambda s:[{'type':'FixtureEvent','authority':'simulation fixture','changes':{'Human':{'H1':{'id':'H1'}}}}])

    def test_persistence_idempotency_and_replay(self):
        first = self.send()
        self.assertEqual(self.send(), first)
        reopened = Store(self.path)
        self.assertEqual(reopened.state(), first['state'])
        self.assertEqual(len(reopened.events()), 1)
        self.assertEqual(Store.replay(reopened.events()), reopened.state())

    def test_multiple_formal_events_are_atomic(self):
        def failure(state):
            raise RuntimeError('injected domain interruption')
        with self.assertRaises(RuntimeError): self.store.transact('H1','bad',{},'bad',failure)
        self.assertEqual(self.store.events(), [])
        self.send('bad')
        self.assertEqual(len(self.store.events()), 1)
