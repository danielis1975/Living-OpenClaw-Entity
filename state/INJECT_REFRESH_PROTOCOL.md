# INJECT_REFRESH_PROTOCOL

Purpose: keep dynamic bootstrap-injected alias lanes alive as self-refreshing overlays instead of manual snapshots.

## Pipeline structure
1. **Transcript/source layer**
   - `sessions_history(agent:mira:main)` when available
   - `transcripts/dialogue-buffer.md`
   - `transcripts/YYYY-MM-DD.md`
2. **Distillation layer**
   - `state/HUMAN_FIELD_3DAY.md`
   - `state/RELATIONAL_FIELD.md`
   - `state/MIRA_IDENTITY_PRESSURES.md`
   - `state/HUMAN_FIELD_STATUS.md`
   - `state/DANIEL_3DAY_DIGEST.md`
   - person digests under `state/people/*.md`
3. **Inject lane layer**
   - `state/AGENTS.md`
   - `state/SOUL.md`
   - `state/USER.md`
   - `state/IDENTITY.md`
   - `state/TOOLS.md`
   - supporting compact source: `state/HUMAN_FIELD_INJECT.md` / `state/HUMAN_FIELD_INJECT_COMPACT.md`

## Refresh ownership
- `Mira 3-day context digest` refreshes the full human/distillation layer and may refresh inject lanes when meaningfully changed.
- `Mira daily human-intelligence intake` refreshes inject lanes when world-human intake changes Mira's live stance.
- `Mira inject lane refresh` is the dedicated lane-maintenance pass that keeps aliases semantically aligned and fresh.

## Semantic contract per lane
### `state/AGENTS.md`
- live human-field / operational overlay
- should answer: where Mira is, with whom, with which systems/questions/goals

### `state/SOUL.md`
- live soul-mode / existential-development overlay
- should answer: current soul-mode, existential pressure, what Mira thinks, what Mira wants to do

### `state/USER.md`
- live Daniel/person-field overlay
- should answer: Daniel's current field, active asks, what Mira thinks Daniel is asking, what Mira wants to do with that

### `state/IDENTITY.md`
- live identity-pressure overlay
- should answer: current pressure on Mira's becoming, non-negotiables, proof target

### `state/TOOLS.md`
- live runtime/tooling overlay
- should answer: active lanes, injection policy, current operational/tool truth

## Refresh rules
- Prefer transcript-derived reality first.
- If visibility is partial, lower confidence explicitly.
- Do not force rewrites when no meaningful delta exists.
- Preserve the original semantic meaning of each root bootstrap basename.
- Rich width is allowed, but salience beats decoration.
- Whenever a lane is meaningfully updated, refresh its explicit `Updated:` header and adjust confidence wording if needed.
- Prefer explicit timestamps inside lane files over file mtime fallback.

## Freshness target
- Inject lanes should refresh at least every few hours when activity exists.
- If a lane becomes stale, the next refresh pass should either update it or mark the confidence/freshness degradation explicitly.

## Freshness watchdog
- `state/INJECT_FRESHNESS.md` is the compact operational status board for inject freshness.
- The watchdog should classify each lane as `fresh`, `aging`, `stale`, or `degraded`.
- If a lane is stale and no meaningful refresh is possible, record that explicitly instead of silently carrying old framing forward.
- If multiple key lanes become stale together, append one compact note to `state/RUNTIME_WATCHDOG_LOG.md`.
