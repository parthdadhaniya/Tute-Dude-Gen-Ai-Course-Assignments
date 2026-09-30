# part2_hf_spaces.py - Hugging Face Spaces Deployment Guide & Validation
# Student: Parth Dadhaniya

import os


def print_hf_spaces_guide():
    """Prints the step-by-step deployment guide for Hugging Face Spaces."""
    print("============================================================")
    print("Task 2: Deployment on Hugging Face Spaces")
    print("Student: Parth Dadhaniya")
    print("============================================================")
    print("Step-by-Step Deployment Procedure:")
    print("1. Create New Hugging Face Space:")
    print("   - Visit https://huggingface.co/spaces and click 'Create new Space'.")
    print("   - Space Name : parth-genai-cloud-suite")
    print("   - License    : MIT (or Apache 2.0)")
    print("   - Select SDK : Streamlit")
    print("   - Hardware   : CPU basic (2 vCPU, 16GB RAM - Free)")
    print("2. Repository Linking / Upload:")
    print("   - Method A (Direct Git Push):")
    print("     git remote add space https://huggingface.co/spaces/<username>/parth-genai-cloud-suite")
    print("     git push space main")
    print("   - Method B (GitHub Sync Action):")
    print("     Use Hugging Face Sync Action to mirror GitHub repository changes automatically.")
    print("3. Configure YAML Frontmatter in README.md:")
    print("   - Hugging Face Spaces requires a YAML header in README.md:")
    print("     ---")
    print("     title: GenAI Cloud Productivity Suite")
    print("     emoji: rocket")
    print("     colorFrom: indigo")
    print("     colorTo: purple")
    print("     sdk: streamlit")
    print("     sdk_version: \"1.40.0\"")
    print("     app_file: app.py")
    print("     pinned: false")
    print("     ---")
    print("4. Add Environment Secrets (Optional):")
    print("   - In Space Settings -> Variables and secrets, add secrets like GROQ_API_KEY.")
    print("5. Live Verification:")
    print("   - Space builds automatically in Docker container.")
    print("   - Live URL format: https://huggingface.co/spaces/<username>/<space-name>\n")


def test_hf_space_readiness():
    """Validates that YAML metadata and space assets meet Hugging Face requirements."""
    print("--- Pre-Flight Verification for Hugging Face Spaces ---")
    current_dir = os.path.dirname(__file__)
    readme_path = os.path.join(current_dir, "README.md")
    app_path = os.path.join(current_dir, "app.py")
    req_path = os.path.join(current_dir, "requirements.txt")

    has_app = os.path.exists(app_path)
    has_req = os.path.exists(req_path)
    has_readme = os.path.exists(readme_path)

    print(f"1. Target App Script (app.py)        : {'[FOUND]' if has_app else '[MISSING]'}")
    print(f"2. Package Manifest (requirements)   : {'[FOUND]' if has_req else '[MISSING]'}")
    print(f"3. Space Metadata Doc (README.md)    : {'[FOUND]' if has_readme else '[MISSING]'}")

    # Inspect YAML Frontmatter
    has_yaml_frontmatter = False
    if has_readme:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---") and "sdk: streamlit" in content and "app_file: app.py" in content:
            has_yaml_frontmatter = True
            print("4. YAML Frontmatter Specification    : [VALID]")
            print("   - Detected sdk: streamlit")
            print("   - Detected app_file: app.py")
        else:
            print("4. YAML Frontmatter Specification    : [PENDING / INCOMPLETE]")

    is_ready = has_app and has_req and has_readme
    print(f"\n>> Hugging Face Spaces Readiness: {'READY FOR SPACES DEPLOYMENT' if is_ready else 'INCOMPLETE'}")
    print("------------------------------------------------------------\n")
    return is_ready


def run_task2():
    print_hf_spaces_guide()
    test_hf_space_readiness()


if __name__ == "__main__":
    run_task2()
