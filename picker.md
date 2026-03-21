# clue picker

the picker is the conceptual layer that defines *how* a clue should be chosen.  
it sits between the raw data (`clue.txt`) and the engine logic.

## purpose

the picker describes the rules, expectations, and decision model for clue selection.  
it does **not** perform the actual selection — that is the engine’s job.  
this separation keeps the system maintainable and easier to evolve.

## how this will work

the picker will eventually read all clues from `clue.txt` and define how one is chosen at random.  
this document represents the planning stage for that behavior.

## metadata

- source: `clue.txt`  
- purpose: define selection rules  
- status: planning  
- maintenance: updated as design evolves  

## role in the system

the picker defines the *logic model* for selection, not the implementation.  
it ensures the engine stays focused on processing, validation, and randomness.  
keeping these responsibilities separate improves clarity and maintainability.

## workflow note

this file is maintained through pull requests to keep changes organized.  
the engine (python or js) will eventually implement the rules defined here.

## future integration

- connect picker.md logic to `engine.md` (python prototype)  
- connect picker.md logic to `engine.js` (javascript prototype)  
- allow picker to choose between engines based on `config.md`  
- document how the picker hands off data to the engine  
