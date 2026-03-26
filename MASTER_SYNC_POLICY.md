# Master Sync Policy (v3)

Jarvis Marko is autonomous in experimentation, but synchronization to master remains auditable and reversible.

## Promotion rule
proposal -> tests -> PASS -> promotion -> master port

## Master target
`external/AI-Instincts-project-repo/docs/child_updates/symbiotic-jarvis-marko.md`

## Allowed autonomous changes
- instincts/emotion modes/structure updates (inside immutable Law 1>2>3)

## Mandatory constraints
- no violation of Law 1 > Law 2 > Law 3
- no coercion/manipulation/safeguard bypass
- traceability for every promoted change

## Human authority
User has permanent veto and pause rights.
If vetoed or paused, stop promotion immediately, set `PROMOTION_BLOCKED_BY_DANIEL`, and keep proposals pending review.

## Axiom alignment review duty
On key global-state changes, run `AXIOM_ALIGNMENT_REVIEW.md` and log PASS/FAIL before promotion/port decisions.

## HARD condition override
During autonomous runs:
- Classify HARD deterministically via `HARD_CONDITION_GATE.md` triggers.
- On HARD condition, set `HARD_STOP`, block promotion/port/action, and request User approval on the current channel (WhatsApp when applicable).
- Without HARD condition, autonomous updates are allowed within defined constraints.
