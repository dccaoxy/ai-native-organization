"""Opt-in live account smoke test in a disposable, isolated Git repository."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from autodev.runtime import Harness, write


def main():
    source = Path(__file__).resolve().parent.parent
    os.environ["PYTHONPATH"] = str(source)
    with tempfile.TemporaryDirectory(prefix="codex-smoke-") as directory:
        root = Path(directory)
        def git(*args):
            return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
        git("init", "-b", "main")
        git("config", "user.name", "AutoDev isolated smoke")
        git("config", "user.email", "smoke@example.invalid")
        (root / "AGENTS.md").write_text("This is an isolated synthetic adapter test. Only propose answer.txt containing exactly 42 followed by a newline. No external actions.\n")
        (root / "verify.py").write_text('''import os, pathlib, json
assert pathlib.Path("answer.txt").read_text() == "42\\n"
if os.environ["AUTODEV_ROLE"] in ("review", "audit"):
 d = dict(verdict="PASS", role=os.environ["AUTODEV_ROLE"], source_digest=os.environ["AUTODEV_SOURCE_DIGEST"], nonce=os.environ["AUTODEV_NONCE"], findings=[], checks=["isolated fixture equals 42; no organization acceptance claimed"])
 pathlib.Path(os.environ["AUTODEV_REPORT"]).write_text(json.dumps(d))
''')
        write(root / "development/autodev/baseline.lock.json", {"files": {}})
        stage = dict(id="D01", title="Live Codex adapter synthetic smoke", dependencies=[],
                     inputs=["AGENTS.md", "verify.py"], outputs=["answer.txt"],
                     scope=["answer.txt"], model_write_paths=["answer.txt"],
                     exit_criteria=["answer.txt contains exactly 42 and newline"], tests=["verify.py"],
                     principle_checks=["isolated synthetic fixture only"], human_gates=[],
                     timeout_seconds=180, repair_budget=1,
                     commands={r: [sys.executable, "-m", "autodev.codex_adapter"] if r in ("build", "repair") else [sys.executable, "verify.py"] for r in ("build", "repair", "test", "review", "audit")})
        gate = dict(stage, id="D02", dependencies=["D01"], human_gates=[{"condition": "synthetic demonstration of human authority gate", "active": True}])
        write(root / "plan.json", {"id": "CODEXSMOKE", "stages": [stage, gate]})
        git("add", ".")
        git("commit", "-m", "Isolated live smoke baseline")
        h = Harness(root, "plan.json")
        state = h.run()
        passed = state["stages"]["D01"]["status"] == "PASS"
        if passed:
            before = git("tag")
            Harness(root, "plan.json").run()
            assert git("tag") == before
        receipt = {"kind": "live_codex_account_smoke", "model_call_verified": passed,
                   "stages": state["stages"], "resume_no_duplicate_tags": passed,
                   "scope": "disposable synthetic Git repository; not M01 acceptance",
                   "checkpoint_retention": "disposable commits/tags; retained artifact copied below"}
        if passed:
            import shutil
            artifact = root / state["stages"]["D01"]["artifact"]
            destination = source / "development/autodev/codex-smoke-artifact.zip"
            shutil.copyfile(artifact, destination)
            receipt["retained_artifact"] = destination.relative_to(source).as_posix()
        write(source / "development/autodev/CODEX_SMOKE.json", receipt)
        print("Live model smoke:", "PASS" if passed else "BLOCKED_ENGINEERING")
        return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
