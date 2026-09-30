# app.py - Streamlit PDF Query RAG with AstraDB & Session State
# Student: Parth Dadhaniya

import os
import streamlit as st
from config import (
    ASTRA_DB_APPLICATION_TOKEN,
    ASTRA_DB_API_ENDPOINT,
    ASTRA_DB_COLLECTION,
    get_astradb_vectorstore,
    get_embeddings,
    get_rag_llm
)
from part2_pdf_processing import load_pdf_document, split_pdf_pages, store_in_astradb
from part3_rag_pipeline import build_rag_pipeline, query_rag_system

# Page configuration
st.set_page_config(
    page_title="AstraDB PDF Query RAG",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource(show_spinner="Connecting to AstraDB and loading document...")
def initialize_system():
    """Initializes embeddings, PDF ingestion, and AstraDB vector store once per session."""
    pages = load_pdf_document()
    chunks = split_pdf_pages(pages, chunk_size=350, chunk_overlap=50)
    store, mode = store_in_astradb(chunks)
    rag_chain, retriever, _ = build_rag_pipeline()
    return {
        "pages_count": len(pages),
        "chunks_count": len(chunks),
        "mode": mode,
        "rag_chain": rag_chain,
        "retriever": retriever
    }


def main():
    st.title("📚 AstraDB Cloud PDF Query RAG")
    st.caption("Enterprise RAG System with DataStax AstraDB & Session State | Student: Parth Dadhaniya")

    # Initialize RAG system
    system_data = initialize_system()

    # Sidebar: Database & Document Info
    with st.sidebar:
        st.header("⚙️ System Status")
        st.write(f"**Vector Store:** `{system_data['mode']}`")
        st.write(f"**Target Collection:** `{ASTRA_DB_COLLECTION}`")
        has_token = bool(ASTRA_DB_APPLICATION_TOKEN and ASTRA_DB_API_ENDPOINT)
        if has_token:
            st.success("🟢 Live AstraDB Cloud Connected")
        else:
            st.info("🔵 Local AstraDB Store Active")

        st.divider()
        st.subheader("📄 Document Details")
        st.write(f"**Document:** `enterprise_ai_manual.pdf`")
        st.write(f"**Total Pages:** {system_data['pages_count']}")
        st.write(f"**Indexed Chunks:** {system_data['chunks_count']}")

        st.divider()
        st.subheader("💡 Quick Sample Questions")
        samples = [
            "What models are approved for production workloads?",
            "What is the real-time latency requirement?",
            "Which vector database is mandated?",
            "What is the recipe for baking chocolate cookies?"
        ]

        for sample in samples:
            if st.button(sample, use_container_width=True):
                st.session_state["user_query_input"] = sample

        st.divider()
        if st.button("🗑️ Clear Conversation History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    # Session State: Maintain Conversation History
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I am your Enterprise AI Assistant connected to DataStax AstraDB. Ask me any question from the Enterprise AI Policy manual."
            }
        ]

    # Render previous conversation history from session state
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "sources" in msg and msg["sources"]:
                with st.expander("🔍 View Retrieved Sources"):
                    for idx, src in enumerate(msg["sources"], 1):
                        st.markdown(f"**Source [{idx}] (Page {src['page']}):**")
                        st.caption(src["snippet"])

    # Handle query input
    user_input = st.chat_input("Ask a question about the document...")
    if "user_query_input" in st.session_state and st.session_state["user_query_input"]:
        user_input = st.session_state.pop("user_query_input")

    if user_input:
        # Append and display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response using AstraDB RAG pipeline
        with st.chat_message("assistant"):
            with st.spinner("Retrieving from AstraDB & generating grounded answer..."):
                result = query_rag_system(
                    system_data["rag_chain"],
                    system_data["retriever"],
                    user_input
                )

                st.markdown(result["answer"])

                # Prepare source metadata for session state
                source_records = []
                if result["sources"]:
                    with st.expander("🔍 View Retrieved Sources", expanded=True):
                        for idx, doc in enumerate(result["sources"][:2], 1):
                            page_num = doc.metadata.get("page", 0) + 1
                            snippet = doc.page_content.strip()
                            st.markdown(f"**Source [{idx}] (Page {page_num}):**")
                            st.caption(f"{snippet[:250]}...")
                            source_records.append({"page": page_num, "snippet": snippet[:250]})

                # Store assistant response with sources in session state
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": source_records
                })


if __name__ == "__main__":
    main()

