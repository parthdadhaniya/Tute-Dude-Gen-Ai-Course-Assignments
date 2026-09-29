# Task 3: Vector Store Retriever
# Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("--- Task 3: Vector Store Retriever ---")

# 1. load document
loader = TextLoader("data/knowledge_base.txt", encoding="utf-8")
docs = loader.load()
print(f"Loaded {len(docs)} document.")

# 2. split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)
print(f"Split into {len(chunks)} chunks.")

# 3. embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. store in ChromaDB
db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
print("Saved to ChromaDB.")

# 5. create retriever
retriever = db.as_retriever(search_kwargs={"k": 2})

# 6. similarity search
query = "How does RAG solve hallucinations?"
print("\nQuery:", query)

results = retriever.invoke(query)
print(f"\nRetrieved {len(results)} chunks:")
for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content.strip())
