# app.py - Streamlit CodeLlama Developer Assistant
# Student: Parth Dadhaniya

import streamlit as st
from config import (
    DEFAULT_MODEL,
    OLLAMA_BASE_URL,
    is_ollama_running,
    get_codellama_llm
)
from part3_code_assistant import (
    generate_code,
    explain_code,
    debug_code,
    optimize_code
)

# Page Configuration
st.set_page_config(
    page_title="CodeLlama Coding Assistant",
    page_icon="💻",
    layout="wide"
)

# Default presets for quick testing
SAMPLE_PRESETS = {
    "Generate Code": "Write a Python function to find the longest palindromic substring in a string",
    "Explain Code": (
        "def binary_search(arr, target):\n"
        "    low, high = 0, len(arr) - 1\n"
        "    while low <= high:\n"
        "        mid = (low + high) // 2\n"
        "        if arr[mid] == target:\n"
        "            return mid\n"
        "        elif arr[mid] < target:\n"
        "            low = mid + 1\n"
        "        else:\n"
        "            high = mid - 1\n"
        "    return -1"
    ),
    "Debug Code": (
        "def append_item(val, lst=[]):\n"
        "    lst.append(val)\n"
        "    return lst"
    ),
    "Optimize Code": (
        "def find_duplicates(arr):\n"
        "    dups = []\n"
        "    for i in range(len(arr)):\n"
        "        for j in range(i + 1, len(arr)):\n"
        "            if arr[i] == arr[j] and arr[i] not in dups:\n"
        "                dups.append(arr[i])\n"
        "    return dups"
    )
}


def main():
    st.title("💻 CodeLlama Developer Assistant")
    st.caption("Local AI Coding Assistant powered by Ollama & CodeLlama | Student: Parth Dadhaniya")

    # Check Ollama server status
    server_online = is_ollama_running()
    _, active_mode = get_codellama_llm()

    # Sidebar: Model and Presets
    with st.sidebar:
        st.header("⚙️ Model Configuration")
        st.write(f"**Model:** `{DEFAULT_MODEL}`")
        st.write(f"**Backend:** `{active_mode}`")

        if server_online:
            st.success("🟢 Local Ollama Server Active (Port 11434)")
        else:
            st.info("🔵 Local CodeLlama Student Emulator Active")

        st.divider()
        st.subheader("💡 Quick Sample Presets")
        for task_name, preset_code in SAMPLE_PRESETS.items():
            if st.button(f"Load {task_name}", use_container_width=True):
                st.session_state["selected_task"] = task_name
                st.session_state["input_code"] = preset_code
                st.rerun()

        st.divider()
        st.markdown(
            "**Ollama Setup Quick Reference:**\n"
            "1. `ollama pull codellama:7b`\n"
            "2. `ollama serve`\n"
            "3. Refresh this page to connect live!"
        )

    # Main Interface
    task_options = ["Generate Code", "Explain Code", "Debug Code", "Optimize Code"]
    current_task = st.session_state.get("selected_task", "Generate Code")
    task_index = task_options.index(current_task) if current_task in task_options else 0

    task_type = st.selectbox(
        "Select Task Type:",
        task_options,
        index=task_index
    )

    # Dynamic label and placeholder
    if task_type == "Generate Code":
        input_label = "Enter Code Specification / Problem Description:"
        default_val = st.session_state.get("input_code", SAMPLE_PRESETS["Generate Code"])
        height = 120
    else:
        input_label = "Enter Python Code Snippet:"
        default_val = st.session_state.get("input_code", SAMPLE_PRESETS.get(task_type, ""))
        height = 220

    user_input = st.text_area(input_label, value=default_val, height=height)

    # Optional extra input for Debug task
    error_info = ""
    if task_type == "Debug Code":
        error_info = st.text_input(
            "Error Message / Observed Symptoms (Optional):",
            value="List retains values across consecutive function calls instead of resetting"
        )

    # Run button
    if st.button("🚀 Run CodeLlama Assistant", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("Please provide code or a specification before running.")
            return

        with st.spinner(f"Running CodeLlama for {task_type}..."):
            if task_type == "Generate Code":
                result = generate_code(user_input)
            elif task_type == "Explain Code":
                result = explain_code(user_input)
            elif task_type == "Debug Code":
                result = debug_code(user_input, error_info=error_info)
            elif task_type == "Optimize Code":
                result = optimize_code(user_input)
            else:
                result = "Unknown task type."

        st.subheader("📋 CodeLlama Output")
        st.markdown(result)


if __name__ == "__main__":
    main()
