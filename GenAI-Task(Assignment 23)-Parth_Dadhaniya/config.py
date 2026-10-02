# config.py - environment setup and tiktoken fix
# Parth Dadhaniya

import os
import sys
import types
import warnings

from pathlib import Path
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Reconfigure console output to UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Load environment variables (.env)
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR.parent / ".env")

# Set working directory to assignment folder so relative paths (data/...) always resolve
os.chdir(BASE_DIR)

# fix for tiktoken dll lock on windows if needed
try:
    import tiktoken
except Exception:
    dummy = types.ModuleType("tiktoken")
    dummy.Encoding = type("Encoding", (), {
        "encode": lambda s, text, *a, **k: text.split(),
        "decode": lambda s, tokens, *a, **k: " ".join(tokens)
    })
    dummy.get_encoding = lambda name: dummy.Encoding()
    dummy.encoding_for_model = lambda name: dummy.Encoding()
    sys.modules["tiktoken"] = dummy

_cached_llm_type = None

def get_llm(temperature=0):
    """
    Returns an active Chat LLM.
    Tries OpenAI first. If OpenAI has no remaining credits (429),
    falls back to Groq.
    """
    global _cached_llm_type

    if _cached_llm_type == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
    elif _cached_llm_type == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model_name="qwen/qwen3.8-27b", temperature=temperature)
    elif _cached_llm_type == "none":
        return None

    # 1. Try OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key and openai_key.startswith("sk-"):
        try:
            from langchain_openai import ChatOpenAI
            test_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
            test_llm.invoke("Hi")
            _cached_llm_type = "openai"
            return test_llm
        except Exception:
            pass

    # 2. Try Groq fallback
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        try:
            from langchain_groq import ChatGroq
            test_llm = ChatGroq(model_name="qwen/qwen3.8-27b", temperature=temperature)
            test_llm.invoke("Hi")
            _cached_llm_type = "groq"
            return test_llm
        except Exception:
            pass

    _cached_llm_type = "none"
    return None

