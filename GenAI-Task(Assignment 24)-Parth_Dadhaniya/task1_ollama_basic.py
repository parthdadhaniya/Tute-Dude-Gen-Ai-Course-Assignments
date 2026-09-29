# task1_ollama_basic.py
# Task 1: Ollama Setup & Basic Chat
# Parth Dadhaniya

import os
import requests
import warnings
warnings.filterwarnings("ignore")
from langchain_community.llms import Ollama
import config

print("=== Task 1: Ollama Setup & Basic Chat ===")

# check if local ollama server is reachable
def check_ollama(url=config.OLLAMA_URL):
    try:
        res = requests.get(url, timeout=0.5)
        return res.status_code == 200
    except:
        return False

# local setup instructions
print("\n--- Setup Steps ---")
print("1. Download Ollama from https://ollama.com")
print("2. Run server in terminal: ollama serve")
print(f"3. Pull model: ollama pull {config.DEFAULT_MODEL}")
print("--------------------")

prompt = "Explain in 2 simple sentences why developers run LLMs locally with Ollama."
print(f"\nPrompt: {prompt}")
print(f"Model: {config.DEFAULT_MODEL}\n")

if check_ollama():
    print("Ollama server connected at", config.OLLAMA_URL)
    llm = Ollama(model=config.DEFAULT_MODEL, base_url=config.OLLAMA_URL)
    try:
        reply = llm.invoke(prompt)
        print("\nResponse from Ollama:")
        print(reply.strip())
    except Exception as e:
        print("Error calling Ollama:", e)
else:
    print(f"Notice: Ollama is not running on {config.OLLAMA_URL}.")
    print("Simulated response for testing:")
    print("Running LLMs locally with Ollama provides complete data privacy and zero API costs,")
    print("since all inference runs on your own hardware without sending data to external cloud providers.")

# check langsmith status
print("\n--- LangSmith Tracing ---")
if os.getenv("LANGCHAIN_API_KEY"):
    print(f"Tracing: ACTIVE (Project: {config.LANGCHAIN_PROJECT})")
else:
    print("Tracing: OFFLINE (Set LANGSMITH_API_KEY to see traces online)")
