"""Independent verification process: adversarial tests, not Builder's verdict.

This deterministic reviewer is deliberately labelled as such. It is not an
independent human or a claim of exhaustive LLM architecture review.
"""
import os
from pathlib import Path
import subprocess
import sys
from autodev.runtime import read, write


def main():
    sid = os.environ["AUTODEV_STAGE"]
    plan = read("development/autodev/M01.json")
    stage = next(s for s in plan["stages"] if s["id"] == sid)
    checks = stage["review_tests"]
    results = []
    for test in checks:
        run = subprocess.run([sys.executable, "-m", "unittest", test, "-v"], capture_output=True, text=True)
        print(run.stdout + run.stderr)
        results.append({"test": test, "passed": run.returncode == 0})
    findings = [{"severity": "blocking", "check": r["test"], "reason": "Adversarial test failed"}
                for r in results if not r["passed"]]
    report = {"role": "review", "kind": "independent-process deterministic adversarial review",
              "verdict": "FAIL" if findings else "PASS", "checks": results, "findings": findings,
              "source_digest": os.environ["AUTODEV_SOURCE_DIGEST"], "nonce": os.environ["AUTODEV_NONCE"],
              "limitations": ["Does not replace independent human/LLM semantic review", "Only configured engineering tests are covered"]}
    path = Path(os.environ["AUTODEV_REPORT"])
    write(path, report)
    path.with_suffix(".md").write_text("# Independent Review\n\n" + report["kind"] + "\n\n" +
                                      "\n".join(f"- {r['test']}: {'PASS' if r['passed'] else 'FAIL'}" for r in results) +
                                      "\n\nLimit: finite adversarial checks, not exhaustive design certification.\n", encoding="utf-8")
    sys.exit(bool(findings))


if __name__ == "__main__":
    main()
