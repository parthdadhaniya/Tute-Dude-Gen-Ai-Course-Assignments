# Task 7: Train Skip-Gram Word2Vec Model & Compare with CBOW
# Author: Parth Dadhaniya

import os
import time
import pandas as pd
from gensim.models import Word2Vec

# load dataset
csv_path = "cleaned_text_corpus.csv"
if not os.path.exists(csv_path):
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_text_corpus.csv")

df = pd.read_csv(csv_path)
sentences = [str(t).strip().split() for t in df["clean_text"] if str(t).strip()]

# 1. Train CBOW (sg=0) and time it
t0 = time.time()
model_cbow = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0, seed=42, epochs=50)
cbow_time = time.time() - t0
print(f"CBOW (sg=0) Training Time:      {cbow_time * 1000:.2f} ms")

# 2. Train Skip-Gram (sg=1) and time it
t1 = time.time()
model_sg = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1, seed=42, epochs=50)
sg_time = time.time() - t1
print(f"Skip-Gram (sg=1) Training Time: {sg_time * 1000:.2f} ms")

# save skip-gram model
save_path = os.path.join(os.path.dirname(__file__), "word2vec_skipgram.model")
model_sg.save(save_path)
print("\nSaved model as: word2vec_skipgram.model")

# 3. Compare top similar words for key query words
test_words = ["movie", "king", "phone"]
print("\nComparing Similar Words (CBOW vs Skip-Gram):")

for w in test_words:
    print(f"\nWord: '{w}'")
    cbow_sims = [sim_w for sim_w, _ in model_cbow.wv.most_similar(w, topn=3)]
    sg_sims = [sim_w for sim_w, _ in model_sg.wv.most_similar(w, topn=3)]
    print("  CBOW:     ", cbow_sims)
    print("  Skip-Gram:", sg_sims)
