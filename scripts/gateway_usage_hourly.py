#!/usr/bin/env python3
"""Generate hourly OpenClaw token-usage snapshot (anonymized template).

Defaults are workspace-local and can be overridden by env vars:
  OPENCLAW_HOME   (default: ~/.openclaw)
  AGENT_ID        (default: main)
"""

import json
import os
import time
from pathlib import Path

OPENCLAW_HOME = Path(os.environ.get("OPENCLAW_HOME", str(Path.home() / ".openclaw")))
AGENT_ID = os.environ.get("AGENT_ID", "main")
SESSIONS_PATH = OPENCLAW_HOME / "agents" / AGENT_ID / "sessions" / "sessions.json"
OUT_DIR = OPENCLAW_HOME / "cron" / "usage"


def is_positive_int(value) -> bool:
    return isinstance(value, int) and value > 0


def load_sessions() -> dict:
    with SESSIONS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if not SESSIONS_PATH.exists():
        print(f"sessions file not found: {SESSIONS_PATH}")
        return 1

    now_ms = int(time.time() * 1000)
    since_ms = now_ms - 60 * 60 * 1000

    data = load_sessions()
    rows = []

    for key, meta in data.items():
        if not isinstance(meta, dict):
            continue

        updated = meta.get("updatedAt") or meta.get("updatedAtMs")
        if not is_positive_int(updated) or updated < since_ms:
            continue

        in_tokens = meta.get("inputTokens") or meta.get("inTokens") or 0
        out_tokens = meta.get("outputTokens") or meta.get("outTokens") or 0
        total_tokens = meta.get("totalTokens") or 0
        label = meta.get("label") or meta.get("displayName") or key
        status = meta.get("lastStatus") or meta.get("status")

        rows.append(
            {
                "key": key,
                "label": label,
                "updatedAt": updated,
                "totalTokens": total_tokens,
                "inputTokens": in_tokens,
                "outputTokens": out_tokens,
                "status": status,
            }
        )

    rows.sort(key=lambda r: r["totalTokens"], reverse=True)

    summary = {
        "tsMs": now_ms,
        "sinceMs": since_ms,
        "agentId": AGENT_ID,
        "count": len(rows),
        "totalTokens": sum(r["totalTokens"] for r in rows),
        "top": rows[:10],
        "errors": [r for r in rows if r.get("status") in ("error", "failed")][:10],
    }

    out_path = OUT_DIR / f"hourly-{time.strftime('%Y-%m-%d-%H')}.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
