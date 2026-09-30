# main.py - Runs all tasks for Assignment 33
# Student: Parth Dadhaniya

import part1_sqlite_database
import part2_database_engine
import part3_mysql_workbench
import part4_sql_agent
import part5_safety_ambiguity
import task11_observations


def main():
    print("=" * 60)
    print("Assignment 33: Chat with SQL Database using LangChain")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n--- Part 1: SQLite Database Setup ---")
    part1_sqlite_database.main()

    print("\n--- Part 2: SQLAlchemy Engine & LangChain SQLDatabase ---")
    part2_database_engine.main()

    print("\n--- Part 3: MySQL Workbench Configuration ---")
    part3_mysql_workbench.main()

    print("\n--- Part 4: SQL Agent with LangChain SQL Toolkit ---")
    part4_sql_agent.main()

    print("\n--- Part 5: Safe Execution & Handling Ambiguity ---")
    part5_safety_ambiguity.main()

    print("\n--- Task 11: Conceptual Observations ---")
    task11_observations.main()

    print("\n" + "=" * 60)
    print("All tasks finished successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
