# Task 8: BoW vs TF-IDF Comparison
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

# 1. BoW
cv = CountVectorizer()
bow_matrix = cv.fit_transform(corpus)

# 2. TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(corpus)

feature_names = cv.get_feature_names_out()
avg_bow = bow_matrix.toarray().mean(axis=0)
avg_tfidf = tfidf_matrix.toarray().mean(axis=0)

comp_df = pd.DataFrame({
    "word": feature_names,
    "avg_bow": avg_bow,
    "avg_tfidf": avg_tfidf
})

print("Words with Highest Average TF-IDF Scores:")
top_words = comp_df.sort_values(by="avg_tfidf", ascending=False).head(5)
for word, bow_val, tfidf_val in top_words.values:
    print(f"  {word:<12} -> BoW: {round(bow_val, 2)} | TF-IDF: {round(tfidf_val, 4)}")

print("\nWords with Lowest Non-Zero Average TF-IDF Scores:")
low_words = comp_df[comp_df["avg_tfidf"] > 0].sort_values(by="avg_tfidf").head(5)
for word, bow_val, tfidf_val in low_words.values:
    print(f"  {word:<12} -> BoW: {round(bow_val, 2)} | TF-IDF: {round(tfidf_val, 4)}")

print("\nWhy TF-IDF Down-Weights Common Words:")
print("- In BoW, a word that appears 10 times in every document gets a huge count.")
print("- TF-IDF multiplies Term Frequency (TF) by Inverse Document Frequency (IDF).")
print("- If a word is everywhere, IDF becomes near 0, which reduces its score.")
print("- This allows unique, important words to stand out.")
