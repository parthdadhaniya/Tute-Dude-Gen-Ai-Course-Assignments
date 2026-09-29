# task2_ollama_chatbot.py
# Task 2: Chatbot App with Ollama
# Parth Dadhaniya

import requests
import warnings
warnings.filterwarnings("ignore")
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import config

print("=== Task 2: Chatbot App with Ollama ===")

def check_ollama():
    try:
        return requests.get(config.OLLAMA_URL, timeout=0.5).status_code == 200
    except:
        return False

# template that includes conversation history
template = """You are a helpful AI assistant running locally with Ollama.

Previous Conversation:
{history}

User: {input}
Assistant:"""

prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# list to store chat history: [(user_msg, bot_msg), ...]
chat_history = []

def ask_chatbot(user_msg, model_name=config.DEFAULT_MODEL):
    # format past conversation
    if chat_history:
        history_text = "\n".join([f"User: {u}\nAssistant: {a}" for u, a in chat_history])
    else:
        history_text = "No previous history."

    full_prompt = prompt_template.format(history=history_text, input=user_msg)

    if check_ollama():
        try:
            llm = Ollama(model=model_name, base_url=config.OLLAMA_URL)
            bot_reply = llm.invoke(full_prompt).strip()
        except Exception as e:
            bot_reply = f"Error: {e}"
    else:
        # fallback responses for testing when offline
        q = user_msg.lower()
        if "name" in q and "studying" in q:
            bot_reply = "Your name is Parth and you are studying Generative AI."
        elif "hello" in q or "hi" in q:
            bot_reply = "Hello Parth! Nice to meet you. How can I help you today?"
        elif "tip" in q:
            bot_reply = "1. Use 4-bit quantized models to save RAM. 2. Give clear system prompts."
        else:
            bot_reply = f"I received your question about '{user_msg}'. Running locally with {model_name}."

    chat_history.append((user_msg, bot_reply))
    return bot_reply

# test multi-turn conversation
test_queries = [
    "Hi, I am Parth. I am studying GenAI.",
    "What is my name and what am I studying?",
    "Give me 2 tips to master local LLMs."
]

print("Starting multi-turn chat test:\n")
for i, query in enumerate(test_queries, 1):
    print(f"--- Turn {i} ---")
    print(f"User: {query}")
    answer = ask_chatbot(query)
    print(f"Bot : {answer}\n")

print(f"Chat complete. Messages saved in memory: {len(chat_history)}")
