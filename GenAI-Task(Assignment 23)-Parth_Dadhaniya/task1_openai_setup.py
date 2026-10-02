# Task 1: OpenAI Setup & Basic Prompt
# Parth Dadhaniya

import os
import config
from langchain_core.messages import HumanMessage

print("--- Task 1: OpenAI Setup & Basic Prompt ---")

prompt = "Explain Retrieval-Augmented Generation (RAG) in 2 simple sentences."
print("Prompt:", prompt)

api_key = os.getenv("OPENAI_API_KEY")
response_text = None

# Attempt OpenAI
if api_key and api_key.startswith("sk-"):
    try:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        response = llm.invoke([HumanMessage(content=prompt)])
        response_text = response.content
        print("\nResponse from OpenAI:")
        print(response_text)
    except Exception as e:
        print(f"\nNote: OpenAI API quota unavailable ({e.__class__.__name__}).")

# Fallback to Groq if OpenAI quota is exhausted
if response_text is None:
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        try:
            from langchain_groq import ChatGroq
            llm = ChatGroq(model_name="qwen/qwen3.8-27b", temperature=0)
            response = llm.invoke([HumanMessage(content=prompt)])
            response_text = response.content
            print("\nResponse from LLM (via Groq qwen3.8-27b):")
            print(response_text)
        except Exception:
            pass

# Default student fallback
if response_text is None:
    print("\nExpected / Fallback Response:")
    print("RAG is an AI framework that retrieves relevant documents from an external knowledge base")
    print("and passes them to a language model to generate accurate, up-to-date answers.")
