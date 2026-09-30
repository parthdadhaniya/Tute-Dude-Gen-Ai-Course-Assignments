# Part 4: ReAct AI Agent (Tasks 7, 8 & 9)
# Student: Parth Dadhaniya

import re
from config import get_llm
from part1_tools_intro import calculator, search_knowledge
from part2_custom_tools import company_policy_lookup


def explain_react():
    print("--- Task 7: ReAct Agent Overview ---")
    print("1. What is ReAct (Reason + Act)?")
    print("ReAct combines reasoning ('Thought') with taking actions ('Action') and observing feedback ('Observation').\n")

    print("2. Why ReAct agents are powerful:")
    print("By thinking before taking an action and observing tool outputs before answering, the model avoids guessing and can solve multi-step problems reliably.\n")


# Task 8: ReAct Agent Loop
def run_react_agent(question, tools, llm=None, max_steps=4):
    if llm is None:
        llm = get_llm()
    tools_by_name = {t.name: t for t in tools}

    print("=" * 45)
    print(f"Question: {question}")
    print("=" * 45)

    scratchpad = ""
    for _ in range(max_steps):
        prompt = f"Question: {question}\n{scratchpad}Thought:"
        res = llm.invoke(prompt)
        text = res.content.strip()

        if "Final Answer:" in text:
            print(text)
            return

        # Look for Action and Action Input
        act_match = re.search(r"Action:\s*(\w+)", text)
        inp_match = re.search(r"Action Input:\s*(.+)", text)

        if act_match and inp_match:
            action = act_match.group(1).strip()
            action_input = inp_match.group(1).strip()

            print(text)

            # Call tool
            if action in tools_by_name:
                t = tools_by_name[action]
                try:
                    obs = t.invoke(action_input)
                except Exception:
                    obs = t.invoke({"query": action_input} if "query" in str(t.args) else {"expression": action_input})
            else:
                obs = f"Tool {action} not found."

            print(f"Observation: {obs}")
            scratchpad += f"{text}\nObservation: {obs}\n"
        else:
            print(text)
            return


def main():
    explain_react()

    print("--- Tasks 8 & 9: Testing ReAct Agent ---")
    agent_tools = [calculator, company_policy_lookup, search_knowledge]

    # Test 1: Math calculation
    run_react_agent("Calculate 15 * 8", agent_tools)

    # Test 2: Policy lookup
    run_react_agent("What is our company policy on annual leave?", agent_tools)

    # Test 3: Knowledge search
    run_react_agent("Who is Alan Turing?", agent_tools)


if __name__ == "__main__":
    main()
