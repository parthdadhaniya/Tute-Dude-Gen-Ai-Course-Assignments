# task10_observations.py
# Task 10: Observations & Insights
# Student: Parth Dadhaniya

print("=== Task 10: Observations & Insights ===")

insights = [
    (
        "1. Why is structured output important in production GenAI applications?",
        "LLMs naturally return free-form text which is prone to format errors. Using schemas like "
        "Pydantic forces the model to return typed fields (strings, floats, lists) so APIs, frontends, "
        "and databases can parse responses reliably without crashing on unexpected formatting."
    ),
    (
        "2. What are the advantages of LCEL over traditional chains?",
        "LCEL uses a simple pipe syntax (|) that replaces complex classes like LLMChain. It natively "
        "supports streaming, asynchronous execution, batch processing, and automatic tracing without "
        "writing extra boilerplate."
    ),
    (
        "3. When should you use Parallel Chains versus Conditional Chains?",
        "Use Parallel Chains (RunnableParallel) when you have multiple independent tasks for the same "
        "input that can run at the same time to save latency (like generating an answer and summary simultaneously).\n"
        "Use Conditional Chains (RunnableBranch) when you need to route requests to different paths based "
        "on input rules (like sending factual questions to a vector store and greetings directly to the model)."
    )
]

for q, a in insights:
    print(f"\n{q}\n{a}\n" + "-" * 60)

print("\nTask 10 completed successfully.")
