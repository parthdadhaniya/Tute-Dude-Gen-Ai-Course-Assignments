# Assignment 19: Word2Vec Text Embeddings
**Student:** Parth Dadhaniya  
**Course:** GenAI Course  

---

## 1. Project Overview
In this assignment, we implement and study **Word2Vec Text Embeddings**. Traditional vectorization methods like One-Hot Encoding and Bag of Words (BoW) represent words as sparse, orthogonal vectors that completely ignore word meaning and semantic context. Word2Vec addresses this by training a shallow neural network to map words into continuous, low-dimensional dense vector spaces where semantic relationships are captured mathematically.

This assignment covers:
- Understanding Word Embeddings and why traditional methods fail
- Word2Vec intuition, vocabulary, context window, and embedding dimensions
- Architectural differences between CBOW (Continuous Bag of Words) and Skip-Gram
- Neural network weights functioning as embedding lookup tables
- Custom corpus tokenization (list-of-lists format)
- Training CBOW (`sg=0`) and Skip-Gram (`sg=1`) models with Gensim
- Semantic word similarity, pairwise cosine distance, and vector analogies (`king - man + woman = queen`)
- 2D PCA visualization demonstrating domain-specific clustering
- In-depth technical observations and transition to modern transformer models

---

## 2. Dataset Description
- **Dataset File:** `cleaned_text_corpus.csv`
- **Total Samples:** 45 domain-balanced sentences
- **Cleaned Text:** Preprocessed using NLP pipeline (lowercase, removed punctuation, special characters, URLs, and stopwords)
- **Domain Categories:**
  1. *Movie Reviews & Cinema:* films, actors, directors, theaters, plot, performances.
  2. *Tech & Gadgets:* smartphones, laptops, battery life, screens, wireless devices.
  3. *Customer Support:* service tickets, orders, refunds, delivery, response times.
  4. *Royalty & Society:* king, queen, prince, princess, royal palace, kingdom.
  5. *NLP & Machine Learning:* embeddings, vectors, CBOW, Skip-Gram, semantics.

---

## 3. Directory Structure
```
GenAI-Task(Assignment 19)-Parth_Dadhaniya/
│
├── cleaned_text_corpus.csv           # 45-sample domain-balanced text corpus
├── task1_word_embeddings_intro.py    # Conceptual Q&A on word embeddings
├── task2_word2vec_overview.py        # Word2Vec concepts, window, dimensions
├── task3_cbow_vs_skipgram.py         # CBOW vs Skip-Gram mechanics & usage
├── task4_neural_network_intuition.py # 3-layer neural network architecture
├── task5_prepare_text.py             # Sentence and word tokenization
├── task6_train_cbow.py               # CBOW model training (sg=0)
├── task7_train_skipgram.py           # Skip-Gram model training (sg=1) & comparison
├── task8_similarity_and_arithmetic.py# Similarity, analogies, odd-one-out
├── task9_visualize_embeddings.py     # 2D PCA visualization & plot generation
├── task10_observations.py            # Summary of findings and limitations
├── main.py                           # Master script running all tasks sequentially
├── assignment19.ipynb                # Interactive Jupyter Notebook
├── word2vec_cbow.model               # Trained CBOW model artifact
├── word2vec_skipgram.model           # Trained Skip-Gram model artifact
├── word_embeddings_2d_plot.png       # Generated 2D PCA cluster plot
└── README.md                         # Documentation
```

---

## 4. Key Experiments & Results

### Task 1: Word Embeddings vs Traditional Representations
- **One-Hot / BoW Limitations:** Every word is represented as an independent orthogonal vector. Dot product of any two distinct words is always `0`.
- **Word Embeddings:** Represent words as dense, real-valued vectors (e.g., 100 dimensions). Semantic similarity corresponds to cosine distance in vector space.

### Task 2 & 3: CBOW vs Skip-Gram
| Feature | CBOW (`sg=0`) | Skip-Gram (`sg=1`) |
| :--- | :--- | :--- |
| **Prediction Task** | Context words $\rightarrow$ Center word | Center word $\rightarrow$ Context words |
| **Hidden Layer** | Averages context vectors | Direct vector projection |
| **Speed** | Significantly faster | Slower (more training pairs) |
| **Best For** | Large corpora, frequent words | Small/medium corpora, rare words |

### Task 6 & 7: Model Training Details
- **Architecture Parameters:** `vector_size=100`, `window=5`, `min_count=1`, `epochs=50`.
- **Vocabulary Size:** ~160+ unique words.
- Both models successfully produce 100-dimensional dense vectors for all corpus words.

### Task 8: Vector Arithmetic & Similarity
- **Vector Analogy:**
  $$\vec{v}_{\text{king}} - \vec{v}_{\text{man}} + \vec{v}_{\text{woman}} \approx \vec{v}_{\text{queen}}$$
- **Cosine Similarities:**
  - High similarity between synonyms: `movie` $\leftrightarrow$ `film`, `king` $\leftrightarrow$ `queen`, `phone` $\leftrightarrow$ `battery`.
  - Near zero / low similarity between cross-domain terms: `king` $\leftrightarrow$ `battery`.
- **Outlier Detection (`doesnt_match`):**
  - In `['phone', 'laptop', 'battery', 'king']` $\rightarrow$ Correctly detects `'king'`.
  - In `['movie', 'film', 'cinema', 'refund']` $\rightarrow$ Correctly detects `'refund'`.

### Task 9: 2D Embedding Visualization
PCA dimensionality reduction maps the 100-dimensional embeddings to 2D components. Plotting words across categories confirms distinct spatial clustering:
- Cinema words cluster together in Component 1-2 space.
- Hardware/Tech terms group tightly around battery and laptop.
- Royalty words form a well-separated cluster.

---

## 5. How to Run

### Run All Tasks Sequentially:
```bash
py -3.12 main.py
```

### Run Individual Tasks:
```bash
py -3.12 task5_prepare_text.py
py -3.12 task6_train_cbow.py
py -3.12 task7_train_skipgram.py
py -3.12 task8_similarity_and_arithmetic.py
py -3.12 task9_visualize_embeddings.py
```
