# Assignment 35: Text-to-Math Problem Solver Agent

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering - TuteDude  

---

## Overview

In this assignment, I built a **Text-to-Math Problem Solver Agent** equipped with deterministic tool calling and multi-turn session state. Pure Large Language Models (LLMs) are probabilistic next-token predictors that struggle with reliable arithmetic, often hallucinating numbers during multi-digit multiplication, percentage calculations, or multi-step logic.

By structuring the solution as an **AI Agent**:
1. **Natural Language Understanding:** The model parses complex word problems, identifies known quantities, and extracts relationships.
2. **Deterministic Computation:** Arithmetic expressions are outsourced to a secure Python `calculator` tool, guaranteeing 100% calculation accuracy.
3. **Session State Memory:** Built a Streamlit interface using `st.session_state` that retains conversation history and previous mathematical results across multiple turns, enabling natural follow-up questions (e.g. *"Now add 15 to that result"* or *"Divide that equally among 2 people"*).

---

## File Structure

```text
GenAI-Task(Assignment 35)-Parth_Dadhaniya/
├── config.py                 # LLM configuration (ChatGroq / ChatOpenAI with student fallback)
├── part1_overview.py         # Task 1: Conceptual overview of Text-to-Math agents
├── part2_math_agent.py       # Task 2: Math agent implementation & 3 core problem tests
├── part3_session_state.py    # Task 3: Multi-turn session state simulation & context tests
├── app.py                    # Task 3: Interactive Streamlit UI with st.session_state
├── main.py                   # Master runner executing all tasks sequentially
├── assignment35.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Task Details

### Part 1: Text-to-Math Agent Overview (Task 1)
- **What is a Text-to-Math Problem?** A natural language word problem where numerical quantities, relationships, and constraints must be translated into formal mathematical operations.
- **Why Agents are Needed:** Standard LLMs lack internal ALUs and guess token sequences. An agent couples semantic reasoning with deterministic external tools.
- **Normal LLM vs Agent Reasoning:** Normal LLMs predict numbers probabilistically in one pass with high risk of compounding errors. Agents use a ReAct loop (`Thought -> Action -> Observation -> Final Answer`), verifying each intermediate step before proceeding.

### Part 2: Build Text-to-Math Agent (Task 2)
- Implemented a secure `@tool def calculator(expression: str) -> str` supporting arithmetic and percentage evaluation.
- Tested the 3 required problem categories:
  1. **Arithmetic Word Problem:**
     - *Problem:* "A store has 150 apples. If they sell 45 in the morning and 38 in the afternoon, how many apples are left?"
     - *Calculation:* `150 - 45 - 38` $\to$ **67 apples**.
  2. **Percentage Problem:**
     - *Problem:* "A laptop costs $1200. If there is a 15% discount and an 8% sales tax, what is the final price?"
     - *Calculation:* `(1200 * (1 - 0.15)) * (1 + 0.08)` $\to$ **$1,101.60**.
  3. **Simple Algebra:**
     - *Problem:* "If 3x + 15 = 45, what is the value of x?"
     - *Calculation:* `(45 - 15) / 3` $\to$ **x = 10**.

### Part 3: Session State for Application (Task 3)
- Built a Streamlit interactive application (`app.py`).
- Utilized `st.session_state.messages` to store complete conversation turns.
- Utilized `st.session_state.last_result` to preserve numerical outputs across interactions, enabling pronouns and relative terms (*"that"*, *"previous answer"*, *"more"*) to resolve accurately.

---

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Master Verification Script:**
   ```bash
   python main.py
   ```

3. **Run Individual Task Scripts:**
   ```bash
   python part1_overview.py
   python part2_math_agent.py
   python part3_session_state.py
   ```

4. **Launch Interactive Streamlit App:**
   ```bash
   streamlit run app.py
   ```

5. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook assignment35.ipynb
   ```
