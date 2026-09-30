# Part 2: Creating LangChain Database Engine (Tasks 3 & 4)
# Student: Parth Dadhaniya

import os
from sqlalchemy import create_engine, inspect
from langchain_community.utilities import SQLDatabase

db_path = os.path.join(os.path.dirname(__file__), "company.db")
db_uri = f"sqlite:///{db_path}"


def get_sqlalchemy_engine():
    """Task 3: Create SQLAlchemy database engine and fetch table names."""
    engine = create_engine(db_uri)
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    return engine, table_names


def get_langchain_sqldb():
    """Task 4: Create LangChain SQLDatabase object."""
    db = SQLDatabase.from_uri(db_uri)
    return db


def main():
    print("--- Task 3: SQLAlchemy Engine Connection ---")
    engine, tables = get_sqlalchemy_engine()
    print(f"Connected to SQLite URI: {db_uri}")
    print(f"Discovered Tables: {tables}")

    print("\n--- Task 4: LangChain SQLDatabase Object ---")
    db = get_langchain_sqldb()
    print(f"Usable Tables in LangChain SQLDatabase: {db.get_usable_table_names()}\n")

    print("Table Schema & Sample Rows:")
    print(db.get_table_info())


if __name__ == "__main__":
    main()
