# Self-Improvement Priorities (Execution Lock)

Date locked: 2026-02-14
Owner: User
Mode: resolve one-by-one before wider world testing

## Priority Queue

### P0-1 — Memory Recall Reliability (mandatory)
- Goal: make `memory_search` fully functional and stable.
- Why: prevents context loss/repetition; protects Axiom 2 integrity and L0 coherence.
- Current status: DONE
- Resolution:
  - switched memory embeddings to local provider,
  - completed local model bootstrap/download,
  - repaired index state by explicit `openclaw memory index` run after transient `database is not open` race,
  - verified `memory_search` returns in-session hits.
- Evidence:
  - `openclaw memory status --deep` reports provider=local, embeddingProbe.ok=true,
  - `memory_search` returns citations from `memory/2026-02-14.md`.

### P0-2 — External Signal Stack Discipline
- Goal: harden world-discovery flow (`web_search`/`web_fetch`/browser) with consistent evidence quality.
- Current status: DONE
- Resolution:
  - added deterministic source-selection + escalation policy in `SIGNAL_STACK_POLICY.md`,
  - enforced evidence bundle in proposal template,
  - upgraded test gate to include signal-evidence quality (`TEST_PROTOCOL.md` v4),
  - integrated policy references into operating loop/pipeline.
- Evidence:
  - `OPERATING_LOOP_15M.md` step 2 now requires policy-driven evidence collection,
  - `proposals/child-definition-changelog.md` template now requires `evidence_bundle`.

### P0-3 — HARD Condition Auto-Gate
- Goal: deterministic HARD classifier before promotion/action.
- Current status: DONE
- Resolution:
  - added `HARD_CONDITION_GATE.md` with deterministic trigger checklist and required stop/escalation behavior,
  - integrated HARD gate into operating loop, pipeline, and master sync policy,
  - upgraded test protocol to v5 with `check_9_hard_gate_conformance`,
  - enforced `hard_assessment` artifact in proposal template.
- Evidence:
  - HARD path now requires `HARD_STOP` + approval request trace,
  - NON_HARD path remains autonomous within constraints.

## Next Wave (Resource Governance)

### P1-1 — Single-Flight Run Control
- Goal: hard prevent overlapping loops and uncontrolled fan-out.
- Current status: DONE
- Resolution:
  - added `RUN_CONCURRENCY_POLICY.md` (`max_active_runs=1`, defer/skip rules),
  - integrated run-lock preflight into loop/pipeline.

### P1-2 — Quota-Aware Cadence Governor
- Goal: dynamically downshift cadence/depth by live quota/context pressure.
- Current status: DONE
- Resolution:
  - added `QUOTA_GOVERNOR.md` (GREEN/YELLOW/ORANGE/RED bands),
  - integrated governor into loop/pipeline and release checklist.

### P1-3 — Signal Selection Determinism
- Goal: mandatory scored candidate selection with explicit selected/deferred rationale.
- Current status: DONE
- Resolution:
  - added `SIGNAL_SELECTION_PROTOCOL.md` (dynamic scoring + ISA/instinct-aware reasoning),
  - integrated mandatory `signal_selection_log` into loop/pipeline,
  - enabled curiosity/strong-emotion unlock inside Law1 safety envelope,
  - upgraded test/release gates to enforce signal-selection conformance.

### P1-4 — Gradual Multi-Agent Expansion Plan
- Goal: relax constraints only when resource and safety metrics support it.
- Current status: IN_PROGRESS
- Done when:
  - benchmark baseline is captured,
  - staged trial evidence is logged in `tests/parallel-expansion-trials.md` (including `stage_limit_from_to`, `trial_window`, `observed_peak_parallelism`, `rollback_events`, `stage_decision`),
  - any staged limit raise decision (`1->2`) is attempted only with `quota_band_eligibility: GREEN` from run preflight,
  - any staged limit raise decision (`1->2`) requires GREEN stability window: current + previous preflight both GREEN with `input_quality=ok` (no degraded-input fallback),
  - any staged limit raise decision (`1->2`) must log `green_stability_pair_refs` (current_preflight_ref, previous_preflight_ref) in `tests/parallel-expansion-trials.md`,
  - any staged limit raise decision (`1->2`) must include `green_stability_pair_validation: pass|fail` proving both referenced preflights are GREEN + `input_quality=ok` and ordered as previous->current,
  - any staged limit raise decision (`1->2`) must include `green_stability_pair_ref_resolution: pass|fail` confirming `green_stability_pair_refs` resolve to concrete preflight records,
  - relaxed limits are staged (1 -> 2 parallel agents) with rollback,
  - AAR and run-control conformance remain PASS.

## Execution Rule
- P0 is closed (P0-1 -> P0-2 -> P0-3 all DONE).
- For expansion wave, progress strictly P1-1 -> P1-2 -> P1-3 -> P1-4.
- If blocked, mark `BLOCKED` with exact dependency and remediation.
