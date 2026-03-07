# run.py
# upgraded entry point for the clue system

from engine import pick_clue_with_config
from engine import load_clues  # assuming this exists in your engine
from config import load_config  # assuming this exists too

def show_menu():
    print("\n=== clue system menu ===")
    print("1. pick a clue")
    print("2. show total number of clues")
    print("3. preview rare clues")
    print("4. exit")
    print("========================")

def action_pick_clue():
    try:
        result = pick_clue_with_config()
        print("\nchosen clue:", result)
    except Exception as e:
        print("error picking clue:", e)

def action_show_total():
    try:
        clues = load_clues()
        print(f"\nthere are {len(clues)} clues available.")
    except Exception as e:
        print("error loading clues:", e)

def action_preview_rare():
    try:
        config = load_config()
        rare_list = config.get("rare", [])
        if not rare_list:
            print("\nno rare clues defined.")
        else:
            print("\nrare clues:")
            for r in rare_list:
                print("-", r)
    except Exception as e:
        print("error reading rare clues:", e)

def main():
    print("starting upgraded clue system...")

    while True:
        show_menu()
        choice = input("choose an option: ").strip()

        if choice == "1":
            action_pick_clue()
        elif choice == "2":
            action_show_total()
        elif choice == "3":
            action_preview_rare()
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice, try again.")

if __name__ == "__main__":
    main()
