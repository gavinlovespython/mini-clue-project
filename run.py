# run.py
# upgraded entry point for the clue system

from engine import pick_clue_with_config
from engine import load_clues
from config import load_config

last_clue = None
clue_history = []
debug_override = None

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
    print("8. show clue history")
    print("9. toggle debug mode")
    print("========================")

def debug_print(msg):
    cfg = load_config()
    debug_enabled = cfg.get("debug", False)

    if debug_override is not None:
        debug_enabled = debug_override

    if debug_enabled:
        print("[debug]", msg)

def action_pick_clue():
    global last_clue
    try:
        debug_print("starting clue pick")
        result = pick_clue_with_config()
        last_clue = result
        clue_history.append(result)

        debug_print(f"picked clue: {result}")
        debug_print(f"history size: {len(clue_history)}")

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
            clue_history.append(result)
            print(f"{i+1}. {result}")
    except Exception as e:
        print("error during test:", e)

def action_show_history():
    if not clue_history:
        print("\nno clues have been picked yet.")
        return

    print("\n=== clue history ===")
    for i, c in enumerate(clue_history, start=1):
        print(f"{i}. {c}")
    print("====================")

def action_toggle_debug():
    global debug_override
    if debug_override is None:
        debug_override = True
        print("\ndebug mode forced ON")
    elif debug_override is True:
        debug_override = False
        print("\ndebug mode forced OFF")
    else:
        debug_override = None
        print("\ndebug mode returned to config-controlled")

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
        elif choice == "8":
            action_show_history()
        elif choice == "9":
            action_toggle_debug()
        else:
            print("invalid choice, try again.")

if __name__ == "__main__":
    main()

# coauthor test line v3
