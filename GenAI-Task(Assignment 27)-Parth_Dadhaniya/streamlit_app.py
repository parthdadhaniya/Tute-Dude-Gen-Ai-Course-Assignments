# Streamlit Web UI for Stateful Chatbot
# Student: Parth Dadhaniya

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import get_chat_model

st.set_page_config(page_title="Stateful Chatbot", page_icon="💬")

st.title("Stateful Chatbot with LangChain")
st.write("Student: Parth Dadhaniya | Assignment 27")

# Sidebar controls
max_turns = st.sidebar.slider("Max Context Turns", min_value=1, max_value=8, value=3)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# Chat input
user_input = st.chat_input("Ask a question (e.g. Explain Python lists)...")
if user_input:
    # Display user input
    with st.chat_message("user"):
        st.write(user_input)

    # Trim history to sliding window
    window = max_turns * 2
    history = st.session_state.messages[-window:] if len(st.session_state.messages) > window else st.session_state.messages

    # Call LangChain model
    model = get_chat_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful customer support assistant. Use past conversation to answer follow-up questions."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])
    chain = prompt | model

    with st.chat_message("assistant"):
        response = chain.invoke({"history": history, "question": user_input})
        st.write(response.content)

    # Append to session history
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.session_state.messages.append(AIMessage(content=response.content))
