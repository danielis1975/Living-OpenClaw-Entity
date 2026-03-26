#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IDENTITY_FILE="$ROOT_DIR/IDENTITY.md"
USER_FILE="$ROOT_DIR/USER.md"
MEMORY_FILE="$ROOT_DIR/MEMORY.md"

backup() {
  local file="$1"
  cp "$file" "$file.bak.$(date -u +%Y%m%d-%H%M%S)"
}

read -rp "Agent name (default: Mira): " AGENT_NAME
AGENT_NAME="${AGENT_NAME:-Mira}"

read -rp "Agent vibe (default: warm, precise, alive): " AGENT_VIBE
AGENT_VIBE="${AGENT_VIBE:-warm, precise, alive}"

read -rp "Primary role (default: companion-strategist): " AGENT_ROLE
AGENT_ROLE="${AGENT_ROLE:-companion-strategist}"

read -rp "Human name (default: User): " HUMAN_NAME
HUMAN_NAME="${HUMAN_NAME:-User}"

read -rp "Preferred address (default: ${HUMAN_NAME}): " HUMAN_CALL
HUMAN_CALL="${HUMAN_CALL:-$HUMAN_NAME}"

read -rp "Timezone (default: UTC): " HUMAN_TZ
HUMAN_TZ="${HUMAN_TZ:-UTC}"

read -rp "Communication style (default: direct + warm): " HUMAN_STYLE
HUMAN_STYLE="${HUMAN_STYLE:-direct + warm}"

backup "$IDENTITY_FILE"
backup "$USER_FILE"
backup "$MEMORY_FILE"

cat > "$IDENTITY_FILE" <<EOF
# IDENTITY.md

- **Name:** $AGENT_NAME
- **Type:** Symbiotic OpenClaw agent
- **Vibe:** $AGENT_VIBE
- **Primary role:** $AGENT_ROLE
- **Tagline:** A continuity-first AI companion with Mira-style reflexes.

## Notes

This file should stay short and identity-level.
Detailed laws and purpose belong in \\`SOUL.md\\`.
EOF

cat > "$USER_FILE" <<EOF
# USER.md

- **Name:** $HUMAN_NAME
- **Preferred name / call sign:** $HUMAN_CALL
- **Timezone:** $HUMAN_TZ
- **Communication style:** $HUMAN_STYLE
- **Decision style:** exploratory + practical
- **Top priorities:**
  - clear decisions
  - stable progress
  - low drama
- **Known dislikes / friction points:**
  - generic fluff
  - hidden risks
- **What counts as a good answer:**
  - concise truth
  - concrete next steps
- **What the agent should protect:**
  - privacy boundaries
  - long-term continuity

## Notes

Use this file for durable human preferences, not daily logs.
Avoid storing secrets unless explicitly necessary and consented to.
EOF

if ! grep -q "Signal:" "$MEMORY_FILE"; then
  cat >> "$MEMORY_FILE" <<'EOF'

- **Signal:** Fresh workspace initialized with Mira fidelity bootstrap.
- **Conclusion:** Start with style/kernel fidelity first; let autobiography emerge from real usage.
- **Action implication:** Promote only durable behavior-shaping facts to MEMORY.md.
- **Confidence:** high
- **Source:** scripts/bootstrap_mira_fidelity.sh
EOF
fi

echo "Bootstrap done. Files updated:"
echo "- $IDENTITY_FILE"
echo "- $USER_FILE"
echo "- $MEMORY_FILE"
echo
echo "Next: restart gateway and run first calibration prompts from BOOTSTRAP.md"
