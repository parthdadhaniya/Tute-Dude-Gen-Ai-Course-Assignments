# Assignment 21: LangChain Document Loaders & Text Splitters
**Student:** Parth Dadhaniya  
**Course:** GenAI Course  
**Role:** Generative AI Engineer  
**Scenario:** Personal Knowledge Assistant (Ingestion & Chunking Layer)

---

## 1. Project Overview
Before building Retrieval-Augmented Generation (RAG) systems or autonomous agents, unstructured and semi-structured enterprise data must be reliably ingested and divided into coherent chunks. Passing raw, multi-page documents directly into Large Language Models (LLMs) leads to context window overflows, attention degradation ("lost in the middle"), high latency, and excessive API costs.

In this assignment, we implement the complete ingestion and chunking layer using LangChain:
- **Document Loaders:** Ingesting plain text (`.txt`), tabular data (`.csv`), multi-page PDFs (`.pdf`), local directory trees (`DirectoryLoader`), and live web pages (`WebBaseLoader`).
- **Text Splitters:** Evaluating length-based splitting (`CharacterTextSplitter`), structure-preserving recursive splitting (`RecursiveCharacterTextSplitter`), document outline splitting (`MarkdownHeaderTextSplitter`), and semantic meaning-based splitting.
- **Unified Pipeline:** A single ingestion function `load_and_split_documents(path_or_url)` capable of processing any local file, directory, or public URL.
- **Architectural Observations:** Documenting loader trade-offs, optimal splitter strategies, and the critical role of chunk overlap.

---

## 2. Directory Structure
```
GenAI-Task(Assignment 21)-Parth_Dadhaniya/
│
├── data/
│   ├── notes.txt                  # Company notes on architecture & AI policy
│   ├── data.csv                   # Tabular employee and project records
│   ├── handbook.md                # Structured markdown handbook with headers
│   └── sample.pdf                 # Multi-page reference PDF document
│
├── task1_text_loader.py           # Task 1: TextLoader for .txt files
├── task2_csv_loader.py            # Task 2: CSVLoader for tabular .csv files
├── task3_pdf_loader.py            # Task 3: PyPDFLoader for .pdf documents
├── task4_directory_loader.py      # Task 4: DirectoryLoader for multi-format folders
├── task5_web_loader.py            # Task 5: WebBaseLoader for live webpages
├── task6_why_splitting.py         # Task 6: Conceptual rationale for chunking
├── task7_character_splitter.py    # Task 7: CharacterTextSplitter (length-based)
├── task8_recursive_splitter.py    # Task 8: RecursiveCharacterTextSplitter
├── task9_structure_splitter.py    # Task 9: Structure-aware splitting (Markdown & PDF)
├── task10_semantic_splitter.py    # Task 10: Semantic meaning-based splitting & demo
├── task11_pipeline.py             # Task 11: Unified load_and_split_documents pipeline
├── task12_observations.py         # Task 12: Core observations and answers
│
├── main.py                        # Master sequential runner executing all tasks
├── assignment21.ipynb             # Interactive Jupyter Notebook
├── requirements.txt               # Dependencies (langchain, pypdf, bs4, etc.)
└── README.md                      # Assignment documentation
```

---

## 3. Implementation Details

### Part 1 — Document Loaders in LangChain
1. **Text Loader (`task1_text_loader.py`):**
   - Ingests `data/notes.txt` into a LangChain `Document` object.
   - Retains source metadata: `{'source': 'data/notes.txt'}`.
2. **CSV Loader (`task2_csv_loader.py`):**
   - Converts each row of `data/data.csv` into an isolated `Document`.
   - Automatically formats columns into human-readable key-value pairs (e.g., `id: 101`, `name: Aarav Sharma`, `role: Backend Engineer`).
3. **PDF Loader (`task3_pdf_loader.py`):**
   - Uses `PyPDFLoader` to parse multi-page PDFs page by page.
   - Retains page numbers in metadata (`page: 0`, `page: 1`) essential for exact source citations.
4. **Directory Loader (`task4_directory_loader.py`):**
   - Scans the `data/` directory and applies format-specific loaders (`TextLoader`, `CSVLoader`, `PyPDFLoader`) via glob patterns.
   - Verified that all 8 documents/rows/pages are indexed properly.
5. **WebBase Loader (`task5_web_loader.py`):**
   - Ingests live documentation and HTML pages from Wikipedia via `BeautifulSoup`.
   - Extracts clean textual content while retaining page title and source URL in metadata.

---

### Part 2 — Text Splitters in LangChain
1. **Why Splitting is Required (`task6_why_splitting.py`):**
   - Large documents cannot be passed directly due to context window limits, token latency, API costs, and retrieval dilution.
   - Chunking enables fine-grained semantic retrieval, high intra-chunk coherence, and zero irrelevant noise.
2. **Length-Based Splitting (`task7_character_splitter.py`):**
   - Configured `chunk_size=250` and `chunk_overlap=40` with `CharacterTextSplitter`.
   - Observed that if a single block between separators exceeds `chunk_size`, the splitter cannot break it further without custom regex.
3. **Structure-Based Splitting (`task8_recursive_splitter.py`):**
   - Evaluated `RecursiveCharacterTextSplitter` with separator hierarchy `["\n\n", "\n", " ", ""]`.
   - Keeps paragraphs intact first, falls back to sentences, then words. Completely eliminates mid-word slicing and produces well-bounded passages.
4. **Document Structure-Based Splitting (`task9_structure_splitter.py`):**
   - Evaluated `MarkdownHeaderTextSplitter` on `data/handbook.md`.
   - Automatically attached section hierarchies (`Header 1`, `Header 2`, `Header 3`) into chunk metadata.
   - Evaluated page-level preservation with `PyPDFLoader`.
5. **Semantic Meaning-Based Splitting (`task10_semantic_splitter.py`):**
   - Analyzed how sentence embeddings and cosine similarity curves identify semantic breakpoints/topic shifts.
   - Demonstrated semantic sentence clustering that groups topically related sentences together and splits when similarity dips below threshold.

---

### Part 3 — Mini Integration Task & Insights
1. **Unified Pipeline (`task11_pipeline.py`):**
   - Implemented `load_and_split_documents(path_or_url, chunk_size=400, chunk_overlap=50)`.
   - Automatically routes web URLs to `WebBaseLoader` and directory/file paths to format-specific loaders, then splits chunks recursively.
   - Successfully processed local `data/` folder (15 chunks) and web documentation (792 chunks).
2. **Observations & Insights (`task12_observations.py`):**
   - **Loader Mapping:** Plain text (`TextLoader`), tabular data (`CSVLoader`), PDFs (`PyPDFLoader`), directories (`DirectoryLoader`), web pages (`WebBaseLoader`).
   - **Best Splitter Selection:**
     - *Small text:* `CharacterTextSplitter` or single-block preservation.
     - *Large PDFs:* `PyPDFLoader` (page-aware) + `RecursiveCharacterTextSplitter`.
     - *Web data:* `RecursiveCharacterTextSplitter` or `MarkdownHeaderTextSplitter` / `HTMLHeaderTextSplitter`.
   - **Importance of Chunk Overlap:** Preserves contextual continuity across chunk boundaries, prevents lost facts in RAG searches, and mitigates LLM hallucinations.

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
python task1_text_loader.py
python task2_csv_loader.py
python task3_pdf_loader.py
python task4_directory_loader.py
python task5_web_loader.py
python task6_why_splitting.py
python task7_character_splitter.py
python task8_recursive_splitter.py
python task9_structure_splitter.py
python task10_semantic_splitter.py
python task11_pipeline.py
python task12_observations.py
```
