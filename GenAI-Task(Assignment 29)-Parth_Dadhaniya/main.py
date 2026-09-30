# Assignment 29: Q&A Chatbot Application (OpenAI & Ollama)
# Master Runner
# Student: Parth Dadhaniya

from part1_openai_chatbot import task1_setup, task2_basic_qa, task3_multi_turn_qa
from part2_ollama_chatbot import task4_ollama_setup, task5_ollama_chat, task6_comparison
from part3_unified_app import task7_switch_demo
from task9_observations import task9_observations


def main():
    print("=" * 60)
    print("Assignment 29: Q&A Chatbot Application (OpenAI & Ollama)")
    print("Student: Parth Dadhaniya | TuteDude Gen AI Course")
    print("=" * 60)

    # Part 1: OpenAI Q&A Chatbot (Tasks 1, 2, 3)
    task1_setup()
    task2_basic_qa()
    task3_multi_turn_qa()

    # Part 2: Ollama Local Q&A Chatbot (Tasks 4, 5, 6)
    task4_ollama_setup()
    task5_ollama_chat()
    task6_comparison()

    # Part 3: Unified App & Model Switch Logic (Tasks 7 & 8)
    task7_switch_demo()

    # Part 4: Observations & Conceptual Questions (Task 9)
    task9_observations()

    print("=" * 60)
    print("All Assignment 29 tasks completed successfully!")
    print("Optional Streamlit app: streamlit run streamlit_app.py")
    print("Interactive CLI app   : python part3_unified_app.py --interactive")
    print("=" * 60)


if __name__ == "__main__":
    main()
