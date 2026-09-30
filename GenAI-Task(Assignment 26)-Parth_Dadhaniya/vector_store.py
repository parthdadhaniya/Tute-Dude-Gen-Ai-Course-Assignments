# vector_store.py
# Student: Parth Dadhaniya
# Course: Generative AI Engineering

import os
import warnings
warnings.filterwarnings("ignore")

import config

# cached vectorstore instance
_db = None

def get_vectorstore():
    global _db
    if _db is not None:
        return _db
    
    if os.path.exists(config.CHROMA_DIR) and len(os.listdir(config.CHROMA_DIR)) > 0:
        try:
            from langchain_community.embeddings import HuggingFaceEmbeddings
            from langchain_community.vectorstores import Chroma
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            _db = Chroma(persist_directory=config.CHROMA_DIR, embedding_function=embeddings)
            return _db
        except Exception:
            return None
    return None

def get_relevant_chunks(query, k=2):
    """
    Retrieves the most relevant document chunks for a query from Chroma or data/ files.
    """
    db = get_vectorstore()
    if db is not None:
        try:
            results = db.similarity_search(query, k=k)
            return [
                {
                    "content": doc.page_content.strip(),
                    "source": os.path.basename(doc.metadata.get("source", "document"))
                }
                for doc in results
            ]
        except Exception:
            pass

    # fast fallback: search local text files directly
    chunks = []
    q_words = set(query.lower().split())

    for filename in ["handbook.md", "notes.txt", "data.csv"]:
        filepath = os.path.join(config.DATA_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                paragraphs = [p.strip() for p in content.split("\n\n") if len(p.strip()) > 30]
                for p in paragraphs:
                    chunks.append({"content": p, "source": filename})

    scored = []
    for c in chunks:
        score = sum(1 for w in q_words if w in c["content"].lower())
        scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for score, c in scored[:k]]

if __name__ == "__main__":
    test_query = "What is the annual leave policy?"
    matches = get_relevant_chunks(test_query, k=2)
    print(f"Retrieved {len(matches)} chunks for: '{test_query}'")
    for i, m in enumerate(matches, 1):
        print(f"\n[Chunk {i}] Source: {m['source']}")
        print(m["content"][:120] + "...")
