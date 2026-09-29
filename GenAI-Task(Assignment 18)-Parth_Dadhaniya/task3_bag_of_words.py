# Task 3: Bag of Words (BoW) Representation
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# load full corpus of 25 documents
df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

# standard CountVectorizer for Bag of Words
cv = CountVectorizer()
bow_matrix = cv.fit_transform(corpus)
feature_names = cv.get_feature_names_out()

print("Bag of Words Representation:")
print("Total Documents:     ", len(corpus))
print("Total Vocabulary Size:", len(feature_names))
print("BoW Matrix Shape:    ", bow_matrix.shape)

print("\nSample Vocabulary Words:")
print(list(feature_names[:10]))

# show non-zero word counts for Document 1
print("\nDocument 1 Word Counts:")
print("Text:", corpus[0])
doc1_counts = bow_matrix[0].toarray()[0]
for word, count in zip(feature_names, doc1_counts):
    if count > 0:
        print(f"  {word} : {count}")
