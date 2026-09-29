# Task 4: Directory Loader
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import DirectoryLoader, TextLoader, CSVLoader, PyPDFLoader

# loading different file types from data directory using appropriate loader classes
loaders = {
    "Text (.txt)": DirectoryLoader("data", glob="**/*.txt", loader_cls=TextLoader),
    "CSV (.csv)": DirectoryLoader("data", glob="**/*.csv", loader_cls=CSVLoader),
    "PDF (.pdf)": DirectoryLoader("data", glob="**/*.pdf", loader_cls=PyPDFLoader)
}

all_documents = []

print("Loading documents from 'data/' directory...\n")
for file_type, loader in loaders.items():
    docs = loader.load()
    all_documents.extend(docs)
    print(f"Loaded {len(docs)} documents using {file_type} loader.")

print(f"\nTotal documents loaded from directory: {len(all_documents)}")
print("\nDocument Verification (Source and Length):")
for i, doc in enumerate(all_documents, 1):
    source = doc.metadata.get("source", "unknown")
    page = doc.metadata.get("page", "-")
    content_len = len(doc.page_content)
    print(f"{i}. Source: {source} | Page: {page} | Characters: {content_len}")
