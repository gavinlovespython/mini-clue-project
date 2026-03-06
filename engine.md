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

## future expansion ideas

- allow weighted clues  
- allow categories  
- allow multiple output formats  
## code prototype (pseudo-python)

def pick_clue():
    with open("clue.txt", "r") as f:
        clues = [line.strip() for line in f.readlines()]

    # validation rules
    clues = [c for c in clues if c]  # remove empty
    clues = list(dict.fromkeys(clues))  # remove duplicates
    clues = [c for c in clues if len(c) <= 120]  # length rule

    import random
    return random.choice(clues)
