# Task 8: WordNet Lemmatization vs Stemming
# Author: Parth Dadhaniya

import sys
from nltk.stem import PorterStemmer, WordNetLemmatizer

sys.stdout.reconfigure(encoding="utf-8")

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# list of words with part of speech tags
# n = noun, v = verb, a = adjective, r = adverb
test_words = [
    ("running", "v"),
    ("studies", "n"),
    ("leaves", "n"),
    ("better", "a"),
    ("corpora", "n"),
    ("caring", "v"),
    ("happily", "r"),
    ("batteries", "n"),
    ("easily", "r"),
    ("connected", "v")
]

print("Comparing Stemming vs Lemmatization:")
print("Word         | POS | Stemmed (Porter) | Lemmatized (WordNet)")
print("-------------|-----|------------------|---------------------")

for word, pos in test_words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word, pos=pos)
    print(f"{word:<12} | {pos:<3} | {stemmed:<16} | {lemmatized}")

print("\nDifferences:")
print("- Lemmatization produces valid dictionary words (studies -> study, leaves -> leaf).")
print("- Stemming just cuts off suffixes, which can create non-words (studies -> studi, leaves -> leav).")
print("- Lemmatization uses part of speech tags to understand word context.")
