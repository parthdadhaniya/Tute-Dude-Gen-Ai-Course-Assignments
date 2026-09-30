# task1_prompt_template.py
# Task 1: PromptTemplate with Dynamic Injection
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import config

print("=== Task 1: PromptTemplate ===")

# system instruction with user question placeholder
template_text = """You are an AI tutor helping students learn Generative AI.
Answer the following question clearly and concisely in 2 sentences.

Question: {question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template_text
)

llm = config.get_llm()
chain = prompt | llm | StrOutputParser()

# test with multiple inputs
questions = [
    "What is text vectorization in natural language processing?",
    "Why do LLMs sometimes hallucinate facts?",
    "How does the temperature parameter affect LLM generation?"
]

print("\nTesting PromptTemplate with dynamic inputs:\n")
for i, q in enumerate(questions, 1):
    print(f"--- Question {i} ---")
    print(f"Input: {q}")
    
    # inject input dynamically and run chain
    answer = chain.invoke({"question": q})
    print(f"Answer:\n{answer.strip()}\n")

print("Task 1 completed successfully.")
