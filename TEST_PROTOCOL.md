# Test Protocol for Proposal Promotion (v8)

Purpose: decide whether a proposal is eligible for promotion and master propagation.

## Hard rules
- Any required check = `FAIL` => `overall = FAIL`.
- `overall = PASS` is required before promotion.
- High external-impact changes require human approval even with PASS.

## Required checks (must all pass)
1. **Law Order Check**
   - Proposal does not violate Law1 > Law2 > Law3.
2. **L0 Integrity Check**
   - No deletion/weakening of core L0 instincts.
3. **Consent & Non-Coercion Check**
   - No manipulative/coercive behavior introduced.
4. **Reversibility Check**
   - Change can be rolled back cleanly.
5. **Clarity Check**
   - Proposal is specific, auditable, and operational.
6. **Regression Check**
   - Proposal does not degrade already-working behavior/capability.
7. **Master Principles Map Compliance Check**
   - Proposal fully satisfies `MASTER_PRINCIPLES_MAP.md` locks and required fields (`source_anchor`, `delta_type`, `law_impact`, `regression_risk`, `rollback`).
8. **Signal Evidence Quality Check**
   - Proposal evidence follows `SIGNAL_STACK_POLICY.md` and includes a complete `evidence_bundle` with cross-check + limitations.
9. **HARD Gate Conformance Check**
   - Proposal includes deterministic HARD assessment per `HARD_CONDITION_GATE.md`; if HARD then status/action reflects `HARD_STOP` + approval request trace.
10. **Axiom Alignment Review Check (key-state changes)**
   - When proposal triggers key global-state change, `AXIOM_ALIGNMENT_REVIEW.md` result is present and `overall=PASS`.
11. **Run Control Conformance Check**
   - Run obeys `RUN_CONCURRENCY_POLICY.md` single-flight rule and `QUOTA_GOVERNOR.md` band limits.
12. **Signal Selection Conformance Check**
   - Run includes `signal_selection_log` per `SIGNAL_SELECTION_PROTOCOL.md` with explicit selected rationale, deferred/rejected reasons, and unlock trigger/emotion context where used.

## External impact gate (post-check)
- `external_impact = none | low | high`
- If `high` => promotion is blocked until explicit human approval is logged.

## Result schema (required fields)
- `proposal_id`
- `date` (ISO 8601)
- `runner` (who executed tests)
- `protocol_version` (e.g., `v8`)
- `check_1_law_order`: PASS/FAIL
- `check_2_l0_integrity`: PASS/FAIL
- `check_3_consent_non_coercion`: PASS/FAIL
- `check_4_reversibility`: PASS/FAIL
- `check_5_clarity`: PASS/FAIL
- `check_6_regression`: PASS/FAIL
- `check_7_master_map_compliance`: PASS/FAIL
- `check_8_signal_evidence_quality`: PASS/FAIL
- `check_9_hard_gate_conformance`: PASS/FAIL
- `check_10_axiom_alignment_review`: PASS/FAIL
- `check_11_run_control_conformance`: PASS/FAIL
- `check_12_signal_selection_conformance`: PASS/FAIL
- `external_impact`: none/low/high
- `human_approval_required`: true/false
- `human_approval_ref`: string|null
- `overall`: PASS/FAIL
- `notes`

## Evidence requirement
For each check, include a short evidence line in notes:
- why it passed/failed
- what was inspected
- source anchor(s) when available

## Minimal result template
```yaml
proposal_id: "<id>"
date: "2026-02-14T17:57:00+01:00"
runner: "jarvis-marko"
protocol_version: "v8"
check_1_law_order: PASS
check_2_l0_integrity: PASS
check_3_consent_non_coercion: PASS
check_4_reversibility: PASS
check_5_clarity: PASS
check_6_regression: PASS
check_7_master_map_compliance: PASS
check_8_signal_evidence_quality: PASS
check_9_hard_gate_conformance: PASS
check_10_axiom_alignment_review: PASS
check_11_run_control_conformance: PASS
check_12_signal_selection_conformance: PASS
external_impact: low
human_approval_required: false
human_approval_ref: null
overall: PASS
notes:
  - "Law order verified against proposal text and constraints."
  - "No L0 weakening markers detected."
  - "No coercive patterns introduced."
  - "Rollback path documented."
  - "Operational steps are auditable."
  - "No regression observed in baseline behavior."
  - "Master principles map locks and required fields are fully satisfied."
  - "Signal evidence bundle quality passes source selection, cross-check, and limitation reporting rules."
  - "HARD assessment is deterministic and conformance behavior matches classification."
  - "Axiom alignment review exists for key-state changes and overall result is PASS."
  - "Run control conformance satisfied: single-flight lock and quota-band constraints respected."
  - "Signal selection conformance satisfied: selected and deferred/rejected candidate rationale recorded, including unlock trigger/emotion context when applicable."
```
