# part4_observations.py - Observations & Architectural Insights
# Student: Parth Dadhaniya


def print_observations_and_insights():
    """Prints concise, comprehensive answers to the three core assignment questions."""
    print("============================================================")
    print("Observations & Architectural Insights")
    print("Student: Parth Dadhaniya")
    print("============================================================\n")

    print("1. Why AstraDB is Useful for Production RAG:")
    print("   - Serverless Cloud Native: Eliminates the overhead of provisioning, patching, and tuning")
    print("     self-managed vector clusters (like raw Milvus or self-hosted Qdrant).")
    print("   - Built on Apache Cassandra: Delivers proven high availability (99.999%), horizontal scaling,")
    print("     and sub-millisecond read/write latency across billions of vector embeddings.")
    print("   - Native Metadata Filtering: Allows combining vector ANN search with structured relational")
    print("     predicates (e.g., filter by tenant_id, security clearance, or timestamp) in a single query.")
    print("   - Enterprise Compliance: Includes automated multi-region replication, continuous backups,")
    print("     SOC2 Type II, HIPAA, and PCI-DSS compliance out of the box.\n")

    print("2. Importance of Session State in GenAI Applications:")
    print("   - Conversational Continuity: Large Language Models are completely stateless HTTP endpoints.")
    print("     Session state (e.g. Streamlit `st.session_state` or LangChain `MessagesPlaceholder`) preserves")
    print("     conversation history so users can ask contextual follow-ups (e.g. 'explain that in more detail').")
    print("   - UI Persistence: In reactive web frameworks like Streamlit, the entire script re-executes on")
    print("     every user interaction; session state preserves uploaded documents, vector store instances,")
    print("     and message logs across UI reruns.")
    print("   - Memory Management & Cost Optimization: Allows sliding-window history trimming, summarizing past")
    print("     turns to keep context sizes within LLM token budgets and minimize per-turn token costs.\n")

    print("3. Comprehensive Comparison: FAISS vs DataStax AstraDB:")
    print("-" * 75)
    print(f"{'Feature':<22} | {'FAISS (Meta)':<24} | {'DataStax AstraDB':<24}")
    print("-" * 75)
    print(f"{'Architecture':<22} | {'Local C++ library':<24} | {'Distributed cloud DB':<24}")
    print(f"{'Persistence':<22} | {'In-memory / Manual dump':<24} | {'Automatic persistent disk':<24}")
    print(f"{'Scalability':<22} | {'Single-node RAM/GPU limit':<24} | {'Petabyte / Multi-region':<24}")
    print(f"{'Concurrency':<22} | {'No built-in multi-user':<24} | {'High concurrent access':<24}")
    print(f"{'Security & RBAC':<22} | {'None (file system level)':<24} | {'Role-based tokens & IAM':<24}")
    print(f"{'Maintenance':<22} | {'Self-managed':<24} | {'Fully managed serverless':<24}")
    print("-" * 75)


def main():
    print_observations_and_insights()


if __name__ == "__main__":
    main()

