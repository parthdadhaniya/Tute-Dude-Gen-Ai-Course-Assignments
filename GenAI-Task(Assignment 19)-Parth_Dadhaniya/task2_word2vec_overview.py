# Task 2: Word2Vec Overview & Concepts
# Author: Parth Dadhaniya

print("1. What is Word2Vec?")
print("- Word2Vec is a shallow neural network model introduced by Tomas Mikolov and Google in 2013.")
print("- It learns word vectors by scanning text and observing which words appear next to each other.")

print("\n2. The Core Idea: Predicting Words from Context")
print("- It follows the idea: 'You shall know a word by the company it keeps'.")
print("- Instead of just counting words like BoW, Word2Vec slides a small window across text.")
print("- It trains a small network to predict target words from context words, or context words from a target word.")
print("- Through this training, words in similar contexts get similar vector numbers.")

print("\n3. Key Definitions:")
print("a) Vocabulary (V):")
print("   - All unique words in the text dataset that meet a minimum count threshold.")
print("b) Context Window:")
print("   - Number of words before and after the target word to consider as context.")
print("   - Example: with window=2, for 'the cute dog barked loudly', context for 'dog' is ['the', 'cute', 'barked', 'loudly'].")
print("c) Embedding Dimension (d):")
print("   - Size of the dense vector for each word (like 50, 100, or 300 numbers).")
print("   - Higher dimension captures more details but takes more memory and training data.")
