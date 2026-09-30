# Part 1: PDF Ingestion & Preprocessing (Tasks 1 & 2)
# Student: Parth Dadhaniya

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data_folder = os.path.join(os.path.dirname(__file__), "data")


def load_pdfs():
    # load enterprise manual and sample pdf
    files = ["enterprise_ai_manual.pdf", "sample.pdf"]
    pages = []
    for f in files:
        path = os.path.join(data_folder, f)
        if os.path.exists(path):
            loader = PyPDFLoader(path)
            pages.extend(loader.load())
    return pages


def split_text(pages):
    # split into 300 character chunks with 50 overlap
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    return splitter.split_documents(pages)


def main():
    print("--- Task 1: Load PDF Documents ---")
    pages = load_pdfs()
    print(f"Total pages loaded: {len(pages)}")
    if pages:
        print(f"Sample page content:\n{pages[0].page_content[:200]}...\n")

    print("--- Task 2: Text Splitting ---")
    chunks = split_text(pages)
    print(f"Total chunks created: {len(chunks)}")
    if chunks:
        print(f"Sample chunk:\n{chunks[0].page_content.strip()}")


if __name__ == "__main__":
    main()
