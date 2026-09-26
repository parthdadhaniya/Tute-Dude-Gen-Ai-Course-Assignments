# Task 5: Sentence Tokenization
# Author: Parth Dadhaniya

import sys
import pandas as pd
from nltk.tokenize import sent_tokenize

sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("customer_reviews.csv")

# select 3 samples with multiple sentences
sample_ids = [2, 7, 10]
samples = df[df["id"].isin(sample_ids)]

print("Sentence Tokenization on 3 Samples:")
for i, row in samples.iterrows():
    text = row["raw_text"]
    sentences = sent_tokenize(text)
    
    print(f"\nSample {row['id']} [{row['category']}]:")
    print("Raw Text:", text)
    print(f"Total Sentences: {len(sentences)}")
    for idx, sentence in enumerate(sentences, 1):
        print(f"  Sentence {idx}: {sentence}")
