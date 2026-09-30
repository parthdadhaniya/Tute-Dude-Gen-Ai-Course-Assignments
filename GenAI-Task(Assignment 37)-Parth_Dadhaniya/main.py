# main.py - Master Pipeline Runner for Assignment 37
# Assignment: AstraDB RAG (DataStax)
# Student: Parth Dadhaniya

import sys
from part1_astradb_setup import run_tasks_1_and_2
from part2_pdf_processing import run_tasks_3_and_4
from part3_rag_pipeline import run_tasks_5_and_6
from part4_observations import print_observations_and_insights


def main():
    print("=" * 68)
    print("Assignment 37: AstraDB Cloud Vector Database & PDF Query RAG")
    print("Student: Parth Dadhaniya")
    print("Course: Generative AI Engineering - TuteDude")
    print("=" * 68)

    print("\n>>> PART 1: Getting Started with AstraDB & Connection Setup (Tasks 1 & 2) <<<")
    run_tasks_1_and_2()

    print("\n>>> PART 2: Load, Split PDF & Store Embeddings in AstraDB (Tasks 3 & 4) <<<")
    run_tasks_3_and_4()

    print("\n>>> PART 3: PDF Query RAG Pipeline & Testing Validation (Tasks 5 & 6) <<<")
    run_tasks_5_and_6()

    print("\n>>> PART 4: Observations & Architectural Insights <<<")
    print_observations_and_insights()

    print("\n" + "=" * 68)
    print("All tasks for Assignment 37 completed successfully!")
    print("To launch the interactive Streamlit Web UI, run:")
    print("  streamlit run app.py")
    print("=" * 68)


if __name__ == "__main__":
    main()

