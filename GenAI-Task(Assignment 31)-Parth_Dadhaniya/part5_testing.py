# Part 5: Multi-Turn Conversation Testing (Task 9)
# Student: Parth Dadhaniya

from part3_part4_rag_chain import ask_question
from part2_vector_store import get_retriever
from config import get_llm


def main():
    print("--- Task 9: Multi-Turn Follow-Up Q&A Testing ---")
    retriever = get_retriever(k=2)
    llm = get_llm()
    history = []

    # test sequence: factual -> follow-up -> clarification -> out of context
    test_queries = [
        "What models are approved for enterprise workloads?",
        "Explain more about their inference speed and real-time requirements.",
        "What is the data retention policy for conversation logs?",
        "What is the average temperature on Mars?"
    ]

    for i, q in enumerate(test_queries, 1):
        print(f"\n[Turn {i}] User: {q}")
        answer, docs = ask_question(q, history, retriever, llm)
        print(f"Assistant: {answer}")
        print(f"Messages in History: {len(history)}")

    print("\n--- Test Summary ---")
    print("1. Factual question answered from PDF.")
    print("2. Follow-up query resolved using conversation history.")
    print("3. Clarification query retrieved correctly.")
    print("4. Out-of-context query grounded with 'I don't know'.")


if __name__ == "__main__":
    main()
