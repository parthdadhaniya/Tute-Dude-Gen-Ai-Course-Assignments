# Part 1: Text-to-Math Agent Overview (Task 1)
# Student: Parth Dadhaniya


def print_overview():
    print("=" * 60)
    print("Task 1: Text-to-Math Agent Overview")
    print("Student: Parth Dadhaniya")
    print("=" * 60)

    print("\n1. What is a Text-to-Math problem?")
    print("   A Text-to-Math problem is a natural language word problem that requires understanding")
    print("   context, identifying numerical quantities, formulating mathematical expressions,")
    print("   and executing calculations to reach the correct solution.")

    print("\n2. Why are AI Agents useful for math reasoning?")
    print("   - Standard LLMs are trained to predict the next word, not do arithmetic. They often hallucinate")
    print("     multiplication, multi-digit operations, and percentages.")
    print("   - An AI Agent bridges this gap by combining natural language comprehension with external tools")
    print("     (like a Python calculator or SymPy engine), delegating the actual math to a deterministic tool.")

    print("\n3. Difference between normal LLM response vs Agent-based reasoning:")
    print("   - Normal LLM : Generates text directly from memory/weights. Arithmetic errors happen easily")
    print("                  and cannot be verified or self-corrected.")
    print("   - Agent (ReAct): Uses 'Thought -> Action -> Observation' steps. The agent decides what calculation")
    print("                    is needed, executes the calculator tool, verifies the result, and uses that verified")
    print("                    number to finish solving the problem.")


def main():
    print_overview()


if __name__ == "__main__":
    main()
