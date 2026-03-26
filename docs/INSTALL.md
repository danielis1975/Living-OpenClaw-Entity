# INSTALL.md

## Goal

Install this repository as the workspace for an OpenClaw agent.

If you are a non-technical user, start here first:
- `docs/INSTALL_FOR_BEGINNERS.md`

## Basic installation

1. Clone this repository to a workspace path.
2. Point the target agent workspace to this directory.
3. Customize the core files:
   - `IDENTITY.md`
   - `USER.md`
   - `MEMORY.md`
   - bootstrap kernels
4. Start or restart OpenClaw.

## Recommended OpenClaw settings

Recommended ideas for configuration:
- enable memory search
- enable memory sync on session start and on search
- add key root files to `memorySearch.extraPaths`
- optionally inject `bootstrap-kernels/*/*.md` via bootstrap-extra-files hook

## Suggested memorySearch extraPaths

Recommended extra paths:
- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `IDENTITY.md`
- `HEARTBEAT.md`
- `bootstrap-kernels`
- `state`
- `notes`
- `dream-cycles`
- `proposals`
- `experience`
- `world-scan`

## Trust note

Keep sensitive personal memory out of shared-context agents.
If you deploy multiple agents, give each one its own workspace and memory boundary.
