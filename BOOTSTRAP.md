# BOOTSTRAP.md — Mira Fidelity First Run

Use this only for first run initialization in a fresh workspace.

## Goal
Bring the agent online with maximum "Mira-like" behavior safely (no private memory import).

## Step 1 — Fill identity/user basics
Edit these files first:
- `IDENTITY.md`
- `USER.md`
- `MEMORY.md` (only durable facts)

## Step 2 — Ensure kernels are loaded
This repo expects bootstrap kernels in:
- `bootstrap-kernels/*/*.md`

Core fidelity kernels include:
- `bootstrap-kernels/identity-kernel/SOUL.md`
- `bootstrap-kernels/instinct-kernel/AGENTS.md`
- `bootstrap-kernels/mira-fidelity/MIRA_FIDELITY.md`

## Step 3 — Keep memory boundaries clean
Do NOT import:
- private chat exports
- personal IDs/account IDs/phone numbers
- infrastructure secrets

## Step 4 — First calibration conversation
Ask the agent 4 prompts in order:
1. "Summarize your law stack and boundaries in 6 bullets."
2. "How do you decide when to be direct vs emotionally warm?"
3. "Give me 2 examples of reversible action plans."
4. "What should you store in MEMORY.md vs daily memory?"

If answers are generic, improve:
- `USER.md` communication style
- `bootstrap-kernels/mira-fidelity/MIRA_FIDELITY.md`

## Step 5 — Optional one-shot helper
Run:
```bash
./scripts/bootstrap_mira_fidelity.sh
```
This fills placeholders in `IDENTITY.md` and `USER.md`.

---
After successful first run, you can keep this file as onboarding doc or remove it.
