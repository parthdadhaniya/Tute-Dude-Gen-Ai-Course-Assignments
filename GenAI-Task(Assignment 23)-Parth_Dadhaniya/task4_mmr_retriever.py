# Task 4: Maximal Marginal Relevance (MMR) Retriever
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("--- Task 4: Maximal Marginal Relevance (MMR) Retriever ---")

# load and chunk text
docs = TextLoader("data/knowledge_base.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings)

query = "Vector databases ChromaDB and FAISS similarity search"
print(f"Query: {query}\n")

# 1. normal similarity search
sim_retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
sim_results = sim_retriever.invoke(query)

print("1. Normal Similarity Search Results:")
for i, d in enumerate(sim_results, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:110]}...")

# 2. MMR search (balances relevance with diversity)
mmr_retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 3, "fetch_k": 8, "lambda_mult": 0.5})
mmr_results = mmr_retriever.invoke(query)

print("\n2. MMR Search Results (More Diverse):")
for i, d in enumerate(mmr_results, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:110]}...")

print("\nWhy MMR helps:")
print("- Normal similarity returns chunks that can be almost identical.")
print("- MMR adds a penalty for similar documents, giving the LLM a wider range of facts.")
