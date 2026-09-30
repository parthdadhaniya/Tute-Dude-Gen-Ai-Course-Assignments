# Assignment 30: Chat Groq RAG Application with Streamlit UI
# Student: Parth Dadhaniya

from part1_groq_setup import run_part1
from part2_part3_rag_pipeline import run_rag_demo
from part5_testing import test_conversational_rag
from task11_observations import print_observations


def main():
    print("=" * 60)
    print("Assignment 30: Chat Groq RAG Application")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n[Step 1] Running Part 1: Groq Setup & Basic Chat (Tasks 1 & 2)")
    run_part1()

    print("\n[Step 2] Running Parts 2 & 3: RAG Pipeline & Chain (Tasks 3 - 6)")
    run_rag_demo()

    print("\n[Step 3] Running Part 5: Multi-Turn Conversation Testing (Task 9)")
    test_conversational_rag()

    print("\n[Step 4] Running Part 6: Observations & Learnings (Task 11)")
    print_observations()

    print("=" * 60)
    print("All tasks finished successfully.")
    print("To launch the Streamlit web app: streamlit run app.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
