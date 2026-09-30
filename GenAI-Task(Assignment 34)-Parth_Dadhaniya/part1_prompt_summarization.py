# Part 1: Basic Text Summarization using PromptTemplate (Tasks 1, 2 & 3)
# Student: Parth Dadhaniya

import os
from langchain_core.prompts import PromptTemplate
from config import get_llm

doc_path = os.path.join(os.path.dirname(__file__), "data", "enterprise_ai_overview.txt")


def load_document():
    """Task 1: Load text document and display statistics."""
    with open(doc_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("--- Task 1: Load and Prepare Document ---")
    print(f"Document File   : enterprise_ai_overview.txt")
    print(f"Total Characters: {len(text):,}")
    print(f"Total Words     : {len(text.split()):,}")
    print("\nSample Preview (First 250 characters):")
    print("-" * 50)
    print(text[:250] + "...")
    print("-" * 50)
    return text


def basic_summarization(text, llm):
    """Task 2: Prompt-based summarization using LangChain PromptTemplate."""
    print("\n--- Task 2: Prompt-Based Summarization ---")

    template = """You are a helpful AI assistant specialized in text summarization.
Summarize the following text clearly and concisely, preserving the main points:

Text:
{document_text}

Summary:"""

    prompt = PromptTemplate(template=template, input_variables=["document_text"])
    chain = prompt | llm

    response = chain.invoke({"document_text": text})
    summary = response.content if hasattr(response, "content") else str(response)

    print("Generated Summary:")
    print(summary)
    return summary


def prompt_variations(text, llm):
    """Task 3: Testing prompt variations (short summary vs bullet-point summary)."""
    print("\n--- Task 3: Prompt Variations ---")

    # Variation 1: Short paragraph summary (5-6 lines)
    short_template = """You are an executive assistant.
Summarize the following document in a short paragraph of 5 to 6 lines:

Document:
{document_text}

Short Summary:"""
    short_prompt = PromptTemplate(template=short_template, input_variables=["document_text"])
    short_chain = short_prompt | llm
    short_res = short_chain.invoke({"document_text": text})
    short_summary = short_res.content if hasattr(short_res, "content") else str(short_res)

    print("\n[Variation A: Short Paragraph Summary (5-6 lines)]")
    print(short_summary)

    # Variation 2: Bullet-point summary
    bullet_template = """You are a research analyst.
Extract the key takeaways from the following document as concise bullet points:

Document:
{document_text}

Key Bullet Points:"""
    bullet_prompt = PromptTemplate(template=bullet_template, input_variables=["document_text"])
    bullet_chain = bullet_prompt | llm
    bullet_res = bullet_chain.invoke({"document_text": text})
    bullet_summary = bullet_res.content if hasattr(bullet_res, "content") else str(bullet_res)

    print("\n[Variation B: Bullet-Point Summary]")
    print(bullet_summary)


def main():
    llm = get_llm()
    text = load_document()
    basic_summarization(text, llm)
    prompt_variations(text, llm)


if __name__ == "__main__":
    main()
