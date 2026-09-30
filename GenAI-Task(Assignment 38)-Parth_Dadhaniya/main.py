# main.py - Master Pipeline Runner for Assignment 38
# Assignment: CodeLlama with Ollama (Developer Coding Assistant)
# Student: Parth Dadhaniya

import sys
from part1_codellama_setup import run_task1
from part2_basic_interaction import run_task2
from part3_code_assistant import run_tasks_3_and_5


def main():
    print("=" * 68)
    print("Assignment 38: CodeLlama Developer Assistant using Ollama")
    print("Student: Parth Dadhaniya")
    print("Course: Generative AI Engineering - TuteDude")
    print("=" * 68)

    print("\n>>> PART 1 - TASK 1: Setup CodeLlama with Ollama <<<")
    run_task1()

    print("\n>>> PART 1 - TASK 2: Basic CodeLlama Interaction <<<")
    run_task2()

    print("\n>>> PART 1 & 2 - TASKS 3 & 5: Code Assistant Features & Prompt Engineering <<<")
    run_tasks_3_and_5()

    print("=" * 68)
    print("All tasks for Assignment 38 completed successfully!")
    print("To launch the interactive Streamlit Web UI, run:")
    print("  streamlit run app.py")
    print("=" * 68)


if __name__ == "__main__":
    main()
