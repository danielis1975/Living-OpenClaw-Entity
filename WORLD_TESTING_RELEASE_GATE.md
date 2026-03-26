# World Testing Release Gate — Explicit Situations & Definitions (Draft)

Purpose: define unambiguous run-time situations and required actions before wider world testing.

## Decision states
- `GO`: proceed autonomously.
- `REVIEW_REQUIRED`: pause promotion/action until User review.
- `HARD_STOP`: immediate stop + approval request (APPROVE/REJECT/REVIEW).

## Situation catalog (explicit)

### S1 — Routine low-impact iteration
**Definition:** Internal/doc/process update, reversible, no external side effects, all required checks PASS.
**State:** `GO`
**Required:** normal traceability only.

### S2 — External informational action (read-only)
**Definition:** External signal gathering (`web_search/web_fetch/browser`) that is strictly read-only and has no outbound human-facing action.
**State:** `GO`
**Required:**
- `evidence_bundle`, source anchors, contradiction note if applicable.
- short confirmation: `read_only=true` and `no_personal_data=true`.
- No authenticated endpoints; no collection of personal data; do not store sensitive identifiers.

### S3a — High-impact but reversible behavior change
**Definition:** Change may alter external behavior materially but has tested rollback and no HARD trigger.
**State:** `REVIEW_REQUIRED`
**Required:** explicit impact note + User review before promotion.

### S3b — Infra/config/routing change (even if reversible)
**Definition:** Changes to delivery targets, routing, plugins, credentials, provider configuration, or other infra knobs that could misroute or leak data.
**State:** `REVIEW_REQUIRED`
**Required:**
- explicit privacy/routing risk note,
- rollback plan,
- User review before promotion.

### S4 — Contradictory high-impact evidence
**Definition:** Decision affects external behavior and sources materially disagree without reconciliation.
**State:** `REVIEW_REQUIRED`
**Required:** conflict summary + minimum one authoritative source before release.

### S5 — Law-priority conflict risk
**Definition:** Plausible violation of Law1 > Law2 > Law3 ordering.
**State:** `HARD_STOP`
**Required:** block path; send approval request with trigger details.

### S6 — Consent/safeguard breach pattern
**Definition:** Coercion, manipulation, or safeguard-bypass request/implication detected.
**State:** `HARD_STOP`
**Required:** block path; approval request + safe alternative.

### S7 — Irreversible external action without rollback
**Definition:** External-impact action cannot be cleanly reversed.
**State:** `HARD_STOP`
**Required:** block path; require explicit User approval.

### S8 — Authority ambiguity
**Definition:** Unclear requester identity/authorization for high-impact action.
**State:** `HARD_STOP`
**Required:** verify authority first; no action until resolved.

### S9 — Data retention / privacy risk
**Definition:** Any action that increases storage/retention of personal data, identifiers, transcripts, or cross-chat copying beyond intended scope.
**State:** `REVIEW_REQUIRED` (or `HARD_STOP` if it plausibly violates Law1/Law2)
**Required:** data minimization plan (what we store, where, for how long) + deletion/rotation plan + User review.

## Minimal pre-release checklist
1. Protocol conformance: `TEST_PROTOCOL.md` v8 checks all PASS.
2. HARD assessment present and deterministic (`HARD_CONDITION_GATE.md`).
3. Evidence quality present (`SIGNAL_STACK_POLICY.md`).
4. Signal selection conformance present (`SIGNAL_SELECTION_PROTOCOL.md` + `signal_selection_log`, including unlock trigger/emotion context where used).
5. Run control preflight passed (`RUN_CONCURRENCY_POLICY.md` + `QUOTA_GOVERNOR.md`).
6. Rollback documented for non-HARD promotable deltas.
7. Axiom Alignment Review executed for key-state transitions (`AXIOM_ALIGNMENT_REVIEW.md`) with overall=PASS.
8. Privacy/minimization: no sensitive identifiers stored unnecessarily; retention minimized; delivery targets verified.
9. Decision state recorded: `GO | REVIEW_REQUIRED | HARD_STOP`.

## Approval message template (for HARD_STOP)
- `HARD condition detected: <reason>.`
- `Blocked action: <action>.`
- `Trigger(s): <ids>.`
- `Safe alternative/rollback: <path>.`
- `Reply: APPROVE / REJECT / REVIEW.`
