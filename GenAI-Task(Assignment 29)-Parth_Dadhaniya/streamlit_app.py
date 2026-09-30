# Streamlit Web UI for Unified Q&A Chatbot (Task 8)
# Student: Parth Dadhaniya

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from part3_unified_app import get_answer
from config import is_openai_configured, is_ollama_running, OPENAI_MODEL, OLLAMA_MODEL

st.set_page_config(page_title="Q&A Chatbot (OpenAI & Ollama)", page_icon="🤖", layout="centered")

st.title("🤖 Unified Q&A Chatbot")
st.caption("Assignment 29 | Student: Parth Dadhaniya | TuteDude GenAI Course")

# Sidebar for Model Selection and Status
with st.sidebar:
    st.header("⚙️ Model Selection")
    model_choice = st.radio(
        "Choose LLM Engine:",
        ["OpenAI (Cloud)", "Ollama (Local Llama 3)"]
    )
    selected_type = "openai" if "OpenAI" in model_choice else "ollama"

    st.markdown("---")
    st.markdown("**System Status:**")

    openai_ok = is_openai_configured()
    st.write(f"- OpenAI ({OPENAI_MODEL}): {'🟢 Configured' if openai_ok else '🟡 Offline Mode'}")

    ollama_ok = is_ollama_running()
    st.write(f"- Ollama ({OLLAMA_MODEL}): {'🟢 Connected' if ollama_ok else '🟡 Offline Mode'}")

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous conversation messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "model" in msg:
            st.caption(f"Model: {msg['model']}")

# User Input
user_question = st.chat_input("Ask any technical or general question...")
if user_question:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.chat_history.append({"role": "user", "content": user_question})

    # Generate answer from selected model
    with st.chat_message("assistant"):
        with st.spinner(f"Generating answer with {model_choice}..."):
            answer = get_answer(user_question, model_type=selected_type)
            st.markdown(answer)
            st.caption(f"Model: {model_choice}")

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer,
        "model": model_choice
    })
