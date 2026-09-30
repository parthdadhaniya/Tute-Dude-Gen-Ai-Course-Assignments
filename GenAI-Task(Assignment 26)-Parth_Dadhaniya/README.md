# Assignment 26: Groq API Chatbot, RAG & FastAPI Serving

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering  

---

## Overview

This assignment covers building a low-latency AI backend using the **Groq API**, constructing a document-grounded **Retrieval-Augmented Generation (RAG)** pipeline with Chroma, and serving the application as a production-grade REST API using **FastAPI** and **Pydantic**.

### Core Objectives:
1. **Groq API Inference:** Set up the official Groq Python SDK and query low-latency open-weight models (e.g. `llama3-8b-8192` or `llama-3.1-70b-versatile`).
2. **Chatbot Core Logic:** Build `groq_chat()` handling system and user message roles.
3. **Groq + RAG Pipeline:** Retrieve relevant chunks from local documents (`notes.txt`, `data.csv`, `sample.pdf`, `handbook.md`), construct grounded prompt templates, and return answers with source citations.
4. **FastAPI Backend:** Expose endpoints (`GET /health`, `POST /chat`) with Pydantic request validation and error handling.
5. **Local Serving & Testing:** Run and verify endpoints using Uvicorn, Swagger UI, and automated test clients.
6. **Production Readiness:** Environment-based secrets management, logging, and performance analysis.

---

## Project Structure

```text
GenAI-Task(Assignment 26)-Parth_Dadhaniya/
│
├── data/                             # Reused dataset documents
│   ├── notes.txt                     # Text document (GenAI notes)
│   ├── data.csv                      # Tabular CSV document (Employees data)
│   ├── sample.pdf                    # PDF document (AI Knowledge Base)
│   └── handbook.md                   # Markdown document (Company handbook)
│
├── chroma_db/                        # Persisted Chroma vector database
├── config.py                         # Groq API configuration and inference handler
├── vector_store.py                   # Document loader, chunking & retrieval logic
│
├── task1_groq_setup.py               # Task 1: Groq API setup and basic prompt test
├── task2_groq_chatbot.py             # Task 2: Core chatbot function with system/user roles
├── task3_task4_groq_rag.py           # Tasks 3 & 4: Grounded RAG pipeline & prompt template
├── app.py                            # Tasks 5, 6 & 8: FastAPI backend with Pydantic validation & logging
├── task7_task9_api_test.py           # Tasks 7 & 9: Automated FastAPI endpoint verification
├── task10_observations.py            # Task 10: Observations & insights
│
├── main.py                           # Master runner executing all tasks sequentially
├── assignment26.ipynb                # Interactive Jupyter Notebook
├── requirements.txt                  # Python dependencies
└── README.md                         # Assignment documentation
```

---

## Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Groq API Key (Optional for Live Cloud Calls)
1. Sign up for a free account at [https://console.groq.com](https://console.groq.com).
2. Generate an API Key in the **API Keys** section.
3. Set the key in your terminal:
   - **Windows (PowerShell):**
     ```powershell
     $env:GROQ_API_KEY="gsk_your_actual_key_here"
     ```
   - **Linux / macOS:**
     ```bash
     export GROQ_API_KEY="gsk_your_actual_key_here"
     ```

*Note: If no API key is set, the application automatically uses a built-in context-aware student fallback so all scripts, RAG queries, and FastAPI tests run offline without errors.*

---

## How to Run

### Run All Assignment Tasks:
```bash
python main.py
```

### Run Individual Task Scripts:
```bash
python task1_groq_setup.py
python task2_groq_chatbot.py
python task3_task4_groq_rag.py
python task7_task9_api_test.py
python task10_observations.py
```

### Start the Live FastAPI Backend Service:
```bash
uvicorn app:app --reload --port 8000
```
Once started, visit:
- **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Health Check Endpoint:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## API Endpoints Reference

### 1. `GET /health`
Returns service status, model name, and API key configuration state.
- **Response:**
  ```json
  {
    "status": "healthy",
    "service": "Groq LLM & RAG Backend",
    "model": "llama3-8b-8192",
    "groq_api_key_configured": true
  }
  ```

### 2. `POST /chat`
Accepts a user query, optionally applies RAG retrieval against local documents, and returns the grounded answer with latency metrics.
- **Request Body:**
  ```json
  {
    "query": "What is the annual leave policy according to the employee handbook?",
    "use_rag": true
  }
  ```
- **Response:**
  ```json
  {
    "query": "What is the annual leave policy according to the employee handbook?",
    "answer": "According to the employee handbook, team members receive 20 days of paid annual leave.",
    "latency_seconds": 0.045,
    "sources": ["sample.pdf", "notes.txt"],
    "model": "llama3-8b-8192"
  }
  ```

---

## Part 5: Observations & Insights (Task 10)

### 1. Why is Groq suitable for real-time applications?
Groq uses custom hardware called Language Processing Units (LPUs). Unlike traditional GPUs that rely on high-bandwidth external memory (HBM) and dynamic instruction scheduling, Groq LPUs use on-chip SRAM with deterministic compiler scheduling. This generates tokens at speeds exceeding 300 to 500 tokens per second, making it ideal for real-time conversational agents, voice interfaces, and instant search engines.

### 2. Groq vs OpenAI latency comparison (conceptual):
- **Groq:** Extremely low time-to-first-token (TTFT) and throughput often 3x-10x faster than cloud GPU clusters. Ideal for low-latency production inference on open weights (Llama 3, Mistral).
- **OpenAI:** Industry-leading reasoning depth (GPT-4o) and multimodal support, but incurs higher queuing times and round-trip network latency due to centralized server infrastructure.

### 3. What are the benefits of an API-first GenAI architecture?
- **Frontend Agnostic:** A single FastAPI service can serve web apps, mobile apps, Slack bots, and internal tools.
- **Decoupled Scalability:** The backend can scale horizontally and swap underlying LLM providers (e.g. Groq, OpenAI, Ollama) without touching client-side code.
- **Centralized Security & Governance:** API keys, rate limits, PII sanitization, and RAG retrieval pipelines remain securely hosted on the server without exposing secrets to frontend clients.
