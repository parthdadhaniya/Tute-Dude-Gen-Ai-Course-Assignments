# Part 6: Observations & Learnings (Task 11)
# Student: Parth Dadhaniya


def print_observations():
    print("--- Task 11: Observations & Learnings ---")
    print("Student: Parth Dadhaniya\n")

    print("1. Why Groq is suitable for RAG chatbots:")
    print("Groq's LPU architecture uses on-chip SRAM instead of external GPU memory (HBM). This removes memory bandwidth bottlenecks, allowing speeds of 300 to 500+ tokens per second. In RAG chatbots, this gives users instant responses without streaming lag.\n")

    print("2. Difference between Groq RAG and OpenAI RAG:")
    print("- Speed: Groq runs significantly faster (300-500+ tokens/sec vs ~50-80 tokens/sec on OpenAI).")
    print("- Cost: Groq hosts open-source models like Llama 3 at lower pricing than proprietary frontier models.")
    print("- Capability: OpenAI models support multimodal inputs and large context windows, while Groq focuses on blazing fast execution of open weights.\n")

    print("3. Role of Streamlit in rapid GenAI prototyping:")
    print("Streamlit lets you build full web chat apps entirely in Python. Features like st.chat_input, st.chat_message, st.session_state, and st.file_uploader allow you to build an interactive RAG interface with document upload in under 100 lines of code.")


if __name__ == "__main__":
    print_observations()
