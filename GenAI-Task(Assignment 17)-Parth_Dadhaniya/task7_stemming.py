# Task 7: Word Stemming using Porter Stemmer
# Author: Parth Dadhaniya

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "running",
    "watched",
    "acting",
    "studies",
    "leaves",
    "caring",
    "carefully",
    "repeatedly",
    "amaziiing",
    "connected",
    "sleeping",
    "predictable"
]

print("Original Word -> Stemmed Word:")
for w in words:
    print(f"  {w:<15} -> {stemmer.stem(w)}")

print("\nNotes on Stemming:")
print("- Stemming strips suffixes like -ing, -ed, -ly using fixed rules.")
print("- It often makes non-dictionary words (e.g. 'studies' -> 'studi').")
print("- It is fast and does not use a dictionary.")
