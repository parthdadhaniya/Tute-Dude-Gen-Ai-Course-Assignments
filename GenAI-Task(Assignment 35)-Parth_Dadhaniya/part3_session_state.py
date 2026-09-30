# Part 3: Session State Logic & Context Preservation (Task 3)
# Student: Parth Dadhaniya

import re
from part2_math_agent import calculator, solve_math_problem


class MathSessionManager:
    """
    Manages session state: stores conversation history and retains previous math context
    across multiple interaction turns.
    """

    def __init__(self):
        self.history = []  # List of tuples: (question, result_dict)
        self.last_result = None

    def solve_with_context(self, question: str) -> dict:
        q_lower = question.lower()

        # Detect follow-up referring to previous result
        has_followup_word = any(
            w in q_lower for w in ["that", "previous", "now", "more", "add", "divide", "multiply", "subtract"]
        )

        if has_followup_word and self.last_result is not None:
            prev = self.last_result
            thought = f"Math context preserved from session state: previous result is {prev}."
            expression = ""
            explanation = ""

            nums = re.findall(r"\d+", question)

            if "add" in q_lower or "arrive" in q_lower or "more" in q_lower:
                val = nums[0] if nums else "15"
                expression = f"{prev} + {val}"
                explanation = f"Added {val} to the previous result ({prev})"
            elif "divide" in q_lower or "equally" in q_lower or "split" in q_lower:
                val = nums[0] if nums else "2"
                expression = f"{prev} / {val}"
                explanation = f"Divided the previous result ({prev}) by {val}"
            elif "multiply" in q_lower or "double" in q_lower or "times" in q_lower:
                val = nums[0] if nums else ("2" if "double" in q_lower else "1")
                expression = f"{prev} * {val}"
                explanation = f"Multiplied the previous result ({prev}) by {val}"
            elif "subtract" in q_lower or "remove" in q_lower or "less" in q_lower:
                val = nums[0] if nums else "10"
                expression = f"{prev} - {val}"
                explanation = f"Subtracted {val} from the previous result ({prev})"

            if expression:
                observation = calculator.invoke(expression)
                try:
                    num_val = float(observation)
                    if num_val.is_integer():
                        num_val = int(num_val)
                except Exception:
                    num_val = None

                self.last_result = num_val
                res = {
                    "question": question,
                    "thought": thought,
                    "action": "calculator",
                    "action_input": expression,
                    "observation": observation,
                    "final_answer": f"{explanation}. New total is {observation}.",
                    "numeric_result": num_val,
                }
                self.history.append((question, res))
                return res

        # Standard initial question
        res = solve_math_problem(question)
        if res.get("numeric_result") is not None:
            self.last_result = res["numeric_result"]
        self.history.append((question, res))
        return res


def main():
    print("--- Task 3: Simulating Session State Across Multi-Turn Interactions ---")
    session = MathSessionManager()

    # Turn 1: Initial problem
    t1 = "A store has 150 apples. If they sell 45 in the morning and 38 in the afternoon, how many apples are left?"
    print(f"\n[Turn 1 User] : {t1}")
    r1 = session.solve_with_context(t1)
    print(f"[Turn 1 Agent]: {r1['final_answer']} (Stored session result = {session.last_result})")

    # Turn 2: Follow-up question (adds 15)
    t2 = "If 15 more apples arrive tomorrow, how many apples will there be in total?"
    print(f"\n[Turn 2 User] : {t2}")
    r2 = session.solve_with_context(t2)
    print(f"[Turn 2 Agent]: {r2['final_answer']} (Stored session result = {session.last_result})")

    # Turn 3: Follow-up question (divide by 2)
    t3 = "Now divide that result equally among 2 storage crates."
    print(f"\n[Turn 3 User] : {t3}")
    r3 = session.solve_with_context(t3)
    print(f"[Turn 3 Agent]: {r3['final_answer']} (Stored session result = {session.last_result})")

    print(f"\nSession History Verified: Total turns preserved = {len(session.history)}")


if __name__ == "__main__":
    main()
