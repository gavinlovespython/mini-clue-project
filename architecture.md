# system architecture

this document defines the high-level architecture of the clue system.

## overview

the system consists of four core components, each with a single, focused responsibility.

1. **clue storage**  
   - implemented by clue.txt  
   - contains raw clue data  

2. **validation layer**  
   - defined in spec.md  
   - ensures all clues follow the required rules  

3. **engine**  
   - described in engine.md  
   - loads, validates, filters, and selects clues  
   - applies optional features such as rarity and configuration settings

4. **interface layer**  
   - currently conceptual  
   - future component that will display or return the chosen clue  

## data flow

clue.txt → validation rules → engine → output clue

## architectural notes

- each layer is intentionally simple and replaceable  
- the engine is designed to grow without breaking existing behavior  
- configuration is kept external to avoid hard‑coding logic  

## future architecture goals

- modularize the engine into separate phases  
- allow multiple input sources (not just clue.txt)  
- support multiple output formats  
- introduce configuration files  
- support plugin-like extensions  
- improve documentation for each architectural layer  
- explore a lightweight API-style interface for external tools
