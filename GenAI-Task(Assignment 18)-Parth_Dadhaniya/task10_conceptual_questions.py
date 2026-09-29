# Task 10: Conceptual Questions
# Author: Parth Dadhaniya

print("1. Difference between One-Hot Encoding and Bag of Words (BoW):")
print("- One-Hot Encoding is binary (0 or 1) and only tells if a word is present.")
print("- Bag of Words stores word count (integer), telling how many times a word appears in a text.")

print("\n2. Why N-grams increase dimensionality:")
print("- Instead of just single words, N-grams make combinations of 2 or 3 adjacent words.")
print("- There are many more word pairs (bigrams) and triplets (trigrams), so the vocabulary size grows quickly.")

print("\n3. When to prefer TF-IDF over BoW:")
print("- When doing text classification or search.")
print("- Words that appear in almost all documents get penalized by IDF, so common words don't overpower meaningful keywords.")

print("\n4. Limitations of count-based vectorization (BoW & TF-IDF):")
print("- They lose word order and grammar because text is treated like a bag of words.")
print("- They produce very sparse vectors with mostly zeros.")
print("- They do not understand word similarity (e.g. 'happy' and 'glad' are seen as completely different words).")
