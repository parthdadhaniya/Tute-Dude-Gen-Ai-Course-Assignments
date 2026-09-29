# Task 11: Unified Preprocessing Pipeline
# Author: Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")

os.environ["USER_AGENT"] = "PersonalKnowledgeAssistant/1.0"

from langchain_community.document_loaders import TextLoader, CSVLoader, PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_documents(path_or_url, chunk_size=400, chunk_overlap=50):
    """
    Unified ingestion & splitting pipeline:
    - Automatically handles Web URLs, directories, or individual files.
    - Loads raw documents using appropriate LangChain loaders.
    - Splits content into chunks using RecursiveCharacterTextSplitter.
    """
    raw_docs = []
    
    # 1. Handle Web URL
    if str(path_or_url).startswith(("http://", "https://")):
        print(f"Loading web content from: {path_or_url}")
        loader = WebBaseLoader(path_or_url)
        raw_docs = loader.load()
        
    # 2. Handle Directory
    elif os.path.isdir(path_or_url):
        print(f"Loading all files from directory: '{path_or_url}'")
        for root, _, files in os.walk(path_or_url):
            for filename in files:
                file_path = os.path.join(root, filename)
                ext = os.path.splitext(filename)[1].lower()
                
                if ext == ".txt":
                    raw_docs.extend(TextLoader(file_path, encoding="utf-8").load())
                elif ext == ".csv":
                    raw_docs.extend(CSVLoader(file_path, encoding="utf-8").load())
                elif ext == ".pdf":
                    raw_docs.extend(PyPDFLoader(file_path).load())

    # 3. Handle Single File
    elif os.path.isfile(path_or_url):
        print(f"Loading single file: '{path_or_url}'")
        ext = os.path.splitext(path_or_url)[1].lower()
        if ext == ".txt":
            raw_docs = TextLoader(path_or_url, encoding="utf-8").load()
        elif ext == ".csv":
            raw_docs = CSVLoader(path_or_url, encoding="utf-8").load()
        elif ext == ".pdf":
            raw_docs = PyPDFLoader(path_or_url).load()
    else:
        raise ValueError(f"Target not found: {path_or_url}")

    print(f"Raw documents loaded: {len(raw_docs)}")

    # 4. Split loaded documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_documents(raw_docs)
    print(f"Total chunks generated: {len(chunks)}")
    return chunks


if __name__ == "__main__":
    print("=" * 65)
    print("Test 1: Applying Pipeline to Local 'data/' Directory")
    print("=" * 65)
    local_chunks = load_and_split_documents("data", chunk_size=350, chunk_overlap=40)
    print(f"Local chunks produced: {len(local_chunks)}")
    print("\nSample Local Chunk:")
    print("Source:", local_chunks[0].metadata)
    print("Content Preview:\n", local_chunks[0].page_content.strip())

    print("\n" + "=" * 65)
    print("Test 2: Applying Pipeline to Web URL")
    print("=" * 65)
    web_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    web_chunks = load_and_split_documents(web_url, chunk_size=400, chunk_overlap=50)
    print(f"Web chunks produced: {len(web_chunks)}")
    print("\nSample Web Chunk:")
    print("Source:", web_chunks[0].metadata)
    print("Content Preview:\n", " ".join(web_chunks[0].page_content.split())[:200])
