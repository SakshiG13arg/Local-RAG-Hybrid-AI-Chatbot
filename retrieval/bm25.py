from rank_bm25 import BM25Okapi


def build_bm25(chunks):
    """
    Builds a BM25 index from document chunks.
    """

    tokenized_chunks = [
        chunk.split()
        for chunk in chunks
    ]

    return BM25Okapi(tokenized_chunks)


def bm25_search(
    bm25,
    chunks,
    query,
    top_k=3
):
    """
    Returns the top matching chunks using BM25.
    """

    tokenized_query = query.split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        zip(scores, chunks),
        reverse=True
    )

    return [
        chunk
        for _, chunk in ranked[:top_k]
    ]
