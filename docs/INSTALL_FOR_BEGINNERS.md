# INSTALL_FOR_BEGINNERS.md (OpenClaw)

This is the easiest path for non-technical users.

## 0) What you are installing
You are installing a **personality + behavior workspace** for OpenClaw.
It is not a standalone app by itself.

## 1) Get the files
Clone this repository into a folder on your machine:

```bash
git clone https://github.com/danielis1975/Living-OpenClaw-Entity.git
```

Example folder created:
`~/Living-OpenClaw-Entity`

## 2) Point OpenClaw agent to this workspace
Open your OpenClaw config file:
- usually: `~/.openclaw/openclaw.json`

Set your target agent workspace to this folder.

Example (inside `agents.list`):
```json
{
  "id": "main",
  "name": "main",
  "workspace": "/home/you/Living-OpenClaw-Entity"
}
```

## 3) Ensure bootstrap kernels are auto-loaded
In config, enable bootstrap-extra-files hook:

```json
"hooks": {
  "internal": {
    "enabled": true,
    "entries": {
      "bootstrap-extra-files": {
        "enabled": true,
        "paths": ["bootstrap-kernels/*/*.md"]
      }
    }
  }
}
```

## 4) Restart OpenClaw gateway
```bash
openclaw gateway restart
```

## 5) Personalize the minimum files
Edit these files:
- `IDENTITY.md` (agent name + vibe)
- `USER.md` (your style/preferences)
- `MEMORY.md` (durable facts only)

Optional helper:
```bash
./scripts/bootstrap_mira_fidelity.sh
```

## 6) First chat test
Ask:
- "Who are you and what are your core laws?"
- "How do you handle risky requests?"
- "How do you keep memory boundaries?"

If behavior feels too generic, tune:
- `bootstrap-kernels/mira-fidelity/MIRA_FIDELITY.md`
- `USER.md`

## 7) HD voice quality (optional)
Default local route can use Piper (if configured in your environment).
Use OpenAI TTS only when explicitly requested for HD/high quality.

---
If you get stuck, open:
- `docs/INSTALL.md` (technical version)
- `docs/CUSTOMIZATION.md`
