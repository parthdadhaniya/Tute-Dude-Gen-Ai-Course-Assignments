# Task 7: Length-Based Text Splitter
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# 1. Load document
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
print(f"Original Document length: {len(docs[0].page_content)} characters")

# 2. Configure CharacterTextSplitter
chunk_size = 250
chunk_overlap = 40

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

# 3. Split document into chunks
chunks = splitter.split_documents(docs)

print(f"\nConfiguration: chunk_size={chunk_size}, chunk_overlap={chunk_overlap}")
print(f"Total Chunks Created: {len(chunks)}")

print("\n--- Sample Chunk 1 ---")
print(f"Length: {len(chunks[0].page_content)} chars")
print(chunks[0].page_content)
print("Metadata:", chunks[0].metadata)

print("\n--- Sample Chunk 2 ---")
print(f"Length: {len(chunks[1].page_content)} chars")
print(chunks[1].page_content)
print("Metadata:", chunks[1].metadata)

print("\nObservations on CharacterTextSplitter:")
print("- Splits strictly on a single separator ('\\n').")
print("- If a paragraph exceeds chunk_size without the separator, it cannot split it further.")
