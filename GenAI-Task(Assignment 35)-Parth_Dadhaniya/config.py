# config.py - LLM Setup for Math Agent
# Student: Parth Dadhaniya

import os
from dotenv import load_dotenv

load_dotenv()


def get_llm():
    """Loads ChatGroq or ChatOpenAI if API keys exist, else returns None for offline student execution."""
    groq_key = os.getenv("GROQ_API_KEY", "").strip()
    if groq_key:
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(model_name="qwen/qwen3.8-27b", groq_api_key=groq_key, temperature=0.0)
        except Exception:
            pass

    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    if openai_key:
        try:
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_key, temperature=0.0)
        except Exception:
            pass

    return None
