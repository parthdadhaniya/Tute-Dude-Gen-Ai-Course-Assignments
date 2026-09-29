# Assignment 18: Text Vectorization Techniques

This project implements and compares core text vectorization techniques in Python using Scikit-Learn, Pandas, and NumPy.

## Dataset
- **File:** `cleaned_text_dataset.csv`
- **Source:** Preprocessed text dataset from Assignment 17 containing 25 samples of movie reviews, product reviews, tweets, and support tickets.
- **Columns:** `id`, `category`, `raw_text`, `final_clean_text`.

## Files Included

- **`cleaned_text_dataset.csv`**: Text dataset with 25 samples.
- **`task1_manual_one_hot.py`**: Manual implementation of text-level One-Hot Encoding using Python lists.
- **`task2_sklearn_one_hot.py`**: One-Hot Encoding using `CountVectorizer(binary=True)`.
- **`task3_bag_of_words.py`**: Bag of Words (BoW) vector representation of the entire dataset.
- **`task4_word_frequency.py`**: Computing word frequency, identifying top 10 and least frequent words.
- **`task5_ngrams.py`**: Comparing Unigrams (1,1), Bigrams (2,2), and Trigrams (3,3) vocabulary size.
- **`task6_combined_ngrams.py`**: Combined Unigrams and Bigrams (`ngram_range=(1,2)`) to capture context.
- **`task7_tfidf.py`**: TF-IDF vectorization with `TfidfVectorizer()`.
- **`task8_bow_vs_tfidf.py`**: Comparing BoW frequencies vs TF-IDF scores and explaining IDF down-weighting.
- **`task9_vectorizer_parameters.py`**: Exploring `max_features`, `min_df`, and `max_df` parameters.
- **`task10_conceptual_questions.py`**: Answers to conceptual questions on vectorization.
- **`main.py`**: Runs all 10 tasks in order.
- **`assignment18.ipynb`**: Complete Jupyter Notebook.

## How to Run

Run all tasks:
```bash
python main.py
```

Or run any task individually:
```bash
python task1_manual_one_hot.py
python task2_sklearn_one_hot.py
python task3_bag_of_words.py
python task4_word_frequency.py
python task5_ngrams.py
python task6_combined_ngrams.py
python task7_tfidf.py
python task8_bow_vs_tfidf.py
python task9_vectorizer_parameters.py
python task10_conceptual_questions.py
```
