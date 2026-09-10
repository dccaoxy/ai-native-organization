"""Repository state is the protocol; a process is only a replaceable worker.

Commands are trusted repository configuration, not a security sandbox. Cloud
jobs must run reviewed default-branch code with explicitly scoped credentials.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time
import uuid
import zipfile
from contextlib import contextmanager


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def file_hash(path):
    data = Path(path).read_bytes()
    # Git text checkout may convert CRLF on Windows. Bind semantic text bytes
    # consistently across Work/Linux; binary artifacts retain exact byte hashes.
    try:
        data.decode("utf-8")
        data = data.replace(b"\r\n", b"\n")
    except UnicodeDecodeError:
        pass
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


class Harness:
    def __init__(self, root, plan="development/autodev/M01.json"):
        self.root = Path(root).resolve()
        self.plan_path = self.safe(plan)
        self.plan = read(self.plan_path)
        self.home = self.root / "development/autodev"
        self.state_path = self.home / (self.plan["id"] + ".state.json")
        self.state = read(self.state_path) if self.state_path.exists() else {
            "schema_version": 1, "plan": self.plan["id"], "stages": {}, "events": []}
        self.validate()

    def safe(self, value):
        path = (self.root / value).resolve()
        if not path.is_relative_to(self.root) or path == self.root:
            raise ValueError("Path must remain inside repository: " + str(value))
        return path

    def git(self, *args, check=True):
        return subprocess.run(["git", *args], cwd=self.root, text=True,
                              encoding="utf-8", capture_output=True, check=check).stdout.strip()

    def validate(self):
        seen = set()
        for stage in self.plan["stages"]:
            sid = stage["id"]
            if not sid.replace("-", "").isalnum() or sid in seen:
                raise ValueError("Invalid or duplicate stage id")
            if not set(stage["dependencies"]).issubset(seen):
                raise ValueError("Dependencies must precede stage")
            seen.add(sid)
            for field in ("inputs", "outputs", "exit_criteria", "tests",
                          "principle_checks", "human_gates", "scope"):
                if field not in stage:
                    raise ValueError("Missing stage field: " + field)
            for field in ("inputs", "outputs", "scope"):
                for path in stage[field]:
                    self.safe(path)
            for role in ("build", "test", "review", "audit", "repair"):
                if not isinstance(stage["commands"].get(role), list):
                    raise ValueError("Commands must be argv arrays")
            if not stage["exit_criteria"] or not stage["tests"] or not stage["principle_checks"]:
                raise ValueError("Empty acceptance is not permitted")
            if stage.get("repair_budget", 2) not in range(0, 6):
                raise ValueError("Repair budget must be bounded 0..5")

    @contextmanager
    def lease(self):
        # OS advisory lock is released even if the worker dies. No time-based
        # stealing from a slow worker. CI supplies repository-wide concurrency.
        path = Path(self.git("rev-parse", "--git-common-dir"))
        if not path.is_absolute():
            path = self.root / path
        with (path / "autodev.lock").open("a+b") as lock:
            lock.seek(0)
            lock.write(b"0")
            lock.flush()
            lock.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                yield
            finally:
                lock.seek(0)
                if os.name == "nt":
                    msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    fcntl.flock(lock, fcntl.LOCK_UN)

    def event(self, sid, status, **details):
        self.state["events"].append({"sequence": len(self.state["events"]) + 1,
                                     "stage": sid, "status": status,
                                     "time": time.time(), **details})
        self.state["stages"].setdefault(sid, {}).update(status=status, **details)
        write(self.state_path, self.state)

    def manifest(self, stage):
        files = set()
        for name in stage["inputs"] + stage["outputs"] + stage["scope"] + [str(self.plan_path.relative_to(self.root))]:
            path = self.safe(name)
            if path.is_file():
                files.add(path)
            elif path.is_dir():
                files.update(p for p in path.rglob("*") if p.is_file())
        return {p.relative_to(self.root).as_posix(): file_hash(p)
                for p in sorted(files) if "__pycache__" not in p.parts
                and p.suffix not in (".pyc", ".tmp")}

    def frozen_changes(self):
        lock = self.home / "baseline.lock.json"
        if not lock.exists():
            return ["Missing baseline lock"]
        expected = read(lock)
        # Verify against the original Git objects too: editing both the baseline
        # and its manifest must not manufacture compliance.
        failures = []
        for name, sha in expected["files"].items():
            path = self.safe(name)
            if not path.exists() or file_hash(path) != sha:
                failures.append(name)
            if expected.get('source_commit'):
                original = subprocess.run(['git','show',expected['source_commit'] + ':' + name],
                                          cwd=self.root, capture_output=True)
                original_hash = hashlib.sha256(original.stdout.replace(b'\r\n', b'\n')).hexdigest()
                if original.returncode or original_hash != sha:
                    failures.append('Baseline provenance mismatch: ' + name)
        return failures

    def command(self, stage, role, attempt, source_digest):
        argv = stage["commands"][role]
        if not argv:
            return {"ok": False, "reason": "No " + role + " adapter configured"}
        argv = [sys.executable if part == "{python}" else part for part in argv]
        run = self.home / "runs" / self.plan["id"] / stage["id"] / str(attempt)
        run.mkdir(parents=True, exist_ok=True)
        report = run / (role + ".json")
        nonce = uuid.uuid4().hex
        env = dict(os.environ, AUTODEV_STAGE=stage["id"], AUTODEV_ROLE=role,
                   AUTODEV_REPORT=str(report), AUTODEV_SOURCE_DIGEST=source_digest,
                   AUTODEV_NONCE=nonce, PYTHONUTF8="1")
        start = time.time()
        try:
            result = subprocess.run(argv, cwd=self.root, env=env, capture_output=True,
                                    encoding="utf-8", errors="replace", timeout=stage.get("timeout_seconds", 120))
            code, output = result.returncode, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            code, output = 124, "Adapter exceeded stage timeout; worker terminated."
        except OSError as exc:
            code, output = 127, str(exc)
        (run / (role + ".log")).write_text(output, encoding="utf-8")
        receipt = {"ok": code == 0, "exit_code": code, "argv": argv,
                   "source_digest": source_digest, "started": start, "finished": time.time()}
        if role in ("review", "audit"):
            data = read(report) if report.exists() else {}
            receipt["ok"] = receipt["ok"] and all((
                data.get("verdict") == "PASS", data.get("role") == role,
                data.get("source_digest") == source_digest, data.get("nonce") == nonce,
                isinstance(data.get("findings"), list), bool(data.get("checks"))))
            receipt["report"] = data
        write(run / (role + ".receipt.json"), receipt)
        return receipt

    def project(self):
        if self.plan["id"] != "M01":
            return
        entries = self.state["stages"]
        rows = [f"| {s['id']} {s['title']} | {entries.get(s['id'], {}).get('status', 'PENDING')} | {entries.get(s['id'], {}).get('tag', '')} |"
                for s in self.plan["stages"]]
        table = "| Stage | Status | Checkpoint tag |\n|---|---|---|\n" + "\n".join(rows)
        block = "<!-- AUTODEV:START -->\n## AutoDev repository projection\n\n" + table + (
            "\n\nSource: `development/autodev/M01.state.json`. "
            "Simulation evidence is not Human Pilot or E01–E08 evidence. "
            "Phase 9 requires real Humans, time and experimental results.\n<!-- AUTODEV:END -->")
        paths = ["development/CURRENT_STATE.md", "development/NEXT_ACTIONS.md",
                 "development/MILESTONES.md", "development/milestones/M01_MINIMUM_ORGANIZATION.md",
                 "development/autodev/DASHBOARD.md"]
        for name in paths:
            path = self.root / name
            old = path.read_text(encoding="utf-8") if path.exists() else "# AutoDev Dashboard\n"
            if "<!-- AUTODEV:START -->" in old:
                before, tail = old.split("<!-- AUTODEV:START -->", 1)
                _, after = tail.split("<!-- AUTODEV:END -->", 1)
                new = before + block + after
            else:
                new = old.rstrip() + "\n\n" + block + "\n"
            path.write_text(new, encoding="utf-8")

    def checkpoint(self, stage):
        sid = stage["id"]
        item = self.state["stages"][sid]
        tag = item["tag"]
        exists = self.git("rev-parse", "--verify", "refs/tags/" + tag, check=False)
        if not exists:
            self.project()
            paths = stage["scope"] + ["development/autodev"]
            if self.plan["id"] == "M01":
                paths += ["development/CURRENT_STATE.md", "development/NEXT_ACTIONS.md",
                          "development/MILESTONES.md", "development/milestones/M01_MINIMUM_ORGANIZATION.md"]
            paths = [p for p in paths if self.safe(p).exists()]
            if self.git("diff", "--cached", "--name-only"):
                raise RuntimeError("Index is not empty; do not mix unrelated staged work")
            self.git("add", "--", *paths)
            # If a worker died after commit but before tag, recognize its durable
            # marker rather than creating a duplicate commit.
            marker = "autodev: " + tag
            if self.git("log", "-1", "--format=%s") != marker:
                self.git("commit", "--allow-empty", "-m", marker)
            self.git("tag", "-a", tag, "-m", "PASS evidence: " + item["source_digest"])
        commit = self.git("rev-list", "-n", "1", tag)
        lineage = subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=self.root)
        if lineage.returncode:
            raise RuntimeError("Unexpected checkpoint lineage")
        self.event(sid, "PASS", commit=commit)
        self.project()

    def flush(self):
        self.project()
        paths = ["development/autodev"]
        if self.plan["id"] == "M01":
            paths += ["development/CURRENT_STATE.md", "development/NEXT_ACTIONS.md",
                      "development/MILESTONES.md", "development/milestones/M01_MINIMUM_ORGANIZATION.md"]
        if self.git("diff", "--cached", "--name-only"):
            raise RuntimeError("Index contains unrelated changes")
        self.git("add", "--", *paths)
        if self.git("diff", "--cached", "--name-only"):
            self.git("commit", "-m", "chore(autodev): persist recovery state and projections")

    def run(self, limit=None):
        with self.lease():
            self.state = read(self.state_path) if self.state_path.exists() else self.state
            completed = 0
            for stage in self.plan["stages"]:
                sid = stage["id"]
                item = self.state["stages"].get(sid, {})
                if item.get("status") == "PASS":
                    continue
                if item.get("status") == "CHECKPOINT_PENDING":
                    if digest(self.manifest(stage)) != item["source_digest"]:
                        self.event(sid, "BLOCKED_ENGINEERING", reason="Candidate changed before checkpoint recovery")
                        break
                    self.checkpoint(stage)
                    completed += 1
                    if limit and completed >= limit:
                        break
                    continue
                if not all(self.state["stages"].get(dep, {}).get("status") == "PASS" for dep in stage["dependencies"]):
                    self.event(sid, "BLOCKED_ENGINEERING", reason="Dependency has not passed")
                    break
                gates = [g for g in stage["human_gates"] if g["active"]]
                changed = self.frozen_changes()
                if gates or changed:
                    self.event(sid, "HUMAN_DECISION_REQUIRED", gates=gates, frozen_changes=changed)
                    break
                missing = [p for p in stage["inputs"] if not self.safe(p).exists()]
                if missing:
                    self.event(sid, "BLOCKED_ENGINEERING", reason="Missing engineering inputs", missing=missing)
                    break
                # Interrupted attempts consume budget, and resume starts at Build:
                # earlier PASS receipts cannot approve a new candidate.
                attempt = item.get("attempt", 0)
                success = False
                while attempt <= stage.get("repair_budget", 2):
                    attempt += 1
                    self.event(sid, "BUILD", attempt=attempt, worker=socket.gethostname())
                    ok = self.command(stage, "build", attempt, "building")["ok"]
                    manifest = self.manifest(stage)
                    source = digest(manifest)
                    for role in ("test", "review", "audit"):
                        if not ok:
                            break
                        self.event(sid, role.upper(), attempt=attempt)
                        ok = self.command(stage, role, attempt, source)["ok"]
                        if self.manifest(stage) != manifest:
                            ok = False
                            self.event(sid, "FAILED", reason=role + " changed candidate")
                    ok = ok and all(self.safe(p).exists() for p in stage["outputs"])
                    if ok and not self.frozen_changes():
                        artifact = self.home / "runs" / self.plan["id"] / sid / str(attempt) / "artifact.zip"
                        with zipfile.ZipFile(artifact, "w", zipfile.ZIP_DEFLATED) as archive:
                            archive.writestr("manifest.json", canonical(manifest))
                            for name in manifest:
                                archive.write(self.safe(name), name)
                        tag = f"autodev/{self.plan['id']}/{sid}/v1"
                        self.event(sid, "CHECKPOINT_PENDING", source_digest=source, tag=tag,
                                   artifact=artifact.relative_to(self.root).as_posix(),
                                   artifact_sha256=hashlib.sha256(artifact.read_bytes()).hexdigest())
                        self.checkpoint(stage)
                        success = True
                        completed += 1
                        break
                    self.event(sid, "FAILED", attempt=attempt, reason="Build/test/review/audit/output failure")
                    if attempt <= stage.get("repair_budget", 2):
                        self.event(sid, "REPAIR", attempt=attempt)
                        if not self.command(stage, "repair", attempt, source)["ok"]:
                            break
                if not success:
                    self.event(sid, "BLOCKED_ENGINEERING", reason="Repair budget exhausted or repair adapter unavailable")
                    break
                if limit and completed >= limit:
                    break
            self.flush()
        return self.state

    def rollback(self, tag, destination):
        if not tag.startswith("autodev/") or not self.git("tag", "--list", tag):
            raise ValueError("Rollback must target an existing AutoDev checkpoint")
        target = self.safe(destination)
        if target.exists():
            raise ValueError("Rollback destination must be new")
        # Non-destructive: create a new detached recovery worktree; never reset,
        # delete events, replace tags, or force-push the active line of history.
        self.git("worktree", "add", "--detach", str(target), tag)
        return str(target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["run", "status", "rollback"])
    parser.add_argument("--plan", default="development/autodev/M01.json")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--tag")
    parser.add_argument("--destination")
    args = parser.parse_args()
    harness = Harness(Path.cwd(), args.plan)
    if args.command == "run":
        result = harness.run(args.limit)
    elif args.command == "rollback":
        result = harness.rollback(args.tag, args.destination)
    else:
        result = harness.state
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
