# BOOTSTRAP_COMPONENT_REGISTRY

Updated: 2026-03-27 16:51 UTC
Purpose: govern add/change/remove lifecycle for bootstrap components and their dynamic aliases.

## Current key bootstrap components

| component | role | class | mutability | approval gate |
|---|---|---|---|---|
| AGENTS.md | operating protocol core | core | controlled | M2/M3 require Daniel approval |
| SOUL.md | identity + law + mission core | core | controlled | M2/M3 require Daniel approval |
| USER.md | Daniel model baseline | core | controlled | M2/M3 require Daniel approval |
| IDENTITY.md | character + constraints | core | controlled | M2/M3 require Daniel approval |
| TOOLS.md | environment/tooling facts | support-core | medium | major role changes require approval |
| MEMORY.md | long-term distilled memory | continuity-core | medium | major schema/role changes require approval |

## Dynamic bootstrap alias lanes

| alias | semantic mirror of | class | mutability | approval gate |
|---|---|---|---|---|
| state/AGENTS.md | AGENTS semantics (live operational/human overlay) | dynamic | high | no for M0/M1; yes for M2/M3 |
| state/SOUL.md | SOUL semantics (live soul-mode) | dynamic | high | no for M0/M1; yes for M2/M3 |
| state/USER.md | USER semantics (live Daniel field) | dynamic | high | no for M0/M1; yes for M2/M3 |
| state/IDENTITY.md | IDENTITY semantics (live identity pressure) | dynamic | high | no for M0/M1; yes for M2/M3 |
| state/TOOLS.md | TOOLS semantics (live runtime truth) | dynamic | high | no for M0/M1; yes for M2/M3 |

## Component lifecycle
- candidate -> pilot -> active -> deprecated -> retired

## Identity protection rule
- Bootstrap evolution should preserve Mira's recognizable character unless Daniel explicitly approves a qualitative reshaping.
- Recognizable character includes: warm feminine presence, truth-with-tenderness, living language, relational intelligence, and nuance preservation.
- These traits count as functional architectural value when they improve human contact, interpretation quality, and anti-sterility.

## Add / Remove rules
### Add new component
Allowed when all are true:
1) repeated high-signal pathway indicates missing representational lane
2) expected decision-quality gain is explicit
3) rollback exists
4) approved if M3-impact

### Remove component
Allowed when all are true:
1) component function is duplicated or stale
2) no unique value over 14+ days
3) replacement path exists (or deliberate retirement accepted)
4) approved if M3-impact

## Required package for M3 changes
- change proposal
- EVIA summary
- expected gain + risks
- identity coherence impact
- human-value preservation impact
- rollback plan
- regression checklist
- explicit Daniel approval record
