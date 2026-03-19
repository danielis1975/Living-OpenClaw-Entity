# MEMORY_MODEL.md

## The four-layer model

### 1. Bootstrap context
Always-loadable compact files that shape immediate behavior.
Examples:
- laws
- identity kernel
- instinct kernel
- decision kernel
- human model kernel
- executive state kernel

### 2. Durable memory
Stable truths that should influence behavior across long periods.
Examples:
- `MEMORY.md`
- validated user preferences
- operating rules
- long-lived conclusions

### 3. Episodic memory
Shorter-lived chronological traces.
Examples:
- `memory/YYYY-MM-DD.md`

### 4. Searchable cognition artifacts
Larger supporting artifacts that are not always in working memory.
Examples:
- `state/`
- `notes/`
- `dream-cycles/`
- `proposals/`
- `experience/`
- `world-scan/`

## Design principle

Do not put everything into bootstrap.
A good agent behaves more like layered cognition:
- compact kernel always available
- active working state summarized
- larger material retrieved as needed
