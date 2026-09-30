# app.py - GenAI Multi-Task Suite (Streamlit Cloud & Hugging Face Spaces)
# Student: Parth Dadhaniya

import streamlit as st
from config import get_deployment_environment, get_secret, run_genai_pipeline

# Configure Streamlit page layout and title
st.set_page_config(
    page_title="GenAI Cloud Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Preset sample data for 1-click demonstration
SAMPLE_TEXT = (
    "Generative Artificial Intelligence (GenAI) is revolutionizing industries by enabling automated content creation, "
    "intelligent code synthesis, and advanced conversational agents. Unlike traditional machine learning that primarily "
    "focuses on pattern classification or numerical prediction, GenAI models generate novel, context-aware text, code, "
    "and multimodal media. Modern deployment platforms like Streamlit Community Cloud and Hugging Face Spaces allow "
    "developers to package these models into accessible, cloud-hosted web applications with continuous integration."
)

SAMPLE_CODE_SPEC = "Write a Python function to calculate the moving average of a list of numbers using a sliding window."

SAMPLE_QA = "What is the primary difference between Streamlit Cloud and Hugging Face Spaces for GenAI deployment?"


def main():
    # Detect active cloud platform
    env_info = get_deployment_environment()

    # Top Header & Platform Badge
    col_title, col_badge = st.columns([3, 1])
    with col_title:
        st.title("🚀 GenAI Cloud Productivity Suite")
        st.caption("Production-Ready GenAI Web Application | Student: Parth Dadhaniya")
    with col_badge:
        st.markdown(f"### `{env_info['badge']}`")
        st.caption(f"Platform: **{env_info['platform']}**")

    # Sidebar: Settings & Deployment Guide
    with st.sidebar:
        st.header("⚙️ Deployment Controls")
        st.write(f"**Target Host:** `{env_info['platform']}`")

        # Optional API Key input
        api_key_input = st.text_input(
            "API Key (Groq / Optional):",
            type="password",
            value="",
            help="Leave blank to use zero-config local student engine."
        )

        st.divider()
        st.subheader("💡 1-Click Demo Presets")
        if st.button("Load Summarizer Sample", use_container_width=True):
            st.session_state["active_tab"] = "Summarizer"
            st.session_state["input_text"] = SAMPLE_TEXT

        if st.button("Load Code Assistant Sample", use_container_width=True):
            st.session_state["active_tab"] = "Code Assistant"
            st.session_state["input_code"] = SAMPLE_CODE_SPEC

        if st.button("Load Q&A Sample", use_container_width=True):
            st.session_state["active_tab"] = "Grounded Q&A"
            st.session_state["input_qa"] = SAMPLE_QA

        st.divider()
        st.subheader("🌐 Deployment Links")
        st.markdown(
            "- [Streamlit Cloud](https://share.streamlit.io)\n"
            "- [Hugging Face Spaces](https://huggingface.co/spaces)\n"
            "- [GitHub Repository](https://github.com/parthdadhaniya/Tute-Dude-Gen-Ai-Course-Assignments)"
        )

    # Main Tabs
    tab_sum, tab_code, tab_qa = st.tabs(["📄 Text Summarizer", "💻 Code Assistant", "❓ Grounded Q&A"])

    # 1. Text Summarizer Tab
    with tab_sum:
        st.subheader("Executive Text Summarizer")
        st.write("Extract concise overviews and bulleted key takeaways from articles, reports, and documentation.")

        sum_input = st.text_area(
            "Enter text to summarize:",
            value=st.session_state.get("input_text", SAMPLE_TEXT),
            height=160
        )

        if st.button("Generate Summary", type="primary", key="btn_sum"):
            if sum_input.strip():
                with st.spinner("Generating executive summary..."):
                    summary = run_genai_pipeline("Summarization", sum_input, api_key=api_key_input)
                st.markdown(summary)
            else:
                st.warning("Please enter text to summarize.")

    # 2. Code Assistant Tab
    with tab_code:
        st.subheader("AI Software Engineering Assistant")
        st.write("Generate clean Python functions with docstrings, type annotations, and complexity analysis.")

        code_spec = st.text_area(
            "Enter function requirement or algorithm specification:",
            value=st.session_state.get("input_code", SAMPLE_CODE_SPEC),
            height=120
        )

        if st.button("Generate Python Code", type="primary", key="btn_code"):
            if code_spec.strip():
                with st.spinner("Synthesizing Python code and complexity..."):
                    code_result = run_genai_pipeline("Code Assistant", code_spec, api_key=api_key_input)
                st.markdown(code_result)
            else:
                st.warning("Please provide a specification.")

    # 3. Grounded Q&A Tab
    with tab_qa:
        st.subheader("Grounded Technical Q&A")
        st.write("Ask technical and deployment architecture questions.")

        qa_input = st.text_input(
            "Enter your question:",
            value=st.session_state.get("input_qa", SAMPLE_QA)
        )

        if st.button("Ask Question", type="primary", key="btn_qa"):
            if qa_input.strip():
                with st.spinner("Retrieving grounded answer..."):
                    answer = run_genai_pipeline("Grounded Q&A", qa_input, api_key=api_key_input)
                st.info(f"**Answer:** {answer}")
            else:
                st.warning("Please enter a question.")


if __name__ == "__main__":
    main()
