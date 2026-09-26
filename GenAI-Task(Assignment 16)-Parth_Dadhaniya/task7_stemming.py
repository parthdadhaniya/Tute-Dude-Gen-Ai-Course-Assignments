# Task 7: Word Stemming using Porter Stemmer
# Author: Parth Dadhaniya

import sys
from nltk.stem import PorterStemmer

sys.stdout.reconfigure(encoding="utf-8")

stemmer = PorterStemmer()

# words from our dataset
words = [
    "running",
    "studies",
    "attentive",
    "carefully",
    "repeatedly",
    "happily",
    "leaves",
    "easily",
    "connected",
    "prescribing",
    "delivery",
    "batteries"
]

print("Porter Stemmer - Original vs Stemmed Words:")
print("Original Word   | Stemmed Word")
print("----------------|-------------")

for w in words:
    stemmed = stemmer.stem(w)
    print(f"{w:<15} | {stemmed}")

print("\nObservations:")
print("- Stemming removes common word endings like -ing, -ly, -ies.")
print("- It often creates words that are not in the dictionary, like 'studies' -> 'studi'.")
print("- It is fast and does not need a dictionary.")
