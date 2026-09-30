# Assignment 27: Chatbots with Conversation History using LangChain
# Student: Parth Dadhaniya

from task1_task2_messages_placeholder import task1_conceptual_answers, task2_messages_placeholder
from task3_task4_history_trimming import task3_basic_history, task4_trimming_demo
from task5_qa_chatbot import test_chatbot
from task6_stateful_app import run_demo
from task7_observations import task7_observations


def main():
    print("=" * 60)
    print("Assignment 27: Chatbots with Conversation History")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    # Part 1: Messages and MessagesPlaceholder
    task1_conceptual_answers()
    task2_messages_placeholder()

    # Part 2: Conversation History & Trimming
    task3_basic_history()
    task4_trimming_demo()

    # Part 3: Q&A Chatbot & Stateful Mini Project
    test_chatbot()
    run_demo()

    # Observations
    task7_observations()

    print("=" * 60)
    print("All tasks completed successfully!")
    print("Optional Streamlit app: streamlit run streamlit_app.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
