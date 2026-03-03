import time
import sys
import threading
from colorama import init, Fore, Style
from game.stages import stages

# Initialize colorama
init(autoreset=True)

TOTAL_STAGES = len(stages)
score = 0

# Countdown hint function
def countdown_hint(stage, seconds=5):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rHint in {i} seconds...")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f"\rHint: {stage['hint']}{' ' * 20}\n")

def ask_stage(stage):
    global score
    print(f"\nStage {stages.index(stage)+1} of {TOTAL_STAGES}: {stage['name']}")
    print(stage['ascii_art'])
    print(stage['narrative'])

    # Countdown hint in background
    hint_thread = threading.Thread(target=countdown_hint, args=(stage, 5))
    hint_thread.start()

    attempts = 3
    while attempts > 0:
        print("\nOptions:")
        for key, val in stage['options'].items():
            print(f"{key}: {val}")
        answer = input("Your choice (A/B/C): ").strip().upper()

        if answer == stage['answer']:
            print(Fore.GREEN + "Correct! " + stage['teaching'][answer])
            score += 1
            break
        elif answer in stage['options']:
            print(Fore.RED + "Wrong! " + stage['teaching'][answer])
            attempts -= 1
            if attempts > 0:
                print(f"Try again! Attempts left: {attempts}")
            else:
                print(Fore.YELLOW + f"No attempts left. The correct answer was: {stage['answer']} - {stage['options'][stage['answer']]}")
        else:
            print(Fore.RED + "Invalid choice. Please select A, B, or C.")

    hint_thread.join()  # Ensure hint thread ends

def main():
    print(Fore.CYAN + Style.BRIGHT + f"Welcome to the CI/CD Dungeon Escape! There are {TOTAL_STAGES} stages to complete.\n")
    for stage in stages:
        ask_stage(stage)

    print(Fore.MAGENTA + Style.BRIGHT + f"\nDungeon completed! Your score: {score}/{TOTAL_STAGES}")
    if score == TOTAL_STAGES:
        print(Fore.YELLOW + "Amazing! You defeated all monsters and conquered the CI/CD dungeon!")
    elif score >= TOTAL_STAGES // 2:
        print(Fore.YELLOW + "Good job! You survived most of the dungeon.")
    else:
        print(Fore.RED + "The dungeon proved too challenging. Try again to improve your CI/CD skills!")

if __name__ == "__main__":
    main()