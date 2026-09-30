# Part 3: Unified Q&A Chatbot App (Tasks 7 & 8)
# Student: Parth Dadhaniya

import sys
from langchain_core.prompts import ChatPromptTemplate
from config import get_model, is_openai_configured, is_ollama_running


# Prompt template shared across all models
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and knowledgeable software engineering assistant. Answer questions clearly."),
    ("human", "{question}")
])


def get_answer(question, model_type="openai"):
    """
    Task 7: Returns answer from selected model ('openai' or 'ollama').
    Uses LangChain LCEL chain to generate structured conversational response.
    """
    selected_model = get_model(model_type)
    chain = qa_prompt | selected_model
    response = chain.invoke({"question": question})
    return response.content


def task7_switch_demo():
    print("--- Task 7: Model Switch Logic Demo ---")

    sample_questions = [
        "What is the difference between supervised and unsupervised learning?",
        "What are the primary advantages of vector databases in AI?"
    ]

    for q in sample_questions:
        print(f"\nQuestion: {q}")
        ans_openai = get_answer(q, model_type="openai")
        ans_ollama = get_answer(q, model_type="ollama")

        print(f"[OpenAI Response]:\n{ans_openai}")
        print(f"[Ollama Response]:\n{ans_ollama}")
        print("-" * 50)


def run_cli_chatbot():
    """Task 8: Simple interactive CLI chatbot allowing model switching."""
    print("=" * 60)
    print("Unified Q&A Chatbot (CLI)")
    print("Commands:")
    print("  /switch  - Toggle between OpenAI and Ollama")
    print("  /status  - Check API and local server status")
    print("  exit     - Quit the chatbot")
    print("=" * 60)

    current_model = "openai"
    print(f"Current Model: {current_model.upper()}\n")

    while True:
        try:
            user_input = input(f"[{current_model.upper()}] Ask a question: ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                print("Exiting chatbot. Goodbye!")
                break

            if user_input.lower() == "/switch":
                current_model = "ollama" if current_model == "openai" else "openai"
                print(f"Switched model to: {current_model.upper()}")
                continue

            if user_input.lower() == "/status":
                print(f"OpenAI Configured: {is_openai_configured()}")
                print(f"Ollama Online    : {is_ollama_running()}")
                continue

            # Get answer from currently active model
            answer = get_answer(user_input, model_type=current_model)
            print(f"\nAnswer:\n{answer}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["--interactive", "-i", "--cli"]:
        run_cli_chatbot()
    else:
        task7_switch_demo()
