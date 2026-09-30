# Part 3: Connecting to MySQL Workbench Database
# Student: Parth Dadhaniya

import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from part2_database_engine import get_langchain_sqldb

load_dotenv()

# MySQL Workbench Connection Parameters
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "company_db")

MYSQL_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"


def get_database(preferred="sqlite"):
    """
    Returns SQLDatabase object for either MySQL Workbench or SQLite.
    Allows seamless communication with both database backends.
    """
    if preferred == "mysql":
        try:
            db = SQLDatabase.from_uri(MYSQL_URI)
            # Test connection
            db.get_usable_table_names()
            return db, "MySQL Workbench (company_db)"
        except Exception as e:
            print(f"Notice: Could not connect to MySQL Workbench ({e}).")
            print("Falling back to local SQLite 'company.db' for seamless execution.")

    # Default to SQLite
    db = get_langchain_sqldb()
    return db, "SQLite (company.db)"


def main():
    print("--- Part 3: MySQL Workbench Configuration & Connection ---")
    print(f"MySQL Host     : {MYSQL_HOST}")
    print(f"MySQL Port     : {MYSQL_PORT}")
    print(f"MySQL User     : {MYSQL_USER}")
    print(f"Target DB      : {MYSQL_DB}")
    print(f"Generated URI  : mysql+pymysql://{MYSQL_USER}:****@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}")
    print(f"Workbench File : company_workbench.sql (ready to execute in MySQL Workbench)\n")

    # Connect and inspect
    db, active_backend = get_database(preferred="mysql")
    print(f"Active Connected Backend: {active_backend}")
    print(f"Discovered Tables       : {db.get_usable_table_names()}")


if __name__ == "__main__":
    main()
