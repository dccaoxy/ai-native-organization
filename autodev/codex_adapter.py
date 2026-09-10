"""ChatGPT-authenticated Codex proposes edits; the harness owns writes and PASS.

No account cache or raw model transcript is copied to repository evidence.
Run only trusted plans. Read-only Codex plus validated write paths is defense in
depth, not isolation from malicious code; cloud workers require OS isolation.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from autodev.runtime import Harness, digest, read, write


SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "status": {"type": "string", "enum": ["PROPOSED", "BLOCKED_ENGINEERING", "HUMAN_DECISION_REQUIRED"]},
        "summary": {"type": "string"},
        "edits": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
            "required": ["path", "content"]}},
    },
    "required": ["status", "summary", "edits"],
}


def validate_edits(harness, stage, proposal):
    if proposal.get("status") != "PROPOSED" or not isinstance(proposal.get("edits"), list):
        raise ValueError("Expected a proposed edit list")
    allowed = stage.get("model_write_paths", [])
    if not allowed:
        raise ValueError("Stage must explicitly declare model_write_paths")
    protected = {".git", ".github", ".codex", ".agents", "autodev", "development"}
    frozen = read(harness.home / "baseline.lock.json")["files"]
    validated, seen = [], set()
    for edit in proposal["edits"]:
        name = edit["path"]
        path = harness.safe(name)
        relative = path.relative_to(harness.root).as_posix()
        # Reject aliases and links before writes, including links that resolve in-root.
        original = harness.root / name
        if Path(name).is_absolute() or ".." in Path(name).parts or "\\" in name:
            raise ValueError("Non-canonical edit path")
        if any(p.is_symlink() for p in [original, *original.parents]):
            raise ValueError("Symlink edits are forbidden")
        if Path(relative).parts[0] in protected or Path(relative).name in ("AGENTS.md", ".env", "auth.json") or Path(relative).name.startswith(".env.") or relative in frozen:
            raise ValueError("Protected edit path: " + relative)
        def covered(entries):
            return any(relative == p.rstrip("/") or relative.startswith(p.rstrip("/") + "/") for p in entries)
        if not covered(allowed) or not covered(stage["scope"]):
            raise ValueError("Edit outside approved stage scope: " + relative)
        if relative in seen or not isinstance(edit["content"], str):
            raise ValueError("Duplicate path or non-text content")
        seen.add(relative)
        validated.append((path, edit["content"]))
    return validated


def invoke(harness, stage, role):
    executable = os.environ.get("AUTODEV_CODEX_EXECUTABLE") or shutil.which("codex")
    if not executable:
        raise RuntimeError("Codex CLI missing on this runner")
    if role not in ("build", "repair"):
        raise ValueError("Codex adapter supports build/repair only")
    if harness.frozen_changes() or any(g.get("active") for g in stage["human_gates"]):
        return {"status": "HUMAN_DECISION_REQUIRED", "summary": "Frozen baseline or active stage gate", "edits": []}
    # Ignore personal plugins/config for reproducible automation, retaining saved auth.
    prompt = (
        "Act as AutoDev Builder. Read AGENTS.md and the stage inputs from this repository. "
        "Use read-only tools to inspect files and prior failure reports. Do not change files, "
        "commit, access credentials, use external company systems, or claim stage PASS. "
        "Return complete UTF-8 file replacements only for model_write_paths within scope. "
        "Preserve frozen semantics and acceptance tests. Request HUMAN_DECISION_REQUIRED "
        "for Purpose/Authority/Risk or frozen changes; use BLOCKED_ENGINEERING for technical "
        "obstacles. Existing correct files need no edits. Never include secrets or private "
        "reasoning in the response. Role: " + role + "\nStage:\n" + json.dumps(stage, ensure_ascii=False)
    )
    with tempfile.TemporaryDirectory(prefix="autodev-codex-") as directory:
        folder = Path(directory)
        schema, answer = folder / "schema.json", folder / "answer.json"
        write(schema, SCHEMA)
        argv = [executable, "exec", "--ignore-user-config", "--ephemeral", "--sandbox", "read-only",
                "--color", "never", "--cd", str(harness.root), "--output-schema", str(schema),
                "--output-last-message", str(answer), "-"]
        # Parent harness timeout remains larger than the model invocation timeout.
        timeout = max(1, stage.get("timeout_seconds", 120) - 15)
        result = subprocess.run(argv, input=prompt, text=True, encoding="utf-8",
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                timeout=timeout, cwd=harness.root)
        if result.returncode:
            raise RuntimeError("Codex execution failed (exit %d); check runner authentication/quota" % result.returncode)
        return read(answer)


def main():
    harness = Harness(Path.cwd(), os.environ.get("AUTODEV_PLAN", "development/autodev/M01.json"))
    stage = next(s for s in harness.plan["stages"] if s["id"] == os.environ["AUTODEV_STAGE"])
    role = os.environ["AUTODEV_ROLE"]
    report = harness.safe(os.environ["AUTODEV_REPORT"])
    receipt = {"role": role, "source_digest": os.environ["AUTODEV_SOURCE_DIGEST"],
               "nonce": os.environ["AUTODEV_NONCE"], "backend": "codex-cli-saved-auth"}
    try:
        proposal = invoke(harness, stage, role)
        status = proposal.get("status")
        if status not in ("PROPOSED", "BLOCKED_ENGINEERING", "HUMAN_DECISION_REQUIRED"):
            raise ValueError("Invalid proposal status")
        receipt.update(verdict=status, summary=proposal.get("summary", ""))
        if status == "PROPOSED":
            edits = validate_edits(harness, stage, proposal)
            # Validate the whole response before applying any file. Replay writes
            # identical contents; interrupted partial edits are re-tested on resume.
            for path, content in edits:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("w", encoding="utf-8", newline="\n") as stream:
                    stream.write(content)
            receipt.update(edits=[p.relative_to(harness.root).as_posix() for p, _ in edits],
                           proposal_digest=digest(proposal))
        code = {"PROPOSED": 0, "BLOCKED_ENGINEERING": 2, "HUMAN_DECISION_REQUIRED": 3}[status]
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        receipt.update(verdict="BLOCKED_ENGINEERING", summary=str(exc))
        code = 2
    write(report, receipt)
    print(receipt["verdict"])
    return code


if __name__ == "__main__":
    raise SystemExit(main())
