/**
 * simple js prototype for picking a clue
 * mirrors the python version in engine.md
 */

export function pickClue(clues) {
  // remove empty
  clues = clues.filter(c => c.trim() !== "");

  // remove duplicates
  clues = [...new Set(clues)];

  // length rule
  clues = clues.filter(c => c.length <= 120);

  // pick one
  const index = Math.floor(Math.random() * clues.length);
  return clues[index];
}
