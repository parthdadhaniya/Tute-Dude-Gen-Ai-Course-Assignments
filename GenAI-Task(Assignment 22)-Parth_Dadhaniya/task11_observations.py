# Task 11: Observations & Insights
# Parth Dadhaniya

print("Task 11: Observations & Insights\n")

print("1. Importance of Embeddings in GenAI:")
print("- Converts words and sentences into numbers (vectors) that computers can compare mathematically.")
print("- Captures semantic meaning so that synonyms and related concepts match even if different words are used.")
print("- Enables calculating cosine similarity between a user question and document chunks.\n")

print("2. Why Vector Databases are Required:")
print("- Regular SQL databases are made for exact matching (LIKE, =), which cannot find similar meanings.")
print("- Vector databases use Approximate Nearest Neighbor (ANN) search to search through thousands or millions")
print("  of vectors in just a few milliseconds.")
print("- They allow combining vector similarity with metadata filters (like filtering by date or department).\n")

print("3. How This Pipeline Enables RAG Systems:")
print("- Ingestion: Load company documents and split them into chunks.")
print("- Indexing: Convert chunks to embeddings and store in a vector database.")
print("- Retrieval: When a user asks a question, find the most relevant chunks using similarity search.")
print("- Generation: Pass those relevant chunks to the LLM as context so it gives accurate, factual answers.")
