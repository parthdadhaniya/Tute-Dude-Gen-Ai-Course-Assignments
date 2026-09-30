# Task 7: Observations & Insights
# Student: Parth Dadhaniya


def task7_observations():
    print("--- Task 7: Observations & Insights ---")

    print("""
1. Why is chat history important?
   - LLMs are stateless by default. Each request is treated as a new conversation.
   - Chat history gives the model memory so it can understand pronouns ("it", "they")
     and follow-up questions (like "Give an example" or "What about tuples?").
   - Without history, the user would have to repeat the entire context in every prompt.

2. Trade-offs between long memory and performance:
   - Latency: Sending a long history means the model takes more time to process the prompt tokens.
   - Cost: For cloud APIs like OpenAI or Groq, sending long conversation history repeatedly
     costs more money on every single message turn.
   - Quality: When context gets too long, models can get confused or ignore earlier instructions
     (often called 'lost in the middle').

3. When to summarize vs trim history?
   - Trimming (Sliding Window): Best when only the last few messages are relevant (like coding Q&A
     or quick customer support). It is fast and does not require an extra LLM call.
   - Summarizing: Best when a conversation is very long (dozens of turns) and key facts (user preferences,
     account details) must be preserved without sending dozens of conversational messages.

4. Difference between message placeholders and memory:
   - MessagesPlaceholder: A template slot in ChatPromptTemplate that marks where past messages
     should be inserted inside the prompt. It does not store anything itself.
   - Memory: The storage system (like Python lists, Redis, or SQLite) that actually saves,
     retrieves, and trims the list of messages between turns.
""")


if __name__ == "__main__":
    task7_observations()
