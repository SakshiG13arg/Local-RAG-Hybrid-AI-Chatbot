from fastapi import FastAPI
from pydantic import BaseModel

from harness.pipeline import run_pipeline
from utils.web_search import search_web

app = FastAPI(
    title="Hybrid AI Tutor Chatbot",
    version="1.0.0"
)


# ----------------------------
# Request Models
# ----------------------------

class ChatRequest(BaseModel):
    question: str
    search_mode: str = "auto"
    mode: str = "multi_agent"


class WebSearchRequest(BaseModel):
    question: str
    max_results: int = 5


# ----------------------------
# Health Endpoint
# ----------------------------

@app.get("/health")
def health():

    return {
        "status": "ok",
        "service": "Hybrid AI Tutor Chatbot",
        "version": "1.0.0"
    }


# ----------------------------
# Chat Endpoint
# ----------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    state = run_pipeline(
        question=request.question,
        history=[],
        index=None,
        chunks=None,
        bm25=None,
        search_mode=request.search_mode,
        mode=request.mode
    )

    return {
        "answer": state.answer,
        "plan": state.plan,
        "review": state.review,
        "used_web": state.used_web,
        "search_mode": state.search_mode,
        "mode": state.mode,
        "tool_trace": state.logs,
        "iterations": state.iteration,
        "finished": not state.review.upper().startswith("SORRY"),
        "sources": state.sources if hasattr(state, "sources") else [],
        "errors": state.errors if hasattr(state, "errors") else []
    }


# ----------------------------
# Internet Only Chat
# ----------------------------

@app.post("/chat/internet")
def internet_chat(request: ChatRequest):

    state = run_pipeline(
        question=request.question,
        history=[],
        index=None,
        chunks=None,
        bm25=None,
        search_mode="internet_only",
        mode=request.mode
    )

    return {
        "answer": state.answer,
        "mode": request.mode,
        "search_mode": "internet_only",
        "tool_trace": state.logs
    }


# ----------------------------
# Web Search Endpoint
# ----------------------------

@app.post("/web/search")
def web_search_endpoint(request: WebSearchRequest):

    results = search_web(
        request.question,
        request.max_results
    )

    return {
        "query": request.question,
        "count": len(results),
        "results": results
    }