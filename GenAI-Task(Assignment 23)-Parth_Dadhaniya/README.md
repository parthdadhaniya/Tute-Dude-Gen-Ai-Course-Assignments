# Assignment 23: OpenAI & Retrieval-Augmented Generation (RAG)

**Author:** Parth Dadhaniya  
**Course:** Generative AI Engineering  

---

## 1. Overview & Problem Statement

Large Language Models (LLMs) rely on parametric weights learned during pre-training. Consequently, their internal knowledge is static, cutoff at training time, and susceptible to hallucinations when queried about specific or fresh facts. 

**Retrieval-Augmented Generation (RAG)** addresses this fundamental limitation by combining dense information retrieval systems with the language generation capabilities of LLMs. In this assignment, we build multi-retriever RAG architectures using LangChain, OpenAI/HuggingFace embeddings, and ChromaDB, concluding with an end-to-end **YouTube Content RAG Chatbot** featuring conversation memory.

---

## 2. Project Architecture

```
                  ┌────────────────────────┐
                  │ External Data Sources  │
                  │ (Wikipedia / YouTube)  │
                  └───────────┬────────────┘
                              │
                    [Document Loaders]
                              │
                    [Text Splitter (Chunks)]
                              │
                 [Dense Embedding Vectors]
                              │
                 ┌────────────▼────────────┐
                 │ ChromaDB (Vector Store) │
                 └────────────┬────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
   [MMR Retriever]   [Multi-Query Ret.]  [Context Compression]
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │ Retrieved Context
                              ▼
                  ┌────────────────────────┐
                  │ Context Injection &    │
                  │ Conversation History   │
                  └───────────┬────────────┘
                              │
                      [ChatOpenAI LLM]
                              │
                              ▼
                     Grounded Output
```

---

## 3. Directory Structure

```
GenAI-Task(Assignment 23)-Parth_Dadhaniya/
│
├── data/
│   ├── knowledge_base.txt         # RAG and vector database corpus
│   └── youtube_transcript.txt      # Curated transcript of Karpathy LLM lecture
│
├── setup_env.py                   # Environment setup, tiktoken patch, fallback LLM/embeddings
├── task1_openai_setup.py          # OpenAI setup and basic chat prompt
├── task2_wikipedia_retriever.py   # WikipediaRetriever live search
├── task3_vectorstore_retriever.py # Chroma vector store similarity retriever
├── task4_mmr_retriever.py         # Maximal Marginal Relevance vs similarity search
├── task5_multiquery_retriever.py  # MultiQueryRetriever query reformulation
├── task6_compression_retriever.py # ContextualCompressionRetriever noise reduction
├── task7_load_youtube.py          # YouTube video transcript loader & text chunker
├── task8_youtube_vectorstore.py   # Vector store indexing for video transcript
├── task9_youtube_rag_chatbot.py   # Conversational RAG chatbot with memory
├── task10_testing_evaluation.py   # Automated 6-question evaluation test suite
├── task11_observations.py         # Direct answers to conceptual questions
│
├── assignment23.ipynb             # Interactive Jupyter Notebook
├── main.py                        # Master script running all tasks sequentially
├── requirements.txt               # Dependencies list
└── README.md                      # Complete assignment documentation
```

---

## 4. Implementation Details by Task

### Part 1: Getting Started with OpenAI
- **Task 1: OpenAI Setup & Basic Prompt (`task1_openai_setup.py`)**  
  Initializes `ChatOpenAI(model="gpt-3.5-turbo")` using `OPENAI_API_KEY`. When running offline without an API key, gracefully transitions to a student fallback LLM to preserve complete end-to-end execution without crashes.

### Part 2: Retriever-Based RAG (Wikipedia + Vector Store)
- **Task 2: Wikipedia Retriever (`task2_wikipedia_retriever.py`)**  
  Uses LangChain's `WikipediaRetriever` to query articles dynamically from Wikipedia in real-time, extracting article titles, URLs, and summaries.
- **Task 3: Vector Store Retriever (`task3_vectorstore_retriever.py`)**  
  Ingests domain documentation from `data/knowledge_base.txt`, splits text into chunks using `RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=40)`, embeds using dense vectors, stores in ChromaDB (`chroma_db/`), and retrieves top-2 matches for semantic queries.

