# Part 3 & Part 4: RAG Prompt, Chain, Message History & Trimming (Tasks 5, 6, 7, 8)
# Student: Parth Dadhaniya

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from part2_vector_store import get_retriever
from config import get_chat_model


def create_rag_prompt():
    """Task 5: Create ChatPromptTemplate with strict grounding and MessagesPlaceholder."""
    system_instructions = (
        "You are a helpful document assistant. Answer the user's question based strictly on the provided context.\n"
        "Rules:\n"
        "- Only use facts from the context.\n"
        "- If the answer cannot be found in the context, say: 'I don't know based on the provided documents.'\n"
        "- Use conversation history to understand follow-up questions."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_instructions),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])
    return prompt


def format_docs(docs):
    """Combine retrieved document chunks into a single readable context string."""
    return "\n\n".join([d.page_content.strip() for d in docs])


def trim_history(messages, max_turns=3):
    """Task 8: Keep only the most recent N turns to prevent token overflow."""
    max_messages = max_turns * 2
    if len(messages) <= max_messages:
        return messages
    return messages[-max_messages:]


class ConversationalRAGChain:
    """Tasks 6 & 7: Manages document retrieval, context injection, prompt, and message history."""

    def __init__(self, max_turns=3):
        self.retriever = get_retriever(k=2)
        self.model = get_chat_model()
        self.prompt = create_rag_prompt()
        self.chain = self.prompt | self.model
        self.max_turns = max_turns
        self.history = []

    def query(self, user_question):
        # 1. Retrieve relevant document chunks
        docs = self.retriever.invoke(user_question)
        context = format_docs(docs)

        # 2. Trim history
        active_history = trim_history(self.history, max_turns=self.max_turns)

        # 3. Call RAG chain
        response = self.chain.invoke({
            "context": context,
            "chat_history": active_history,
            "question": user_question
        })
        answer = response.content

        # 4. Save to message history
        self.history.append(HumanMessage(content=user_question))
        self.history.append(AIMessage(content=answer))

        return answer, docs


def test_chain_demo():
    print("--- Tasks 5 to 8: RAG Chain with Message History Demo ---")
    bot = ConversationalRAGChain(max_turns=2)

    q1 = "What is the annual leave policy?"
    print(f"\nUser: {q1}")
    ans1, docs1 = bot.query(q1)
    print(f"Bot : {ans1}")
    print(f"Sources: {[d.metadata.get('source', '') for d in docs1]}")
    print(f"History messages: {len(bot.history)}")


if __name__ == "__main__":
    test_chain_demo()
