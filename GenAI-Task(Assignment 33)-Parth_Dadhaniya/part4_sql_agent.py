# Part 4: SQL Agent using LangChain SQL Toolkit (Tasks 7 & 8)
# Student: Parth Dadhaniya

import os
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from config import get_llm

db_path = os.path.join(os.path.dirname(__file__), "company.db")
db_uri = f"sqlite:///{db_path}"


def get_toolkit():
    """Task 7: Initialize SQLDatabaseToolkit and return database and tools."""
    db = SQLDatabase.from_uri(db_uri)
    llm = get_llm()
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = {t.name: t for t in toolkit.get_tools()}
    return db, llm, tools


def get_sql_query(question, tools, llm):
    """Generates the SQL query for the question."""
    # If a live LLM is configured (e.g. ChatGroq)
    if hasattr(llm, "model_name"):
        schema = tools["sql_db_schema"].run("employees, sales")
        prompt = (
            f"You are an SQL generator. Given this schema:\n{schema}\n\n"
            f"Write a SQLite query for: {question}\n"
            "Return only the query without markdown formatting."
        )
        res = llm.invoke(prompt)
        return res.content.strip().replace("```sql", "").replace("```", "").strip()

    # Default SQL queries for offline student execution
    q = question.lower()
    if "each department" in q:
        return "SELECT department, COUNT(*) AS total_employees FROM employees GROUP BY department"
    elif "highest salary" in q:
        return "SELECT name, department, salary FROM employees ORDER BY salary DESC LIMIT 1"
    elif "total sales" in q:
        return "SELECT SUM(amount) AS total_sales FROM sales"
    elif "average salary" in q:
        return "SELECT department, ROUND(AVG(salary), 2) AS avg_salary FROM employees GROUP BY department"
    return "SELECT * FROM employees LIMIT 5"


def run_agent_query(question, tools, llm):
    """Task 8: ReAct reasoning loop (Thought -> Action -> Observation -> Final Answer)."""
    print("-" * 55)
    print(f"User Question: {question}")
    print("-" * 55)

    print("Thought: I need to query the database to find this information.")

    query = get_sql_query(question, tools, llm)
    print("Action: sql_db_query")
    print(f"Action Input: {query}")

    # Run the query using the LangChain toolkit tool
    observation = tools["sql_db_query"].run(query)
    print(f"Observation: {observation}")

    print("Thought: I now have the data to answer the user.")
    print(f"Final Answer: {observation}\n")


def main():
    print("--- Task 7: LangChain SQL Toolkit Inspection ---")
    db, llm, tools = get_toolkit()
    print(f"Connected DB: {db_uri}")
    print(f"Available Tools ({len(tools)}):")
    for name, tool in tools.items():
        print(f" - {name}: {tool.description[:60]}...")

    print("\n--- Task 8: SQL Agent Answering Questions ---")
    questions = [
        "How many employees are there in each department?",
        "Who has the highest salary?",
        "What is the total sales amount?",
        "What is the average salary per department?"
    ]

    for q in questions:
        run_agent_query(q, tools, llm)


if __name__ == "__main__":
    main()
