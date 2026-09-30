# Part 1: Tools in AI Agents (Tasks 1 & 2)
# Student: Parth Dadhaniya

import datetime
from langchain_core.tools import tool


def explain_tools():
    print("--- Task 1: Understanding Tools ---")
    print("1. What is a tool in an AI Agent?")
    print("A tool is a function or utility that an agent can call to interact with external data, perform calculations, or run API calls.\n")

    print("2. Why do agents need tools?")
    print("LLMs alone cannot do precise math, don't have real-time info, and cannot run actions. Tools give them capabilities beyond static text generation.\n")

    print("3. Difference between a chatbot and an agent:")
    print("A chatbot only returns text responses in a single turn. An agent can reason, pick tools, run them, observe results, and repeat steps until a goal is met.\n")


# Task 2: Define 3 tools
@tool
def calculator(expression: str) -> str:
    """Useful for doing math calculations like addition, multiplication, division."""
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in expression):
            return "Error: Invalid math expression."
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@tool
def search_knowledge(query: str) -> str:
    """Useful for searching general knowledge and factual information."""
    data = {
        "alan turing": "Alan Turing was an English mathematician and computer scientist who pioneered artificial intelligence.",
        "langchain": "LangChain is a framework that makes it easy to build LLM applications with tools and memory.",
        "python": "Python is a popular programming language widely used in AI and data science."
    }
    q = query.lower()
    for topic, text in data.items():
        if topic in q:
            return text
    return f"Search result for '{query}': relevant facts found."


@tool
def get_current_time(dummy: str = "") -> str:
    """Useful for getting the current system date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    explain_tools()

    print("--- Task 2: Testing Tools Individually ---")
    # 1. Calculator
    res1 = calculator.invoke({"expression": "15 * 8 + 40"})
    print(f"Calculator ('15 * 8 + 40') -> {res1}")

    # 2. Search
    res2 = search_knowledge.invoke({"query": "Alan Turing"})
    print(f"Search ('Alan Turing') -> {res2}")

    # 3. Time
    res3 = get_current_time.invoke({})
    print(f"Current Time -> {res3}")


if __name__ == "__main__":
    main()
