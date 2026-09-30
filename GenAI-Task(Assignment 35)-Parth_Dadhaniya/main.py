# main.py - Master Runner for Assignment 35
# Student: Parth Dadhaniya

import part1_overview
import part2_math_agent
import part3_session_state


def main():
    print("=" * 65)
    print("Assignment 35: Text-to-Math Problem Solver Agent")
    print("Student: Parth Dadhaniya")
    print("=" * 65)

    print("\n>>> PART 1: Text-to-Math Agent Overview (Task 1) <<<")
    part1_overview.main()

    print("\n>>> PART 2: Build Text-to-Math Agent (Task 2) <<<")
    part2_math_agent.main()

    print("\n>>> PART 3: Session State Multi-Turn Context (Task 3) <<<")
    part3_session_state.main()

    print("\n" + "=" * 65)
    print("All tasks completed successfully!")
    print("To launch the interactive Streamlit UI, run:")
    print("  streamlit run app.py")
    print("=" * 65)


if __name__ == "__main__":
    main()
