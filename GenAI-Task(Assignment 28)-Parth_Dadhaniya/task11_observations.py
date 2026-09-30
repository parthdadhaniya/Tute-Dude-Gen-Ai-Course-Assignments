# Task 11: Observations & Insights
# Student: Parth Dadhaniya


def task11_observations():
    print("--- Task 11: Observations & Insights ---")

    print("""
1. Difference between normal RAG and conversational RAG:
   - Normal RAG is stateless (single-turn). It treats every query in isolation.
     Follow-up questions like "Explain more" or "What about the previous point?" fail
     because the retriever searches for the literal words "Explain more" without knowing the topic.
   - Conversational RAG maintains chat history using MessagesPlaceholder, allowing the model
     to understand pronouns and follow-up references across multi-turn conversations.

2. Role of message history in follow-up questions:
   - It provides conversational context (anaphora resolution). When a user asks
     "Explain more about how it is carried forward", the history tells the model that "it"
     refers to the "annual leave policy" discussed in the previous turn.

3. Trade-offs between long memory and performance:
   - Latency: Processing large message histories increases prompt token length and slows down TTFT.
   - Token Costs: On pay-per-token APIs (Groq, OpenAI), re-sending dozens of turns compounds
     costs quadratically (O(N^2) tokens across N turns).
   - Context Confusion: If the history is too large, the LLM may get distracted by old dialogue
     and pay less attention to newly retrieved document facts.

4. How trimming affects answer quality:
   - Beneficial Effect: Sliding window trimming discards stale, irrelevant earlier turns,
     keeping prompt size predictable and answers crisp.
   - Risk: If trimming is too aggressive (e.g., keeping only 1 message), the bot forgets
     context from 2-3 turns ago. A window of 2 to 4 turns (4 to 8 messages) strikes the
     ideal balance for document Q&A assistants.
""")


if __name__ == "__main__":
    task11_observations()
