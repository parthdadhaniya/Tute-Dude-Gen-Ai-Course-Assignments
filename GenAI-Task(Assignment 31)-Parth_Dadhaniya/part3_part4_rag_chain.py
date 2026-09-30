# Part 3 & 4: Conversational Prompt, RAG Chain & History Trimming (Tasks 5 - 8)
# Student: Parth Dadhaniya

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from config import get_llm
from part2_vector_store import get_retriever


# Task 5: RAG prompt template with message history
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the question based only on the following PDF context:\n\n{context}\n\nIf the answer is not in the context, say 'I don't know based on the provided documents.'"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])


# Task 8: Trimming history using sliding window
def trim_history(history, max_messages=6):
    if len(history) > max_messages:
        return history[-max_messages:]
    return history


# Tasks 6 & 7: Conversational RAG pipeline
def ask_question(question, history, retriever=None, llm=None):
    if retriever is None:
        retriever = get_retriever(k=2)
    if llm is None:
        llm = get_llm()

    # 1. trim history to prevent overflow
    trimmed = trim_history(history, max_messages=4)

    # 2. retrieve relevant chunks
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content.strip() for d in docs])

    # 3. generate answer
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "chat_history": trimmed,
        "question": question
    })
    answer = response.content

    # 4. update history
    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=answer))

    return answer, docs


def main():
    print("--- Tasks 5 - 8: Conversational RAG Chain ---")
    retriever = get_retriever(k=2)
    llm = get_llm()
    history = []

    questions = [
        "What encryption standards are required for vector databases?",
        "What is the retention policy for conversation logs?",
        "Explain that in more detail."
    ]

    for q in questions:
        print(f"\nUser: {q}")
        ans, docs = ask_question(q, history, retriever, llm)
        print(f"Assistant: {ans}")
        print(f"History count: {len(history)} messages")


if __name__ == "__main__":
    main()
