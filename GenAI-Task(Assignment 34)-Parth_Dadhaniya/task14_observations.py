# Task 14: Observations & Conceptual Insights
# Student: Parth Dadhaniya


def print_observations():
    print("=" * 60)
    print("Task 14: Summarization Observations & Insights")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n1. Best summarization strategy for very long documents:")
    print("- For truly massive documents (books, 100+ page reports, transcripts), Map-Reduce is the best")
    print("  choice because it can process chunks in parallel across multiple threads or API workers.")
    print("- Refine is ideal when deep narrative coherence is paramount and latency is secondary, as it")
    print("  allows subsequent sections to update and contextualize prior findings.")

    print("\n2. Trade-offs between speed and quality:")
    print("- Speed & Latency : Stuff (1 call, fastest) > Map-Reduce (parallel chunk calls) > Refine (sequential, slowest).")
    print("- Summary Quality : Refine produces the smoothest narrative; Stuff is great for short texts;")
    print("                    Map-Reduce provides a high-level executive view but can feel slightly fragmented.")
    print("- Token Cost      : Stuff uses the fewest tokens. Refine sends the running summary repeatedly,")
    print("                    incurring higher cumulative token costs.")

    print("\n3. Real-world use cases for each method:")
    print("- Prompt-Based : Customer support tickets, short emails, news snippets.")
    print("- Stuff Chain  : 1-3 page company memos, short articles, meeting minutes fitting in context.")
    print("- Map-Reduce   : Earnings call transcripts, quarterly 10-Q reports, multi-chapter whitepapers.")
    print("- Refine       : Legal contract audits, medical records, research surveys where chronological")
    print("                 continuity and progressive nuance are critical.")


def main():
    print_observations()


if __name__ == "__main__":
    main()
