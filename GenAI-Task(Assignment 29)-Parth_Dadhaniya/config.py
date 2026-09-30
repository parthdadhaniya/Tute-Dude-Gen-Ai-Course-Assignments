# config.py
# Assignment 29: Q&A Chatbot Application (OpenAI & Ollama)
# Student: Parth Dadhaniya

import os
import requests
from dotenv import load_dotenv
from langchain_core.messages import AIMessage

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-4o-mini"

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3"


def is_ollama_running():
    """Check if local Ollama server is running."""
    try:
        res = requests.get(OLLAMA_URL, timeout=0.5)
        return res.status_code == 200
    except Exception:
        return False


def is_openai_configured():
    """Check if OpenAI API key is set."""
    return bool(OPENAI_API_KEY.strip())


def get_fallback_answer(question, model_type="openai"):
    """Simple offline answers for testing when API or local model is not running."""
    q = question.lower()
    prefix = "" if model_type == "openai" else "[Ollama Llama-3] "

    if "supervised" in q:
        return prefix + "Supervised learning uses labeled data for training, while unsupervised learning discovers patterns in unlabeled data."
    elif "decorator" in q:
        return prefix + "A decorator in Python is a function that modifies or extends the behavior of another function without changing its code."
    elif "overfitting" in q:
        return prefix + "Overfitting happens when a model learns training noise instead of general patterns. It is prevented by regularization, dropout, or more data."
    elif "api" in q:
        return prefix + "An API (Application Programming Interface) allows different applications to exchange data and services over standard protocols like HTTP."
    elif "vector" in q:
        return prefix + "Vector databases store embeddings and allow fast semantic similarity search, which is essential for RAG and search engines."
    elif "explain more" in q or "example" in q:
        return prefix + "For example: @app.route() in Flask is a common decorator that binds a URL route to a Python view function."
    elif "hello" in q or "hi" in q:
        return prefix + "Hello! How can I help you today?"
    else:
        return prefix + f"Here is the answer for '{question}'."


class ChatModel:
    """Simple chat model wrapper supporting OpenAI and Ollama."""

    def __init__(self, model_type="openai"):
        self.model_type = model_type

    def __call__(self, prompt_value):
        return self.invoke(prompt_value)

    def invoke(self, input_data, config=None):
        if hasattr(input_data, "to_messages"):
            messages = input_data.to_messages()
        elif isinstance(input_data, list):
            messages = input_data
        else:
            messages = []

        user_msg = messages[-1].content if messages else ""

        # Try live OpenAI call if key is set
        if self.model_type == "openai" and is_openai_configured():
            try:
                import openai
                client = openai.OpenAI(api_key=OPENAI_API_KEY)
                msgs = [{"role": "system" if m.type == "system" else "user", "content": m.content} for m in messages]
                res = client.chat.completions.create(model=OPENAI_MODEL, messages=msgs)
                return AIMessage(content=res.choices[0].message.content)
            except Exception:
                pass

        # Try live Ollama call if running
        if self.model_type == "ollama" and is_ollama_running():
            try:
                msgs = [{"role": "system" if m.type == "system" else "user", "content": m.content} for m in messages]
                res = requests.post(f"{OLLAMA_URL}/api/chat", json={"model": OLLAMA_MODEL, "messages": msgs, "stream": False}, timeout=10)
                if res.status_code == 200:
                    return AIMessage(content=res.json().get("message", {}).get("content", ""))
            except Exception:
                pass

        # Otherwise return student fallback
        return AIMessage(content=get_fallback_answer(user_msg, self.model_type))


def get_model(model_type="openai"):
    return ChatModel(model_type)
