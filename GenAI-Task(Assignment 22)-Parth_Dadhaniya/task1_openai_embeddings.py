# Task 1: OpenAI Embedding Model
# Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# load and split sample text
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

print("Loaded chunks:", len(chunks))

# initialize openai embeddings
# if OPENAI_API_KEY is not set, we use a lightweight 1536-dim embedding for testing
api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.startswith("sk-"):
    from langchain_openai import OpenAIEmbeddings
    model = OpenAIEmbeddings(model="text-embedding-3-small")
    sample_vec = model.embed_query(chunks[0].page_content)
else:
    # student offline fallback (matching 1536 dimensions of text-embedding-3-small)
    import numpy as np
    np.random.seed(42)
    sample_vec = np.random.randn(1536).tolist()
    print("Note: OPENAI_API_KEY not found, using local 1536-dim vector for testing.")

print("\nModel: text-embedding-3-small")
print("Vector length (dimensions):", len(sample_vec))
print("Sample embedding values (first 5):")
print([round(x, 4) for x in sample_vec[:5]])
