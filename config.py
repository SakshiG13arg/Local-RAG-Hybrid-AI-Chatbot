# ---------------- Chunking ----------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

CHUNKING_STRATEGIES = {
    "small": (300, 50),
    "medium": (500, 100),
    "large": (700, 150),
}

DEFAULT_CHUNKING = "medium"


# ---------------- Retrieval ----------------

TOP_K = 5

SIMILARITY_THRESHOLD = 1.0


# ---------------- Reranking ----------------

RERANKING_STRATEGY = "cross_encoder"


# ---------------- Models ----------------

DEFAULT_MODEL = "qwen2.5:3b"

PLANNER_MODEL = "qwen2.5:3b"

ANSWER_MODEL = "llama3"

CRITIC_MODEL = "llama3"

EMBEDDING_MODEL = "nomic-embed-text"


AVAILABLE_MODELS = [
    "qwen2.5:3b",
    "llama3"
]


# ---------------- Agent ----------------

MAX_AGENT_LOOPS = 3

# ---------------- Search Mode ----------------

DEFAULT_SEARCH_MODE = "auto"

SEARCH_MODES = [
    "auto",
    "rag",
    "rag_plus_web",
    "internet_only"
]

# ---------------- Agent Mode ----------------

DEFAULT_AGENT_MODE = "multi_agent"

AGENT_MODES = [
    "legacy",
    "multi_agent"
]

CHUNKING_METHODS = [
    "fixed",
    "recursive",
    "semantic"
]


TOP_K = 3


EVAL_QUESTIONS = [
    {
        "question": "What is RAG?",
        "expected_keyword": "retrieval"
    },
    {
        "question": "What is Qdrant?",
        "expected_keyword": "vector"
    }
]
