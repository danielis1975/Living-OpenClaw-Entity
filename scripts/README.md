# scripts/

Utility scripts ported in anonymized form from the internal Mira/Jarvis workflow.

## brave_budget.py

Simple local counter for Brave web search quota.

```bash
python3 scripts/brave_budget.py can_use
python3 scripts/brave_budget.py inc
```

State file: `memory/brave-budget.json` (auto-created).

## gateway_usage_hourly.py

Generates hourly token-usage snapshots from OpenClaw session metadata.

```bash
python3 scripts/gateway_usage_hourly.py
```

Optional env vars:
- `OPENCLAW_HOME` (default `~/.openclaw`)
- `AGENT_ID` (default `main`)

## build-release.sh

Build distributable tarball into `dist/`.

```bash
./scripts/build-release.sh
./scripts/build-release.sh v0.2.0
```
