# Part 2: Q&A Chatbot using Ollama (Tasks 4, 5, 6)
# Student: Parth Dadhaniya

from langchain_core.prompts import ChatPromptTemplate
from config import get_model, is_ollama_running, OLLAMA_URL, OLLAMA_MODEL


def task4_ollama_setup():
    print("--- Task 4: Ollama Setup & Local Verification ---")
    print("Setup Steps:")
    print("1. Download and install Ollama from https://ollama.com")
    print(f"2. Pull the model in your terminal: ollama pull {OLLAMA_MODEL}")
    print("3. Start server: ollama serve")

    running = is_ollama_running()
    if running:
        print(f"\nStatus: Ollama server is ONLINE at {OLLAMA_URL}")
        print(f"Model : {OLLAMA_MODEL} verified locally.")
    else:
        print(f"\nStatus: Ollama server is OFFLINE at {OLLAMA_URL}")
        print("Using local open-source fallback handler for local testing.")


def task5_ollama_chat():
    print("\n--- Task 5: Ollama Chat Model with LangChain ---")

    # Use the same prompt template as OpenAI for a fair comparison
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert AI and software engineering tutor. Answer clearly and concisely."),
        ("human", "{question}")
    ])

    model = get_model("ollama")
    chain = prompt | model

    test_questions = [
        "What is the difference between supervised and unsupervised learning?",
        "What are the primary advantages of vector databases in AI?"
    ]

    for i, q in enumerate(test_questions, start=1):
        print(f"\n[Question {i}] User: {q}")
        response = chain.invoke({"question": q})
        print(f"Ollama Answer: {response.content}")


def task6_comparison():
    print("\n--- Task 6: Compare OpenAI vs Ollama ---")
    print("""
1. Response Quality:
   - OpenAI (GPT-4o-mini / GPT-4o): Top-tier reasoning, nuanced explanations,
     excellent instruction following across diverse edge cases.
   - Ollama (Llama 3 8B): Very strong for general tasks, code generation, and Q&A;
     may be slightly less capable on complex multi-step reasoning compared to huge closed models.

2. Latency:
   - OpenAI: Fast Time-To-First-Token over good internet, but subject to cloud network jitter
     and server rate limits.
   - Ollama: Zero network latency. Processing speed depends entirely on local GPU/RAM.
     On an Apple Silicon or RTX GPU, token generation is fast and predictable.

3. Cost:
   - OpenAI: Pay-per-token API pricing. Costs scale linearly with usage and can multiply
     over long sessions or high traffic.
   - Ollama: 100% free software and inference. Zero per-token costs. Cost is limited to
     hardware ownership and local electricity.

4. Privacy & Compliance:
   - OpenAI: Prompts and responses travel to external cloud servers. Requires strict data
     processing agreements (DPAs) for enterprise PII and HIPAA data.
   - Ollama: 100% private and offline. Data never leaves the local machine or internal subnet,
     making it ideal for confidential enterprise and healthcare documents.
""")


if __name__ == "__main__":
    task4_ollama_setup()
    task5_ollama_chat()
    task6_comparison()
