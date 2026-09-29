# Task 2: Hugging Face Embedding Model
# Parth Dadhaniya

import time
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# load chunks
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

# load local huggingface model
print("Loading Hugging Face model: all-MiniLM-L6-v2...")
t0 = time.time()
model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print(f"Model loaded in {time.time() - t0:.2f} seconds.")

# embed first chunk
vec = model.embed_query(chunks[0].page_content)

print("\nModel: sentence-transformers/all-MiniLM-L6-v2")
print("Vector length (dimensions):", len(vec))
print("Sample values (first 5):", [round(x, 4) for x in vec[:5]])

# test embedding multiple chunks
t1 = time.time()
batch_vecs = model.embed_documents([c.page_content for c in chunks[:3]])
print(f"\nEmbedded 3 chunks in {time.time() - t1:.3f} seconds.")
print("Each vector dimension:", len(batch_vecs[0]))

print("\nComparison with OpenAI:")
print("- HuggingFace: 384 dimensions (runs locally, free, completely offline)")
print("- OpenAI: 1536 dimensions (cloud API, pay-per-token)")
