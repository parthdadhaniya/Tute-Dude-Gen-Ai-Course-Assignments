# Task 6: Ollama Embedding Model (Local Setup)
# Parth Dadhaniya

import json
import urllib.request
import numpy as np

print("Task 6: Ollama Local Embedding Setup\n")

print("How to run Ollama locally:")
print("1. Install Ollama from https://ollama.ai")
print("2. Run in terminal: ollama serve")
print("3. Pull embedding model: ollama pull nomic-embed-text")
print("4. Endpoint runs at: http://localhost:11434/api/embeddings\n")

# test text
text = "The Personal Knowledge Assistant helps team members query documents."

# try connecting to local ollama instance
ollama_url = "http://localhost:11434/api/embeddings"
payload = json.dumps({"model": "nomic-embed-text", "prompt": text}).encode("utf-8")
req = urllib.request.Request(ollama_url, data=payload, headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req, timeout=2) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        vector = data["embedding"]
        print("Connected to live Ollama server successfully!")
except Exception:
    # student fallback for offline testing
    np.random.seed(123)
    vector = np.random.randn(768).tolist()
    print("Ollama server not active on localhost:11434. Generated nomic-embed-text 768-dim format for testing.")

print("\nModel: nomic-embed-text")
print("Vector dimensions:", len(vector))
print("Sample values (first 5):", [round(x, 4) for x in vector[:5]])

print("\nComparison with OpenAI embeddings:")
print("- Ollama (nomic-embed-text): 768 dimensions, 100% private, free, runs on local RAM/GPU.")
print("- OpenAI (text-embedding-3-small): 1536 dimensions, requires internet and API billing.")
