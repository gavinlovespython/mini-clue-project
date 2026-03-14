export function pickClue(clues, options = {}) {

    // config with optional features
    const config = {
        logging: options.logging || false,
        seed: options.seed || null,
        ultraRareChance: 0.01,
        rareChance: 0.05,
        maxLength: 120
    };

    // optional seeded RNG
    let rng = Math.random;
    if (config.seed !== null) {
        let s = config.seed % 2147483647;
        if (s <= 0) s += 2147483646;
        rng = () => (s = s * 16807 % 2147483647) / 2147483647;
    }

    const log = (...msg) => {
        if (config.logging) console.log("[engine]", ...msg);
    };

    // safety: missing list
    if (!clues || clues.length === 0) {
        log("no clues provided");
        return "no clues available";
    }

    // sanitize + trim
    clues = clues.map(c => c.trim());

    // remove empty
    clues = clues.filter(c => c !== "");

    // remove duplicates
    clues = [...new Set(clues)];

    // length rule
    clues = clues.filter(c => c.length <= config.maxLength);

    // if everything got filtered out
    if (clues.length === 0) {
        log("all clues filtered out");
        return "no valid clues";
    }

    // rarity roll
    const roll = rng();
    log("rarity roll:", roll.toFixed(4));

    if (roll < config.ultraRareChance) {
        log("ultra rare triggered");
        return "💎 ultra‑rare clue discovered";
    }

    if (roll < config.rareChance) {
        log("rare triggered");
        return "✨ rare clue found";
    }

    // weighted scoring system
    const scored = clues.map(c => {
        let weight = 1;

        // keyword boosts
        const lower = c.toLowerCase();
        if (lower.includes("secret")) weight += 2;
        if (lower.includes("warning")) weight += 1;

        // short clues get a tiny boost
        if (c.length < 40) weight += 0.5;

        return { text: c, weight };
    });

    // compute total weight
    const totalWeight = scored.reduce((sum, item) => sum + item.weight, 0);

    // weighted pick
    let pick = rng() * totalWeight;

    for (const item of scored) {
        if (pick < item.weight) {
            log("picked:", item.text);
            return item.text;
        }
        pick -= item.weight;
    }

    // fallback (should never hit)
    log("fallback triggered");
    return clues[0];
}
