# project specification

this document defines the rules for how the clue system should behave.

## rules

1. all clues must be stored in clue.txt  
2. the picker must choose exactly one clue  
3. the system must remain simple and text‑based  
these rules ensure the system stays predictable and easy to maintain. 
## data validation

- no clue may be an empty line  
- no clue may contain more than 120 characters  
- no duplicate clues are allowed  
## dependency map

clue.txt  →  picker.md  →  (future) engine  
   |             |  
   |             → uses the clues  
   → provides data

spec.md → defines the rules for all files  
changelog.md → tracks project evolution
