# Task 10: Semantic Meaning-Based Splitting (Conceptual + Demo)
# Author: Parth Dadhaniya

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 65)
print("Task 10: Semantic Meaning-Based Splitting")
print("=" * 65)

# 1. Conceptual Explanation
print("\n1. What is Semantic Chunking?")
print("-" * 55)
print("""Semantic chunking splits text based on meaning and topical shifts,
rather than arbitrary character counts or fixed punctuation boundaries.

Instead of cutting text at every 500 characters (which can cut an idea
in half), semantic chunking groups together sentences that discuss the
same concept and creates a new chunk only when the topic changes.""")

print("\n2. How do Embeddings Help Semantic Splitting?")
print("-" * 55)
print("""- Step 1: Split raw text into individual sentences.
- Step 2: Generate dense vector embeddings for each sentence (or sliding window).
- Step 3: Compute cosine similarity between consecutive sentence vectors.
- Step 4: Detect breakpoints where similarity drops below a threshold.
- Step 5: Merge sentences between breakpoints into coherent semantic chunks.""")

# 2. Interactive / Executable Demonstration
print("\n" + "=" * 65)
print("Demonstration: Semantic Chunking by Sentence Similarity")
print("=" * 65)

sample_text_sentences = [
    # Topic 1: Machine Learning & Model Training
    "Machine learning models learn patterns from training data.",
    "Deep neural network models optimize internal weights during training.",
    "These machine learning models evaluate performance on validation sets.",
    # Topic 2: Relational Databases & SQL
    "Relational database tables store structured business records safely.",
    "SQL queries retrieve structured data from database tables efficiently.",
    # Topic 3: Cloud & Container Deployment
    "Docker containers package applications into portable deployable units.",
    "Cloud Kubernetes clusters orchestrate and scale application containers."
]

print(f"Total Sentences in Corpus: {len(sample_text_sentences)}\n")

# Vectorize sentences to compute pairwise similarity between consecutive sentences
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sample_text_sentences)

similarity_threshold = 0.10
chunks = []
current_chunk = [sample_text_sentences[0]]

print("Consecutive Sentence Similarities:")
for i in range(len(sample_text_sentences) - 1):
    sim = cosine_similarity(vectors[i], vectors[i + 1])[0][0]
    print(f"Sentence {i + 1} <-> Sentence {i + 2} | Cosine Similarity: {sim:.3f}")
    if sim < similarity_threshold:
        # Topic shift detected -> split into new chunk
        chunks.append(" ".join(current_chunk))
        current_chunk = [sample_text_sentences[i + 1]]
    else:
        # Same topic -> group into current chunk
        current_chunk.append(sample_text_sentences[i + 1])

chunks.append(" ".join(current_chunk))

print(f"\nResult: Text segmented into {len(chunks)} Semantic Chunks (Threshold = {similarity_threshold}):")
for idx, chunk in enumerate(chunks, 1):
    print(f"\nChunk {idx}:")
    print(f"'{chunk}'")

print("\nConclusion:")
print("- Semantic chunking adapts chunk boundaries to content meaning.")
print("- It yields higher quality RAG retrieval results with fewer hallucinations.")
