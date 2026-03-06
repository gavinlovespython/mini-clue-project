# engine design

the engine is responsible for:
- loading all clues from clue.txt
- validating them using the rules in spec.md
- selecting exactly one clue
- returning the chosen clue to the user or another system

## algorithm (draft)

1. read clue.txt line by line  
2. remove empty lines  
3. remove duplicates  
4. discard clues longer than 120 characters  
5. store the remaining clues in a list  
6. choose one clue at random  
7. output the chosen clue  

## validation rules

- empty clues are ignored  
- duplicates are removed  
- clues longer than 120 characters are removed  

these rules keep the clue list clean and predictable.

## rare clue mechanic

the engine now includes a small “rare clue” feature.

- there is a 5% chance to return a special clue  
- this happens before the normal selection  
- it adds a tiny bit of randomness and fun

## code prototype (pseudo-python)
def pick_clue(): with open("clue.txt", "r") as f: clues = [line.strip() for line in f.readlines()]
# validation rules
clues = [c for c in clues if c]  # remove empty
clues = list(dict.fromkeys(clues))  # remove duplicates
clues = [c for c in clues if len(c) <= 120]  # length rule

import random

# rare clue
if random.random() < 0.05:
    return "✨ rare clue found"

return random.choice(clues)

## javascript version

the js version follows the same rules and includes the rare clue mechanic.
export function pickClue(clues) { // remove empty clues = clues.filter(c => c.trim() !== "");
// remove duplicates clues = [...new Set(clues)];
// length rule clues = clues.filter(c => c.length <= 120);
// 5% chance to return a rare clue const rareChance = Math.random(); if (rareChance < 0.05) { return "✨ rare clue found"; }
// normal clue const index = Math.floor(Math.random() * clues.length); return clues[index]; }

## future expansion ideas

- allow weighted clues  
- allow categories  
- allow multiple output formats  
- add a “super rare” clue tier  
- add logging for debugging  
