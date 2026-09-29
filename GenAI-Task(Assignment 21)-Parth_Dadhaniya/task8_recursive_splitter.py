# Task 8: Text Structure-Based Splitter
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# 1. Load document
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
print(f"Original Document length: {len(docs[0].page_content)} characters")

chunk_size = 250
chunk_overlap = 40

# 2. CharacterTextSplitter (length/single separator)
char_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
char_chunks = char_splitter.split_documents(docs)

# 3. RecursiveCharacterTextSplitter (structure-based hierarchy)
rec_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", " ", ""]
)
rec_chunks = rec_splitter.split_documents(docs)

# 4. Compare outputs
print("\n" + "=" * 55)
print("Comparison: CharacterTextSplitter vs RecursiveCharacterTextSplitter")
print("=" * 55)
print(f"CharacterTextSplitter chunks created: {len(char_chunks)}")
print(f"RecursiveCharacterTextSplitter chunks created: {len(rec_chunks)}")

print("\n--- Recursive Splitter Sample Chunk 1 ---")
print(f"Length: {len(rec_chunks[0].page_content)} chars")
print(rec_chunks[0].page_content)

print("\n--- Recursive Splitter Sample Chunk 2 ---")
print(f"Length: {len(rec_chunks[1].page_content)} chars")
print(rec_chunks[1].page_content)

print("\nWhy RecursiveCharacterTextSplitter respects structure:")
print("1. It uses a prioritized list of separators: ['\\n\\n', '\\n', ' ', '']")
print("2. It first attempts to keep paragraphs together ('\\n\\n').")
print("3. If a paragraph is larger than chunk_size, it splits by sentences ('\\n').")
print("4. If still larger, it splits by spaces (' ') to keep whole words intact.")
print("5. It never splits in the middle of words unless absolutely necessary,")
print("   unlike basic splitters that cause awkward sentence cutoffs.")
