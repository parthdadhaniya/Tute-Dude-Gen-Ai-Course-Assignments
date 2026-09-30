# Part 1: Getting Started with Groq API (Tasks 1 & 2)
# Student: Parth Dadhaniya

import os
import time
from langchain_core.prompts import ChatPromptTemplate
from config import get_chat_model, DEFAULT_MODEL


def test_groq_setup():
    print("--- Task 1: Groq Setup ---")
    key = os.getenv("GROQ_API_KEY", "").strip()
    if key:
        print("Groq API key found in environment.")
    else:
        print("Note: GROQ_API_KEY not set. Using local model fallback for testing.")
    print(f"Target Model: {DEFAULT_MODEL}")


def test_basic_chat():
    print("\n--- Task 2: Basic Chat with ChatGroq ---")
    llm = get_chat_model()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant. Answer in 1-2 concise sentences."),
        ("human", "{question}")
    ])

    chain = prompt | llm
    user_q = "Why are Groq LPUs faster than GPUs for LLM inference?"
    print(f"Prompt: {user_q}")

    start = time.time()
    response = chain.invoke({"question": user_q})
    elapsed = time.time() - start

    print(f"Response: {response.content}")
    print(f"Latency: {elapsed:.3f} seconds")


def run_part1():
    test_groq_setup()
    test_basic_chat()


if __name__ == "__main__":
    run_part1()
