# Assignment 22: Embedding Models, Vector Stores & Similarity Search
# Author: Parth Dadhaniya
# Master Runner Script

import os
import subprocess
import sys

tasks = [
    ("Task 1: OpenAI Embedding Model", "task1_openai_embeddings.py"),
    ("Task 2: Hugging Face Embedding Model", "task2_huggingface_embeddings.py"),
    ("Task 3: Comparison - OpenAI vs Hugging Face", "task3_comparison.py"),
    ("Task 4: Similarity Search App (Core Logic)", "task4_similarity_search_app.py"),
    ("Task 5: Similarity Search with LangChain", "task5_langchain_search.py"),
    ("Task 6: Ollama Embeddings (Local Setup)", "task6_ollama_embeddings.py"),
    ("Task 7: FAISS Vector Store", "task7_faiss_vectorstore.py"),
    ("Task 8: ChromaDB Vector Store", "task8_chroma_vectorstore.py"),
    ("Task 9: FAISS vs ChromaDB Comparison", "task9_faiss_vs_chroma.py"),
    ("Task 10: End-to-End Similarity Search Pipeline", "task10_similarity_pipeline.py"),
    ("Task 11: Observations & Insights", "task11_observations.py"),
]

def main():
    print("Running Assignment 22 Tasks (Parth Dadhaniya)\n")

    for title, script in tasks:
        print("-" * 60)
        print(f"Running: {title} ({script})")
        print("-" * 60)
        
        script_path = os.path.join(os.path.dirname(__file__), script)
        result = subprocess.run([sys.executable, "-u", script_path], capture_output=False)
        if result.returncode != 0:
            print(f"Error while running {script}")
            break
        print()

    print("All Assignment 22 tasks finished successfully.")

if __name__ == "__main__":
    main()
