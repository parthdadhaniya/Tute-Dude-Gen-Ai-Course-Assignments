# part2_hf_langchain.py - HuggingFace Integration with LangChain
# Student: Parth Dadhaniya

import time
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import get_hf_llm, DEFAULT_MODEL


def build_huggingface_chain(model_id: str = DEFAULT_MODEL):
    """
    Builds a LangChain LCEL chain powered by Hugging Face instead of OpenAI.
    Pipeline: PromptTemplate -> HuggingFace LLM -> StrOutputParser
    """
    # Initialize Hugging Face LLM wrapper
    hf_llm = get_hf_llm(model_id=model_id, temperature=0.3, max_new_tokens=256)

    # Prompt Template
    prompt_template = PromptTemplate.from_template(
        "You are a helpful GenAI assistant. Answer the following request clearly and concisely:\n\n"
        "Request: {user_input}\n\n"
        "Answer:"
    )

    # LCEL Chain (replacing OpenAI in the pipeline)
    chain = prompt_template | hf_llm | StrOutputParser()
    return chain, hf_llm


def run_task2():
    """Executes Task 2: LangChain Wrapper integration and multiple prompt testing."""
    print("============================================================")
    print("Task 2: HuggingFace with LangChain (Replacing OpenAI)")
    print("Student: Parth Dadhaniya")
    print("============================================================")
    print("\n[Architecture Note]")
    print("In LangChain, switching from OpenAI to Hugging Face is straightforward:")
    print("  Previous (OpenAI):")
    print("    from langchain_openai import ChatOpenAI")
    print("    llm = ChatOpenAI(model='gpt-3.5-turbo')")
    print("  New (Hugging Face Open-Source):")
    print("    from langchain_huggingface import HuggingFaceEndpoint")
    print("    llm = HuggingFaceEndpoint(repo_id='google/flan-t5-base', max_new_tokens=256)")
    print("  Unified Pipeline: chain = prompt | llm | StrOutputParser()")

    # Build chain
    chain, hf_llm = build_huggingface_chain()
    print(f"\nActive Hugging Face LLM Wrapper: {type(hf_llm).__name__} (Model: {DEFAULT_MODEL})\n")

    # Diverse Test Prompts
    test_prompts = [
        {
            "category": "Factual / Technical Q&A",
            "prompt": "Explain the difference between supervised and unsupervised learning in 3 bullet points."
        },
        {
            "category": "Code Generation & Explanation",
            "prompt": "Write a short Python function to reverse a string and explain how it works."
        },
        {
            "category": "Enterprise GenAI Strategy",
            "prompt": "List 3 major benefits of using open-source AI models compared to closed APIs for an enterprise."
        }
    ]

    for idx, item in enumerate(test_prompts, 1):
        print(f"--- Prompt {idx}: {item['category']} ---")
        print(f"Input : {item['prompt']}")

        start_time = time.time()
        output = chain.invoke({"user_input": item["prompt"]})
        elapsed = round(time.time() - start_time, 3)

        print("-" * 60)
        print("LangChain Chain Output:")
        print(output.strip())
        print("-" * 60)
        print(f"Stats : {len(output.split())} words | Latency: {elapsed}s\n")

    print(">>> Summary for Task 2 <<<")
    print("- Seamless integration: Hugging Face endpoints plug directly into LangChain pipelines.")
    print("- Zero vendor lock-in: Swapped OpenAI dependency with open-source Hugging Face models.")
    print("- Consistent LCEL syntax: `prompt | llm | parser` behaves identically across model providers.")


if __name__ == "__main__":
    run_task2()
