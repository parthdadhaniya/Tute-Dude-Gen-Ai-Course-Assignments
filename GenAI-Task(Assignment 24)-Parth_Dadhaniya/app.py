# app.py - Streamlit Chatbot with Ollama & LangSmith Tracking
# Parth Dadhaniya

import os
import time
import requests
import streamlit as st
from langchain_community.llms import Ollama
import config

st.set_page_config(page_title="Ollama Chatbot - Parth Dadhaniya", layout="wide")

st.title("Ollama Local Chatbot")
st.write("Student: Parth Dadhaniya | Course: Generative AI")

# sidebar configuration
st.sidebar.header("Settings")
model_choice = st.sidebar.selectbox("Choose Model", ["llama3", "mistral", "gemma:2b"], index=0)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)

def check_ollama():
    try:
        return requests.get(config.OLLAMA_URL, timeout=0.5).status_code == 200
    except:
        return False

is_live = check_ollama()
if is_live:
    st.sidebar.success("Ollama: Connected (localhost:11434)")
else:
    st.sidebar.warning("Ollama: Offline (Demo Mode)")

if os.getenv("LANGCHAIN_API_KEY"):
    st.sidebar.success(f"LangSmith: Active ({config.LANGCHAIN_PROJECT})")
else:
    st.sidebar.info("LangSmith: Offline (Local Mode)")

with st.sidebar.expander("Setup Instructions"):
    st.write("1. Install Ollama from ollama.com")
    st.write("2. Run: ollama serve")
    st.write(f"3. Run: ollama pull {model_choice}")

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# initialize messages list
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your local Ollama assistant. How can I help you today?"}
    ]

# display conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input
user_input = st.chat_input("Type your message here...")

if user_input:
    # add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # generate response
    with st.chat_message("assistant"):
        start_time = time.time()
        
        if is_live:
            try:
                llm = Ollama(model=model_choice, temperature=temperature, base_url=config.OLLAMA_URL)
                past_dialogue = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages[-4:]])
                prompt = f"Previous conversation:\n{past_dialogue}\n\nRespond as Assistant:"
                reply = llm.invoke(prompt).strip()
            except Exception as e:
                reply = f"Ollama error: {e}"
        else:
            time.sleep(0.3)
            q = user_input.lower()
            if "name" in q:
                reply = f"I am a chatbot powered by local {model_choice} model via Ollama."
            elif "parth" in q:
                reply = "Hello Parth! Your local Generative AI setup is working properly."
            elif "langsmith" in q:
                reply = "LangSmith tracks every prompt, output response, latency, and token metrics."
            else:
                reply = f"You asked: '{user_input}'. Running locally with {model_choice} ensures total privacy."

        elapsed = round(time.time() - start_time, 2)
        st.write(reply)
        st.caption(f"Model: {model_choice} | Latency: {elapsed}s")

    st.session_state.messages.append({"role": "assistant", "content": reply})
