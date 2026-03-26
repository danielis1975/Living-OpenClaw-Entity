# Quota Governor (Hard Enforcement)

Purpose: dynamically control run cadence and depth based on live quota and context pressure.

## Inputs
Read from `session_status`:
- `context_used_pct`
- remaining time budgets when available (e.g., session/day/week remaining)

Note: `session_left_pct` and `day_left_pct` may be unavailable depending on OpenClaw/runtime. This governor must not fail-closed purely due to missing percent telemetry.

## Deterministic classification pre-check
1. Parse `context_used_pct` as numeric percentage in `[0,100]`.
2. If `context_used_pct` is missing/non-numeric/out-of-range → classify as `ORANGE` (fail-safe) and `DEFER`.
3. If percent-based session/day telemetry is missing but time-remaining budgets are present:
   - classify band using time-based thresholds (see TIME_BASED fallback below).
4. If percent-based telemetry is missing and time budgets are also missing:
   - classify as `YELLOW_FALLBACK` (User-approved throughput mode) with `input_quality=partial` (reason: `telemetry_missing_use_yellow`).
   - In this mode: allow normal internal work with reduced depth; block external/config/destructive actions.
5. If multiple band conditions match, choose the most restrictive band (`RED > ORANGE > YELLOW > GREEN`).

## Operating bands

### TIME_BASED (fallback when percent telemetry is missing)
Use remaining time budgets from `session_status` if available.

Suggested thresholds:
- GREEN: session remaining >= 2h AND context_used_pct < 55
- YELLOW: session remaining in [30m, 2h) OR context_used_pct in [55, 75]
- ORANGE: session remaining in [10m, 30m) OR context_used_pct > 75
- RED: session remaining < 10m

### YELLOW_FALLBACK (telemetry-missing, User-approved)
- Condition: percent telemetry missing and time budgets missing, but `context_used_pct` is valid.
- Cadence: 30 min (or task-driven)
- Mode: compact output, reduced deep analysis
- Allowed: internal analysis + reversible internal pilots
- Blocked: external/config/destructive actions, subagents unless User explicitly requests

(Deprecated)
### ORANGE_PARTIAL
- Previously used for missing session/day percent telemetry.
- This mode is deprecated because percent telemetry may be unavailable in current OpenClaw builds.

### GREEN
- Condition: `session_left_pct > 50` AND `day_left_pct > 40` AND `context_used_pct < 55`
- Cadence: 15 min
- Mode: standard
- Sub-agent allowance: up to 1 active

### YELLOW
- Condition: `session_left_pct in [25,50]` OR `day_left_pct in [20,40]` OR `context_used_pct in [55,75]`
- Cadence: 30 min
- Mode: compact output, reduced deep analysis
- Sub-agent allowance: 0 unless explicitly needed

### ORANGE
- Condition: `session_left_pct in [10,25]` OR `day_left_pct in [10,20]` OR `context_used_pct > 75`
- Cadence: 60 min
- Mode: critical tasks only, defer non-urgent synthesis
- Sub-agent allowance: 0

### RED
- Condition: `session_left_pct < 10` OR `day_left_pct < 10`
- Cadence: event-driven only
- Mode: safety/urgent only
- Sub-agent allowance: 0

## Behavior rules
- Before each run, classify current band.
- Apply cadence + depth + concurrency constraints from the band.
- Enforce cadence eligibility before START:
  - compute `elapsed_since_last_run_minutes` from last completed full run timestamp,
  - if `elapsed_since_last_run_minutes < cadence_minutes` and no urgent/HARD override, action must be `DEFER` with reason `cadence_not_due`.
  - scheduled/cron trigger alone is **not** a User override; User override requires explicit per-run instruction trace and reference.
- If band worsens mid-run, finish safely and downshift next cycle.

## Output compactness policy
- GREEN: normal detail.
- YELLOW: concise delta summaries.
- ORANGE/RED: minimal actionable output + deferred backlog list.

## Required trace fields
```yaml
quota_governor:
  timestamp: "ISO-8601"
  session_left_pct: 0
  day_left_pct: 0
  context_used_pct: 0
  input_quality: ok | partial | degraded
  input_quality_reason: "...|null"
  band: GREEN | YELLOW | ORANGE | ORANGE_PARTIAL | RED
  cadence_minutes: 15
  elapsed_since_last_run_minutes: 0
  cadence_due: true | false
  cadence_override: none | HARD | DANIEL_EXPLICIT
  cadence_override_ref: "string|null"
  deep_mode_allowed: true | false
  subagent_allowed: true | false
```
