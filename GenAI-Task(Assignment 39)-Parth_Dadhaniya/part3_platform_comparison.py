# part3_platform_comparison.py - Platform Comparison & Decision Matrix
# Student: Parth Dadhaniya


def print_platform_comparison():
    """Prints comprehensive technical comparison between Streamlit Cloud and Hugging Face Spaces."""
    print("============================================================")
    print("Task 3: Compare Deployment Platforms")
    print("Student: Parth Dadhaniya")
    print("============================================================\n")

    print("1. Streamlit Cloud vs Hugging Face Spaces (Architectural Overview):")
    print("   - Streamlit Community Cloud: A specialized platform engineered by Snowflake/Streamlit.")
    print("     It integrates natively with GitHub, automatically pulling code on every commit and running")
    print("     it in lightweight containerized virtual machines optimized strictly for Streamlit apps.")
    print("   - Hugging Face Spaces: A versatile AI application hosting platform built directly into the")
    print("     Hugging Face Hub. It supports Streamlit, Gradio, Docker containers, and Static HTML, allowing")
    print("     developers to leverage open-source models, datasets, and high-performance GPU hardware.\n")

    print("2. Pros & Cons of Each Platform:")
    print("   [Streamlit Community Cloud]")
    print("   - Pros:")
    print("     * Seamless GitHub CI/CD: Every 'git push' automatically updates the live deployment.")
    print("     * Zero Configuration: No Dockerfile or complex configuration needed.")
    print("     * Custom Subdomains: Generates clean, professional URLs (e.g. your-app.streamlit.app).")
    print("     * Simple Secrets Management: Built-in UI editor for TOML secrets (st.secrets).")
    print("   - Cons:")
    print("     * Strict Memory Limits: Free tier is capped at ~1GB RAM, causing OOM crashes on heavy models.")
    print("     * No GPU Support: Cannot run local deep learning or transformer inference on GPUs.")
    print("     * App Dormancy: Apps go to sleep after prolonged periods of inactivity.")
    print("\n   [Hugging Face Spaces]")
    print("   - Pros:")
    print("     * Generous Free Tier: Provides 2 vCPUs and 16GB RAM for free -- 16x more RAM than Streamlit Cloud.")
    print("     * Multi-Framework Flexibility: Supports Streamlit, Gradio, and arbitrary Docker containers.")
    print("     * On-Demand GPU Upgrades: Instant access to Nvidia T4, A10G, and A100 GPUs on pay-as-you-go.")
    print("     * Massive AI Community: Native discoverability on the Hugging Face Hub with likes and forks.")
    print("   - Cons:")
    print("     * Dual Repository Management: Requires pushing to Hugging Face Git remote or setting up actions.")
    print("     * Slower Initial Builds: Downloading PyTorch/Transformers dependencies can take 3-5 minutes.")
    print("     * Iframe Wrapping: Default space interface runs inside an embedded iframe.\n")

    print("3. Comprehensive Comparison Table:")
    print("-" * 78)
    print(f"{'Feature':<22} | {'Streamlit Cloud':<24} | {'Hugging Face Spaces':<26}")
    print("-" * 78)
    print(f"{'Primary Focus':<22} | {'Streamlit Dashboards':<24} | {'ML/GenAI Apps & Models':<26}")
    print(f"{'Free Tier Memory':<22} | {'~1 GB RAM':<24} | {'16 GB RAM (2 vCPUs)':<26}")
    print(f"{'GPU Availability':<22} | {'None (CPU only)':<24} | {'Paid upgrades (T4/A10G/A100)':<26}")
    print(f"{'Supported SDKs':<22} | {'Streamlit only':<24} | {'Streamlit, Gradio, Docker':<26}")
    print(f"{'Git Source':<22} | {'GitHub repository':<24} | {'Hugging Face Hub / GitHub':<26}")
    print(f"{'Secrets Management':<22} | {'st.secrets (TOML)':<24} | {'Space Variables & Secrets':<26}")
    print(f"{'Community Discovery':<22} | {'Direct URL sharing':<24} | {'Hugging Face Hub feed':<26}")
    print("-" * 78)

    print("\n4. When to Use Which (Decision Matrix):")
    print("   - Choose Streamlit Cloud when:")
    print("     * You are building business intelligence dashboards, lightweight GenAI apps using API wrappers")
    print("       (like Groq, OpenAI, or Anthropic), where heavy weights are not loaded into memory.")
    print("     * You want immediate, frictionless continuous deployment directly tied to your GitHub branch.")
    print("   - Choose Hugging Face Spaces when:")
    print("     * You are loading open-source models directly into memory (e.g. sentence-transformers, diffusers,")
    print("       or PyTorch pipelines) that require more than 1GB RAM.")
    print("     * You require GPU acceleration, custom Docker runtimes, or desire visibility within the AI community.")


def run_task3():
    print_platform_comparison()


if __name__ == "__main__":
    run_task3()
