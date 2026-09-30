# Streamlit Web UI for Conversational Document RAG Chatbot
# Student: Parth Dadhaniya

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from part3_part4_rag_chain import create_rag_prompt, format_docs, trim_history
from part2_vector_store import get_retriever
from config import get_chat_model

st.set_page_config(page_title="Document RAG Chatbot", page_icon="📚", layout="centered")

st.title("📚 Conversational Document RAG Assistant")
st.caption("Assignment 28 | Student: Parth Dadhaniya | TuteDude GenAI Course")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    max_turns = st.slider("Max History Turns (Sliding Window)", min_value=1, max_value=6, value=3)
    k_chunks = st.slider("Retrieved Chunks (k)", min_value=1, max_value=4, value=2)

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.rag_history = []
        st.rerun()

    st.markdown("---")
    st.markdown("**Dataset Information:**")
    st.write("- Document: `company_policy.txt`")
    st.write("- Vector Store: `ChromaDB` (384-dim MiniLM)")

# Initialize session state for chat history
if "rag_history" not in st.session_state:
    st.session_state.rag_history = []

# Display conversation
for msg in st.session_state.rag_history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# User Chat Input
user_question = st.chat_input("Ask a question about company policies...")
if user_question:
    # Display user query
    with st.chat_message("user"):
        st.write(user_question)

    # 1. Retrieve document context
    retriever = get_retriever(k=k_chunks)
    docs = retriever.invoke(user_question)
    context = format_docs(docs)

    # 2. Trim chat history
    active_history = trim_history(st.session_state.rag_history, max_turns=max_turns)

    # 3. Call RAG chain
    model = get_chat_model()
    prompt = create_rag_prompt()
    chain = prompt | model

    with st.chat_message("assistant"):
        with st.spinner("Searching documents & generating answer..."):
            response = chain.invoke({
                "context": context,
                "chat_history": active_history,
                "question": user_question
            })
            answer = response.content
            st.write(answer)

            # Display source chunks
            with st.expander("📄 View Retrieved Document Chunks"):
                for idx, doc in enumerate(docs, 1):
                    st.markdown(f"**Chunk {idx}:**")
                    st.text(doc.page_content.strip())

    # Save to history
    st.session_state.rag_history.append(HumanMessage(content=user_question))
    st.session_state.rag_history.append(AIMessage(content=answer))
