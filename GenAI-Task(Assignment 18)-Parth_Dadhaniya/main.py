# Assignment 18: Text Vectorization Techniques
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# load preprocessed text dataset
df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()
sentences = corpus[:5]

# Task 1: Manual One-Hot Encoding
vocab = sorted(list(set(" ".join(sentences).split())))
manual_vecs = [[1 if w in set(s.split()) else 0 for w in vocab] for s in sentences]
print("Task 1 - Manual One-Hot Encoding:")
print("5 Sentences | Vocab Size:", len(vocab))
print("Sample Vector 1:", manual_vecs[0][:8], "...")

# Task 2: Scikit-learn One-Hot Encoding
cv_binary = CountVectorizer(binary=True)
X_ohe = cv_binary.fit_transform(sentences)
print("\nTask 2 - Scikit-Learn One-Hot Encoding:")
print("Encoded Matrix Shape:", X_ohe.shape)

# Task 3: Bag of Words (BoW)
cv = CountVectorizer()
X_bow = cv.fit_transform(corpus)
print("\nTask 3 - Bag of Words:")
print(f"Total Docs: {len(corpus)} | Vocab Size: {len(cv.get_feature_names_out())} | Shape: {X_bow.shape}")

# Task 4: Word Frequency
totals = X_bow.toarray().sum(axis=0)
freq_series = pd.Series(totals, index=cv.get_feature_names_out()).sort_values(ascending=False)
print("\nTask 4 - Top 5 Frequent Words:")
print(list(freq_series.head(5).items()))

# Task 5: N-Grams
cv_uni = CountVectorizer(ngram_range=(1, 1)).fit(corpus)
cv_bi = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
cv_tri = CountVectorizer(ngram_range=(3, 3)).fit(corpus)
print("\nTask 5 - N-Gram Vocab Sizes:")
print("Unigrams:", len(cv_uni.get_feature_names_out()), "| Bigrams:", len(cv_bi.get_feature_names_out()), "| Trigrams:", len(cv_tri.get_feature_names_out()))

# Task 6: Combined N-Grams
cv_comb = CountVectorizer(ngram_range=(1, 2)).fit(corpus)
print("\nTask 6 - Combined (1, 2) Vocab Size:", len(cv_comb.get_feature_names_out()))

# Task 7: TF-IDF
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)
print("\nTask 7 - TF-IDF Matrix Shape:", X_tfidf.shape)

# Task 8: BoW vs TF-IDF
avg_tfidf = pd.Series(X_tfidf.toarray().mean(axis=0), index=tfidf.get_feature_names_out()).sort_values(ascending=False)
print("\nTask 8 - Top TF-IDF Weighted Words:")
print(list(avg_tfidf.head(5).round(3).items()))

# Task 9: Parameter Exploration
print("\nTask 9 - Parameter Exploration:")
for params, label in [
    ({"max_features": 30}, "max_features=30"),
    ({"min_df": 2}, "min_df=2"),
    ({"max_df": 0.5}, "max_df=0.5")
]:
    v = TfidfVectorizer(**params).fit(corpus)
    print(f"  {label:<15} -> Vocab: {len(v.get_feature_names_out())}")

# Task 10: Conceptual Questions
print("\nTask 10 - Conceptual Questions Summary:")
print("1. One-Hot vs BoW: One-Hot is binary presence (0 or 1); BoW stores word count frequency.")
print("2. N-grams: Word combinations rapidly expand vocabulary size and dimensionality.")
print("3. TF-IDF: Down-weights common words and highlights unique keywords.")
print("4. Limitations: Count-based methods lose word order and lack semantic similarity.")
