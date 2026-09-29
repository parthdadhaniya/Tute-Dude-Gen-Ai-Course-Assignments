# Task 9: FAISS vs ChromaDB Comparison
# Parth Dadhaniya

print("Task 9: FAISS vs ChromaDB Comparison\n")

print("1. In-Memory vs Persistent Storage:")
print("- FAISS: Loads vectors in RAM for fast search, but does not save automatically to disk")
print("  unless you call save_local(). When the program stops, memory is cleared.")
print("- ChromaDB: Automatically persists embeddings, text chunks, and metadata to disk using")
print("  SQLite/DuckDB. It survives program restarts without manual saving.\n")

print("2. When to Use FAISS?")
print("- For very large vector datasets (millions or billions of items) needing GPU acceleration.")
print("- For quick in-memory lookups during a temporary script or session.")
print("- When you only need raw distance search without database features.\n")

print("3. When to Use ChromaDB?")
print("- For complete RAG applications needing persistent local storage.")
print("- When you need to filter results by metadata (like department, date, or author).")
print("- When you want built-in collection management (add, update, delete documents easily).")
