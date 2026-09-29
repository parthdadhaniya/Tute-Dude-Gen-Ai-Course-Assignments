# Task 4: Similarity Computation (Cosine Similarity)
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cleaned_movies.csv")

# vectorize
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df["clean_text"])

# compute similarity matrix
similarity = cosine_similarity(tfidf_matrix)

print("Cosine Similarity Matrix Shape:", similarity.shape)
print("Diagonal self-similarity (first 5):", similarity.diagonal()[:5])

print("\nWhy Cosine Similarity is used:")
print("1. It measures the angle between vectors rather than Euclidean length.")
print("2. A long movie description and a short movie description of the same genre")
print("   will still have high cosine similarity because length does not penalize them.")
print("3. Values range between 0 and 1, which makes sorting and ranking recommendations simple.")
