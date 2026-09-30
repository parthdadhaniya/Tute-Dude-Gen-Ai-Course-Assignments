# task2_chat_prompt_template.py
# Task 2: ChatPromptTemplate & Message Templates
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import config

print("=== Task 2: ChatPromptTemplate & Message Templates ===")

# chat template using system, human, and ai messages
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python and Generative AI mentor."),
    ("human", "Hi, what does a vector store do?"),
    ("ai", "A vector store indexes embeddings to enable fast similarity search across documents."),
    ("human", "{user_input}")
])

llm = config.get_llm()
chat_chain = chat_prompt | llm | StrOutputParser()

user_question = "How does FAISS compare to ChromaDB for storing embeddings?"
print(f"\nUser Question: {user_question}\n")

# inspect formatted message objects
messages = chat_prompt.format_messages(user_input=user_question)
print("--- Formatted Message Objects ---")
for m in messages:
    print(f"[{m.type.upper()}]: {m.content}")

# get model response
response = chat_chain.invoke({"user_input": user_question})
print("\n--- Model Response ---")
print(response.strip())

# comparison
print("\n" + "=" * 50)
print("--- PromptTemplate vs ChatPromptTemplate ---")
print("1. PromptTemplate:")
print("   - Produces a single flat text string.")
print("   - Used for text completion models.")
print("2. ChatPromptTemplate:")
print("   - Produces structured message objects (system, human, ai).")
print("   - Fits modern chat APIs and preserves system instructions.")
print("=" * 50)

print("\nTask 2 completed successfully.")
