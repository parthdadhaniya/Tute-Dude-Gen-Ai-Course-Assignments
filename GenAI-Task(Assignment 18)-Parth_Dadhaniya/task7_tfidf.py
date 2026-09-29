# Task 7: TF-IDF Vectorization
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)
feature_names = tfidf.get_feature_names_out()

print("TF-IDF Vectorization:")
print("Total Documents:    ", len(corpus))
print("Vocabulary Size:    ", len(feature_names))
print("TF-IDF Matrix Shape:", X_tfidf.shape)

print("\nSample Vocabulary:")
print(list(feature_names[:10]))

# sample TF-IDF values for Document 1
print("\nDocument 1 TF-IDF Weights:")
print("Text:", corpus[0])
doc1_tfidf = X_tfidf[0].toarray()[0]
for word, score in zip(feature_names, doc1_tfidf):
    if score > 0:
        print(f"  {word} : {round(score, 4)}")
