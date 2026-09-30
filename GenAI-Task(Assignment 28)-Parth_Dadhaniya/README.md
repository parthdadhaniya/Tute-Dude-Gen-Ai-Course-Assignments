# Assignment 28: Q&A RAG Chatbot with Message History

**Student:** Parth Dadhaniya  
**Course:** GenAI - TuteDude  

---

## Overview

In real-world GenAI production systems, a chatbot cannot answer questions in isolation. Users ask follow-up questions like *"Explain more"*, *"What about sick leave compared to that?"*, or reference previous answers using pronouns. 

In this assignment, I built a complete conversational RAG system using LangChain that combines:
1. **Document Ingestion**: Loading documents using `TextLoader` and `PyPDFLoader`, and chunking with `RecursiveCharacterTextSplitter`.
2. **Vector Store & Retrieval**: Storing embeddings using Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`) inside a persistent `ChromaDB` index.
3. **Conversational RAG Prompt**: Grounding answers strictly in retrieved context using `ChatPromptTemplate` and dynamic chat history with `MessagesPlaceholder`.
4. **History Management & Trimming**: Sliding window trimming to prevent token context overflow.
5. **Multi-Turn Testing**: Validating context retention across factual questions, follow-ups, comparisons, and out-of-scope grounding tests.
6. **Stateful Chatbot Mini-Project**: Supporting session isolation (`session_id`), CLI interaction, and an optional Streamlit web UI.

---

## File Structure

```text
GenAI-Task(Assignment 28)-Parth_Dadhaniya/
├── data/
│   ├── company_policy.txt            # Document covering company policies
│   └── sample.pdf                    # Reused PDF document
├── chroma_db/                        # Persisted Chroma vector store index
├── config.py                         # Model setup (Groq or local fallback)
├── part1_document_ingestion.py       # Tasks 1 & 2: Document loading and text splitting
├── part2_vector_store.py             # Tasks 3 & 4: Embeddings and vector store retrieval
├── part3_part4_rag_chain.py          # Tasks 5-8: RAG prompt, chain, history, and trimming
├── part5_testing.py                  # Task 9: Multi-turn Q&A testing
├── part6_chatbot_app.py              # Task 10: Stateful RAG assistant mini project & CLI
├── streamlit_app.py                  # Task 10: Optional Streamlit web chat UI
├── task11_observations.py            # Task 11: Conceptual observations & trade-offs
├── main.py                           # Master script running all tasks
├── assignment28.ipynb                # Interactive Jupyter Notebook
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
```

---

## Tasks Summary

### Part 1: Document Ingestion (Tasks 1 & 2)
- Used `TextLoader` and `PyPDFLoader` to load policy documents and PDFs.
- Split documents using `RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)`.
- Verified chunk boundaries and metadata.

### Part 2: Vector Store & Retriever (Tasks 3 & 4)
- Generated 384-dimensional embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Persisted vector representations inside `chroma_db/`.
- Created a top-$k$ retriever (`k=2`).

### Part 3 & 4: RAG Prompt, Chain, History & Trimming (Tasks 5, 6, 7, 8)
- Structured the prompt with strict system instructions:
  - Answer strictly based on retrieved context.
  - Say *"I don't know based on the provided documents"* if missing.
  - Insert past conversation using `MessagesPlaceholder(variable_name="chat_history")`.
- Implemented sliding-window trimming to keep the last $N$ turns, ensuring prompt tokens remain predictable.

### Part 5: Multi-Turn Q&A Testing (Task 9)
Tested the full pipeline through a 4-turn dialog:
1. *Initial question:* `"What is the annual leave policy?"` -> Returns 20 days entitlement.
2. *Follow-up:* `"Explain more about how it is carried forward."` -> Understands "it" refers to annual leave and explains carry-forward limits.
3. *Clarification / Contrast:* `"What about sick leave compared to that?"` -> Contrasts 10 days sick leave with the previous annual leave rules.
4. *Grounding test:* `"What is the capital of Mars?"` -> Correctly responds *"I don't know based on the provided documents."*

### Part 6: Mini Project & Observations (Tasks 10 & 11)
- Built `DocumentRAGChatbot` supporting multiple isolated user sessions (`session_1`, `session_2`) and session reset.
- Provided an interactive CLI mode (`--interactive`).
- Built an optional Streamlit chat interface (`streamlit_app.py`) displaying conversation bubbles and retrieved source chunks.
- Documented key engineering trade-offs regarding conversational RAG, anaphora resolution, token latency, and history trimming.

---

## How to Run

### Run All Tasks (Master Script)
```bash
python main.py
```

### Run Individual Parts
```bash
python part1_document_ingestion.py
python part2_vector_store.py
python part3_part4_rag_chain.py
python part5_testing.py
python part6_chatbot_app.py
python task11_observations.py
```

### Interactive Terminal CLI
```bash
python part6_chatbot_app.py --interactive
```

### Launch Optional Streamlit Web App
```bash
streamlit run streamlit_app.py
```
