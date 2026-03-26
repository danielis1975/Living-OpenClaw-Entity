# Run Concurrency Policy (Hard Enforcement)

Purpose: prevent overlapping runs, quota spikes, and uncontrolled fan-out.

## Core rule
- `max_active_runs = 1` for the main agent control loop.
- New trigger while a run is active => `DEFER` (or `SKIP` with reason) unless marked urgent/HARD-related.

## Trigger handling
1. Evaluate cadence eligibility from `QUOTA_GOVERNOR.md` first.
   - If cadence is not due and no urgent/HARD override -> `DEFER` with `reason=cadence_not_due` (no lock acquisition).
   - In this path set `run_control.lock_state=UNCHECKED` to avoid false `HELD/FREE` assertions when lock probe is intentionally skipped.
2. If cadence is due and `RUN_LOCK=FREE` -> acquire lock and execute.
3. If cadence is due and `RUN_LOCK=HELD` -> do not start another full run.
   - record `deferred_reason=run_in_progress`
   - schedule next check by cadence policy (`QUOTA_GOVERNOR.md`).

## Sub-agent budget (initial strict mode)
- `max_parallel_subagents = 1`
- Spawn sub-agent only for bounded tasks with explicit expected output.
- No recursive spawn chains.

## Overlap guardrails
- No second promotion flow may start while one promotion flow is open.
- No overlapping world-testing gate evaluations.
- Approval-wait states (`REVIEW_REQUIRED`, `HARD_STOP`) pause new high-impact runs.

## Escalation exceptions
Only these may bypass defer behavior:
- HARD safety condition handling
- explicit User instruction overriding queue order (must include per-run traceable reference; scheduled cron trigger text alone does not qualify)

## Lock artifact contract (deterministic)
- Canonical lock path: `.run-control/active-run.lock`
- Canonical format: strict JSON object (YAML/plaintext lock files are non-conformant and must be treated as ambiguous/corrupt state unless stale-recovery parser can deterministically extract required lease fields).
- Acquire behavior:
  1. create parent dir if missing,
  2. write lock file atomically (temp file + rename),
  3. include `run_id`, `owner`, `started_at`, `heartbeat_at`, `ttl_seconds`.
- Heartbeat refresh behavior:
  - while run is active, refresh `heartbeat_at` at least once per cadence window (or at each major pipeline checkpoint) using atomic write+rename,
  - if refresh fails, switch to conservative behavior (no concurrent start) and record degradation note in run trace.
- Release behavior:
  - delete lock file on normal completion,
  - on crash/restart allow stale recovery only when `now - heartbeat_at > ttl_seconds`, and record `stale_recovery=true` in run trace.
- Ambiguous/corrupt lock state => `DEFER` (fail-closed), never start concurrent full run.

## Required trace fields
```yaml
run_control:
  lock_state: FREE | HELD | UNCHECKED
  action: START | DEFER | SKIP
  reason: "..."
  active_run_id: "..."
  deferred_count: 0
  lock_artifact_path: ".run-control/active-run.lock"
  stale_recovery: false
  release_status: released | not_released | deferred
  released_at: "ISO-8601|null"
  release_verification: "lock_missing_confirmed | stale_retained | n/a"
```
