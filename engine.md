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
## config-aware prototype

def load_config():
    return {
        "allow_duplicates": False,
        "max_length": 120,
        "random_seed": None,
        "output_format": "text"
    }

def pick_clue_with_config():
    cfg = load_config()

    with open("clue.txt", "r") as f:
        clues = [line.strip() for line in f.readlines()]

    # apply config rules
    if not cfg["allow_duplicates"]:
        clues = list(dict.fromkeys(clues))

    clues = [c for c in clues if c and len(c) <= cfg["max_length"]]

    import random
    if cfg["random_seed"] is not None:
        random.seed(cfg["random_seed"])

    return random.choice(clues)
