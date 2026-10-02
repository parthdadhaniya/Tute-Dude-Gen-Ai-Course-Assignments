# Streamlit ChatGroq RAG Application (Tasks 7, 8 & 10)
# Student: Parth Dadhaniya

import os
import tempfile
import streamlit as st
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, AIMessage

from config import get_chat_model
from part2_part3_rag_pipeline import get_embeddings, get_vectorstore, get_rag_prompt

st.set_page_config(page_title="ChatGroq Document RAG", page_icon="⚡", layout="wide")

# Sidebar
with st.sidebar:
    st.title("⚡ Settings")
    groq_key = st.text_input("Groq API Key", type="password", value=os.environ.get("GROQ_API_KEY", ""))
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key

    model_name = st.selectbox(
        "Choose Groq Model",
        ["qwen/qwen3.8-27b", "openai/gpt-oss-20b", "openai/gpt-oss-120b", "llama-3.1-8b-instant"],
        index=0
    )

    st.write("---")
    st.subheader("📄 Upload Document")
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

    if st.button("Index Uploaded File", use_container_width=True):
        if uploaded_file is not None:
            with st.spinner("Processing document into ChromaDB..."):
                ext = ".pdf" if uploaded_file.name.lower().endswith(".pdf") else ".txt"
                temp_dir = tempfile.gettempdir()
                tmp_path = os.path.join(temp_dir, f"rag_{uploaded_file.name}")

                try:
                    with open(tmp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())

                    if ext == ".pdf":
                        loader = PyPDFLoader(tmp_path)
                    else:
                        loader = TextLoader(tmp_path, encoding="utf-8")
                    
                    raw_docs = loader.load()
                    if not raw_docs:
                        st.warning("The uploaded file does not contain readable text.")
                    else:
                        for d in raw_docs:
                            d.metadata["source"] = uploaded_file.name

                        splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
                        chunks = splitter.split_documents(raw_docs)

                        if not chunks:
                            st.warning("Could not extract text chunks from the document.")
                        else:
                            embeddings = get_embeddings()
                            st.session_state["vectorstore"] = Chroma.from_documents(chunks, embeddings)
                            st.session_state["doc_name"] = uploaded_file.name
                            st.session_state["messages"] = []
                            st.session_state["chat_history"] = []
                            st.success(f"Indexed {len(chunks)} chunks from {uploaded_file.name}!")
                except Exception as e:
                    st.error(f"Error processing file: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        try:
                            os.remove(tmp_path)
                        except Exception:
                            pass
        else:
            st.warning("Please upload a file first.")

    if st.button("Reset to Default Handbook", use_container_width=True):
        st.session_state["vectorstore"] = get_vectorstore()
        st.session_state["doc_name"] = "ai_handbook.txt"
        st.session_state["messages"] = []
        st.session_state["chat_history"] = []
        st.info("Reset to default knowledge base.")

    if st.button("Clear Chat", use_container_width=True):
        st.session_state["messages"] = []
        st.session_state["chat_history"] = []
        st.rerun()

    active_doc = st.session_state.get("doc_name", "ai_handbook.txt (Default)")
    st.caption(f"**Active Knowledge Base:** {active_doc}")


# Main UI
st.title("⚡ Document Q&A Assistant with ChatGroq")
st.write("Fast, grounded question answering from uploaded documents using Groq LPUs and LangChain RAG.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "vectorstore" not in st.session_state:
    st.session_state["vectorstore"] = get_vectorstore()
    st.session_state["doc_name"] = "ai_handbook.txt (Default)"

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "sources" in message and message["sources"]:
            with st.expander(f"📚 Retrieved Sources ({len(message['sources'])} chunks)"):
                for i, src in enumerate(message["sources"], 1):
                    st.caption(f"**Chunk {i}** | Source: `{src['source']}`")
                    st.text(src["text"])

# Handle user input
user_question = st.chat_input("Ask a question about the document...")
if user_question:
    # Display user query
    st.session_state["messages"].append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.write(user_question)

    # Retrieval and answer generation
    with st.chat_message("assistant"):
        with st.spinner("Searching document and querying Groq..."):
            vs = st.session_state.get("vectorstore")
            if vs is None:
                st.warning("No document indexed yet. Please upload a document or click 'Reset to Default Handbook'.")
            else:
                try:
                    retriever = vs.as_retriever(search_kwargs={"k": 2})
                    retrieved_docs = retriever.invoke(user_question)
                    context = "\n\n".join([d.page_content.strip() for d in retrieved_docs])

                    llm = get_chat_model(model_name=model_name)
                    prompt = get_rag_prompt()
                    chain = prompt | llm

                    response = chain.invoke({
                        "context": context,
                        "chat_history": st.session_state["chat_history"],
                        "question": user_question
                    })
                    answer = response.content

                    sources = [
                        {"source": os.path.basename(d.metadata.get("source", "doc")), "text": d.page_content.strip()}
                        for d in retrieved_docs
                    ]

                    st.write(answer)
                    if sources:
                        with st.expander(f"📚 Retrieved Sources ({len(sources)} chunks)"):
                            for i, src in enumerate(sources, 1):
                                st.caption(f"**Chunk {i}** | Source: `{src['source']}`")
                                st.text(src["text"])

                    # Save state
                    st.session_state["chat_history"].append(HumanMessage(content=user_question))
                    st.session_state["chat_history"].append(AIMessage(content=answer))
                    st.session_state["messages"].append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })
                except Exception as e:
                    st.error(f"Error generating answer: {e}")
