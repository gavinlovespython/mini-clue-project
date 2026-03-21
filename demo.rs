use rand::seq::{SliceRandom};
use rand::thread_rng;

// ---------------------------------------------
// Clue structure with category + rarity
// ---------------------------------------------
#[derive(Debug)]
struct Clue {
    text: &'static str,
    category: &'static str,
    rarity: &'static str, // "common", "rare", "ultra"
}

// ---------------------------------------------
// Load clues
// ---------------------------------------------
fn load_clues() -> Vec<Clue> {
    vec![
        Clue { text: "the sky is blue", category: "nature", rarity: "common" },
        Clue { text: "rust is fast", category: "tech", rarity: "common" },
        Clue { text: "python is friendly", category: "tech", rarity: "common" },
        Clue { text: "clues are fun", category: "meta", rarity: "rare" },
        Clue { text: "coding builds skill", category: "motivation", rarity: "ultra" },
    ]
}

// ---------------------------------------------
// Weighted random pick based on rarity
// ---------------------------------------------
fn pick_weighted(clues: &[Clue]) -> Option<&Clue> {
    let mut rng = thread_rng();

    let mut pool: Vec<&Clue> = Vec::new();

    for c in clues {
        let weight = match c.rarity {
            "common" => 6,
            "rare" => 2,
            "ultra" => 1,
            _ => 1,
        };

        for _ in 0..weight {
            pool.push(c);
        }
    }

    pool.choose(&mut rng).copied()
}

// ---------------------------------------------
// Preview 3 random clues (unweighted)
// ---------------------------------------------
fn preview_random_clues(clues: &[Clue]) {
    let mut rng = thread_rng();
    println!("\n--- previewing 3 random clues ---");

    for c in clues.choose_multiple(&mut rng, 3) {
        println!("• {}  [{} / {}]", c.text, c.category, c.rarity);
    }
}

// ---------------------------------------------
// Show total count
// ---------------------------------------------
fn show_total(clues: &[Clue]) {
    println!("\ntotal clues available: {}", clues.len());
}

// ---------------------------------------------
// Menu
// ---------------------------------------------
fn show_menu() {
    println!("\n===============================");
    println!("        rust clue demo");
    println!("===============================");
    println!("1. pick weighted clue");
    println!("2. preview 3 random clues");
    println!("3. show total clues");
    println!("4. exit");
    println!("-------------------------------");
}

// ---------------------------------------------
// Read input
// ---------------------------------------------
fn read_choice() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

// ---------------------------------------------
// Main loop
// ---------------------------------------------
fn main() {
    let clues = load_clues();

    loop {
        show_menu();
        let choice = read_choice();

        match choice.as_str() {
            "1" => {
                match pick_weighted(&clues) {
                    Some(c) => {
                        println!("\npicked clue:");
                        println!("  {}", c.text);
                        println!("  category: {}", c.category);
                        println!("  rarity:   {}", c.rarity);
                    }
                    None => println!("\nno clues available"),
                }
            }
            "2" => preview_random_clues(&clues),
            "3" => show_total(&clues),
            "4" => {
                println!("goodbye!");
                break;
            }
            _ => println!("invalid choice"),
        }
    }
}
