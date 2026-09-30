# Part 2: Stuff Summarization Chain (Tasks 4, 5 & 6)
# Student: Parth Dadhaniya

import os
from langchain_core.documents import Document
from config import get_llm
from summarize_chains import load_summarize_chain

doc_path = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_overview.txt")


def explain_stuff_chain():
    """Task 4: Conceptual overview of Stuff Summarization Chain."""
    print("--- Task 4: Stuff Summarization Chain (Conceptual) ---")
    print("1. What is a Stuff Summarization Chain?")
    print("   The 'Stuff' chain takes all text or document chunks and concatenates ('stuffs') them")
    print("   directly into a single prompt template sent to the LLM in one API call.\n")

    print("2. When is it suitable to use?")
    print("   - Small to medium documents (e.g. short blog posts, single-page memos, meeting transcripts).")
    print("   - When total word/token count is well within the model's context window limit.")
    print("   - When fast, low-cost summarization is needed in a single call.\n")

    print("3. Limitations of Stuff Chain:")
    print("   - Context Window Overflow: Hard fails if document exceeds maximum model tokens.")
    print("   - 'Lost in the Middle': Models struggle to recall details buried deep in the middle of massive prompts.")
    print("   - High token cost / memory latency on very large single prompts.\n")


def run_stuff_chain(docs, llm):
    """Task 5: Implement Stuff Summarization Chain using load_summarize_chain."""
    print("--- Task 5: Implement Stuff Summarization Chain ---")
    chain = load_summarize_chain(llm, chain_type="stuff")

    result = chain.invoke({"input_documents": docs})
    summary = result["output_text"]

    print("Stuff Chain Summary Output:")
    print(summary)
    return summary


def compare_prompt_vs_stuff(prompt_summary, stuff_summary):
    """Task 6: Compare Prompt-based vs Stuff Chain summarization."""
    print("\n--- Task 6: Comparison: Prompt-Based vs Stuff Chain ---")
    print("Key Differences:")
    print("1. Input Handling:")
    print("   - Prompt-based: Expects a raw string passed to a PromptTemplate.")
    print("   - Stuff Chain: Standardized LangChain chain accepting a list of Document objects with metadata.")
    print("2. Extensibility:")
    print("   - Prompt-based is custom-coded per use case.")
    print("   - Stuff Chain integrates directly into LangChain document loaders, vector stores, and retrieval chains.")
    print("3. Context Limit:")
    print("   - Both methods suffer from the same fundamental limitation: they cannot handle documents larger")
    print("     than the model's single-call context window.")


def main():
    explain_stuff_chain()

    # Load document as LangChain Document object
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    docs = [Document(page_content=content, metadata={"source": "enterprise_ai_overview.txt"})]

    llm = get_llm()
    stuff_summary = run_stuff_chain(docs, llm)
    compare_prompt_vs_stuff("Prompt Summary", stuff_summary)


if __name__ == "__main__":
    main()
