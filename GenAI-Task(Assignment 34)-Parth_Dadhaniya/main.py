# main.py - Master Runner for Assignment 34
# Student: Parth Dadhaniya

import part1_prompt_summarization
import part2_stuff_chain
import part3_map_reduce_chain
import part4_refine_chain
import part5_document_summarizer
import task14_observations


def main():
    print("=" * 65)
    print("Assignment 34: Text Summarization using LangChain")
    print("Student: Parth Dadhaniya")
    print("=" * 65)

    print("\n>>> PART 1: Basic Text Summarization using PromptTemplate <<<")
    part1_prompt_summarization.main()

    print("\n>>> PART 2: Stuff Summarization Chain <<<")
    part2_stuff_chain.main()

    print("\n>>> PART 3: Map-Reduce Summarization Chain <<<")
    part3_map_reduce_chain.main()

    print("\n>>> PART 4: Refine Summarization Chain <<<")
    part4_refine_chain.main()

    print("\n>>> PART 5: Document Summarizer Mini Project <<<")
    part5_document_summarizer.main()

    print("\n>>> TASK 14: Observations & Conceptual Insights <<<")
    task14_observations.main()

    print("\n" + "=" * 65)
    print("All tasks completed successfully!")
    print("=" * 65)


if __name__ == "__main__":
    main()
