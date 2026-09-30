# Part 6: Observations & Learnings (Task 11)
# Student: Parth Dadhaniya

ANSWERS = {
    "1. Why Groq is suitable for RAG chatbots": (
        "Groq's LPU (Language Processing Unit) architecture uses on-chip SRAM instead of external "
        "GPU memory (HBM). This removes memory bandwidth bottlenecks, allowing inference speeds "
        "of 300 to 500+ tokens per second. In RAG chatbots, this ultra-low latency gives users instant "
        "conversational responses without noticeable streaming delays."
    ),
    "2. Difference between Groq RAG and OpenAI RAG": (
        "- Inference Speed: Groq runs much faster (300-500+ tokens/sec) compared to OpenAI APIs (around 50-80 tokens/sec).\n"
        "- Cost: Groq hosts open-source models like Llama 3 at lower pricing than proprietary frontier models.\n"
        "- Ecosystem: OpenAI models support multimodal inputs and very large context windows (128k+), while Groq specializes in blazing-fast execution of open-source weights."
    ),
    "3. Role of Streamlit in rapid GenAI prototyping": (
        "Streamlit lets you build full web-based chat interfaces completely in Python without needing HTML or JavaScript. "
        "Components like st.chat_input, st.chat_message, st.session_state, and st.file_uploader make it easy to manage "
        "multi-turn conversation memory, upload documents, and show source chunks in under 100 lines of code."
    )
}


def print_observations():
    print("--- Task 11: Observations & Learnings ---")
    print("Student: Parth Dadhaniya\n")
    for q, a in ANSWERS.items():
        print(f"[{q}]\n{a}\n")


if __name__ == "__main__":
    print_observations()
