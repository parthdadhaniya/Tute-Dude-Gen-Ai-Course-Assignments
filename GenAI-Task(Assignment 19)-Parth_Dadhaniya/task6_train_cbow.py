# Task 6: Train CBOW Word2Vec Model
# Author: Parth Dadhaniya

import os
import pandas as pd
from gensim.models import Word2Vec

# load sentences
csv_path = "cleaned_text_corpus.csv"
if not os.path.exists(csv_path):
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_text_corpus.csv")

df = pd.read_csv(csv_path)
sentences = [str(t).strip().split() for t in df["clean_text"] if str(t).strip()]

print(f"Loaded {len(sentences)} sentences for training.")

# train Word2Vec model using CBOW (sg=0)
model_cbow = Word2Vec(
    sentences=sentences,
    vector_size=100,
    window=5,
    min_count=1,
    sg=0,
    seed=42,
    epochs=50
)

# vocabulary size
vocab_size = len(model_cbow.wv.key_to_index)
print(f"CBOW Vocabulary Size: {vocab_size} unique words")

# inspect sample word vector
sample_word = "movie"
sample_vector = model_cbow.wv[sample_word]
print(f"\nSample word: '{sample_word}'")
print(f"Vector length: {len(sample_vector)}")
print("First 10 vector values:")
print(sample_vector[:10])

# save model
save_path = os.path.join(os.path.dirname(__file__), "word2vec_cbow.model")
model_cbow.save(save_path)
print("\nSaved model as: word2vec_cbow.model")
