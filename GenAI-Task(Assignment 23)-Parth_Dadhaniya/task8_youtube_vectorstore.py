# Task 8: YouTube Embeddings & Vector Store
# Parth Dadhaniya

import os
import shutil
import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("--- Task 8: YouTube Embeddings & Vector Store ---")

# load video transcript
loader = TextLoader("data/youtube_transcript.txt", encoding="utf-8")
docs = loader.load()

# split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=280, chunk_overlap=30)
chunks = splitter.split_documents(docs)
print(f"Loaded {len(chunks)} transcript chunks.")

# create embeddings and store in ChromaDB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

persist_dir = "./chroma_youtube"
if os.path.exists(persist_dir):
    try:
        shutil.rmtree(persist_dir)
    except Exception:
        pass

db = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
print("Saved video chunks to ChromaDB at:", persist_dir)

# test search
query = "What are the two files that make up an LLM?"
print("\nTesting query:", query)

retriever = db.as_retriever(search_kwargs={"k": 2})
matches = retriever.invoke(query)

print(f"\nTop match from video:")
print(matches[0].page_content.strip())
