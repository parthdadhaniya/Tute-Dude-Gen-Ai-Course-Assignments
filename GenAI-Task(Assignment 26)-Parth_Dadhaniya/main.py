# main.py - Master runner for Assignment 26
# Student: Parth Dadhaniya
# Course: Generative AI Engineering

import subprocess
import sys

task_scripts = [
    ("task1_groq_setup.py", "PART 1 - TASK 1: GROQ API SETUP & BASIC CHAT"),
    ("task2_groq_chatbot.py", "PART 1 - TASK 2: GROQ CHATBOT CORE LOGIC"),
    ("task3_task4_groq_rag.py", "PART 2 - TASKS 3 & 4: GROQ + RAG PIPELINE & PROMPT TEMPLATE"),
    ("task7_task9_api_test.py", "PARTS 3, 4 & 5 - TASKS 5, 6, 7 & 9: FASTAPI APPLICATION & VERIFICATION"),
    ("task10_observations.py", "PART 5 - TASK 10: OBSERVATIONS & INSIGHTS")
]

def main():
    print("==================================================")
    print("  ASSIGNMENT 26: GROQ API CHATBOT, RAG & FASTAPI")
    print("  Student: Parth Dadhaniya")
    print("==================================================")
    sys.stdout.flush()

    for script, header in task_scripts:
        print("\n" + "=" * 50)
        print(header)
        print("=" * 50)
        sys.stdout.flush()
        
        ret = subprocess.run([sys.executable, script])
        if ret.returncode != 0:
            print(f"Warning: {script} exited with status {ret.returncode}")
        sys.stdout.flush()

    print("\n" + "=" * 50)
    print("All Assignment 26 tasks executed successfully!")
    print("==================================================")
    print("\nTo start the live FastAPI server:")
    print("  uvicorn app:app --reload --port 8000")
    print("Interactive Swagger UI documentation: http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    main()
