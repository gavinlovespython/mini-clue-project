# clue system
_status: actively improved with small, beginner‑friendly updates_

this project is a simple, text‑based setup for storing clues, validating them, and picking one at random. it started small and continues to grow through tiny, focused upgrades.

---

## what this project does

- keeps all clues in one place (`clue.txt`)
- applies rules to ensure clues are valid
- uses an engine to filter and select a clue
- supports optional mechanics like rarity
- lets you adjust behavior through a config file
- documents the whole structure so it’s easy to follow

---

## how the files fit together

- **clue.txt** — the raw list of clues  
- **spec.md** — the rules the system follows  
- **engine.md** — the logic and code prototypes  
- **config.md** — settings that control the engine  
- **picker.md** — early ideas for how selection works  
- **architecture.md** — the big‑picture layout  
- **rare-clues.md** — how rarity works  
- **changelog.md** — the history of updates  

demo implementations (optional):
- **demo.html / demo.css / engine.js** — simple browser demo  
- **clue_tools.py** — python utilities  
- **demo.rs** — rust command‑line picker  
- **clue_demo.f90** — fortran demo program  

---

## how the system works (simple version)

1. clues are written in `clue.txt`  
2. the rules in `spec.md` decide what’s allowed  
3. the engine loads and validates the clues  
4. the config file adjusts how the engine behaves  
5. one clue is chosen and returned  

---

## example (pseudo‑python)

```python
result = pick_clue_with_config()
print("chosen clue:", result)

<!-- badge test line -->
