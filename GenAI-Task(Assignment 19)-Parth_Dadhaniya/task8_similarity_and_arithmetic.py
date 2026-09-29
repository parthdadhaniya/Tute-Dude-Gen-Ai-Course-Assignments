# Task 8: Word Similarity & Vector Operations
# Author: Parth Dadhaniya

import os
import pandas as pd
from gensim.models import Word2Vec

# load trained skip-gram model
model_path = os.path.join(os.path.dirname(__file__), "word2vec_skipgram.model")
if os.path.exists(model_path):
    model = Word2Vec.load(model_path)
else:
    # fallback to train if not saved yet
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_text_corpus.csv")
    df = pd.read_csv(csv_path)
    sentences = [str(t).strip().split() for t in df["clean_text"] if str(t).strip()]
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1, seed=42, epochs=50)

wv = model.wv

# 1. Most Similar Words
print("1. Most Similar Words:")
for word in ["king", "movie", "customer", "battery"]:
    matches = wv.most_similar(word, topn=3)
    print(f"\nTop 3 words similar to '{word}':")
    for w, score in matches:
        print(f"  {w} : {score:.4f}")

# 2. Vector Arithmetic (Analogy Reasoning)
print("\n2. Vector Arithmetic (Analogy):")

# king - man + woman ~= queen
print("\nAnalogy: king - man + woman")
analogy1 = wv.most_similar(positive=["king", "woman"], negative=["man"], topn=3)
for w, score in analogy1:
    print(f"  {w} : {score:.4f}")

# actor - man + woman ~= actress
print("\nAnalogy: actor - man + woman")
analogy2 = wv.most_similar(positive=["actor", "woman"], negative=["man"], topn=3)
for w, score in analogy2:
    print(f"  {w} : {score:.4f}")

# 3. Pairwise Cosine Similarity
print("\n3. Pairwise Cosine Similarity:")
pairs = [
    ("movie", "film"),
    ("king", "queen"),
    ("phone", "battery"),
    ("customer", "service"),
    ("king", "battery"),  # unrelated
]
for w1, w2 in pairs:
    sim = wv.similarity(w1, w2)
    print(f"  similarity('{w1}', '{w2}') = {sim:.4f}")

# 4. Odd-One-Out (doesnt_match)
print("\n4. Odd-One-Out Detection (doesnt_match):")
group1 = ["phone", "laptop", "battery", "king"]
print(f"  Group: {group1} -> Odd word: '{wv.doesnt_match(group1)}'")

group2 = ["movie", "film", "cinema", "refund"]
print(f"  Group: {group2} -> Odd word: '{wv.doesnt_match(group2)}'")
