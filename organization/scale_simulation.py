"""M02 labelled synthetic load; never Human Pilot or business evidence."""
import argparse
from pathlib import Path
import tempfile
import time
from autodev.runtime import write
from organization.core import Organization
from organization.identity import DELEGABLE
from organization.store import Store


def scenario(send, tasks=30):
    if not isinstance(tasks, int) or not 1 <= tasks <= 30:
        raise ValueError("Fixture task count must be 1..30")
    def call(actor, command, data, key):
        return send(actor=actor, command=command, data=data, idempotency_key="m02/" + key)
    for n in range(10):
        call("SIMULATOR", "register_human", {"id": f"H{n}", "display_name": f"Synthetic Human {n}"}, f"human-{n}")
        call(f"H{n}", "bind_agent", {"hau_id": f"U{n}", "agent_id": f"A{n}", "permissions": sorted(DELEGABLE)}, f"agent-{n}")
    for g in range(3):
        call("H0", "activate_goal", {"id": f"G{g}", "desired_change": "Synthetic load only", "success_criteria": "Traceable attempts", "boundary": ["read", "draft"], "goal_authority": "H0"}, f"goal-{g}")
    for t in range(tasks):
        tid = f"T{t}"
        call("H0", "create_task", {"id": tid, "primary_goal": f"G{t % 3}", "expected_output": "Synthetic alternatives", "acceptance_criteria": "Recorded evidence", "boundary": ["read"], "execution_mode": "parallel", "review_authority": "H8", "acceptance_authority": "H0", "selection_authority": "H9"}, tid)
        call("H0", "publish", {"task_id": tid}, tid + "-publish")
        for branch in range(2):
            n = (t * 2 + branch) % 10
            eid = f"E{t}-{branch}"
            call(f"A{n}", "claim", {"id": eid, "task_id": tid, "hau_id": f"U{n}"}, eid)
            call(f"A{n}", "ack", {"execution_id": eid}, eid + "-ack")
        for branch in range(2):
            n = (t * 2 + branch) % 10
            eid, rid = f"E{t}-{branch}", f"R{t}-{branch}"
            if branch == 1 and t % 5 == 1:
                call(f"A{n}", "blocked", {"execution_id": eid, "summary": "Synthetic capability/scope gap"}, eid + "-blocked")
                call(f"A{n}", "request_boundary", {"id": "B" + eid, "execution_id": eid, "requested_scope": ["read", "draft"], "reason": "Explicit draft authorization needed"}, eid + "-boundary")
                call("H0", "decide_boundary", {"request_id": "B" + eid, "decision": "approved"}, eid + "-approve")
                call(f"H{n}", "resume", {"execution_id": eid, "summary": "Authorized synthetic resumption"}, eid + "-resume")
            if branch == 1 and t % 5 == 2:
                call(f"A{n}", "agent_status", {"agent_id": f"A{n}", "runtime_status": "offline"}, eid + "-offline")
                call(f"H{n}", "resume", {"execution_id": eid, "summary": "Human fixture takes over interrupted attempt"}, eid + "-takeover")
            failed = branch == 1 and t % 5 == 0
            call(f"H{n}", "fail" if failed else "submit", {"id": rid, "execution_id": eid, "result": "Synthetic failure" if failed else "Synthetic candidate", "observed_terrain": "Software fixture only", "major_execution_facts": "See event trail", "reflection": "No real organization inference"}, rid)
            call("H8", "review", {"id": "V" + rid, "return_id": rid, "credible": True, "evidence": "Fixture command outcomes"}, "V" + rid)
            call("H0", "accept", {"id": "C" + rid, "return_id": rid, "review_id": "V" + rid, "accepted": not failed, "rationale": "Synthetic intended-use decision"}, "C" + rid)
            if branch == 1 and t % 5 == 2:
                call(f"H{n}", "agent_status", {"agent_id": f"A{n}", "runtime_status": "online"}, eid + "-online")
        call("H9", "select", {"id": "SEL" + tid, "task_id": tid, "return_id": f"R{t}-0", "rationale": "Select one accepted candidate; retain both attempts"}, "SEL" + tid)


def verify(state, events, tasks=30):
    executions, returns = state["Execution"], state["Return"]
    checks = {
        "population": len(state["HAU"]) == 10 and len(state["Goal"]) == 3 and len(state["Task"]) == tasks and len(executions) == tasks * 2,
        "all_attempts_formally_closed": all(e["status"] == "closed" and e["return_id"] in returns for e in executions.values()),
        "owner_matches_hau": all(e["accountable_owner"] == state["HAU"][e["hau_id"]]["human_id"] for e in executions.values()),
        "two_distinct_attempts_per_task": all(sum(e["task_id"] == t for e in executions.values()) == 2 for t in state["Task"]),
        "review_acceptance_selection_separate": len(state["Review"]) == tasks * 2 and len(state["Acceptance"]) == tasks * 2 and len(state["Selection"]) == tasks,
        "failure_not_accepted": all(not a["accepted"] for a in state["Acceptance"].values() if returns[a["return_id"]]["outcome"] == "failure"),
        "selection_retains_alternatives": len(returns) == tasks * 2 and all(state["Task"][s["task_id"]]["status"] == "closed" for s in state["Selection"].values()),
        "event_replay_equals_state": Store.replay(events) == state,
        "simulation_labels": all(e["simulation"] is True for e in events),
        "continuous_event_sequence": [e["sequence"] for e in events] == list(range(1, len(events) + 1)),
    }
    if tasks >= 3:
        types = {e["type"] for e in events}
        checks["boundary_and_interruption_observable"] = {"BoundaryApproved", "ExecutionInterrupted", "ExecutionFailed"}.issubset(types)
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=".autodev/m02-scale")
    args = parser.parse_args()
    start = time.monotonic()
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / "scale.sqlite3"
        org = Organization(path)
        scenario(org.execute)
        state, events = org.store.state(), org.store.events()
        checks = verify(state, events)
        reopened = Organization(path)
        checks["restart_state_preserved"] = reopened.store.state() == state
        scenario(reopened.execute)
        checks["full_command_replay_idempotent"] = reopened.store.events() == events
        assert all(checks.values())
        output = Path(args.output)
        report = {"kind": "synthetic software execution only", "verdict": "PASS", "real_human_participants": 0,
                  "checks": checks, "object_counts": {k: len(v) for k, v in state.items()},
                  "event_count": len(events), "elapsed_seconds": round(time.monotonic() - start, 3),
                  "limitations": ["Sequential command load with overlapping attempts, not simultaneous worker load", "Goal Challenge remains unspecified and unimplemented", "Not Phase 4 final acceptance or production capacity certification"]}
        write(output / "report.json", report)
        write(output / "events.json", {"simulation": True, "events": events})
        write(output / "state.json", {"simulation": True, "state": state})
        print(report)


if __name__ == "__main__":
    main()
