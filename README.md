# Local-RAG-Hybrid-AI-Chatbot
Hybrid AI Tutor Chatbot

A local-first AI Tutor Chatbot built using Ollama, FAISS, Hybrid Retrieval (FAISS + BM25), Multi-Agent AI, and FastAPI. The chatbot can answer questions from PDF documents as well as the web using a modular retrieval pipeline.

Features
📄 PDF Question Answering (RAG)
🤖 Multi-Agent Architecture
Planner Agent
Retriever Agent
Answer Generator
Critic Agent
🔍 Hybrid Retrieval
Dense Search (FAISS)
Sparse Search (BM25)
📊 Cross-Encoder Reranking
🌐 Web Search Fallback (DuckDuckGo)
🧠 Conversation Memory
⚙ Multiple Chunking Strategies
Fixed Chunking
Recursive Chunking
Semantic Chunking
🚀 FastAPI REST API
📝 Modular Prompt Templates
💻 Fully Local using Ollama (No Paid APIs)
Project Architecture
                User Question
                      │
                      ▼
              Planner Agent
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
     PDF Retrieval          Web Search
     (FAISS + BM25)       (DuckDuckGo)
          │                       │
          └───────────┬───────────┘
                      ▼
                Hybrid Context
                      │
                      ▼
              Cross Encoder
                 Reranker
                      │
                      ▼
             Answer Generator
                      │
                      ▼
               Critic Agent
                      │
          Good? ──────┴────── No
             │                │
             ▼                │
      Return Answer      Next Iteration
Project Structure
AI Chatbot/
│
├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── answer.py
│   ├── critic.py
│   └── agent_loop.py
│
├── api/
│   └── api.py
│
├── chunking/
│   ├── fixed.py
│   ├── recursive.py
│   ├── semantic.py
│   └── router.py
│
├── ingestion/
│   ├── loader.py
│   ├── cleaner.py
│   ├── embedder.py
│   ├── vector_store.py
│   └── pipeline.py
│
├── retrieval/
│   ├── hybrid.py
│   ├── bm25.py
│   ├── reranker.py
│   ├── confidence.py
│   └── ...
│
├── harness/
│   ├── pipeline.py
│   ├── state.py
│   ├── budget.py
│   ├── logger.py
│   └── gates.py
│
├── memory/
├── prompts/
├── utils/
├── app.py
└── config.py
Technologies Used
Technology	Purpose
Python	Programming Language
Ollama	Local LLM Inference
Llama3	Answer Generation
Qwen2.5	Planning Agent
nomic-embed-text	Text Embeddings
FAISS	Dense Vector Search
BM25	Keyword Retrieval
Cross Encoder MiniLM	Reranking
FastAPI	REST API
pdfplumber	PDF Text Extraction
LangChain	Recursive Text Splitting
DuckDuckGo Search	Web Search
NumPy	Vector Operations
Retrieval Pipeline
Load PDF
Clean extracted text
Split text into chunks
Generate embeddings using Ollama
Store embeddings in FAISS
Perform Hybrid Search
FAISS
BM25
Rerank retrieved chunks
Check retrieval confidence
Use Web Search if confidence is low
Generate final answer
Multi-Agent Workflow
Planner Agent

Determines the retrieval strategy (PDF, Web, or both).

Retriever Agent

Fetches relevant information using Hybrid Retrieval.

Answer Agent

Generates the final response using retrieved context.

Critic Agent

Evaluates the generated answer and requests another iteration if necessary.

Chunking Strategies

The project supports multiple chunking techniques for experimentation and evaluation.

Fixed Chunking
Recursive Chunking (Default)
Semantic Chunking

Chunk size and overlap can be configured through the project configuration.

API Endpoints
Health Check
GET /health

Returns application status.

Chat
POST /chat

Generate an answer using the Hybrid Multi-Agent pipeline.

Internet Chat
POST /chat/internet

Generate answers using Internet search only.

Web Search
POST /web/search

Returns raw DuckDuckGo search results.

Installation
Clone Repository
git clone https://github.com/yourusername/hybrid-ai-chatbot.git

cd hybrid-ai-chatbot
Create Virtual Environment
python -m venv .venv

Activate

Windows

.venv\Scripts\activate

Linux/Mac

source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Install Ollama Models
ollama pull llama3

ollama pull qwen2.5:3b

ollama pull nomic-embed-text
Run the Application

CLI

python app.py

FastAPI

uvicorn api.api:app --reload

Swagger Documentation

http://127.0.0.1:8000/docs
Configuration

The following parameters can be configured in config.py.

Chunk Size
Chunk Overlap
Chunking Strategy
Retrieval Top-K
Similarity Threshold
Default Models
Future Improvements
Streaming Responses
Persistent Conversation Memory
Qdrant Integration
LangGraph-based Agent Workflow
Authentication & User Sessions
Web Interface
Docker Deployment
Learning Outcomes

This project demonstrates practical implementation of:

Retrieval-Augmented Generation (RAG)
Multi-Agent AI Systems
Hybrid Search (Dense + Sparse Retrieval)
Vector Databases
Embeddings
Prompt Engineering
Cross-Encoder Reranking
FastAPI REST APIs
Local LLM Deployment with Ollama
Modular AI System Design
License

This project is intended for educational and learning purposes. Feel free to fork, modify, and extend it for personal or academic use.
