# clue system

this project is a simple, text‑based setup for storing clues, checking them, and picking one at random. it started small and has been growing step by step, with each update building toward a more complete system.

---

## what this project does

- keeps all clues in one place (`clue.txt`)
- applies rules to make sure the clues are valid
- uses an engine to filter and pick a clue
- lets you adjust behavior through a config file
- documents the whole structure so it’s easy to follow

---

## how the files fit together

- **clue.txt** — the raw list of clues  
- **picker.md** — early ideas for how selection works  
- **spec.md** — the rules the system follows  
- **engine.md** — the logic and code prototypes  
- **config.md** — settings that control the engine  
- **architecture.md** — the big‑picture layout  
- **changelog.md** — the history of updates  

---

## how the system works (simple version)

1. clues are written in `clue.txt`  
2. the rules in `spec.md` decide what’s allowed  
3. the engine loads the clues and filters them  
4. the config file adjusts how the engine behaves  
5. one clue is chosen and returned  

---
result = pick_clue_with_config() print("chosen clue:", result)

---

## future ideas

- clue categories  
- weighted randomness  
- multiple output styles  
- plugin‑style extensions  

## example (pseudo‑python)
