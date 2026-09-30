# Assignment 34: Text Summarization using LangChain

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I built multiple text summarization pipelines using LangChain to understand how modern Generative AI systems summarize documents of varying lengths and complexities. Large language models face hard context window boundaries and quadratic attention costs, requiring distinct summarization strategies:

1. **Prompt-Based Summarization:** Direct prompt engineering using LangChain's `PromptTemplate` for rapid single-text summaries with custom variations (short paragraph vs key bullet points).
2. **Stuff Summarization Chain:** Concatenating entire documents into a single prompt (`chain_type="stuff"`), ideal for short documents that fit well within model context limits.
3. **Map-Reduce Summarization Chain:** Dividing documents into chunks, independently summarizing each chunk in parallel (Map), and synthesizing all intermediate summaries into an overarching executive summary (Reduce).
4. **Refine Summarization Chain:** Sequentially processing chunks where each step receives the running summary and the new text chunk to progressively refine the summary, preserving narrative continuity.
5. **Unified Document Summarizer Mini Project:** A reusable function `summarize_document(text_or_docs, method=...)` that dynamically toggles between `prompt`, `stuff`, `map_reduce`, and `refine`.

---

## File Structure

```text
GenAI-Task(Assignment 34)-Parth_Dadhaniya/
├── data/
│   └── enterprise_ai_overview.txt    # 4,500+ character document on AI in enterprise
├── config.py                         # LLM configuration (ChatGroq / ChatOpenAI / offline student model)
├── summarize_chains.py               # Stuff, Map-Reduce & Refine chain implementations
├── part1_prompt_summarization.py     # Tasks 1, 2 & 3: Document stats, basic summary & variations
├── part2_stuff_chain.py              # Tasks 4, 5 & 6: Stuff chain implementation & comparisons
├── part3_map_reduce_chain.py         # Tasks 7, 8 & 9: Map-Reduce chain & intermediate chunk analysis
├── part4_refine_chain.py             # Tasks 10, 11 & 12: Refine chain & 4-method comparison matrix
├── part5_document_summarizer.py      # Task 13: Unified reusable summarize_document() mini project
├── task14_observations.py           # Task 14: Conceptual observations, trade-offs & use cases
├── main.py                           # Master runner executing all parts sequentially
├── assignment34.ipynb                # Interactive Jupyter Notebook
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## Task Details

### Part 1: Basic Text Summarization using PromptTemplate (Tasks 1, 2 & 3)
- Loaded `enterprise_ai_overview.txt` (4,564 characters, 592 words across 5 sections).
- Built a LangChain `PromptTemplate` and executed direct prompt-based summarization (`prompt | llm`).
- Tested two prompt variations:
  - **Variation A:** Short executive paragraph (5–6 lines).
  - **Variation B:** Concise bullet-point takeaways.

### Part 2: Stuff Summarization Chain (Tasks 4, 5 & 6)
- Answered core concepts: What stuffing is, when it works, and why context window limits ("Lost in the Middle") cause it to fail on long documents.
- Implemented `load_summarize_chain(llm, chain_type="stuff")` accepting LangChain `Document` objects.
- Compared prompt-only vs stuff chain: stuff chains integrate seamlessly into document loaders and vector stores.

### Part 3: Map-Reduce Summarization Chain (Tasks 7, 8 & 9)
- Explained why massive documents require chunking and two-stage processing.
- Split the document into 5 chunks (1,200 chars with 150-char overlap).
- Implemented `load_summarize_chain(llm, chain_type="map_reduce")`.
- Inspected and printed intermediate summaries for each chunk (Map step) and observed the final consolidated executive summary (Reduce step).

### Part 4: Refine Summarization Chain (Tasks 10, 11 & 12)
- Explained the iterative refine loop ($c_1 \to c_2 \to \dots \to c_n$).
- Highlighted key differences between Map-Reduce (parallel, executive view) and Refine (sequential, deep narrative coherence).
- Implemented `load_summarize_chain(llm, chain_type="refine")`.
- Produced a 4-way evaluation matrix comparing Quality, Coherence, Scalability, and Latency.

### Part 5: Mini Project - Document Summarizer (Task 13)
- Created the unified function:
  ```python
  def summarize_document(text_or_docs, method="map_reduce"):
      ...
  ```
- Supports `'prompt'`, `'stuff'`, `'map_reduce'`, and `'refine'`.
- Normalizes both raw strings and lists of `Document` objects automatically.

### Task 14: Observations & Conceptual Insights
- **Best Strategy for Long Documents:** Map-Reduce for massive scale and parallel processing; Refine for narrative depth and legal/medical continuity.
- **Speed vs Quality Trade-offs:** Stuff is fastest (1 call); Map-Reduce is fast with parallel workers; Refine is slowest due to sequential dependencies but delivers the highest narrative flow.
- **Real-World Use Cases:**
  - Prompt: Quick emails and customer support tickets.
  - Stuff: 1–3 page memos and short news articles.
  - Map-Reduce: Earnings call transcripts and 10-K financial filings.
  - Refine: Complex legal contracts, medical charts, and research literature.

---

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run All Tasks:**
   ```bash
   python main.py
   ```

3. **Run Individual Tasks:**
   ```bash
   python part1_prompt_summarization.py
   python part2_stuff_chain.py
   python part3_map_reduce_chain.py
   python part4_refine_chain.py
   python part5_document_summarizer.py
   python task14_observations.py
   ```

4. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook assignment34.ipynb
   ```
