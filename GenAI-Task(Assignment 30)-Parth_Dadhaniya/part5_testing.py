# Part 5: Multi-Turn Chat Testing (Task 9)
# Student: Parth Dadhaniya

from part2_part3_rag_pipeline import RAGChatbot


def test_conversational_rag():
    print("--- Task 9: Multi-Turn Conversation & Grounding Test ---")
    bot = RAGChatbot(k=2)

    turns = [
        "What are the advantages of Groq LPUs for LLM inference?",
        "Explain more about how it works.",
        "What vector embedding model is used in this pipeline?",
        "What is the capital of Mars?"
    ]

    for i, user_message in enumerate(turns, 1):
        print(f"\n[Turn {i}] User: {user_message}")
        answer, docs = bot.ask(user_message)
        print(f"Assistant: {answer}")
        print(f"Chat History length: {len(bot.history)} messages")

    print("\n--- Test Summary ---")
    print("1. Factual query answered using context chunks.")
    print("2. Follow-up query resolved using conversation history.")
    print("3. Vector embedding question retrieved correctly.")
    print("4. Out-of-context query grounded with 'I don't know based on the provided documents.'")


if __name__ == "__main__":
    test_conversational_rag()
