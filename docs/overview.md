# overview

this document provides a simple overview of how the clue system works and how the pieces fit together.

## what the system does

the clue system loads a list of clues, validates them, applies optional mechanics like rarity, and returns one clue on request.  
the goal is to keep everything small, predictable, and easy to extend.

## core components

1. **clue storage**  
   - raw clue data lives in `clue.txt`  
   - each line represents one clue  
   - future versions may support multiple input files

2. **validation**  
   - rules are defined in `spec.md`  
   - ensures clues follow formatting and structural requirements  
   - prevents malformed or oversized clues from entering the engine

3. **engine**  
   - described in `engine.md`  
   - loads clues, validates them, applies filters, and selects the final clue  
   - supports optional rarity mechanics and weighted selection

4. **interface layer**  
   - currently conceptual  
   - future ui or api that will display or return the chosen clue  
   - demo implementations exist in html, rust, python, and fortran

## data flow
clue.txt → validation → engine → output clue

## design goals

- keep each layer simple  
- avoid hidden logic  
- allow small features to be added without breaking anything  
- make the system easy to read and easy to extend  
- keep behavior predictable even as new languages and demos are added

## notes

- celebrated hitting 100 commits on the mini clue project  
- the system continues to grow through small, focused upgrades  
