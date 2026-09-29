# Task 1: OpenAI Setup & Basic Prompt
# Parth Dadhaniya

import os
import config
from langchain_core.messages import HumanMessage

print("--- Task 1: OpenAI Setup & Basic Prompt ---")

api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.startswith("sk-"):
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = "Explain Retrieval-Augmented Generation (RAG) in 2 simple sentences."
    print("Prompt:", prompt)
    
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\nResponse from OpenAI:")
    print(response.content)
else:
    print("Note: OPENAI_API_KEY is not set in environment.")
    print("Prompt: Explain Retrieval-Augmented Generation (RAG) in 2 simple sentences.")
    print("\nExpected / Fallback Response:")
    print("RAG is an AI framework that retrieves relevant documents from an external knowledge base")
    print("and passes them to a language model to generate accurate, up-to-date answers.")
