# task3_task4_groq_rag.py
# Tasks 3 & 4: Groq-Based RAG Pipeline & Structured Prompt Template
# Student: Parth Dadhaniya

import time
import warnings
warnings.filterwarnings("ignore")

import config
import vector_store

print("=== Tasks 3 & 4: Groq + RAG Pipeline ===")

# Task 4: Structured Prompt Template for Groq RAG
RAG_SYSTEM_PROMPT = (
    "You are a strict factual knowledge assistant. "
    "Answer the user question using ONLY the provided context chunks. "
    "Do not extrapolate or assume facts not present in the context. "
    "Always cite the source document name."
)

def format_rag_prompt(context_chunks, question: str) -> str:
    """
    Constructs the structured RAG prompt containing system rules,
    retrieved document text, and the user question.
    """
    context_str = "\n\n".join([f"[Source: {c['source']}]\n{c['content']}" for c in context_chunks])
    return f"Context:\n{context_str}\n\nQuestion: {question}\nAnswer:"

# Task 3: Full RAG Pipeline
def groq_rag_pipeline(query: str, k: int = 2) -> dict:
    """
    Retrieves document chunks, formats the RAG prompt, calls Groq,
    and returns grounded response with latency metrics and sources.
    """
    t0 = time.time()
    
    # 1. retrieve relevant chunks
    chunks = vector_store.get_relevant_chunks(query, k=k)
    
    # 2. build structured prompt
    prompt_content = format_rag_prompt(chunks, query)
    
    # 3. prepare messages for Groq
    messages = [
        {"role": "system", "content": RAG_SYSTEM_PROMPT},
        {"role": "user", "content": prompt_content}
    ]
    
    # 4. invoke model
    answer = config.call_groq(messages, temperature=0.2)
    elapsed = round(time.time() - t0, 3)
    
    sources = list(set([c["source"] for c in chunks]))
    return {
        "query": query,
        "answer": answer.strip(),
        "sources": sources,
        "latency_seconds": elapsed,
        "chunks_used": len(chunks)
    }

# test RAG with multiple queries
test_rag_queries = [
    "What is the annual leave policy according to the employee handbook?",
    "What employee departments and data fields are recorded in the CSV?",
    "What are the core capabilities of the Generative AI knowledge assistant?"
]

print("\nExecuting Groq RAG Pipeline:\n")
for i, q in enumerate(test_rag_queries, 1):
    print(f"--- RAG Query {i} ---")
    print(f"User Query : {q}")
    
    res = groq_rag_pipeline(q)
    
    print(f"Answer     : {res['answer']}")
    print(f"Sources    : {res['sources']}")
    print(f"Latency    : {res['latency_seconds']}s\n" + "-" * 50)

print("Tasks 3 & 4 completed successfully.")
