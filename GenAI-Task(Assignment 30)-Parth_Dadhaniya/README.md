# Assignment 30: Chat Groq RAG Application with Streamlit UI

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I built a Retrieval-Augmented Generation (RAG) chatbot using the **Groq API (`ChatGroq`)** and deployed it as an interactive web application with **Streamlit**.

Key features:
1. **Low-Latency Inference:** Groq LPU models (`llama-3.1-8b-instant`) generate tokens at 300-500+ tokens per second.
2. **Document Ingestion:** Loading `.txt` and `.pdf` files, then chunking them with `RecursiveCharacterTextSplitter`.
3. **Embeddings & ChromaDB:** Storing 384-dimensional vector embeddings (`all-MiniLM-L6-v2`) in a Chroma vector store.
4. **Conversational Prompting:** Using `ChatPromptTemplate` and `MessagesPlaceholder` to ground answers in document context and support multi-turn follow-ups.
5. **Streamlit UI:** A clean interface allowing users to upload documents, ask questions, and inspect the retrieved source chunks.

---

## File Structure

```text
GenAI-Task(Assignment 30)-Parth_Dadhaniya/
├── data/
│   ├── ai_handbook.txt               # Knowledge base text document
│   └── sample.pdf                    # Reused PDF document
├── chroma_db/                        # Persistent ChromaDB vector index
├── config.py                         # ChatGroq model setup with local fallback
├── part1_groq_setup.py               # Tasks 1 & 2: Setup and basic latency benchmark
├── part2_part3_rag_pipeline.py       # Tasks 3 - 6: Ingestion, ChromaDB, RAG prompt and chain
├── part5_testing.py                  # Task 9: Multi-turn chat testing & grounding
├── task11_observations.py            # Task 11: Conceptual questions & answers
├── app.py                            # Tasks 7, 8 & 10: Streamlit web application
├── streamlit_app.py                  # Alias for Streamlit
├── main.py                           # Master script running all console tasks
├── assignment30.ipynb                # Jupyter Notebook
├── requirements.txt                  # Python libraries
└── README.md                         # Project documentation
```

---

## Task Details

### Part 1: Groq Setup & Basic Chat (Tasks 1 & 2)
- Initialized `ChatGroq` with `llama-3.1-8b-instant`.
- Measured inference turnaround time (~0.02s - 0.04s), verifying high throughput.

### Parts 2 & 3: RAG Pipeline & Chain (Tasks 3 - 6)
- Loaded technical documents with `TextLoader` and `PyPDFLoader`.
- Split documents into 300-character chunks with 50-character overlap.
- Created embeddings with Hugging Face (`all-MiniLM-L6-v2`) and indexed them in ChromaDB.
- Constructed a RAG chain connecting retriever, context injection, chat history, and ChatGroq.

### Part 4: Streamlit UI (Tasks 7, 8 & 10)
- Built `app.py` with:
  - Sidebar for API key, model selection, and PDF/TXT file uploader.
  - Interactive chat panel using `st.chat_input` and `st.chat_message`.
  - Collapsible source citations using `st.expander` for answer transparency.

### Part 5: Multi-Turn Conversation Testing (Task 9)
Tested four conversational turns:
1. Factual question: Retrieval from document chunks.
2. Follow-up query: Resolves context using chat history.
3. Clarification: Queries specific technical terms (embeddings, vector store).
4. Out-of-context check: Answered with *"I don't know based on the provided documents."*

### Part 6: Observations & Learnings (Task 11)
1. **Why Groq is suitable for RAG:**  
   Groq LPUs use on-chip SRAM instead of GPU memory bus, delivering 300-500+ tokens/sec so conversational turnarounds feel instant.
2. **Groq RAG vs. OpenAI RAG:**  
   Groq provides drastically faster token generation and lower per-token cost for open models. OpenAI provides stronger general multimodal capabilities and larger context windows.
3. **Role of Streamlit:**  
   Allows building complete full-stack web chat applications in pure Python without frontend web frameworks.

---

## How to Run

### 1. Run All Console Tasks
```bash
python main.py
```

### 2. Launch the Streamlit App
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.
