# Assignment 19: Word2Vec Text Embeddings
# Author: Parth Dadhaniya

import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec

# load cleaned corpus
csv_path = "cleaned_text_corpus.csv"
if not os.path.exists(csv_path):
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_text_corpus.csv")

df = pd.read_csv(csv_path)
sentences = [str(t).strip().split() for t in df["clean_text"] if str(t).strip()]

print("Assignment 19: Word2Vec Text Embeddings")
print("Author: Parth Dadhaniya")
print(f"Loaded {len(sentences)} sentences from cleaned_text_corpus.csv")

# Task 5: Text Preparation
print("\n--- Task 5: Text Preparation ---")
print("Total Sentences:", len(sentences))
print("Sample Sentence 1:", sentences[0])

# Task 6: Train CBOW Word2Vec (sg=0)
print("\n--- Task 6: Train CBOW Word2Vec (sg=0) ---")
model_cbow = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0, seed=42, epochs=50)
print("CBOW Vocabulary Size:", len(model_cbow.wv.key_to_index))
print("Sample vector for 'movie':", model_cbow.wv["movie"][:8], "...")

# Task 7: Train Skip-Gram Word2Vec (sg=1) & compare
print("\n--- Task 7: Train Skip-Gram Word2Vec (sg=1) ---")
t0 = time.time()
model_cbow_timed = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0, seed=42, epochs=50)
t_cbow = time.time() - t0

t1 = time.time()
model_sg = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1, seed=42, epochs=50)
t_sg = time.time() - t1

print(f"CBOW Training Time:      {t_cbow * 1000:.2f} ms")
print(f"Skip-Gram Training Time: {t_sg * 1000:.2f} ms")

print("\nSimilar words for 'king':")
print("CBOW:     ", [w for w, _ in model_cbow.wv.most_similar("king", topn=3)])
print("Skip-Gram:", [w for w, _ in model_sg.wv.most_similar("king", topn=3)])

# Task 8: Word Similarity and Vector Operations
print("\n--- Task 8: Similarity & Vector Arithmetic ---")
wv = model_sg.wv
print("Most similar to 'movie':", [w for w, _ in wv.most_similar("movie", topn=3)])

print("Analogy (king - man + woman):")
for w, score in wv.most_similar(positive=["king", "woman"], negative=["man"], topn=2):
    print(f"  {w} : {score:.4f}")

print("Cosine Similarity:")
print("  movie <-> film:", round(wv.similarity("movie", "film"), 4))
print("  king <-> queen:", round(wv.similarity("king", "queen"), 4))
print("  king <-> battery (unrelated):", round(wv.similarity("king", "battery"), 4))

print("Odd-One-Out (['phone', 'laptop', 'battery', 'king']):", wv.doesnt_match(["phone", "laptop", "battery", "king"]))

# Task 9: 2D PCA Visualization
print("\n--- Task 9: Visualizing Embeddings (PCA) ---")
words_to_plot = ["movie", "film", "actor", "phone", "battery", "laptop", "king", "queen", "palace"]
vecs = [wv[w] for w in words_to_plot]
coords = PCA(n_components=2, random_state=42).fit_transform(vecs)

plt.figure(figsize=(8, 5))
for i, w in enumerate(words_to_plot):
    plt.scatter(coords[i, 0], coords[i, 1], s=60)
    plt.annotate(w, (coords[i, 0], coords[i, 1]), xytext=(5, 5), textcoords="offset points")
plt.title("Word2Vec 2D Embeddings (PCA)")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("word_embeddings_2d_plot.png", dpi=300)
plt.close()
print("Saved 2D PCA plot to: word_embeddings_2d_plot.png")

# Task 10: Summary
print("\n--- Task 10: Key Observations ---")
print("1. CBOW is faster to train; Skip-Gram handles infrequent words better.")
print("2. Word2Vec produces dense semantic vectors capable of analogical reasoning, unlike BoW/TF-IDF.")
print("3. Word2Vec produces static embeddings (polysemy limitation). Modern NLP uses contextual transformers (BERT/GPT).")
