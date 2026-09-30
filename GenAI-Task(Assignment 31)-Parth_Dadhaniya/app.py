# Streamlit App: Conversational PDF Q&A Chatbot (Task 10)
# Student: Parth Dadhaniya

import os
import tempfile
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, AIMessage

from config import get_llm
from part2_vector_store import get_embeddings, get_vectorstore
from part3_part4_rag_chain import prompt, trim_history

st.set_page_config(page_title="PDF Chatbot", page_icon="📄")

# Sidebar
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Groq API Key", type="password", value=os.environ.get("GROQ_API_KEY", ""))
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    st.subheader("Upload PDF")
    uploaded = st.file_uploader("Choose a PDF file", type=["pdf"])

    if st.button("Index PDF", use_container_width=True):
        if uploaded:
            with st.spinner("Processing PDF..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded.getvalue())
                    tmp_path = tmp.name

                try:
                    loader = PyPDFLoader(tmp_path)
                    pages = loader.load()
                    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
                    chunks = splitter.split_documents(pages)

                    embeddings = get_embeddings()
                    st.session_state["db"] = Chroma.from_documents(chunks, embeddings)
                    st.session_state["pdf_name"] = uploaded.name
                    st.session_state["history"] = []
                    st.session_state["messages"] = []
                    st.success(f"Loaded {len(chunks)} chunks from {uploaded.name}")
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)

    if st.button("Reset Chat", use_container_width=True):
        st.session_state["history"] = []
        st.session_state["messages"] = []
        st.rerun()


# Main Chat
st.title("📄 Conversational PDF Q&A Chatbot")
st.write("Ask questions from your PDF documents with conversational history.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "history" not in st.session_state:
    st.session_state["history"] = []
if "db" not in st.session_state:
    st.session_state["db"] = get_vectorstore()

# Show message history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "sources" in msg and msg["sources"]:
            with st.expander("View Source Chunks"):
                for s in msg["sources"]:
                    st.text(s)

# Handle user query
user_query = st.chat_input("Ask a question about the PDF...")
if user_query:
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            retriever = st.session_state["db"].as_retriever(search_kwargs={"k": 2})
            docs = retriever.invoke(user_query)
            context = "\n\n".join([d.page_content.strip() for d in docs])

            trimmed = trim_history(st.session_state["history"], max_messages=4)
            llm = get_llm()
            chain = prompt | llm

            res = chain.invoke({
                "context": context,
                "chat_history": trimmed,
                "question": user_query
            })
            answer = res.content
            sources = [d.page_content.strip() for d in docs]

            st.write(answer)
            with st.expander("View Source Chunks"):
                for s in sources:
                    st.text(s)

            st.session_state["history"].append(HumanMessage(content=user_query))
            st.session_state["history"].append(AIMessage(content=answer))
            st.session_state["messages"].append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })
