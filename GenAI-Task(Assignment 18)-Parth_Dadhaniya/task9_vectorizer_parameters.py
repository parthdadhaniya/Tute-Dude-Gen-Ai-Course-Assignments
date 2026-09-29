# Task 9: Vectorizer Parameter Exploration
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("cleaned_text_dataset.csv")
corpus = df["final_clean_text"].tolist()

# baseline: default parameters
vec_base = TfidfVectorizer().fit(corpus)
print("Baseline vocabulary size:   ", len(vec_base.get_feature_names_out()))

# max_features: limits vocabulary to top N words
vec_max30 = TfidfVectorizer(max_features=30).fit(corpus)
print("With max_features = 30:     ", len(vec_max30.get_feature_names_out()))

# min_df: ignores words that appear in less than 2 documents
vec_min2 = TfidfVectorizer(min_df=2).fit(corpus)
print("With min_df = 2 (in >=2 docs):", len(vec_min2.get_feature_names_out()))

# max_df: ignores words that appear in more than 50% of documents
vec_maxdf = TfidfVectorizer(max_df=0.5).fit(corpus)
print("With max_df = 0.5 (in <=50%):", len(vec_maxdf.get_feature_names_out()))

print("\nObservations:")
print("- max_features controls the maximum size of the feature matrix.")
print("- min_df removes rare words or typos that only appear once.")
print("- max_df removes words that appear too often across all texts.")
