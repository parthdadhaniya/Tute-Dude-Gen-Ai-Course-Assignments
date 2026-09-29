# Task 8: ChromaDB Vector Store
# Parth Dadhaniya

import os
import shutil
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# clean old directory to test fresh
if os.path.exists("chroma_db"):
    try:
        shutil.rmtree("chroma_db")
    except Exception:
        pass

# 1. Load document chunks
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
docs.extend(CSVLoader("data/data.csv", encoding="utf-8").load())
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Create and persist ChromaDB
print("Creating persistent ChromaDB collection in 'chroma_db'...")
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)
print("Saved document embeddings to ChromaDB.")

# 3. Similarity search
query = "Who is the DevOps Cloud Architect?"
print(f"\nQuery: '{query}'")
results = db.similarity_search(query, k=2)

for i, doc in enumerate(results, 1):
    src = doc.metadata.get("source", "unknown")
    print(f"Result {i} (source: {src}):")
    print(" ", doc.page_content.strip()[:100].replace("\n", " "), "...")

# 4. Reload from disk to verify persistence
print("\nReloading ChromaDB from disk...")
reloaded_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)
reloaded_results = reloaded_db.similarity_search(query, k=1)
print("Top match from reloaded database:")
print(" ", reloaded_results[0].page_content.strip()[:100].replace("\n", " "), "...")
