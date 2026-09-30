# main.py - Master Deployment Pipeline & Comparison Runner
# Assignment 39: GenAI App Deployment (Streamlit Cloud & Hugging Face Spaces)
# Student: Parth Dadhaniya

import sys
from part1_streamlit_cloud import run_task1
from part2_hf_spaces import run_task2
from part3_platform_comparison import run_task3


def main():
    print("=" * 68)
    print("Assignment 39: GenAI App Deployment (Streamlit Cloud & HF Spaces)")
    print("Student: Parth Dadhaniya")
    print("Course: Generative AI Engineering - TuteDude")
    print("=" * 68)

    print("\n>>> PART 1: Deployment on Streamlit Cloud (Task 1) <<<")
    run_task1()

    print("\n>>> PART 2: Deployment on Hugging Face Spaces (Task 2) <<<")
    run_task2()

    print("\n>>> PART 3: Validation & Platform Comparison (Task 3) <<<")
    run_task3()

    print("=" * 68)
    print("All tasks for Assignment 39 completed successfully!")
    print("To launch the multi-task cloud app locally, run:")
    print("  streamlit run app.py")
    print("=" * 68)


if __name__ == "__main__":
    main()
