# app.py - FastAPI Application Serving Groq Chatbot & RAG
# Student: Parth Dadhaniya
# Course: Generative AI Engineering

import time
import logging
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import config
from task2_groq_chatbot import groq_chat
from task3_task4_groq_rag import groq_rag_pipeline

# logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger("groq_api")

app = FastAPI(
    title="Groq AI Chatbot & RAG API",
    description="Low-latency AI backend powered by Groq and FastAPI",
    version="1.0.0"
)

# request & response models
class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User question or prompt")
    use_rag: bool = Field(default=True, description="Enable RAG retrieval")

class ChatResponse(BaseModel):
    query: str
    answer: str
    latency_seconds: float
    sources: List[str] = []
    model: str

# root endpoint
@app.get("/")
def home():
    return {
        "message": "Groq AI FastAPI Backend is running",
        "student": "Parth Dadhaniya",
        "docs": "/docs",
        "health": "/health"
    }

# health check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": config.DEFAULT_MODEL,
        "groq_api_configured": bool(config.GROQ_API_KEY)
    }

# chat endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    start = time.time()
    try:
        if request.use_rag:
            rag_output = groq_rag_pipeline(request.query)
            ans = rag_output["answer"]
            sources = rag_output["sources"]
        else:
            ans = groq_chat(request.query)
            sources = []

        elapsed = round(time.time() - start, 3)
        return {
            "query": request.query,
            "answer": ans,
            "latency_seconds": elapsed,
            "sources": sources,
            "model": config.DEFAULT_MODEL
        }
    except Exception as e:
        logger.error(f"Error handling request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
