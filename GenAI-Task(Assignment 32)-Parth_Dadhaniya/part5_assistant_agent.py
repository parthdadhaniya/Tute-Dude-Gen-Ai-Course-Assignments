# Part 5: Mini Project - AI Agent Assistant (Task 10)
# Student: Parth Dadhaniya

from part4_react_agent import run_react_agent
from part1_tools_intro import calculator, search_knowledge, get_current_time
from part2_custom_tools import company_policy_lookup, employee_lookup


def main():
    print("--- Task 10: AI Assistant Agent Mini Project ---")
    tools = [
        calculator,
        company_policy_lookup,
        employee_lookup,
        search_knowledge,
        get_current_time
    ]

    queries = [
        "What is the company leave policy?",
        "Calculate 15 * 8",
        "Who is Alan Turing?"
    ]

    for q in queries:
        run_react_agent(q, tools)
        print()


if __name__ == "__main__":
    main()
