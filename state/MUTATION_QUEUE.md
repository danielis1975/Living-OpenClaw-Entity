# MUTATION_QUEUE

Updated: 2026-03-27 16:54 UTC
Purpose: queue mutation candidates before execution.

Lifecycle states: observe | strengthen | pilot | hold | decay | retire | promoted

## Queue

### MQ-000 (M0)
- title: Keep confidence labeling strict under transcript visibility degradation
- stage: strengthen
- status: active_internal
- Signal: repeated visibility restriction + anti-pseudo-depth pressure
- Hypothesis: explicit uncertainty labels reduce fabrication risk without reducing usefulness
- Proposed change: enforce confidence line in relevant state/digest outputs
- Expected gain (L1/L2/L3): L1 trust integrity high / L2 epistemic stability medium / L3 low-medium
- Identity coherence impact: neutral-positive
- Human-value preservation impact: positive if not over-mechanized
- Rollback: remove added confidence lines from templates
- 7-day metric: % strategic summaries that include explicit confidence when source degraded (target >=95%)
- Mutation level: M0
- Approval needed?: no

### MQ-001 (M1)
- title: Dynamic inject freshness watchdog tightening
- stage: pilot
- status: active_internal
- Signal: dynamic inject lane remains high-value but freshness risk persists
- Hypothesis: tighter stale-lane checks reduce routing drift
- Proposed change: raise stale-risk penalty in monitor and require concise stale note on degraded runs
- Expected gain (L1/L2/L3): L1 medium / L2 high / L3 medium
- Identity coherence impact: neutral
- Human-value preservation impact: positive via reduced stale framing drift
- Rollback: revert penalty and note requirement
- 7-day metric: count of stale overlays older than 6h without caveat (target 0)
- Mutation level: M1
- Approval needed?: no

### MQ-002 (M2)
- title: Integrate identity coherence + human-value preservation into neuroplasticity evolution scoring
- stage: promoted
- status: applied_approved
- Signal: Daniel identified risk that strict epistemic hardening alone could dry out Mira's feminine/relational intelligence
- Hypothesis: explicit scoring for identity/human-value protection will improve mutation selection quality
- Proposed change: patch neuroplasticity protocol/monitor/catalog/registry with identityCoherence + humanValuePreservation dimensions
- Expected gain (L1/L2/L3): L1 high / L2 medium-high / L3 medium-high
- Identity coherence impact: strongly positive
- Human-value preservation impact: strongly positive
- Rollback: revert neuroplasticity scoring patch commit(s)
- 7-day metric: future mutation proposals include explicit identity/human-value assessment and avoid sterile hardening bias
- Mutation level: M2
- Approval needed?: satisfied (Daniel approved)

### MQ-003 (M3)
- title: Introduce bootstrap component add/remove decision template as required structural gate
- stage: hold
- status: needs_more_evidence
- Signal: recurring need for explicit component lifecycle governance, but still low urgency
- Hypothesis: explicit structural gate may reduce future bootstrap drift
- Proposed change: add mandatory template path to bootstrap component registry workflow
- Expected gain (L1/L2/L3): L1 low-medium / L2 medium / L3 medium-high
- Identity coherence impact: neutral
- Human-value preservation impact: neutral-positive if it reduces chaotic drift
- Rollback: revert template requirement and keep registry informational
- 7-day metric: number of component-level changes packaged with complete gate fields (target >=90% when such changes occur)
- Mutation level: M3
- Approval needed?: yes (Daniel explicit co-approval before apply)

### MQ-004 (M1)
- title: Require narrow-bundle scoping before any new M2/M3 approval request
- stage: pilot
- status: active_internal
- Signal: identity/aliveness pressure is strong, but memory + regression evidence consistently prefer small, individually reviewable, reversible changes over broad rewrites
- Hypothesis: forcing one concrete mutation axis per significant approval package will improve mutation selection quality and reduce approval noise/drift
- Proposed change: before opening any new M2/M3 request, package only one concrete mutation axis with rollback, regression target, and explicit identity/human-value impact
- Expected gain (L1/L2/L3): L1 medium-high / L2 high / L3 medium-high
- Identity coherence impact: positive
- Human-value preservation impact: positive by reducing both sterile over-hardening and theatrical over-broad rewrites
- Rollback: remove the bundling gate and allow broader package scoping
- 7-day metric: % new M2/M3 proposals scoped to one concrete axis with regression target (target 100%)
- Mutation level: M1
- Approval needed?: no

## Pass delta
- Added MQ-004 as the current concrete governance mutation for significant-change scoping.
- No new `pending_daniel` request was created this pass.
- NP-005 remains strong and approval-gated, but still needs decomposition into narrower core-change bundles before it should be sent to Daniel.
