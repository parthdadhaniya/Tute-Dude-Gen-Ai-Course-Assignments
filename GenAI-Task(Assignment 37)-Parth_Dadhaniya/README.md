# Assignment 37: AstraDB Cloud Vector Database & PDF Query RAG

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering — TuteDude  
**Topic:** DataStax AstraDB Serverless Vector Database, Document Splitting, Dense Embeddings, LangChain RAG, Multi-Turn Session State, and Grounding Guardrails  

---

## 📌 Problem Statement & Enterprise Scenario

Many real-world GenAI products require **cloud-native, horizontally scalable vector databases** to index millions of enterprise documents and power low-latency Retrieval-Augmented Generation (RAG). Local in-memory vector stores (like basic FAISS) do not support concurrent multi-user workloads or automated cloud persistence.

In this assignment, we build an end-to-end **PDF Query RAG System using DataStax AstraDB**, demonstrating:
1. Connecting LangChain with AstraDB using application tokens and DB API endpoints.
2. Ingesting, chunking, and embedding multi-page PDF documents.
3. Storing dense 384-dimensional vector embeddings in AstraDB with persistence verification.
4. Constructing a grounded RAG pipeline that answers in-scope questions and gracefully refuses out-of-context queries.
5. Providing an interactive **Streamlit web application** leveraging `st.session_state` for conversational memory.

---

## 📂 Project Structure

```
GenAI-Task(Assignment 37)-Parth_Dadhaniya/
├── config.py                 # AstraDB configuration, embedding setup, and local persistent fallback
├── data/
│   ├── enterprise_ai_manual.pdf     # 5-page enterprise AI deployment manual
│   └── astradb_persisted_store.json # Persisted vectors and metadata
├── part1_astradb_setup.py    # Tasks 1 & 2: AstraDB setup guide & connection verification
├── part2_pdf_processing.py   # Tasks 3 & 4: PDF loading, chunking, embedding & persistence check
├── part3_rag_pipeline.py     # Tasks 5 & 6: RAG chain & 5+ question testing (with negative test)
├── part4_observations.py     # Core answers: Production RAG, Session State, FAISS vs AstraDB
├── app.py                    # Interactive Streamlit UI with st.session_state conversation history
├── main.py                   # Master runner executing all tasks sequentially
├── assignment37.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Student assignment documentation
```

---

## 🚀 Tasks & Implementation Details

### Tasks 1 & 2: AstraDB Setup & Connection
- **File:** `part1_astradb_setup.py`
- **DataStax AstraDB Setup:**
  1. Create a serverless vector database (`genai_rag_db`) at `https://astra.datastax.com`.
  2. Generate an Application Token with `Database Administrator` permissions (`AstraCS:...`).
  3. Copy the DB API Endpoint URL (`https://<db-id>-<region>.apps.astra.datastax.com`).
  4. Integrate with `langchain-astradb`:
     ```python
     from langchain_astradb import AstraDBVectorStore
     store = AstraDBVectorStore(
         collection_name="pdf_rag_collection",
         embedding=embeddings,
         api_endpoint=endpoint,
         token=token,
         namespace="default_keyspace"
     )
     ```
  5. The system includes an authentic local persistent vector store (`LocalAstraDBStore`) that saves records to `data/astradb_persisted_store.json` for offline testing without active cloud tokens.

---

### Tasks 3 & 4: PDF Ingestion, Splitting & Embedding Storage
- **File:** `part2_pdf_processing.py`
- **PDF Ingestion:** Loads `enterprise_ai_manual.pdf` (5 pages) using `PyPDFLoader`.
- **Text Splitting:** Uses `RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50)`.
- **Vector Storage:** Embeds text chunks into 384-dimensional vectors using `all-MiniLM-L6-v2` and persists them in AstraDB.
- **Persistence Verification:** Confirms all 10 document chunks are written to disk/cloud and validates via a live similarity query.

---

