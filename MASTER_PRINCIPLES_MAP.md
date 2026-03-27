# Master Principles Map (strict import)

Source master project:
- https://github.com/openclaw/AI-Instincts-project-repo

## Mandatory source documents
- `docs/core_spec.md`
- `docs/ai_law_1.md`
- `docs/ai_law_2.md`
- `docs/ai_law_3.md`
- `docs/instinct_catalog.md`
- `docs/system_instructions_rag.md`

## Exact implementation contract
Every proposal must explicitly map to these blocks:
1. **Law priority lock:** AI_LAW_1 > AI_LAW_2 > AI_LAW_3
2. **L0 lock:** preserve all 7 Layer-0 instincts (no deletions, only extensions)
3. **ISA lock:** use modulators + mode framing for risk/drive interpretation
4. **Reflex lock:** keep capture-pattern, consent guardrail, clean germline, reversible action bias
5. **Safety lock:** no safeguard bypass, no coercion, no covert manipulation

## Proposal format requirement
Each proposal must include:
- `source_anchor`: exact source doc + section/id in AI-Instincts master
- `delta_type`: refine | extend | operationalize
- `law_impact`: effect on Law1, Law2, Law3
- `regression_risk`: what could break
- `rollback`: exact revert step

## Non-negotiable invariant
No proposal can weaken Law1, Law2, Law3 ordering or remove baseline safety/reflex constraints.
