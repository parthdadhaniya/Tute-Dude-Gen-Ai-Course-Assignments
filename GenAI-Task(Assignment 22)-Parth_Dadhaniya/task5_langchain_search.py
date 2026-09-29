# Task 5: Similarity Search with LangChain Abstraction
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load chunks
docs = TextLoader("data/notes.txt", encoding="utf-8").load()
docs.extend(CSVLoader("data/data.csv", encoding="utf-8").load())
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

# 2. Embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 3. Create Chroma vectorstore
print("Creating in-memory Chroma vector store...")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. Search using vectorstore.similarity_search
query = "What are the rules for data privacy and security?"
print(f"\nQuery: '{query}'")

results = vectorstore.similarity_search(query, k=2)

print(f"\nRetrieved {len(results)} documents:")
for i, doc in enumerate(results, 1):
    src = doc.metadata.get("source", "unknown")
    print(f"\nResult {i} (source: {src}):")
    print("Content:", doc.page_content.strip()[:140].replace("\n", " "), "...")
