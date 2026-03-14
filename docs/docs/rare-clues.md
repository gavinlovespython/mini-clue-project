# rare clue rules

this document explains how the system handles rare clues and why the mechanic exists.

## what makes a clue rare

a clue is considered rare if it appears in the `rare` list inside the config file.

rare clues:
- are valid clues
- appear less frequently than normal clues
- can be used to highlight special hints, secrets, or easter eggs

## how rarity works

the engine uses a small probability check before picking a normal clue.

1. the system rolls a random value
2. if the value falls within the rare range, a rare clue is returned
3. otherwise, the engine continues with normal clue selection

this keeps rare clues surprising without making them impossible to find.

## how the engine treats rare clues

- rare clues are included in the overall clue pool
- they are not removed or filtered out
- they simply have a lower chance of being selected
- when chosen, they behave exactly like any other clue

## why this mechanic exists

the goal is to add a bit of unpredictability and fun.

rare clues:
- break repetition
- reward curiosity
- make the system feel more alive
- allow creators to hide special messages or hints

## notes for future expansion

ideas that might be added later:
- multiple rarity tiers (common, rare, ultra-rare)
- rarity weights that can be tuned in config
- category-based rarity (e.g., “secret” clues)
- logs showing when rare clues were triggered
