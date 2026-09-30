# Assignment 32: AI Agents using LangChain

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I transitioned from passive chatbots to autonomous **AI Agents** using LangChain. Unlike standard chatbots that only generate text from weights or static context, an AI agent can dynamically reason, choose external tools, inspect execution feedback, and take goal-oriented actions.

Key concepts implemented:
1. **Built-in & Custom Tools:** Using the `@tool` decorator to create modular capabilities (math calculation, Wikipedia lookup, datetime, and company policy lookup).
2. **Toolkits:** Grouping related tools into a cohesive `CompanyToolkit` for enterprise workflows.
3. **Tool Binding & Calling:** Using `llm.bind_tools(tools)` to let the model inspect tool schemas and generate structured tool-call requests.
4. **ReAct Architecture:** Implementing the Reason + Act pattern (`Thought -> Action -> Action Input -> Observation -> Final Answer`).
5. **Autonomous Decision-Making:** Testing multi-step reasoning traces across math, factual research, and policy retrieval.

---

## File Structure

```text
GenAI-Task(Assignment 32)-Parth_Dadhaniya/
├── config.py                 # LLM configuration (ChatGroq with offline fallback)
├── part1_tools_intro.py      # Tasks 1 & 2: Conceptual overview & built-in tools
├── part2_custom_tools.py     # Tasks 3 & 4: Custom tools & CompanyToolkit
├── part3_tool_calling.py     # Tasks 5 & 6: Tool binding and calling flow
├── part4_react_agent.py      # Tasks 7 - 9: ReAct agent loop and reasoning trace
├── part5_assistant_agent.py  # Task 10: Multi-tool assistant agent mini-project
├── task11_observations.py   # Task 11: Conceptual observations & trade-offs
├── main.py                   # Master script running all tasks sequentially
├── assignment32.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Task Details

### Part 1: Tools in AI Agents (Tasks 1 & 2)
- Answered core concepts: What tools are, why agents need them, and how agents differ from passive chatbots.
- Initialized and tested 3 tools:
  1. `calculator`: Safely evaluates math expressions (`15 * 8 + 40 -> 160`).
  2. `wikipedia_search`: Fetches factual entity summaries.
  3. `get_current_time`: Returns system date and time.

### Part 2: Custom Tools & Toolkits (Tasks 3 & 4)
- Created `@tool def company_policy_lookup(query: str)` for enterprise rules (leaves, remote work, equipment).
- Created `@tool def employee_directory_lookup(name: str)` for staff records.
- Grouped tools into `CompanyToolkit` to facilitate modular tool injection.

### Part 3: Tool Binding & Tool Calling Flow (Tasks 5 & 6)
- Bound tools to the model via `llm.bind_tools(tools)`.
- Implemented the tool calling cycle:
  `Query -> LLM Decision -> Tool Execution -> Final Synthesis`
- Verified automatic tool selection for math expressions and policy queries.

### Part 4: Creating a ReAct AI Agent (Tasks 7, 8 & 9)
- Explained ReAct: interleaving reasoning traces with environment actions to prevent hallucination.
- Implemented the ReAct execution loop:
  1. Generates `Thought:`
  2. Selects `Action:` and `Action Input:`
  3. Observes tool output `Observation:`
  4. Formulates `Final Answer:`
- Tested with factual questions, calculations, and multi-step reasoning.

### Part 5: Mini Project & Observations (Tasks 10 & 11)
- Built `build_enterprise_assistant()` integrating all custom and built-in tools.
- Recorded observations on agent benefits, infinite loop risks, chain vs. agent differences, and when to use agents over RAG.

---

## ReAct Reasoning Trace Example

```text
Question: Calculate 15 * 8
--------------------------------------------------
Thought: I need to calculate this mathematical expression.
Action: calculator
Action Input: 15 * 8
Observation: 120
Thought: I have calculated the result.
Final Answer: 15 * 8 equals 120.
```

---

## How to Run

Execute the master script to run all tasks end-to-end:
```bash
python main.py
```
