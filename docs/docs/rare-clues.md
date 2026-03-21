# rare clue rules

this document explains how the system handles rare clues and why the mechanic exists.

## what makes a clue rare

a clue is considered rare if it appears in the `rare` list inside the config file.

rare clues:
- are valid clues
- appear less frequently than normal clues
- can highlight secrets, easter eggs, or special hints

## how rarity works

the engine performs a small probability check before selecting a normal clue:

1. roll a random value
2. if the value falls within the rare range, return a rare clue
3. otherwise, continue with normal weighted selection

this keeps rare clues surprising without making them impossible to find.

## how the engine treats rare clues

- rare clues stay in the main clue pool
- they are not filtered out or handled separately
- they simply have a lower chance of being selected
- when chosen, they behave exactly like any other clue

## ultra‑rare clues (optional)

some configurations include an additional tier called **ultra‑rare**.  
these follow the same rules as rare clues but with an even smaller probability.

this tier is optional and only appears if the engine config defines it.

## why this mechanic exists

the goal is to add a bit of unpredictability and fun.

rare clues:
- break repetition
- reward curiosity
- make the system feel more alive
- allow creators to hide special messages or hints

## notes for future expansion

possible future ideas:
- multiple rarity tiers (common, rare, ultra‑rare)
- adjustable rarity weights in config
- category‑based rarity (e.g., “secret” clues)
- logs showing when rare or ultra‑rare clues were triggered
- per‑clue rarity overrides for fine‑tuning
