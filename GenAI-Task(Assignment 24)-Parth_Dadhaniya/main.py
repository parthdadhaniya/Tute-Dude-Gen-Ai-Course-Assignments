# main.py - Master runner for Assignment 24
# Parth Dadhaniya

import subprocess
import sys

def run_task(script_name, title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)
    sys.stdout.flush()
    subprocess.run([sys.executable, script_name])
    sys.stdout.flush()

def main():
    print("Assignment 24: Ollama Chatbot & LangSmith Tracking")
    print("Student: Parth Dadhaniya")

    run_task("task1_ollama_basic.py", "TASK 1: OLLAMA SETUP & BASIC CHAT")
    run_task("task2_ollama_chatbot.py", "TASK 2: MULTI-TURN CHATBOT WITH MEMORY")
    run_task("task3_langsmith_tracking.py", "TASK 3: LANGSMITH RUN TRACKING")

    print("\n" + "=" * 50)
    print("All tasks finished successfully.")
    print("Run Streamlit app: streamlit run app.py")
    print("=" * 50)

if __name__ == "__main__":
    main()
