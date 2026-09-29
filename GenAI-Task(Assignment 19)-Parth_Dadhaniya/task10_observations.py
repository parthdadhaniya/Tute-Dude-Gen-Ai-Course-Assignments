# Task 10: Observations & Limitations
# Author: Parth Dadhaniya

print("1. Difference between CBOW and Skip-Gram in practice:")
print("- CBOW is faster to train and averages context words. It gives good representations for frequent words.")
print("- Skip-Gram takes more time because it creates more word pairs, but it performs better on rare and infrequent words.")
print("- In our test, Skip-Gram took ~7 seconds vs CBOW ~2 seconds, but Skip-Gram gave better neighbors for domain terms.")

print("\n2. Advantages of Word2Vec over TF-IDF:")
print("- Dense vs Sparse: Word2Vec produces short, dense vectors (e.g. 100 numbers) instead of huge sparse vectors (10,000 numbers).")
print("- Semantic meaning: Synonyms like 'movie' and 'film' have high cosine similarity in Word2Vec. TF-IDF sees them as completely separate.")
print("- Vector arithmetic: Word2Vec allows analogical math like king - man + woman = queen, which is impossible with TF-IDF counts.")

print("\n3. Limitations of Word2Vec:")
print("- Static embeddings: Each word gets only one fixed vector. It cannot handle multiple meanings (e.g. 'apple' fruit vs 'apple' company).")
print("- Out of Vocabulary (OOV): If a new word was not in the training corpus, the model cannot make a vector for it.")
print("- Needs large text: To get high-quality vectors for large vocabularies, it requires massive amounts of training text.")

print("\n4. Why context still matters in modern NLP (Lead-in to Transformers):")
print("- Word2Vec vectors are static and cannot change based on the sentence.")
print("- Modern models like BERT and GPT use self-attention to generate dynamic contextual embeddings.")
print("- For example, 'bank' gets a different vector in 'river bank' than in 'bank deposit'. This led directly to modern LLMs.")
