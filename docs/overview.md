# overview

this document provides a simple overview of how the clue system works and how the pieces fit together.

## what the system does

the clue system loads a list of clues, validates them, applies optional mechanics like rarity, and returns one clue on request.  
the goal is to keep everything small, predictable, and easy to extend.

## core components

1. **clue storage**  
   - raw clue data lives in clue.txt  
   - each line represents one clue  

2. **validation**  
   - rules are defined in spec.md  
   - ensures clues follow formatting and structural requirements  

3. **engine**  
   - described in engine.md  
   - loads clues, validates them, applies filters, and selects the final clue  

4. **interface layer**  
   - currently conceptual  
   - future ui or api that will display or return the chosen clue  

## data flow

clue.txt → validation → engine → output clue

## design goals

- keep each layer simple  
- avoid hidden logic  
- allow small features to be added without breaking anything  
- make the system easy to read and easy to extend  

## notes

- celebrated hitting 100 commits on the mini clue project and the system continues to grow one tiny upgrade at a time