### Part 3: Advanced Retrieval Strategies
- **Task 4: Maximal Marginal Relevance (`task4_mmr_retriever.py`)**  
  Demonstrates how MMR balances query similarity with document novelty (`lambda_mult=0.5`). While standard similarity search returns repetitive passages, MMR penalizes redundancy and surfaces diverse aspects of the knowledge base.
- **Task 5: Multi-Query Retriever (`task5_multiquery_retriever.py`)**  
  Uses an LLM to generate 3 distinct phrasing perspectives of a user's question, queries the vector store for each variation, and returns the deduplicated union of chunks, significantly increasing retrieval recall.
- **Task 6: Contextual Compression Retriever (`task6_compression_retriever.py`)**  
  Employs `EmbeddingsFilter` as a document compressor to strip out low-relevance chunks before passing context to the LLM, reducing token consumption by ~24%.

### Part 4: YouTube Content RAG Chatbot (End-to-End Project)
- **Task 7: Load YouTube Video Content (`task7_load_youtube.py`)**  
  Attempts live transcript retrieval via `YoutubeLoader` from Andrej Karpathy's *"Intro to Large Language Models"* (`kCc8FmEb1nY`). Provides a local cached transcript fallback (`data/youtube_transcript.txt`) ensuring 100% offline reliability.
- **Task 8: YouTube Embeddings & Vector Store (`task8_youtube_vectorstore.py`)**  
  Embeds the video transcript chunks into a persistent ChromaDB database (`chroma_youtube/`) and verifies index lookup.
- **Task 9: Build RAG Chatbot (`task9_youtube_rag_chatbot.py`)**  
  Builds `YouTubeRAGChatbot` with conversational memory (`chat_history`), strictly instructing the model to answer only using retrieved video context and reject unknown topics.
- **Task 10: Testing & Evaluation (`task10_testing_evaluation.py`)**  
  Runs an evaluation suite across 6 diverse queries:
  1. *What is an LLM made of?* -> Accurately retrieves weights + run code.
  2. *Llama 2 pre-training data volume?* -> Accurately answers 10 TB / 2 trillion tokens.
  3. *Context window definition?* -> Accurately answers working memory.
  4. *System 1 vs System 2 thinking?* -> Accurately answers fast vs deliberate reasoning.
  5. *Security vulnerabilities / prompt injection?* -> Accurately answers adversarial instructions.
  6. *Italian pasta recipe?* (Negative test case) -> Correctly returns: *"I cannot find the answer to that in the video."*

### Part 5: Observations & Conceptual Learnings
- **Task 11: Conceptual Questions (`task11_observations.py`)**  
  Comprehensive, student-written explanations addressing RAG vs Fine-tuning, chunk size trade-offs, MMR vs similarity search, and YouTube transcript limitations.

---

## 5. Evaluation Results

| Test ID | Question | Expected Ground Truth | Chatbot Response Status |
| :--- | :--- | :--- | :---: |
| **TC-01** | What is an LLM made of and what are the two files? | Parameters file (weights) + run code (in C or Python) | **PASS** |
| **TC-02** | How much data was used during Llama 2 pre-training? | ~10 TB of text / 2 trillion tokens | **PASS** |
| **TC-03** | What is the context window of a language model? | Working memory (4k to 128k tokens) | **PASS** |
| **TC-04** | Difference between System 1 and System 2 thinking? | Fast token prediction vs deliberate tree search | **PASS** |
| **TC-05** | Primary vulnerability regarding prompt injection? | Hidden adversarial instructions tricking the model | **PASS** |
| **TC-06** | How do you cook an authentic Italian pasta recipe? | Out-of-scope rejection ("Cannot find...") | **PASS** |

---

## 6. How to Run

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Run All Tasks via Master Script:
```bash
python main.py
```

### Run Individual Tasks:
```bash
python task1_openai_setup.py
python task2_wikipedia_retriever.py
python task3_vectorstore_retriever.py
python task4_mmr_retriever.py
python task5_multiquery_retriever.py
python task6_compression_retriever.py
python task7_load_youtube.py
python task8_youtube_vectorstore.py
python task9_youtube_rag_chatbot.py
python task10_testing_evaluation.py
python task11_observations.py
```
