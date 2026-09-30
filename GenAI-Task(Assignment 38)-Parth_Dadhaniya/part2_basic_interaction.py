# part2_basic_interaction.py - Basic CodeLlama Interaction
# Student: Parth Dadhaniya

import time
from config import get_codellama_llm, DEFAULT_MODEL


def run_basic_prompt(llm, prompt: str):
    """Executes a single prompt against CodeLlama and returns result with latency."""
    start = time.time()
    response = llm.invoke(prompt)
    elapsed = round(time.time() - start, 3)
    return response, elapsed


def run_task2():
    """Executes Task 2: Basic interaction testing with CodeLlama."""
    print("============================================================")
    print("Task 2: Basic CodeLlama Interaction")
    print("Student: Parth Dadhaniya")
    print("============================================================")

    llm, mode = get_codellama_llm(temperature=0.1)
    print(f"Active LLM Backend : {mode} (Model: {DEFAULT_MODEL})\n")

    # Prompt 1: Code Generation
    prompt_1 = "Write a Python function to check prime numbers"
    print(f"--- Prompt 1: Code Generation ---")
    print(f"User Input: \"{prompt_1}\"")
    output_1, time_1 = run_basic_prompt(llm, prompt_1)
    print("CodeLlama Response:")
    print(output_1.strip())
    print(f"(Latency: {time_1}s)\n")

    # Prompt 2: Code Explanation
    prompt_2 = "Explain this code: def add(a, b): return a + b"
    print(f"--- Prompt 2: Code Explanation ---")
    print(f"User Input: \"{prompt_2}\"")
    output_2, time_2 = run_basic_prompt(llm, prompt_2)
    print("CodeLlama Response:")
    print(output_2.strip())
    print(f"(Latency: {time_2}s)\n")

    print(">>> Task 2 Takeaways <<<")
    print("- CodeLlama generates syntactically valid Python code with docstrings.")
    print("- Code explanation breaks down functions into parameters, operations, and complexity.")


if __name__ == "__main__":
    run_task2()
