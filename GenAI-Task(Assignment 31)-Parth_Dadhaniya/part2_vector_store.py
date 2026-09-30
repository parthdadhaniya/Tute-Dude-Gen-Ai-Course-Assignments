# Part 2: Embeddings & Vector Store (Tasks 3 & 4)
# Student: Parth Dadhaniya

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from part1_pdf_ingestion import load_pdfs, split_text

chroma_path = os.path.join(os.path.dirname(__file__), "chroma_db")


def get_embeddings():
    # 384-dimensional dense vectors
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def get_vectorstore():
    embeddings = get_embeddings()
    # load if already indexed, else create
    if os.path.exists(chroma_path) and os.listdir(chroma_path):
        return Chroma(persist_directory=chroma_path, embedding_function=embeddings)

    pages = load_pdfs()
    chunks = split_text(pages)
    return Chroma.from_documents(chunks, embeddings, persist_directory=chroma_path)


def get_retriever(k=2):
    db = get_vectorstore()
    return db.as_retriever(search_kwargs={"k": k})


def main():
    print("--- Tasks 3 & 4: Embeddings & Vector Store ---")
    retriever = get_retriever(k=2)

    query = "What models are approved for enterprise workloads?"
    print(f"Test query: {query}")
    results = retriever.invoke(query)
    print(f"Found {len(results)} matching chunks.")
    if results:
        print(f"Top chunk snippet: {results[0].page_content.strip()[:150]}")


if __name__ == "__main__":
    main()
