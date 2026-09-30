# Part 2: Build Text-to-Math Agent (Task 2)
# Student: Parth Dadhaniya

import re
from langchain_core.tools import tool
from config import get_llm


@tool
def calculator(expression: str) -> str:
    """Evaluates a mathematical expression safely using Python's eval."""
    try:
        allowed = set("0123456789+-*/(). %")
        cleaned = expression.strip().replace("x", "*")
        if not all(c in allowed for c in cleaned):
            return "Error: Invalid mathematical characters."
        result = eval(cleaned, {"__builtins__": None}, {})
        return str(round(result, 2))
    except Exception as e:
        return f"Error: {e}"


def parse_math_expression(question: str):
    """
    Parses natural language math word problems into mathematical expressions.
    Works generically across arithmetic, percentages, and simple algebra.
    """
    text = question.strip()
    text_lower = text.lower()

    # 1. Simple Linear Algebra: e.g. 3x + 15 = 45 or 4y - 20 = 60
    alg_match = re.search(r"(\d+)\s*([a-zA-Z])\s*([\+\-])\s*(\d+)\s*=\s*(\d+)", text)
    if alg_match:
        coeff, var, sign, const, target = alg_match.groups()
        opp_sign = "-" if sign == "+" else "+"
        expr = f"({target} {opp_sign} {const}) / {coeff}"
        thought = f"To solve for {var}: isolate the variable by moving {const} ({opp_sign}), then dividing by {coeff}."
        return thought, expr, f"The value of {var} is"

    # 2. Percentage Word Problems (e.g. price with discount and sales tax)
    pct_matches = re.findall(r"(\d+(?:\.\d+)?)\s*%", text)
    if pct_matches:
        all_numbers = re.findall(r"\b\d+(?:\.\d+)?\b", text)
        base_candidates = [float(n) for n in all_numbers if n not in pct_matches]
        if base_candidates:
            base = base_candidates[0]
            expr = f"{base}"
            thought_parts = [f"Base price: ${base}"]

            # Apply discount and tax rates based on words following the percentage
            for p in pct_matches:
                rate = float(p) / 100.0
                pos = text_lower.find(p + "%")
                after = text_lower[pos : pos + 18]
                if "discount" in after or "off" in after or "coupon" in after:
                    expr = f"({expr} * (1 - {rate}))"
                    thought_parts.append(f"apply {p}% discount")
                elif "tax" in after or "tip" in after or "markup" in after:
                    expr = f"({expr} * (1 + {rate}))"
                    thought_parts.append(f"add {p}% tax")
                else:
                    expr = f"({expr} * {rate})"
                    thought_parts.append(f"multiply by {p}%")

            thought = " -> ".join(thought_parts)
            return thought, expr, "The final calculated price is $"

    # 3. Arithmetic Word Problems (additions, deductions, remaining amounts)
    nums = [int(n) for n in re.findall(r"\b\d+\b", text)]
    if len(nums) >= 2:
        base = nums[0]
        deductions = nums[1:]
        sub_keywords = ["sell", "sold", "left", "spend", "spent", "give", "lost", "remove", "subtract"]

        if any(w in text_lower for w in sub_keywords):
            expr = f"{base} - " + " - ".join(str(n) for n in deductions)
            thought = f"Initial count of {base}, subtracting deductions: {deductions}."
            return thought, expr, "The remaining count is"
        else:
            expr = " + ".join(str(n) for n in nums)
            thought = f"Adding all quantities together: {nums}."
            return thought, expr, "The total sum is"

    # 4. Direct arithmetic expression fallback
    cleaned_expr = re.sub(r"[^0-9\+\-\*\/\(\)\. ]", "", text).strip()
    if cleaned_expr:
        return f"Computing direct arithmetic: {cleaned_expr}", cleaned_expr, "Result:"

    return "No clear mathematical expression found.", "0", "Result:"


def solve_math_problem(question: str, llm=None) -> dict:
    """
    Task 2: Text-to-Math Problem Solver Agent.
    Combines reasoning with the calculator tool to return step-by-step solutions.
    """
    if llm is None:
        llm = get_llm()

    thought = ""
    expression = ""
    label = ""

    # If live LLM is provided (e.g. ChatGroq / ChatOpenAI)
    if llm is not None:
        prompt = (
            f"You are a math tutor. Solve this problem step by step.\n"
            f"Write the mathematical expression to compute in the format:\n"
            f"EXPRESSION: <expression>\n\nProblem: {question}"
        )
        res = llm.invoke(prompt)
        text = res.content if hasattr(res, "content") else str(res)
        match = re.search(r"EXPRESSION:\s*(.+)", text)
        if match:
            expression = match.group(1).strip()
            thought = text.split("EXPRESSION:")[0].strip()
            label = "The answer is"

    # Otherwise use dynamic problem parser
    if not expression:
        thought, expression, label = parse_math_expression(question)

    # Action: Execute the calculator tool
    observation = calculator.invoke(expression)

    # Parse numeric result
    try:
        num_val = float(observation)
        if num_val.is_integer():
            num_val = int(num_val)
    except Exception:
        num_val = None

    return {
        "question": question,
        "thought": thought,
        "action": "calculator",
        "action_input": expression,
        "observation": observation,
        "final_answer": f"{label} {observation}.",
        "numeric_result": num_val,
    }


def print_agent_trace(result: dict):
    print("\n" + "-" * 55)
    print(f"Question     : {result['question']}")
    print(f"Thought      : {result['thought']}")
    print(f"Action       : {result['action']}")
    print(f"Action Input : {result['action_input']}")
    print(f"Observation  : {result['observation']}")
    print(f"Final Answer : {result['final_answer']}")
    print("-" * 55)


def main():
    print("--- Task 2: Testing Text-to-Math Agent ---")

    # Test 1: Arithmetic word problem
    p1 = "A store has 150 apples. If they sell 45 in the morning and 38 in the afternoon, how many apples are left?"
    r1 = solve_math_problem(p1)
    print_agent_trace(r1)

    # Test 2: Percentage problem
    p2 = "A laptop costs $1200. If there is a 15% discount and an 8% sales tax, what is the final price?"
    r2 = solve_math_problem(p2)
    print_agent_trace(r2)

    # Test 3: Simple algebra
    p3 = "If 3x + 15 = 45, what is the value of x?"
    r3 = solve_math_problem(p3)
    print_agent_trace(r3)


if __name__ == "__main__":
    main()
