# Part 6: Observations & Insights (Task 11)
# Student: Parth Dadhaniya


def main():
    print("--- Task 11: Observations & Insights ---")
    print("Student: Parth Dadhaniya\n")

    print("1. Difference between PDF Q&A and conversational PDF Q&A:")
    print("Regular PDF Q&A answers one question at a time without remembering past context. Conversational PDF Q&A stores chat history so users can ask follow-up questions like 'explain that more' or refer to earlier topics.\n")

    print("2. Role of message history in follow-up questions:")
    print("Message history provides context for the LLM. When a user asks 'Why is that needed?', the model looks at earlier turns to know what 'that' refers to and answers accurately.\n")

    print("3. Trade-offs between long memory and performance:")
    print("Keeping too many past messages increases token usage and latency. It can also cause the model to get distracted by old topics or exceed context limits.\n")

    print("4. How trimming history affects answer quality:")
    print("Trimming old messages (e.g. keeping only the last 3-4 turns) keeps the bot fast and responsive while still remembering the active topic. If you trim too aggressively, the bot forgets earlier context.")


if __name__ == "__main__":
    main()
