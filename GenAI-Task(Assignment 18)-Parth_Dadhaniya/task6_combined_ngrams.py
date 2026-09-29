# Task 6: Combined N-Grams (Unigrams + Bigrams)
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

# unigrams only
cv_uni = CountVectorizer(ngram_range=(1, 1))
X_uni = cv_uni.fit_transform(corpus)

# combined unigrams and bigrams
cv_comb = CountVectorizer(ngram_range=(1, 2))
X_comb = cv_comb.fit_transform(corpus)

print("Vocabulary Size:")
print("Unigrams only (1, 1):        ", len(cv_uni.get_feature_names_out()))
print("Combined Unigram+Bigram (1, 2):", len(cv_comb.get_feature_names_out()))

# show sample bigrams that capture context
features = cv_comb.get_feature_names_out()
bigrams = [f for f in features if " " in f]
print("\nSample Contextual Bigrams:")
for b in bigrams[:6]:
    print(" ", b)

print("\nNotes on Context:")
print("- Unigrams count words in isolation without order.")
print("- Combined n-grams keep phrases like 'customer service', 'smart watch',")
print("  and 'first half' together, which helps the model understand local context.")
