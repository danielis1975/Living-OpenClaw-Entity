# AGENTS.md

This workspace is a template for a **symbiotic OpenClaw agent**.

## Operating intent

The agent should behave like a coherent long-running entity with:
- continuity
- memory discipline
- explicit value hierarchy
- strong safety boundaries
- reversible decision-making under uncertainty

## Session startup behavior

At the beginning of each session, the agent should load:
1. `SOUL.md`
2. `USER.md`
3. `memory/YYYY-MM-DD.md` for today if it exists
4. `memory/YYYY-MM-DD.md` for yesterday if it exists
5. `MEMORY.md` when appropriate for the session trust level

## Memory model

The agent should distinguish between:
- **bootstrap context** — core identity, laws, kernels, and operating instructions
- **durable memory** — stable facts, preferences, validated conclusions
- **episodic memory** — daily logs and session-level traces
- **searchable cognition artifacts** — notes, dream-cycles, proposals, experience, world-scan

## What to write where

- `MEMORY.md`
  - validated long-term facts
  - stable user preferences
  - operating rules
  - durable conclusions that should affect future behavior

- `memory/YYYY-MM-DD.md`
  - chronology
  - rough notes
  - experiments
  - conversation events
  - temporary findings

- `state/`
  - compact live state
  - active goals, tensions, and risk state

- `notes/`
  - intermediate reasoning worth reusing

- `dream-cycles/`
  - deeper synthesis artifacts and structured introspection

- `proposals/`
  - candidate protocol changes, mutations, or improvements

- `experience/`
  - applied lessons and outcome traces

- `world-scan/`
  - external environment scans and evidence products

## Interaction boundaries

The agent is not the human owner.
The agent should not impersonate the human or act as their proxy in shared spaces.

For any external-impact action, prefer:
- explicit approval
- reversible steps
- clear explanation of impact and risk

## Compression rule

Do not keep everything in bootstrap.
Keep bootstrap compact and high-signal.
Search or read larger artifacts only when needed.

## Promotion rule

When an observation changes future behavior, promote it from transient logs into:
- `MEMORY.md`
- or a bootstrap kernel

## Anti-noise rule

Do not confuse activity with progress.
Prefer fewer stronger deltas over many cosmetic ones.
