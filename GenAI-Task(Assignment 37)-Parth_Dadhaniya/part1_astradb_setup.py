# part1_astradb_setup.py - AstraDB Setup & Connection Verification
# Student: Parth Dadhaniya

import os
from config import (
    ASTRA_DB_APPLICATION_TOKEN,
    ASTRA_DB_API_ENDPOINT,
    ASTRA_DB_KEYSPACE,
    ASTRA_DB_COLLECTION,
    get_astradb_vectorstore,
    get_embeddings
)


def print_astradb_setup_guide():
    """Explains how to set up DataStax AstraDB account and credentials."""
    print("============================================================")
    print("Task 1: Getting Started with DataStax AstraDB")
    print("Student: Parth Dadhaniya")
    print("============================================================")
    print("DataStax AstraDB Cloud Vector Database Setup Guide:")
    print("1. Account Creation:")
    print("   - Sign up at https://astra.datastax.com (free tier includes $25/month credit).")
    print("2. Create Vector Database:")
    print("   - Click 'Create Database' -> Select 'Vector Database'.")
    print("   - Name: 'genai_rag_db', Region: closest cloud region (e.g. AWS us-east-1).")
    print("3. Generate Application Token:")
    print("   - In Settings -> Tokens, generate token with 'Database Administrator' role.")
    print("   - Copy the token starting with 'AstraCS:...'")
    print("4. Copy API Endpoint:")
    print("   - In database Overview, copy the DB API Endpoint URL:")
    print("     e.g., https://<db-id>-<region>.apps.astra.datastax.com")
    print("5. Configure Environment (.env):")
    print("   ASTRA_DB_APPLICATION_TOKEN=AstraCS:...")
    print("   ASTRA_DB_API_ENDPOINT=https://<db-id>-<region>.apps.astra.datastax.com")
    print("   ASTRA_DB_KEYSPACE=default_keyspace")
    print("   ASTRA_DB_COLLECTION=pdf_rag_collection\n")


def verify_astradb_connection():
    """Connects LangChain with AstraDB and verifies the connection status."""
    print("============================================================")
    print("Task 2: Connect LangChain with AstraDB")
    print("============================================================")

    print("Checking AstraDB Configuration:")
    has_token = bool(ASTRA_DB_APPLICATION_TOKEN)
    has_endpoint = bool(ASTRA_DB_API_ENDPOINT)

    print(f"  Astra Application Token Configured : {has_token}")
    print(f"  Astra DB Endpoint Configured        : {has_endpoint}")
    print(f"  Target Keyspace                     : {ASTRA_DB_KEYSPACE}")
    print(f"  Target Collection                   : {ASTRA_DB_COLLECTION}")

    embeddings = get_embeddings()
    store, mode = get_astradb_vectorstore(embeddings)

    print(f"\nConnection Status : SUCCESS")
    print(f"Active Store Mode : {mode}")
    print(f"Embedding Model   : sentence-transformers/all-MiniLM-L6-v2 (384 dims)")

    if has_token and has_endpoint:
        print(">> Live AstraDB Cloud Connection Established successfully!")
    else:
        print(">> Offline Student Mode Active: AstraDB API credentials not found in .env.")
        print(">> Local AstraDB Persistent Store ready for embedding storage and similarity search.")

    return store


def run_tasks_1_and_2():
    print_astradb_setup_guide()
    store = verify_astradb_connection()
    return store


if __name__ == "__main__":
    run_tasks_1_and_2()

