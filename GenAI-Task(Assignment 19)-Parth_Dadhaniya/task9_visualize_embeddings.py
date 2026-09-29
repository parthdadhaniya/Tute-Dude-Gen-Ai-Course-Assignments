# Task 9: Visualizing Word Embeddings (PCA 2D)
# Author: Parth Dadhaniya

import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec

# load trained skip-gram model
model_path = os.path.join(os.path.dirname(__file__), "word2vec_skipgram.model")
model = Word2Vec.load(model_path)
wv = model.wv

# choose 4 categories to plot
words_to_plot = {
    "Cinema": ["movie", "film", "actor", "actress", "cinema", "director"],
    "Tech": ["phone", "battery", "laptop", "screen", "keyboard", "device"],
    "Support": ["customer", "service", "support", "refund", "ticket", "order"],
    "Royalty": ["king", "queen", "prince", "princess", "palace", "kingdom"],
}

colors = {"Cinema": "red", "Tech": "blue", "Support": "green", "Royalty": "purple"}

all_words = []
all_vectors = []
all_colors = []

for category, word_list in words_to_plot.items():
    for w in word_list:
        if w in wv:
            all_words.append(w)
            all_vectors.append(wv[w])
            all_colors.append(colors[category])

print(f"Selected {len(all_words)} words across 4 categories.")

# reduce 100D vectors down to 2D using PCA
pca = PCA(n_components=2, random_state=42)
coords_2d = pca.fit_transform(all_vectors)

# plot scatter plot
plt.figure(figsize=(9, 6))

for i, word in enumerate(all_words):
    x, y = coords_2d[i, 0], coords_2d[i, 1]
    plt.scatter(x, y, color=all_colors[i], s=70)
    plt.annotate(word, (x, y), xytext=(5, 5), textcoords="offset points", fontsize=10)

# create legend
for category, color in colors.items():
    plt.scatter([], [], color=color, label=category)

plt.legend(title="Category")
plt.title("2D Projection of Word Embeddings (PCA)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

output_path = os.path.join(os.path.dirname(__file__), "word_embeddings_2d_plot.png")
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Saved plot as: word_embeddings_2d_plot.png")
print("Observation: Words from the same topic group cluster near each other in 2D space.")
