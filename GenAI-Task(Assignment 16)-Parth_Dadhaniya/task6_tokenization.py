# Task 6: Word and Sentence Tokenization
# Author: Parth Dadhaniya

import sys
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("customer_reviews.csv")

# select 3 samples with multiple sentences
sample_ids = [2, 7, 10]
samples = df[df["id"].isin(sample_ids)]

print("Word and Sentence Tokenization on 3 Samples:")
for i, row in samples.iterrows():
    text = row["raw_text"]
    
    # 1. sentence tokenization
    sentences = sent_tokenize(text)
    
    # 2. word tokenization
    words = word_tokenize(text)
    
    print(f"\n--- Sample {row['id']} [{row['category']}] ---")
    print("Raw Text:", text)
    
    print(f"\nSentences ({len(sentences)}):")
    for s_idx, sentence in enumerate(sentences, 1):
        print(f"  Sentence {s_idx}: {sentence}")
        
    print(f"\nWords ({len(words)} tokens):")
    print(" ", words[:12], "...")

print("\nNotes:")
print("- Sentence tokenization splits text based on sentence punctuation like '.', '!', '?'.")
print("- Word tokenization breaks sentences into words and punctuation tokens.")
