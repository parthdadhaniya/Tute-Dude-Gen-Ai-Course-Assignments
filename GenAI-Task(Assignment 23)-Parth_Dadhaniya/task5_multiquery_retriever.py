# Task 5: Multi-Query Retriever
# Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.language_models.fake import FakeListLLM

try:
    from langchain_classic.retrievers.multi_query import MultiQueryRetriever
except ImportError:
    from langchain.retrievers.multi_query import MultiQueryRetriever

print("--- Task 5: Multi-Query Retriever ---")

# load data and build vector store
docs = TextLoader("data/knowledge_base.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=30)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings)
base_retriever = db.as_retriever(search_kwargs={"k": 2})

# initialize LLM using config helper (OpenAI -> Groq -> FakeListLLM)
llm = config.get_llm()
if llm is None:
    llm = FakeListLLM(responses=[
        "1. What are vector databases and embeddings in RAG?\n"
        "2. How do vector stores improve retrieval in language models?\n"
        "3. Explain embeddings and vector search."
    ])

mq_retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

query = "How do vector stores and embeddings assist RAG systems?"
print("User Query:", query)

# compare single query vs multi query
single_docs = base_retriever.invoke(query)
mq_docs = mq_retriever.invoke(query)

print(f"\nSingle Query found {len(single_docs)} chunks:")
for i, d in enumerate(single_docs, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:100]}...")

print(f"\nMulti-Query found {len(mq_docs)} unique chunks:")
for i, d in enumerate(mq_docs, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:100]}...")

print("\nTakeaway: Multi-Query rephrases the prompt from different angles so we don't miss relevant chunks.")
