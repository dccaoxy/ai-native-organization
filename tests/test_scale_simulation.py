from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import tempfile
import unittest
from organization.core import Organization
from organization.scale_simulation import scenario, verify
from organization.store import DomainError


class ScaleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "test.sqlite3"
        self.org = Organization(self.path)

    def test_scaled_paths_reopen_and_replay(self):
        scenario(self.org.execute, tasks=3)
        events = self.org.store.events()
        state = self.org.store.state()
        self.assertTrue(all(verify(state, events, tasks=3).values()))
        reopened = Organization(self.path)
        self.assertEqual(reopened.store.state(), state)
        scenario(reopened.execute, tasks=3)
        self.assertEqual(reopened.store.events(), events)

    def test_simultaneous_duplicate_receipts_are_exactly_once(self):
        body = dict(actor="SIMULATOR", command="register_human", data={"id": "H1", "display_name": "Synthetic Human"}, idempotency_key="concurrent")
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(lambda _: self.org.execute(**body), range(24)))
        self.assertTrue(all(r == results[0] for r in results))
        self.assertEqual(len(self.org.store.events()), 1)
        with self.assertRaises(DomainError):
            self.org.execute(**dict(body, data={"id": "H2", "display_name": "Conflicting payload"}))
        self.assertEqual(len(self.org.store.events()), 1)

    def test_rejected_cross_task_selection_adds_no_event(self):
        scenario(self.org.execute, tasks=3)
        self.open_task()
        before = self.org.store.events()
        with self.assertRaises(DomainError):
            self.org.execute("H9", "select", {"id": "bad", "task_id": "parallel", "return_id": "R1-0", "rationale": "Invalid cross-task fixture"}, "invalid")
        self.assertEqual(self.org.store.events(), before)

    def open_task(self):
        self.org.execute("H0", "create_task", {"id": "parallel", "primary_goal": "G0", "expected_output": "Synthetic concurrent attempts", "acceptance_criteria": "Ownership preserved", "boundary": ["read"], "execution_mode": "parallel", "review_authority": "H8", "acceptance_authority": "H0", "selection_authority": "H9"}, "parallel-task")
        self.org.execute("H0", "publish", {"task_id": "parallel"}, "parallel-publish")

    def test_simultaneous_claims_preserve_separate_execution_owners(self):
        scenario(self.org.execute, tasks=1)
        self.open_task()
        def claim(n):
            return self.org.execute(f"A{n % 10}", "claim", {"id": f"parallel-{n}", "task_id": "parallel", "hau_id": f"U{n % 10}"}, f"claim-{n}")
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(claim, range(20)))
        state = self.org.store.state()
        attempts = [e for e in state["Execution"].values() if e["task_id"] == "parallel"]
        self.assertEqual(len(attempts), 20)
        self.assertTrue(all(e["accountable_owner"] == state["HAU"][e["hau_id"]]["human_id"] for e in attempts))

    def test_fixture_parameters_fail_early(self):
        with self.assertRaises(ValueError):
            scenario(self.org.execute, tasks=0)
        self.assertEqual(self.org.store.events(), [])

    def test_goal_challenge_with_live_attempt_and_replay(self):
        scenario(self.org.execute, tasks=3, with_goal_challenge=True)
        events = self.org.store.events()
        self.assertTrue(all(verify(self.org.store.state(), events, tasks=3, with_goal_challenge=True).values()))
        scenario(self.org.execute, tasks=3, with_goal_challenge=True)
        self.assertEqual(self.org.store.events(), events)
