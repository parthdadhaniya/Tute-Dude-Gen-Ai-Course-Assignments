# Task 2: One-Hot Encoding using Scikit-Learn
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# load dataset and get first 5 sentences
df = pd.read_csv("cleaned_text_dataset.csv")
sentences = df["final_clean_text"].head(5).tolist()

# binary=True makes CountVectorizer act as one-hot encoder
cv = CountVectorizer(binary=True)
encoded_matrix = cv.fit_transform(sentences)

print("Scikit-Learn CountVectorizer (binary=True):")
print("Vocabulary Size:", len(cv.vocabulary_))

# display vocabulary words
feature_names = cv.get_feature_names_out()
print("\nFirst 10 words in vocabulary:")
for word in feature_names[:10]:
    print(" ", word)

# show encoded matrix as DataFrame
df_encoded = pd.DataFrame(
    encoded_matrix.toarray(),
    columns=feature_names,
    index=[f"Sentence {i+1}" for i in range(5)]
)

print("\nEncoded Matrix Shape:", df_encoded.shape)
print("\nFirst 6 Columns:")
print(df_encoded.iloc[:, :6])
