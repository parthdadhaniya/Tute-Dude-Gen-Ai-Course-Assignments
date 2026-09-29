# Task 2: CSV Loader
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import CSVLoader

# loading tabular data where each row becomes one Document
loader = CSVLoader("data/data.csv", encoding="utf-8")
docs = loader.load()

print("Number of documents loaded from CSV:", len(docs))
print("(Each row is converted into a separate Document object)\n")

print("Sample Document 1:")
print(docs[0].page_content)
print("\nMetadata:", docs[0].metadata)

print("\nSample Document 2:")
print(docs[1].page_content)
print("\nMetadata:", docs[1].metadata)
