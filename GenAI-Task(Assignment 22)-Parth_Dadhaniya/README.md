# Assignment 22: Embedding Models, Vector Stores & Similarity Search
**Student:** Parth Dadhaniya  
**Course:** GenAI Course  
**Role:** Generative AI Engineer  
**Scenario:** Personal Knowledge Search Engine (Core Retrieval Backbone for RAG)

---

## 1. Project Overview
After documents are loaded and split into coherent chunks, the foundation of any Retrieval-Augmented Generation (RAG) system is:
1. Converting text chunks into mathematical vectors (embeddings) using embedding models (OpenAI, Hugging Face, Ollama).
2. Storing and indexing vectors in vector databases (FAISS, ChromaDB).
3. Performing similarity search (Cosine / L2 distance) to retrieve relevant context for user queries.

This assignment implements and evaluates each component of the retrieval pipeline in a clean, human-writable Python student codebase.

---

## 2. Directory Structure
```
GenAI-Task(Assignment 22)-Parth_Dadhaniya/
│
├── data/
│   ├── notes.txt                        # Company notes on architecture & AI policy
│   ├── data.csv                         # Tabular employee and project records
│   ├── handbook.md                      # Structured markdown handbook with headers
│   └── sample.pdf                       # Multi-page reference PDF document
│
├── task1_openai_embeddings.py           # Task 1: OpenAI embedding model (1536 dims)
├── task2_huggingface_embeddings.py      # Task 2: Hugging Face all-MiniLM-L6-v2 (384 dims)
├── task3_comparison.py                  # Task 3: Comparison - OpenAI vs Hugging Face
├── task4_similarity_search_app.py       # Task 4: Core cosine similarity search app
├── task5_langchain_search.py            # Task 5: Similarity search with LangChain abstraction
├── task6_ollama_embeddings.py           # Task 6: Ollama nomic-embed-text local setup
├── task7_faiss_vectorstore.py           # Task 7: FAISS vector store & index persistence
├── task8_chroma_vectorstore.py          # Task 8: ChromaDB vector store & persistence
├── task9_faiss_vs_chroma.py             # Task 9: FAISS vs ChromaDB comparison
├── task10_similarity_pipeline.py        # Task 10: End-to-End switchable similarity pipeline
├── task11_observations.py               # Task 11: Core observations & RAG insights
│
├── main.py                              # Master sequential runner executing all tasks
├── assignment22.ipynb                   # Interactive Jupyter Notebook
├── requirements.txt                     # Project dependencies
└── README.md                            # Assignment documentation
```

---

## 3. Implementation Details

### Part 1 — Embedding Models
- **Task 1: OpenAI Embedding Model (`task1_openai_embeddings.py`):**
  - Uses OpenAI's `text-embedding-3-small` (1536 dimensions).
  - Demonstrates vector generation with a clean student offline fallback.
- **Task 2: Hugging Face Embedding Model (`task2_huggingface_embeddings.py`):**
  - Uses `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions).
  - Fast, local, and 100% offline inference with zero API cost.
- **Task 3: Comparison (`task3_comparison.py`):**
  - Compares cloud vs local trade-offs: data privacy, offline capabilities, compute requirements, and API token costs.

### Part 2 — Document Similarity Search
- **Task 4: Core Similarity Search App (`task4_similarity_search_app.py`):**
  - Implements `search(query, top_k=3)` using raw NumPy cosine similarity over the embeddings matrix.
  - Tested across 3 diverse queries: compliance rules, backend engineers, and text splitting rationale.
- **Task 5: LangChain Abstraction (`task5_langchain_search.py`):**
  - Uses LangChain's vector store abstraction (`vectorstore.similarity_search(query)`) with ChromaDB.

### Part 3 — Ollama Embeddings
- **Task 6: Ollama Local Setup (`task6_ollama_embeddings.py`):**
  - Details local Ollama installation (`ollama serve`, `ollama pull nomic-embed-text`).
  - Generates 768-dimensional embeddings and evaluates local privacy benefits.

### Part 4 — Vector Stores
- **Task 7: FAISS Vector Store (`task7_faiss_vectorstore.py`):**
  - Builds in-memory index, runs similarity search, persists to disk (`faiss_index/`), and reloads to verify persistence.
- **Task 8: ChromaDB Vector Store (`task8_chroma_vectorstore.py`):**
  - Creates an on-disk collection in `chroma_db/`, stores document chunks with metadata, queries the database, and tests reloaded persistence.
- **Task 9: FAISS vs ChromaDB (`task9_faiss_vs_chroma.py`):**
  - Compares in-memory vs persistent storage, billion-scale GPU indexing (FAISS), and metadata-rich application databases (ChromaDB).

### Part 5 — Mini Project Integration
- **Task 10: End-to-End Similarity Pipeline (`task10_similarity_pipeline.py`):**
  - Pipeline: `Documents -> Splitter -> Embeddings -> Vector Store -> Similarity Search`.
  - Supports switchable embedding backends (`openai`, `huggingface`) and vector stores (`faiss`, `chroma`).
- **Task 11: Observations & Insights (`task11_observations.py`):**
  - Answers importance of embeddings, necessity of vector databases (ANN vs B-Tree), and how this forms the retrieval backbone of RAG.

---

## 4. How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tasks Sequentially
```bash
python main.py
```

### Run Individual Tasks
```bash
python task1_openai_embeddings.py
python task2_huggingface_embeddings.py
python task3_comparison.py
python task4_similarity_search_app.py
python task5_langchain_search.py
python task6_ollama_embeddings.py
python task7_faiss_vectorstore.py
python task8_chroma_vectorstore.py
python task9_faiss_vs_chroma.py
python task10_similarity_pipeline.py
python task11_observations.py
```
