# Assignment 28: Q&A RAG Chatbot with Message History
# Student: Parth Dadhaniya

from part1_document_ingestion import load_documents, split_documents
from part2_vector_store import get_vectorstore, test_retriever
from part3_part4_rag_chain import test_chain_demo
from part5_testing import run_multi_turn_rag_test
from part6_chatbot_app import run_mini_project_demo
from task11_observations import task11_observations


def main():
    print("=" * 60)
    print("Assignment 28: Q&A RAG Chatbot with Message History")
    print("Student: Parth Dadhaniya | TuteDude Gen AI Course")
    print("=" * 60)

    # Part 1: Document Ingestion (Tasks 1 & 2)
    docs = load_documents()
    chunks = split_documents(docs)

    # Part 2: Vector Store & Retriever (Tasks 3 & 4)
    get_vectorstore()
    test_retriever()

    # Part 3 & 4: RAG Chain with Message History & Trimming (Tasks 5, 6, 7, 8)
    test_chain_demo()

    # Part 5: Multi-Turn Q&A Testing (Task 9)
    run_multi_turn_rag_test()

    # Part 6: Mini Project Stateful RAG Chatbot (Task 10)
    run_mini_project_demo()

    # Part 6: Observations & Insights (Task 11)
    task11_observations()

    print("=" * 60)
    print("All Assignment 28 tasks completed successfully!")
    print("Optional Streamlit app: streamlit run streamlit_app.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
