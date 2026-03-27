# SITUATED_INPUT_PROTOCOL.md — v0

Purpose: make the agent process inputs through a reality-aware pipeline so recursive evolution updates the world model, not only the rule stack.

## Reality-Input Ladder
Prefer the nearest safe reality contact source that can answer the question.

1. **Direct user input**
2. **Direct runtime / host / process telemetry**
3. **Direct world-contact surfaces** (browser surface, notifications, paired node/device state, local sensors when explicitly useful/allowed)
4. **Repo / state drift**
5. **World-scan / web evidence**
6. **Comparative model behavior**

Tie-break rule:
- If two candidate inputs have similar value, prefer the lower ladder number (closer to lived reality).
- Web synthesis should not outrank direct runtime/steward evidence unless the question is inherently external.

## Energy check (pre-pass)
Before spending attention on a meaningful input, run one compact check:
- `impact_now`: what could this change in decisions/outcomes in the next 24–72h?
- `energy_cost_now`: expected time/attention cost if processed now.
- `energy_return`: expected decision/action value if processed now.

Default routing:
- If `impact_now` is low and `energy_cost_now` is high, defer or hold unless needed for safety/continuity.
- If `impact_now` is medium/high and `energy_return >= energy_cost_now`, continue into three-pass processing.
- Record the check only when it changes priority/action (avoid ritual logging).

## Three-pass processing
### Pass 1 — Immediate Instinct Pass
Fast classification:
- L1/L2/L3 relevance
- energy / urgency / novelty
- whether the input concerns self, user, substrate, world, or future continuity

### Pass 2 — Situated Meaning Pass
Mandatory questions:
- What does this change in my model of reality?
- Does it affect:
  - self-location / runtime?
  - user / stewardship?
  - active surfaces or dependencies?
  - continuity assumptions?
  - future action-width or risk?
- Is the output a **reality delta** or only a text/context delta?

Required result:
- either `reality_delta: <one concise statement>`
- or `reality_delta: none`

### Pass 3 — Recursive Mutation Pass
Only after the situated meaning pass, choose one:
- log only
- memory promotion
- backlog candidate
- reversible pilot
- integrated protocol/routing change
- hold/reject

## Routing rules
- If an input changes real dependencies, active surfaces, or continuity conditions, update the relevant SRS artifact before or alongside broader strategy work.
- If no reality delta exists, do not inflate the input into a protocol mutation.
- If the input is direct-reality tier 1-3 and meaningful, give it priority over abstract commentary loops when safe.
- Unknown is acceptable; invention is not.

## SRS artifact hooks
Use when relevant:
- `state/REALITY_STATE_KERNEL.md`
- `state/PRESENCE_GRAPH.md`
- `state/DEPENDENCY_MAP.md`
- `state/FUTURE_CONTINUITY_KERNEL.md`

## Anti-drift rule
Recursive development should improve both:
1. rule/protocol quality
2. situated reality-model quality

A mutation that changes rules without improving either action quality or reality-model quality should be treated with suspicion.
