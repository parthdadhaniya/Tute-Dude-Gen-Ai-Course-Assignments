# Task 6: Stateful Chatbot Application (Mini Project)
# Student: Parth Dadhaniya

import sys
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import get_chat_model


class StatefulChatbot:
    """A stateful chatbot that manages multiple sessions and trims old messages."""

    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.model = get_chat_model()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a friendly customer support chatbot. Use past conversation to answer questions."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.model
        # Dictionary to store history per session: {session_id: [messages]}
        self.sessions = {}

    def get_history(self, session_id="default"):
        """Get history for a specific session."""
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        return self.sessions[session_id]

    def chat(self, question, session_id="default"):
        """Send question, trim history for LLM, and update session history."""
        history = self.get_history(session_id)

        # Trimming: keep only the last max_turns * 2 messages (user + AI pairs)
        window_size = self.max_turns * 2
        trimmed_history = history[-window_size:] if len(history) > window_size else history

        response = self.chain.invoke({
            "history": trimmed_history,
            "question": question
        })
        reply = response.content

        # Save to full session history
        history.append(HumanMessage(content=question))
        history.append(AIMessage(content=reply))

        return reply

    def clear(self, session_id="default"):
        """Reset history for a session."""
        self.sessions[session_id] = []


def run_demo():
    print("--- Task 6: Stateful Chatbot Mini Project ---")
    bot = StatefulChatbot(max_turns=2)

    # 1. Multi-turn chat in user session 1
    print("\n[Session 1 - Technical Q&A]")
    dialogue = [
        "Explain Python lists",
        "Give an example",
        "What about tuples?"
    ]

    for q in dialogue:
        print(f"User : {q}")
        reply = bot.chat(q, session_id="user_1")
        print(f"Bot  : {reply}")

    print(f"\nSession 1 saved message count: {len(bot.get_history('user_1'))}")

    # 2. Independent Session 2
    print("\n[Session 2 - Independent User]")
    print("User : Hi, my name is Parth.")
    r1 = bot.chat("Hi, my name is Parth.", session_id="user_2")
    print(f"Bot  : {r1}")

    print("User : What is my name?")
    r2 = bot.chat("What is my name?", session_id="user_2")
    print(f"Bot  : {r2}")

    print(f"\nSession 2 saved message count: {len(bot.get_history('user_2'))}")

    # 3. Clear session 2
    bot.clear("user_2")
    print(f"Cleared Session 2. Messages remaining: {len(bot.get_history('user_2'))}")
    print(f"Session 1 messages still intact: {len(bot.get_history('user_1'))}")


def run_interactive():
    """Terminal chat loop for testing."""
    bot = StatefulChatbot(max_turns=3)
    print("Stateful Chatbot CLI (type 'exit' to quit, 'clear' to reset)")
    while True:
        try:
            msg = input("\nYou: ").strip()
            if not msg:
                continue
            if msg.lower() in ["exit", "quit", "q"]:
                break
            if msg.lower() == "clear":
                bot.clear()
                print("History cleared!")
                continue
            print(f"Bot: {bot.chat(msg)}")
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["--interactive", "-i"]:
        run_interactive()
    else:
        run_demo()
