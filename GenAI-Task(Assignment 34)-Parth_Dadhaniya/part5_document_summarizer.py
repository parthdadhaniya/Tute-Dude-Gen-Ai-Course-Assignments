# Part 5: Mini Project - Document Summarizer (Task 13)
# Student: Parth Dadhaniya

import os
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from config import get_llm
from summarize_chains import load_summarize_chain

doc_path = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_overview.txt")


def chunk_text(text, chunk_size=1200, chunk_overlap=150):
    """Utility to split text into LangChain Document chunks."""
    chunks = []
    start = 0
    idx = 1
    while start < len(text):
        end = start + chunk_size
        chunks.append(Document(page_content=text[start:end], metadata={"chunk": idx}))
        start += chunk_size - chunk_overlap
        idx += 1
    return chunks


def summarize_document(text_or_docs, method="map_reduce", llm=None):
    """
    Task 13: Unified reusable summarization function.
    Supports switching between:
      - 'prompt'     : Direct PromptTemplate execution
      - 'stuff'      : Stuff all documents into a single prompt
      - 'map_reduce' : Summarize chunks independently, then combine
      - 'refine'     : Iteratively update summary chunk-by-chunk
    """
    if llm is None:
        llm = get_llm()

    # Normalize input into text and documents
    if isinstance(text_or_docs, str):
        raw_text = text_or_docs
        docs = chunk_text(raw_text)
        single_doc = [Document(page_content=raw_text)]
    else:
        docs = text_or_docs
        raw_text = "\n\n".join([d.page_content for d in docs])
        single_doc = docs

    method_clean = method.lower().strip()

    # Strategy 1: Prompt-based
    if method_clean == "prompt":
        prompt = PromptTemplate(
            template="Summarize the following document clearly:\n\n{text}\n\nSummary:",
            input_variables=["text"],
        )
        chain = prompt | llm
        res = chain.invoke({"text": raw_text})
        return res.content if hasattr(res, "content") else str(res)

    # Strategy 2: Stuff Chain
    elif method_clean == "stuff":
        chain = load_summarize_chain(llm, chain_type="stuff")
        res = chain.invoke({"input_documents": single_doc})
        return res["output_text"]

    # Strategy 3: Map-Reduce Chain
    elif method_clean == "map_reduce":
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        res = chain.invoke({"input_documents": docs})
        return res["output_text"]

    # Strategy 4: Refine Chain
    elif method_clean == "refine":
        chain = load_summarize_chain(llm, chain_type="refine")
        res = chain.invoke({"input_documents": docs})
        return res["output_text"]

    else:
        raise ValueError(f"Unknown summarization method: '{method}'. Choose from: prompt, stuff, map_reduce, refine.")


def main():
    print("==========================================================")
    print("Part 5: Unified Document Summarizer Function (Task 13)")
    print("==========================================================")

    with open(doc_path, "r", encoding="utf-8") as f:
        text = f.read()

    methods = ["prompt", "stuff", "map_reduce", "refine"]
    for m in methods:
        print(f"\n--- Method: '{m}' ---")
        summary = summarize_document(text, method=m)
        print(f"Summary Output:\n{summary}")


if __name__ == "__main__":
    main()
