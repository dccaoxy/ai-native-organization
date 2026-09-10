"""Offline contract tests use explicit fixtures, never claim live model evidence."""
import unittest
from unittest.mock import patch
from autodev.codex_adapter import validate_edits, invoke
from autodev.runtime import write
from tests import test_harness


class CodexAdapterTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_harness.HarnessTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.h = self.fixture.harness()
        self.stage = self.h.plan["stages"][0]
        self.stage["model_write_paths"] = ["answer.txt"]

    def proposal(self, path="answer.txt"):
        return {"status": "PROPOSED", "edits": [{"path": path, "content": "correct"}]}

    def test_allowed_write_and_no_implicit_authority(self):
        self.assertEqual(validate_edits(self.h, self.stage, self.proposal())[0][1], "correct")
        del self.stage["model_write_paths"]
        with self.assertRaises(ValueError):
            validate_edits(self.h, self.stage, self.proposal())

    def test_escape_protected_scope_and_duplicates(self):
        for path in ["../outside", ".git/config", "autodev/runtime.py", "AGENTS.md", ".env", "development/x", "other.txt"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                validate_edits(self.h, self.stage, self.proposal(path))
        proposal = self.proposal()
        proposal["edits"] *= 2
        with self.assertRaises(ValueError):
            validate_edits(self.h, self.stage, proposal)

    def test_frozen_output_rejected_even_in_scope(self):
        write(self.h.home / "baseline.lock.json", {"files": {"answer.txt": "frozen"}})
        with self.assertRaises(ValueError):
            validate_edits(self.h, self.stage, self.proposal())

    def test_missing_cli_and_active_gate(self):
        with patch.dict("os.environ", {"AUTODEV_CODEX_EXECUTABLE": "codex"}):
            self.stage["human_gates"][0]["active"] = True
            self.assertEqual(invoke(self.h, self.stage, "build")["status"], "HUMAN_DECISION_REQUIRED")
        with patch.dict("os.environ", {}, clear=True), patch("shutil.which", return_value=None):
            with self.assertRaises(RuntimeError):
                invoke(self.h, self.stage, "build")

    def test_model_gate_is_durable_and_does_not_trigger_repair(self):
        (self.h.root / "adapter.py").write_text('''import json, os, pathlib
d = dict(verdict="HUMAN_DECISION_REQUIRED", summary="Need purpose decision", role=os.environ["AUTODEV_ROLE"], nonce=os.environ["AUTODEV_NONCE"], source_digest=os.environ["AUTODEV_SOURCE_DIGEST"])
pathlib.Path(os.environ["AUTODEV_REPORT"]).write_text(json.dumps(d))
raise SystemExit(3)
''')
        self.h.run()
        item = self.h.state["stages"]["D01"]
        self.assertEqual(item["status"], "HUMAN_DECISION_REQUIRED")
        nonce = item["model_gate"]
        restored = self.fixture.harness()
        restored.run()
        self.assertEqual(restored.state["stages"]["D01"]["model_gate"], nonce)
        self.assertEqual(restored.state["stages"]["D01"]["attempt"], 1)
        self.assertFalse(any(e["status"] == "REPAIR" for e in restored.state["events"]))
        self.assertEqual(self.fixture.git("tag"), "")


if __name__ == "__main__":
    unittest.main()
