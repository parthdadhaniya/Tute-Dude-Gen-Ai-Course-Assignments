# config.py
# Parth Dadhaniya

import os

# ollama local settings
OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3"

# langsmith tracking settings
LANGCHAIN_PROJECT = "ollama-chatbot-assignment24"
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "")

# enable tracing when api key is provided
if LANGSMITH_API_KEY:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = LANGSMITH_API_KEY
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
else:
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
