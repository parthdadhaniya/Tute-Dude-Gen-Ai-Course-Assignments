# Task 6: Word and Sentence Tokenization
# Author: Parth Dadhaniya

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

df = pd.read_csv("raw_text_data.csv")

# select 3 samples with multiple sentences
sample_ids = [2, 4, 14]
samples = df[df["id"].isin(sample_ids)]

print("Tokenization for 3 Samples:")

for i, row in samples.iterrows():
    text = row["raw_text"]
    
    # sentence tokenization
    sentences = sent_tokenize(text)
    
    # word tokenization
    words = word_tokenize(text)
    
    print(f"\nSample {row['id']} [{row['category']}]:")
    print("Raw text:", text)
    print(f"Sentences ({len(sentences)}):")
    for idx, s in enumerate(sentences, 1):
        print(f"  {idx}. {s}")
    print(f"Words ({len(words)} tokens):")
    print(" ", words[:10], "...")

print("\nNotes:")
print("- Sentence tokenization splits text into individual sentences based on punctuation.")
print("- Word tokenization breaks sentences into words and punctuation marks.")
