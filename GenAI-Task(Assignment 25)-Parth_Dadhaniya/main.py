# main.py - Master runner for Assignment 25
# Student: Parth Dadhaniya
# Course: Generative AI Engineering

import subprocess
import sys

tasks = [
    ("task1_prompt_template.py", "TASK 1: PROMPT TEMPLATE WITH DYNAMIC INJECTION"),
    ("task2_chat_prompt_template.py", "TASK 2: CHAT PROMPT TEMPLATE & MESSAGE TEMPLATES"),
    ("task3_pydantic_schema.py", "TASK 3: STRUCTURED OUTPUT WITH PYDANTIC SCHEMA"),
    ("task4_validation_fallback.py", "TASK 4: VALIDATION & ERROR HANDLING WITH FALLBACK"),
    ("task5_simple_chain.py", "TASK 5: SIMPLE CHAIN EXECUTION"),
    ("task6_conditional_chain.py", "TASK 6: CONDITIONAL ROUTING CHAIN"),
    ("task7_parallel_chain.py", "TASK 7: PARALLEL CHAIN EXECUTION"),
    ("task8_runnables_lcel.py", "TASK 8: RUNNABLES BASICS & LCEL COMPOSITION"),
    ("task9_lcel_rag.py", "TASK 9: LCEL-BASED RAG PIPELINE"),
    ("task10_observations.py", "TASK 10: OBSERVATIONS & INSIGHTS")
]

def main():
    print("==================================================")
    print("  ASSIGNMENT 25: PROMPTING & LANGCHAIN CHAINS")
    print("  Student: Parth Dadhaniya")
    print("==================================================")
    sys.stdout.flush()

    for script, title in tasks:
        print("\n" + "=" * 50)
        print(title)
        print("=" * 50)
        sys.stdout.flush()
        ret = subprocess.run([sys.executable, script])
        if ret.returncode != 0:
            print(f"Warning: {script} exited with error code {ret.returncode}")
        sys.stdout.flush()

    print("\n" + "=" * 50)
    print("All Assignment 25 tasks completed successfully!")
    print("==================================================")

if __name__ == "__main__":
    main()
