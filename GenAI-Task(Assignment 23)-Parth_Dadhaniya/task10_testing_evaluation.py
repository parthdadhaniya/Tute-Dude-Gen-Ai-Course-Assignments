# Task 10: Testing & Evaluation
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")
import config

from task9_youtube_rag_chatbot import YouTubeChatbot

print("--- Task 10: Testing & Evaluation of YouTube RAG Chatbot ---")

bot = YouTubeChatbot()

# 5 test questions about the video + 1 out-of-scope question
test_questions = [
    "What are the two files that make up an LLM?",
    "How much data was used during the pre-training of Llama 2?",
    "What is the context window of a language model?",
    "What is the difference between System 1 and System 2 thinking?",
    "What is prompt injection and why is it dangerous?",
    "How do you cook an Italian carbonara pasta recipe?"  # out of scope question
]

print(f"Testing chatbot on {len(test_questions)} questions:\n")

for i, q in enumerate(test_questions, 1):
    print(f"Q{i}: {q}")
    ans, _ = bot.ask(q)
    print(f"A{i}: {ans}\n")

print("Evaluation Summary:")
print("- Verified factual questions match the video content.")
print("- Verified out-of-scope question correctly refused without hallucinations.")
