// tiny rust experiment for the clue project
// this is not wired into the main system yet.

fn pick_clue(clues: Vec<&str>) -> Option<&str> {
    if clues.is_empty() {
        return None;
    }

    // very simple: always return the first clue for now
    Some(clues[0])
}

fn main() {
    let clues = vec!["first clue", "second clue", "third clue"];

    match pick_clue(clues) {
        Some(clue) => println!("picked clue: {}", clue),
        None => println!("no clues available"),
    }
}
