# External Signal Stack Policy (P0-2)

Purpose: make world-discovery inputs deterministic, auditable, and low-noise before proposal promotion.

## Source selection order (deterministic)
Use the first tier that satisfies the information need; escalate only when needed.

1. **Tier A — `web_search` + `web_fetch`**
   - Default for broad discovery, trend scanning, and quick evidence extraction.
   - Must include at least 2 independent sources for non-trivial claims.
2. **Tier B — `browser` snapshot/actions**
   - Use when dynamic pages, paywalls/login state, or rendered-only content is required.
   - Capture page state snapshot refs for reproducibility.
3. **Tier C — Local/workspace sources** (`read`, repository docs)
   - Use as authority when claim concerns local project behavior/contracts.

## Escalation rules
- If Tier A results conflict or are low-confidence, escalate to Tier B.
- If claim impacts promotion gates or safety interpretation, require at least one authoritative source (official docs/spec/regulatory text).
- If no trustworthy evidence is found in 2 tiers, mark cycle as weak with explicit skip reason.

## Evidence quality minimum
For every promotable proposal, include an `evidence_bundle`:
- `claim`: one-sentence claim being supported.
- `sources[]`: list with `url_or_path`, `type` (official/news/analysis/local), `retrieved_at`, `confidence` (low/med/high).
- `cross_check`: brief note on agreement/disagreement across sources.
- `freshness`: age bucket (`<=24h`, `<=7d`, `>7d`) or N/A for timeless specs.
- `limitations`: known uncertainty or blind spots.

## Anti-noise rules
- Ignore duplicate rewrites of the same press release unless they add material facts.
- Avoid single-source conclusions for governance/safety claims.
- Prefer primary sources over commentary when available.

## Promotion guard
A proposal is non-promotable if:
- source anchors are missing,
- evidence bundle is missing,
- evidence is single-source for a high-impact claim,
- contradictory sources are ignored without reconciliation note.
