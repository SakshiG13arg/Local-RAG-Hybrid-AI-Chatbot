def evaluate_retrieval(
    questions,
    retriever,
    top_k=3
):
    """
    Evaluates retrieval quality using hit-rate.

    A retrieval is considered successful when
    the expected keyword appears in the top-k
    retrieved chunks.
    """

    if not questions:
        return {
            "hit_rate": 0,
            "correct": 0,
            "total": 0
        }


    hits = 0


    for item in questions:

        question = item["question"]

        expected_keyword = (
            item["expected_keyword"]
            .lower()
        )


        retrieved_chunks = retriever(
            question
        )[:top_k]


        success = any(
            expected_keyword in chunk.lower()
            for chunk in retrieved_chunks
        )


        if success:
            hits += 1



    hit_rate = (
        hits / len(questions)
    ) * 100



    return {
        "hit_rate": round(hit_rate, 2),
        "correct": hits,
        "total": len(questions)
    }
