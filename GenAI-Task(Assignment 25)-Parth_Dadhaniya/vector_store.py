# vector_store.py
# Student: Parth Dadhaniya
# Course: Generative AI Engineering

import os
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, CSVLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import config

def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # load existing chroma store if already built
    if os.path.exists(config.CHROMA_DIR) and len(os.listdir(config.CHROMA_DIR)) > 0:
        return Chroma(persist_directory=config.CHROMA_DIR, embedding_function=embeddings)

    docs = []

    # load text file
    txt_file = os.path.join(config.DATA_DIR, "notes.txt")
    if os.path.exists(txt_file):
        docs.extend(TextLoader(txt_file, encoding="utf-8").load())

    # load csv file
    csv_file = os.path.join(config.DATA_DIR, "data.csv")
    if os.path.exists(csv_file):
        docs.extend(CSVLoader(csv_file, encoding="utf-8").load())

    # load pdf file
    pdf_file = os.path.join(config.DATA_DIR, "sample.pdf")
    if os.path.exists(pdf_file):
        try:
            docs.extend(PyPDFLoader(pdf_file).load())
        except:
            pass

    # split documents into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # persist into chroma
    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=config.CHROMA_DIR)
    db.persist()
    return db

def get_retriever(k=2):
    db = get_vectorstore()
    return db.as_retriever(search_kwargs={"k": k})

if __name__ == "__main__":
    retriever = get_retriever(k=2)
    sample_query = "What is machine learning?"
    results = retriever.invoke(sample_query)
    print(f"Retrieved {len(results)} chunks for query: '{sample_query}'")
    for i, doc in enumerate(results, 1):
        print(f"\nChunk {i} [Source: {doc.metadata.get('source')}]:")
        print(doc.page_content[:120] + "...")
