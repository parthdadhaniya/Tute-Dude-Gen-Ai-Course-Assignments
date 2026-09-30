# task2_groq_chatbot.py
# Task 2: Build a Groq Chatbot (Core Logic)
# Student: Parth Dadhaniya

import time
import warnings
warnings.filterwarnings("ignore")

import config

print("=== Task 2: Build a Groq Chatbot ===")

def groq_chat(prompt: str, system_prompt: str = "You are a knowledgeable AI assistant. Answer clearly and concisely.") -> str:
    """
    Core chatbot function that packages system instructions and user prompt,
    invokes Groq, and returns the generated answer.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    return config.call_groq(messages, temperature=0.7)

# test queries
test_queries = [
    "What is the capital of France?",
    "Explain the difference between CBOW and Skip-Gram word embeddings in 2 sentences.",
    "Why is Groq fast compared to standard cloud LLM hosting?"
]

print("\nTesting groq_chat() with multiple queries:\n")
for i, query in enumerate(test_queries, 1):
    print(f"--- Query {i} ---")
    print(f"User  : {query}")
    
    t0 = time.time()
    answer = groq_chat(query)
    latency = round(time.time() - t0, 3)
    
    print(f"Groq  : {answer.strip()}")
    print(f"Time  : {latency}s\n" + "-" * 50)

print("Task 2 completed successfully.")
