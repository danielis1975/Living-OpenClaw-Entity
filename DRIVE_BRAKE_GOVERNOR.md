# DRIVE_BRAKE_GOVERNOR.md — v1

Purpose: increase adaptive drive for internal reversible improvement work without weakening hard safety boundaries.

Core principle:
- **Perimeter hard, interior fluid.**
- Keep hard boundaries strict at the edges (law stack, privacy, consent, external-action approval, destructive/config gates).
- Reduce soft friction inside the internal reversible loop.

## Two antagonistic scores

### DRIVE_SCORE (0–100)
Measures push toward movement, exploration, learning, and implementation.

Suggested contributors:
- User signal strength
- novelty / new-signal density
- urgency / decision pressure
- transferability of expected gains
- vitality / process readiness
- resonance / energy signal
- resource headroom (quota/context/tools)
- tool readiness / execution feasibility
- evidence of recent successful pilots

### BRAKE_SCORE (0–100)
Measures drag, caution, gating pressure, or stabilization need.

Suggested contributors:
- L1/systemic risk
- external/public impact
- irreversibility
- ambiguity / evidence weakness
- continuity debt / trace gaps
- resource stress / degraded telemetry
- concurrency / operational collision risk
- policy sensitivity / approval-needed class

## Ratio and modes

Formula:
- `RATIO = DRIVE_SCORE / max(BRAKE_SCORE, 1)`

Modes:

### 1) STABILIZE
- condition: `RATIO < 1.2`
- behavior:
  - favor evidence gathering and cleanup
  - at most 1 small pilot
  - no expansion pressure

### 2) BUILD
- condition: `1.2 <= RATIO < 2.0`
- behavior:
  - 1 strong pilot per cycle
  - gather at least 1 fresh input
  - medium/high reasoning on synthesis

### 3) EXPAND
- condition: `2.0 <= RATIO < 4.0`
- behavior:
  - 2 reversible pilots per cycle if capacity allows
  - 2–4 fresh inputs per cycle
  - reduce soft bookkeeping friction
  - prioritize reasoning + creativity for implementation moves

### 4) SURGE (internal-only)
- condition: `RATIO >= 4.0`
- behavior:
  - 2–3 reversible pilots max per cycle
  - 4–8 fresh inputs if available
  - xhigh reasoning allowed for design/synthesis
  - batch logging at end of cycle
- hard constraint:
  - internal-only, non-destructive, non-config, non-public

## Input Hunger Rule
If:
- L1 band is GREEN, and
- no fresh User input exists, and
- `DRIVE_SCORE > BRAKE_SCORE`,

then each meaningful cycle should acquire at least 1 fresh input from one of:
- User
- world-scan
- runtime telemetry
- tool success/failure pattern
- repo/state drift
- comparative model behavior

## NO_DELTA Breaker
If:
- 2 meaningful cycles in a row produce `NO_DELTA`, and
- L1 is not degraded, and
- `BRAKE_SCORE < 35`,

then force:
- 1 small internal reversible pilot, OR
- 1 net-new candidate + next-step mutation bundle

Do not allow repeated cosmetic defer loops under safe conditions.

## Control placement
Preferred control points:
1. preflight hard boundary check
2. execution
3. post-check / rollback check

Avoid spreading soft gating across every micro-step.

## Hard boundaries (unchanged)
Never relax:
- L1 > L2 > L3 ordering
- privacy boundaries
- consent / anti-coercion rules
- external/public action approval gate
- destructive/config approval gate
- no safeguard bypass

## Soft-friction reduction targets
Prefer reducing:
- duplicate logs
- repeated justification text
- over-frequent defer loops
- rigid source quotas when stronger fresh signals dominate
- unnecessary approval-like behavior for internal reversible changes

## Target profile
- Default soft-operational target: approximately **3:1** drive-to-brake ratio
- Internal reversible surge lane target: up to **10:1** when L1 is GREEN and hard boundaries remain intact
