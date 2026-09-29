# Assignment 21: LangChain Document Loaders & Text Splitters
# Author: Parth Dadhaniya
# Master Runner Script

import os
import subprocess
import sys

tasks = [
    ("Task 1: Text Loader", "task1_text_loader.py"),
    ("Task 2: CSV Loader", "task2_csv_loader.py"),
    ("Task 3: PDF Loader", "task3_pdf_loader.py"),
    ("Task 4: Directory Loader", "task4_directory_loader.py"),
    ("Task 5: WebBase Loader", "task5_web_loader.py"),
    ("Task 6: Why Text Splitting is Required", "task6_why_splitting.py"),
    ("Task 7: Length-Based Text Splitter", "task7_character_splitter.py"),
    ("Task 8: Structure-Based Splitter", "task8_recursive_splitter.py"),
    ("Task 9: Document Structure-Based Splitting", "task9_structure_splitter.py"),
    ("Task 10: Semantic Meaning-Based Splitting", "task10_semantic_splitter.py"),
    ("Task 11: Unified Preprocessing Pipeline", "task11_pipeline.py"),
    ("Task 12: Observations & Insights", "task12_observations.py"),
]

def main():
    print("=" * 70)
    print("Assignment 21: LangChain Document Loaders & Text Splitters")
    print("Student: Parth Dadhaniya")
    print("=" * 70)

    for title, script in tasks:
        print("\n" + "#" * 70)
        print(f"RUNNING: {title} ({script})")
        print("#" * 70 + "\n")
        
        script_path = os.path.join(os.path.dirname(__file__), script)
        result = subprocess.run([sys.executable, "-u", script_path], capture_output=False)
        if result.returncode != 0:
            print(f"Error occurred while executing {script}")
            break

    print("\n" + "=" * 70)
    print("All Assignment 21 tasks executed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
