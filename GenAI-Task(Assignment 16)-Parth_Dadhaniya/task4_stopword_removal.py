# Task 4: Stopword Removal
# Author: Parth Dadhaniya

import sys
import re
import pandas as pd
from nltk.corpus import stopwords

sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("customer_reviews.csv")

# helper function for clean text
def clean_text(text):
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()

df["clean_text_advanced"] = df["raw_text"].apply(clean_text)

# load stopwords
stop_words = set(stopwords.words("english"))
print("Total English stopwords in NLTK:", len(stop_words))

# remove stopwords
def remove_stopwords(text):
    words = text.split()
    clean_words = [w for w in words if w not in stop_words]
    return " ".join(clean_words)

# store in text_no_stopwords column
df["text_no_stopwords"] = df["clean_text_advanced"].apply(remove_stopwords)

print("\nStopword Removal Results (First 3 Samples):")
for i in range(3):
    before = df["clean_text_advanced"].iloc[i]
    after = df["text_no_stopwords"].iloc[i]
    print(f"\nSample {i+1} Before (Words: {len(before.split())}):")
    print(before)
    print(f"Sample {i+1} After (Words: {len(after.split())}):")
    print(after)

# save to processed_text.csv
df.to_csv("processed_text.csv", index=False)
