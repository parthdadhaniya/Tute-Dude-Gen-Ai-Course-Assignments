# Assignment 23: OpenAI & Retrieval-Augmented Generation (RAG)
# Author: Parth Dadhaniya
# Master Runner Script

import os
import subprocess
import sys

tasks = [
    ("Task 1: OpenAI Setup & Basic Prompt", "task1_openai_setup.py"),
    ("Task 2: Wikipedia Retriever", "task2_wikipedia_retriever.py"),
    ("Task 3: Vector Store Retriever", "task3_vectorstore_retriever.py"),
    ("Task 4: Maximal Marginal Relevance (MMR)", "task4_mmr_retriever.py"),
    ("Task 5: Multi-Query Retriever", "task5_multiquery_retriever.py"),
    ("Task 6: Contextual Compression Retriever", "task6_compression_retriever.py"),
    ("Task 7: Load YouTube Video Content", "task7_load_youtube.py"),
    ("Task 8: YouTube Embeddings & Vector Store", "task8_youtube_vectorstore.py"),
    ("Task 9: YouTube Content RAG Chatbot", "task9_youtube_rag_chatbot.py"),
    ("Task 10: Testing & Evaluation", "task10_testing_evaluation.py"),
    ("Task 11: Conceptual Questions & Observations", "task11_observations.py"),
]

def main():
    print("=" * 65)
    print(" Running Assignment 23: OpenAI & RAG Systems (Parth Dadhaniya)")
    print("=" * 65 + "\n")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    for title, script in tasks:
        print("\n" + "=" * 65, flush=True)
        print(f"Executing: {title} ({script})", flush=True)
        print("=" * 65, flush=True)
        
        script_path = os.path.join(current_dir, script)
        result = subprocess.run([sys.executable, "-u", script_path], cwd=current_dir, capture_output=False)
        if result.returncode != 0:
            print(f"Error occurred while executing {script} (code {result.returncode})", flush=True)
            sys.exit(result.returncode)

    print("\n" + "=" * 65, flush=True)
    print("All Assignment 23 tasks completed successfully!", flush=True)
    print("=" * 65, flush=True)

if __name__ == "__main__":
    main()
