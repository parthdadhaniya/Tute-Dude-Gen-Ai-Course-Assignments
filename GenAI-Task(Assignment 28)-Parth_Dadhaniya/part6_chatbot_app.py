# Part 6: Mini Project - Conversational RAG Assistant (Task 10)
# Student: Parth Dadhaniya

import sys
from langchain_core.messages import HumanMessage, AIMessage
from part3_part4_rag_chain import create_rag_prompt, format_docs, trim_history
from part2_vector_store import get_retriever
from config import get_chat_model


class DocumentRAGChatbot:
    """A production-ready conversational RAG assistant supporting sessions and trimming."""

    def __init__(self, max_turns=3, k_retrieval=2):
        self.retriever = get_retriever(k=k_retrieval)
        self.model = get_chat_model()
        self.prompt = create_rag_prompt()
        self.chain = self.prompt | self.model
        self.max_turns = max_turns
        self.sessions = {}

    def get_history(self, session_id="default"):
        """Get history for a session."""
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        return self.sessions[session_id]

    def chat(self, question, session_id="default"):
        """Retrieve relevant context, trim history, and generate answer."""
        history = self.get_history(session_id)

        # 1. Retrieve document chunks
        docs = self.retriever.invoke(question)
        context = format_docs(docs)

        # 2. Trim history using sliding window
        active_history = trim_history(history, max_turns=self.max_turns)

        # 3. Generate grounded answer
        response = self.chain.invoke({
            "context": context,
            "chat_history": active_history,
            "question": question
        })
        answer = response.content

        # 4. Save to session history
        history.append(HumanMessage(content=question))
        history.append(AIMessage(content=answer))

        return answer, docs

    def clear(self, session_id="default"):
        """Reset conversation memory for a session."""
        self.sessions[session_id] = []


def run_mini_project_demo():
    print("--- Task 10: Conversational RAG Assistant Mini Project ---")
    bot = DocumentRAGChatbot(max_turns=3)

    print("\n[Session 1: Employee Handbook Q&A]")
    dialogue = [
        "What is the annual leave policy?",
        "Explain more about how it is carried forward.",
        "What about sick leave compared to that?"
    ]

    for q in dialogue:
        print(f"\nUser: {q}")
        reply, docs = bot.chat(q, session_id="session_1")
        print(f"Bot : {reply}")

    print(f"\nSession 1 Total History: {len(bot.get_history('session_1'))} messages")

    # Independent Session 2
    print("\n[Session 2: Independent Session Isolation]")
    q2 = "What is the annual learning allowance?"
    print(f"User: {q2}")
    reply2, _ = bot.chat(q2, session_id="session_2")
    print(f"Bot : {reply2}")
    print(f"Session 2 Total History: {len(bot.get_history('session_2'))} messages")


def run_interactive():
    """Terminal chat mode for user interaction."""
    bot = DocumentRAGChatbot(max_turns=3)
    print("Document RAG Assistant CLI (type 'exit' to quit, 'clear' to reset)")
    while True:
        try:
            msg = input("\nYou: ").strip()
            if not msg:
                continue
            if msg.lower() in ["exit", "quit", "q"]:
                break
            if msg.lower() == "clear":
                bot.clear()
                print("Chat history cleared!")
                continue
            answer, _ = bot.chat(msg)
            print(f"Bot: {answer}")
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["--interactive", "-i"]:
        run_interactive()
    else:
        run_mini_project_demo()
