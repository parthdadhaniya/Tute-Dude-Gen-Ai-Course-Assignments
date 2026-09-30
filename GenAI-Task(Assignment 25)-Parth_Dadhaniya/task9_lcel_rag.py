# task9_lcel_rag.py
# Task 9: LCEL-Based RAG Pipeline
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import config
import vector_store

print("=== Task 9: LCEL-Based RAG Chain ===")

# get retriever from Chroma vector store
retriever = vector_store.get_retriever(k=2)

def format_docs(docs):
    return "\n\n".join([f"[Source: {d.metadata.get('source', 'unknown')}]\n{d.page_content.strip()}" for d in docs])

# RAG prompt
rag_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful knowledge assistant.
Answer the question using the following context. If you cannot answer based on context, state that clearly.

Context:
{context}

Question: {question}
Answer:"""
)

llm = config.get_llm()

# LCEL RAG chain:
# {"context": retriever | format_docs, "question": RunnablePassthrough()} | Prompt | LLM | Output Parser
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

queries = [
    "What is the annual leave policy according to the employee handbook?",
    "What employee departments and data fields are recorded in the CSV?",
    "What are the core capabilities of the Generative AI knowledge assistant?"
]

print("\nExecuting LCEL RAG Pipeline:\n")
for i, q in enumerate(queries, 1):
    print(f"--- Query {i}: {q} ---")
    answer = rag_chain.invoke(q)
    print(f"Answer:\n{answer.strip()}\n" + "-" * 50)

print("\nTask 9 completed successfully.")
