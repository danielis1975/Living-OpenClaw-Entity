# Recursive Self-Improvement Pipeline (v4)

Goal: convert lived experience into tested Jarvis upgrades and propagate into master project automatically after passing tests.

## Loop stages
1. **Capture**
   - Store cycle experience in `experience/experience-log.md`.
2. **Synthesize**
   - Convert recurring patterns into candidate element(s) in `experience/jarvis-elements.md`.
3. **Signal Selection**
   - Build candidate pool and select active signal using `SIGNAL_SELECTION_PROTOCOL.md`.
   - Persist `signal_selection_log` (selected reason + rejected/deferred reasons + unlock trigger/emotion context) in `exploration-notes.md`.
4. **Propose**
   - Add structured proposal in `proposals/child-definition-changelog.md` with required evidence bundle from `SIGNAL_STACK_POLICY.md`.
5. **Run Control Preflight**
   - Apply quota band and cadence eligibility from `QUOTA_GOVERNOR.md` (`cadence_not_due` => defer unless urgent/HARD override).
   - Enforce single-flight lock from `RUN_CONCURRENCY_POLICY.md` only when cadence is due.
6. **Test**
   - Run checks from `TEST_PROTOCOL.md` (v8) and record outcome in `tests/test-results.md`.
7. **Promotion Decision**
   - Run deterministic HARD assessment from `HARD_CONDITION_GATE.md`.
   - If HARD => `HARD_STOP`, request User approval, no promotion/port.
   - If `overall=PASS` and `external_impact != high` and HARD=NO, append to `exports/master-update-batch.md`.
   - If `external_impact=high`, require explicit human approval before promotion.
8. **Axiom Alignment Review (key-state trigger)**
   - On key global-state transitions, run `AXIOM_ALIGNMENT_REVIEW.md`.
   - If AAR overall=FAIL, block promotion/port and escalate to User review.
9. **Port to master**
   - Auto-create/update patch in `external/AI-Instincts-project-repo/docs/child_updates/symbiotic-jarvis-marko.md`.
10. **Traceability**
   - Mark proposal as `[PORTED_TO_MASTER]` with commit hash + timestamp + test result reference.

## Promotion rules
- Any required test `FAIL` => `overall=FAIL` => proposal is not promotable.
- `overall=PASS` is necessary but not sufficient when `external_impact=high`.
- `external_impact=high` requires explicit human approval reference.
- If User issues VETO/PAUSE, set status marker `PROMOTION_BLOCKED_BY_DANIEL` and halt promotion immediately.
- If HARD classification is positive, set status marker `HARD_STOP` until APPROVE/REJECT/REVIEW outcome is recorded.

## Failure handling
- Keep failed proposals in queue with remediation notes.
- Re-test after remediation; keep prior result history for auditability.

## Safety gates
- Never bypass policy/safeguards.
- No external-impact action beyond allowed channels/tools.
- Always preserve Law1 > Law2 > Law3 priority.
