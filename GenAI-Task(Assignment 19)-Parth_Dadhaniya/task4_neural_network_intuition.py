# Task 4: Neural Network Intuition Behind Word2Vec
# Author: Parth Dadhaniya

print("1. Architecture Overview:")
print("Word2Vec uses a simple 3-layer neural network with no non-linear activation in the hidden layer.")
print("The prediction task is just a fake helper task; our real goal is extracting the learned weight matrix W.")

print("\nSimple Network Diagram:")
print("Input Layer (1 x V one-hot) ---> Hidden Layer (1 x d linear) ---> Output Layer (1 x V softmax)")
print("            [Weight Matrix W: V x d]         [Weight Matrix W': d x V]")

print("\n2. Explanation of Each Layer:")
print("a) Input Layer:")
print("   - Words enter as 1 x V one-hot vectors (1 at the word index, 0 elsewhere).")
print("b) Hidden Layer (Embedding Layer):")
print("   - Multiplying a one-hot vector by weight matrix W (size V x d) simply pulls out row 'i' of W.")
print("   - In CBOW, the selected rows of all context words are averaged together.")
print("   - No activation function like ReLU or Sigmoid is used here.")
print("c) Output Layer:")
print("   - Hidden vector (1 x d) multiplies output weights W' (size d x V).")
print("   - Softmax converts scores into probabilities over the entire vocabulary.")
print("   - Network calculates cross-entropy loss against the true target word.")

print("\n3. How Weights Become Word Embeddings:")
print("- During training, backpropagation updates weight matrix W using gradient descent.")
print("- Once training finishes, we throw away the output layer and softmax completely.")
print("- Matrix W (size V x d) becomes our embedding lookup table.")
print("- Row 'k' in matrix W is the learned d-dimensional vector for word 'k'.")
