# app.py - Streamlit UI for Text-to-Math Problem Solver with Session State (Task 3)
# Student: Parth Dadhaniya

import streamlit as st
import re
from part2_math_agent import calculator, solve_math_problem
from config import get_llm

st.set_page_config(page_title="Text-to-Math Agent", page_icon="🧮", layout="wide")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None


def solve_with_session(question: str) -> dict:
    """Processes math question using session context."""
    q_lower = question.lower()
    has_followup_word = any(
        w in q_lower for w in ["that", "previous", "now", "more", "add", "divide", "multiply", "subtract"]
    )

    if has_followup_word and st.session_state.last_result is not None:
        prev = st.session_state.last_result
        thought = f"Retrieved previous result ({prev}) from session state."
        nums = re.findall(r"\d+", question)
        expression = ""
        explanation = ""

        if "add" in q_lower or "more" in q_lower or "arrive" in q_lower:
            val = nums[0] if nums else "15"
            expression = f"{prev} + {val}"
            explanation = f"Added {val} to {prev}"
        elif "divide" in q_lower or "equally" in q_lower or "split" in q_lower:
            val = nums[0] if nums else "2"
            expression = f"{prev} / {val}"
            explanation = f"Divided {prev} by {val}"
        elif "multiply" in q_lower or "double" in q_lower or "times" in q_lower:
            val = nums[0] if nums else ("2" if "double" in q_lower else "1")
            expression = f"{prev} * {val}"
            explanation = f"Multiplied {prev} by {val}"
        elif "subtract" in q_lower or "remove" in q_lower or "less" in q_lower:
            val = nums[0] if nums else "10"
            expression = f"{prev} - {val}"
            explanation = f"Subtracted {val} from {prev}"

        if expression:
            obs = calculator.invoke(expression)
            try:
                num = float(obs)
                if num.is_integer():
                    num = int(num)
            except Exception:
                num = None
            st.session_state.last_result = num
            return {
                "question": question,
                "thought": thought,
                "action": "calculator",
                "action_input": expression,
                "observation": obs,
                "final_answer": f"{explanation}. New total is **{obs}**.",
                "numeric_result": num,
            }

    # Standard solver
    res = solve_math_problem(question)
    if res.get("numeric_result") is not None:
        st.session_state.last_result = res["numeric_result"]
    return res


# Sidebar Controls
with st.sidebar:
    st.title("🧮 Math Agent Controls")
    st.markdown("**Student:** Parth Dadhaniya")
    st.markdown("---")

    st.subheader("Current Session Context")
    if st.session_state.last_result is not None:
        st.metric(label="Last Math Result", value=st.session_state.last_result)
    else:
        st.info("No prior calculation in memory.")

    st.markdown("---")
    st.subheader("Sample Problem Quick-Picks")
    sample_1 = "A store has 150 apples. If they sell 45 in the morning and 38 in the afternoon, how many apples are left?"
    sample_2 = "A laptop costs $1200. If there is a 15% discount and an 8% sales tax, what is the final price?"
    sample_3 = "If 3x + 15 = 45, what is the value of x?"
    sample_4 = "Now add 20 to that result."

    if st.button("🍎 Arithmetic Problem"):
        st.session_state.sample_input = sample_1
    if st.button("💻 Percentage Problem"):
        st.session_state.sample_input = sample_2
    if st.button("📐 Algebra Problem"):
        st.session_state.sample_input = sample_3
    if st.button("➕ Follow-up ('add 20 to that')"):
        st.session_state.sample_input = sample_4

    if st.button("🗑️ Clear History & Memory", type="secondary"):
        st.session_state.messages = []
        st.session_state.last_result = None
        st.rerun()


# Main Chat Interface
st.title("🧮 Text-to-Math Problem Solver Agent")
st.caption("AI Agent with Step-by-Step Reasoning, Calculator Tool Calling & Streamlit Session State")

# Display conversation messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Chat Input
user_input = st.chat_input("Enter a math word problem or follow-up question...")
if "sample_input" in st.session_state and st.session_state.sample_input:
    user_input = st.session_state.sample_input
    del st.session_state.sample_input

if user_input:
    # Append and render user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process problem with session state
    result = solve_with_session(user_input)

    response_text = (
        f"**Thought:** {result['thought']}\n\n"
        f"**Action:** `{result['action']}`\n\n"
        f"**Action Input:** `{result['action_input']}`\n\n"
        f"**Observation:** `{result['observation']}`\n\n"
        f"### Final Answer\n{result['final_answer']}"
    )

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)
