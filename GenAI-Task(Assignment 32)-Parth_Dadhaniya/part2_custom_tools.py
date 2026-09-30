# Part 2: Custom Tools & Toolkits (Tasks 3 & 4)
# Student: Parth Dadhaniya

from langchain_core.tools import tool
from part1_tools_intro import calculator, get_current_time


# Task 3: Custom Tool
@tool
def company_policy_lookup(query: str) -> str:
    """Returns company policy information regarding leaves, remote work, and expenses."""
    policies = {
        "leave": "Employees get 20 days of paid annual leave, 10 sick days, and 5 personal days.",
        "remote": "Employees can work remotely up to 3 days per week with manager approval.",
        "expense": "Daily travel meal allowance is up to $75 with valid receipts."
    }
    q = query.lower()
    for topic, answer in policies.items():
        if topic in q:
            return answer
    return "Policy not found. Try searching for leave, remote, or expense."


@tool
def employee_lookup(name: str) -> str:
    """Finds employee title and department by name."""
    employees = {
        "parth": "Parth Dadhaniya | AI Engineer | Department: AI Research",
        "alice": "Alice Johnson | Lead Developer | Department: Engineering",
        "bob": "Bob Smith | DevOps Specialist | Department: Infrastructure"
    }
    for emp_name, details in employees.items():
        if emp_name in name.lower():
            return details
    return f"No records found for '{name}'."


# Task 4: Custom Toolkit
def get_company_toolkit():
    return [
        company_policy_lookup,
        employee_lookup,
        calculator,
        get_current_time
    ]


def main():
    print("--- Task 3: Testing Custom Tool ---")
    query = "What is the policy for annual leave?"
    print(f"Query: {query}")
    print(f"Result: {company_policy_lookup.invoke({'query': query})}\n")

    print("--- Task 4: Testing Custom Toolkit ---")
    tools = get_company_toolkit()
    print(f"Tools in toolkit: {[t.name for t in tools]}")
    emp_res = employee_lookup.invoke({"name": "Parth"})
    print(f"Employee lookup test -> {emp_res}")


if __name__ == "__main__":
    main()
