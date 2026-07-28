# Local-RAG-Hybrid-AI-Chatbot
# 🤖 Hybrid AI Tutor Chatbot

A **Local AI Tutor Chatbot** built using **Retrieval-Augmented Generation (RAG)**, **Hybrid Search**, and a **Multi-Agent AI Pipeline**.

The chatbot can answer questions from uploaded PDF documents as well as general knowledge using web search when required. It runs completely on local models using **Ollama**, making it privacy-friendly and cost-effective.

---

# 🚀 Features

- 📄 PDF-based Question Answering
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Hybrid Search (FAISS + BM25)
- 🌐 Automatic Web Search Fallback
- 🤖 Multi-Agent AI Pipeline
- 📝 Conversation Memory
- ⚡ Local LLMs using Ollama
- 🎯 Cross-Encoder Reranking
- 📊 Multiple Chunking Strategies
- 🌍 FastAPI REST API

---

# 🛠 Tech Stack

- Python
- Ollama
- Llama3
- Qwen2.5
- nomic-embed-text
- FAISS
- BM25
- FastAPI
- pdfplumber
- DuckDuckGo Search
- Sentence Transformers

---

# 📂 Project Structure

```
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
│   ├── chunker.py
│   ├── embedder.py
│   ├── pipeline.py
│   └── vector_store.py
│
├── retrieval/
│   ├── bm25.py
│   ├── confidence.py
│   ├── hybrid.py
│   └── reranker.py
│
├── memory/
│
├── prompts/
│
├── harness/
│
├── utils/
│
├── app.py
└── config.py
```

---

# ⚙️ Pipeline

```
PDF
   │
   ▼
Load PDF
   │
   ▼
Clean Text
   │
   ▼
Chunking
   │
   ▼
Embeddings
   │
   ▼
FAISS Vector Store
   │
   ▼
User Question
   │
   ▼
Planner Agent
   │
   ▼
Retriever Agent
   │
   ├────────► FAISS
   │
   ├────────► BM25
   │
   └────────► Web Search (if needed)
   │
   ▼
Reranker
   │
   ▼
Answer Generator
   │
   ▼
Critic Agent
   │
   ▼
Final Response
```

---

# 🧩 Chunking Strategies

- Fixed Chunking
- Recursive Chunking
- Semantic Chunking

The project also evaluates chunk statistics such as:

- Number of chunks
- Average chunk size
- Total characters

---

# 🔍 Retrieval Pipeline

The chatbot combines multiple retrieval techniques:

- Dense Retrieval using FAISS
- Sparse Retrieval using BM25
- Hybrid Retrieval
- Cross-Encoder Reranking
- Confidence-Based Web Fallback

---

# 🤖 Multi-Agent Architecture

The chatbot follows a multi-agent workflow:

### Planner Agent
Determines how the question should be answered.

### Retriever Agent
Retrieves relevant information from the knowledge base and the web.

### Answer Agent
Generates the final response using the retrieved context.

### Critic Agent
Reviews the generated answer for quality before returning it.

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/health` | Health check |
| `/chat` | Chat with the AI |
| `/chat/internet` | Internet-only chat |
| `/web/search` | Raw web search results |

---

# 📚 Concepts Implemented

- Retrieval-Augmented Generation (RAG)
- Hybrid Search
- Dense Retrieval
- Sparse Retrieval
- BM25
- FAISS Vector Search
- Sentence Embeddings
- Cross-Encoder Reranking
- Prompt Engineering
- Multi-Agent Systems
- Confidence-Based Retrieval
- Web Search Integration
- Conversation Memory
- FastAPI REST API

---

# ▶️ Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Run the chatbot

```bash
python app.py
```

Run the API

```bash
uvicorn api.api:app --reload
```

---

# 📈 Future Improvements

- Streaming Responses
- Qdrant Vector Database
- Multi-PDF Support
- Citation Support
- Authentication
- Docker Deployment
- Web Interface

---

# 👩‍💻 Author

**Sakshi Garg**

B.Tech – Electronics & Communication Engineering

Interested in:

- Artificial Intelligence
- Machine Learning
- Generative AI
- Retrieval-Augmented Generation (RAG)
- Multi-Agent Systems

---

⭐ If you found this project useful, consider giving it a star!
