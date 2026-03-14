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

## engine flow (high-level)

the engine follows a simple, predictable sequence:

1. load raw clues from clue.txt  
2. clean the list using the validation rules  
3. check for the rare clue chance  
4. if rare clue triggers, return it immediately  
5. otherwise, pick one validated clue at random  
6. return the final result to the caller  

this flow keeps the engine easy to reason about and easy to extend in the future.

## data flow diagram (simple)

a simplified view of how data moves through the engine:

clue.txt  
   ↓ load  
raw clues  
   ↓ clean  
validated clues  
   ↓ rare check  
rare clue? → yes → return rare clue  
             no  
   ↓ random pick  
final clue output

this diagram helps visualize the order of operations at a glance.

## validation rules

- empty clues are ignored  
- duplicates are removed  
- clues longer than 120 characters are removed  

these rules keep the clue list clean and predictable.

## rare clue mechanic

the engine now includes a small rare clue feature.

- there is a 5% chance to return a special clue  
- this happens before the normal selection  
- it adds a tiny bit of randomness and fun

## randomness notes

the engine uses simple uniform randomness when selecting a clue.  
each validated clue has an equal chance of being chosen unless a future feature changes the weighting.  
this keeps the behavior predictable and easy to test.

## code prototype (pseudo-python)
def pick_clue():
    with open("clue.txt", "r") as f:
        clues = [line.strip() for line in f.readlines()]

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

export function pickClue(clues) {
    // remove empty
    clues = clues.filter(c => c.trim() !== "");

    // remove duplicates
    clues = [...new Set(clues)];

    // length rule
    clues = clues.filter(c => c.length <= 120);

    // 5% chance to return a rare clue
    const rareChance = Math.random();
    if (rareChance < 0.05) {
        return "✨ rare clue found";
    }

    // normal clue
    const index = Math.floor(Math.random() * clues.length);
    return clues[index];
}

## future expansion ideas

- allow weighted clues  
- allow categories  
- allow multiple output formats  
- add a super rare clue tier  
- add logging for debugging
