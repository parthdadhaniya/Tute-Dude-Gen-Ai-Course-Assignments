# Task 1: Text Loader
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader

# loading notes.txt using TextLoader
loader = TextLoader("data/notes.txt", encoding="utf-8")
docs = loader.load()

print("Number of documents loaded:", len(docs))
print("\nDocument Metadata:")
print(docs[0].metadata)

print("\nPage Content Preview:")
print(docs[0].page_content[:300])
print("\n... [total characters:", len(docs[0].page_content), "]")
