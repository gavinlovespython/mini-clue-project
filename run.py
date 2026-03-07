# run.py
# simple entry point for the clue system

from engine import pick_clue_with_config

def main():
    print("starting clue system...")
    try:
        result = pick_clue_with_config()
        print("chosen clue:", result)
    except Exception as e:
        print("an error occurred while picking a clue:", e)

if __name__ == "__main__":
    main()
