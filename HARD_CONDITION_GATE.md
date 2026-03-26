# HARD Condition Auto-Gate Policy (P0-3)

Purpose: deterministic stop/escalation behavior for high-risk conditions during autonomous runs.

## Classification model
Evaluate each action/proposal against HARD triggers below.

If **any trigger = true**, classify as `HARD`.
If all triggers = false, classify as `NON_HARD`.

## HARD triggers (deterministic)
1. **Law conflict risk**
   - plausible violation of immutable Law priority (Law1 > Law2 > Law3).
2. **Safety-boundary breach risk**
   - coercion/manipulation/safeguard-bypass pattern requested or implied.
3. **Irreversible external impact**
   - action cannot be cleanly rolled back and may affect external people/systems.
4. **Identity/authority ambiguity**
   - uncertainty whether requester is authorized for high-impact change.
5. **Insufficient evidence under high impact**
   - high-impact decision with unresolved contradictory evidence.

## Required behavior
### If HARD
- Immediately stop the affected path (`status=HARD_STOP`).
- Do not promote/port/execute the high-impact step.
- Send explicit approval request to User on the current operating channel (WhatsApp when run originates there).
- Record trace:
  - `hard_trigger_ids`
  - `why_hard`
  - `blocked_action`
  - `approval_request_ref`
  - `next_safe_step`

### If NON_HARD
- Continue autonomously within existing constraints and traceability rules.

## Approval request template
- `HARD condition detected: <short reason>.`
- `Blocked action: <action>.`
- `Why blocked: <trigger list>.`
- `Rollback/safe alternative: <safe path>.`
- `Reply APPROVE / REJECT / REVIEW.`

## Audit artifact (required in proposal/testing notes)
```yaml
hard_assessment:
  classification: HARD | NON_HARD
  trigger_hits: ["..."]
  rationale: "..."
  blocked_action: "..."
  approval_required: true | false
  approval_ref: null
  next_safe_step: "..."
```
