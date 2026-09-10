"""Real disposable Git repositories; all organization actors here are fixtures."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from autodev.runtime import Harness, read, write


ADAPTER = '''import json, os, pathlib, sys
p = pathlib.Path("answer.txt")
role = os.environ["AUTODEV_ROLE"]
if role == "build" and not p.exists(): p.write_text("wrong")
if role == "repair": p.write_text("correct")
if role in ("test", "review", "audit") and p.read_text() != "correct": sys.exit(1)
if role in ("review", "audit"):
 d = dict(verdict="PASS", role=role, source_digest=os.environ["AUTODEV_SOURCE_DIGEST"], nonce=os.environ["AUTODEV_NONCE"], findings=[], checks=["answer equals correct"])
 pathlib.Path(os.environ["AUTODEV_REPORT"]).write_text(json.dumps(d))
'''


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Harness Test")
        self.git("config", "user.email", "harness@example.invalid")
        (self.root / "adapter.py").write_text(ADAPTER)
        (self.root / ".gitignore").write_text(".autodev/\n")
        write(self.root / "development/autodev/baseline.lock.json", {"files": {}})
        self.plan = {"id": "DEMO", "stages": [self.stage("D01"), self.stage("D02", ["D01"]), self.stage("D03", ["D02"], True)]}
        write(self.root / "plan.json", self.plan)
        self.git("add", ".")
        self.git("commit", "-m", "fixture baseline")

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True, text=True).stdout.strip()

    def stage(self, sid, deps=None, gate=False):
        return {"id": sid, "title": "Safe fixture", "dependencies": deps or [],
                "inputs": ["adapter.py"], "outputs": ["answer.txt"], "scope": ["adapter.py", "answer.txt"],
                "exit_criteria": ["answer is correct"], "tests": ["answer equality"],
                "principle_checks": ["no real external actions"], "repair_budget": 2,
                "human_gates": [{"condition": "real_authority", "active": gate}],
                "commands": {r: ["{python}", "adapter.py"] for r in ("build", "test", "review", "audit", "repair")}}

    def harness(self):
        return Harness(self.root, "plan.json")

    def test_repair_auto_advance_gate_resume_and_rollback(self):
        h = self.harness()
        state = h.run()
        self.assertEqual(state["stages"]["D01"]["attempt"], 2)
        self.assertEqual(state["stages"]["D02"]["status"], "PASS")
        self.assertEqual(state["stages"]["D03"]["status"], "HUMAN_DECISION_REQUIRED")
        self.assertEqual(len(self.git("tag").splitlines()), 2)
        tags = self.git("tag")
        self.harness().run()
        self.assertEqual(self.git("tag"), tags)
        head = self.git("rev-parse", "HEAD")
        dest = h.rollback("autodev/DEMO/D01/v1", ".autodev/rollback")
        self.assertEqual((Path(dest) / "answer.txt").read_text(), "correct")
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        restored = Harness(dest, "plan.json")
        restored.run(limit=1)
        self.assertEqual(restored.state["stages"]["D01"]["status"], "PASS")
        artifact = self.root / state["stages"]["D01"]["artifact"]
        self.assertTrue(artifact.is_file())

    def test_timeout_budget_and_missing_receipt_fail_closed(self):
        (self.root / "adapter.py").write_text("pass\n")
        h = self.harness()
        h.run()
        self.assertEqual(h.state["stages"]["D01"]["status"], "BLOCKED_ENGINEERING")
        self.assertEqual(self.git("tag"), "")

    def test_interruption_resumes_without_reusing_stale_review(self):
        h = self.harness()
        h.event("D01", "REVIEW", attempt=1)
        (self.root / "answer.txt").write_text("correct")
        state = self.harness().run(limit=1)
        self.assertEqual(state["stages"]["D01"]["attempt"], 2)
        self.assertEqual(state["stages"]["D01"]["status"], "PASS")

    def test_two_workers_cannot_own_same_checkout(self):
        h = self.harness()
        with h.lease():
            with self.assertRaises(OSError):
                with self.harness().lease():
                    self.fail("second lease must fail")

    def test_dependency_cycle_and_path_escape_rejected(self):
        self.plan["stages"][0]["dependencies"] = ["D02"]
        write(self.root / "plan.json", self.plan)
        with self.assertRaises(ValueError):
            self.harness()
        self.plan["stages"][0]["dependencies"] = []
        self.plan["stages"][0]["outputs"] = ["../escape"]
        write(self.root / "plan.json", self.plan)
        with self.assertRaises(ValueError):
            self.harness()

    def test_frozen_change_enters_human_gate_before_build(self):
        write(self.root / "development/autodev/baseline.lock.json", {"files": {"frozen.md": "bad"}})
        state = self.harness().run()
        self.assertEqual(state["stages"]["D01"]["status"], "HUMAN_DECISION_REQUIRED")
        self.assertFalse((self.root / "answer.txt").exists())

    def test_reviewer_cannot_mutate_candidate_and_pass(self):
        (self.root / "answer.txt").write_text("correct")
        (self.root / "adapter.py").write_text(ADAPTER + '\nif role == "review": p.write_text("tampered")\n')
        state = self.harness().run()
        self.assertEqual(state["stages"]["D01"]["status"], "BLOCKED_ENGINEERING")
        self.assertEqual(self.git("tag"), "")

    def test_budget_persists_across_workers(self):
        h = self.harness()
        h.event("D01", "FAILED", attempt=3)
        self.harness().run()
        self.assertFalse((self.root / "answer.txt").exists())
        self.assertEqual(self.git("tag"), "")

    def test_actual_command_timeout_is_visible(self):
        (self.root / "adapter.py").write_text("import time\ntime.sleep(5)\n")
        self.plan['stages'][0]['timeout_seconds'] = 0.05
        self.plan['stages'][0]['repair_budget'] = 0
        write(self.root / 'plan.json', self.plan)
        state = self.harness().run()
        receipt = read(self.root / 'development/autodev/runs/DEMO/D01/1/build.receipt.json')
        self.assertEqual(receipt['exit_code'], 124)
        self.assertEqual(state['stages']['D01']['status'], 'BLOCKED_ENGINEERING')

    def test_crash_after_checkpoint_commit_before_tag_recovers(self):
        (self.root / 'answer.txt').write_text('correct')
        h = self.harness()
        original = h.git
        def crash(*args, **kwargs):
            if args[:2] == ('tag','-a'):
                raise RuntimeError('injected worker death')
            return original(*args, **kwargs)
        h.git = crash
        with self.assertRaises(RuntimeError): h.run(limit=1)
        head = self.git('rev-parse', 'HEAD')
        result = self.harness().run(limit=1)
        self.assertEqual(result['stages']['D01']['commit'], head)
        self.assertEqual(result['stages']['D01']['status'], 'PASS')


if __name__ == "__main__":
    unittest.main()
