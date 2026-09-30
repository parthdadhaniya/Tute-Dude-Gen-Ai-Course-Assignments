# task6_conditional_chain.py
# Task 6: Conditional Chain (Routing: Retrieval vs Direct LLM)
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
import config
import vector_store

print("=== Task 6: Conditional Chain ===")

llm = config.get_llm()
retriever = vector_store.get_retriever(k=2)

# helper to join retrieved docs
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

# branch 1: RAG branch for factual questions
rag_prompt = PromptTemplate.from_template(
    """Answer the question using the provided context:
Context: {context}

Question: {question}
Answer:"""
)
rag_branch = (
    {"context": (lambda x: x["question"]) | retriever | format_docs, "question": lambda x: x["question"]}
    | rag_prompt
    | llm
    | StrOutputParser()
)

# branch 2: Direct LLM branch for casual conversation
direct_prompt = PromptTemplate.from_template(
    """Respond politely and conversationally:
User: {question}
Assistant:"""
)
direct_branch = direct_prompt | llm | StrOutputParser()

# condition to check if question requires document retrieval
def is_factual(inputs):
    text = inputs["question"].lower()
    keywords = ["policy", "leave", "handbook", "csv", "salary", "employee", "what is", "document"]
    return any(w in text for w in keywords)

# build conditional chain
conditional_chain = RunnableBranch(
    (is_factual, rag_branch),
    direct_branch
)

queries = [
    {"question": "What is the company leave policy according to the handbook?", "type": "Factual (Doc lookup)"},
    {"question": "Hello, good morning! How are you doing today?", "type": "Conversational (Direct LLM)"},
    {"question": "What columns and employee roles are recorded in the CSV?", "type": "Factual (Doc lookup)"},
    {"question": "Can you give me a friendly welcome greeting?", "type": "Conversational (Direct LLM)"}
]

print("\nRunning Conditional Chain:\n")
for item in queries:
    q = item["question"]
    routed = "Retrieval Branch (RAG)" if is_factual({"question": q}) else "Direct LLM Branch"
    print(f"Question : {q}")
    print(f"Category : {item['type']}")
    print(f"Routed To: {routed}")
    ans = conditional_chain.invoke({"question": q})
    print(f"Output   : {ans.strip()}\n" + "-" * 50)

print("\nTask 6 completed successfully.")
