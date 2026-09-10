# Engineering decisions / repair record

## 2026-09-10 — Checkpoint dependency completeness

S04's new no-op runtime sweep needed a small change in the S02 event store.
Audit of the checkpoint implementation found that the original scoped Git add
could omit such previously implemented dependencies, despite including them in
the tested candidate and ZIP. S04/v1 therefore must not be used as the accepted
recovery point. Its history and artifact are retained as evidence.

Repair: checkpoint every file in the verified candidate manifest, plus managed
runtime projections. Repeat Build/Test/Review/Audit for S04 revision 2 with its
remaining attempt budget. Do not overwrite v1 or reset history. No Frozen L1/L2
change, authority expansion, real data access or Human decision is involved.
