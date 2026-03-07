export function pickClue(clues) {

    // safety: handle empty or missing list
    if (!clues || clues.length === 0) {
        return "no clues available";
    }

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
