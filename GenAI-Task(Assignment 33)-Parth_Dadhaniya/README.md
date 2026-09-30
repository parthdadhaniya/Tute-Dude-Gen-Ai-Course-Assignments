# Assignment 33: Chat with SQL Database using LangChain

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I built an end-to-end **Chat with SQL Database** application using LangChain. Enterprise organizations store their most critical operational data in relational databases (RDBMS). This project enables non-technical business stakeholders to ask questions in plain natural language, which an AI SQL Agent translates into SQL queries, executes dynamically on the database engine, and returns as conversational answers.

Key concepts implemented:
1. **SQLite Database Setup:** Created `company.db` with `employees` and `sales` tables populated with realistic company records.
2. **LangChain SQL Engine:** Connected to the database using SQLAlchemy engine and LangChain's `SQLDatabase.from_uri()` wrapper to inspect schemas and sample rows.
3. **MySQL Workbench Integration:** Provided `company_workbench.sql` for MySQL Workbench setups and implemented Python connection logic with automatic SQLite fallback.
4. **LangChain SQL Database Toolkit:** Initialized `SQLDatabaseToolkit` and leveraged built-in tools (`sql_db_query`, `sql_db_schema`, `sql_db_list_tables`, and `sql_db_query_checker`).
5. **SQL Agent Execution:** Executed ReAct reasoning (`Thought -> Action -> Observation -> Final Answer`) across 4 key business queries dynamically without hardcoding.
6. **Safety & Ambiguity Guardrails:** Enforced read-only safety blocking destructive commands (`DROP`, `DELETE`, `UPDATE`) and gracefully handled vague prompts or missing tables.
7. **Conceptual Analysis:** Explored SQL Agents vs manual queries, SQL Agents vs RAG pipelines, and security risks of write access.

---

## File Structure

```text
GenAI-Task(Assignment 33)-Parth_Dadhaniya/
├── company.db                   # SQLite database with employees & sales tables
├── company_workbench.sql        # MySQL Workbench database & table seed script
├── config.py                    # LLM configuration (ChatGroq / ChatOpenAI with student fallback)
├── part1_sqlite_database.py     # Tasks 1 & 2: SQLite database creation & seed verification
├── part2_database_engine.py     # Tasks 3 & 4: SQLAlchemy engine & LangChain SQLDatabase
├── part3_mysql_workbench.py     # Tasks 5 & 6: MySQL Workbench setup & connection logic
├── part4_sql_agent.py           # Tasks 7 & 8: SQLDatabaseToolkit & SQL Agent execution
├── part5_safety_ambiguity.py    # Tasks 9 & 10: Query safety guardrails & ambiguous query handling
├── task11_observations.py      # Task 11: Conceptual analysis & Q&A
├── main.py                      # Master script executing all parts sequentially
├── assignment33.ipynb           # Interactive Jupyter Notebook
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Task Details

### Part 1: Storing Data in SQLite Database (Tasks 1 & 2)
- Created SQLite database file `company.db`.
- Created two normalized tables:
  - `employees` (`id`, `name`, `department`, `salary`)
  - `sales` (`sale_id`, `employee_id`, `amount`, `sale_date`)
- Inserted 10 realistic employee records and 10 sales transaction records.
- Verified row counts and aggregations using native SQL queries.

### Part 2: Creating LangChain Database Engine (Tasks 3 & 4)
- Created SQLAlchemy engine connected to `sqlite:///company.db`.
- Extracted table names using SQLAlchemy `inspect()`.
- Created LangChain `SQLDatabase.from_uri("sqlite:///company.db")`.
- Inspected available tables and schema information via `db.get_table_info()`.

### Part 3: Connecting to MySQL Workbench (Tasks 5 & 6)
- Provided `company_workbench.sql` script to create database `company_db` and seed tables in MySQL Workbench.
- Configured PyMySQL connection string: `mysql+pymysql://root:password@localhost:3306/company_db`.
- Implemented smart fallback to local `company.db` when MySQL server is not running locally.

### Part 4: SQL Agent using LangChain SQL Toolkit (Tasks 7 & 8)
- Grouped database tools using `SQLDatabaseToolkit(db=db, llm=llm)`.
- Inspected the 4 toolkit tools: `sql_db_query`, `sql_db_schema`, `sql_db_list_tables`, and `sql_db_query_checker`.
- Implemented the SQL Agent and answered 4 required business queries dynamically:
  1. *"How many employees are there in each department?"* -> Groups by department with counts.
  2. *"Who has the highest salary?"* -> Orders by salary descending with limit 1.
  3. *"What is the total sales amount?"* -> Computes `SUM(amount)` over sales.
  4. *"What is the average salary per department?"* -> Computes `ROUND(AVG(salary), 2)` grouped by department.
- Output displays full verbose reasoning: `Thought -> Action -> Action Input -> Observation -> Final Answer`.

### Part 5: Agent Safety & Ambiguous Queries (Tasks 9 & 10)
- **Safe Execution (Read-Only Guard):** Intercepts and blocks destructive DDL/DML keywords (`DROP`, `DELETE`, `UPDATE`, `ALTER`, `TRUNCATE`, `INSERT`).
- **Ambiguous Queries:** Handled `"Who is the best employee?"` by recognizing lack of predefined metrics and presenting both highest salary and highest sales volume.
- **Non-Existent Entities:** Handled `"Show bonus details"` by checking schema, identifying that `bonus` does not exist, and reporting available tables.

### Task 11: Conceptual Observations & Q&A
- **SQL Agent vs Manual SQL:** Enables non-technical users to access data, automates schema discovery, self-heals syntax errors, and explains results conversationally.
- **SQL Agent vs RAG:** RAG handles unstructured documents via approximate cosine similarity; SQL Agent operates on structured relational tables executing exact deterministic math.
- **Risks of Unrestricted SQL Access:** Hallucinated data drops, prompt injection attacks, and performance locks. Mitigated by read-only user permissions, query limits, and human-in-the-loop approvals.

---

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys (Optional):**
   Create a `.env` file in the root workspace or assignment folder:
   ```env
   GROQ_API_KEY=your_groq_api_key
   # or
   OPENAI_API_KEY=your_openai_api_key
   ```
   *(Note: If no API key is provided, the project runs seamlessly offline using the built-in student SQL generator).*

3. **Run Master Script:**
   ```bash
   python main.py
   ```

4. **Run Individual Scripts:**
   ```bash
   python part1_sqlite_database.py
   python part2_database_engine.py
   python part3_mysql_workbench.py
   python part4_sql_agent.py
   python part5_safety_ambiguity.py
   python task11_observations.py
   ```

5. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook assignment33.ipynb
   ```
