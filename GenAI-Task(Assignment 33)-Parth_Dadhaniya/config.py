# config.py - LLM Setup
# Student: Parth Dadhaniya

import os
from dotenv import load_dotenv
from langchain_core.language_models.fake import FakeListLLM

load_dotenv()


def get_llm():
    """Loads Groq or OpenAI model if API keys exist, else returns FakeListLLM for local running."""
    groq_key = os.getenv("GROQ_API_KEY", "").strip()
    if groq_key:
        from langchain_groq import ChatGroq
        return ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_key, temperature=0.0)

    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    if openai_key:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_key, temperature=0.0)

    return FakeListLLM(responses=["SELECT * FROM employees"])
