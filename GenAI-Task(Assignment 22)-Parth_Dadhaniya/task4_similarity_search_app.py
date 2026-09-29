# Task 4: Similarity Search App (Core Logic)
# Parth Dadhaniya

import numpy as np
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Load documents
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
docs.extend(CSVLoader("data/data.csv", encoding="utf-8").load())

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)
print("Total chunks in index:", len(chunks))

# 2. Convert chunks to embeddings
model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
chunk_texts = [c.page_content for c in chunks]
chunk_vectors = np.array(model.embed_documents(chunk_texts))

# normalize vectors for cosine similarity
chunk_vectors = chunk_vectors / np.linalg.norm(chunk_vectors, axis=1, keepdims=True)

# 3. Search function
def search(query, top_k=3):
    q_vec = np.array(model.embed_query(query))
    q_vec = q_vec / np.linalg.norm(q_vec)
    
    # cosine similarity is dot product of unit vectors
    scores = np.dot(chunk_vectors, q_vec)
    top_indices = np.argsort(scores)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append((chunks[idx], scores[idx]))
    return results

# 4. Test 3 queries
queries = [
    "What are the privacy and compliance rules?",
    "Who works on the backend engineer role?",
    "Why is text splitting needed for large documents?"
]

for q in queries:
    print(f"\nQuery: '{q}'")
    matches = search(q, top_k=2)
    for i, (chunk, score) in enumerate(matches, 1):
        src = chunk.metadata.get("source", "unknown")
        print(f"  Match {i} (score: {score:.3f}, source: {src}):")
        print("   ", chunk.page_content.strip()[:100].replace("\n", " "), "...")
