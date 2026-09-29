# Task 3: Comparison - OpenAI vs Hugging Face Embeddings
# Parth Dadhaniya

print("Task 3: Comparison - OpenAI vs Hugging Face Embeddings\n")

print("1. When to prefer OpenAI embeddings?")
print("- When building production cloud apps that need high accuracy across many languages.")
print("- When you don't want to manage local GPUs or model weights.")
print("- When 1536 or 3072 dimensions are needed for nuanced search.\n")

print("2. When to prefer Hugging Face embeddings?")
print("- When data privacy is critical and documents cannot leave your local server.")
print("- In completely offline or air-gapped systems.")
print("- When indexing large volumes of documents where API costs would be too high.")
print("- When you need domain-specific fine-tuned models (e.g. biobert, legal-bert).\n")

print("3. Cost vs Performance Trade-offs:")
print("- OpenAI: Very fast setup with an API key, but ongoing per-token cost ($0.02 per 1M tokens).")
print("- Hugging Face: Zero API fees, but requires local computer RAM and CPU/GPU power.")
