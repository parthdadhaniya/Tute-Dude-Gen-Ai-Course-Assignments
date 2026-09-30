# Part 1: Q&A Chatbot using OpenAI (Tasks 1, 2, 3)
# Student: Parth Dadhaniya

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import get_model, is_openai_configured, OPENAI_MODEL


def task1_setup():
    print("--- Task 1: OpenAI Setup ---")
    if is_openai_configured():
        print(f"OpenAI API Key : Configured in environment")
        print(f"Model Selected : {OPENAI_MODEL}")
    else:
        print("Notice: OPENAI_API_KEY not found in environment.")
        print(f"Using local student fallback for '{OPENAI_MODEL}' so all tests pass offline.")


def task2_basic_qa():
    print("\n--- Task 2: Basic OpenAI Q&A Chatbot (5 Questions) ---")

    # Prompt template with System and Human messages
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert AI and software engineering tutor. Answer clearly and concisely."),
        ("human", "{question}")
    ])

    model = get_model("openai")
    chain = prompt | model

    # 5 diverse technical questions
    test_questions = [
        "What is the difference between supervised and unsupervised learning?",
        "How do Python decorators work in practice?",
        "Explain the concept of overfitting and how to prevent it.",
        "What is an API and why is it used in web development?",
        "What are the primary advantages of vector databases in AI?"
    ]

    for i, q in enumerate(test_questions, start=1):
        print(f"\n[Question {i}] User: {q}")
        response = chain.invoke({"question": q})
        print(f"AI Answer: {response.content}")


def task3_multi_turn_qa():
    print("\n--- Task 3: Multi-Turn Q&A with History ---")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Python tutor. Use the chat history to understand follow-up questions."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])

    model = get_model("openai")
    chain = prompt | model

    history = []
    dialogue = [
        "How do Python decorators work in practice?",
        "Can you explain more with a simple example?"
    ]

    for turn, q in enumerate(dialogue, start=1):
        print(f"\nTurn {turn} -> User: {q}")
        response = chain.invoke({"history": history, "question": q})
        answer = response.content
        print(f"Assistant: {answer}")

        # Update history
        history.append(HumanMessage(content=q))
        history.append(AIMessage(content=answer))

    print(f"\nTotal conversation messages stored: {len(history)}")


if __name__ == "__main__":
    task1_setup()
    task2_basic_qa()
    task3_multi_turn_qa()
