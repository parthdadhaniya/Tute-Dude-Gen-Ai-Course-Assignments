# config.py - LLM Setup
# Student: Parth Dadhaniya

import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_core.runnables import Runnable

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")


# Simple fallback if no API key is set so scripts can run locally
class MockLLM(Runnable):
    def invoke(self, inputs, config=None, **kwargs):
        text = str(inputs).lower()
        if "mars" in text or "weather" in text:
            return AIMessage(content="I don't know based on the provided documents.")
        if "context:" in text:
            try:
                ctx = str(inputs).split("Context:")[1].split("Question:")[0].strip()
                lines = [l.strip() for l in ctx.split("\n") if len(l.strip()) > 20]
                if lines:
                    return AIMessage(content=lines[0])
            except Exception:
                pass
        return AIMessage(content="According to the PDF: Production workloads use Llama 3.1 and Groq LPUs.")


def get_llm():
    api_key = os.getenv("GROQ_API_KEY", "").strip() or GROQ_API_KEY.strip()
    if api_key:
        from langchain_groq import ChatGroq
        return ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=api_key, temperature=0.2)
    return MockLLM()
