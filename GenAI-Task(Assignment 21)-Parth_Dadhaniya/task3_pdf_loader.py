# Task 3: PDF Loader
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader

# loading pdf document using PyPDFLoader
loader = PyPDFLoader("data/sample.pdf")
pages = loader.load()

print("Total pages loaded:", len(pages))

print("\n--- Page 1 Content ---")
print(pages[0].page_content)
print("Metadata:", pages[0].metadata)

if len(pages) > 1:
    print("\n--- Page 2 Content ---")
    print(pages[1].page_content)
    print("Metadata:", pages[1].metadata)
