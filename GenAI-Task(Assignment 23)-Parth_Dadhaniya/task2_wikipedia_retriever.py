# Task 2: Wikipedia Retriever
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.retrievers import WikipediaRetriever

print("--- Task 2: Wikipedia Retriever ---")

# initialize wikipedia retriever to get top 2 results
retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "Artificial Intelligence"
print("Searching Wikipedia for:", query)

try:
    docs = retriever.invoke(query)
    print(f"\nFound {len(docs)} articles:\n")
    for i, doc in enumerate(docs, 1):
        print(f"[{i}] Title: {doc.metadata.get('title')}")
        print(f"Source: {doc.metadata.get('source')}")
        print(f"Summary: {doc.page_content[:200]}...\n")
except Exception as e:
    print("Could not connect to Wikipedia:", e)
