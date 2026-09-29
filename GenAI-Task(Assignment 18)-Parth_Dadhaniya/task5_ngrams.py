# Task 5: Unigrams, Bigrams & Trigrams
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

# unigrams
cv_uni = CountVectorizer(ngram_range=(1, 1))
X_uni = cv_uni.fit_transform(corpus)

# bigrams
cv_bi = CountVectorizer(ngram_range=(2, 2))
X_bi = cv_bi.fit_transform(corpus)

# trigrams
cv_tri = CountVectorizer(ngram_range=(3, 3))
X_tri = cv_tri.fit_transform(corpus)

print("Vocabulary Size Comparison:")
print("Unigrams (1, 1):", len(cv_uni.get_feature_names_out()))
print("Bigrams  (2, 2):", len(cv_bi.get_feature_names_out()))
print("Trigrams (3, 3):", len(cv_tri.get_feature_names_out()))

# display sample features
print("\nSample Bigrams (Word Pairs):")
print(list(cv_bi.get_feature_names_out()[:6]))

print("\nSample Trigrams (3-Word Phrases):")
print(list(cv_tri.get_feature_names_out()[:6]))

# vector comparison for Document 1
print("\nDocument 1 Non-Zero Elements:")
print("Unigram non-zero features:", X_uni[0].nnz)
print("Bigram non-zero features: ", X_bi[0].nnz)
print("Trigram non-zero features:", X_tri[0].nnz)
