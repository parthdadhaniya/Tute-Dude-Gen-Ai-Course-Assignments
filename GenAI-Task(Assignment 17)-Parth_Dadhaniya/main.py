# Assignment 17: Text Cleaning, Preprocessing & NLP Pipeline
# Author: Parth Dadhaniya

import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# load dataset
df = pd.read_csv("raw_text_data.csv")

# Task 1: Understanding Raw Text Data
print("Task 1 - Dataset Loaded:")
print(f"Total samples: {len(df)} | Columns: {list(df.columns)}")
print("\nFirst 3 samples:")
for i, row in df.head(3).iterrows():
    print(f"Sample {row['id']} [{row['category']}] ({len(row['raw_text'])} chars): {row['raw_text']}")

# Task 2: Basic Text Cleaning
def basic_clean(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip()

df["clean_text_basic"] = df["raw_text"].apply(basic_clean)
print("\nTask 2 - Basic Cleaning (Sample 1):")
print(df["clean_text_basic"].iloc[0])

# Task 3: Removing Noise
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
print("\nTask 3 - Advanced Noise Removal (Sample 1):")
print(df["clean_text_advanced"].iloc[0])

# Task 4: Handling Stopwords
stop_words = set(stopwords.words("english"))

def remove_stopwords(text):
    words = text.split()
    return " ".join([w for w in words if w not in stop_words])

df["text_no_stopwords"] = df["clean_text_advanced"].apply(remove_stopwords)
print("\nTask 4 - Stopword Removal (Sample 1):")
print(df["text_no_stopwords"].iloc[0])

# Task 5: Handling Repeated Characters & Slang
slang_dict = {
    "u": "you",
    "gr8": "great",
    "pls": "please",
    "thx": "thanks",
    "omg": "oh my god",
    "bcoz": "because",
    "idk": "i do not know"
}

def clean_slang_and_repeats(text):
    text = re.sub(r"(.)\1{2,}", r"\1", text)
    words = text.split()
    return " ".join([slang_dict.get(w.lower(), w) for w in words])

sample_slang = "omg this phone battery is terribleeee... pls fix it u guys promised gr8 performance"
print("\nTask 5 - Slang & Repeated Characters Normalization:")
print("Original:  ", sample_slang)
print("Normalized:", clean_slang_and_repeats(sample_slang))

# Task 6: Word & Sentence Tokenization
print("\nTask 6 - Tokenization for 3 Samples:")
for sample_id in [2, 4, 14]:
    row = df[df["id"] == sample_id].iloc[0]
    sentences = sent_tokenize(row["raw_text"])
    words = word_tokenize(row["raw_text"])
    print(f"\nSample {sample_id} Sentences ({len(sentences)}): {sentences}")
    print(f"Sample {sample_id} First 6 Words: {words[:6]}")

# Task 7: Stemming
stemmer = PorterStemmer()
sample_words = ["running", "watched", "studies", "leaves", "caring", "carefully"]
print("\nTask 7 - Porter Stemming:")
for w in sample_words:
    print(f"  {w:<10} -> {stemmer.stem(w)}")

# Task 8: Lemmatization vs Stemming
lemmatizer = WordNetLemmatizer()
compare_pairs = [("running", "v"), ("studies", "n"), ("leaves", "n"), ("better", "a")]
print("\nTask 8 - Stemming vs Lemmatization:")
for w, pos in compare_pairs:
    print(f"  {w:<10} | Stemmed: {stemmer.stem(w):<10} | Lemmatized: {lemmatizer.lemmatize(w, pos=pos)}")

# Task 9: Final NLP Pipeline Creation
def nlp_preprocess(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"(.)\1{2,}", r"\1", text)
    text = text.lower().strip()
    words = [slang_dict.get(w, w) for w in text.split()]
    text = " ".join(words)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    clean_tokens = [lemmatizer.lemmatize(t) for t in text.split() if t not in stop_words and len(t) > 1]
    return " ".join(clean_tokens)

df["final_clean_text"] = df["raw_text"].apply(nlp_preprocess)
print("\nTask 9 - Final NLP Pipeline Applied (First 3 Samples):")
for i in range(3):
    print(f"Sample {i+1} Clean: {df['final_clean_text'].iloc[i]}")

# save final dataset
df.to_csv("cleaned_text_final.csv", index=False)
print("\nSaved output to cleaned_text_final.csv")

# Task 10: Observations & Insights
print("\nTask 10 - Observations & Insights:")
print("1. Basic vs Advanced: Basic cleaning leaves broken URL and HTML pieces; advanced cleaning removes whole noise patterns.")
print("2. Stemming vs Lemmatization: Stemming strips suffixes quickly but creates non-words ('studi'); lemmatization creates valid dictionary roots ('study').")
print("3. Preprocessing Importance: Reduces noise, shrinks vocabulary dimension, and enhances downstream NLP generalization.")
