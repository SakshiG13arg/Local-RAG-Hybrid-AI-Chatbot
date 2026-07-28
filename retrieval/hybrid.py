from utils.embeddings import get_embedding
from config import (
    TOP_K,
    SIMILARITY_THRESHOLD
)
from retrieval.confidence import is_confident
from retrieval.bm25 import bm25_search
import numpy as np
from utils.web_search import search_web
from retrieval.reranker import rerank
def hybrid_search(
    question,
    index,
    chunks,
    bm25
):
    retrieved_chunks = []
    context = ""
    web_context = ""
    use_web = False
    """
    Searches PDF using:
    - FAISS
    - BM25
    - Reranking

    Returns:
        context
        confidence
    """

    if index is not None and chunks is not None:

        question_embedding = np.array(
        [get_embedding(question)],
        dtype="float32"
    )

        distances, indices = index.search(
        question_embedding,
        k=TOP_K
    )

        faiss_distances = distances[0]

    print("\n========== FAISS RESULTS ==========")

    for distance, idx in zip(
                distances[0],
                indices[0]
            ):

        print(
                    f"Chunk: {idx} | Distance: {distance:.4f}"
                )

        if (
                    idx != -1
                    and distance < SIMILARITY_THRESHOLD
                ):

                    retrieved_chunks.append(
                        chunks[idx]
                    )

        print("===================================\n")

            # ------------------------
            # Confidence Check
            # ------------------------

    if not is_confident(
                faiss_distances,
                SIMILARITY_THRESHOLD
            ):

                use_web = True

        # ------------------------------------
        # BM25 Retrieval
        # ------------------------------------

    if bm25 is not None and chunks is not None:

        print("\n========== BM25 RESULTS ==========\n")

        keyword_chunks = bm25_search(
                bm25,
                chunks,
                question,
                top_k=TOP_K
            )

        retrieved_chunks.extend(
                keyword_chunks
            )

        print(
                f"Retrieved {len(keyword_chunks)} keyword chunks."
            )

        print("\n=================================\n")

        if use_web:

                print("\nSearching Web...\n")

                results = search_web(question)

                for result in results:

                    web_context += (
                        f"Title: {result['title']}\n"
                    )

                    web_context += (
                        f"{result['body']}\n\n"
                    )
        print("\n========== WEB FALLBACK ==========")

        if use_web:
                print("Using Web Search")
        else:
                print("Using PDF Knowledge Base")

        print("=================================\n")
        # ------------------------------------
        # Remove Duplicate Chunks
        # ------------------------------------

        retrieved_chunks = list(
            dict.fromkeys(
                retrieved_chunks
            )
        )

        # ------------------------------------
        # Reranking
        # ------------------------------------

        if len(retrieved_chunks) > 1:

            retrieved_chunks = rerank(
                question,
                retrieved_chunks
            )

        # ------------------------------------
        # Keep Best 3
        # ------------------------------------

        retrieved_chunks = retrieved_chunks[:3]

        print("\n========== FINAL CHUNKS ==========\n")

        for i, chunk in enumerate(
            retrieved_chunks
        ):

            print(f"Chunk {i+1}")
            print("-" * 30)
            print(chunk[:200])
            print()

        print("==================================\n")

        # ------------------------------------
        # Build Context
        # ------------------------------------

        context = "\n\n".join(retrieved_chunks)

    if web_context:

        context += "\n\nWeb Information:\n"
        context += web_context

    return context, use_web
