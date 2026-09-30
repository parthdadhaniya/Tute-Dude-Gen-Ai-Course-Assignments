# task1_groq_setup.py
# Task 1: Groq API Setup & Basic Chat
# Student: Parth Dadhaniya

import os
import time
import warnings
warnings.filterwarnings("ignore")

import config

print("=== Task 1: Groq API Setup & Basic Chat ===")

# setup instructions
print("\n--- Setup Instructions ---")
print("1. Create an account at https://console.groq.com")
print("2. Generate an API Key under API Keys section.")
print("3. Set in your environment: $env:GROQ_API_KEY='your-key'")
print("4. Installed Python SDK: pip install groq")
print("---------------------------\n")

api_key = config.GROQ_API_KEY
print(f"Configured Model : {config.DEFAULT_MODEL}")
print(f"Groq API Key     : {'CONFIGURED (Live Cloud)' if api_key else 'NOT DETECTED (Offline local mode)'}")

# simple test prompt
test_prompt = "Explain in 2 sentences why Groq LPUs provide faster inference than traditional GPUs."
print(f"\nPrompt: {test_prompt}\n")

messages = [
    {"role": "user", "content": test_prompt}
]

start_time = time.time()
response = config.call_groq(messages, temperature=0.5)
elapsed = round(time.time() - start_time, 3)

print("--- Groq Response ---")
print(response.strip())
print(f"\nExecution Latency: {elapsed} seconds")
print("Task 1 completed successfully.")
