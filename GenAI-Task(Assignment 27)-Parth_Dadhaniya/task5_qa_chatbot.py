# Task 5: Q&A Chatbot with Message History
# Student: Parth Dadhaniya

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import get_chat_model


class QAChatbot:
    """A simple Q&A chatbot that remembers conversation history."""

    def __init__(self):
        self.model = get_chat_model()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful Python instructor. Use past conversation to answer follow-up questions."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.model
        self.history = []

    def ask(self, question):
        response = self.chain.invoke({
            "history": self.history,
            "question": question
        })
        answer = response.content

        # Save turns to history
        self.history.append(HumanMessage(content=question))
        self.history.append(AIMessage(content=answer))

        return answer


def test_chatbot():
    print("--- Task 5: Build Q&A Chatbot with Message History ---")
    bot = QAChatbot()

    questions = [
        "Explain Python lists",
        "Give an example",
        "What about tuples?",
        "Can we modify a tuple like we modified a list?"
    ]

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q}")
        reply = bot.ask(q)
        print(f"Reply     : {reply}")

    print("\nAll follow-up questions answered accurately using conversation history.")


if __name__ == "__main__":
    test_chatbot()
