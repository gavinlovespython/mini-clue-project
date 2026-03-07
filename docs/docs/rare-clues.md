# rare clue rules

this file describes the small mechanic used for handling rare clues.

## what makes a clue rare

a clue is considered rare if it appears in the `rare` list inside the config file.
rare clues are still valid, but they are picked less often.

## how the engine treats them

- rare clues are included in the pool
- they have a lower chance of being selected
- the engine still returns them normally when chosen

## purpose

this mechanic adds a tiny bit of variety without making the system complicated.
