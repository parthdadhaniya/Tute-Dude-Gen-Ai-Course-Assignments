# Part 3: Map-Reduce Summarization Chain (Tasks 7, 8 & 9)
# Student: Parth Dadhaniya

import os
from langchain_core.documents import Document
from config import get_llm
from summarize_chains import load_summarize_chain

doc_path = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_overview.txt")


def explain_map_reduce():
    """Task 7: Conceptual explanation of Map-Reduce summarization."""
    print("--- Task 7: Map-Reduce Summarization (Conceptual) ---")
    print("1. Why do large documents need Map-Reduce?")
    print("   When documents are 20, 50, or 200 pages long (books, reports, transcripts), they exceed")
    print("   the LLM's single-prompt context window. Stuff chains would crash or truncate the text.")
    print("   Map-Reduce solves this by partitioning the document into manageable chunks.\n")

    print("2. How Map and Reduce steps work:")
    print("   - Map Step    : The LLM summarizes each text chunk independently and in parallel.")
    print("   - Reduce Step : All intermediate chunk summaries are consolidated and passed to a final")
    print("                   LLM call to produce an overarching, coherent executive summary.\n")


def split_text_into_chunks(text, chunk_size=1200, chunk_overlap=150):
    """Splits raw text into overlapping chunks and wraps them in Document objects."""
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


def run_map_reduce_chain(docs, llm):
    """Tasks 8 & 9: Implement Map-Reduce Chain and inspect intermediate outputs."""
    print("--- Task 8: Implement Map-Reduce Summarization Chain ---")
    print(f"Total chunks to process: {len(docs)}")

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    result = chain.invoke({"input_documents": docs})

    # Task 9: Analyze intermediate map outputs
    print("\n--- Task 9: Analyze Map Outputs (Intermediate Chunk Summaries) ---")
    for i, step_summary in enumerate(result.get("intermediate_steps", []), 1):
        print(f" [Map Step Chunk {i}]: {step_summary}")

    print("\n[Reduce Step - Final Combined Summary]:")
    print(result["output_text"])
    return result["output_text"]


def main():
    explain_map_reduce()

    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()

    docs = split_text_into_chunks(content)
    llm = get_llm()
    run_map_reduce_chain(docs, llm)


if __name__ == "__main__":
    main()
