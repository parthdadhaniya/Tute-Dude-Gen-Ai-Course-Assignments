# Task 11: Conceptual Observations
# Student: Parth Dadhaniya


def print_observations():
    print("=" * 60)
    print("Task 11: Observations & Conceptual Q&A")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n1. Why is an SQL Agent better than manually writing SQL queries?")
    print("- Non-technical business users can ask questions in plain English without knowing SQL.")
    print("- The agent reads the table schemas automatically so users don't need to remember column names.")
    print("- If a query fails with a syntax error, the agent can look at the error message and fix it automatically.")
    print("- It returns clear, friendly conversational answers instead of just raw database tuples.")

    print("\n2. What is the difference between an SQL Agent and RAG (Retrieval-Augmented Generation)?")
    print("- Data Type: RAG works on unstructured text like PDFs, docs, or web pages. SQL Agents work on structured tabular data in databases.")
    print("- Search Method: RAG searches by vector similarity (embeddings). SQL Agent generates exact SQL queries (SELECT, GROUP BY, WHERE).")
    print("- Accuracy: RAG struggles with exact calculations (sums, averages, counts). An SQL Agent executes exact math using the database engine.")

    print("\n3. What are the risks of giving an LLM unrestricted SQL write access?")
    print("- Data Loss: The model might accidentally run DROP TABLE or DELETE without a WHERE clause and wipe out data.")
    print("- Security: Attackers could use prompt injection to alter records or read sensitive data.")
    print("- Performance: Badly written queries could lock tables and slow down the system.")
    print("- Prevention: Always use read-only database permissions and human approval before making any changes.")


def main():
    print_observations()


if __name__ == "__main__":
    main()
