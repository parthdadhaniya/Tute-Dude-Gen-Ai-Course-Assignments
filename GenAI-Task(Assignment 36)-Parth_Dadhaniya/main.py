# main.py - Master Pipeline Runner for Assignment 36
# Assignment: HuggingFace Integration with LangChain
# Student: Parth Dadhaniya

import sys
from part1_hf_direct import run_task1
from part2_hf_langchain import run_task2
from part3_chat_prompt import run_task3


def main():
    print("=" * 65)
    print("Assignment 36: HuggingFace Integration with LangChain")
    print("Student: Parth Dadhaniya")
    print("=" * 65)

    print("\n>>> PART 1: Getting Started with HuggingFace Models <<<")
    run_task1()

    print("\n>>> PART 2: HuggingFace with LangChain (Replacing OpenAI) <<<")
    run_task2()

    print("\n>>> PART 3: Chat Prompt Template with HuggingFace <<<")
    run_task3()

    print("\n" + "=" * 65)
    print("All tasks for Assignment 36 completed successfully!")
    print("=" * 65)


if __name__ == "__main__":
    main()
