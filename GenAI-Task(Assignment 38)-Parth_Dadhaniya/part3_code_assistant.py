# part3_code_assistant.py - Developer-Focused Code Assistant Features
# Student: Parth Dadhaniya

import time
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import get_codellama_llm, DEFAULT_MODEL


# Task 5: Prompt Engineering Templates for CodeLlama
GENERATE_PROMPT = PromptTemplate.from_template(
    "You are an expert Python software engineer.\n"
    "Task: Generate clean, production-ready Python code for the following requirement.\n"
    "Ensure the output includes:\n"
    "- Meaningful variable names and type annotations\n"
    "- Descriptive docstring explaining parameters and return values\n"
    "- Algorithmic time and space complexity\n"
    "- Realistic example usage\n\n"
    "Requirement:\n{spec}\n\n"
    "Response:"
)

EXPLAIN_PROMPT = PromptTemplate.from_template(
    "You are a senior software architect and educator.\n"
    "Task: Provide a structured, clear explanation of the following code snippet.\n"
    "Structure your response as follows:\n"
    "1. High-Level Purpose\n"
    "2. Step-by-Step Logic Breakdown\n"
    "3. Algorithmic Complexity (Time & Auxiliary Space)\n\n"
    "Code:\n{code}\n\n"
    "Explanation:"
)

DEBUG_PROMPT = PromptTemplate.from_template(
    "You are a senior Python debugging expert.\n"
    "Task: Identify, diagnose, and fix the bug in the provided code snippet.\n"
    "Structure your response as follows:\n"
    "1. Root Cause Identification\n"
    "2. Corrected Code Block\n"
    "3. Key Takeaway / Best Practice\n\n"
    "Buggy Code:\n{code}\n\n"
    "Error Info / Symptoms:\n{error_info}\n\n"
    "Diagnosis & Solution:"
)

OPTIMIZE_PROMPT = PromptTemplate.from_template(
    "You are a performance optimization specialist.\n"
    "Task: Optimize the following code for maximum runtime efficiency and clean memory usage.\n"
    "Structure your response as follows:\n"
    "1. Inefficiency Bottleneck Analysis\n"
    "2. Optimized Implementation\n"
    "3. Complexity Comparison (Original vs Optimized)\n\n"
    "Code to Optimize:\n{code}\n\n"
    "Optimization Analysis:"
)


# Task 3: Code Assistant Feature Pipelines
def get_assistant_chains():
    """Initializes LCEL chains for all 4 developer features."""
    llm, mode = get_codellama_llm(temperature=0.2)
    parser = StrOutputParser()

    generate_chain = GENERATE_PROMPT | llm | parser
    explain_chain = EXPLAIN_PROMPT | llm | parser
    debug_chain = DEBUG_PROMPT | llm | parser
    optimize_chain = OPTIMIZE_PROMPT | llm | parser

    return {
        "generate": generate_chain,
        "explain": explain_chain,
        "debug": debug_chain,
        "optimize": optimize_chain,
        "mode": mode
    }


def generate_code(spec: str) -> str:
    """Generates Python code based on user specification."""
    chains = get_assistant_chains()
    return chains["generate"].invoke({"spec": spec})


def explain_code(code: str) -> str:
    """Explains logic and complexity of a code snippet."""
    chains = get_assistant_chains()
    return chains["explain"].invoke({"code": code})


def debug_code(buggy_code: str, error_info: str = "Unexpected behavior or runtime failure") -> str:
    """Diagnoses and fixes bugs in the provided code."""
    chains = get_assistant_chains()
    return chains["debug"].invoke({"code": buggy_code, "error_info": error_info})


def optimize_code(code: str) -> str:
    """Analyzes and improves code performance and algorithmic efficiency."""
    chains = get_assistant_chains()
    return chains["optimize"].invoke({"code": code})


def run_tasks_3_and_5():
    """Executes Task 3 (Features) and Task 5 (Prompt Engineering) validation."""
    print("============================================================")
    print("Task 3 & 5: Code Assistant Features & Prompt Engineering")
    print("Student: Parth Dadhaniya")
    print("============================================================")

    # 1. Test Feature 1: Code Generation
    print(">>> 1. FEATURE: Code Generation <<<")
    spec = "Write a function to find the longest palindromic substring in a string"
    print(f"Spec: \"{spec}\"")
    gen_result = generate_code(spec)
    print("-" * 60)
    print(gen_result.strip())
    print("-" * 60 + "\n")

    # 2. Test Feature 2: Code Explanation
    print(">>> 2. FEATURE: Code Explanation <<<")
    sample_code_explain = (
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
    )
    print(f"Target Code:\n{sample_code_explain}")
    explain_result = explain_code(sample_code_explain)
    print("-" * 60)
    print(explain_result.strip())
    print("-" * 60 + "\n")

    # 3. Test Feature 3: Bug Fixing
    print(">>> 3. FEATURE: Bug Fixing / Debugging <<<")
    buggy_sample = (
        "def append_item(val, lst=[]):\n"
        "    lst.append(val)\n"
        "    return lst"
    )
    print(f"Buggy Code:\n{buggy_sample}")
    error_desc = "List retains values from previous calls instead of resetting"
    debug_result = debug_code(buggy_sample, error_desc)
    print("-" * 60)
    print(debug_result.strip())
    print("-" * 60 + "\n")

    # 4. Test Feature 4: Code Optimization
    print(">>> 4. FEATURE: Code Optimization <<<")
    inefficient_sample = (
        "def find_duplicates(arr):\n"
        "    dups = []\n"
        "    for i in range(len(arr)):\n"
        "        for j in range(i + 1, len(arr)):\n"
        "            if arr[i] == arr[j] and arr[i] not in dups:\n"
        "                dups.append(arr[i])\n"
        "    return dups"
    )
    print(f"Inefficient Code:\n{inefficient_sample}")
    opt_result = optimize_code(inefficient_sample)
    print("-" * 60)
    print(opt_result.strip())
    print("-" * 60 + "\n")


if __name__ == "__main__":
    run_tasks_3_and_5()
