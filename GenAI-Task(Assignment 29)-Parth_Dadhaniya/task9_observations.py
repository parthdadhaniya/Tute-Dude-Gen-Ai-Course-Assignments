# Part 4: Observations & Insights (Task 9)
# Student: Parth Dadhaniya


def task9_observations():
    print("--- Task 9: Observations & Insights ---")

    print("""
1. When to prefer OpenAI models:
   - Complex Multi-Step Reasoning: Leading closed models (GPT-4o) excel at difficult logic,
     nuanced prompt adherence, and multilingual edge cases.
   - Rapid Prototyping & MVPs: Developers can launch an AI feature in hours without managing
     GPU drivers, vRAM limits, or infrastructure orchestration.
   - Zero DevOps Overhead: Automatic scaling, high availability, and state-of-the-art updates
     are handled entirely by the provider.

2. When to prefer open-source models (Ollama / Llama 3):
   - Strict Data Privacy & Compliance: Healthcare (HIPAA), defense, banking, and proprietary IP
     where data can never leave the corporate perimeter.
   - Offline / Edge Deployments: Systems running in air-gapped data centers, local desktop tools,
     or environments with intermittent internet access.
   - Custom Weight Fine-Tuning: Full freedom to modify model weights, quantize for edge hardware,
     and avoid model deprecation or forced API version sunsets.

3. Trade-offs in production systems:
   - Closed Cloud APIs (OpenAI): Superior out-of-the-box accuracy, but subject to internet latency,
     unpredictable rate limits, and risk of vendor lock-in.
   - Open-Source (Ollama): Complete control and privacy, but requires investing in GPU hardware,
     memory management, and DevOps monitoring to maintain throughput under load.

4. Cost and scalability considerations:
   - Pay-Per-Token vs Fixed Hardware: Cloud APIs are cost-effective for variable or low-to-medium traffic.
     However, at massive enterprise scale (millions of tokens daily), cloud costs explode.
   - At high sustained volume, dedicated GPU clusters hosting open-source models deliver
     far lower marginal cost per query.
""")


if __name__ == "__main__":
    task9_observations()
