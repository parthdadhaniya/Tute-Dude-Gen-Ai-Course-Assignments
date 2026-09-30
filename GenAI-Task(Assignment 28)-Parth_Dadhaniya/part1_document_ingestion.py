# Part 1: Document Ingestion for RAG (Tasks 1 & 2)
# Student: Parth Dadhaniya

import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def load_documents():
    """Task 1: Load text and PDF documents using LangChain loaders."""
    print("--- Task 1: Load Documents ---")
    documents = []

    # 1. Load Text Document
    txt_path = os.path.join(DATA_DIR, "company_policy.txt")
    if os.path.exists(txt_path):
        txt_loader = TextLoader(txt_path, encoding="utf-8")
        txt_docs = txt_loader.load()
        documents.extend(txt_docs)
        print(f"Loaded Text Document : {os.path.basename(txt_path)} ({len(txt_docs)} doc)")

    # 2. Load PDF Document
    pdf_path = os.path.join(DATA_DIR, "sample.pdf")
    if os.path.exists(pdf_path):
        try:
            pdf_loader = PyPDFLoader(pdf_path)
            pdf_docs = pdf_loader.load()
            documents.extend(pdf_docs)
            print(f"Loaded PDF Document  : {os.path.basename(pdf_path)} ({len(pdf_docs)} pages)")
        except Exception as e:
            print(f"PDF loading skipped: {e}")

    print(f"Total documents loaded: {len(documents)}")
    print("\nSample content from first document:")
    print("-" * 50)
    print(documents[0].page_content[:250].strip() + "...\n")
    return documents


def split_documents(docs, chunk_size=300, chunk_overlap=50):
    """Task 2: Split loaded documents into chunks using RecursiveCharacterTextSplitter."""
    print("--- Task 2: Text Splitting ---")
    print(f"Configuring RecursiveCharacterTextSplitter (chunk_size={chunk_size}, chunk_overlap={chunk_overlap})...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_documents(docs)

    print(f"Total document chunks created: {len(chunks)}")
    print("\nSample Chunk 1:")
    print("-" * 50)
    print(chunks[0].page_content.strip())
    print("-" * 50)
    print(f"Metadata: {chunks[0].metadata}")
    return chunks


if __name__ == "__main__":
    raw_docs = load_documents()
    doc_chunks = split_documents(raw_docs)
