from stages import stages

def play_game():
    print("\n🧙 Welcome to CI/CD Dungeon Escape")
    print("Stabilize the pipeline to escape the dungeon.\n")

    score = 0

    for stage in stages:
        print("=" * 60)
        print(f"\n⚔️  {stage['name']}\n")

        # Narrative
        print("📖 Situation:")
        print(stage["narrative"])
        print()

        # Technical explanation
        print("🔍 Technical Insight:")
        print(stage["technical"])
        print()

        # Options
        print("Choose your action:\n")
        for key, value in stage["options"].items():
            print(f"{key}. {value}")

        choice = input("\nYour decision: ").strip().upper()

        if choice == stage["answer"]:
            print("\n✅ Correct. The pipeline stabilizes.\n")
            score += 1
        else:
            print("\n❌ That action worsened the instability.\n")

    print("=" * 60)
    print(f"\n🏆 Final Score: {score}/{len(stages)}")

    if score == len(stages):
        print("🎉 You escaped the dungeon. Production is stable.")
    else:
        print("⚠️ The pipeline survives… but improvements remain.")

if __name__ == "__main__":
    play_game()