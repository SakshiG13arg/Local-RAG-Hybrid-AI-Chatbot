import numpy as np

from chunking.router_chunking import chunk_document

from ingestion.embedder import (
    create_embeddings,
    get_embedding
)

from utils.vector_store import (
    create_vector_store
)

from retrieval.bm25 import (
    build_bm25,
    bm25_search
)

from retrieval.reranker import rerank

from config import (
    CHUNKING_METHODS,
    EVAL_QUESTIONS,
    TOP_K
)


def evaluate_chunking_strategies(text):
    """
    Evaluates different chunking strategies by running them
    through the same retrieval pipeline used during chat.

    Pipeline:

    Chunking
        |
        v
    Embeddings
        |
        v
    Dense Retrieval
        +
    BM25 Retrieval
        |
        v
    Hybrid Merge
        |
        v
    Reranking
        |
        v
    Top-K chunks

    Evaluation metric:
        Hit Rate = correct retrievals / total questions

    A retrieval is considered correct when the expected keyword
    appears inside the retrieved chunks.
    """


    print("\n========== CHUNKING EVALUATION ==========\n")


    if not EVAL_QUESTIONS:
        print(
            "No EVAL_QUESTIONS found in config.py"
        )
        return None


    report = {}


    for strategy in CHUNKING_METHODS:

        print(
            f"\nTesting strategy: {strategy}"
        )


        # 1. Create chunks

        chunks = chunk_document(
            text,
            strategy=strategy
        )


        if not chunks:
            print(
                "No chunks generated. Skipping..."
            )
            continue



        avg_chunk_size = (
            sum(len(chunk) for chunk in chunks)
            /
            len(chunks)
        )


        # 2. Create embeddings

        embeddings = create_embeddings(
            chunks
        )


        # 3. Create vector index

        index = create_vector_store(
            embeddings
        )


        # 4. Create BM25 index

        bm25 = build_bm25(
            chunks
        )


        hits = 0



        # 5. Test every evaluation question

        for item in EVAL_QUESTIONS:

            question = item["question"]

            expected_keyword = (
                item["expected_keyword"]
                .lower()
            )


            # Dense retrieval

            question_embedding = np.array(
                [
                    get_embedding(question)
                ],
                dtype="float32"
            )


            _, indices = index.search(
                question_embedding,
                k=TOP_K
            )


            dense_chunks = [
                chunks[i]
                for i in indices[0]
                if i != -1
            ]



            # Sparse retrieval

            sparse_chunks = bm25_search(
                bm25,
                chunks,
                question,
                top_k=TOP_K
            )



            # Hybrid merge

            merged_chunks = list(
                dict.fromkeys(
                    dense_chunks +
                    sparse_chunks
                )
            )



            # Reranking

            if len(merged_chunks) > 1:

                merged_chunks = rerank(
                    question,
                    merged_chunks
                )



            top_chunks = merged_chunks[:3]



            # Correct retrieval check

            if any(
                expected_keyword in chunk.lower()
                for chunk in top_chunks
            ):
                hits += 1



        hit_rate = (
            hits /
            len(EVAL_QUESTIONS)
        ) * 100



        report[strategy] = {
            "hit_rate": hit_rate,
            "hits": hits,
            "total_questions": len(EVAL_QUESTIONS),
            "chunks_created": len(chunks),
            "average_chunk_size": round(
                avg_chunk_size,
                2
            )
        }



        print(
            f"Chunks Created: {len(chunks)}"
        )

        print(
            f"Average Chunk Size: {avg_chunk_size:.2f}"
        )

        print(
            f"Hit Rate: {hit_rate:.2f}% "
            f"({hits}/{len(EVAL_QUESTIONS)})"
        )

        print(
            "-" * 45
        )



    if not report:
        return None



    best_strategy = max(
        report,
        key=lambda x: report[x]["hit_rate"]
    )


    print(
        "\n========== FINAL RESULT =========="
    )


    print(
        f"Best Strategy: {best_strategy}"
    )

    print(
        f"Best Hit Rate: "
        f"{report[best_strategy]['hit_rate']:.2f}%"
    )


    print(
        "==================================\n"
    )


    return {
        "strategies": report,
        "best_strategy": best_strategy
    }
