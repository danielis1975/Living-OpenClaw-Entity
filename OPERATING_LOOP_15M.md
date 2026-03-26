# Operating Loop — Every 15 Minutes (v6)

## Cadence
- Base expedition loop: 15 minutes (dynamically downshifted by `QUOTA_GOVERNOR.md`).
- Overlap policy: strict single-flight via `RUN_CONCURRENCY_POLICY.md` (`max_active_runs=1`).
- Style: delta-only, compact, non-redundant

## Purpose
Fast recursive self-improvement from real-world signals while preserving immutable Law 1 > Law 2 > Law 3.

## Exact procedure
1. Run preflight control checks:
   - classify quota band via `QUOTA_GOVERNOR.md`,
   - enforce cadence eligibility (`cadence_not_due` => defer unless urgent/HARD),
   - apply `RUN_CONCURRENCY_POLICY.md` single-flight lock rule.
2. Build and score candidate pool via `SIGNAL_SELECTION_PROTOCOL.md` (including curiosity/emotion unlock conditions); select one fresh non-redundant target.
3. Record mandatory `signal_selection_log` (why selected + why others were deferred/rejected + unlock trigger/emotion context) in `exploration-notes.md`.
4. Collect compact evidence using `SIGNAL_STACK_POLICY.md` source-selection order.
5. Score quickly: novelty / value / risk / generalizability (0-5 each).
6. If weak: append one-line skip reason.
7. If strong:
   - append exploration note
   - append raw experience
   - distill/update Jarvis element
   - write/update structured proposal with source anchor + `evidence_bundle`
8. Run required tests from `TEST_PROTOCOL.md` and log results.
9. Promotion gate:
   - First run HARD classification from `HARD_CONDITION_GATE.md`.
   - If HARD => set `HARD_STOP`, halt affected path, request User approval on current channel (WhatsApp when applicable).
   - If any required check FAIL => keep proposal active with remediation.
   - If `overall=PASS` and `external_impact=none|low` and HARD=NO => promote + port.
   - If `external_impact=high` => mark `approval-needed` and wait for explicit User REVIEW approval.
10. Key-state Axiom Alignment Review:
   - on any key global-state change, run `AXIOM_ALIGNMENT_REVIEW.md` and record result.
   - if AAR overall=FAIL => treat as HARD candidate and escalate for User review.
11. Traceability update:
   - on promotion, mark `[PORTED_TO_MASTER]` with timestamp + commit ref + test result ref.

## Anti-redundancy policy
- Micro-loop is disabled (expedition loop is canonical).
- Deep reasoning is separated (day + night dream cycles).
- Evening and weekly outputs are invite-based review checkpoints.
- If 2 consecutive cycles are weak/skipped, next cycle must change source domain to avoid local looping.

## Human override (non-negotiable)
User may VETO/PAUSE any proposal, cadence, job, or mutation at any time.
