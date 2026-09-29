# Task 3: Vectorization using TF-IDF
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("cleaned_movies.csv")

# TF-IDF vectorization with unigrams and bigrams
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df["clean_text"])

print("TF-IDF Vectorization Completed!")
print("Number of Movies:   ", tfidf_matrix.shape[0])
print("Vocabulary Features:", tfidf_matrix.shape[1])
print("Matrix Shape:       ", tfidf_matrix.shape)

feature_names = tfidf.get_feature_names_out()
print("\nFirst 10 Features:")
print(list(feature_names[:10]))
