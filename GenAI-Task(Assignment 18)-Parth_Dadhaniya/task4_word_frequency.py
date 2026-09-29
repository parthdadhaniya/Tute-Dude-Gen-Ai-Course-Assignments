# Task 4: Understanding Word Frequency in BoW
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

cv = CountVectorizer()
bow_matrix = cv.fit_transform(corpus)
feature_names = cv.get_feature_names_out()

# sum counts for each word across all documents
totals = bow_matrix.toarray().sum(axis=0)

freq_series = pd.Series(totals, index=feature_names).sort_values(ascending=False)

print("Top 10 Most Frequent Words:")
for word, count in freq_series.head(10).items():
    print(f"  {word:<12} -> {count} times")

least_frequent = freq_series[freq_series == 1]
print(f"\nLeast Frequent Words (Count = 1): {len(least_frequent)} words")
print("Sample least frequent words:", list(least_frequent.head(6).index))

print("\nHow BoW Captures Word Frequency:")
print("- One-Hot Encoding only checks if a word exists (0 or 1).")
print("- Bag of Words counts the actual number of times a word occurs in each sentence.")
print("- Words with higher counts get larger numbers in the vector.")
