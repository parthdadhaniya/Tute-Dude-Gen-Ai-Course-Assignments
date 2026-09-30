# Part 2: Vector Store & Retriever (Tasks 3 & 4)
# Student: Parth Dadhaniya

import os
import warnings

# Suppress noisy deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from part1_document_ingestion import load_documents, split_documents

CHROMA_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")

_embeddings = None
_vectorstore = None


def get_embeddings():
    """Task 3: Initialize embedding model."""
    global _embeddings
    if _embeddings is None:
        print("--- Task 3: Create Embeddings ---")
        print("Loading HuggingFace embedding model: all-MiniLM-L6-v2...")
        _embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        print("Embedding model ready (Dimension: 384).")
    return _embeddings


def get_vectorstore(force_rebuild=False):
    """Task 4: Store document embeddings in Chroma vector store and return it."""
    global _vectorstore
    if _vectorstore is not None and not force_rebuild:
        return _vectorstore

    embeddings = get_embeddings()

    # If Chroma DB already exists on disk and has data, load it directly
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR) and not force_rebuild:
        print("Loading existing Chroma vector store from disk...")
        _vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
        return _vectorstore

    print("--- Task 4: Store Embeddings in Vector Store ---")
    print("Ingesting document chunks into Chroma vector store...")
    docs = load_documents()
    chunks = split_documents(docs)

    _vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    print(f"Stored {len(chunks)} chunks in Chroma DB at: {CHROMA_DIR}")
    return _vectorstore


def get_retriever(k=2):
    """Creates a retriever from the vector store."""
    vstore = get_vectorstore()
    return vstore.as_retriever(search_kwargs={"k": k})


def test_retriever():
    retriever = get_retriever(k=2)
    query = "What is the annual leave policy?"
    print(f"\nTesting retriever with query: '{query}'")
    results = retriever.invoke(query)
    print(f"Retrieved {len(results)} chunks:")
    for i, doc in enumerate(results, 1):
        print(f"\nChunk {i} (Source: {os.path.basename(doc.metadata.get('source', 'unknown'))}):")
        print(doc.page_content.strip())


if __name__ == "__main__":
    get_embeddings()
    get_vectorstore()
    test_retriever()
