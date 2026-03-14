# run.py
# entry point for the clue system

from engine import pick_clue_with_config
from engine import load_clues
from config import load_config

last_clue = None
print("system initialized")

def show_menu():
    print("\n=== clue system menu ===")
    print("1. pick a clue")
    print("2. show total number of clues")
    print("3. preview rare clues")
    print("4. exit")
    print("5. show last picked clue")
    print("6. reload config")
    print("7. test multiple picks")
    print("========================")

def action_pick_clue():
    global last_clue
    try:
        result = pick_clue_with_config()
        last_clue = result
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

def action_show_last():
    if last_clue is None:
        print("\nno clue has been picked yet.")
    else:
        print("\nlast picked clue:", last_clue)

def action_reload_config():
    try:
        cfg = load_config()
        print("\nconfig reloaded. keys:", ", ".join(cfg.keys()))
    except Exception as e:
        print("error reloading config:", e)

def action_test_multiple():
    try:
        count = input("\nhow many picks? ").strip()
        if not count.isdigit():
            print("invalid number.")
            return
        count = int(count)
        print(f"\nrunning {count} picks...")
        for i in range(count):
            result = pick_clue_with_config()
            print(f"{i+1}. {result}")
    except Exception as e:
        print("error during test:", e)

def main():
    print("starting clue system...")

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
        elif choice == "5":
            action_show_last()
        elif choice == "6":
            action_reload_config()
        elif choice == "7":
            action_test_multiple()
        else:
            print("invalid choice, try again.")

if __name__ == "__main__":
    main()

# coauthor test line v2
