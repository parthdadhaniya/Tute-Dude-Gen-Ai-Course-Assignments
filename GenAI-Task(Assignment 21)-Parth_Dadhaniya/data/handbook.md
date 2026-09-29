# Enterprise AI Assistant Handbook

## 1. Overview
The Enterprise AI Assistant is built to index company knowledge and provide verifiable answers with source citations.

## 2. Document Ingestion Rules
### 2.1 File Formats
We support plain text files, CSV tables, PDF reports, and web documentation.

### 2.2 Metadata Standards
Every loaded document must retain metadata including source file path, author, and timestamp.

## 3. Chunking Guidelines
### 3.1 Chunk Size
Standard chunk size should be between 300 and 500 characters for fine-grained retrieval.

### 3.2 Chunk Overlap
A 10% to 20% overlap prevents loss of context at chunk boundaries.