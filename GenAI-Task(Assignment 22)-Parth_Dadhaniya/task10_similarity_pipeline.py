# Task 10: End-to-End Similarity Search Pipeline
# Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, CSVLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# load all files from folder
def load_and_chunk(data_dir="data"):
    docs = []
    for root, _, files in os.walk(data_dir):
        for f in files:
            p = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()
            if ext == ".txt" or ext == ".md":
                docs.extend(TextLoader(p, encoding="utf-8").load())
            elif ext == ".csv":
                docs.extend(CSVLoader(p, encoding="utf-8").load())
            elif ext == ".pdf":
                docs.extend(PyPDFLoader(p).load())
                
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    return splitter.split_documents(docs)

# pipeline supporting switchable embedding and vector store backends
def run_similarity_pipeline(query, embedding_choice="huggingface", store_choice="chroma"):
    print(f"\n--- Pipeline: Embedding='{embedding_choice}' | VectorStore='{store_choice}' ---")
    
    # 1. Documents & Chunker
    chunks = load_and_chunk("data")
    print(f"Loaded {len(chunks)} chunks.")
    
    # 2. Embedding Model
    if embedding_choice == "huggingface":
        emb = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    else:
        # fallback embedding for testing
        from langchain_core.embeddings import Embeddings
        import numpy as np
        class DemoEmbeddings(Embeddings):
            def embed_documents(self, texts):
                np.random.seed(42)
                return [np.random.randn(1536).tolist() for _ in texts]
            def embed_query(self, text):
                np.random.seed(42)
                return np.random.randn(1536).tolist()
        emb = DemoEmbeddings()

    # 3. Vector Store
    if store_choice == "chroma":
        store = Chroma.from_documents(chunks, emb)
    else:
        # FAISS in-memory
        from task7_faiss_vectorstore import SimpleFAISS
        store = SimpleFAISS.from_documents(chunks, emb)
        
    # 4. Similarity Search
    print(f"Searching for: '{query}'")
    results = store.similarity_search(query, k=1)
    print("Top Result:")
    print(" ", results[0].page_content.strip()[:120].replace("\n", " "), "...")
    return results

if __name__ == "__main__":
    # Test 1: Hugging Face + ChromaDB
    run_similarity_pipeline("Who is the NLP specialist?", "huggingface", "chroma")
    
    # Test 2: OpenAI style + FAISS
    run_similarity_pipeline("What are the compliance rules?", "openai", "faiss")
