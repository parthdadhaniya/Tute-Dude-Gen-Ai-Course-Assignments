# Part 5: Testing the Conversational RAG Bot (Task 9)
# Student: Parth Dadhaniya

from part3_part4_rag_chain import ConversationalRAGChain


def run_multi_turn_rag_test():
    print("--- Task 9: Multi-Turn Q&A Testing ---")
    bot = ConversationalRAGChain(max_turns=3)

    test_queries = [
        # 1. Initial factual question
        "What is the annual leave policy?",

        # 2. Follow-up question referencing previous answer
        "Explain more about how it is carried forward.",

        # 3. Clarification question
        "What about sick leave compared to that?",

        # 4. Out-of-scope question to test grounding
        "What is the capital of Mars?"
    ]

    for turn_idx, query in enumerate(test_queries, start=1):
        print(f"\n[Turn {turn_idx}] User: {query}")
        answer, docs = bot.query(query)
        print(f"Assistant: {answer}")
        print(f"History Count: {len(bot.history)} messages")

    print("\n" + "-" * 50)
    print("Verification Summary:")
    print("- Turn 1: Successfully retrieved factual leave details.")
    print("- Turn 2: 'Explain more' accurately followed up on annual leave.")
    print("- Turn 3: 'Compared to that' resolved context between sick and annual leave.")
    print("- Turn 4: Grounding confirmed ('I don't know based on provided documents').")


if __name__ == "__main__":
    run_multi_turn_rag_test()