### Tasks 5 & 6: PDF Query RAG Pipeline & Validation
- **File:** `part3_rag_pipeline.py`
- **Pipeline Architecture:**
  $$\text{PDF} \longrightarrow \text{Splitter} \longrightarrow \text{Embeddings} \longrightarrow \text{AstraDB} \longrightarrow \text{Retriever} \longrightarrow \text{LLM} \longrightarrow \text{Answer}$$
- **Prompt Guardrail:** Strictly instructs the model to use **only** the retrieved context and reply `"I do not know based on the provided document"` when information is missing.
- **Testing Results Across 6 Scenarios:**

| Q# | Scenario | Target Policy / Section | Result & Grounding Verification |
| :--- | :--- | :--- | :--- |
| **Q1** | Approved Models | Section 1.2 | Llama 3.1 8B/70B and Groq LPU inference. |
| **Q2** | Real-Time Latency | Section 1.3 | Sub-100ms first-token latency. |
| **Q3** | Vector DB Mandate | Section 3.2 | DataStax AstraDB with 384-dim MiniLM-L6-v2. |
| **Q4** | Out-of-Scope Policy | Section 4.3 | Model must state refusal and refuse speculation. |
| **Q5** | Data Privacy & PII | Section 2.1 | Tier-1 access controls and encrypted storage. |
| **Q6** | Negative Test (Cookie Recipe) | Out-of-Context | Correctly refused: *"I do not know based on the provided document..."* |

---

## 💡 Observations & Architectural Insights

### 1. Why AstraDB is Useful for Production RAG
- **Serverless Scaling:** Eliminates the operational complexity of managing, sharding, and provisioning vector index nodes.
- **Cassandra Core:** Built on Apache Cassandra, providing five-nines (99.999%) availability, multi-region replication, and sub-millisecond retrieval.
- **Unified Hybrid Search:** Supports combining vector similarity search with structured metadata filtering (e.g., user tenants, timestamps, access tiers).

### 2. Importance of Session State in GenAI Applications
- **Conversational Memory:** Preserves multi-turn dialogue context across HTTP requests, allowing natural follow-ups using pronouns (*"what about its latency?"*).
- **UI State Preservation:** Frameworks like Streamlit rerun the entire script on each interaction; `st.session_state` preserves chat history and index caches.
- **Token Cost Control:** Enables sliding-window trimming to keep prompts within LLM token budgets.

### 3. Comparison: FAISS vs DataStax AstraDB

| Feature | FAISS (Meta) | DataStax AstraDB |
| :--- | :--- | :--- |
| **Architecture** | Local C++ vector search library | Distributed cloud vector database |
| **Persistence** | Ephemeral in-memory (manual dump) | Automatic, durable persistent cloud storage |
| **Scalability** | Bound to single-node RAM/VRAM | Scales horizontally to billions of vectors |
| **Concurrency** | Single-process / non-concurrent | High concurrent multi-user read/write |
| **Security & RBAC** | None (file permission only) | Cloud IAM, application tokens, encryption at rest |
| **Maintenance** | Self-managed infrastructure | Fully managed serverless service |

---

## 🛠️ How to Run

### 1. Installation
```bash
cd "GenAI-Task(Assignment 37)-Parth_Dadhaniya"
pip install -r requirements.txt
```

### 2. (Optional) Configure Live AstraDB Credentials
Create a `.env` file in the folder:
```env
ASTRA_DB_APPLICATION_TOKEN=AstraCS:...
ASTRA_DB_API_ENDPOINT=https://<database-id>-<region>.apps.astra.datastax.com
ASTRA_DB_KEYSPACE=default_keyspace
ASTRA_DB_COLLECTION=pdf_rag_collection
```
*(If no `.env` is supplied, the project runs in offline mode using the verified local persistent vector store.)*

### 3. Run the Master CLI Runner
```bash
python main.py
```

### 4. Run the Streamlit Interactive Web Application
```bash
streamlit run app.py
```

### 5. Launch the Jupyter Notebook
```bash
jupyter notebook assignment37.ipynb
```

