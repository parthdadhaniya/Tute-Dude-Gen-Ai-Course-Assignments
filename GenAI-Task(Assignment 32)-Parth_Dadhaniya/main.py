# Assignment 32: AI Agents using LangChain
# Student: Parth Dadhaniya

import part1_tools_intro
import part2_custom_tools
import part3_tool_calling
import part4_react_agent
import part5_assistant_agent
import task11_observations


def main():
    print("=" * 55)
    print("Assignment 32: AI Agents using LangChain")
    print("Student: Parth Dadhaniya")
    print("=" * 55)

    print("\n[Step 1] Tools in AI Agents (Tasks 1 & 2)")
    part1_tools_intro.main()

    print("\n[Step 2] Custom Tools & Toolkits (Tasks 3 & 4)")
    part2_custom_tools.main()

    print("\n[Step 3] Tool Binding & Calling Flow (Tasks 5 & 6)")
    part3_tool_calling.main()

    print("\n[Step 4] ReAct AI Agent (Tasks 7 - 9)")
    part4_react_agent.main()

    print("\n[Step 5] Assistant Agent & Insights (Tasks 10 & 11)")
    part5_assistant_agent.main()
    task11_observations.main()

    print("=" * 55)
    print("All Assignment 32 tasks completed successfully.")
    print("=" * 55)


if __name__ == "__main__":
    main()
