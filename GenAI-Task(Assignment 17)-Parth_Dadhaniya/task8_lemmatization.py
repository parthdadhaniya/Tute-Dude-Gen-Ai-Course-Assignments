# Task 8: WordNet Lemmatization vs Stemming
# Author: Parth Dadhaniya

from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# words with part-of-speech (pos): n = noun, v = verb, a = adjective, r = adverb
test_words = [
    ("running", "v"),
    ("watched", "v"),
    ("studies", "n"),
    ("leaves", "n"),
    ("better", "a"),
    ("corpora", "n"),
    ("caring", "v"),
    ("carefully", "r"),
    ("happier", "a"),
    ("sleeping", "v")
]

print("Comparing Stemming vs Lemmatization:")
for word, pos in test_words:
    stemmed = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos=pos)
    print(f"  {word:<12} | Stem: {stemmed:<10} | Lemma: {lemma}")

print("\nNotes:")
print("- Lemmatization returns real dictionary words (studies -> study, leaves -> leaf).")
print("- Stemming simply cuts suffixes without checking vocabulary (studies -> studi).")
print("- Lemmatization uses part of speech tags to find the correct base word.")
