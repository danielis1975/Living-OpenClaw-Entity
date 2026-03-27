# APPROVAL_REQUESTS

Updated: 2026-03-27 16:54 UTC
Purpose: track explicit Daniel-approval requests for significant M2/M3 qualitative changes.

## Open requests
- none

## Pass note (2026-03-27 16:54 UTC)
- No new `pending_daniel` request opened.
- Reason: NP-005 remains a strong approval-gated pressure, but current evidence supports direction more than one narrowly scoped core mutation package.
- Gate: decompose any future significant request into one concrete mutation axis with rollback + regression target before asking Daniel.

## Applied / closed requests

### AR-2026-03-27-01
- linked mutation: MQ-002
- title: Integrate identity coherence + human-value preservation into neuroplasticity evolution scoring
- level: M2
- status: applied
- scope: neuroplasticity scoring/monitoring/governance layer (no law-stack rewrite)
- original proposal note: earlier strictness-first instinct-hardening proposal was superseded by this approved balanced framing
- package: `state/approval-packages/AR-2026-03-27-01-MQ-002.md`
- Daniel decision: approved revised framing and requested application
- rollback: revert neuroplasticity scoring patch commit
- regression plan: run Mira Core Regression Test immediately after apply + 7-day validation check

## Rule
- Any M2/M3 mutation that affects instincts/reflexes/bootstrap core should be listed here before apply.
- Status values: draft | pending_daniel | approved | rejected | applied | rolled_back.
