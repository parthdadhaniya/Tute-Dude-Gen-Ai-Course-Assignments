# Part 4: Refine Summarization Chain (Tasks 10, 11 & 12)
# Student: Parth Dadhaniya

import os
from langchain_core.documents import Document
from config import get_llm
from summarize_chains import load_summarize_chain

doc_path = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_overview.txt")


def explain_refine_chain():
    """Task 10: Conceptual overview of Refine Summarization Chain."""
    print("--- Task 10: Refine Summarization Chain (Conceptual) ---")
    print("1. How Refine Summarization Works:")
    print("   - Initial Step: The LLM generates a summary of the very first chunk.")
    print("   - Refine Loop : For each subsequent chunk, the model receives BOTH the running summary")
    print("                   and the new text chunk, refining the summary step-by-step.")
    print("   - Final Output: A cumulative, continuously refined summary encompassing all chunks.\n")

    print("2. Key Differences Between Map-Reduce and Refine:")
    print("   - Parallelism : Map-Reduce summarizes chunks concurrently; Refine must run sequentially.")
    print("   - Coherence   : Refine builds continuous narrative flow because each step sees prior context.")
    print("                   Map-Reduce treats chunks in isolation, which can result in repetitive summaries.")
    print("   - Latency     : Map-Reduce is faster for parallel workers; Refine has cumulative latency.\n")


def split_text_into_chunks(text, chunk_size=1200, chunk_overlap=150):
    """Splits raw text into chunks for the Refine pipeline."""
    chunks = []
    start = 0
    idx = 1
    while start < len(text):
        end = start + chunk_size
        chunk_content = text[start:end]
        chunks.append(Document(page_content=chunk_content, metadata={"chunk": idx}))
        start += chunk_size - chunk_overlap
        idx += 1
    return chunks


def run_refine_chain(docs, llm):
    """Task 11: Implement Refine Summarization Chain."""
    print("--- Task 11: Implement Refine Summarization Chain ---")
    print(f"Iteratively refining across {len(docs)} chunks...\n")

    chain = load_summarize_chain(llm, chain_type="refine")
    result = chain.invoke({"input_documents": docs})

    print("[Final Refined Summary Output]:")
    print(result["output_text"])
    return result["output_text"]


def compare_all_methods():
    """Task 12: Comprehensive comparison of all four summarization strategies."""
    print("\n--- Task 12: Comparison of All Summarization Methods ---")
    comparison_data = [
        ("Prompt-Based", "Good for 1-off text", "High", "Single prompt limit", "Fast (1 call)"),
        ("Stuff Chain", "Clean for short docs", "High", "Context window bound", "Fast (1 call)"),
        ("Map-Reduce", "High (executive view)", "Moderate", "Scales to any length", "Medium (N+1 calls, parallel)"),
        ("Refine", "Highest detail & flow", "Highest", "Scales to any length", "Slower (N calls, sequential)"),
    ]

    print(f"{'Method':<14} | {'Summary Quality':<22} | {'Coherence':<10} | {'Long Docs Suitability':<22} | {'Latency & Calls'}")
    print("-" * 90)
    for method, qual, coh, suit, lat in comparison_data:
        print(f"{method:<14} | {qual:<22} | {coh:<10} | {suit:<22} | {lat}")


def main():
    explain_refine_chain()

    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()

    docs = split_text_into_chunks(content)
    llm = get_llm()
    run_refine_chain(docs, llm)
    compare_all_methods()


if __name__ == "__main__":
    main()
