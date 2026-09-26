# Assignment 16: NLP Text Preprocessing Pipeline

This project implements an end-to-end text preprocessing pipeline in Python using NLTK and Pandas.

## Dataset
- **File:** `customer_reviews.csv`
- **Source:** Self-curated customer feedback and product reviews dataset (25 samples) containing real-world raw text noise.
- **Issues included:** URLs, emails, HTML tags, emojis, punctuation, numbers, inconsistent casing, and stopwords.

## Files Included

- **`customer_reviews.csv`**: Raw text dataset.
- **`task1_load_inspect.py`**: Loading data, printing 5 samples with lengths, and identifying text issues.
- **`task2_basic_cleaning.py`**: Lowercasing, removing punctuation, numbers, and extra spaces (`clean_text_basic`).
- **`task3_advanced_noise_removal.py`**: Regex cleaning for URLs, emails, HTML, and emojis (`clean_text_advanced`).
- **`task4_stopword_removal.py`**: Removing stopwords using NLTK (`text_no_stopwords`).
- **`task5_tokenization.py`**: Sentence tokenization on 3 samples.
- **`task6_tokenization.py`**: Word and sentence tokenization on 3 samples.
- **`task7_stemming.py`**: Word stemming using PorterStemmer.
- **`task8_lemmatization.py`**: Comparing WordNet lemmatizer vs Porter stemmer.
- **`task9_pipeline.py`**: Complete `nlp_preprocess(text)` pipeline saved to `cleaned_reviews_final.csv`.
- **`task10_observations.py`**: Technical observations on cleaning, stemming vs lemmatization, and preprocessing.
- **`main.py`**: Runs all tasks in order.
- **`assignment16.ipynb`**: Complete Jupyter Notebook.

## How to Run

Run all tasks:
```bash
python main.py
```

Or run any task individually:
```bash
python task1_load_inspect.py
python task2_basic_cleaning.py
python task3_advanced_noise_removal.py
python task4_stopword_removal.py
python task5_tokenization.py
python task6_tokenization.py
python task7_stemming.py
python task8_lemmatization.py
python task9_pipeline.py
python task10_observations.py
```
