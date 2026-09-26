# Assignment 16: NLP Text Preprocessing Pipeline
# Author: Parth Dadhaniya

import sys
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

sys.stdout.reconfigure(encoding="utf-8")

# load dataset
df = pd.read_csv("customer_reviews.csv")

# Task 1: Load text dataset and inspect
print("Task 1 - Dataset Loaded:")
print(f"Total rows: {len(df)} | Columns: {list(df.columns)}")
print("\nFirst 3 samples:")
for i, row in df.head(3).iterrows():
    print(f"Sample {row['id']} [{row['category']}] ({len(row['raw_text'])} chars): {row['raw_text']}")

# Task 2: Basic cleaning
def basic_clean(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip()

df["clean_text_basic"] = df["raw_text"].apply(basic_clean)
print("\nTask 2 - Basic Cleaning (clean_text_basic Sample 1):")
print(df["clean_text_basic"].iloc[0])

# Task 3: Advanced noise removal
def advanced_noise_removal(text):
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()

df["clean_text_advanced"] = df["raw_text"].apply(advanced_noise_removal)
print("\nTask 3 - Advanced Noise Removal (clean_text_advanced Sample 1):")
print(df["clean_text_advanced"].iloc[0])

# Task 4: Stopword removal
stop_words = set(stopwords.words("english"))

def remove_stopwords(text):
    words = text.split()
    return " ".join([w for w in words if w not in stop_words])

df["text_no_stopwords"] = df["clean_text_advanced"].apply(remove_stopwords)
print("\nTask 4 - Stopword Removal (text_no_stopwords Sample 1):")
print(df["text_no_stopwords"].iloc[0])

# Task 6: Word & sentence tokenization
print("\nTask 6 - Tokenization for 3 Samples:")
for sample_id in [2, 7, 10]:
    row = df[df["id"] == sample_id].iloc[0]
    sentences = sent_tokenize(row["raw_text"])
    words = word_tokenize(row["raw_text"])
    print(f"\nSample {sample_id} Sentences ({len(sentences)}): {sentences}")
    print(f"Sample {sample_id} First 6 Words: {words[:6]}")

# Task 7: Porter stemming
stemmer = PorterStemmer()
sample_words = ["running", "studies", "attentive", "carefully", "happily", "leaves"]
print("\nTask 7 - Porter Stemming:")
for w in sample_words:
    print(f"  {w} -> {stemmer.stem(w)}")

# Task 8: WordNet lemmatization vs stemming
lemmatizer = WordNetLemmatizer()
compare_words = [("running", "v"), ("studies", "n"), ("leaves", "n"), ("better", "a")]
print("\nTask 8 - Stemming vs Lemmatization:")
for w, pos in compare_words:
    print(f"  {w:<10} | Stemmed: {stemmer.stem(w):<10} | Lemmatized: {lemmatizer.lemmatize(w, pos=pos)}")

# Task 9: Pipeline
def nlp_preprocess(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    tokens = text.lower().strip().split()
    cleaned = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words and len(t) > 1]
    return " ".join(cleaned)

df["final_clean_text"] = df["raw_text"].apply(nlp_preprocess)
print("\nTask 9 - NLP Pipeline Results (First 3 Samples):")
for i in range(3):
    print(f"Sample {i+1} Clean: {df['final_clean_text'].iloc[i]}")

# save final dataset
df.to_csv("cleaned_reviews_final.csv", index=False)
print("\nSaved final cleaned dataset to cleaned_reviews_final.csv")

# Task 10: Technical observations
print("\nTask 10 - Technical Observations:")
print("1. Basic cleaning leaves broken URL and HTML pieces; advanced cleaning removes whole noise patterns.")
print("2. Stemming cuts off suffixes (studies -> studi); lemmatization finds the dictionary root (studies -> study).")
print("3. Preprocessing cuts down vocabulary size and removes noise, helping NLP models learn better.")
