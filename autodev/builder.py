"""Initial command backend builds checked-in engineering inputs.

A model/agent can supply a separate reviewed build/repair argv adapter. No
credentials, chat history or silently invented implementation are required.
"""
import compileall
import os
import subprocess
import sys
from autodev.runtime import read


def main():
    stage = next(s for s in read("development/autodev/M01.json")["stages"] if s["id"] == os.environ["AUTODEV_STAGE"])
    role = os.environ["AUTODEV_ROLE"]
    if role == "build":
        sys.exit(not all(compileall.compile_dir(p, quiet=1) for p in stage["build_directories"]))
    if role == "test":
        sys.exit(subprocess.call([sys.executable, "-m", "unittest", *stage["tests"], "-v"]))
    print("BLOCKED_ENGINEERING: no unattended code-authoring repair adapter configured; preserve failed evidence for the next worker.")
    sys.exit(2)


if __name__ == "__main__":
    main()
