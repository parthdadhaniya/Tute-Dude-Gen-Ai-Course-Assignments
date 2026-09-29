# Task 1: Understanding Word Embeddings (Conceptual)
# Author: Parth Dadhaniya

print("1. What are word embeddings?")
print("- Word embeddings are dense numerical vectors that represent words in a continuous space.")
print("- Words with similar meanings end up close to each other in this vector space.")
print("- Unlike one-hot vectors which are huge and sparse, embeddings use small dense dimensions like 50, 100, or 300.")

print("\n2. Why One-Hot Encoding and BoW fail to capture semantics:")
print("- They treat every word as completely independent and perpendicular to other words.")
print("- The dot product between any two distinct one-hot vectors is always 0, so 'king' and 'queen' have zero similarity.")
print("- They ignore word order, context, and meaning.")
print("- Vocabulary size makes vectors huge and mostly filled with zeros.")

print("\n3. How word embeddings solve these problems:")
print("- They use low-dimensional dense vectors (e.g. 100 numbers instead of 10,000 zeros).")
print("- Words used in similar contexts share similar vector coordinates, so cosine similarity is high.")
print("- They capture relationships with vector math, like: king - man + woman = queen.")
print("- Models generalize much better to new sentences having synonyms.")
