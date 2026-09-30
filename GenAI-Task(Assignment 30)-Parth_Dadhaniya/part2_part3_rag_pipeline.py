# Part 2 & 3: RAG Backend Pipeline & ChatGroq RAG Chain (Tasks 3 - 6)
# Student: Parth Dadhaniya

import os
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from config import get_chat_model

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")


# Task 3: Load documents
def load_docs():
    docs = []
    txt_path = os.path.join(DATA_DIR, "ai_handbook.txt")
    if os.path.exists(txt_path):
        docs.extend(TextLoader(txt_path, encoding="utf-8").load())

    pdf_path = os.path.join(DATA_DIR, "sample.pdf")
    if os.path.exists(pdf_path):
        try:
            docs.extend(PyPDFLoader(pdf_path).load())
        except Exception:
            pass
    return docs


# Task 3: Split documents into chunks
def split_docs(docs, chunk_size=300, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)


# Task 4: Embedding model and Chroma vector store
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def get_vectorstore():
    embeddings = get_embeddings()
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

    docs = load_docs()
    chunks = split_docs(docs)
    return Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_DIR)


# Task 5: RAG Prompt Template
def get_rag_prompt():
    system_prompt = (
        "You are a helpful assistant answering questions based on the provided documents.\n"
        "Guidelines:\n"
        "- Answer truthfully using only the context provided below.\n"
        "- If you cannot find the answer in the context, say: 'I don't know based on the provided documents.'\n"
        "- Use previous conversation turns to answer follow-up questions."
    )
    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])


# Task 6: RAG Chain
class RAGChatbot:
    def __init__(self, k=2):
        self.vectorstore = get_vectorstore()
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})
        self.llm = get_chat_model()
        self.prompt = get_rag_prompt()
        self.chain = self.prompt | self.llm
        self.history = []

    def ask(self, question):
        # Retrieve top chunks
        docs = self.retriever.invoke(question)
        context = "\n\n".join([doc.page_content.strip() for doc in docs])

        # Run chain
        response = self.chain.invoke({
            "context": context,
            "chat_history": self.history,
            "question": question
        })
        answer = response.content

        # Save conversation history
        self.history.append(HumanMessage(content=question))
        self.history.append(AIMessage(content=answer))

        return answer, docs


def run_rag_demo():
    print("--- Tasks 3-6: RAG Pipeline Demo ---")
    docs = load_docs()
    chunks = split_docs(docs)
    print(f"Loaded {len(docs)} documents and split into {len(chunks)} chunks.")

    bot = RAGChatbot(k=2)
    sample_queries = [
        "What are the advantages of Groq LPUs for LLM inference?",
        "What vector embedding model is used in this pipeline?"
    ]

    for q in sample_queries:
        print(f"\nUser: {q}")
        ans, retrieved_docs = bot.ask(q)
        print(f"Answer: {ans}")
        sources = [os.path.basename(d.metadata.get("source", "doc")) for d in retrieved_docs]
        print(f"Retrieved from: {sources}")


if __name__ == "__main__":
    run_rag_demo()
