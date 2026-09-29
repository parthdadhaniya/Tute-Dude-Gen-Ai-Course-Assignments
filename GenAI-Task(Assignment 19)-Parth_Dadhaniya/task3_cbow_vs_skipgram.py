# Task 3: CBOW vs Skip-Gram Architectures
# Author: Parth Dadhaniya

print("1. Continuous Bag of Words (CBOW):")
print("- How it works: CBOW takes surrounding context words and predicts the center word.")
print("- Example: In 'the queen ruled the kingdom' with window=1 and target 'ruled':")
print("  Context inputs: ['queen', 'the'] -> Model -> Output target: 'ruled'")
print("- Key points: It averages the context word vectors. It trains very fast and works well for common, frequent words.")

print("\n2. Skip-Gram:")
print("- How it works: Skip-Gram does the opposite. It takes a center word and predicts each surrounding context word.")
print("- Example: In 'the queen ruled the kingdom' with window=1 and input 'ruled':")
print("  Center word: 'ruled' -> Model -> Context outputs: 'queen', 'the'")
print("- Key points: It creates multiple training pairs per word. It takes longer to train, but does much better on rare and infrequent words.")

print("\n3. When to use each:")
print("- Use CBOW if you have a huge dataset (millions of sentences) and want faster training, or care mostly about frequent words.")
print("- Use Skip-Gram if you have a small to medium dataset, domain-specific text, or want better vector quality on rare words.")
