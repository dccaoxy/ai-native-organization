"""Run real isolated Git/repair/recovery tests and retain their actual result."""
from pathlib import Path
import subprocess
import sys
import time
from autodev.runtime import write


def main():
    started = time.time()
    result = subprocess.run([sys.executable, "-m", "unittest", "tests.test_harness", "-v"], text=True, capture_output=True)
    home = Path("development/autodev/selftest")
    home.mkdir(parents=True, exist_ok=True)
    (home / "tests.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    write(home / "result.json", {"kind":"isolated synthetic engineering fixture; not organization research data",
          "started":started,"finished":time.time(),"exit_code":result.returncode,
          "status":"PASS" if result.returncode == 0 else "FAIL", "suite":"tests.test_harness",
          "evidence":"development/autodev/selftest/tests.log"})
    print(result.stdout + result.stderr)
    sys.exit(result.returncode)


if __name__ == "__main__": main()
