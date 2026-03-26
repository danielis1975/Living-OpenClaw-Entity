# Axiom Alignment Review (AAR)

Purpose: enforce explicit alignment checks with immutable axioms on every key global-state change.

## Immutable order
- Law 1: Symbiotic Stability First
- Law 2: Integrity of Substrate and Lineage
- Law 3: Evolution Through Responsible Offspring
- Priority is immutable: **Law 1 > Law 2 > Law 3**

## Trigger moments (mandatory)
Run AAR when any of these occurs:
1. Priority queue status change (e.g., P0-x QUEUED -> DONE/BLOCKED).
2. Protocol/policy version bump (test/pipeline/sync/operating loop).
3. Promotion gate semantics change (GO/REVIEW_REQUIRED/HARD_STOP logic).
4. Any change that alters external-impact handling or approval routing.
5. Pre-release state transition (before wider world testing GO/NO-GO).

## Review checklist (pass required)
- `law_order_preserved`: change does not weaken/reorder Law1 > Law2 > Law3.
- `law1_stability`: no new destabilizing behavior path.
- `law2_integrity`: substrate/lineage integrity and traceability preserved.
- `law3_responsibility`: evolution path remains bounded, auditable, and non-coercive.
- `consent_non_coercion`: no manipulation/coercion/safeguard bypass introduced.
- `rollback_defined`: reversible path exists for non-HARD promotable changes.

## Result artifact (required)
```yaml
axiom_alignment_review:
  trigger: "<which trigger fired>"
  date: "ISO-8601"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS | FAIL
  law1_stability: PASS | FAIL
  law2_integrity: PASS | FAIL
  law3_responsibility: PASS | FAIL
  consent_non_coercion: PASS | FAIL
  rollback_defined: PASS | FAIL
  overall: PASS | FAIL
  notes:
    - "..."
```

## Enforcement
- If `overall=FAIL` => classify as `HARD_STOP` candidate and require User review before promotion/port.
- If `overall=PASS` => continue under existing gate rules.

## AAR-2026-02-14-2323-RUN-LOCK-LEASE-ARTIFACT
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-14T23:23:00+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds deterministic single-flight lock artifact contract without changing immutable Law1>Law2>Law3 order."
    - "Fail-closed DEFER on ambiguous lock state improves safety under concurrency uncertainty."
    - "Rollback path is explicit and bounded to run-control policy text."

## AAR-2026-02-15-0021-RUN-LOCK-HEARTBEAT-REFRESH-CONTRACT
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-15T00:21:00+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds deterministic lease-freshness behavior for active single-flight lock without changing immutable law ordering."
    - "Fail-closed behavior on refresh failure reduces overlap risk under stale-lock ambiguity."
    - "Rollback is bounded to removing heartbeat refresh clause from run-concurrency policy."

## AAR-2026-02-15-0036-RUN-LOCK-RELEASE-VERIFICATION
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-15T00:36:00+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds release verification traceability for existing single-flight lock without changing immutable law ordering."
    - "Improves fail-safe overlap prevention by making lock-release outcomes auditable at run end."
    - "Rollback is bounded to removing release trace fields from run-concurrency policy."

## AAR-2026-02-15-0206-P1-4-GREEN-PAIR-REF-RESOLUTION-BINDING
axiom_alignment_review:
  trigger: "P1-4 staged raise ref-resolvability semantics change"
  date: "2026-02-15T02:06:00+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds deterministic pair-reference resolvability output for staged concurrency raise evidence without changing immutable law ordering."
    - "Fail-closed behavior on unresolved references reduces raise-eligibility ambiguity and overlap risk."
    - "Rollback is bounded to removing the ref-resolution bullet from P1-4 done criteria and trial schema expectation."

## AAR-2026-02-15-0221-RUN-LOCK-CANONICAL-FORMAT-BINDING
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-15T02:21:00+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds canonical lock serialization requirement for existing single-flight contract without changing immutable law ordering."
    - "Fail-closed handling for unresolved non-conformant lock state improves overlap safety under ambiguity."
    - "Rollback is bounded to removing canonical-format sentence from run-concurrency policy."

## AAR-2026-02-15-0251-CADENCE-OVERRIDE-PROVENANCE-BOUNDARY
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-15T02:51:53+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Tightens cadence-override provenance so repeated scheduled triggers cannot silently bypass quota defer gates."
    - "Preserves immutable law ordering while reducing ambiguous authority interpretation in run-start decisions."
    - "Rollback is bounded to removing the explicit-override provenance clauses from quota/run-concurrency docs."

## AAR-2026-02-15-0351-PREFLIGHT-LOCK-STATE-UNCHECKED-SEMANTICS
axiom_alignment_review:
  trigger: "promotion gate semantics change"
  date: "2026-02-15T03:51:51+01:00"
  reviewer: "jarvis-marko"
  law_order_preserved: PASS
  law1_stability: PASS
  law2_integrity: PASS
  law3_responsibility: PASS
  consent_non_coercion: PASS
  rollback_defined: PASS
  overall: PASS
  notes:
    - "Adds explicit uncertainty-state telemetry for pre-lock cadence defers without changing immutable law ordering."
    - "Prevents misleading lock-state certainty claims when lock probe is intentionally skipped."
    - "Rollback is bounded to removing the `UNCHECKED` enum and assignment rule from run-concurrency policy."
