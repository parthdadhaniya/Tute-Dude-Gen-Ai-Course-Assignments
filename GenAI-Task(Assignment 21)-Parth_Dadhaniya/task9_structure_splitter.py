# Task 9: Document Structure-Based Splitting
# Author: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("=" * 60)
print("Part A: Markdown Structure-Based Splitting")
print("=" * 60)

# 1. Read structured markdown file
with open("data/handbook.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

# Define headers to track
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3")
]

# MarkdownHeaderTextSplitter preserves document outline in metadata
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_chunks = md_splitter.split_text(markdown_content)

print(f"Total Markdown Chunks: {len(md_chunks)}")
for i, chunk in enumerate(md_chunks, 1):
    print(f"\nChunk {i}:")
    print("Metadata (Section Hierarchy):", chunk.metadata)
    print("Content:", chunk.page_content.strip())

print("\n" + "=" * 60)
print("Part B: PDF Page-Preserving Structure Splitting")
print("=" * 60)

# 2. PDF page-based splitting preserves page numbers in metadata
pdf_loader = PyPDFLoader("data/sample.pdf")
pdf_pages = pdf_loader.load()

# Split large pages further while keeping page metadata
pdf_text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
pdf_chunks = pdf_text_splitter.split_documents(pdf_pages)

print(f"Total PDF Page-Aware Chunks: {len(pdf_chunks)}")
for i, chunk in enumerate(pdf_chunks[:2], 1):
    print(f"\nPDF Chunk {i}:")
    print("Source Metadata:", chunk.metadata)
    print("Content Preview:", chunk.page_content[:120].strip(), "...")

print("\nKey Takeaway:")
print("- Markdown splitter preserves section headers as queryable metadata.")
print("- PDF loader preserves source page numbers, enabling exact page citations.")
