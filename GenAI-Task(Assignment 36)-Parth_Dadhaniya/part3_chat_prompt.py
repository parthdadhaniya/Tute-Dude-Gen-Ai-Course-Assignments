# part3_chat_prompt.py - ChatPromptTemplate vs Normal Prompt with Hugging Face
# Student: Parth Dadhaniya

import time
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import get_hf_llm, DEFAULT_MODEL


def run_chat_prompt_pipeline(question: str):
    """Generates response using ChatPromptTemplate (system + human messages)."""
    hf_llm = get_hf_llm(model_id=DEFAULT_MODEL, temperature=0.7, max_new_tokens=300)

    chat_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an experienced AI educator. Explain concepts clearly using an everyday analogy, "
            "and keep an encouraging, friendly tone."
        ),
        (
            "human",
            "{question}"
        )
    ])

    chain = chat_prompt | hf_llm | StrOutputParser()

    start_time = time.time()
    response = chain.invoke({"question": question})
    elapsed = round(time.time() - start_time, 3)

    return {
        "type": "ChatPromptTemplate (System + Human)",
        "prompt_structure": chat_prompt.format(question=question),
        "response": response.strip(),
        "time_sec": elapsed
    }


def run_normal_prompt_pipeline(question: str):
    """Generates response using a standard single-string PromptTemplate."""
    hf_llm = get_hf_llm(model_id=DEFAULT_MODEL, temperature=0.7, max_new_tokens=300)

    normal_prompt = PromptTemplate.from_template(
        "Question: {question}\nAnswer:"
    )

    chain = normal_prompt | hf_llm | StrOutputParser()

    start_time = time.time()
    response = chain.invoke({"question": question})
    elapsed = round(time.time() - start_time, 3)

    return {
        "type": "Normal PromptTemplate (Single String)",
        "prompt_structure": normal_prompt.format(question=question),
        "response": response.strip(),
        "time_sec": elapsed
    }


def run_task3():
    """Executes Task 3: ChatPromptTemplate vs Normal Prompt comparison."""
    print("============================================================")
    print("Task 3: Chat Prompt Template with Hugging Face")
    print("Student: Parth Dadhaniya")
    print("============================================================")

    test_question = "What is temperature in Large Language Models?"
    print(f"Target Question: '{test_question}'\n")

    # 1. Chat Prompt Template
    print(">>> 1. Executing ChatPromptTemplate Pipeline <<<")
    chat_result = run_chat_prompt_pipeline(test_question)
    print("Formulated Prompt Representation:")
    print(chat_result["prompt_structure"])
    print("-" * 60)
    print("Hugging Face LLM Response:")
    print(chat_result["response"])
    print("-" * 60)
    print(f"Latency: {chat_result['time_sec']}s\n")

    # 2. Normal Prompt Template
    print(">>> 2. Executing Normal PromptTemplate Pipeline <<<")
    normal_result = run_normal_prompt_pipeline(test_question)
    print("Formulated Prompt Representation:")
    print(normal_result["prompt_structure"])
    print("-" * 60)
    print("Hugging Face LLM Response:")
    print(normal_result["response"])
    print("-" * 60)
    print(f"Latency: {normal_result['time_sec']}s\n")

    # 3. Direct Side-by-Side Comparison
    print("=" * 65)
    print(">>> PART 3 COMPARISON: ChatPromptTemplate vs Normal Prompt <<<")
    print("=" * 65)
    print(f"{'Feature':<25} | {'Normal PromptTemplate':<25} | {'ChatPromptTemplate':<25}")
    print("-" * 79)
    print(f"{'Message Structure':<25} | {'Single unstructured text':<25} | {'System + Human messages':<25}")
    print(f"{'Persona Enforcement':<25} | {'Weak / Unspecified':<25} | {'Strict (Educator + Analogy)':<25}")
    print(f"{'Tone & Style':<25} | {'Direct & Academic':<25} | {'Encouraging & Metaphorical':<25}")
    print(f"{'Prompt Injection Safety':<25} | {'Lower (concatenated text)':<25} | {'Higher (token delimiter tags)':<25}")
    print(f"{'HF Chat Model Support':<25} | {'Raw completion format':<25} | {'Maps to model chat template':<25}")
    print("=" * 65)


if __name__ == "__main__":
    run_task3()
