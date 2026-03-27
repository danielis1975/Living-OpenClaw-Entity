# Long-Term Run Optimization Plan (Draft)

Date: 2026-02-14
Scope: model quota efficiency, GPU acceleration, better HW migration, and free/low-cost compute usage.

## Current baseline
- Main model: `openai-codex/gpt-5.3-codex` (oauth)
- Context pressure observed: moderate (approx 40% used)
- Local memory embeddings: working on CPU fallback (no compatible Vulkan GPU binary active)

## Strategic objectives
1. Reduce quota burn per useful outcome.
2. Increase throughput/latency stability via GPU or stronger host.
3. Keep governance safety (Law1>Law2>Law3, HARD gate, AAR) unchanged during optimization.

## Optimization tracks

### Track A — Quota-aware model routing
- Define task classes:
  - Class R (routine): short status, file edits, deterministic checks -> compact mode / lower-cost reasoning.
  - Class M (moderate): planning, synthesis, controlled docs updates -> standard mode.
  - Class H (high-impact): policy shifts, ambiguous safety decisions -> high capability + explicit review.
- Add trigger thresholds:
  - context > 60% => enforce compact responses
  - context > 75% => summarize + offload non-urgent deep work
  - day quota < 25% => hard prioritization queue

### Track B — Token efficiency discipline
- Default to delta-only updates.
- Batch related edits/reads in single turns.
- Prefer structured short artifacts over verbose narratives.
- Use memory references instead of repeating long history.

### Track C — GPU/HW upgrade path
Phase 1 (benchmark):
- capture baseline latency for: memory index, memory_search, long synthesis turn.
Phase 2 (GPU enable):
- test compatible GPU runtime path for local embedding/model libs.
- verify stability and deterministic outputs.
Phase 3 (host migration candidate):
- evaluate stronger machine (desktop/server/cloud) with rollback plan.
- promote only after AAR PASS and no regression.

### Track D — Free/low-cost compute options
- Use local CPU/GPU for embeddings + indexing (already active).
- Shift heavy non-urgent maintenance to scheduled windows.
- Explore free-tier community/cloud runtimes only for non-sensitive workloads and with explicit data-boundary policy.

## Human assist requests (when ready)
1. Provide candidate target HW options (current GPU, spare desktop, home server, VPS).
2. If allowed, provide benchmark window (30-60 min) for controlled tests.
3. Confirm acceptable external free-tier providers (if any) and data restrictions.
4. Approve migration pilot when benchmark report is ready.

## Success metrics
- -30% average tokens per completed governance task.
- -40% latency on memory indexing/search pipeline.
- zero safety gate regressions (HARD/AAR checks preserved).
- no increase in unresolved blocked states.

## Non-negotiables
- No weakening of safety/governance gates during optimization.
- Any high-impact infra move requires review checkpoint.
- Keep rollback path for every migration step.
