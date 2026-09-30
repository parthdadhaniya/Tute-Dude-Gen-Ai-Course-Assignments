# Assignment 25: Prompting & LangChain Chains

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering  

---

## Overview

This assignment covers advanced prompting, structured output generation with Pydantic, chain architectures (simple, conditional, parallel), and LangChain Expression Language (LCEL) with Runnables and an end-to-end RAG pipeline.

### Objectives:
1. **Prompt Templates:** Build and compare `PromptTemplate` and `ChatPromptTemplate` with dynamic variable injection.
2. **Structured Output with Pydantic:** Enforce an `Answer` schema (`answer`, `confidence`, `source`) using `PydanticOutputParser` and implement validation error recovery.
3. **Chains in LangChain:** Create simple linear chains, conditional routing chains (`RunnableBranch`), and multi-task parallel chains (`RunnableParallel`).
4. **Runnables & LCEL:** Build modular pipelines using `RunnablePassthrough`, `RunnableLambda`, and the LCEL pipe (`|`) operator.
5. **LCEL-Based RAG:** Ingest documents (Text, CSV, PDF), store chunks in a Chroma vector store, and construct a full retrieval pipeline.
6. **Observations & Insights:** Analyze trade-offs between structured vs unstructured outputs, LCEL vs legacy chains, and parallel vs conditional routing.

---

## Project Structure

```text
GenAI-Task(Assignment 25)-Parth_Dadhaniya/
│
├── data/                             # Reused dataset documents
│   ├── notes.txt                     # Text document (GenAI notes)
│   ├── data.csv                      # Tabular CSV document (Employees data)
│   ├── sample.pdf                    # PDF document (AI Knowledge Base)
│   └── handbook.md                   # Markdown document (Company handbook)
│
├── chroma_db/                        # Persisted Chroma vector database
├── config.py                         # Environment paths and LLM handler
├── vector_store.py                   # Document loader, chunking & Chroma index builder
│
├── task1_prompt_template.py          # Task 1: PromptTemplate with dynamic injection
├── task2_chat_prompt_template.py     # Task 2: ChatPromptTemplate with role-based messages
├── task3_pydantic_schema.py          # Task 3: Pydantic Output Schema (Answer model)
├── task4_validation_fallback.py      # Task 4: Error handling and schema recovery
├── task5_simple_chain.py             # Task 5: Simple Chain (Prompt | LLM | Parser)
├── task6_conditional_chain.py        # Task 6: Conditional Routing Chain (RAG vs Direct)
├── task7_parallel_chain.py           # Task 7: Parallel Chain (Answer + Summary + Questions)
├── task8_runnables_lcel.py           # Task 8: Runnables basics & LCEL composition
├── task9_lcel_rag.py                 # Task 9: Complete LCEL RAG pipeline
├── task10_observations.py            # Task 10: Observations & insights
│
├── main.py                           # Master script executing all 10 tasks sequentially
├── assignment25.ipynb                # Interactive Jupyter Notebook
├── requirements.txt                  # Python dependencies
└── README.md                         # Assignment documentation
```

---

## Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Variables (Optional)
If you have an OpenAI API key, set it in your terminal:
- **Windows (PowerShell):**
  ```powershell
  $env:OPENAI_API_KEY="your-api-key-here"
  ```
- **Linux / macOS:**
  ```bash
  export OPENAI_API_KEY="your-api-key-here"
  ```

*Note: If no API key is provided, the project automatically uses `StudentLocalChatModel` so all tasks, RAG retrievals, and tests run offline without errors.*

---

## How to Run

### Run All Tasks Sequentially:
```bash
python main.py
```

### Run Individual Tasks:
```bash
python task1_prompt_template.py
python task2_chat_prompt_template.py
python task3_pydantic_schema.py
python task4_validation_fallback.py
python task5_simple_chain.py
python task6_conditional_chain.py
python task7_parallel_chain.py
python task8_runnables_lcel.py
python task9_lcel_rag.py
python task10_observations.py
```

---

## Task Details & Implementations

### Part 1: Prompt Templates
- **Task 1 (`task1_prompt_template.py`):** Creates a `PromptTemplate` with system instructions and user placeholder. Formats questions dynamically and executes through an LCEL chain.
- **Task 2 (`task2_chat_prompt_template.py`):** Uses `ChatPromptTemplate` with `SystemMessage`, `HumanMessage`, and `AIMessage`. Compares single-string `PromptTemplate` with modern role-separated chat templates.

### Part 2: Structured Output using Pydantic
- **Task 3 (`task3_pydantic_schema.py`):** Defines the `Answer` Pydantic model (`answer: str`, `confidence: float`, `source: str`). Injects parser instructions into the prompt and validates output into strongly typed objects.
- **Task 4 (`task4_validation_fallback.py`):** Demonstrates handling malformed raw outputs and incomplete JSON. Catches `OutputParserException` and safely falls back to a standardized `Answer` instance.

### Part 3: Chains in LangChain
- **Task 5 (`task5_simple_chain.py`):** Implements a linear chain: `Prompt | LLM | StrOutputParser` and executes across multiple topics.
- **Task 6 (`task6_conditional_chain.py`):** Uses `RunnableBranch` to inspect query intent. Factual queries (policies, employee records, definitions) are routed through the Chroma RAG retriever; conversational greetings route directly to the LLM.
- **Task 7 (`task7_parallel_chain.py`):** Uses `RunnableParallel` to execute 3 tasks concurrently: generating an answer, a 1-sentence summary, and 2 follow-up questions from a single input topic.

### Part 4: Runnables & LCEL
- **Task 8 (`task8_runnables_lcel.py`):** Demonstrates `RunnablePassthrough`, `RunnableLambda`, `RunnablePassthrough.assign()`, and runnable execution methods (`invoke` and `batch`).
- **Task 9 (`task9_lcel_rag.py`):** Implements the full LCEL RAG pipeline:
  `{"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()`
  Tested with queries spanning the text, CSV, and handbook documents.

---

## Part 5: Observations & Insights (Task 10)

### 1. Why is structured output important in production GenAI applications?
Large Language Models naturally generate unstructured free-form text, which is unpredictable and difficult to parse reliably in production software. By enforcing structured schemas (like Pydantic models or JSON specifications), downstream services, APIs, databases, and frontends can consume the model's output deterministically without breaking on unexpected syntax or missing attributes.

### 2. What are the main advantages of LCEL over traditional chains?
LCEL provides a unified, declarative syntax using the Unix-style pipe (`|`) operator. Key advantages include:
- **First-class streaming:** Every LCEL chain natively supports real-time token streaming.
- **Native asynchronous and batch support:** `invoke()`, `batch()`, and `astream()` work out of the box without extra code.
- **Optimized parallel execution:** Parallel branches run concurrently without manual multithreading.
- **Built-in observability:** LCEL components automatically attach traces to tools like LangSmith.

### 3. When should you use Parallel Chains versus Conditional Chains?
- **Parallel Chains (`RunnableParallel`):** Use when multiple independent tasks can be computed simultaneously from the same input (e.g., generating an answer, extracting key bullet points, and suggesting follow-up questions at the same time to reduce overall end-to-end latency).
- **Conditional Chains (`RunnableBranch`):** Use when the execution path depends on dynamic input characteristics (e.g., routing factual queries to a vector retriever, code queries to a Python interpreter, or greetings to a fast, lightweight conversational model without expensive database lookups).
