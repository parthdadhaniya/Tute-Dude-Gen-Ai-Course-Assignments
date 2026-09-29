# Task 6: Contextual Compression Retriever
# Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")
import config

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

try:
    from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
    from langchain_classic.retrievers.document_compressors import EmbeddingsFilter
except ImportError:
    from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import EmbeddingsFilter

print("--- Task 6: Contextual Compression Retriever ---")

# load and chunk text
docs = TextLoader("data/knowledge_base.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings)

# base retriever returns 5 candidates
base_retriever = db.as_retriever(search_kwargs={"k": 5})

# compressor filters out low similarity chunks
compressor = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.35)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

query = "How does FAISS optimize fast vector search?"
print("Query:", query)

# compare before and after
raw_results = base_retriever.invoke(query)
compressed_results = compression_retriever.invoke(query)

print(f"\nBefore Compression: {len(raw_results)} chunks retrieved")
for i, d in enumerate(raw_results, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:90]}...")

print(f"\nAfter Compression: {len(compressed_results)} chunks kept")
for i, d in enumerate(compressed_results, 1):
    print(f"[{i}] {d.page_content.replace('\n', ' ')[:90]}...")

raw_chars = sum(len(d.page_content) for d in raw_results)
comp_chars = sum(len(d.page_content) for d in compressed_results)
saved = ((raw_chars - comp_chars) / raw_chars) * 100
print(f"\nCharacters reduced from {raw_chars} to {comp_chars} ({saved:.1f}% reduction).")
print("This cuts down prompt tokens and removes irrelevant noise.")
