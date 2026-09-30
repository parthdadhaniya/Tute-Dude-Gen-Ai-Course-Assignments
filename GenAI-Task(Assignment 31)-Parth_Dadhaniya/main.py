# Assignment 31: Conversational PDF Q&A Chatbot with Message History
# Student: Parth Dadhaniya

import part1_pdf_ingestion
import part2_vector_store
import part3_part4_rag_chain
import part5_testing
import task11_observations


def main():
    print("=" * 60)
    print("Assignment 31: Conversational PDF Q&A Chatbot")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n[Step 1] PDF Ingestion & Text Splitting (Tasks 1 & 2)")
    part1_pdf_ingestion.main()

    print("\n[Step 2] Embeddings & ChromaDB (Tasks 3 & 4)")
    part2_vector_store.main()

    print("\n[Step 3] Conversational RAG Chain & Trimming (Tasks 5 - 8)")
    part3_part4_rag_chain.main()

    print("\n[Step 4] Multi-Turn Follow-Up Q&A Testing (Task 9)")
    part5_testing.main()

    print("\n[Step 5] Observations & Insights (Task 11)")
    task11_observations.main()

    print("=" * 60)
    print("All tasks completed.")
    print("To launch the Streamlit app: streamlit run app.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
