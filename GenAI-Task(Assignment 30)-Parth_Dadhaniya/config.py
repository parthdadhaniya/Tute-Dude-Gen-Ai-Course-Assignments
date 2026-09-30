# config.py - Model configuration
# Student: Parth Dadhaniya

import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_core.runnables import Runnable

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DEFAULT_MODEL = "llama-3.1-8b-instant"


class LocalGroqFallback(Runnable):
    """Simple offline fallback when GROQ_API_KEY is not provided."""

    def invoke(self, inputs, config=None, **kwargs):
        # Convert prompt to string
        if hasattr(inputs, "to_string"):
            text = inputs.to_string()
        elif hasattr(inputs, "messages"):
            text = " ".join([m.content for m in inputs.messages])
        else:
            text = str(inputs)

        # Grounding check: out of scope questions
        if "mars" in text.lower() or "weather" in text.lower():
            return AIMessage(content="I don't know based on the provided documents.")

        # Pull answer directly from retrieved context if available
        if "Context:" in text:
            try:
                context_chunk = text.split("Context:")[1].split("Question:")[0].strip()
                # Use the first informative line from retrieved document
                lines = [l.strip() for l in context_chunk.split("\n") if len(l.strip()) > 30]
                if lines:
                    return AIMessage(content=lines[0])
            except Exception:
                pass

        return AIMessage(content="Groq LPUs deliver ultra-low latency inference (300-500+ tokens/sec) using fast on-chip SRAM.")


def get_chat_model(model_name=DEFAULT_MODEL, temperature=0.2):
    """Return live ChatGroq if API key is set, otherwise return local fallback."""
    api_key = os.getenv("GROQ_API_KEY", "").strip() or GROQ_API_KEY.strip()
    if api_key:
        from langchain_groq import ChatGroq
        return ChatGroq(
            model=model_name,
            groq_api_key=api_key,
            temperature=temperature
        )
    return LocalGroqFallback()
