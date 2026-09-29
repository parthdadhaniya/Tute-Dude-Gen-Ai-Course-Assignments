# Task 2: Text Preprocessing for Recommendation
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

df = pd.read_csv("movies.csv")

# 1. handle missing values
df["genres"] = df["genres"].fillna("")
df["overview"] = df["overview"].fillna("")

# combine genres and overview
df["tags"] = df["genres"] + " " + df["overview"]

# 2. convert to lowercase and remove punctuation
df["clean_text"] = df["tags"].str.lower()
df["clean_text"] = df["clean_text"].str.replace(r"[^\w\s]", " ", regex=True)

# 3. remove stopwords
stop_words = set(ENGLISH_STOP_WORDS)
df["clean_text"] = df["clean_text"].apply(
    lambda x: " ".join([word for word in x.split() if word not in stop_words])
)

print("Preprocessed Total Rows:", len(df))
print("\nSample Original Text (Movie 1):")
print(df["tags"].iloc[0][:100], "...")

print("\nSample Cleaned Text (Movie 1):")
print(df["clean_text"].iloc[0][:100], "...")

# save cleaned dataset
df.to_csv("cleaned_movies.csv", index=False)
print("\nSaved cleaned dataset to cleaned_movies.csv")
