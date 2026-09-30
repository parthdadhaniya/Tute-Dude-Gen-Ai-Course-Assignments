# Part 5: Observations & Insights (Task 11)
# Student: Parth Dadhaniya


def main():
    print("--- Task 11: Observations & Insights ---")
    print("Student: Parth Dadhaniya\n")

    print("1. Benefits of tool-augmented agents:")
    print("Tools allow LLMs to overcome their core weaknesses: math inaccuracy, lack of real-time knowledge, and inability to act on external systems. By grounding actions in calculator or search tools, hallucinations decrease significantly.\n")

    print("2. Challenges with agents:")
    print("Key challenges include higher latency and token costs from multi-step loops, the risk of infinite loops when a tool fails, and occasional tool-calling errors when LLMs pass incorrect argument types.\n")

    print("3. Difference between chains and agents:")
    print("Chains follow a rigid, hardcoded sequence of steps (like prompt -> LLM -> parser). Agents use the LLM as a reasoning engine to dynamically decide WHICH steps and tools to execute at runtime based on intermediate observations.\n")

    print("4. When to use agents over RAG:")
    print("Use RAG for passive Q&A over static documents. Use agents when the problem requires taking actions (like calling an API, modifying a database, or performing math calculations) or when the workflow requires multi-step decision making.")


if __name__ == "__main__":
    main()
