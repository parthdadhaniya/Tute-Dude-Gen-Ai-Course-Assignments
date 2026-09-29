# Task 11: Conceptual Questions & Observations
# Parth Dadhaniya

print("--- Task 11: Conceptual Questions & Observations ---\n")

print("1. Why is RAG preferred over fine-tuning for factual knowledge?")
print("Answer:")
print("Fine-tuning updates model weights, which is slow, expensive, and still hallucinates.")
print("RAG keeps the model frozen and fetches fresh facts from a vector store at query time.")
print("This makes RAG cheaper, easy to update, and verifiable with source citations.\n")

print("2. How does chunk size affect retrieval quality?")
print("Answer:")
print("- Too small chunks (<100 chars): Splits sentences in half and loses meaning.")
print("- Too large chunks (>1500 chars): Packs too many topics together, diluting similarity and wasting context tokens.")
print("- Best size: Around 250-500 characters with 10-15% overlap to keep complete thoughts intact.\n")

print("3. Why use MMR instead of simple similarity search?")
print("Answer:")
print("Simple similarity search often retrieves 3 or 4 chunks that say almost the exact same thing.")
print("MMR balances relevance with diversity by penalizing near-duplicate chunks, giving the LLM a broader view.\n")

print("4. What are the limitations of YouTube transcript-based RAG?")
print("Answer:")
print("- Loses visual information like diagrams, slides, and code shown on screen.")
print("- Auto-generated subtitles often misspell technical terms and have no punctuation.")
print("- Does not identify who is speaking (no speaker diarization).")
print("- YouTube can block or throttle automated requests, so local backups are needed.")
