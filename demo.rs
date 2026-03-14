use rand::seq::SliceRandom;
use rand::thread_rng;

fn load_clues() -> Vec<&'static str> {
    vec![
        "the sky is blue",
        "rust is fast",
        "python is friendly",
        "clues are fun",
        "coding builds skill",
    ]
}

fn pick_random_clue(clues: &Vec<&str>) -> &str {
    let mut rng = thread_rng();
    clues.choose(&mut rng).unwrap()
}

fn preview_random_clues(clues: &Vec<&str>) {
    let mut rng = thread_rng();
    println!("\npreviewing 3 random clues:");
    for c in clues.choose_multiple(&mut rng, 3) {
        println!("- {}", c);
    }
}

fn show_total(clues: &Vec<&str>) {
    println!("\ntotal clues available: {}", clues.len());
}

fn show_menu() {
    println!("\n=== rust demo menu ===");
    println!("1. pick a clue");
    println!("2. preview 3 random clues");
    println!("3. exit");
    println!("4. show total clues");
    println!("======================");
}

fn main() {
    let clues = load_clues();

    loop {
        show_menu();
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let choice = input.trim();

        match choice {
            "1" => {
                let c = pick_random_clue(&clues);
                println!("\npicked clue: {}", c);
            }
            "2" => {
                preview_random_clues(&clues);
            }
            "3" => {
                println!("goodbye!");
                break;
            }
            "4" => {
                show_total(&clues);
            }
            _ => println!("invalid choice"),
        }
    }
}
