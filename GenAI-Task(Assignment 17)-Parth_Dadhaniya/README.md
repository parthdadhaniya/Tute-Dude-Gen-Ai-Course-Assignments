# Assignment 17: Text Cleaning, Preprocessing & NLP Pipeline

This project implements an end-to-end text preprocessing pipeline in Python using NLTK and Pandas.

## Dataset
- **File:** `raw_text_data.csv`
- **Source:** Self-curated dataset of 25 text samples covering movie reviews, product reviews, tweets, and customer support tickets.
- **Issues included:** Uppercase/lowercase mismatch, punctuation clusters, numbers, dates, URLs, emails, HTML tags, emojis, repeated characters, slang, and stopwords.

## Files Included

- **`raw_text_data.csv`**: Raw text dataset.
- **`task1_understanding_raw_text.py`**: Loading data, printing 5 samples with lengths, and identifying text issues.
- **`task2_basic_cleaning.py`**: Lowercasing, removing punctuation, numbers, and extra spaces (`clean_text_basic`).
- **`task3_noise_removal.py`**: Regex cleaning for URLs, emails, HTML tags, and emojis (`clean_text_advanced`).
- **`task4_stopwords.py`**: Removing stopwords using NLTK (`text_no_stopwords`).
- **`task5_slang_and_repeated_chars.py`**: Normalizing repeated letters and replacing slang words (`clean_text_slang`).
- **`task6_tokenization.py`**: Word and sentence tokenization on 3 samples.
- **`task7_stemming.py`**: Word stemming using PorterStemmer.
- **`task8_lemmatization.py`**: Comparing WordNet lemmatizer vs Porter stemmer.
- **`task9_pipeline.py`**: Complete `nlp_preprocess(text)` pipeline saved to `cleaned_text_final.csv`.
- **`task10_observations.py`**: Technical observations on cleaning, stemming vs lemmatization, and preprocessing.
- **`main.py`**: Runs all 10 tasks in order.
- **`assignment17.ipynb`**: Complete Jupyter Notebook.

## How to Run

Run all tasks:
```bash
python main.py
```

Or run any task individually:
```bash
python task1_understanding_raw_text.py
python task2_basic_cleaning.py
python task3_noise_removal.py
python task4_stopwords.py
python task5_slang_and_repeated_chars.py
python task6_tokenization.py
python task7_stemming.py
python task8_lemmatization.py
python task9_pipeline.py
python task10_observations.py
```
