# task5_simple_chain.py
# Task 5: Simple Chain (Prompt -> LLM -> Output)
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import config

print("=== Task 5: Simple Chain ===")

# prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the role of {topic} in modern AI application development in 2 sentences."
)

llm = config.get_llm()

# basic chain: Prompt -> LLM -> StrOutputParser
chain = prompt | llm | StrOutputParser()

topics = [
    "Vector Embeddings",
    "Prompt Engineering",
    "Retrieval-Augmented Generation (RAG)"
]

print("\nExecuting Simple Chain (Prompt | LLM | StrOutputParser):\n")
for i, t in enumerate(topics, 1):
    print(f"--- Topic {i}: {t} ---")
    response = chain.invoke({"topic": t})
    print(f"Response:\n{response.strip()}\n")

print("Task 5 completed successfully.")
