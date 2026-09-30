# part1_codellama_setup.py - Setup CodeLlama with Ollama
# Student: Parth Dadhaniya

import os
import requests
from config import OLLAMA_BASE_URL, DEFAULT_MODEL, is_ollama_running, get_available_ollama_models


def print_setup_guide():
    """Prints the step-by-step setup guide for running CodeLlama locally with Ollama."""
    print("============================================================")
    print("Task 1: Setup CodeLlama with Ollama")
    print("Student: Parth Dadhaniya")
    print("============================================================")
    print("Step-by-Step Local Setup Instructions:")
    print("1. Download & Install Ollama:")
    print("   - Visit https://ollama.com and install Ollama for Windows/macOS/Linux.")
    print("2. Pull the CodeLlama Model:")
    print(f"   - Open your terminal and run:")
    print(f"       ollama pull {DEFAULT_MODEL}")
    print("   - This downloads Meta's CodeLlama 7B model tuned for programming tasks.")
    print("3. Start the Ollama Service:")
    print("   - Run 'ollama serve' (or ensure the background tray app is active).")
    print(f"   - Default API Endpoint: {OLLAMA_BASE_URL}")
    print("4. Verify Model Execution:")
    print("   - Test via CLI: ollama run codellama:7b 'Write hello world in Python'\n")


def verify_ollama_and_model():
    """Checks if Ollama server is running and verifies if CodeLlama is available."""
    print("--- Verifying Local Ollama Server & Model ---")
    server_online = is_ollama_running()
    print(f"Target Server URL : {OLLAMA_BASE_URL}")
    print(f"Target Model      : {DEFAULT_MODEL}")
    print(f"Ollama Server Live: {server_online}")

    if server_online:
        models = get_available_ollama_models()
        print(f"Models Available  : {models}")
        has_codellama = any(DEFAULT_MODEL in m for m in models)
        if has_codellama:
            print(f">> SUCCESS: {DEFAULT_MODEL} is downloaded and ready for inference!")
        else:
            print(f">> Notice: Ollama is running, but {DEFAULT_MODEL} is not yet pulled.")
            print(f">> Run: 'ollama pull {DEFAULT_MODEL}' to download the weights.")
    else:
        print(">> Notice: Local Ollama server is not running on port 11434.")
        print(">> Local CodeLlama Student Emulator is active so all tasks run cleanly offline.")

    print("------------------------------------------------------------\n")
    return server_online


def run_task1():
    print_setup_guide()
    verify_ollama_and_model()


if __name__ == "__main__":
    run_task1()
