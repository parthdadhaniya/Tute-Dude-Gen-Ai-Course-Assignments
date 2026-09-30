# part2_pdf_processing.py - PDF Ingestion, Text Splitting & AstraDB Storage
# Student: Parth Dadhaniya

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import get_astradb_vectorstore, get_embeddings, PERSISTENCE_FILE

PDF_PATH = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_manual.pdf")


def load_pdf_document(pdf_path: str = PDF_PATH):
    """Loads PDF pages using LangChain PyPDFLoader."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages


def split_pdf_pages(pages, chunk_size: int = 350, chunk_overlap: int = 50):
    """Splits document pages into chunks using RecursiveCharacterTextSplitter."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = text_splitter.split_documents(pages)
    return chunks


def store_in_astradb(chunks):
    """Generates embeddings and stores document chunks in AstraDB vector store."""
    embeddings = get_embeddings()
    store, mode = get_astradb_vectorstore(embeddings)

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    # Store embeddings in AstraDB
    store.add_texts(texts, metadatas=metadatas)
    return store, mode


def verify_persistence(store, mode: str):
    """Verifies that vector records are persisted and retrievable."""
    print("\n--- Persistence Verification ---")
    if hasattr(store, "documents"):
        doc_count = len(store.documents)
        print(f"Total documents persisted : {doc_count}")
        print(f"Persistence file location : {PERSISTENCE_FILE}")
        print(f"File exists on disk       : {os.path.exists(PERSISTENCE_FILE)}")
    else:
        print(f"Store Mode: {mode}")
        print("Connected to live AstraDB cloud collection.")

    # Verification similarity search test
    test_query = "approved models for production"
    test_results = store.similarity_search(test_query, k=1)
    if test_results:
        print(f">> Persistence Check Passed: Search query '{test_query}' successfully matched:")
        print(f"   Excerpt: {test_results[0].page_content[:120]}...")
    else:
        print(">> Warning: Persistence search returned 0 results.")


def run_tasks_3_and_4():
    """Executes Task 3 (PDF Ingestion & Splitting) and Task 4 (Embedding & AstraDB Storage)."""
    print("============================================================")
    print("Task 3: Load & Split PDF Document")
    print("Student: Parth Dadhaniya")
    print("============================================================")

    print(f"Target PDF Path: {PDF_PATH}")
    pages = load_pdf_document()
    print(f"Number of Pages Loaded : {len(pages)}")
    print(f"Page 1 Content Preview :\n{pages[0].page_content.strip()[:200]}...\n")

    chunks = split_pdf_pages(pages, chunk_size=350, chunk_overlap=50)
    print(f"Number of Chunks Created : {len(chunks)}")
    print(f"Sample Chunk (Index 0):\n--- Content ---\n{chunks[0].page_content.strip()}")
    print(f"--- Metadata ---\n{chunks[0].metadata}\n")

    print("============================================================")
    print("Task 4: Store Embeddings in AstraDB & Verify Persistence")
    print("============================================================")
    store, mode = store_in_astradb(chunks)
    print(f"Vector Store Backend : {mode}")
    print(f"Total Chunks Stored  : {len(chunks)}")

    verify_persistence(store, mode)
    return store, chunks


if __name__ == "__main__":
    run_tasks_3_and_4()

