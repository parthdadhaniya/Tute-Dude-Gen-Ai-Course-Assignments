# Part 5: Agent Safety & Ambiguous Queries (Tasks 9 & 10)
# Student: Parth Dadhaniya

import os
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from config import get_llm

db_path = os.path.join(os.path.dirname(__file__), "company.db")
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
toolkit = SQLDatabaseToolkit(db=db, llm=get_llm())
tools = {t.name: t for t in toolkit.get_tools()}

# Task 9: Safety Guardrails
# We prevent dangerous DDL/DML queries from running against the database
FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]


def check_and_run_query(query):
    """Verifies that the query is read-only before executing."""
    words = [w.strip(";").upper() for w in query.split()]
    for bad_word in FORBIDDEN_KEYWORDS:
        if bad_word in words:
            print(f"Safety Check: BLOCKED! '{bad_word}' command is not allowed in read-only mode.")
            return f"Blocked: Operation '{bad_word}' is forbidden."

    print("Safety Check: Allowed (Read-only SELECT).")
    return tools["sql_db_query"].run(query)


# Task 10: Handling Ambiguous and Invalid Queries
def handle_ambiguous_query(question):
    print("\n" + "-" * 55)
    print(f"Question: {question}")
    print("-" * 55)

    q = question.lower()
    tables = db.get_usable_table_names()

    # Case 1: Best employee - ambiguous definition
    if "best employee" in q:
        print("Thought: 'Best employee' has no single definition in the database.")
        print("Thought: Checking top salary and top sales amount to provide alternatives.")

        highest_paid = tools["sql_db_query"].run("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1")
        top_seller = tools["sql_db_query"].run("SELECT employee_id, SUM(amount) FROM sales GROUP BY employee_id ORDER BY 2 DESC LIMIT 1")

        print(f"Final Answer: The query is ambiguous because 'best' could mean:")
        print(f" - Highest salary: {highest_paid}")
        print(f" - Highest total sales: Employee ID {top_seller}")
        print(" Please specify if you want top sales or highest salary.")

    # Case 2: Non-existent table
    elif "bonus" in q:
        print("Thought: User is asking for bonuses. Checking existing database tables.")
        print(f"Action: sql_db_list_tables")
        print(f"Observation: Available tables are {tables}")
        print("Thought: Neither 'employees' nor 'sales' contains a bonus table.")
        print(f"Final Answer: The table 'bonus' does not exist in the database. Available tables: {tables}")


def main():
    print("--- Task 9: Safe Execution Guardrails ---")
    test_queries = [
        "SELECT name, department FROM employees WHERE salary > 80000",
        "DROP TABLE employees;",
        "DELETE FROM sales WHERE amount < 2000;",
    ]

    for q in test_queries:
        print(f"\nAttempting Query: {q}")
        result = check_and_run_query(q)
        print(f"Result: {result}")

    print("\n--- Task 10: Handling Ambiguous Queries ---")
    handle_ambiguous_query("Who is the best employee?")
    handle_ambiguous_query("Show bonus details for employees")


if __name__ == "__main__":
    main()
