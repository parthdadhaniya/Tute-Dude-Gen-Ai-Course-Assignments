# Task 3 & Task 4: Message History & History Trimming
# Student: Parth Dadhaniya

from langchain_core.messages import HumanMessage, AIMessage, trim_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import get_chat_model


def trim_history(messages, max_messages=4):
    """Keep only the most recent N messages to avoid token limit overflow."""
    if len(messages) <= max_messages:
        return messages
    return messages[-max_messages:]


def task3_basic_history():
    print("--- Task 3: Basic Message History ---")
    model = get_chat_model()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Python tutor."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])
    chain = prompt | model

    # In-memory list to store all past messages
    history = []

    questions = [
        "Explain Python lists",
        "Give an example",
        "What about tuples?",
        "Can we modify a tuple like we modified a list?"
    ]

    for turn, q in enumerate(questions, start=1):
        print(f"\n[Turn {turn}] Question: {q}")
        response = chain.invoke({"history": history, "question": q})
        answer = response.content

        # Append messages after each interaction
        history.append(HumanMessage(content=q))
        history.append(AIMessage(content=answer))

        print(f"Answer: {answer}")
        print(f"Current history length: {len(history)} messages")


def task4_trimming_demo():
    print("\n--- Task 4: Trimming Chat History ---")
    model = get_chat_model()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Python tutor."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])
    chain = prompt | model

    # Limit to last 4 messages (last 2 full turns)
    MAX_MESSAGES = 4
    full_history = []

    dialogue = [
        "Hi, my name is Parth.",
        "What is my name?",
        "Explain Python lists",
        "Give an example",
        "What about tuples?"
    ]

    for turn, q in enumerate(dialogue, start=1):
        print(f"\nTurn {turn}: User -> {q}")

        # Trim history before passing to LLM
        trimmed = trim_history(full_history, max_messages=MAX_MESSAGES)
        print(f"  [Total saved: {len(full_history)} | Sent to LLM: {len(trimmed)}]")

        response = chain.invoke({"history": trimmed, "question": q})
        answer = response.content
        print(f"AI: {answer}")

        # Always save full interaction to our main history log
        full_history.append(HumanMessage(content=q))
        full_history.append(AIMessage(content=answer))

    print(f"\nFinished dialogue.")
    print(f"Total conversation turns saved: {len(full_history)} messages.")
    print(f"Max sent to LLM at once: {MAX_MESSAGES} messages.")
    print("Trimming successfully prevented context overflow while keeping recent context!")


if __name__ == "__main__":
    task3_basic_history()
    task4_trimming_demo()
