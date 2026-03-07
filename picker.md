# clue picker

the picker is the conceptual layer that decides *how* a clue is chosen.
it sits between the raw data (clue.txt) and the engine logic.

## how this will work

the picker will eventually read all clues from clue.txt and choose one at random.
this is just the planning stage.

## metadata

- source file: clue.txt  
- purpose: select one clue from the list  
- status: planning stage  
- maintained: updated as design evolves
## role in the system

the picker does not perform the actual selection.
instead, it defines the rules and expectations for how selection should work.
this helps keep the engine focused on processing rather than decision logic.
keeping these responsibilities separate makes the system easier to maintain.
## note

this file is now maintained through pull requests to keep the workflow clean.
the engine (python or js) will eventually implement these rules.
this helps ensure changes stay organized and easy to review.
## future integration

- connect picker.md logic to engine.md (python prototype)
- connect picker.md logic to engine.js (javascript prototype)
- allow picker to choose between engines based on config.md
- document how the picker hands off data to the engine
