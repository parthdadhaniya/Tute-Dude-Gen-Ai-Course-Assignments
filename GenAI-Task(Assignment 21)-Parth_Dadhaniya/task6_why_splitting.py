# Task 6: Why Text Splitting is Required (Conceptual)
# Author: Parth Dadhaniya

print("=" * 60)
print("Task 6: Why Text Splitting is Required in GenAI Systems")
print("=" * 60)

print("\n1. Why large documents cannot be directly passed to LLMs?")
print("-" * 55)
print("""- Context Window Limitations:
  Every LLM has a finite context window limit (e.g. 8k, 32k, or 128k tokens).
  Entire books, multi-page PDFs, or codebase repositories easily exceed these limits.

- Attention Degradation ('Lost in the Middle'):
  LLMs struggle to retrieve specific facts buried deep in massive contexts.
  Research shows LLMs attend best to information at the very beginning or end of prompts.

- Latency and API Cost:
  Sending hundreds of pages in every LLM query dramatically increases inference
  time and API costs ($ per token).""")

print("\n2. What problems does chunking solve in GenAI systems?")
print("-" * 55)
print("""- Fine-Grained Retrieval Precision:
  Instead of indexing an entire 100-page manual, chunking creates focused passages
  (e.g., 300-500 chars). The vector database can return only the 2-3 chunks directly
  relevant to the user query.

- Preserving Semantic Coherence:
  Breaking text into logical paragraphs or thoughts ensures each vector embedding
  accurately represents a single topic or fact.

- Eliminating Noise:
  Relevant chunks provide the LLM with concise, focused context, preventing
  hallucinations caused by irrelevant or conflicting background text.

- Scalability:
  Allows enterprise systems to index gigabytes of documents efficiently and
  perform millisecond similarity searches.""")
