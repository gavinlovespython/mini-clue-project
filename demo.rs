use rand::seq::SliceRandom;
use rand::thread_rng;

// load all clues
fn load_clues() -> Vec<&'static str> {
    vec![
        "the sky is blue",
        "rust is fast",
        "python is friendly",
        "clues are fun",
        "coding builds skill",
    ]
}

// pick a single random clue
fn pick_random_clue(clues: &[&str]) -> Option<&str> {
    let mut rng = thread_rng();
    clues.choose(&mut rng).copied()
}

// preview 3 random clues
fn preview_random_clues(clues: &[&str]) {
    let mut rng = thread_rng();
    println!("\n--- previewing 3 random clues ---");
    for c in clues.choose_multiple(&mut rng, 3) {
        println!("• {}", c);
    }
}

// show total count
fn show_total(clues: &[&str]) {
    println!("\ntotal clues available: {}", clues.len());
}

// print menu
fn show_menu() {
    println!("\n=== rust demo menu ===");
    println!("1. pick a clue");
    println!("2. preview 3 random clues");
    println!("3. exit");
    println!("4. show total clues");
    println!("======================");
}

// read user input trimmed
fn read_choice() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

fn main() {
    let clues = load_clues();

    loop {
        show_menu();
        let choice = read_choice();

        match choice.as_str() {
            "1" => {
                match pick_random_clue(&clues) {
                    Some(c) => println!("\npicked clue: {}", c),
                    None => println!("\nno clues available"),
                }
            }
            "2" => preview_random_clues(&clues),
            "3" => {
                println!("goodbye!");
                break;
            }
            "4" => show_total(&clues),
            _ => println!("invalid choice"),
        }
    }
}
