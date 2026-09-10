"""Local-only cumulative tests and integrated synthetic M02 acceptance."""
import subprocess
import sys


def main():
    for command in (
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-q'],
        [sys.executable, '-m', 'organization.scale_simulation', '--with-goal-challenge', '--output', '.autodev/m02-final'],
    ):
        result = subprocess.run(command)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
