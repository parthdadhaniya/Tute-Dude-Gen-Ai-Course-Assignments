# Assignment 31: Conversational PDF Q&A Chatbot with Message History

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I built a Conversational Retrieval-Augmented Generation (RAG) assistant for PDF documents. The application maintains conversational memory across multiple turns, accurately answers follow-up queries using past context, and strictly grounds answers in the retrieved PDF passages.

Key capabilities:
1. **Multi-Page PDF Ingestion:** Loading `.pdf` documents using LangChain `PyPDFLoader` and splitting them into clean chunks with `RecursiveCharacterTextSplitter`.
2. **Dense Vector Embeddings & ChromaDB:** Storing 384-dimensional dense vectors using Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`) in a persistent Chroma vector database.
3. **Conversational Prompting:** Injecting dynamic multi-turn history into `ChatPromptTemplate` using `MessagesPlaceholder(variable_name="chat_history")`.
4. **History Trimming:** Applying sliding-window trimming to retain the most recent interaction turns and prevent context window overflow.
5. **Streamlit Chat Application:** An interactive web UI with PDF upload, memory slider, live vector indexing, and collapsible source citations.

---

## File Structure

```text
GenAI-Task(Assignment 31)-Parth_Dadhaniya/
├── data/
│   ├── enterprise_ai_manual.pdf      # 5-page enterprise AI policy and technical manual
│   └── sample.pdf                    # 2-page sample PDF document
├── chroma_db/                        # Persisted ChromaDB vector index
├── config.py                         # Model setup (ChatGroq with clean local fallback)
├── part1_pdf_ingestion.py            # Tasks 1 & 2: PDF loading and chunk splitting
├── part2_vector_store.py             # Tasks 3 & 4: Embeddings and Chroma vector store
├── part3_part4_rag_chain.py          # Tasks 5 - 8: RAG prompt, chain, history & trimming
├── part5_testing.py                  # Task 9: Multi-turn follow-up testing & grounding
├── task11_observations.py            # Task 11: Conceptual observations & insights
├── app.py                            # Task 10: Streamlit web chatbot application
├── streamlit_app.py                  # Streamlit entrypoint alias
├── main.py                           # Master script running all console tasks
├── assignment31.ipynb                # Interactive Jupyter Notebook
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## Task Details

### Part 1: PDF Ingestion & Preprocessing (Tasks 1 & 2)
- Loaded PDF documents (`enterprise_ai_manual.pdf` and `sample.pdf`, totaling 7 pages) using `PyPDFLoader`.
- Split pages into 14 distinct chunks using `RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)`.
- Verified that page numbers, file names, and document structure are preserved in chunk metadata.

### Part 2: Embeddings & Vector Store (Tasks 3 & 4)
- Generated dense 384-dimensional embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Indexed all chunks into a persistent Chroma vector store (`chroma_db/`).
- Verified similarity retrieval with top-$k$ retriever (`k=2`).

### Part 3 & Part 4: Conversational Prompt, RAG Chain & History Trimming (Tasks 5 - 8)
- Structured the prompt with strict system instructions:
  - Answer strictly using facts from the retrieved PDF context.
  - State *"I don't know based on the provided documents"* if information is absent.
  - Use past conversation turns to understand pronouns and follow-up questions.
- Implemented sliding-window trimming (`trim_history`) to keep recent interaction turns and avoid context degradation.

### Part 5: Multi-Turn Follow-Up Q&A Testing (Task 9)
Tested the pipeline across four conversational turns:
1. **Factual:** *"What models are approved for enterprise workloads?"*  
   -> Returned Llama 3.1 8B/70B and Groq LPU inference.
2. **Follow-Up:** *"Explain more about their inference speed and real-time requirements."*  
   -> Understood reference and retrieved sub-100ms TTFT requirements.
3. **Clarification:** *"What is the data retention policy for conversation logs?"*  
   -> Retrieved 30-day retention rule.
4. **Grounding Test:** *"What is the average temperature on Mars?"*  
   -> Responded with *"I don't know based on the provided documents."*

### Part 6: Mini-Project & Observations (Tasks 10 & 11)
- Built interactive Streamlit UI in `app.py`.
- Conceptual insights:
  1. *PDF Q&A vs. Conversational PDF Q&A:* Standard Q&A treats queries independently; conversational Q&A maintains chat memory to resolve follow-ups.
  2. *Role of Message History:* Provides context to decode pronouns ("that", "it") into precise search intent.
  3. *Long Memory Trade-Offs:* Excessive memory leads to higher latency, token costs, and attention distraction.
  4. *Trimming Impact:* Sliding-window trimming preserves recent turns while keeping inference fast and predictable.

---

## Streamlit Interface Mockup

```text
+---------------------------------------------------------------------------------------+
|  📄 Conversational PDF Assistant                                                      |
|  Ask factual and follow-up questions grounded in your PDF documents.                  |
|                                                                                       |
|  [Sidebar]                           [Chat Conversation]                              |
|  - Groq API Key: [ ************ ]                                                     |
|  - Model: [ llama-3.1-8b-instant ]   Assistant:                                       |
|  - Memory: [ slider: 6 messages ]      Hello! I am your Conversational PDF Assistant.  |
|  - File Upload: [ Browse PDF... ]      Ask me anything about the loaded PDF document. |
|  - [Index Uploaded PDF]                                                               |
|  - Active: enterprise_ai_manual.pdf  User:                                            |
|  - Chunks: 14 chunks                   What models are approved for enterprise work?   |
|  - [Clear Conversation]                                                               |
|                                      Assistant:                                       |
|                                        Production workloads use Llama 3.1 8B/70B      |
|                                        and Groq LPU inference.                        |
|                                                                                       |
|                                        ▼ 🔍 Retrieved PDF Passages (2 chunks)        |
|                                           - Source: enterprise_ai_manual.pdf (Page 1)  |
|                                                                                       |
|                                      [ Ask a question about the PDF... ]              |
+---------------------------------------------------------------------------------------+
```

---

## How to Run

### 1. Run All Console Tasks
```bash
cd "GenAI-Task(Assignment 31)-Parth_Dadhaniya"
python main.py
```

### 2. Launch Streamlit Web UI (Task 10)
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.
