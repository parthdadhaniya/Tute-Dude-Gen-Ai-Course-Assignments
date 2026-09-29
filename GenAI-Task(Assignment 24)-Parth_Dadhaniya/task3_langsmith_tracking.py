# task3_langsmith_tracking.py
# Task 3: Tracking Model Response using LangSmith
# Parth Dadhaniya

import os
import time
import requests
import warnings
warnings.filterwarnings("ignore")
from langsmith import traceable
from langchain_community.llms import Ollama
import config

print("=== Task 3: Tracking Model Responses with LangSmith ===")

def check_ollama():
    try:
        return requests.get(config.OLLAMA_URL, timeout=0.5).status_code == 200
    except:
        return False

print(f"Project Name   : {config.LANGCHAIN_PROJECT}")
print(f"Tracing Active : {os.getenv('LANGCHAIN_TRACING_V2', 'false')}")
print(f"API Key Present: {'Yes' if os.getenv('LANGCHAIN_API_KEY') else 'No (Running in local test mode)'}")

# function tracked by LangSmith
@traceable(name="ollama_chat_trace", tags=["ollama", "assignment24", "parth_dadhaniya"])
def run_tracked_prompt(user_prompt, model_name=config.DEFAULT_MODEL):
    t0 = time.time()
    
    if check_ollama():
        llm = Ollama(model=model_name, base_url=config.OLLAMA_URL)
        response = llm.invoke(user_prompt).strip()
    else:
        # local simulated response when offline
        response = (
            f"This is a tracked response from {model_name}. "
            "LangSmith logs the prompt text, output text, and execution latency."
        )
    
    elapsed = round(time.time() - t0, 3)
    return {
        "prompt": user_prompt,
        "response": response,
        "latency": elapsed,
        "model": model_name
    }

# test sample prompts
test_queries = [
    "What are the benefits of running LLMs locally?",
    "Why is monitoring with LangSmith useful in production?"
]

print("\n--- Running Tracked Prompts ---")
for i, q in enumerate(test_queries, 1):
    print(f"\nQuery {i}: {q}")
    result = run_tracked_prompt(q)
    print(f"Model  : {result['model']}")
    print(f"Latency: {result['latency']}s")
    print(f"Output : {result['response']}")

print("\n--- LangSmith Tracking Details ---")
print("1. Go to https://smith.langchain.com")
print(f"2. Open project: {config.LANGCHAIN_PROJECT}")
print("3. Each call appears under 'Runs' with run name 'ollama_chat_trace'.")
print("4. Click the run to view input prompt, generated output, latency, and tokens.")

print("\n--- Google Drive Submission Steps ---")
print("1. Open the run in LangSmith dashboard.")
print("2. Take a screenshot showing inputs, outputs, and latency.")
print("3. Upload the screenshot to Google Drive.")
print("4. Set share settings to 'Anyone with link can view'.")
print("5. Paste the link into the assignment submission.")
