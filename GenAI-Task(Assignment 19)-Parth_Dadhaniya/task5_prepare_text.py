# Task 5: Prepare Text for Word2Vec
# Author: Parth Dadhaniya

import os
import pandas as pd

# locate dataset
csv_path = "cleaned_text_corpus.csv"
if not os.path.exists(csv_path):
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_text_corpus.csv")

# load cleaned dataset
df = pd.read_csv(csv_path)

# tokenize each sentence into words (list of lists)
sentences = []
for text in df["clean_text"]:
    words = str(text).strip().split()
    if words:
        sentences.append(words)

print("Total sentences loaded:", len(sentences))

total_words = sum(len(s) for s in sentences)
unique_words = len(set(w for s in sentences for w in s))
print("Total word tokens:     ", total_words)
print("Unique vocabulary words:", unique_words)

print("\nSample tokenized sentences (list of lists):")
for i, s in enumerate(sentences[:4], 1):
    print(f"Sentence {i}: {s}")
