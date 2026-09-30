# part1_streamlit_cloud.py - Streamlit Cloud Deployment Guide & Validation
# Student: Parth Dadhaniya

import os
from config import run_genai_pipeline


def print_streamlit_cloud_guide():
    """Prints the step-by-step deployment guide for Streamlit Community Cloud."""
    print("============================================================")
    print("Task 1: Deployment on Streamlit Cloud")
    print("Student: Parth Dadhaniya")
    print("============================================================")
    print("Step-by-Step Deployment Procedure:")
    print("1. Repository & File Preparation:")
    print("   - Ensure 'app.py' and 'requirements.txt' are committed in your GitHub repository.")
    print("   - Recommended: include '.streamlit/config.toml' for headless theme configuration.")
    print("2. Connect Streamlit Community Cloud:")
    print("   - Visit https://share.streamlit.io and sign in with your GitHub account.")
    print("   - Click the 'New app' button.")
    print("3. Configure App Settings:")
    print("   - Repository : parthdadhaniya/Tute-Dude-Gen-Ai-Course-Assignments")
    print("   - Branch     : main")
    print("   - Main file  : GenAI-Task(Assignment 39)-Parth_Dadhaniya/app.py")
    print("   - Custom URL : (Optional) e.g., parth-genai-suite.streamlit.app")
    print("4. Secrets Management (Optional):")
    print("   - In Advanced Settings -> Secrets, paste environment variables (e.g. GROQ_API_KEY).")
    print("5. Deploy & Verify:")
    print("   - Click 'Deploy!'. Streamlit Cloud installs requirements and provisions the container.")
    print("   - Live URL format: https://<app-name>.streamlit.app\n")


def test_streamlit_cloud_readiness():
    """Validates that all essential deployment artifacts are present and functional."""
    print("--- Pre-Flight Verification for Streamlit Cloud ---")
    current_dir = os.path.dirname(__file__)

    app_path = os.path.join(current_dir, "app.py")
    req_path = os.path.join(current_dir, "requirements.txt")
    config_path = os.path.join(current_dir, ".streamlit", "config.toml")

    has_app = os.path.exists(app_path)
    has_req = os.path.exists(req_path)
    has_config = os.path.exists(config_path)

    print(f"1. Entrypoint File (app.py)          : {'[FOUND]' if has_app else '[MISSING]'}")
    print(f"2. Dependencies (requirements.txt)   : {'[FOUND]' if has_req else '[MISSING]'}")
    print(f"3. Streamlit Config (config.toml)    : {'[FOUND]' if has_config else '[MISSING]'}")

    # Inspect requirements.txt packages
    if has_req:
        with open(req_path, "r", encoding="utf-8") as f:
            pkgs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"   Indexed Packages: {pkgs}")

    # Simulate functional query
    print("4. Functional Pipeline Simulation    :")
    sample_res = run_genai_pipeline("Grounded Q&A", "What is Streamlit Cloud?")
    print(f"   Sample Output: {sample_res[:100]}...")

    is_ready = has_app and has_req
    print(f"\n>> Streamlit Cloud Readiness: {'READY FOR CLOUD DEPLOYMENT' if is_ready else 'INCOMPLETE'}")
    print("------------------------------------------------------------\n")
    return is_ready


def run_task1():
    print_streamlit_cloud_guide()
    test_streamlit_cloud_readiness()


if __name__ == "__main__":
    run_task1()
