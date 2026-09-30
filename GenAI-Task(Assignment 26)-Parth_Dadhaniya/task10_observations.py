# task10_observations.py
# Task 10: Observations & Insights
# Student: Parth Dadhaniya

print("=== Task 10: Observations & Insights ===")

qa_pairs = [
    (
        "1. Why is Groq suitable for real-time applications?",
        "Groq uses custom hardware called Language Processing Units (LPUs). Unlike GPUs that rely on "
        "high-bandwidth external memory (HBM) and dynamic scheduling, Groq LPUs use on-chip SRAM with "
        "deterministic compiler scheduling. This generates tokens at speeds exceeding 300 to 500 tokens "
        "per second, making it ideal for real-time chatbots, voice assistants, and instant search interfaces."
    ),
    (
        "2. Groq vs OpenAI latency comparison (conceptual):",
        "- Groq: Extremely low time-to-first-token (TTFT) and throughput often 3x-10x faster than traditional "
        "cloud GPU clusters. Best suited for high-throughput, latency-critical inference on open weights (Llama 3, Mistral).\n"
        "- OpenAI: Industry-leading reasoning capabilities (GPT-4o) and multimodal support, but incurs higher "
        "latency and queue times due to centralized GPU server infrastructure."
    ),
    (
        "3. What are the benefits of an API-first GenAI architecture?",
        "- Frontend Agnostic: A single FastAPI service can serve web apps, mobile apps, Slack bots, and internal tools.\n"
        "- Decoupled Scalability: The backend can scale horizontally and swap underlying LLM providers (e.g. Groq, "
        "OpenAI, Ollama) without touching client-side code.\n"
        "- Centralized Security & Governance: API keys, rate limits, PII sanitization, and RAG retrieval pipelines "
        "remain securely hosted on the server without exposing secrets to frontend clients."
    )
]

for q, a in qa_pairs:
    print(f"\n{q}\n{a}\n" + "-" * 60)

print("\nTask 10 completed successfully.")
