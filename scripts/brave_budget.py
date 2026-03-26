#!/usr/bin/env python3
"""Simple Brave web_search usage counter (anonymized template).

This script does not call Brave. It only manages counters in memory/brave-budget.json.
Usage:
  python scripts/brave_budget.py can_use
  python scripts/brave_budget.py inc
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

STATE = Path(__file__).resolve().parent.parent / "memory" / "brave-budget.json"
DEFAULT_STATE = {
    "tz": "UTC",
    "day": None,
    "month": None,
    "dailyCap": 150,
    "monthlyCap": 3000,
    "dailyUsed": 0,
    "monthlyUsed": 0,
}


def ensure_state() -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    if not STATE.exists():
        STATE.write_text(json.dumps(DEFAULT_STATE, indent=2, ensure_ascii=False) + "\n")


def load() -> dict:
    ensure_state()
    return json.loads(STATE.read_text())


def save(data: dict) -> None:
    STATE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def now(tz: str) -> datetime:
    return datetime.now(ZoneInfo(tz))


def rollover(data: dict) -> dict:
    tz = data.get("tz", "UTC")
    n = now(tz)
    month = n.strftime("%Y-%m")
    day = n.strftime("%Y-%m-%d")

    if data.get("month") != month:
        data["month"] = month
        data["monthlyUsed"] = 0
    if data.get("day") != day:
        data["day"] = day
        data["dailyUsed"] = 0
    return data


def can_use(data: dict) -> bool:
    return (data["dailyUsed"] < data["dailyCap"]) and (data["monthlyUsed"] < data["monthlyCap"])


def inc(data: dict) -> dict:
    data["dailyUsed"] += 1
    data["monthlyUsed"] += 1
    return data


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    data = rollover(load())

    if cmd == "can_use":
        print("YES" if can_use(data) else "NO")
        save(data)
        return 0

    if cmd == "inc":
        if not can_use(data):
            print("BLOCK")
            save(data)
            return 1
        data = inc(data)
        save(data)
        print("OK")
        return 0

    print("usage: brave_budget.py can_use|inc", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
