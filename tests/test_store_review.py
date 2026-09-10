import concurrent.futures
import sqlite3
from organization.store import DomainError
from tests.test_store import StoreTests


class StoreReview(StoreTests):
    def test_key_collision_cannot_change_history(self):
        self.send()
        with self.assertRaises(DomainError):
            self.store.transact('different-human','example',{},'one',lambda s:[])
        self.assertEqual(len(self.store.events()), 1)

    def test_concurrent_delivery_records_fact_once(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda n:self.send(), range(8)))
        self.assertTrue(all(x == results[0] for x in results))
        self.assertEqual(len(self.store.events()), 1)

    def test_tampered_event_is_not_a_valid_replay(self):
        self.send()
        with self.store.connect() as db:
            db.execute("UPDATE events SET envelope=replace(envelope,'H1','H9')")
        with self.assertRaises(DomainError): self.store.state()
