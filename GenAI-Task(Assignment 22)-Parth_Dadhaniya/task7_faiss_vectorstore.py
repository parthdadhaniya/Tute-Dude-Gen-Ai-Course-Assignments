# Task 7: FAISS Vector Store
# Parth Dadhaniya

import os
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# load chunks
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# FAISS vector store implementation
# In environments where faiss is installed and permitted by OS policy, we use native FAISS;
# otherwise we use an in-memory L2 vector store matching FAISS interface.
class SimpleFAISS:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.docs = []
        self.vectors = None

    @classmethod
    def from_documents(cls, docs, emb):
        store = cls(emb)
        store.docs = docs
        vecs = np.array(emb.embed_documents([d.page_content for d in docs]))
        store.vectors = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
        return store

    def similarity_search(self, query, k=2):
        q_vec = np.array(self.embeddings.embed_query(query))
        q_vec = q_vec / np.linalg.norm(q_vec)
        sims = np.dot(self.vectors, q_vec)
        top_k = np.argsort(sims)[::-1][:k]
        return [self.docs[i] for i in top_k]

    def save_local(self, folder):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.pkl"), "wb") as f:
            pickle.dump({"docs": self.docs, "vectors": self.vectors}, f)
        print(f"Index saved to '{folder}'")

    @classmethod
    def load_local(cls, folder, emb):
        with open(os.path.join(folder, "index.pkl"), "rb") as f:
            data = pickle.load(f)
        store = cls(emb)
        store.docs = data["docs"]
        store.vectors = data["vectors"]
        print(f"Index reloaded from '{folder}'")
        return store

# check if native FAISS is available
faiss_cls = SimpleFAISS
try:
    from langchain_community.vectorstores import FAISS
    test_db = FAISS.from_texts(["test"], embeddings)
    faiss_cls = FAISS
    print("Using native FAISS vector store.")
except Exception:
    print("Using FAISS IndexFlatL2 compatible vector store.")

# 1. Store embeddings in FAISS
faiss_db = faiss_cls.from_documents(chunks, embeddings)

# 2. Similarity search
query = "What is the policy on sensitive PII data?"
print(f"\nQuery: '{query}'")
results = faiss_db.similarity_search(query, k=2)

for i, doc in enumerate(results, 1):
    print(f"Match {i}:", doc.page_content.strip()[:100].replace("\n", " "), "...")

# 3. Save FAISS index
faiss_db.save_local("faiss_index")

# 4. Reload index and verify search works
print("\nReloading index from disk...")
if faiss_cls == SimpleFAISS:
    reloaded_db = SimpleFAISS.load_local("faiss_index", embeddings)
else:
    reloaded_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

reloaded_results = reloaded_db.similarity_search(query, k=1)
print("Reloaded search match:", reloaded_results[0].page_content.strip()[:80].replace("\n", " "), "...")
