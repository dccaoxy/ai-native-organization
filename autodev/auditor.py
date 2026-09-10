"""Frozen-baseline preservation plus independently rerun compliance checks."""
import os
from pathlib import Path
import subprocess
import sys
from autodev.runtime import Harness, write


def main():
    h = Harness(Path.cwd())
    stage = next(s for s in h.plan["stages"] if s["id"] == os.environ["AUTODEV_STAGE"])
    findings = [{"severity": "blocking", "principle": "Frozen L1/L2", "evidence": p,
                 "resolution": "HUMAN_DECISION_REQUIRED: baseline change"} for p in h.frozen_changes()]
    checks = [{"id": "baseline-preservation", "passed": not findings}]
    for check in stage["principle_checks"]:
        run = subprocess.run([sys.executable, "-m", "unittest", check["test"], "-v"], capture_output=True, text=True)
        print(run.stdout + run.stderr)
        checks.append({**check, "passed": run.returncode == 0})
        if run.returncode:
            findings.append({"severity": "blocking", "principle": check["id"], "evidence": check["test"], "resolution": "Repair and re-audit"})
    report = {"role": "audit", "verdict": "FAIL" if findings else "PASS", "checks": checks,
              "findings": findings, "source_digest": os.environ["AUTODEV_SOURCE_DIGEST"],
              "nonce": os.environ["AUTODEV_NONCE"], "coverage": "M01 engineering invariants only",
              "out_of_scope": ["Human Pilot evidence", "M1 learning efficacy", "M2 value/culture", "Phase 9 completion"]}
    path = Path(os.environ["AUTODEV_REPORT"])
    write(path, report)
    path.with_suffix(".md").write_text("# Architecture / Principle Audit\n\n" + report["verdict"] +
        "\n\n" + "\n".join(f"- {c['id']}: {'PASS' if c['passed'] else 'FAIL'}" for c in checks) +
        "\n\nCoverage: frozen file integrity and listed executable invariants. No assertion that all 101 L2 principles are implemented.\n", encoding="utf-8")
    sys.exit(bool(findings))


if __name__ == "__main__":
    main()
